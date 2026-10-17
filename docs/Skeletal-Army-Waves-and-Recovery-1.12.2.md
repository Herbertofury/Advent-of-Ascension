# Skeletal Army: all 39 waves and recovery boundaries

**Minecraft 1.12.2 / AoA 3.3.6.** Find the Precasian arena, preserve its Army Block, control when each Elder dies and prepare for Skeletron. This guide follows the released historical handlers. It does not certify a modern restoration or a live multiplayer run.

[Historical first portal and Precasia](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Historical altars](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Altars-and-Summon-Preparation-1.12.2) · [Worlds and travel](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions)

![Eleven Skeletal Army creature appearances and wave advice](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/skeletal-army-wave-roster-1.12.2.webp)

## Prepare before starting

1. Reach **historical Precasia** and locate its Skeletal Army Arena. Generation depends on its configured chance, the surrounding generator branch and terrain checks; it is not guaranteed in every chunk.
2. Keep the **Army Block intact**. The generated structure places it at relative offset **(22, 1, 13)** from its structure origin. This is a structure-relative coordinate, not an absolute world destination.
3. Use a non-Peaceful difficulty for the ordinary shared altar activation path. Clear the arena and bring enough healing and weapon resources for an extended sequence.
4. Keep the Elder near its Army Block. Its qualifying death requires squared distance **strictly below 2,500**, a valid stored block position and an Army Block still at that position.
5. Clear other fighters before deliberately finishing each Elder. The selected advancement callback does **not** wait for all other enemies to die.

### Starting is not a consumable-key purchase

On the server, the Army Block activation condition searches the block-centered box expanded by 100 for **Skele-Elder or Skeletron**. If neither is found, it constructs a wave-zero Elder and explicitly places it at the Army Block's X/Z and Y + 1.

That condition returns false even after this side effect. The shared altar branch therefore does not proceed to its ordinary held-item shrink and activation effect. Do not prescribe a Skeletal Sword, an arbitrary consumed item or a fixed summon-key fee for this path. The separate random-tick starter path is discussed below.

## How progression actually advances

A qualifying Elder death calls `spawnWave` with its stored wave **plus one**. The initial starter has wave zero, so its death starts numbered wave 1. Waves 1–38 each construct one further Elder. Wave 39 constructs **Skeletron** instead.

There is no selected player-kill requirement for the Elder callback and no all-enemies-cleared gate. An early Elder death can overlap the next wave with survivors. If the Elder dies too far away, its stored block is missing or its stored wave is negative, the selected callback does not advance.

The numbered arms contain **281 entity constructions** in total: 38 Elders, one Skeletron and 242 other fighters. The initial starter Elder is additional. These are constructor counts, **not simultaneous enemy counts or guaranteed successful spawns**.

## Complete wave sheet

Each name opens the release-specific model and loot record. “Total” includes the Elder where present.

