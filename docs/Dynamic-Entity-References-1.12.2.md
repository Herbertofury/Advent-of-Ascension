# Dynamic entity references · 1.12.2

These three entities do not have one ordinary AoA creature mesh. Their render paths are identified below with useful visual references. These studies are separate from the 537 static model/texture portraits; they do not pretend to reproduce runtime animation or effects.

## Boss Item: the carried summoning item

![Seven source-defined summoning-item appearances](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-boss-summoning-item-reference.webp)

`aoa3:boss_item` uses the vanilla dropped-item renderer through [BossItemRenderer](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/render/entities/misc/BossItemRenderer.java). Its appearance comes from the carried ItemStack. The inspected [item-toss event](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/event/PlayerEvents.java) replaces tossed BossSpawningItem instances with this entity through [EntityUtil](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/utils/EntityUtil.java). It is a boss-summoning carrier, not a single universal boss-loot model.

The seven source-defined subclasses pictured are Amphibiyte Lung, Nethengeic Callstone, Troll Idol, Haunted Idol, Explosive Idol, Shroom Stone and Heavy Boulder. These are official item-model references; their original artwork is pixel-extruded rather than a bespoke volumetric remodel. Item count, rotation, bobbing and summoning particles are not simulated in this sheet. The carrier can technically hold other stacks, so the sheet does not limit the renderer to these seven appearances.

Example: [Heavy Boulder](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/item/misc/summon/HeavyBoulder.java) summons Rock Rider and checks the configured Haven dimension and a clear spawn volume. Those checks belong to that item's source version, not a universal rule for every summoner.

## Fake TNT: familiar appearance, real source behavior

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-fake-tnt-reference.webp" width="256" alt="Vanilla 1.12.2 TNT block as a reference for Fake TNT">

The [renderer registration](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/render/entities/EntityRenders.java) uses vanilla RenderTNTPrimed. The image above is its underlying 1.12.2 TNT block appearance in a static inventory-style view, with no fuse flashing, swelling, smoke or animated entity transforms. It is not a captured primed-entity frame.

Despite the name, [EntityFakeTnt](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/misc/EntityFakeTnt.java) calls `WorldUtil.createExplosion(..., 4.0f)` when its fuse expires on the server. Do not document it as harmless purely from its name; actual damage and terrain effects depend on the explosion helper and configuration.

## Occult Block: a colored diagnostic volume

![Five harvest-level color examples](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-occult-block-color-study.webp)

[OccultBlockRenderer](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/render/entities/misc/OccultBlockRenderer.java) disables textures and draws the entity bounding box. The registered texture path is not used by that draw path. Its color is selected from the block's harvest level:

| Harvest level | Source color | RGB hex |
|---|---|---|
| 0 | Red | `#FF0000` |
| 1 | Orange | `#DF9900` |
| 2 | Yellow | `#FFFF00` |
| 3 | Pigment green | `#009342` |
| 4 or other/default | Dark lime green | `#009900` |

Values come from [Enums.RGBIntegers](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/library/Enums.java). The diagram uses exact base colors with deliberately shaded side faces for legibility; it is not a runtime lighting or outline reproduction. [EntityOccultBlock](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/misc/EntityOccultBlock.java) sets width and height to 0.99 and reports itself glowing. Its lifetime and full-cube checks are implemented in the entity update method.

## Validation still needed

- Capture actual thrown-item rotation and summoning effects in the target game build.
- Capture Fake TNT across fuse phases, and independently test explosion/configuration behavior in a disposable world.
- Compare Occult Block outlines, depth behavior, harvest-level fallback and visibility against the game renderer.
- Keep all three outside the ordinary static creature-portrait count.

[Return to the historical entity atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Atlas-1.12.2)

AoA source/artwork: Tslat and contributors. Vanilla TNT artwork and rendering conventions: Mojang. Documentation diagrams and independent previews are illustrative.
