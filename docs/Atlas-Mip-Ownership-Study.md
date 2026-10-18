# Atlas ownership at distance: conditional risk study

The corrected bakes keep source owners isolated at bake time. Texture filtering at distance is a different question.

The checker rasterizes actual UV triangles at 1024-square texel centers, then counts simple aligned box footprints containing more than one source owner. Neither model has sampled base-level owner overlap. At mip level 4 (16-square base texels), 276 Apoco and 652 Discharge footprints contain multiple owners. This identifies a potential risk if a rendering path averages those regions.

This is not a native screenshot or proof of visible bleeding. It ignores dilated image margins, same-owner material/island boundaries and actual bilinear, trilinear or anisotropic sampling. Zero mixed footprints at levels0–3 is not a sampler safety guarantee. The tested released glass render-type constructor passes false,false texture flags; applicability must be checked per actual render route.

Do not globally disable mipmaps, reduce texel density or inflate every texture as an unmeasured fix. Before native acceptance, inspect bound sampler states and use view-distance/angle captures. If mipmapped paths need support, compare padded/repacked layouts or material/texture-page separation with equivalent detail, draw cost and memory. Per-part texture arrays are a possible custom-renderer design, not implemented compatibility.

Reproduce with Blender4.3.2: --background --python-exit-code1 --python check.py -- --source <baked blend> --model <merged study object> --out <report.json>. Input blends are in the published owner-isolation study. The checker is diagnostic; it cannot certify artistic quality or gameplay.
