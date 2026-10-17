# Finding seeds and starting a farm · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** This route index covers the sixteen planting items used by the historical crop system. It finds references for fifteen in the scanned recipes, loot tables, trades and selected callbacks. **Thorny Plant Seeds remain unresolved in this bounded audit**; that is not a claim they are impossible to obtain.

## Choose a practical route

- **Already have Heart Fruit or Magic Marang?** One Heart Fruit has a shapeless recipe yielding **three Heart Fruit Seeds**; one Magic Marang yields **two Magic Marang Seeds**. These are reproduction routes once you have the produce, not proof of the first wild source.
- **Shopping for lunar crops?** The Zal Herbalist has separate candidate offers for Lunacrike, Luna Globe and Lunalon Seeds: **five Silver Coins for five seeds** per offer. Generated selection and stock handling still follow the [historical trading rules](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trading-and-Traders-1.12.2).
- **Harvesting wild plants?** The checked selectors connect Red Waterweeds to Floracle Seeds, Tangle Thorns to Heart Fruit Seeds, Trilliad Bloom to Trilliad Seeds, and Bulb Stock Cap to Eye Bulb. Quantity callbacks and external harvest handling matter; see the probability section.
- **Starting Goldicaps?** The Garden Castle builder places six mature Goldicaps crop blocks. Its local positions are (9,5,17), (9,5,18), (9,5,19), (24,5,17), (24,5,18), (24,5,19), relative to that structure. These are blueprint coordinates, not global world coordinates or a promise that a castle exists nearby. Harvesting uses the crop behavior documented separately.
- **Checking loot?** Read the exact table name and its conditions below. A world loot table is a referenced resource, not proof that every creature in that dimension drops the item.

## Illustrated planting-item directory

The portraits are exact crops of the already-published 1.12.2 source-model atlas. They represent the planting items, not the separate age-state world blocks.

| Planting item | Checked acquisition references |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-bubble_berry_seeds.webp" width="72" height="72" alt="Bubble Berry Seeds"><br>[Bubble Berry Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BubbleBerrySeeds.name) | Loot resource: `structures/aquaticcastle/general`.<br>Loot resource: `worlds/lborean`. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-chilli_seeds.webp" width="72" height="72" alt="Chilli Seeds"><br>[Chilli Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ChilliSeeds.name) | Loot resource: `worlds/gardencia`. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-eye_bulb.webp" width="72" height="72" alt="Eye Bulb"><br>[Eye Bulb](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EyeBulb.name) | Local quantity returns 1; selector returns Eye Bulb, which is also its planting item. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-floracle_seeds.webp" width="72" height="72" alt="Floracle Seeds"><br>[Floracle Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FloracleSeeds.name) | State-aware quantity predicate nextInt(max(1,5-Fortune))==0 returns 1, otherwise 0; selector returns Floracle Seeds. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-goldicap_seeds.webp" width="72" height="72" alt="Goldicap Seeds"><br>[Goldicap Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoldicapSeeds.name) | GardenCastle builder places six Goldicaps crop states; static initializer assigns age7. Finding a generated castle and final hook outcomes require separate verification. Harvest links to the checked crop seed loop. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-heart_fruit_seeds.webp" width="72" height="72" alt="Heart Fruit Seeds"><br>[Heart Fruit Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HeartFruitSeeds.name) | Recipe: heart_fruit → 3 seeds.<br>Local quantity predicate nextInt(20)==0 returns 1, otherwise 0; item selector returns Heart Fruit Seeds. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-holly_top_seeds.webp" width="72" height="72" alt="Holly Top Seeds"><br>[Holly Top Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HollyTopSeeds.name) | Loot resource: `misc/generic_chest_loot`.<br>Loot resource: `worlds/overworld`. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-luna_globe_seeds.webp" width="72" height="72" alt="Luna Globe Seeds"><br>[Luna Globe Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunaGlobeSeeds.name) | Zal Herbalist: 5 Silver Coin → 5 seeds. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-lunacrike_seeds.webp" width="72" height="72" alt="Lunacrike Seeds"><br>[Lunacrike Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunacrikeSeeds.name) | Zal Herbalist: 5 Silver Coin → 5 seeds. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-lunalon_seeds.webp" width="72" height="72" alt="Lunalon Seeds"><br>[Lunalon Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunalonSeeds.name) | Zal Herbalist: 5 Silver Coin → 5 seeds. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-magic_marang_seeds.webp" width="72" height="72" alt="Magic Marang Seeds"><br>[Magic Marang Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MagicMarangSeeds.name) | Recipe: magic_marang → 2 seeds.<br>Haunted Leaves only: nextBoolean() AND nextInt(50)<=Fortune selects Magic Marang Seeds. This is conditional on the selector being called; inherited leaf quantity/decay and harvesting paths remain separate. Shearing returns the leaf block. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-mystic_shrooms.webp" width="72" height="72" alt="Mystic Shrooms"><br>[Mystic Shrooms](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MysticShrooms.name) | Loot resource: `entities/bosses/king_shroomus`.<br>Loot resource: `entities/mobs/mysterium/fungung`.<br>Loot resource: `structures/hauntedcastle/top_floor`.<br>Loot resource: `worlds/mysterium`. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-rosidon_seeds.webp" width="72" height="72" alt="Rosidon Seeds"><br>[Rosidon Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidonSeeds.name) | Loot resource: `entities/mobs/gardencia/daysee`. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-tea_seeds.webp" width="72" height="72" alt="Tea Seeds"><br>[Tea Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TeaSeeds.name) | Loot resource: `misc/generic_chest_loot`.<br>Loot resource: `skills/logging/logging`.<br>Loot resource: `worlds/overworld`. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-thorny_plant_seeds.webp" width="72" height="72" alt="Thorny Plant Seeds"><br>[Thorny Plant Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ThornyPlantSeeds.name) | No first-acquisition route established by this scoped scan. Preserve as unresolved. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/planting-item-1.12.2-trilliad_seeds.webp" width="72" height="72" alt="Trilliad Seeds"><br>[Trilliad Seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TrilliadSeeds.name) | Local quantity returns 1; selector returns Trilliad Seeds. |

