/* Original authoring viewer. No Minecraft, TaCZ or gameplay execution. */
'use strict';
const ArmoryPreview = (() => {
  const identity = () => [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1];
  function multiply(a, b) {
    const out = new Array(16).fill(0);
    for (let col = 0; col < 4; col++) for (let row = 0; row < 4; row++)
      for (let k = 0; k < 4; k++) out[col*4+row] += a[k*4+row] * b[col*4+k];
    return out;
  }
  function translation(v) { const m = identity(); m[12]=v[0]; m[13]=v[1]; m[14]=v[2]; return m; }
  function rotationX(degrees) {
    const a=degrees*Math.PI/180, c=Math.cos(a), s=Math.sin(a);
    return [1,0,0,0, 0,c,s,0, 0,-s,c,0, 0,0,0,1];
  }
  function point(m, p) { return [0,1,2].map(r => m[r]*p[0]+m[4+r]*p[1]+m[8+r]*p[2]+m[12+r]); }
  function sample(keys, time) {
    if (!keys?.length) return [0,0,0];
    if (time <= keys[0][0]) return keys[0][1];
    let lo=0, hi=keys.length-1;
    while (lo+1<hi) { const mid=(lo+hi)>>1; if(keys[mid][0]<=time) lo=mid; else hi=mid; }
    if (time>=keys[hi][0]) return keys[hi][1];
    const f=(time-keys[lo][0])/(keys[hi][0]-keys[lo][0]);
    return keys[lo][1].map((v,i)=>v+(keys[hi][1][i]-v)*f);
  }
  function compile(geometry, animations) {
    const g=geometry['minecraft:geometry']?.[0];
    if (!g || !Array.isArray(g.bones) || g.bones.length>64) throw Error('Invalid geometry hierarchy');
    const bones=new Map(), meshes=[]; let triangles=0;
    for(const b of g.bones) {
      if(typeof b.name!=='string'||bones.has(b.name)) throw Error('Duplicate or missing bone');
      if(!Array.isArray(b.pivot)||b.pivot.length!==3||b.pivot.some(x=>!Number.isFinite(x))) throw Error('Invalid pivot');
      if((b.rotation&&b.rotation.some(x=>x!==0))||(b.scale&&b.scale.some(x=>x!==1)))throw Error('Unsupported static bone transform');
      bones.set(b.name,b);
    }
    for(const b of bones.values()) {
      let p=b; const seen=new Set();
      while(p) { if(seen.has(p.name))throw Error('Bone cycle');seen.add(p.name);if(p.parent&&!bones.has(p.parent))throw Error('Missing parent');p=bones.get(p.parent); }
      const m=b.poly_mesh; if(!m)continue;
      if(m.normalized_uvs!==true||!Array.isArray(m.polys)||m.polys.length>200000)throw Error('Unsupported mesh');
      const data=[];
      for(const polygon of m.polys) {
        if(polygon.length!==3)throw Error('Only explicit triangles supported');
        for(const corner of polygon) {
          if(corner.length!==3||corner.some(i=>!Number.isInteger(i)||i<0))throw Error('Invalid mesh index');
          const p=m.positions[corner[0]],n=m.normals[corner[1]],uv=m.uvs[corner[2]];
          if(!p||p.length!==3||!n||n.length!==3||!uv||uv.length!==2)throw Error('Missing vertex attribute');
          if([...p,...n,...uv].some(x=>!Number.isFinite(x)||!Number.isFinite(Math.fround(x)))||uv.some(x=>x<0||x>1)||Math.hypot(...n)<.5||Math.hypot(...n)>1.5)throw Error('Invalid vertex attribute');
          data.push(...p,...n,...uv);
        }
        triangles++; if(triangles>200000)throw Error('Preview triangle budget exceeded');
      }
      meshes.push({name:b.name,data:new Float32Array(data),count:data.length/8});
    }
    const raw=animations.animations?.carrot_cannon_shoot;
    if(!raw||raw.loop!==false||!Number.isFinite(raw.animation_length)||raw.animation_length<=0||raw.animation_length>5)throw Error('Invalid preview clip');
    const tracks=new Map();
    for(const [name,channels] of Object.entries(raw.bones||{})) {
      if(!bones.has(name))throw Error('Unknown animation bone');
      const parsed={};
      for(const [channel,values] of Object.entries(channels)) {
        if(!['position','rotation'].includes(channel))throw Error('Unsupported animation channel');
        const keys=Object.entries(values).map(([t,v])=>[Number(t),v]).sort((a,b)=>a[0]-b[0]);
        if(!keys.length||keys.some(([t,v],i)=>!Number.isFinite(t)||t<0||t>raw.animation_length+1e-6||!Array.isArray(v)||v.length!==3||v.some(x=>!Number.isFinite(x))||(i&&t<=keys[i-1][0])))throw Error('Invalid animation key');
        if(channel==='rotation'&&keys.some(([,v])=>v[1]!==0||v[2]!==0))throw Error('This preview supports the checked X-axis rotations only');
        parsed[channel]=keys;
      }
      tracks.set(name,parsed);
    }
    return {bones,meshes,tracks,triangles,duration:raw.animation_length};
  }
  function pose(model,time) {
    if(!Number.isFinite(time))throw Error('Invalid time');
    const result=new Map();
    function visit(b) {
      if(result.has(b.name))return result.get(b.name);
      const t=model.tracks.get(b.name)||{},p=b.pivot;
      const local=multiply(translation(sample(t.position,time)),multiply(translation(p),multiply(rotationX(sample(t.rotation,time)[0]),translation(p.map(x=>-x)))));
      const value=b.parent?multiply(visit(model.bones.get(b.parent)),local):local;
      result.set(b.name,value);return value;
    }
    for(const b of model.bones.values())visit(b);
    return result;
  }
  function perspective(aspect) {
    const f=1/Math.tan(40*Math.PI/360),near=.1,far=200;
    return [f/aspect,0,0,0,0,f,0,0,0,0,(far+near)/(near-far),-1,0,0,2*far*near/(near-far),0];
  }
  function lookAt(eye,target) {
    const norm=v=>{const n=Math.hypot(...v);return v.map(x=>x/n);};
    const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
    const z=norm(eye.map((v,i)=>v-target[i])),x=norm(cross([0,1,0],z)),y=cross(z,x),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
    return [x[0],y[0],z[0],0,x[1],y[1],z[1],0,x[2],y[2],z[2],0,-dot(x,eye),-dot(y,eye),-dot(z,eye),1];
  }
  return {identity,multiply,translation,rotationX,point,sample,compile,pose,perspective,lookAt};
})();
if(typeof module!=='undefined')module.exports=ArmoryPreview;
if(typeof document!=='undefined') (async function boot() {
  const canvas=document.getElementById('viewer'),status=document.getElementById('status'),fallback=document.getElementById('fallback');
  const buttons=[...document.querySelectorAll('[data-ready]')],timeline=document.getElementById('timeline'),motion=document.getElementById('motion');
  motion.checked=!matchMedia('(prefers-reduced-motion: reduce)').matches;
  let model,image,gl,program,drawables,texture,uniforms,attributes,context2d,softwareFaces,software=false,lost=false,raf=0,start=null,time=0,lastSoftwareFrame=0;
  let yaw=2.13,pitch=.28,distance=23,center=[0,4,0],drag=null;
  const setStatus=text=>{status.textContent=text;};
  function shader(type,source) {
    const s=gl.createShader(type);gl.shaderSource(s,source);gl.compileShader(s);
    if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))throw Error('Preview shader failed');return s;
  }
  function setupSoftware() {
    context2d=canvas.getContext('2d');if(!context2d)throw Error('Neither 3D nor software canvas is available');
    const scratch=document.createElement('canvas');scratch.width=image.width;scratch.height=image.height;
    const pixelsContext=scratch.getContext('2d');pixelsContext.drawImage(image,0,0);
    const pixels=pixelsContext.getImageData(0,0,image.width,image.height).data;
    softwareFaces=[];
    for(const mesh of model.meshes) for(let i=0;i<mesh.data.length;i+=24) {
      const d=mesh.data,positions=[],normal=[0,0,0];let u=0,v=0;
      for(let k=0;k<3;k++){const p=i+k*8;positions.push(d[p],d[p+1],d[p+2]);for(let j=0;j<3;j++)normal[j]+=d[p+3+j];u+=d[p+6]/3;v+=d[p+7]/3;}
      const length=Math.hypot(...normal);for(let j=0;j<3;j++)normal[j]/=length||1;
      const x=Math.max(0,Math.min(image.width-1,Math.floor(u*image.width))),y=Math.max(0,Math.min(image.height-1,Math.floor((1-v)*image.height))),p=(y*image.width+x)*4;
      softwareFaces.push({bone:mesh.name,positions,normal,color:[0,1,2].map(j=>Math.pow(pixels[p+j]/255,2.2)),screen:new Float32Array(6),glow:mesh.name.endsWith('_illuminated')});
    }
    fallback.hidden=true;canvas.hidden=false;lost=false;buttons.forEach(b=>b.disabled=false);
    setStatus(`${model.triangles.toLocaleString()} triangles · reduced-detail software preview ready`);draw();
  }
  function drawSoftware(vp,poses,w,h) {
    const visible=[],light=[.4682929,.7492686,-.5619515];
    for(const face of softwareFaces) {
      const m=poses.get(face.bone),p=face.positions;let depth=0,valid=true;
      for(let k=0;k<3;k++) {
        const i=k*3,x=m[0]*p[i]+m[4]*p[i+1]+m[8]*p[i+2]+m[12],y=m[1]*p[i]+m[5]*p[i+1]+m[9]*p[i+2]+m[13],z=m[2]*p[i]+m[6]*p[i+1]+m[10]*p[i+2]+m[14];
        const cw=vp[3]*x+vp[7]*y+vp[11]*z+vp[15];if(cw<=.01){valid=false;break;}
        face.screen[k*2]=((vp[0]*x+vp[4]*y+vp[8]*z+vp[12])/cw*.5+.5)*w;
        face.screen[k*2+1]=(.5-(vp[1]*x+vp[5]*y+vp[9]*z+vp[13])/cw*.5)*h;
        depth+=(vp[2]*x+vp[6]*y+vp[10]*z+vp[14])/cw;
      }
      const q=face.screen;if(!valid||(q[2]-q[0])*(q[5]-q[1])-(q[3]-q[1])*(q[4]-q[0])>=0)continue;
      const n=face.normal,nx=m[0]*n[0]+m[4]*n[1]+m[8]*n[2],ny=m[1]*n[0]+m[5]*n[1]+m[9]*n[2],nz=m[2]*n[0]+m[6]*n[1]+m[10]*n[2];
      const amount=face.glow?1:.35+.65*Math.max(0,nx*light[0]+ny*light[1]+nz*light[2]);
      face.fill='rgb('+face.color.map(c=>Math.round(255*Math.pow(c*amount,1/2.2))).join(',')+')';face.depth=depth;visible.push(face);
    }
    visible.sort((a,b)=>b.depth-a.depth);context2d.fillStyle='#091219';context2d.fillRect(0,0,w,h);context2d.lineWidth=.4;
    for(const face of visible){const q=face.screen;context2d.fillStyle=face.fill;context2d.strokeStyle=face.fill;context2d.beginPath();context2d.moveTo(q[0],q[1]);context2d.lineTo(q[2],q[3]);context2d.lineTo(q[4],q[5]);context2d.closePath();context2d.fill();context2d.stroke();}
  }
  function setupGpu() {
    gl=canvas.getContext('webgl',{alpha:false,antialias:true});if(!gl)throw Error('WebGL is unavailable');
    const vs=shader(gl.VERTEX_SHADER,'attribute vec3 p;attribute vec3 n;attribute vec2 uv;uniform mat4 model;uniform mat4 vp;varying vec3 normal;varying vec2 tex;void main(){gl_Position=vp*model*vec4(p,1.);normal=mat3(model)*n;tex=uv;}');
    const fs=shader(gl.FRAGMENT_SHADER,'precision mediump float;varying vec3 normal;varying vec2 tex;uniform sampler2D atlas;uniform float glow;void main(){vec3 c=pow(texture2D(atlas,tex).rgb,vec3(2.2));float d=max(dot(normalize(normal),normalize(vec3(.5,.8,-.6))),0.);float light=mix(.35+.65*d,1.,glow);gl_FragColor=vec4(pow(c*light,vec3(1./2.2)),1.);}');
    program=gl.createProgram();gl.attachShader(program,vs);gl.attachShader(program,fs);gl.linkProgram(program);
    if(!gl.getProgramParameter(program,gl.LINK_STATUS))throw Error('Preview program failed');
    gl.deleteShader(vs);gl.deleteShader(fs);gl.useProgram(program);
    attributes={p:gl.getAttribLocation(program,'p'),n:gl.getAttribLocation(program,'n'),uv:gl.getAttribLocation(program,'uv')};
    uniforms={model:gl.getUniformLocation(program,'model'),vp:gl.getUniformLocation(program,'vp'),glow:gl.getUniformLocation(program,'glow')};
    drawables=model.meshes.map(mesh=>{const buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,mesh.data,gl.STATIC_DRAW);return {...mesh,buffer};});
    texture=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,texture);gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL,true);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,image);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);
    gl.uniform1i(gl.getUniformLocation(program,'atlas'),0);gl.enable(gl.DEPTH_TEST);gl.enable(gl.CULL_FACE);gl.clearColor(.035,.055,.07,1);
    fallback.hidden=true;canvas.hidden=false;lost=false;setStatus(`${model.triangles.toLocaleString()} triangles · authoring preview ready`);buttons.forEach(b=>b.disabled=false);draw();
  }
  function draw(now=performance.now()) {
    raf=0;if(!model||(!gl&&!context2d)||lost||document.hidden)return;
    if(software&&start!==null&&now-lastSoftwareFrame<66){raf=requestAnimationFrame(draw);return;}lastSoftwareFrame=now;
    if(start!==null) {time=Math.min(model.duration,(now-start)/1000);if(time>=model.duration){start=null;setStatus('Authoring recoil ended; ready pose restored.');}timeline.value=time;}
    document.getElementById('clip-time').textContent=time.toFixed(3)+' s';canvas.dataset.previewState=start===null?'idle':'playing';
    const dpr=Math.min(devicePixelRatio||1,software?1.5:2),w=Math.max(1,Math.round(canvas.clientWidth*dpr)),h=Math.max(1,Math.round(canvas.clientHeight*dpr));
    if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;}if(!software){gl.viewport(0,0,w,h);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);gl.useProgram(program);}
    const eye=[center[0]+distance*Math.sin(yaw)*Math.cos(pitch),center[1]+distance*Math.sin(pitch),center[2]+distance*Math.cos(yaw)*Math.cos(pitch)];
    const vp=ArmoryPreview.multiply(ArmoryPreview.perspective(w/h),ArmoryPreview.lookAt(eye,center)),poses=ArmoryPreview.pose(model,time);
    if(software)drawSoftware(vp,poses,w,h);
    else {gl.uniformMatrix4fv(uniforms.vp,false,new Float32Array(vp));
    for(const mesh of drawables) {
      gl.bindBuffer(gl.ARRAY_BUFFER,mesh.buffer);
      for(const [name,size,offset]of [['p',3,0],['n',3,12],['uv',2,24]]){gl.enableVertexAttribArray(attributes[name]);gl.vertexAttribPointer(attributes[name],size,gl.FLOAT,false,32,offset);}
      gl.uniformMatrix4fv(uniforms.model,false,new Float32Array(poses.get(mesh.name)));gl.uniform1f(uniforms.glow,mesh.name.endsWith('_illuminated')?1:0);gl.drawArrays(gl.TRIANGLES,0,mesh.count);
    }
    }
    if(start!==null)raf=requestAnimationFrame(draw);
  }
  const requestDraw=()=>{if(!raf&&!lost)raf=requestAnimationFrame(draw);};
  function reset(){yaw=2.13;pitch=.28;distance=23;start=null;time=0;timeline.value=0;if(model)setStatus('View and authoring pose reset.');requestDraw();}
  document.getElementById('reset').addEventListener('click',reset);
  document.getElementById('recoil').addEventListener('click',()=>{if(!motion.checked){setStatus('Motion preview is off. Enable it to inspect the authored recoil.');return;}time=0;start=performance.now();setStatus('Playing an authoring recoil clip; no gameplay event');requestDraw();});
  timeline.addEventListener('input',()=>{start=null;time=Number(timeline.value);requestDraw();});
  motion.addEventListener('change',()=>{if(!motion.checked){start=null;time=0;timeline.value=0;requestDraw();}});
  document.getElementById('zoom-in').addEventListener('click',()=>{distance=Math.max(12,distance*.9);requestDraw();});
  document.getElementById('zoom-out').addEventListener('click',()=>{distance=Math.min(60,distance/ .9);requestDraw();});
  canvas.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,id:e.pointerId};canvas.setPointerCapture(e.pointerId);});
  canvas.addEventListener('pointermove',e=>{if(!drag||drag.id!==e.pointerId)return;yaw+=(e.clientX-drag.x)*.009;pitch=Math.max(-1.3,Math.min(1.3,pitch+(e.clientY-drag.y)*.009));drag.x=e.clientX;drag.y=e.clientY;requestDraw();});
  const stopDrag=()=>{drag=null;};canvas.addEventListener('pointerup',stopDrag);canvas.addEventListener('pointercancel',stopDrag);
  canvas.addEventListener('wheel',e=>{e.preventDefault();distance=Math.max(12,Math.min(60,distance*Math.exp(e.deltaY*.001)));requestDraw();},{passive:false});
  canvas.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','+','-'].includes(e.key))return;e.preventDefault();if(e.key==='ArrowLeft')yaw-=.12;if(e.key==='ArrowRight')yaw+=.12;if(e.key==='ArrowUp')pitch=Math.min(1.3,pitch+.1);if(e.key==='ArrowDown')pitch=Math.max(-1.3,pitch-.1);if(e.key==='+')distance=Math.max(12,distance*.9);if(e.key==='-')distance=Math.min(60,distance/.9);requestDraw();});
  canvas.addEventListener('webglcontextlost',e=>{e.preventDefault();lost=true;start=null;cancelAnimationFrame(raf);raf=0;buttons.forEach(b=>b.disabled=true);fallback.hidden=false;canvas.hidden=true;setStatus('3D context lost. The static authoring image is shown.');});
  canvas.addEventListener('webglcontextrestored',()=>{try{setupGpu();}catch(error){setStatus(error.message+'; showing the static image.');}});
  document.addEventListener('visibilitychange',()=>{if(document.hidden){start=null;cancelAnimationFrame(raf);raf=0;setStatus('Preview paused while hidden. Use Preview recoil to restart.');}else requestDraw();});
  new ResizeObserver(requestDraw).observe(canvas);
  try {
    gl=canvas.getContext('webgl',{alpha:false,antialias:true});software=!gl;
    const responses=await Promise.all([software?'carrot-cannon-study.software.geo.json':'carrot-cannon-study.geo.json','carrot-cannon-study.animation.json'].map(async url=>{const r=await fetch(url);if(!r.ok)throw Error('Model resource unavailable');return r.json();}));
    model=ArmoryPreview.compile(...responses);if(model.triangles!==(software?6111:49616)||model.meshes.length!==3)throw Error('Unexpected study revision');
    image=await new Promise((resolve,reject)=>{const img=new Image();img.onload=()=>resolve(img);img.onerror=()=>reject(Error('Texture unavailable'));img.src='carrot-cannon-study-basecolor.png';});if(software)setupSoftware();else setupGpu();
  } catch(error){fallback.hidden=false;canvas.hidden=true;setStatus(error.message+'. Static authoring image shown; 3D controls unavailable.');}
})();
