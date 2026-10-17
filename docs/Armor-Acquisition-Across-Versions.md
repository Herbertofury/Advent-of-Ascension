# Armor acquisition across versions

**Which older release supplies the missing acquisition design?** This comparison follows the **204 armor identities registered in the inspected 1.21.1 release** back through exact recipe outputs and explicit item loot entries in 1.12.2, 1.16.5 and 1.20.1. It is a restoration map, not advice to combine incompatible JARs.

[Modern acquisition ledger](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1) · [Armor Atelier](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

## The useful result

Of the **141 modern items without a route in the selected modern source categories**, historical recipe/loot references cover:

| Inspected release | Historical references for modern unresolved items | All matching modern armor identities |
|---|---:|---:|
| Minecraft 1.12.2 / AoA 3.3.6 | 124 / 141 | 177 / 204 |
| Minecraft 1.16.5 / AoA 3.6.11 | 128 / 141 | 180 / 204 |
| Minecraft 1.20.1 / AoA 3.7.1 | 99 / 141 | 147 / 204 |

The three historical scans together identify routes for **128 of those 141**. This makes **1.16.5 / AoA 3.6.11 a particularly useful armor-acquisition reference**, while the newer target still supplies its own registration, mechanics and loader contracts. A retained old loot table does not establish that its old mob still spawns in a newer release.

## What the modern release explicitly labels

The released `UnobtainableItems.CURRENT_SET` contains **92 armor items**. Its memoized supplier resolves the listed item holders; the normal AoA creative-tab collector filters out members of that set. Those same 92 armor identities also occur in the checked recipe-viewer hiding tag.

This is stronger evidence of upstream intent than a missing recipe search alone. It still does not prevent commands, custom datapacks or other mods from supplying an item, and it does not certify what a private Enderloom build does. The other **49** of the 141 selected-route gaps are not automatically assigned that upstream label.

## Use this as a restoration checklist

1. Choose a target armor set below and open its historical item records. Preserve the target registry IDs and existing saves.
2. Identify the entire acquisition dependency: recipe ingredients and station, or mob/boss plus dimension, structure and loot conditions.
3. Rebuild the route using the target loader and schemas. Do not copy a 1.12.2 assets-path recipe or a legacy loot function verbatim into 1.21.1.
4. Preserve branching semantics. A multi-entry full-set reward, a one-piece weighted pool and a random station output are different systems.
5. Check balance against the target armor effects, skills and resource costs; historical statistics and textures are not assumed identical.
6. Validate copied saves, recipes, spawn conditions, multiplayer and performance before changing a restoration status to implemented or tested.

## Read the release columns

- Counts show pieces with an exact selected recipe or item-loot reference, not a guarantee of obtaining the set.
- Source names below are resource basenames; the evidence file retains full paths, original JSON and hashes.
- The only cross-release registry alias used is legacy `_legs` → modern `_leggings`. No fuzzy-name match silently substitutes another item.
- The 1.12.2 inventory browser uses localization-key records. Its links are resolved through pinned registration title/base pairs and slot suffixes, while original loot/recipe IDs remain in the evidence. Old Boot is a hidden SimpleItem in that older source, so a same-ID reference does not imply the modern boots-slot behavior.
- Pictures show the **modern target set**. Historical item links open the corresponding historical inventory records; the modern picture is not presented as a legacy render.

## Ordinary armor sets

### Alacrity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-alacrity-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Alacrity target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#alacrity).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `alacrity_boots.json`<br>`alacrity_chestplate.json`<br>`alacrity_helmet.json`<br>`alacrity_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AlacrityHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AlacrityChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AlacrityLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AlacrityBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_alacrity_boots.json`<br>`infusion_alacrity_chestplate.json`<br>`infusion_alacrity_helmet.json`<br>`infusion_alacrity_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aalacrity_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aalacrity_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aalacrity_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aalacrity_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_alacrity_boots.json`<br>`infusion_alacrity_chestplate.json`<br>`infusion_alacrity_helmet.json`<br>`infusion_alacrity_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aalacrity_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aalacrity_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aalacrity_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aalacrity_boots) |

### Archaic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-archaic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Archaic target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#archaic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `flash.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ArchaicHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ArchaicChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ArchaicLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ArchaicBoots.name) |
| 1.16.5 | 4/4 | loot, recipe | `flash.json`<br>`upgrade_kit_archaic_boots.json`<br>`upgrade_kit_archaic_chestplate.json`<br>`upgrade_kit_archaic_helmet.json`<br>`upgrade_kit_archaic_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aarchaic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aarchaic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aarchaic_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aarchaic_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Baron

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-baron-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Baron target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#baron).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `hive_king.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronBoots.name) |
| 1.16.5 | 4/4 | loot | `hive_king.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abaron_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abaron_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abaron_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abaron_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Battleborn

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-battleborn-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Battleborn target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#battleborn).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `battleborn_boots.json`<br>`battleborn_chestplate.json`<br>`battleborn_helmet.json`<br>`battleborn_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BattlebornHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BattlebornChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BattlebornLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BattlebornBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_battleborn_boots.json`<br>`infusion_battleborn_chestplate.json`<br>`infusion_battleborn_helmet.json`<br>`infusion_battleborn_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abattleborn_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abattleborn_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abattleborn_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abattleborn_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_battleborn_boots.json`<br>`infusion_battleborn_chestplate.json`<br>`infusion_battleborn_helmet.json`<br>`infusion_battleborn_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abattleborn_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abattleborn_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abattleborn_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abattleborn_boots) |

