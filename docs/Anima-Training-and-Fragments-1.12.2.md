# Historical Anima: harvesting, fragments and XP

**Minecraft 1.12.2 / AoA 3.3.6.** Harvest eligible plants, collect the short-lived Anima Stone entity, then decide whether to use its possible fragment for growth or save fragments for tablet crafting. The pickup and fragment-use XP calculations are different in the released code.

[Historical Extraction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2) · [Historical first expedition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Modern skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1)

![Historical Anima harvest, pickup and fragmented-stone loop](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/anima-training-loop-1.12.2.webp)

## 1. Harvest the right plant class

The selected `HarvestDropsEvent` handler rejects a missing harvester and Forge `FakePlayer`, then performs the Anima branch on the server. It matches Java block classes, not an unrestricted tag meaning “all plants.”

| Harvested block class | Extra condition | Random gate for an Anima Stone construction attempt |
|---|---|---|
| `BlockCrops` | Crop must be at maximum age | 1 in 6 |
| `BlockLeaves` | No crop-age check | 1 in 35 |
| `BlockFlower` | No crop-age check | 1 in 8 |
| `BlockVine` | No crop-age check | 1 in 8 |

A modded plant's appearance does not establish that it inherits one of these classes. The selected branch does not require a particular harvesting tool and does not explicitly exclude Silk Touch; other event handlers, harvesting rules and modpack changes still matter.

When its gate passes, the handler constructs an Anima Stone at the harvested block position and calls the world spawn method. It does not check the returned spawn result. These are random gates for **spawn attempts**, not a measured guaranteed rate of collectible stones.

For mature `BlockCrops` harvested during daytime, a separate branch requests +2 Selyan tribute and rolls a 1-in-2,000 Gardener item drop. That daytime branch does not limit the Anima gate to daytime. It has no explicit dimension-zero restriction in the selected code; tribute helpers and other configuration still apply.

## 2. Touch the stone before it expires

The Anima Stone is a temporary entity, not the Fragmented Anima Stone inventory item. Its server player-collision callback, while it is not dead:

1. Gets the colliding player's effective Anima level.
2. Requests Anima XP using the pickup expression below.
3. Plays the use sound and removes the entity.
4. Rolls `nextInt(3) == 0`; on that branch, gives or drops **one Fragmented Anima Stone** for that player.

The selected entity callback has no original-harvester ownership check. Do not assume only the player who harvested the plant can collect it.

Its update method removes it when `ticksExisted >= 200`. At the usual 20 ticks per second, 200 ticks correspond to roughly ten seconds, but lag and entity ticking make this a tick limit, not a promised wall-clock timer. Its custom NBT read/write methods are empty; this audit does not certify preservation of remaining lifetime across world/chunk reloads.

[Inspect the historical Anima Stone source-model portrait](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aanima_stone).

## 3. Choose growth or crafting for the fragment

### Growth use

The fragment first checks whether the player may edit the offset placement position, then calls Forge's bonemeal event hook. A nonzero hook result returns early: positive returns PASS, negative returns FAIL. The hook may involve other mods; this page does not assume what they do with the stack.

With the hook allowing the ordinary path, the clicked block must implement `IGrowable`. If it reports that it can grow and this is the server, the released branches are:

| Target class | Requested action |
|---|---|
| Sapling | Calls its tree-generation method |
| Crop | Sets its age directly to maximum |
| Cocoa | Sets cocoa age to 2 |
| Grass or double plant | At most one `grow` call while the original state remains |
| Other `IGrowable` | At most ten `grow` calls while the original state remains |

After that branch, the method requests Anima XP, plays the growth event and shrinks the fragment stack by one outside Creative. **It does not require a final successful plant-state change before XP and consumption.** A failed tree-generation attempt or a growth implementation that leaves the original state unchanged is therefore a useful regression case; do not promise every spent fragment visibly grows a plant.

An `IGrowable` target can return SUCCESS from the outer interaction even when no server growth branch ran. The action-result label alone is not proof that the item was spent, XP was granted or a crop changed.

### Additional acquisition

