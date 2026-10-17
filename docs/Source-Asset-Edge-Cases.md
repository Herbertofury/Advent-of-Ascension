# Source asset edge cases

## The last seven 1.12.2 inventory candidates

These supplemental previews cover the seven records excluded from the first 2,459-image historical inventory pass. Together the regular galleries and this diagnostic sheet illustrate all **2,466 unambiguous localization/model candidates in that extraction**. This is not a census of every runtime registry entry.

![Seven source edge-case inventory previews](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-source-edge-cases.webp)

Models and textures: **Tslat and contributors**, official AoA 3.3.6 artifact. These are independently rendered documentation images.

| Asset | Why the strict first pass stopped | Supplemental handling |
|---|---|---|
| Filtration System | Some faces reference undefined `#missing` texture aliases | Explicit magenta/black diagnostic texture for those faces; original visible faces retained |
| Boiling Filtration System | Undefined texture aliases | Same explicit diagnostic handling |
| Gold Skeletron Statue | 64 undefined aliases on zero-area faces | Resolved: discard degenerate faces before texture lookup |
| Iropole | Undefined texture aliases | Same explicit diagnostic handling |
| Ornate Skeletron Statue | 64 undefined aliases on zero-area faces | Resolved by the same geometric-area check |
| Skeletron Statue | 64 undefined aliases on zero-area faces | Resolved by the same geometric-area check |
| Shyre Cloud | The original cutout threshold discarded its translucent pixels | Preserve nonzero alpha in a nearest-depth reference preview |

The unresolved faces are largely hidden in this view. Their absence from the visible screenshot does not prove the source contains no defects. No source textures or mod files were patched, and no guessed replacement artwork was substituted.

The Shyre Cloud view preserves the source alpha but does not implement full runtime translucent surface blending. Its color and opacity can differ against other backgrounds or under the game's lighting.

## Three statue cases resolved without changing source assets

![Corrected statue references and remaining diagnostic cases](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-degenerate-face-references.webp)

A geometric check found that all 64 unbound texture references in each of the three Skeletron statue variants belong to **zero-area faces**. They cannot contribute rasterized surface area. The documentation renderer had tried to resolve those textures too early; it now discards degenerate faces first. The real, nondegenerate faces use their original textures. No replacement texture was guessed and no upstream asset was patched.

The remaining Filtration System, Boiling Filtration System and Iropole cases have respectively **7, 7 and 40 positive-area unbound references** and remain explicitly diagnostic. Positive area alone does not prove those faces are visible from outside; in-game occlusion still matters.

Three unaffected baseline models rendered pixel-identically before and after the change. The normal Skeletron Statue is now available as a proper source-model loot reference. [Geometric checks](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/degenerate-face-validation.json) · [Statue-specific evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skeletron-statue-render-evidence.json).

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
| Compressed Item | [Model resource](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/assets/models/item/compressed_item.json) is empty. [The item](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/CompressedItem.java) uses a component carrying another stack and compression count. | Released nested model selection is now traced below; final tint/glint/custom-renderer parity remains unverified. |

Six additional localization candidates (Discovery, Expedition, Lessons, Primitive, Raw Herring and The Portal) lack matching models in the inspected modern artifact, and this pass found no matching literal registration in its pinned registration sources. They remain **unqualified localization candidates**, not certified missing active items. Likewise, the Trickster geometry resource has no matching texture or class in the inspected 1.21.1 artifact; do not count it as a verified active creature merely because a geometry file remains.

This distinction is important for Enderloom's content union: preserve evidence about legacy/unused resources without conflating them with active target behavior. Resolve runtime registration, custom loaders and conversion intent before treating an exception as an upstream defect.

## Creature Essence: authentic layers, unresolved runtime presentation

![Creature Essence base and overlay textures, shown separately](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/creature-essence-source-layers.webp)

The inspected 1.16.5 (3.6.11), 1.20.1 (3.7.1) and 1.21.1 (3.7.16.1) releases contain the same two 16×16 sprites. Their model inherits `minecraft:item/generated` but declares `base` and `overlay`, without numbered generated-item layers. This sheet enlarges the real sprites separately over a checkerboard. It does not guess their combination, color tint or in-game item appearance. Inventory cards now expose this study while retaining the unresolved runtime-render status.

Creature Essence is registered in the inspected source, so it should not be dismissed as an unused localization entry. Its behavior is version-sensitive:

- In the inspected 1.16.5 and 1.20.1 released classes, `getStoredEntity` and `getStoredEntityName` exist. The pinned source reads the `essence_entity` and `essence_entity_name` tags.
- In 1.21.1, the entity getter is commented out in the pinned source and absent from the released class. The stored-name method returns `?`; the old tag-reading body is commented out. Do not promise legacy stored-creature behavior on that basis.
- A direct literal scan of all classes in each released artifact finds this item's class and registration class only. That does not rule out generic resource loading, reflection or another mod supplying behavior, and it does not establish survival acquisition.

For an Enderloom restoration, resolve the target release's model-loader and tint path before building a composed preview or changing the game assets. Preserve any older item data until its migration has been explicitly tested. [Released model, sprite hashes and class-method evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/creature-essence-evidence.json) · [Pinned modern item source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/CreatureEssence.java).

## Compressed Item: the nested model-selection path

![Two stored-model examples and the released compressed-item model delegation rules](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/compressed-item-model-delegation-1.21.1.webp)

For **Minecraft 1.21.1 / AoA 3.7.16.1**, the released client mixin configuration includes `client.function.ItemRendererMixin`. Its inspected callback first checks that the item is the Compressed Item and has `COMPRESSED_ITEM_DATA`. It then retrieves `compressedStack()`, calls `getModel` for that stored stack with the **same level, entity and seed**, and sets the returned model as the callback result. The pinned source injects this callback at the head of `getModel`, with cancellation enabled.

This resolves the model-selection route that the empty standalone model file did not explain. The two images above are existing source-model previews of example stored contents. They are not screenshots of compressed packets or a guarantee of their final in-game appearance.

- **Compression count:** the selected callback does not read it, so it does not itself select a different mesh, scale or color for higher tiers.
- **Missing data component:** this branch does not replace the selected model. An empty standalone model resource alone does not establish the complete fallback appearance.
- **Nested compressed data:** the callback calls model selection again and contains no local depth limit. Check malformed or deeply nested data separately; ordinary compression stores a stack and tier rather than proving that arbitrary nesting is safe.
- **Final presentation:** selecting a nested BakedModel does not prove that later rendering uses the nested stack's tint, glint, special renderer or every component. Hand/GUI transforms, resource packs and other renderer mixins still need runtime checks.

For a restoration adapter, preserve the stored stack and its components, resolve its model using the relevant entity/world context, and test simple items, block items, tinted items, custom-rendered items and damaged or missing data separately. Do not manufacture one universal compressed-item cube and call it an exact preview.

[Released callback and resource evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/compressed-item-model-evidence-1.21.1.json) · [Diagram crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/compressed-item-art-evidence-1.21.1.json) · [Infused Press operation and acquisition limits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infused-Press-Compression-and-Piston-Control-1.21.1).