### Biogenic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-biogenic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Biogenic target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#biogenic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `elder_guardian_drops.json`<br>`guardian_drops.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BiogenicHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BiogenicChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BiogenicLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BiogenicBoots.name) |
| 1.16.5 | 4/4 | loot | `elder_guardian.json`<br>`guardian.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abiogenic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abiogenic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abiogenic_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abiogenic_boots) |
| 1.20.1 | 4/4 | loot | `elder_guardian.json`<br>`guardian.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abiogenic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abiogenic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abiogenic_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abiogenic_boots) |

### Boreic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-boreic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Boreic target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#boreic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `boreic_boots.json`<br>`boreic_chestplate.json`<br>`boreic_helmet.json`<br>`boreic_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreicHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreicChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreicLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreicBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_boreic_boots.json`<br>`infusion_boreic_chestplate.json`<br>`infusion_boreic_helmet.json`<br>`infusion_boreic_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aboreic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aboreic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aboreic_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aboreic_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_boreic_boots.json`<br>`infusion_boreic_chestplate.json`<br>`infusion_boreic_helmet.json`<br>`infusion_boreic_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aboreic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aboreic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aboreic_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aboreic_boots) |

### Candy

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-candy-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Candy target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#candy).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `cotton_candor.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyBoots.name) |
| 1.16.5 | 4/4 | loot | `cotton_candor.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acandy_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acandy_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acandy_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acandy_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Commander

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-commander-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Commander target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#commander).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `blue_rune_templar.json`<br>`green_rune_templar.json`<br>`red_rune_templar.json`<br>`yellow_rune_templar.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CommanderHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CommanderChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CommanderLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CommanderBoots.name) |
| 1.16.5 | 4/4 | loot | `blue_rune_templar.json`<br>`green_rune_templar.json`<br>`red_rune_templar.json`<br>`yellow_rune_templar.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acommander_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acommander_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acommander_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acommander_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Crystallis

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-crystallis-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Crystallis target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#crystallis).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `crystallis_boots.json`<br>`crystallis_chestplate.json`<br>`crystallis_helmet.json`<br>`crystallis_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystallisHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystallisChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystallisLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystallisBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_crystallis_boots.json`<br>`infusion_crystallis_chestplate.json`<br>`infusion_crystallis_helmet.json`<br>`infusion_crystallis_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acrystallis_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acrystallis_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acrystallis_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acrystallis_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_crystallis_boots.json`<br>`infusion_crystallis_chestplate.json`<br>`infusion_crystallis_helmet.json`<br>`infusion_crystallis_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acrystallis_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acrystallis_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acrystallis_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acrystallis_boots) |

### Elecanyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-elecanyte-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Elecanyte target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#elecanyte).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `elecanyte_boots.json`<br>`elecanyte_chestplate.json`<br>`elecanyte_helmet.json`<br>`elecanyte_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ElecanyteHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ElecanyteChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ElecanyteLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ElecanyteBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_elecanyte_boots.json`<br>`infusion_elecanyte_chestplate.json`<br>`infusion_elecanyte_helmet.json`<br>`infusion_elecanyte_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aelecanyte_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aelecanyte_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aelecanyte_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aelecanyte_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_elecanyte_boots.json`<br>`infusion_elecanyte_chestplate.json`<br>`infusion_elecanyte_helmet.json`<br>`infusion_elecanyte_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aelecanyte_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aelecanyte_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aelecanyte_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aelecanyte_boots) |

### Embrodium

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-embrodium-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Embrodium target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#embrodium).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `embrodium_boots.json`<br>`embrodium_chestplate.json`<br>`embrodium_helmet.json`<br>`embrodium_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EmbrodiumHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EmbrodiumChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EmbrodiumLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EmbrodiumBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_embrodium_boots.json`<br>`infusion_embrodium_chestplate.json`<br>`infusion_embrodium_helmet.json`<br>`infusion_embrodium_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aembrodium_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aembrodium_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aembrodium_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aembrodium_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_embrodium_boots.json`<br>`infusion_embrodium_chestplate.json`<br>`infusion_embrodium_helmet.json`<br>`infusion_embrodium_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aembrodium_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aembrodium_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aembrodium_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aembrodium_boots) |

### Exoplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-exoplate-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Exoplate target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#exoplate).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `exoplate_boots.json`<br>`exoplate_chestplate.json`<br>`exoplate_helmet.json`<br>`exoplate_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExoplateHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExoplateChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExoplateLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExoplateBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_exoplate_boots.json`<br>`infusion_exoplate_chestplate.json`<br>`infusion_exoplate_helmet.json`<br>`infusion_exoplate_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexoplate_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexoplate_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexoplate_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexoplate_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_exoplate_boots.json`<br>`infusion_exoplate_chestplate.json`<br>`infusion_exoplate_helmet.json`<br>`infusion_exoplate_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexoplate_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexoplate_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexoplate_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexoplate_boots) |

### Explosive

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-explosive-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Explosive target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#explosive).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `king_bambambam.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveBoots.name) |
| 1.16.5 | 4/4 | loot | `king_bambambam.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexplosive_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexplosive_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexplosive_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexplosive_boots) |
| 1.20.1 | 4/4 | loot | `king_bambambam.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexplosive_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexplosive_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexplosive_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexplosive_boots) |

### Fungal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-fungal-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Fungal target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#fungal).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `fungal_boots.json`<br>`fungal_chestplate.json`<br>`fungal_helmet.json`<br>`fungal_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FungalHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FungalChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FungalLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FungalBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_fungal_boots.json`<br>`infusion_fungal_chestplate.json`<br>`infusion_fungal_helmet.json`<br>`infusion_fungal_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Afungal_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Afungal_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Afungal_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Afungal_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_fungal_boots.json`<br>`infusion_fungal_chestplate.json`<br>`infusion_fungal_helmet.json`<br>`infusion_fungal_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Afungal_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Afungal_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Afungal_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Afungal_boots) |

### Ghastly

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghastly-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Ghastly target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#ghastly).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `ghastly_boots.json`<br>`ghastly_chestplate.json`<br>`ghastly_helmet.json`<br>`ghastly_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhastlyHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhastlyChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhastlyLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhastlyBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_ghastly_boots.json`<br>`infusion_ghastly_chestplate.json`<br>`infusion_ghastly_helmet.json`<br>`infusion_ghastly_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghastly_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghastly_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghastly_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghastly_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_ghastly_boots.json`<br>`infusion_ghastly_chestplate.json`<br>`infusion_ghastly_helmet.json`<br>`infusion_ghastly_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghastly_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghastly_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghastly_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghastly_boots) |