[Historical Logging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2#logging-reward-table) can select 1–2 fragments at effective Logging level 40, through its separate gate and loot-table branch.

Historical Extraction's loot table includes Fragmented Anima Stone at effective Extraction level **60**, count **1–4**, base weight **100**. That is one conditional entry after Extraction's separate success gate, not a guaranteed source every cycle. See the [complete Extraction reward ladder](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2#reward-ladder).

### Save fragments for tablet recipes

Use the [complete Soul Tablet catalog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Tablets-Effects-and-Ownership-1.12.2) to compare all 17 effects, Soul costs, deactivation and ownership behavior.

The released recipe scan finds **17 tablet recipes** referencing the fragment. Links open the exact historical grids and ingredient images; a recipe reference does not by itself certify placement, skill level, Soul supply or the tablet's effect.

- [Agility Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aagility_tablet)
- [Awareness Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aawareness_tablet)
- [Breeding Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Abreeding_tablet)
- [Cleansing Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Acleansing_tablet)
- [Distortion Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Adistortion_tablet)
- [Energy Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aenergy_tablet)
- [Gravity Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Agravity_tablet)
- [Oxygen Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aoxygen_tablet)
- [Pressure Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Apressure_tablet)
- [Proficiency Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aproficiency_tablet)
- [Resistance Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aresistance_tablet)
- [Sanctity Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Asanctity_tablet)
- [Satiation Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Asatiation_tablet)
- [Sight Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Asight_tablet)
- [Strength Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Astrength_tablet)
- [Untiring Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Auntiring_tablet)
- [Vitality Tablet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Avitality_tablet)

## The two XP expressions are not interchangeable

The released methods use different operation order:

- Stone pickup: `getXpRequiredForNextLevel(level / denominator(level))`. The level division is integer division **inside** the XP lookup argument.
- Fragment growth: `getXpRequiredForNextLevel(level) / denominator(level)`. The XP lookup happens first, followed by floating-point division.

The independent model follows the released operation order and float32 conversion. These are **base XP requests before modifiers**, not live measurements or an intended-balance guarantee.

| Effective Anima level | Denominator | Stone pickup base XP | Fragment growth base XP, approximately |
|---:|---:|---:|---:|
| 1 | 4 | 50 | 13.750 |
| 4 | 4 | 55 | 18.301 |
| 8 | 8 | 55 | 13.397 |
| 14 | 8 | 55 | 23.734 |
| 15 | 30 | 50 | 6.962 |
| 30 | 60 | 50 | 14.541 |
| 60 | 112 | 50 | 135.929 |
| 95 | 280 | 50 | 1527.978 |
| 100 | 280 | 50 | 2460.824 |

Across effective levels 1–100, the pickup model requests **55** at level 4 and levels 8–14, and **50** at every other level. The fragment expression scales differently and drops at denominator boundaries. Do not publish one smooth XP curve for both actions.

| Effective level | Anima denominator |
|---|---:|
| 1–4 | 4 |
| 5–14 | 8 |
| 15–29 | 30 |
| 30–44 | 60 |
| 45–59 | 85 |
| 60–74 | 112 |
| 75–89 | 180 |
| 90–94 | 220 |
| 95–100 | 280 |

The shared effective-level getter caps at 100; a higher displayed vanity level is separate. Skills-disabled configuration returns effective level 100, while the shared XP-granting helper exits without awarding skill XP. Do not extrapolate the device or pickup formulas using displayed levels above 100.

## Why Anima matters for Soul tablets

The shared historical tablet placement path checks an upward-facing solid support face, the required Anima level (or Creative), entity collision and a Soul payment. Its requested placement cost is:

`basePlacementCost × (1 − (effectiveAnimaLevel − 1) / 200) × fullSetFactor`

The full Anima set factor is 0.5; otherwise it is 1. At effective level 1 the level factor is 1, and at 100 it is 0.505. This reduces the initial payment, not a guarantee of unlimited ongoing use.

The selected ongoing supply helper requests `baseSoulDrain × 5 × fullSetFactor`; it does not apply that initial level factor. The full-set armor callbacks also add/remove a 0.3 Anima XP modifier, and the armor declares level 100 as its requirement. These selected shared helpers are not a complete catalog of individual tablet effects or owner/reload behavior.

The placement code pays Soul, calls the entity-spawn method and then shrinks the item outside Creative without checking the spawn return value. Treat cancellation or rejected entity spawning as a resource/item recovery test target before trusting a port.

## Troubleshooting and restoration checks

- [ ] Mature versus immature crops; leaves, flowers and vines; real player versus FakePlayer automation.
- [ ] Another player touches the stone first; full inventory; entity-spawn cancellation.
- [ ] Stone lifetime around ticks 199/200 and chunk/world save/reload behavior.
- [ ] Compare pickup and fragment XP at levels 4/5, 8, 14/15, 94/95 and 100.
- [ ] Fragment growth with obstructed saplings, mature crops, grass, cocoa and a modded growable that leaves its state unchanged.
- [ ] Forge bonemeal hook outcomes; protection permissions; Survival/Creative and skills-disabled configuration.
- [ ] Full/partial Anima armor, XP modifiers and exact initial versus ongoing Soul costs.
- [ ] Tablet placement cancellation, owner disconnect and save/reload in a dedicated-server test before claiming restoration complete.

## Evidence

Sixteen selected released methods, 17 fragment-referencing recipe resources and 100 independent XP comparisons support this guide. The historical source portrait and inventory crop retain image provenance. No Minecraft/game/mod execution was performed.

- [Released-method and XP evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/anima-training-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/anima-training-art-evidence-1.12.2.json)
- [Pinned upstream harvest handler](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/event/PlayerEvents.java)
- [Pinned upstream Anima Stone](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/misc/EntityAnimaStone.java)
- [Pinned upstream fragment use](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/item/misc/FragmentedAnimaStone.java)
