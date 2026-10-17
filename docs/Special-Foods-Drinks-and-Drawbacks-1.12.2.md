# Special foods, drinks and drawbacks · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** Nineteen concrete food classes are checked here, complementing the separate [fish healing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cooking-Fish-and-Hunger-Scaled-Healing-1.12.2), [tea brewing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Tea-Sink-Brewing-Priority-and-Drink-Effects-1.12.2) and [Rosidons escape](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rosidons-Escape-and-Destination-Safety-1.12.2) guides. This is a scoped special-food reference, not a complete runtime food registry.

## Read before eating

- Two hunger points equal one full food-bar icon; two health points equal one heart. The saturation modifier is not a direct restoration amount.
- “Always edible” is a class setting, not a guarantee that every pack or player state accepts the use.
- Potion entries below are **requests**: existing effects, effect-combination rules and Forge hooks can change the outcome. Duration is in ticks; seconds assume 20 ticks per second.
- Amplifiers are zero-based. The source value is preserved, especially for Trilliad Leaves; do not turn a large number into an unsupported claim about actual movement or damage.
- Empty recipe/trade references do not mean an item is unobtainable. Crop drops, entity interactions and other routes are separate.

## Illustrated reference

### Bubble Berries

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-bubble_berries.webp" width="190" height="190" alt="Bubble Berries source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Adds 50 to air, capped at 300. This is not a Water Breathing potion or indefinite underwater protection.

Local use-duration override: **18 ticks** (nominally 0.9 seconds at 20 TPS).

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BubbleBerries.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Abubble_berries) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Chilli

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-chilli.webp" width="190" height="190" alt="Chilli source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests 3 seconds of fire. A server-player branch also checks Nether dimension −1 and being in lava for the overheat advancement. Do not treat it as a harmless snack.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Chilli.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Achilli) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Eye Candy

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-eye_candy.webp" width="190" height="190" alt="Eye Candy source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests +10 Energy through the player-resource helper. It uses the drink action despite its candy name.

Local use-duration override: **24 ticks** (nominally 1.2 seconds at 20 TPS).

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EyeCandy.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Aeye_candy) · [Exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fmisc%2Feye_candy)

### Fiery Chops

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-fiery_chops.webp" width="190" height="190" alt="Fiery Chops source-model portrait">

**Hunger:** 5 points · **Saturation modifier:** 0.5 · **Always edible:** not enabled locally.

Requests +20 Rage through the resource helper, alongside normal food restoration.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FieryChops.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Afiery_chops)

### Floracle Sticks

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-floracle_sticks.webp" width="190" height="190" alt="Floracle Sticks source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests 8 vanilla experience points, not eight levels.

Local use-duration override: **16 ticks** (nominally 0.8 seconds at 20 TPS).

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FloracleSticks.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Afloracle_sticks) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Goldicap Petals

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-goldicap_petals.webp" width="190" height="190" alt="Goldicap Petals source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests Speed and Jump Boost effects listed below; always edible, but not a sustained movement buff.

Local use-duration override: **24 ticks** (nominally 1.2 seconds at 20 TPS).

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Speed | 40 | 2 | 1 | hidden |
| Jump Boost | 40 | 2 | 1 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoldicapPetals.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Agoldicap_petals) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Halycon Beef

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-halycon_beef.webp" width="190" height="190" alt="Halycon Beef source-model portrait">

**Hunger:** 7 points · **Saturation modifier:** 0.7 · **Always edible:** not enabled locally.

Still requests Nausea after cooking. Cooking removes the raw version’s local Poison request, not every drawback.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Nausea | 150 | 7.5 | 0 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HalyconBeef.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Ahalycon_beef) · [Exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_halycon_beef)

### Halycon Milk

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-halycon_milk.webp" width="190" height="190" alt="Halycon Milk source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests 2 health points of healing, then cures effects using a Milk Bucket as the curative item, then adds Nausea and returns a Bucket. It is not a guarantee that every modded effect is removed.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Nausea | 100 | 5 | 0 | shown |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HalyconMilk.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Ahalycon_milk)

### Heart Fruit

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-heart_fruit.webp" width="190" height="190" alt="Heart Fruit source-model portrait">

**Hunger:** 15 points · **Saturation modifier:** 0.3 · **Always edible:** not enabled locally.

Calls the self-harm helper with 7 health points. The helper skips Creative; when the subtraction would not leave positive health, it uses an absolute, armor-bypassing damage path. This can be dangerous. The alive-player Precasia/Blank Realmstone branch is part of Candyland progression.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HeartFruit.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Aheart_fruit) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Hot Rod

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-hot_rod.webp" width="190" height="190" alt="Hot Rod source-model portrait">

**Hunger:** 9 points · **Saturation modifier:** 0.9 · **Always edible:** not enabled locally.

Requests +20 Rage, the same resource addition as Fiery Chops, but has different food values.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HotRod.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Ahot_rod) · [Exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fmisc%2Fhot_rod)

### Luna Globe

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-luna_globe.webp" width="190" height="190" alt="Luna Globe source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests Invisibility for 120 ticks. This alone is not a guarantee that mobs ignore equipment, sounds or other detection rules.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Invisibility | 120 | 6 | 0 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunaGlobe.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Aluna_globe) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Lunacrike

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-lunacrike.webp" width="190" height="190" alt="Lunacrike source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests addVelocity(current motion X, 2, current motion Z), then Jump Boost. These are velocity arguments, not a two-block teleport or a measured jump height. No fall-immunity request appears here.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Jump Boost | 40 | 2 | 1 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Lunacrike.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Alunacrike) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Lunalons

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-lunalons.webp" width="190" height="190" alt="Lunalons source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Requests Night Vision for 40 ticks; the raw amplifier is 1.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Night Vision | 40 | 2 | 1 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Lunalons.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Alunalons) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Lunarade

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-lunarade.webp" width="190" height="190" alt="Lunarade source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0.2 · **Always edible:** yes.

