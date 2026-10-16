# Source asset edge cases

## The last seven 1.12.2 inventory candidates

These supplemental previews cover the seven records excluded from the first 2,459-image historical inventory pass. Together the regular galleries and this diagnostic sheet illustrate all **2,466 unambiguous localization/model candidates in that extraction**. This is not a census of every runtime registry entry.

![Seven source edge-case inventory previews](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-source-edge-cases.webp)

Models and textures: **Tslat and contributors**, official AoA 3.3.6 artifact. These are independently rendered documentation images.

| Asset | Why the strict first pass stopped | Supplemental handling |
|---|---|---|
| Filtration System | Some faces reference undefined `#missing` texture aliases | Explicit magenta/black diagnostic texture for those faces; original visible faces retained |
| Boiling Filtration System | Undefined texture aliases | Same explicit diagnostic handling |
| Gold Skeletron Statue | Undefined texture aliases | Same explicit diagnostic handling |
| Iropole | Undefined texture aliases | Same explicit diagnostic handling |
| Ornate Skeletron Statue | Undefined texture aliases | Same explicit diagnostic handling |
| Skeletron Statue | Undefined texture aliases | Same explicit diagnostic handling |
| Shyre Cloud | The original cutout threshold discarded its translucent pixels | Preserve nonzero alpha in a nearest-depth reference preview |

The unresolved faces are largely hidden in this view. Their absence from the visible screenshot does not prove the source contains no defects. No source textures or mod files were patched, and no guessed replacement artwork was substituted.

The Shyre Cloud view preserves the source alpha but does not implement full runtime translucent surface blending. Its color and opacity can differ against other backgrounds or under the game's lighting.

## Restoration implications

- Inspect and test undefined aliases before changing them. Hidden internal faces may be deliberately irrelevant to the visible mesh; a broad material replacement could introduce a regression.
- Keep cutout and translucent rendering paths separate. A threshold suitable for plants can erase a cloud-like block.
- Check every model from several angles and against contrasting backgrounds in the target game before declaring renderer parity.
- Preserve the exact source generation. In particular, an old statue asset does not establish the behavior or appearance of a later entity implementation.

[Historical galleries](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Galleries) · [Coverage and remaining work](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage)

## Translucent Shyre Cloud in later releases

![Shyre Cloud transparent source studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/shyre-cloud-translucent-references.webp)

The inspected 1.16.5, 1.20.1 and 1.21.1 textures use alpha 77/255 throughout. The original generic cutout threshold discarded them, producing a blank documentation image. These independent previews retain nonzero alpha and show the nearest surface over a checkerboard. They are source-asset studies, not full Minecraft translucent sorting or overlapping-face blending. The earlier blank result was a limitation of the showcase renderer, not proof that the texture was absent.

## Intentionally empty and unqualified modern candidates

| Candidate | Verified source/resource evidence | Documentation treatment |
|---|---|---|
| Air Gap | [AirGap](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/block/functional/misc/AirGap.java) returns RenderShape.INVISIBLE and an empty shape. | Explain the invisible helper; do not invent a visible block skin. |
| Banner Extension | [BannerExtension](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/block/decoration/banner/BannerExtension.java) returns RenderShape.INVISIBLE and coordinates with its paired banner block. | It is not a second independent cloth mesh. |
| Killzone | [KillzoneBlock](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/block/functional/misc/KillzoneBlock.java) returns MODEL, while [its model resource](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/assets/models/block/killzone.json) inherits the empty block parent. | Distinguish empty geometry from the functional server-side hazard. No claim of an ordinary visible cube. |
| Creature Essence | [Model resource](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/assets/models/item/creature_essence.json) has base/overlay texture keys instead of the ordinary generated-item numbered layers. | A dedicated mapping/renderer is not verified here; a made-up combined image would not certify the item. |
| Compressed Item | [Model resource](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/assets/models/item/compressed_item.json) is empty. [The item](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/CompressedItem.java) uses a component carrying another stack and compression count. | Runtime appearance needs a verified adapter; no fixed generic mesh is assumed. |

Six additional localization candidates (Discovery, Expedition, Lessons, Primitive, Raw Herring and The Portal) lack matching models in the inspected modern artifact, and this pass found no matching literal registration in its pinned registration sources. They remain **unqualified localization candidates**, not certified missing active items. Likewise, the Trickster geometry resource has no matching texture or class in the inspected 1.21.1 artifact; do not count it as a verified active creature merely because a geometry file remains.

This distinction is important for Enderloom's content union: preserve evidence about legacy/unused resources without conflating them with active target behavior. Resolve runtime registration, custom loaders and conversion intent before treating an exception as an upstream defect.