### Ghoulish

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghoulish-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Ghoulish target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#ghoulish).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `ghoulish_boots.json`<br>`ghoulish_chestplate.json`<br>`ghoulish_helmet.json`<br>`ghoulish_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhoulishHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhoulishChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhoulishLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhoulishBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_ghoulish_boots.json`<br>`infusion_ghoulish_chestplate.json`<br>`infusion_ghoulish_helmet.json`<br>`infusion_ghoulish_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghoulish_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghoulish_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghoulish_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aghoulish_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_ghoulish_boots.json`<br>`infusion_ghoulish_chestplate.json`<br>`infusion_ghoulish_helmet.json`<br>`infusion_ghoulish_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghoulish_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghoulish_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghoulish_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aghoulish_boots) |

### Hazmat

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hazmat-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Hazmat target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#hazmat).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `hazmat_boots.json`<br>`hazmat_chestplate.json`<br>`hazmat_helmet.json`<br>`hazmat_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HazmatHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HazmatChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HazmatLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HazmatBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_hazmat_boots.json`<br>`infusion_hazmat_chestplate.json`<br>`infusion_hazmat_helmet.json`<br>`infusion_hazmat_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahazmat_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahazmat_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahazmat_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahazmat_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_hazmat_boots.json`<br>`infusion_hazmat_chestplate.json`<br>`infusion_hazmat_helmet.json`<br>`infusion_hazmat_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ahazmat_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ahazmat_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ahazmat_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ahazmat_boots) |

### Hydrangic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydrangic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Hydrangic target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#hydrangic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 0/4 | No selected reference | — | — |
| 1.16.5 | 0/4 | No selected reference | — | — |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Hydroplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydroplate-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Hydroplate target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#hydroplate).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `hydrolisk.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HydroplateHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HydroplateChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HydroplateLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HydroplateBoots.name) |
| 1.16.5 | 4/4 | loot | `dracyon.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahydroplate_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahydroplate_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahydroplate_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahydroplate_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Ice

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ice-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Ice target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#ice).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `ice_boots.json`<br>`ice_chestplate.json`<br>`ice_helmet.json`<br>`ice_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IceHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IceChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IceLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IceBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_ice_boots.json`<br>`infusion_ice_chestplate.json`<br>`infusion_ice_helmet.json`<br>`infusion_ice_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aice_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aice_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aice_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aice_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_ice_boots.json`<br>`infusion_ice_chestplate.json`<br>`infusion_ice_helmet.json`<br>`infusion_ice_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aice_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aice_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aice_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aice_boots) |

### Infernal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-infernal-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Infernal target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#infernal).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `infernal_boots.json`<br>`infernal_chestplate.json`<br>`infernal_helmet.json`<br>`infernal_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.InfernalHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.InfernalChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.InfernalLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.InfernalBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_infernal_boots.json`<br>`infusion_infernal_chestplate.json`<br>`infusion_infernal_helmet.json`<br>`infusion_infernal_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ainfernal_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ainfernal_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ainfernal_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ainfernal_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_infernal_boots.json`<br>`infusion_infernal_chestplate.json`<br>`infusion_infernal_helmet.json`<br>`infusion_infernal_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ainfernal_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ainfernal_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ainfernal_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ainfernal_boots) |

### Knight

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-knight-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Knight target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#knight).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `knight_boots.json`<br>`knight_chestplate.json`<br>`knight_helmet.json`<br>`knight_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KnightHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KnightChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KnightLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KnightBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_knight_boots.json`<br>`infusion_knight_chestplate.json`<br>`infusion_knight_helmet.json`<br>`infusion_knight_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aknight_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aknight_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aknight_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aknight_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_knight_boots.json`<br>`infusion_knight_chestplate.json`<br>`infusion_knight_helmet.json`<br>`infusion_knight_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aknight_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aknight_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aknight_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aknight_boots) |