Removes Blindness, requests Night Vision and Jump Boost, and returns a Lunarade Mug.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Night Vision | 40 | 2 | 1 | hidden |
| Jump Boost | 40 | 2 | 0 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Lunarade.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Alunarade) · [Trader offer](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:zal_vendor&q=aoa3%3Alunarade)

### Magic Marang

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-magic_marang.webp" width="190" height="190" alt="Magic Marang source-model portrait">

**Hunger:** 5 points · **Saturation modifier:** 0.7 · **Always edible:** not enabled locally.

Requests both Night Vision and Glowing. Visibility help comes with an outline-related effect; it is not a stealth food.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Night Vision | 200 | 10 | 0 | hidden |
| Glowing | 200 | 10 | 0 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MagicMarang.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Amagic_marang) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Mystic Shrooms

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-mystic_shrooms.webp" width="190" height="190" alt="Mystic Shrooms source-model portrait">

**Hunger:** 2 points · **Saturation modifier:** 0.4 · **Always edible:** not enabled locally.

A plantable ItemSeedFood with no custom potion callback in this class. It also supplies the first-priority Fungal Tea additive. Keep some for planting.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MysticShrooms.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Amystic_shrooms) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Raw Halycon Beef

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-raw_halycon_beef.webp" width="190" height="190" alt="Raw Halycon Beef source-model portrait">

**Hunger:** 2 points · **Saturation modifier:** 0.3 · **Always edible:** not enabled locally.

Requests Nausea and Poison. The cooked version has different nutrition and omits the local Poison request.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Nausea | 150 | 7.5 | 0 | hidden |
| Poison | 40 | 2 | 0 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RawHalyconBeef.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Araw_halycon_beef)

### Trilliad Leaves

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-trilliad_leaves.webp" width="190" height="190" alt="Trilliad Leaves source-model portrait">

**Hunger:** 0 points · **Saturation modifier:** 0 · **Always edible:** yes.

Removes Nausea, then requests Blindness, Slowness, Regeneration, Poison and Jump Boost together. Several amplifiers are unusually large. Do not describe this as a simple healing or movement item.

| Effect request | Ticks | Nominal seconds | Raw amplifier | Particles |
|---|---:|---:|---:|---|
| Blindness | 130 | 6.5 | 0 | hidden |
| Slowness | 100 | 5 | 10 | shown |
| Regeneration | 100 | 5 | 2 | hidden |
| Poison | 100 | 5 | 7 | shown |
| Jump Boost | 100 | 5 | 128 | hidden |

All requests in this table set the ambient flag to true. Hidden potion particles do not make the effect absent.

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TrilliadLeaves.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Atrilliad_leaves) · [Growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2)

### Yeti Fingernails

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-food-1.12.2-yeti_fingernails.webp" width="190" height="190" alt="Yeti Fingernails source-model portrait">

**Hunger:** 1 points · **Saturation modifier:** 0.1 · **Always edible:** yes.

Uses a 100-tick duration override and a server-side flavor message on completion. Its Creative tab is set to null; that does not prove it is unobtainable.

Local use-duration override: **100 ticks** (nominally 5 seconds at 20 TPS).

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.YetiFingernails.name) · [Creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=aoa3%3Ayeti_fingernails)

## Obtaining Halycon Milk

The inspected Halycon interaction accepts a Bucket. Outside Creative it shrinks the held bucket stack by one. If that stack is empty afterward, the hand is replaced with Halycon Milk; otherwise the milk is passed to the give-or-drop helper. The food itself has maximum stack size 1.

There is no explicit local server guard in this entity interaction method. That is a client/server test target for restoration, not evidence that duplicate milk occurs in an actual session. The drinking callback’s local effect branch is server-gated.

## Lunarade and its returned mug

The checked Zal Vendor candidates include **5 Copper Coins → 1 Lunarade** and **1 Lunarade Mug → 1 Copper Coin**. Drinking returns the mug. If both trades are available and accepted, redeeming it recovers one coin, making that particular purchase-and-return loop a net four Copper Coins. It is not an automatic refund or a promise that both generated offers will always be available.

## Practical cautions

- Preserve the order of Halycon Milk’s healing, cure, new Nausea and Bucket return. “Clears effects” alone would miss the newly added effect.
- Heart Fruit’s self-harm and Candyland challenge use separate checks. See [historical realmstone challenges](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-and-Challenges-1.12.2) before attempting progression with low health.
- Resource foods pass their requested additions through regeneration buffs, then cap the stored value at 200. When resources are disabled, the inspected getter reports 200. A +10 Energy request is not automatically ten percent of the bar or a guaranteed final increase.
- Lunacrike changes velocity, and Trilliad Leaves uses raw Jump Boost amplifier 128. Validate movement, saving/synchronization and interaction with other effects before claiming restoration parity.
- The normal potion system decides whether a new effect combines with or replaces an existing one. These tables do not guarantee additive stacking or total healing over the entire duration.

## Evidence

- [Released methods, nineteen declarations and eighteen potion requests](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/special-food-effects-evidence-1.12.2.json). Effect identities are also checked against vanilla MobEffects registry strings and mappings.
- [Source portrait receipts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/special-food-art-evidence-1.12.2.json).
- Original assets and mechanics by Tslat and AoA contributors; vanilla effect mapping by Mojang. No game or mod code was executed.
