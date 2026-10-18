# Soul Storm: editable sculpt and motion study

**New authoring reconstruction · visual acceptance open · not a native TaCZ gunpack.**

![Current v9 Blender render](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v9-preview.png)

[Play the sampled four-emitter motion](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v9-motion.webp) · [Download editable sources, Blender files and retained v5–v9 iterations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-reconstruction-v5-v9.zip)

## What is built

The new mesh has the circular spirit reservoir, indigo/silver/cyan palette, four hollow emitter slots, separately animated top-to-bottom recoil, flying soul-disc authoring cues and a Soul Flame sight. The main flame has a fixed-root shape-key animation. These are actual modeled/rendered objects, not a generated image presented as a working gun.

Five iterations are retained in one archive. The wire-like core, broad cloud disk and pinwheel-like spiral were visually weak; later iterations add thinner core filaments, tapered armor, wrapped grip ribs and side flame tongues. These files are newly authored after the workspace reset, not recovered copies of the unavailable older sculpt drafts.

## Reproduce and inspect

Open the selected `.blend`, or regenerate with Blender 4.3.2:

```sh
blender -b -t 4 --python build.py
blender -b -t 4 --python check.py
blender -b -t 4 --python render_motion.py
```

The check and motion scripts are provided for v9. The web animation samples fifteen Blender frames across half a second; it is an authoring preview, not gameplay footage or an approved rate-of-fire change.

The bounded QA sampled 121 times with no nonfinite emitter transforms, recoil-range violations or simultaneous recoil events. It found no zero-area polygons or duplicate-position vertices in the visible current mesh, and verified that the main flame's shape-key root stays fixed. The duplicated flame pole vertices found during the earlier iteration were welded before these checks. [Scoped geometry receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v9-qa.json).

## Quality gates still open

- More sculpted ornamental detail and purposeful texture painting to approach the approved concept.
- Greater apparent depth and richness in the spirit reservoir; current procedural effects remain a study.
- Real hands, grip clearance, aim alignment, inspection choreography and cancellation.
- All barrel/sight/skin variants and their motion clearances.
- A verified native export/bake/rendering path. Standard TaCZ cube JSON does not automatically consume this Blender mesh, material graph or shape keys.
- Actual projectile behavior, resources, damage, multiplayer, save migration, shader/Vulkan compatibility and measured frame times.

Passing the bounded authoring checks does not close these gates. Original AoA identity and credits remain with Tslat and contributors.

[Original behavior and upgrade direction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile) · [Default Soul Flame and optional sights](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Sights)

Source archive SHA-256: `c5e119c64ca689aee32835e24679f8e4015b257e83e51db91fc0326c81c9a2a2`.