### Lunar

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lunar-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Lunar target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#lunar).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 0/4 | No selected reference | — | — |
| 1.16.5 | 4/4 | recipe | `infusion_lunar_boots.json`<br>`infusion_lunar_chestplate.json`<br>`infusion_lunar_helmet.json`<br>`infusion_lunar_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alunar_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alunar_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alunar_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alunar_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_lunar_boots.json`<br>`infusion_lunar_chestplate.json`<br>`infusion_lunar_helmet.json`<br>`infusion_lunar_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alunar_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alunar_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alunar_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alunar_boots) |

### Lyndamyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyndamyte-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Lyndamyte target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#lyndamyte).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `lyndamyte_boots.json`<br>`lyndamyte_chestplate.json`<br>`lyndamyte_helmet.json`<br>`lyndamyte_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyndamyteHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyndamyteChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyndamyteLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyndamyteBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_lyndamyte_boots.json`<br>`infusion_lyndamyte_chestplate.json`<br>`infusion_lyndamyte_helmet.json`<br>`infusion_lyndamyte_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyndamyte_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyndamyte_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyndamyte_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyndamyte_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_lyndamyte_boots.json`<br>`infusion_lyndamyte_chestplate.json`<br>`infusion_lyndamyte_helmet.json`<br>`infusion_lyndamyte_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyndamyte_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyndamyte_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyndamyte_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyndamyte_boots) |

### Lyonic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyonic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Lyonic target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#lyonic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `lyonic_boots.json`<br>`lyonic_chestplate.json`<br>`lyonic_helmet.json`<br>`lyonic_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_lyonic_boots.json`<br>`infusion_lyonic_chestplate.json`<br>`infusion_lyonic_helmet.json`<br>`infusion_lyonic_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyonic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyonic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyonic_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alyonic_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_lyonic_boots.json`<br>`infusion_lyonic_chestplate.json`<br>`infusion_lyonic_helmet.json`<br>`infusion_lyonic_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyonic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyonic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyonic_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alyonic_boots) |

### Mercurial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-mercurial-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Mercurial target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#mercurial).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `mercurial_boots.json`<br>`mercurial_chestplate.json`<br>`mercurial_helmet.json`<br>`mercurial_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MercurialHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MercurialChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MercurialLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MercurialBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_mercurial_boots.json`<br>`infusion_mercurial_chestplate.json`<br>`infusion_mercurial_helmet.json`<br>`infusion_mercurial_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Amercurial_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Amercurial_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Amercurial_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Amercurial_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_mercurial_boots.json`<br>`infusion_mercurial_chestplate.json`<br>`infusion_mercurial_helmet.json`<br>`infusion_mercurial_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Amercurial_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Amercurial_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Amercurial_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Amercurial_boots) |

### Necro

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-necro-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Necro target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#necro).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `faceless_floater.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NecroHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NecroChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NecroLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NecroBoots.name) |
| 1.16.5 | 4/4 | loot | `faceless_floater.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anecro_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anecro_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anecro_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anecro_boots) |
| 1.20.1 | 4/4 | loot | `faceless_floater.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anecro_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anecro_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anecro_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anecro_boots) |

### Nethengeic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nethengeic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Nethengeic target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#nethengeic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `nethengeic_beast.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethengeicHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethengeicChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethengeicLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethengeicBoots.name) |
| 1.16.5 | 4/4 | loot | `nethengeic_beast.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anethengeic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anethengeic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anethengeic_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anethengeic_boots) |
| 1.20.1 | 4/4 | loot | `nethengeic_beast.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anethengeic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anethengeic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anethengeic_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anethengeic_boots) |

### Nightmare

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nightmare-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Nightmare target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#nightmare).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `nightmare_boots.json`<br>`nightmare_chestplate.json`<br>`nightmare_helmet.json`<br>`nightmare_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_nightmare_boots.json`<br>`infusion_nightmare_chestplate.json`<br>`infusion_nightmare_helmet.json`<br>`infusion_nightmare_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anightmare_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anightmare_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anightmare_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anightmare_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_nightmare_boots.json`<br>`infusion_nightmare_chestplate.json`<br>`infusion_nightmare_helmet.json`<br>`infusion_nightmare_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anightmare_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anightmare_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anightmare_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anightmare_boots) |

### Omni

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-omni-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Omni target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#omni).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 0/4 | No selected reference | — | — |
| 1.16.5 | 0/4 | No selected reference | — | — |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Phantasm

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-phantasm-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Phantasm target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#phantasm).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 0/4 | No selected reference | — | — |
| 1.16.5 | 0/4 | No selected reference | — | — |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Poison

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-poison-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Poison target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#poison).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `poison_boots.json`<br>`poison_chestplate.json`<br>`poison_helmet.json`<br>`poison_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_poison_boots.json`<br>`infusion_poison_chestplate.json`<br>`infusion_poison_helmet.json`<br>`infusion_poison_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apoison_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apoison_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apoison_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apoison_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_poison_boots.json`<br>`infusion_poison_chestplate.json`<br>`infusion_poison_helmet.json`<br>`infusion_poison_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apoison_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apoison_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apoison_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apoison_boots) |

