# Block model explorer · 1.21.1

[Interactive plant-state explorer · 1.21.1: 18 plants and 179 age/height states](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Interactive-Plant-Growth-States-1.21.1)

[Open the interactive block-model explorer](https://herbertofury.github.io/Advent-of-Ascension/block-models.html?v=1.21.1)

Explore **1,026 block item-model resource references** from Minecraft 1.21.1 / AoA 3.7.16.1. Search by name or resource ID, turn the model around, inspect it from above, and jump directly to the matching item entry.

These are source-model references. A retained model does not establish that its block is registered, obtainable, used by a finished dimension or present in the private Enderloom build.

![Six source-model examples, including the Precasian Grass tint limitation](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/block-model-explorer-overview-1.21.1.webp)

## Find and inspect a block

1. Type part of its name or resource ID in **Find a block**.
2. Choose the exact entry in **Block model**. The first 100 matching choices are listed initially; use **Show more matching choices** to expand the list. The current selection stays available while you search.
3. Drag to orbit, use the Turn/Tilt/Zoom sliders, or focus the canvas and use arrow keys. + / − changes zoom; 0 resets.
4. Use **Front**, **Side** or **Top angle** for quick comparisons.
5. Follow **Item reference** to its release-specific card, recipe search and other contextual links. These searches may legitimately have no result for retained/unobtainable content.
6. Share **Link to this view** to preserve the model and camera settings.

The ordinary [item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) now links directly to this viewer for every one of the 1,026 indexed references.

## Coverage and exclusions

| Source category | References | Treatment |
|---|---:|---|
| JSON-element block item models | 1,026 | Interactive textured geometry |
| Generated pixel artwork | 152 | Existing item reference; excluded from this volumetric-model collection |
| Model resource could not be resolved in the inspected archives | 31 | Explicit exclusion; no substitute model invented |
| Included models requiring runtime tint | 6 | Included with a visible tint warning |

The six tint-limited references are **Baobab Leaves, Lucalus Leaves, Precasian Grass, Stranglewood, Stranglewood Leaves and Stranglewood Log**. Their source textures are shown without biome/runtime coloring. This is a visual limitation, not proof the texture is broken in-game.

Coverage reconciles all **1,209 block-reference candidates** in the current inventory dataset: 1,026 included plus 183 explicitly excluded. This is a resource inventory, not a claim of 1,209 independently verified registered gameplay blocks.

## Rendering boundaries

- Geometry comes from the **inventory item model**, including inherited JSON parents, element rotations and UVs. Placed-block state, connected textures and custom block-entity renderers are separate systems.
- Animated textures use the first declared source frame.
- The original software canvas renderer uses depth-sorted textured triangles. It does not run Minecraft, mod classes or a game renderer.
- Face ordering is approximate. Intersecting or translucent surfaces can differ from the game; this limitation is visible in the viewer.
- Game lighting, biome tint, fluids and moving machine parts are not simulated.
- A source-sheet fallback remains when canvas rendering cannot be prepared.
- Unsupported releases and unknown IDs are refused rather than replaced with another model.

For a smaller crafting-focused set, use the [seven-workstation inspector](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Interactive-Workstation-Models-1.21.1), which also offers an optional WebGL rendering path.

## Loading and memory budget

The index is **462,710 bytes** and contains metadata, not all mesh/texture payloads. Models are divided into **33 hash-pinned chunks**, with at most 32 models per chunk. Only the selected chunk is fetched; searching and expanding the choice list do not download meshes.

All chunks together contain **17,537 quads** and **5,864,398 bytes** of JSON/embedded PNG data. The largest chunk is **652,659 bytes**. Those totals are not the first-page download size.

The browser retains at most three chunk promises and 128 cached texture-image promises. The current model holds the images it needs while displayed. Rendering is on-demand, with capped canvas density and dimensions, rather than a permanent animation loop. These are documentation design limits, not a measured in-game performance improvement.

## Inspect the receipts

- [Coverage index and explicit exclusions](https://herbertofury.github.io/Advent-of-Ascension/block-mesh-index-1.21.1.json)
- [Archive, texture and mesh evidence](https://herbertofury.github.io/Advent-of-Ascension/block-mesh-evidence-1.21.1.json)
- [Release-specific tutorials](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.21.1)

Every included reference is joined to the inventory dataset by ID and model path. Tests verify the source-resource hashes, PNG bytes/pixels, per-model face hashes, chunk hashes and explicit exclusion count. Original AoA models and textures are by Tslat and contributors.
