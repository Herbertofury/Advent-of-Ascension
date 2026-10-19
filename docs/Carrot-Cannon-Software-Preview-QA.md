# Carrot Cannon software preview investigation

The browser has no WebGL context here. Its fallback is a reduced-detail authoring viewer, not a native renderer or a playable weapon.

## Rejected intermediate results

1. The 6,111-triangle global simplification showed gray triangular patches across the orange body.
2. Reducing each part independently preserved every material region (15,443 triangles, 12 parts retained at full detail). The deployed screenshot still showed occlusion artifacts around curved collars. Material-region validation alone was insufficient.
3. The old painter algorithm sorted complete triangles by their average depth. Long triangles on curved/crossing surfaces cannot be reliably ordered that way.

## Current correction

The software path now interpolates per-pixel normalized depth into a depth buffer. It retains simple centroid texture colors and simplified lighting. Equal-depth surfaces keep the first writer; this does not repair coplanar or overlapping authoring geometry. No antialiasing, transparency, native material or hand-fit claim is made.

Eight depth-raster fixtures cover crossing surfaces in both draw orders, known front/back pixels, clipping, winding, degenerate triangles and equal-depth policy. Existing 4,138 model/math checks and 12 simulated UI scenarios pass. Live cloud-Chrome screenshot on 2026-10-19 verified the curved-collar occlusion patches are removed. Recoil finished at 0.800 s and returned to idle; reset restored 0.000 s; disabled motion blocked playback; slider, keyboard orbit and zoom controls changed the preview. This checks the software path only; WebGL and native gameplay remain untested.

Original full authoring geometry and prior files remain preserved. Reducing geometry does not establish equivalent appearance or native performance.