## Local drop calculations, without inflated odds

| Callback | Local result before other harvesting behavior |
|---|---|
| Tangle Thorns quantity | nextInt(20)==0 gives 1, otherwise 0: **1/20** in this local callback. |
| Red Waterweeds quantity | nextInt(max(1,5−Fortune))==0 gives 1. Fortune 0/1/2/3 gives **1/5,1/4,1/3,1/2** locally; Fortune 4+ reaches 1. Level 4 is an extended/modded boundary, not a claim about the ordinary enchantment cap. |
| Trilliad Bloom / Bulb Stock Cap quantity | The checked local quantity method returns 1. Other harvesting paths, tools and hooks can still change what arrives in inventory. |
| Haunted Leaves item selector | Only Haunted Leaves test nextBoolean() AND nextInt(50)≤Fortune for Magic Marang Seeds. Fortune 0 is **1/100 conditional on this selector being called**; this is not a per-leaf-break chance. Inherited leaf quantity/decay gates are separate. |

Shearing the checked LeavesBlock returns the leaf block itself. Do not tell players that harvesting leaves with shears is the same seed-selection route. Silk Touch and event/modpack interactions require the appropriate path to be checked as well.

## Loot evidence with context

The audit retains **thirteen matching item entries across eleven complete loot-table definitions**, including conditions, functions, rolls and competing entries. Weights are not percentages. Direct incoming table references are indexed where present, but this does not fully trace every root caller or generation hook.

| Planting item | Resource | Exact entry pointer | Direct parent-table references |
|---|---|---|---:|
| Bubble Berry Seeds | `structures/aquaticcastle/general.json` | `/pools/0/entries/10` | 0 |
| Bubble Berry Seeds | `worlds/lborean.json` | `/pools/1/entries/2` | 10 |
| Chilli Seeds | `worlds/gardencia.json` | `/pools/1/entries/2` | 11 |
| Holly Top Seeds | `misc/generic_chest_loot.json` | `/pools/0/entries/2` | 0 |
| Holly Top Seeds | `worlds/overworld.json` | `/pools/1/entries/4` | 95 |
| Mystic Shrooms | `entities/bosses/king_shroomus.json` | `/pools/1/entries/9` | 0 |
| Mystic Shrooms | `entities/mobs/mysterium/fungung.json` | `/pools/1/entries/1` | 0 |
| Mystic Shrooms | `structures/hauntedcastle/top_floor.json` | `/pools/0/entries/3` | 0 |
| Mystic Shrooms | `worlds/mysterium.json` | `/pools/1/entries/1` | 15 |
| Rosidon Seeds | `entities/mobs/gardencia/daysee.json` | `/pools/1/entries/1` | 0 |
| Tea Seeds | `misc/generic_chest_loot.json` | `/pools/0/entries/1` | 0 |
| Tea Seeds | `skills/logging/logging.json` | `/pools/0/entries/2` | 0 |
| Tea Seeds | `worlds/overworld.json` | `/pools/1/entries/3` | 95 |

### Chilli: a stale comment is not a drop route

A pinned source comment next to the Chilli crop declaration says its seeds drop in Lelyetia. The released JSON reference found in this scan is **worlds/gardencia.json**. The guide follows that actual resource evidence and does not promote the comment into a verified Lelyetia route. This identifies an evidence mismatch, not a live-world reproduction.

## Plant and harvest your new stock

Continue with [all sixteen crops and 128 growth stages](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2). Eye Bulb and Mystic Shrooms are both produce and planting items; the others use separate seeds. Mature right-click harvest resets age, and the extra-seed loop can fail, so maintain a reserve.

## Remaining work

- [ ] Trace a first-acquisition path for Thorny Plant Seeds beyond crop self-propagation and compatibility registrations.
- [ ] Trace every loot-table root caller, structure-generation gate and wild-plant biome placement before claiming guaranteed locations.
- [ ] Verify tool-sensitive harvesting, Forge event changes, actual stock availability, multiplayer and save/reload in the target game build.

## Source receipts

- [Recipes, full loot definitions, trader offers and released callback evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/seed-acquisition-evidence-1.12.2.json).
- [Planting-item portrait crop proof](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/seed-route-art-evidence-1.12.2.json).
- [Crop behavior and growth-state evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/crop-study-evidence-1.12.2.json).
- AoA artwork and systems: Tslat and contributors. Vanilla references: Mojang. Independent static documentation; no game execution or Enderloom runtime certification.
