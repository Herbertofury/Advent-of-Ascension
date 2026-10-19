# Discharge grip and surface study

Original project authoring work. These models remain below the preserved owner concept and are not playable TaCZ weapons.

## Inspect

Open `discharge-surface-detail-v22/discharge-surface-detail.blend` in Blender 4.3.2. The latest scene includes the v21 grip and v22 seated upper-armor traces. All surfaces are procedural; no external image files are required.

## Rebuild

From the extracted archive directory:

1. Run Blender background mode with `--python discharge-grip-study-v21/build.py`.
2. Run `--python discharge-grip-study-v21/check_geometry.py` and `--python discharge-grip-study-v21/check_fit.py`.
3. Run `--python discharge-surface-detail-v22/build.py` and its `check_geometry.py`.

Use `--python-exit-code 1` so a failed assertion returns failure. The archive includes the original authored v19 input checkpoint for these rebuilds. It does not claim to recreate the entire historical model from an empty scene.

## What changed

- Three shallow finger contours within the existing grip envelope.
- Matte, patterned grip panels; a small original branching crest replaces the rejected oversized lightning emblem.
- Edge trim is seated into the panel instead of hovering above it.
- Eight fine ornamental paths follow evaluated upper armor surfaces. These are high-resolution authoring details intended for later bake/LOD work, not a native rendering budget.

## Checked boundaries

V21: 70,228 evaluated triangles, zero degenerate triangles. The trigger and guard exactly match the v19 evaluated static geometry. Twenty-one new visible parts have no static triangle-surface intersections with the trigger.

V22: 74,132 evaluated triangles, zero degenerate triangles. Surface projection found the specified target armor at every sampled point. This is placement evidence, not a complete collision, containment or native shading test.

Still required: significant concept-fidelity sculpting, less slab-like receiver transitions, comfortable native hands, swept animation clearances, export/material conversion, game integration, full weapon features and measured performance. Earlier export and recoil evidence does not automatically transfer to these new scenes.

Original AoA identity remains credited to Tslat and contributors. No original game code or concept artwork is included in this source archive.

## Current v36: grip contours below the guard return

![Revised grip authoring close-up](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-grip-closeup-v36.png)

[Matched before view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-grip-before-v36.png) · [Whole-weapon authoring view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-grip-hero-v36.png) · [Editable source and rebuild](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/discharge-grip-v36-study.zip) · [Scoped QA](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-grip-v36-qa.json).

This refinement places the three finger contours below the existing guard return and improves the patterned inlays, fitted edging and small branching crest. An earlier trial left the return floating at a contour; it was rejected. The published revision retains the original trigger and guard instead of shrinking either to conceal a collision.

The rebuild starts from the bundled authored v34 scene. It preserves 292 earlier mesh/curve objects’ geometry and transforms, hiding superseded surfaces. The new grip is a closed positive-volume 4,700-triangle authoring mesh with zero degenerate triangles. A point-in-mesh test confirms the guard’s return endpoint sits inside the grip. A clean package rebuild reproduced those reported checks.

**This is limited static authoring QA.** The single-point seating test does not prove full guard containment, hand fit, moving clearance or native performance. The full concept still calls for more sculpted, integrated detailing, and the current model remains below that target.

The v35 mapped textures, grouped GLB and animation transport remain a separate export study. They have not been regenerated for this v36 geometry. Do not combine their acceptance evidence or label this archive a playable gunpack.
