# Soul Storm: editable sculpt and motion study

**New authoring reconstruction · visual acceptance open · not a native TaCZ gunpack.**

![Current v12 Blender authoring render](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v12-preview.png)

[Play the sampled four-emitter motion](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v9-motion.webp) · [Download editable sources, Blender files and retained v5–v9 iterations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-reconstruction-v5-v9.zip)

## Newer VFX iterations: v10–v12

![Two-second v12 authoring motion](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v12-motion.webp)

[Editable v10–v12 source archive](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-sculpt-v10-v12.zip) · [v10 procedural-core render](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v10-preview.png) · [v11 volumetric experiment](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v11-preview.png)

- v10 replaces the solid-looking sight with the existing 15-frame Soul Flame alpha atlas and tries a broader turbulent procedural core.
- v11 tries volume scattering and layered filaments. It remains visually weak and is retained as an experiment, not promoted as the preferred version.
- v12 maps a newly generated original soul-vortex VFX texture onto shallow curved, animated reservoir surfaces. This is an actual Blender mesh/material render using an editable texture, not a generated whole-weapon image presented as geometry. The default visible sight remains the Soul Flame atlas; the older solid-flame meshes are hidden history.

The [original VFX texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-core-vfx-texture-v1.png) and exact generation prompt are preserved. Its source alpha has low nonzero values at parts of the border, so final cleanup/masking is still required; it has not passed final texture/export QA. The texture improves the reservoir detail, but the body, emitter ornament and overall material quality still need substantial refinement to reach the concept.

The new motion contains thirty sampled frames over two seconds. It shows one authored four-emitter burst, a reservoir rotation and the sight cycle. It is not a native cadence, projectile or performance demonstration.

[New scoped QA receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sculpt-v12-qa.json): 121 sampled recoil positions stayed bounded and non-overlapping, visible meshes had no zero-area polygons or duplicate-position vertices, and 121 atlas samples reached exactly frames 0–14 without selecting unused cell 15. This does not certify all collisions, hands, shader passes or native rendering. Texture files are packed into the new Blender files for portability.

## Earlier v5–v9 foundation

### What was built in v9

The new mesh has the circular spirit reservoir, indigo/silver/cyan palette, four hollow emitter slots, separately animated top-to-bottom recoil, flying soul-disc authoring cues and a Soul Flame sight. The main flame has a fixed-root shape-key animation. These are actual modeled/rendered objects, not a generated image presented as a working gun.

The earlier five iterations are retained in their original archive. The wire-like core, broad cloud disk and pinwheel-like spiral were visually weak; later iterations add thinner core filaments, tapered armor, wrapped grip ribs and side flame tongues. These files are newly authored after the workspace reset, not recovered copies of the unavailable older sculpt drafts.

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
- Greater apparent depth and richness in the spirit reservoir, final alpha cleanup and native VFX material validation.
- Real hands, grip clearance, aim alignment, inspection choreography and cancellation.
- All barrel/sight/skin variants and their motion clearances.
- A verified native export/bake/rendering path. Standard TaCZ cube JSON does not automatically consume this Blender mesh, material graph or shape keys.
- Actual projectile behavior, resources, damage, multiplayer, save migration, shader/Vulkan compatibility and measured frame times.

Passing the bounded authoring checks does not close these gates. Original AoA identity and credits remain with Tslat and contributors.

[Original behavior and upgrade direction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile) · [Default Soul Flame and optional sights](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Sights)

Earlier v5–v9 source archive SHA-256: `c5e119c64ca689aee32835e24679f8e4015b257e83e51db91fc0326c81c9a2a2`.

New v10–v12 source archive SHA-256: `612a0555cb840c40ce3ff4568b82ec4b17f94be776df65ae582b0548661c757d`.
