/* Original documentation renderer. Static source meshes; no Minecraft code execution.
   Embedded identically in the generated viewers to avoid another startup request. */
function viewDepth(point, model, view) {
  const yaw = view.yaw * Math.PI / 180, pitch = view.pitch * Math.PI / 180;
  const q = point.map((value, i) => value - model.center[i]);
  const z = -Math.sin(yaw) * q[0] + Math.cos(yaw) * q[2];
  return Math.sin(pitch) * q[1] + Math.cos(pitch) * z;
}
function projectedPoint(point, model, view, width, height) {
  const yaw = view.yaw * Math.PI / 180, pitch = view.pitch * Math.PI / 180;
  const q = point.map((value, i) => (value - model.center[i]) / model.radius);
  const x = Math.cos(yaw) * q[0] + Math.sin(yaw) * q[2];
  const z = -Math.sin(yaw) * q[0] + Math.cos(yaw) * q[2];
  const y = Math.cos(pitch) * q[1] - Math.sin(pitch) * z;
  const scale = .85 * view.zoom * Math.min(width, height) / 2;
  return [width / 2 + x * scale, height / 2 - y * scale];
}
function textureTransform(uv, xy) {
  const [a, b, c] = uv, [p, q, r] = xy;
  const denominator = a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]);
  if (Math.abs(denominator) < 1e-10) return null;
  const solve = k => [
    (p[k] * (b[1] - c[1]) + q[k] * (c[1] - a[1]) + r[k] * (a[1] - b[1])) / denominator,
    (p[k] * (c[0] - b[0]) + q[k] * (a[0] - c[0]) + r[k] * (b[0] - a[0])) / denominator,
    (p[k] * (b[0] * c[1] - c[0] * b[1]) + q[k] * (c[0] * a[1] - a[0] * c[1]) + r[k] * (a[0] * b[1] - b[0] * a[1])) / denominator
  ];
  const x = solve(0), y = solve(1);
  return [x[0], y[0], x[1], y[1], x[2], y[2]];
}
function createCanvasRenderer(canvas) {
  const context = canvas.getContext('2d');
  if (!context) return null;
  const imagePromises = new Map(), CACHE_LIMIT = 128;
  function image(id, source) {
    if (imagePromises.has(id)) {
      const cached = imagePromises.get(id);
      imagePromises.delete(id);
      imagePromises.set(id, cached);
      return cached;
    }
    const promise = new Promise((resolve, reject) => {
      const element = new Image();
      element.onload = () => resolve(element);
      element.onerror = () => reject(Error('Source texture could not decode'));
      element.src = source[id].data_url;
    });
    imagePromises.set(id, promise);
    while (imagePromises.size > CACHE_LIMIT) imagePromises.delete(imagePromises.keys().next().value);
    // An older failed request must not remove a newer promise for the same texture.
    promise.catch(() => { if (imagePromises.get(id) === promise) imagePromises.delete(id); });
    return promise;
  }
  async function prepare(model) {
    const textureIds = [...new Set(model.faces.map(face => face.texture))];
    const readyImages = new Map(await Promise.all(textureIds.map(async id => [id, await image(id, model.textures)])));
    // Source geometry is immutable within a loaded reference. Cache its constant work.
    if (!model.canvasFaces) {
      model.canvasFaces = model.faces.map(face => {
        const texture = model.textures[face.texture];
        return {
          vertices: face.vertices,
          texture: face.texture,
          center: [0, 1, 2].map(i => face.vertices.reduce((sum, point) => sum + point[i], 0) / 4),
          uvPixels: face.uv.map(uv => [uv[0] * texture.width, uv[1] * texture.height])
        };
      });
    }
    model.readyImages = readyImages;
  }
  function draw(model, view) {
    if (!model.readyImages || !model.canvasFaces) return;
    const rect = canvas.getBoundingClientRect(), density = Math.min(2, window.devicePixelRatio || 1);
    const width = Math.max(1, Math.min(2048, Math.round(rect.width * density)));
    const height = Math.max(1, Math.min(2048, Math.round(rect.height * density)));
    if (canvas.width !== width || canvas.height !== height) { canvas.width = width; canvas.height = height; }
    context.clearRect(0, 0, width, height);
    context.imageSmoothingEnabled = false;
    const sortedFaces = model.canvasFaces.map(face => ({face, depth: viewDepth(face.center, model, view)})).sort((a, b) => a.depth - b.depth);
    for (const {face} of sortedFaces) {
      const element = model.readyImages.get(face.texture);
      const points = face.vertices.map(point => projectedPoint(point, model, view, width, height));
      for (const indices of [[0, 1, 2], [0, 2, 3]]) {
        const xy = indices.map(i => points[i]), uv = indices.map(i => face.uvPixels[i]);
        const matrix = textureTransform(uv, xy);
        if (!matrix) continue;
        context.save();
        try {
          context.beginPath(); context.moveTo(...xy[0]); context.lineTo(...xy[1]); context.lineTo(...xy[2]);
          context.closePath(); context.clip(); context.transform(...matrix); context.drawImage(element, 0, 0);
        } finally { context.restore(); }
      }
    }
  }
  return {
    prepare, draw,
    label: 'Interactive canvas 3D ready',
    note: 'Software preview uses approximate face ordering; intersecting or translucent surfaces can differ from game rendering.',
    clear() { context.clearRect(0, 0, canvas.width, canvas.height); }
  };
}