### Predatious

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-predatious-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Predatious target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#predatious).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `tyrosaur.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PredatiousHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PredatiousChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PredatiousLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PredatiousBoots.name) |
| 1.16.5 | 4/4 | loot | `tyrosaur.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apredatious_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apredatious_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apredatious_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apredatious_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Primordial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-primordial-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Primordial target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#primordial).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 0/4 | No selected reference | — | — |
| 1.16.5 | 0/4 | No selected reference | — | — |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Purity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-purity-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Purity target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#purity).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `purity_boots.json`<br>`purity_chestplate.json`<br>`purity_helmet.json`<br>`purity_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_purity_boots.json`<br>`infusion_purity_chestplate.json`<br>`infusion_purity_helmet.json`<br>`infusion_purity_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apurity_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apurity_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apurity_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apurity_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_purity_boots.json`<br>`infusion_purity_chestplate.json`<br>`infusion_purity_helmet.json`<br>`infusion_purity_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apurity_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apurity_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apurity_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apurity_boots) |

### Rockbone

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rockbone-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Rockbone target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#rockbone).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `rockbone_boots.json`<br>`rockbone_chestplate.json`<br>`rockbone_helmet.json`<br>`rockbone_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RockboneHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RockboneChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RockboneLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RockboneBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_rockbone_boots.json`<br>`infusion_rockbone_chestplate.json`<br>`infusion_rockbone_helmet.json`<br>`infusion_rockbone_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arockbone_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arockbone_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arockbone_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arockbone_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_rockbone_boots.json`<br>`infusion_rockbone_chestplate.json`<br>`infusion_rockbone_helmet.json`<br>`infusion_rockbone_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arockbone_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arockbone_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arockbone_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arockbone_boots) |

### Rosidian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rosidian-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Rosidian target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#rosidian).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `rosidian_boots.json`<br>`rosidian_chestplate.json`<br>`rosidian_helmet.json`<br>`rosidian_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_rosidian_boots.json`<br>`infusion_rosidian_chestplate.json`<br>`infusion_rosidian_helmet.json`<br>`infusion_rosidian_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arosidian_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arosidian_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arosidian_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arosidian_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_rosidian_boots.json`<br>`infusion_rosidian_chestplate.json`<br>`infusion_rosidian_helmet.json`<br>`infusion_rosidian_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arosidian_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arosidian_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arosidian_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arosidian_boots) |

### Runic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-runic-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Runic target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#runic).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `clunkhead.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicBoots.name) |
| 1.16.5 | 4/4 | loot | `clunkhead.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arunic_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arunic_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arunic_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arunic_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Sharpshot

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-sharpshot-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Sharpshot target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#sharpshot).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `sharpshot_boots.json`<br>`sharpshot_chestplate.json`<br>`sharpshot_helmet.json`<br>`sharpshot_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SharpshotHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SharpshotChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SharpshotLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SharpshotBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_sharpshot_boots.json`<br>`infusion_sharpshot_chestplate.json`<br>`infusion_sharpshot_helmet.json`<br>`infusion_sharpshot_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asharpshot_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asharpshot_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asharpshot_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asharpshot_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_sharpshot_boots.json`<br>`infusion_sharpshot_chestplate.json`<br>`infusion_sharpshot_helmet.json`<br>`infusion_sharpshot_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asharpshot_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asharpshot_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asharpshot_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asharpshot_boots) |

### Skeletal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-skeletal-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Skeletal target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#skeletal).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `skeletal_boots.json`<br>`skeletal_chestplate.json`<br>`skeletal_helmet.json`<br>`skeletal_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_skeletal_boots.json`<br>`infusion_skeletal_chestplate.json`<br>`infusion_skeletal_helmet.json`<br>`infusion_skeletal_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askeletal_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askeletal_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askeletal_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askeletal_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_skeletal_boots.json`<br>`infusion_skeletal_chestplate.json`<br>`infusion_skeletal_helmet.json`<br>`infusion_skeletal_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askeletal_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askeletal_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askeletal_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askeletal_boots) |

