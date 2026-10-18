# Soul Flame: original animated texture candidate

An actual original rendered asset study for Soul Storm's default flame sight. **This is an authoring candidate, not a completed native sight or final visual acceptance.** The candle and gem alternatives remain separate attachments.

![Static frame from the original flame asset](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-frame-candidate-v3.png)

[Open the two-second animated preview](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-loop-candidate-v3.png) · [Inspect the texture atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-atlas-candidate-v3.png)

## What exists

- Fifteen original 256×256 RGBA frames, rendered from an editable procedural flame mesh and shader.
- A 1024×1024 atlas with four columns and four rows. Only cells 0–14 are used; cell 15 is deliberately empty.
- A two-second looping animated PNG preview and an explicit fixed root anchor in the authoring camera.
- Editable Blender source, a portable frame-regeneration script and a renderer-independent UV/time sampler.
- Previous versions are preserved: the first shader produced an unwanted hollow outline; the second filled the silhouette; this third iteration adds internal color variation.

The animated PNG is a web preview, not a promise that TaCZ will animate an APNG texture. The native candidate is the atlas plus a verified renderer/UV integration. A 1024×1024 RGBA8 base level contains 4 MiB of uncompressed texels before any mipmaps or engine overhead; share the atlas across instances rather than duplicating it per weapon.

The flame's root stays fixed while the upper shape changes. This helps attachment alignment, but does not itself calibrate Minecraft aiming or prove that a flame will not obscure the target. The native sight requires separate camera/pose testing and further art refinement.

## Verified checks

- All fifteen frames have transparent outer borders, reducing atlas-neighbor bleed risk. Mipmapping and native filtering still need testing.
- The sampler passed 10,000 time samples, never selecting unused cell 15. It wraps to frame 0 after two seconds and exposes a next-frame/blend value for a renderer that supports interpolation.
- The sampler reuses a caller-owned output object and cached UV rectangles rather than allocating new UV arrays each frame.
- A clean extraction of the source package regenerated all fifteen frames with **pixel-identical RGBA results** under Blender 4.3.2. PNG file bytes differed, so this is explicitly a pixel comparison, not byte-identical reproduction.

[Frame manifest](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-flipbook-candidate-v3.json) · [Reproduction receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-flipbook-reproduction-v3.json)

## Download the original authoring study

[Editable source, textures and tests](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-flipbook-candidate-v3.zip)

Archive SHA-256: `5307cdccbdfbe41fd6474aa5ab4806787f3fe07518df0b1690111ac1afbaee68`.

This archive is not a mod to put in the Mods folder. It contains no third-party game meshes or animation files. The source renderer can regenerate frames; the UV helper does not install itself into TaCZ.

## Native work remaining

- [ ] Attach the effect to the correct functional leaf bone using the [source-backed renderer plan](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Flame-Native-Renderer-Plan).
- [ ] Explicitly disable it for Soul Gem and use the appropriate offset for Soul Candle; ordinary bone visibility alone is insufficient in the inspected callback path.
- [ ] Validate texture filtering, alpha/blending, depth, third-person views, shader passes and the Vulkan compatibility target.
- [ ] Use paused/game-time presentation correctly and avoid gameplay effects or per-frame scans.
- [ ] Test stable aim, hand clearance, inspection interruption and all supported attachment combinations.
- [ ] Measure real frame-time, memory and render-submit changes. No native FPS or zero-regression claim is made by this asset study.

[Soul Storm sight options](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Sights) · [Playful inspection storyboard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Inspection-Storyboard)
