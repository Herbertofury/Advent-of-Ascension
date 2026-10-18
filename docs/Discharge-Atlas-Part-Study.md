# Discharge v11 source-to-atlas/part reconstruction study

Unaccepted authoring/export study using the corrected Discharge v7 source. This is not a playable TaCZ pack, final texture art or native animation integration.

## What this pipeline fixes

- Raw Base Color and Emission Color are baked through unit emission from the untouched source objects. This avoids changing Generated coordinates and avoids treating the diffuse BSDF contribution as raw metallic albedo.
- Emission intensity remains a separate material property in the Blender reconstruction.
- The 1024 atlas prioritizes the fine core-pattern UVs instead of raising every surface to 2048. Native memory and mip behavior still require testing.
- Explicit source-part IDs preserve ownership when rebuilding the temporary merged atlas target into separately controlled objects.
- Preflight rejects unsupported material types, collapsed triangles and inward-oriented closed solids before baking. A prior failed source was caught by this gate; its receipt is retained.

## Recorded verification

143 reconstructed parts retain 100,160 UV corners. Rest-position error and UV error are zero in the recorded test. Maximum corner-normal vector error is approximately 0.000336, below the 0.001 regression limit; normals are not claimed bit-identical. One controlled original-owner translation is reproduced with zero measured position error. This does not test complete animation clips or native bone mapping.

The matched-camera comparison uses 64 samples, seed 17, adaptive sampling off and denoising off. Mean absolute 8-bit RGB differences over the weapon bounding region are approximately 0.605/0.362/0.338; the more sensitive core region is 4.388/1.892/1.688. Exact image hashes, crop regions and results are in matched-comparison.json. These metrics are diagnostics, not artistic acceptance or proof of identical pixels.

## Reproduce

Use Blender 4.3.2. Place the corrected discharge-sculpt-v7/ source folder beside this folder. Run bake.py with --python-exit-code 1, then render_comparison.py, then Python measure_comparison.py (Pillow required), and run check_parts.py through Blender. The packed blend and images can be inspected independently.

The older v1–v10 studies remain local diagnostic history. They are not accepted release assets. The current source model is still below the owner's chosen concept; native rendering, transparency/material channels, hands, animations, effects, mip/seam quality, gameplay and performance remain open.
