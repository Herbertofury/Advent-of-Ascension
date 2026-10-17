# Interactive workstation models · 1.21.1

[Open the 3D workstation inspector](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1)

Turn, tilt and zoom seven source-derived workstation item models. The viewer uses the released **Minecraft 1.21.1 / AoA 3.7.16.1** geometry and original textures. Each model links directly to its item reference and illustrated crafting/use guide.

## Pick a workstation

| Workstation | Inspect | Learn to use it |
|---|---|---|
| Infusion Table | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Ainfusion_table) | [Base slot, repeated ingredients and crafting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1) |
| Imbuing Chamber | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Aimbuing_chamber) | [Enchanting workflow](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Imbuing-Chamber-Enchanting-1.21.1) |
| Rune Randomizer | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Arune_randomizer) | [Rune production and limits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rune-Production-and-Current-Limits-1.21.1) |
| Mending Table | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Amending_table) | [Repair materials](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1) |
| Tea Sink | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Atea_sink) | [Brewing and ingredient priority](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Tea-Sink-Brewing-and-Ingredient-Priority-1.21.1) |
| Infused Press | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Ainfused_press) | [Compression and piston control](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infused-Press-Compression-and-Piston-Control-1.21.1) |
| Frame Bench | [Rotate](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1&id=aoa3%3Aframe_bench) | [Frames and armor shopping lists](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1) |

## Controls and sharing

- Drag the preview to orbit, or use Turn, Tilt and Zoom sliders.
- Focus the preview and use arrow keys to rotate, + / − to zoom, or 0 to reset.
- Front, Side and Top angle provide quick inspection views.
- “Link to this view” includes the selected model and camera settings. It does not upload a screenshot or save game data.
- If WebGL is unavailable, the viewer tries its software canvas renderer. If neither renderer is available, a crop from the existing source sheet remains available with the same guide links.

## Understand the limits

These are **static inventory item models**, not a simulation of the workstation. A cube-shaped item model stays a cube; the viewer does not invent a more elaborate placed-block renderer. Block-entity animation, fluids, active pistons, runtime lighting and machine behavior are outside this view. Animated textures use their first declared frame.

Fishing Cage is deliberately excluded from this seven-model set: its item appearance is generated pixel-extruded artwork rather than one of these JSON-element workstation meshes. Its ordinary reference remains in the item browser.

The software canvas preview sorts faces by depth rather than using a per-pixel depth buffer. Intersecting or translucent surfaces can differ from game rendering; the preview labels this limitation.

Other Minecraft releases are refused explicitly. An unknown model ID does not silently select a replacement.

## Performance and evidence

The viewer fetches one compact, version-pinned mesh/texture payload. It caches decoded textures and prepared geometry and redraws on interaction or resize, rather than running a permanent animation loop. Canvas pixel density and dimensions are capped. This concerns documentation rendering only and makes no in-game FPS claim.

The export contains **7 models, 240 quads and 14 deduplicated textures**. [Evidence receipts](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d-evidence-1.21.1.json) identify the model resources, texture resources, archive hashes and mesh hashes. Original AoA art is by Tslat and contributors. The inspector is original documentation code and does not execute Minecraft or mod classes.

[Return to illustrated walkthroughs](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.21.1) · [Model preview limitations](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Model-Turntables)