| Wave | Constructed lineup | Total |
|---|---|---:|
| 1 | 2 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 3 |
| 2 | 1 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 3 | 2 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 3 |
| 4 | 1 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 5 | 2 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 3 |
| 6 | 1 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 1 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 3 |
| 7 | 1 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 1 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 1 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 8 | 2 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 2 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 5 |
| 9 | 2 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 2 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 2 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 7 |
| 10 | 3 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 11 | 3 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 3 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 7 |
| 12 | 1 × [Skele-Pig (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 13 | 1 × [Skele-Hopper (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 14 | 1 × [Skeleman (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 15 | 3 × [Skele-Pig (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 16 | 3 × [Skele-Hopper (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 17 | 3 × [Skeleman (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 18 | 2 × [Skele-Pig (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_pig), 2 × [Skele-Hopper (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_hopper), 2 × [Skeleman (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 7 |
| 19 | 2 × [Skele-Pig](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_pig), 2 × [Skele-Hopper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_hopper), 2 × [Skeleman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeleman), 2 × [Skele-Pig (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_pig), 2 × [Skele-Hopper (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_hopper), 2 × [Skeleman (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 13 |
| 20 | 1 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 21 | 1 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 22 | 1 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 2 |
| 23 | 3 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 24 | 3 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 25 | 3 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 4 |
| 26 | 2 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 2 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 2 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 7 |
| 27 | 3 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 3 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 3 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 10 |
| 28 | 4 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 4 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 9 |
| 29 | 5 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 5 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 4 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 2 × [Skeleman (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 17 |
| 30 | 8 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 9 |
| 31 | 8 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 9 |
| 32 | 8 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 9 |
| 33 | 12 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 13 |
| 34 | 12 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 13 |
| 35 | 12 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 13 |
| 36 | 6 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 6 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 6 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 2 × [Skele-Pig (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_pig), 2 × [Skele-Hopper (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skele_hopper), 2 × [Skeleman (Strong)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrong_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 25 |
| 37 | 15 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 16 |
| 38 | 10 × [Skele-Pig (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_pig), 10 × [Skele-Hopper (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skele_hopper), 10 × [Skeleman (Elite)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelite_skeleman), 1 × [Skele-Elder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askele_elder) | 31 |
| 39 | 1 × [Skeletron](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Askeletron) | 1 |

### Late-wave pacing

Wave 36 attempts 25 entities and wave 38 attempts 31. These are useful preparation milestones, but they do not cap the number of surviving enemies when waves overlap. Avoid treating the Elder as an ordinary first-priority target if the arena is already crowded.

The selected wave spawn helper draws X offsets from **−17 through +5** and Z offsets from **−11 through +7**, relative to the Army Block. It searches upward for an air block before placing each entity. An air-block check is not a full creature-bounding-box clearance test. Modified ceilings, obstructions and nearby construction need separate testing.

## Skeletron and completion rewards

The historical Skeletron base getters supply **1,100 health** and **70 melee damage**. These are base values, not final player damage after difficulty, armor and other effects. Its army-position constructor uses the Army Block's X/Z and Y + 2.

Its released loot table separates two pools:

| Pool | Entries / base weights |
|---|---|
| Rare reward, one roll | Empty: 75, quality −10; Skeletal Archergun: 24; Skeletal Sword: 24 |
| Statue, one roll | Skeletron Statue |

Weights are not unconditional percentages. Pool conditions and luck-sensitive quality must be considered; the statue pool is separate from the rare selection. Use the Skeletron bestiary record for the underlying loot reference and item images.

### Optional full-set advancement

The selected death callback resolves a player killer or the player owner of a tameable killer. For `precasia/spooky_scary_skeletons`, criterion `full_set_kill`, it then requires a multiplayer-player instance, **Skeletal Sword in the main hand**, and every returned armor stack to be an `AdventArmour` of the **SKELETAL** set.

This is an **optional completion advancement condition, not an entry requirement**. In particular, the sword is not a summon payment. The selected historical death method does not construct a wounded second phase; do not import a different release's Skeletron progression into this guide.

## Save/reload and starter behavior: test before relying on it

### Wave zero is omitted by the selected writer

The default Elder constructor initializes wave to −1. Its writer saves `SkeletalArmyWave` only when **wave > 0**, while the reader replaces the default only if that key exists. The Army Block position is written separately when non-null.

An independent model of those selected branches gives:

| Wave before writing | Wave key written? | Wave after default construction + read |
|---:|---|---:|
| −1 | No | −1 |
| 0, starter | No | −1 |
| 1 | Yes | 1 |
| 38 | Yes | 38 |

This is a **source-derived persistence boundary, not a reproduced live softlock**. A restored negative-wave Elder would fail the selected progression gate and qualify for the class's despawn condition. Despawning and a later starter might recover the encounter; full world/chunk and multiplayer behavior remains untested.

### The random-tick path differs from manual activation

The selected server random-tick branch additionally requires `random.nextBoolean()` and no Skele-Elder in the expanded box. Unlike manual activation, it does not check Skeletron in that query. It constructs an Elder with Army Block position and wave zero, but does not make the manual path's explicit position call. The parameterized Elder constructor stores its home and wave data without setting its entity position.

These are concrete positioning and duplicate-event test targets. They do not by themselves prove a live spawn at the origin, an unavoidable duplicate boss or a permanent failure. Do not rely on a fixed wall-clock delay for automatic restart.

## Restoration and regression checklist

- [ ] Starter activation: Survival/Creative, Peaceful/non-Peaceful, no nearby boss, existing Elder and existing Skeletron.
- [ ] Random ticks: verify actual starter coordinates and behavior while Skeletron remains alive.
- [ ] Progression: defeat Elders at distances just below, exactly at and above 50; preserve versus remove the Army Block.
- [ ] Overlap: kill the Elder before other fighters and verify the intended survivor/next-wave policy.
- [ ] Persistence: save/reload wave zero, wave one and wave 38; unload/reload the arena chunk; repeat on a dedicated server.
- [ ] Spawn safety: obstruct spawn columns and inspect failed spawn return values, creature clearance and recovery.
- [ ] Completion: ordinary kill, tameable-owner kill, full Skeletal equipment and missing/wrong equipment; verify loot pools independently.
- [ ] Porting: preserve stable entity/item IDs and saved wave data; document deliberate behavioral fixes separately from historical parity.

## Evidence and scope

The wave sheet is extracted from all **39 released switch arms**, joined to eleven exact historical creature identities. Twenty selected released methods, structure placement, a loot resource and pinned source hashes support the interpretation. The persistence examples are an independent Python model. No game, server or mod was executed for these checks.

- [Machine-readable released-method and wave evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/skeletal-army-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/skeletal-army-art-evidence-1.12.2.json)
- [Pinned upstream Army Block source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/block/functional/altar/ArmyBlock.java)
- [Pinned upstream Elder source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/boss/skeletalarmy/EntitySkeleElder.java)
- [Pinned upstream Skeletron source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/boss/skeletalarmy/EntitySkeletron.java)