### Spaceking

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-spaceking-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Spaceking target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#spaceking).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `spaceking_boots.json`<br>`spaceking_chestplate.json`<br>`spaceking_helmet.json`<br>`spaceking_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpacekingHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpacekingChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpacekingLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpacekingBoots.name) |
| 1.16.5 | 4/4 | loot | `visualent.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspaceking_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspaceking_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspaceking_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspaceking_boots) |
| 1.20.1 | 0/4 | No selected reference | — | — |

### Speed

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-speed-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Speed target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#speed).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `speed_boots.json`<br>`speed_chestplate.json`<br>`speed_helmet.json`<br>`speed_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpeedHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpeedChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpeedLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpeedBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_speed_boots.json`<br>`infusion_speed_chestplate.json`<br>`infusion_speed_helmet.json`<br>`infusion_speed_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspeed_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspeed_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspeed_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspeed_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_speed_boots.json`<br>`infusion_speed_chestplate.json`<br>`infusion_speed_helmet.json`<br>`infusion_speed_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspeed_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspeed_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspeed_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspeed_boots) |

### Subterranean

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-subterranean-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Subterranean target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#subterranean).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `subterranean_boots.json`<br>`subterranean_chestplate.json`<br>`subterranean_helmet.json`<br>`subterranean_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SubterraneanHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SubterraneanChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SubterraneanLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SubterraneanBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_subterranean_boots.json`<br>`infusion_subterranean_chestplate.json`<br>`infusion_subterranean_helmet.json`<br>`infusion_subterranean_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asubterranean_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asubterranean_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asubterranean_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asubterranean_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_subterranean_boots.json`<br>`infusion_subterranean_chestplate.json`<br>`infusion_subterranean_helmet.json`<br>`infusion_subterranean_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asubterranean_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asubterranean_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asubterranean_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asubterranean_boots) |

### Utopian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-utopian-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Utopian target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#utopian).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `treasure_box.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UtopianHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UtopianChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UtopianLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UtopianBoots.name) |
| 1.16.5 | 4/4 | loot | `treasure_box.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Autopian_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Autopian_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Autopian_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Autopian_boots) |
| 1.20.1 | 4/4 | loot | `treasure_box.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Autopian_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Autopian_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Autopian_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Autopian_boots) |

### Void

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-void-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Void target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#void).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `void_boots.json`<br>`void_chestplate.json`<br>`void_helmet.json`<br>`void_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoidHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoidChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoidLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoidBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_void_boots.json`<br>`infusion_void_chestplate.json`<br>`infusion_void_helmet.json`<br>`infusion_void_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Avoid_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Avoid_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Avoid_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Avoid_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_void_boots.json`<br>`infusion_void_chestplate.json`<br>`infusion_void_helmet.json`<br>`infusion_void_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Avoid_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Avoid_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Avoid_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Avoid_boots) |

### Weaken

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-weaken-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Weaken target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **4/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#weaken).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `weaken_boots.json`<br>`weaken_chestplate.json`<br>`weaken_helmet.json`<br>`weaken_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakenHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakenChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakenLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakenBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_weaken_boots.json`<br>`infusion_weaken_chestplate.json`<br>`infusion_weaken_helmet.json`<br>`infusion_weaken_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aweaken_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aweaken_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aweaken_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aweaken_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_weaken_boots.json`<br>`infusion_weaken_chestplate.json`<br>`infusion_weaken_helmet.json`<br>`infusion_weaken_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aweaken_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aweaken_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aweaken_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aweaken_boots) |

### Wither

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-wither-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Wither target-set study">

Modern selected-route coverage: **4/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#wither).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | recipe | `wither_boots.json`<br>`wither_chestplate.json`<br>`wither_helmet.json`<br>`wither_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherBoots.name) |
| 1.16.5 | 4/4 | recipe | `infusion_wither_boots.json`<br>`infusion_wither_chestplate.json`<br>`infusion_wither_helmet.json`<br>`infusion_wither_legs.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Awither_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Awither_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Awither_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Awither_boots) |
| 1.20.1 | 4/4 | recipe | `infusion_wither_boots.json`<br>`infusion_wither_chestplate.json`<br>`infusion_wither_helmet.json`<br>`infusion_wither_leggings.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Awither_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Awither_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Awither_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Awither_boots) |

