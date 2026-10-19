# Carrot Cannon shared-atlas and geometry transport study

**Unaccepted export study. Not a playable gunpack, finished artwork or native performance result.** The canonical concept and all outstanding gameplay/visual requirements remain unchanged.

[Interactive 3D and recoil preview](https://herbertofury.github.io/Advent-of-Ascension/carrot-cannon-preview.html) · [Editable source and transport bundle](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/carrot-cannon-texture-transport-v1.zip)

![Unaccepted shared-atlas authoring render](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-shared-atlas-v17.png)

The browser preview uses simplified lighting and linear texture filtering, loads its assets once, and renders on interaction or while the bounded clip runs. It has a static-image fallback. It does not exercise Minecraft, TaCZ, native shader materials or gameplay.

## Why the texture path changed

The first per-part smart-projection atlas blurred the orange surface and introduced black leaf seams. Giving individual material classes more weight and using fixed fractional margins still left tiny metal/glass islands visibly black. Both attempts were rejected despite passing sampled interior alpha coverage. A geometry or alpha test cannot substitute for visual comparison.

This candidate uses seven explicitly reserved material regions. Orange shell, leaves and rootwork receive large regions; constant metal, amber and bore colors use dedicated swatches. Existing GrownSurface, LeafSurface and curve UVMap coordinates are mapped into those regions. Parts remain separate and follow their original owners.

The charts cover their complete reserved borders using clamped local source coordinates. There is no overlapping dilation or reliance on unfilled chart corners. Leaf/root noise variation is deliberately sampled on a shared flat chart instead of separately on each original object. This is an art change that still needs final review, not a pixel-identical preservation claim.

## Checked evidence

- 240 retained parts; 49,616 evaluated triangles and 100,600 source loops.
- Maximum source-to-export world-position error: approximately 2.41e-7 authoring units.
- Source normal error: zero in the checked mesh reconstruction.
- UV mapping error: approximately 1.50e-8.
- 49 owner-motion poses; maximum owner-matrix error approximately 3.58e-7.
- Every pixel in the seven reserved texture regions is opaque in the checked color map.
- The geometry transport has three mesh bones and 198,464 vertices after the released TML triangle expansion. Actual pinned TML 0.1.8 baker/consumer checks pass on Java 17 and 21 with narrow graphics/logging stand-ins.
- Float32-safe JSON compaction reduces the transport from 6,123,713 to 4,872,115 bytes, approximately 20.44%, while all 1,587,712 consumed baked float values compare bit-for-bit. This is a serialization reduction, not an FPS measurement.

## Filtering limits that remain open

A software box-mip/bilinear footprint test finds the first cross-class risk at mip level 5 for the textured classes and level 8 for center-sampled constant swatches. These are diagnostics under declared sampling assumptions. They do not simulate anisotropy, trilinear transitions, compression or the actual target renderer.

Native filtering and LOD selection must keep those boundaries from becoming visible. A low-resolution distant model/material or a tested material-specific sampling path is still required. Do not label this atlas universally bleed-free.

## Native integration boundaries

The exported geometry and clip names are an integration candidate only. The native hand anchors, pivot hierarchy, culling, normals, lighting, shader behavior and animation timing still require actual gameplay tests. The released consumer's negative-normal fallback remains a separate native-lighting question.

The authoring renderer still uses bump/metal response not translated by the geometry JSON. An illuminated bone name does not reproduce the complete authoring emission shader. Gameplay registration, ammo/resources, original projectile behavior, muzzle/impact effects, sound, recipes, attachments, multiplayer and profiling are not supplied by this study.

The preserved source model is still below the concept's artistic quality, especially the uniform body segmentation and root-grip detail.

## Reproduction

Start with the published `carrot-cannon-authoring-study-v1.zip`, preserving its sibling directories. Run `carrot-cannon-shared-atlas-v17/build.py` in Blender 4.3.2, then `check.py`. Run `check_filtering.py` with Python, NumPy and Pillow.

`carrot-cannon-transport-v2/export.py` exports the candidate geometry. Its `check.py` uses the included original TML harness and float32 compactor plus separately acquired pinned TML/Gson/JOML dependencies. Upstream game classes and dependency binaries are not redistributed. Reuse the separately published released-animation parser fixture to check the unchanged clip.

Keep failed exports separate. Do not overwrite the canonical concept, increase accepted-weapon counts or treat this source bundle as a drop-in mod.
