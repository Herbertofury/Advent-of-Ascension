# Fluid surface material studies

**24 release-specific material views** now supplement the existing bucket references: 18 for Minecraft 1.16.5, three for 1.20.1 and three for 1.21.1. Fluid resource cards can show their own material instead of linking only to a shared bucket sheet.

**These are source-textured documentation studies, not Minecraft fluid-block renders.** Every view puts the fluid's selected still-texture frame and default source tint onto a deliberately synthetic unit box. Real fluid geometry depends on neighboring fluid levels, corner heights, flow and rendering state. The box must not be mistaken for a new item model or copied into the game as its fluid renderer.

[Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html) · [Separate bucket references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fluid-and-Bucket-References) · [Preview resolution ledger](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Inventory-Preview-Resolution-Ledger)

## Minecraft 1.16.5 · AoA 3.6.11

![Eighteen source-textured fluid material studies, with conditional Tinkers integrations labelled](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-fluid-surface-studies.webp)

- **Core/default fluid references:** Candied Water, Clear Water and Toxic Waste.
- **Tinkers-dependent integration references:** Molten Baronyte, Blazium, Elecanium, Emberstone, Ghastly, Ghoulish, Limonite, Lunar, Lyon, Mystite, Rosite, Shyrestone, Skeletal, Varsium and Charger.

The conditional labels remain important. Resource names and tinted artwork do not prove that the matching block or bucket is registered in an AoA-only installation. The existing [bucket evidence](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fluid-and-Bucket-References) explains the integration's fluid-only versus full block/bucket registration paths.

Molten-metal references use the cached, pinned TConstruct still texture selected by the integration. Molten Charger uses its water-texture default. Clear Water uses the recorded default water tint; the study does not apply a particular biome's live color.

## Minecraft 1.20.1 · AoA 3.7.1

![Candied Water, Toxic Waste and Tar source-textured material studies for 1.20.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-fluid-surface-studies.webp)

Each study uses this release's own AoA and vanilla resource files. The recorded default RGBA tints are:

| Fluid | R | G | B | Alpha |
|---|---:|---:|---:|---:|
| Candied Water | 255 | 105 | 180 | 200 |
| Toxic Waste | 38 | 42 | 23 | 255 |
| Tar | 35 | 35 | 35 | 255 |

Tar and Toxic Waste remain intentionally dark in these references. Their source colors are not brightened into a different material just to make the panel more vivid.

## Minecraft 1.21.1 · AoA 3.7.16.1

![Candied Water, Toxic Waste and Tar source-textured material studies for 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-fluid-surface-studies.webp)

The same three default tint tuples were checked in the released client-extension methods by the earlier artifact audit. This set still uses the 1.21.1 resource files, not an unlabelled image borrowed from another release.

## What is verified

- The version-specific fluid identities and tint tuples match the recorded source-defined bucket-reference metadata.
- The selected original texture bytes are hashed separately for each record.
- Vanilla/AoA animated textures use the renderer's first declared frame selection. The cached TConstruct texture uses its explicitly recorded first square frame.
- RGB and alpha are multiplied by the recorded tint. The renderer preserves non-zero alpha rather than discarding the translucent Candied Water material.
- Every standalone study is a non-empty 256-pixel image. Each fluid card links to its own reference.
- Only 24 fluid-card reference/status fields are changed. The other 125 initial-exception ledger records remain unchanged.

## What remains a runtime-rendering task

These views do not reproduce flowing-texture UV selection, changing corner heights, neighboring-face culling, fluid animation, fog, underwater overlays, emissive behavior, shader-pack effects or multi-layer translucent blending. The offline renderer records the nearest visible surface and its alpha; it is not a volume-transparency simulation.

The source-model atlas counts are not inflated by these studies. They are supplemental material references, just as the bucket studies remain supplemental container references. Invisible helpers, dynamic stored-stack renderers and unqualified localization names keep their own separate limitations.

## Evidence, reproduction and credits

[Per-fluid source hashes, tints, geometry limits and output hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fluid-surface-study-evidence.json) · [Exact inventory-card integration scope](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fluid-surface-integration-proof.json) · [Earlier pinned fluid and tint evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/fluid-bucket-reference-evidence.json).

AoA textures and systems are by Tslat and contributors; vanilla resources are by Mojang/Microsoft; the conditional molten-texture reference is by SlimeKnights/Tinkers' Construct contributors. The geometry, layouts and evidence checks are original documentation work. No game mod code was executed, and no private Enderloom renderer parity is certified.