### Zargonite

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-zargonite-1.21.1.webp" width="180" height="180" alt="Modern 1.21.1 Zargonite target-set study">

Modern selected-route coverage: **0/4**. Upstream current-set classification: **0/4 listed**. [Current route notes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#zargonite).

| Release | Pieces | Reference kind | Resource names | Historical item records |
|---|---:|---|---|---|
| 1.12.2 | 4/4 | loot | `zarg.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ZargoniteHelmet.name) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ZargoniteChestplate.name) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ZargoniteLegs.name) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ZargoniteBoots.name) |
| 1.16.5 | 4/4 | loot | `zarg.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Azargonite_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Azargonite_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Azargonite_legs) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Azargonite_boots) |
| 1.20.1 | 4/4 | loot | `zarg.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Azargonite_helmet) · [chestplate](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Azargonite_chestplate) · [leggings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Azargonite_leggings) · [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Azargonite_boots) |

## Individual helmets and Old Boot

[Modern special-piece model studies](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Armor-and-Skill-Helmets-1.21.1).

### Achelos Helmet

Modern selected route: **unresolved in selected categories**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 1/1 | loot | `corallus.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AchelosHelmet.name) |
| 1.16.5 | 1/1 | loot | `corallus.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aachelos_helmet) |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Oceanus Helmet

Modern selected route: **unresolved in selected categories**. Upstream current-set member: **yes**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 1/1 | loot | `corallus.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.OceanusHelmet.name) |
| 1.16.5 | 1/1 | recipe | `infusion_oceanus_helmet.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aoceanus_helmet) |
| 1.20.1 | 1/1 | recipe | `infusion_oceanus_helmet.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aoceanus_helmet) |

### Sealord Helmet

Modern selected route: **unresolved in selected categories**. Upstream current-set member: **yes**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 1/1 | loot | `dracyon.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SealordHelmet.name) |
| 1.16.5 | 1/1 | recipe | `infusion_sealord_helmet.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asealord_helmet) |
| 1.20.1 | 1/1 | recipe | `infusion_sealord_helmet.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asealord_helmet) |

### Face Mask

Modern selected route: **unresolved in selected categories**. Upstream current-set member: **yes**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 1/1 | recipe | `face_mask.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FaceMask.name) |
| 1.16.5 | 1/1 | recipe | `infusion_face_mask.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aface_mask) |
| 1.20.1 | 1/1 | recipe | `infusion_face_mask.json` | [helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aface_mask) |

### Chroma Goggles

Modern selected route: **unresolved in selected categories**. Upstream current-set member: **yes**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Helm of the Dextrous

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Helm of the Dryad

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Helm of the Ritualist

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Helm of the Trawler

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Helm of the Treasurer

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Helm of the Warrior

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 0/1 | No selected reference | — | — |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

### Old Boot

Modern selected route: **present**. Upstream current-set member: **no**.

| Release | Pieces | Reference kind | Resource names | Historical item record |
|---|---:|---|---|---|
| 1.12.2 | 1/1 | loot | `treasure.json` | [boots](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.OldBoot.name) |
| 1.16.5 | 0/1 | No selected reference | — | — |
| 1.20.1 | 0/1 | No selected reference | — | — |

## Still unresolved after these three historical scans

**Chroma Goggles and all four pieces each of Omni, Phantasm and Primordial armor** have no selected direct recipe/loot reference in these scans. They need separate code-driven, trader, station or historical-design research. This is not a universal claim that they were impossible to obtain.

Minecraft 1.7.10 is not silently substituted: this comparison has no equivalent checked authentic artifact/resource pass for that release.

## Reproducible evidence

[Cross-version routes, original resources and current-set membership](https://herbertofury.github.io/Advent-of-Ascension/armor-version-acquisition-evidence.json). Released archives were read statically; no game or Java/mod code was executed.

AoA content and artwork: Tslat and contributors. Modern neutral armor mesh reference: Mojang/Microsoft. Original comparison and documentation tooling.
