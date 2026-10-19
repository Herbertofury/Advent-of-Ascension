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
