# Interactive plant growth states · 1.21.1

[Open the plant-state explorer](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1)

Inspect **18 plants and 179 released blockstates** from Minecraft 1.21.1 / AoA 3.7.16.1. Change the age, choose a Thorny Plant height slice, rotate the geometry and compare stages without the camera enlarging each young plant to fill the frame.

![Existing Ashfern source-growth reference sheet](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-growth-ashfern_crop.webp)

The sheet above is an existing illustrated source reference. The interactive viewer separately holds the camera bounds constant within each plant.

## Use the viewer

1. Choose a **Plant**. Each selection starts at its released age 0 state.
2. Choose an **Age state**. The values come directly from that plant’s blockstate map.
3. For **Thorny Plant**, also choose **Height slice**: 0/bottom, 1/middle or 2/top model. Each is an independent block-state reference.
4. Rotate with dragging, arrow keys or the Turn/Tilt sliders. Use Front, Side and Top angle for comparisons.
5. Open **Item reference** for the parent block’s release-specific entry, or **Growth-state guide** for its illustrated sheet.
6. Share **Link to this view** to retain plant, age, height slice and camera settings.

Changing age does not simulate elapsed time, soil, light, growth ticks or harvesting. Maximum listed age is a resource-state value; this viewer is not a substitute for the gameplay guide. For planting and harvest behavior, use [Farming, soils and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Farming-Soils-and-Harvesting-1.21.1).

## Every indexed plant

| Plant | Age values | Height values | States |
|---|---|---|---:|
| [Ashfern](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Aashfern_crop&age=0) | 0–7 | No height property | 8 |
| [Bubble Berries](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Abubble_berry_crop&age=0) | 0–7 | No height property | 8 |
| [Chilli](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Achilli_crop&age=0) | 0–7 | No height property | 8 |
| [Eye Bulbs](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Aeye_bulb_crop&age=0) | 0–7 | No height property | 8 |
| [Floracles](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Afloracles_crop&age=0) | 0–7 | No height property | 8 |
| [Goldicaps](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Agoldicaps_crop&age=0) | 0–7 | No height property | 8 |
| [Green Manure](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Agreen_manure&age=0) | 0–7 | No height property | 8 |
| [Heart Fruit](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Aheart_fruit_crop&age=0) | 0–7 | No height property | 8 |
| [Living Growth](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Aliving_growth&age=0) | 0–5 | No height property | 6 |
| [Luna Globes](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Aluna_globe_crop&age=0) | 0–7 | No height property | 8 |
| [Lunacrike](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Alunacrike_crop&age=0) | 0–7 | No height property | 8 |
| [Lunalons](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Alunalon_crop&age=0) | 0–7 | No height property | 8 |
| [Magic Marangs](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Amagic_marang_crop&age=0) | 0–7 | No height property | 8 |
| [Mystic Shrooms](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Amystic_shroom_crop&age=0) | 0–7 | No height property | 8 |
| [Rosidons](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Arosidon_crop&age=0) | 0–7 | No height property | 8 |
| [Tea](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Atea_crop&age=0) | 0–7 | No height property | 8 |
| [Thorny Plant](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Athorny_plant_crop&age=0&height=0) | 0–14 | 0, 1, 2 | 45 |
| [Trilliads](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1&plant=aoa3%3Atrilliad_crop&age=0) | 0–7 | No height property | 8 |

**134 age-only states + 45 Thorny Plant age/height states = 179 references.** All 18 crops are block-only references without a standalone item model in the inspected archive; this does not make their placed growth-state models missing.

## When a state is blank

Fourteen Thorny Plant states sample fully transparent source-texture regions. The viewer labels these explicitly and leaves the geometry visually blank instead of inventing artwork or substituting another age. The other 31 Thorny Plant states contain visible sampled pixels.

The 45 combinations are resource definitions. They are not proof that every combination occurs naturally, and the viewer does not assemble three height slices into a claimed valid tall plant.

## Why the ordinary block-model viewer excludes these

The [block-model explorer](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Block-Model-Coverage-1.21.1) indexes inventory item geometry. These plants instead have age-dependent **placed-block** resources. Keeping those representations separate avoids turning a crop block into an invented inventory item.

The audit of all 31 absent standalone item-model references now distinguishes:

| Resource category | References | What the checked resources establish |
|---|---:|---|
| Plant growth states | 18 | 179 explicit age/height mappings and renderable source geometry |
| Particle-only sign models | 6 | Wall-sign/hanging-sign reference models contain particle textures, not JSON-element geometry |
| Texture-only fluid references | 3 | Candied Water, Tar and Toxic Waste model resources declare textures without JSON-element geometry |
| Empty technical models | 3 | Air Gap, Banner Extension and Killzone resolve without JSON-element geometry |
| Placed portal-axis geometry | 1 | Nowhere Activity Portal has two axis-specific models; see its existing state sheets |

This classification inspects resources. It does not certify a custom runtime renderer, registration, availability or behavior. [Portal and multi-state references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Multi-State-Block-References) · [Inventory preview resolution ledger](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Inventory-Preview-Resolution-Ledger).

## Rendering and loading limits

The source contains **1,588 quads and 109 deduplicated textures** in a **559,009-byte** payload. One fetch serves all plant/state changes; texture images decode on demand. Rendering occurs on interaction or resize, without an automatic animation loop.

Software face ordering is approximate. Textures retain their source appearance; game lighting, world placement, collision and growth behavior are not reproduced. A multi-state reference sheet is available if interactive canvas rendering fails, and is labeled as a sheet rather than an exact single-state fallback.

Unsupported releases, unknown plants and unlisted age/height combinations are refused. No other plant or stage is silently substituted.

## Evidence

- [Plant-state mesh and texture receipts](https://herbertofury.github.io/Advent-of-Ascension/crop-state-mesh-evidence-1.21.1.json)
- [All 31 block-only model classifications](https://herbertofury.github.io/Advent-of-Ascension/block-only-model-classification-1.21.1.json)
- [Existing growth-stage sheets across releases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crops-and-Growth-Stages)

Tests reconcile all 179 selectors to the released blockstate JSON, verify source/texture/mesh hashes, check fixed per-plant bounds, and exercise all 179 viewer state selections. These are static/documentation checks, not an in-game growth test. Original AoA models and textures are by Tslat and contributors.
