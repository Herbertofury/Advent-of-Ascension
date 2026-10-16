# Finding Traders · 1.16.5

**Minecraft 1.16.5 / AoA 3.6.11.** Candidate acquisition evidence is now mapped for **43 of the 44 inspected trader identities**: eight use the custom trader spawner, 33 are embedded in structure templates, and two are produced by crate-breaking hooks. Skill Master remains unresolved in this scan. These are distinct evidence routes, not 43 live-game spawn tests.

[Search their offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.16.5) · [Historical shopping handbook](Trading-and-Traders-1.16.5) · [Filter the bestiary by dimension or biome](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5)

## Start with the right route

| What you want | Where to start |
|---|---|
| Naturalist, Assassin, Realmshifter, ordinary Lottoman | Eligible Overworld plains/hills/forest biome types; see exclusions below |
| Troll Trader | Eligible Overworld beach biome types |
| Metalloid | Iromine’s `aoa3:iromine` biome, through the custom trader spawner |
| Withering Lottoman | Eligible Nether biome types, through the custom trader spawner |
| Regional Lottomans and specialist shops | The structure/piece table below; not a generic wandering-trader rule |
| Toxic Lottoman / Store Keeper | Vox Crate / Vox Store Crate player-break hooks, without Silk Touch |
| Undead Herald | Multiple dimension-specific special-spawner entries, including a water-placement case in L’Borean |

## Custom-spawner conditions

The 29 released NPC builder chains match the pinned source declarations for eight unique traders. For biome-type selectors, the matcher requires **any listed positive type**, rejects **any listed excluded type**, and also requires the Overworld type unless the entry explicitly targets Nether. Mushroom Fields and Mushroom Field Shore are rejected on this type-matching path. Exact-biome entries use a separate direct match.

| Trader | Positive selectors / exact biomes | Important condition |
|---|---|
| [Assassin](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:assassin) | PLAINS, HILLS, FOREST | Excludes CONIFEROUS, SANDY, SAVANNA, SNOWY. Ground placement and raw brightness ≥8. |
| [Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:lottoman) | PLAINS, HILLS, FOREST | Excludes CONIFEROUS, SANDY, SAVANNA, SNOWY. Ground placement and raw brightness ≥8. |
| [Metalloid](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:metalloid) | aoa3:iromine | Ground placement and raw brightness ≥8. |
| [Naturalist](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:naturalist) | PLAINS, HILLS, FOREST | Excludes CONIFEROUS, SANDY, SAVANNA, SNOWY. Ground placement and raw brightness ≥8. |
| [Realmshifter](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:realmshifter) | PLAINS, HILLS, FOREST | Excludes CONIFEROUS, SANDY, SAVANNA, SNOWY. Ground placement and raw brightness ≥8. |
| [Troll Trader](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:troll_trader) | BEACH | Ground placement and raw brightness ≥8. |
| [Undead Herald](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:undead_herald) | Overworld type set, Nether type, and 20 exact AoA biome entries; details below | Excludes CONIFEROUS, SANDY, SAVANNA, SNOWY. Per-entry light and placement rules apply. |
| [Withering Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:withering_lottoman) | NETHER | Ground placement and raw brightness ≥8. |

<details><summary>Undead Herald: all 20 exact-biome placement entries</summary>

| Biome | Placement / heightmap | Darkness bypass |
|---|---|---|
| `aoa3:abyssal_plains` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |
| `aoa3:barren_grounds` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:candy_hills` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:celevian_highlands` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:creepoid_forest` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:crystevian_caverns` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |
| `aoa3:cavern_depths` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |
| `aoa3:dustopian_forest` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |
| `aoa3:floral_islands` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:greckon_mountains` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |
| `aoa3:haven` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:iromine` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:coral_fields` | IN_WATER / OCEAN_FLOOR | Yes; ordinary mob spawn checks still apply |
| `aoa3:lelyetian_plains` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:asteroid_belt` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:fungal_caverns` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |
| `aoa3:precasian_tall_forest` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:runic_cliffs` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:shyre_remnants` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | No; raw brightness ≥8 |
| `aoa3:vox_wastes` | ON_GROUND / MOTION_BLOCKING_NO_LEAVES | Yes; ordinary mob spawn checks still apply |

</details>

### Why waiting does not guarantee a trader

- The special spawner is installed for the Overworld, Nether and AoA-namespace worlds other than Nowhere in the pinned event code. This does not imply support in the End or every other mod’s dimension.
- Passive spawning must be enabled and `doMobSpawning` must permit it. The spawner selects living, non-spectator server players.
- A pass makes up to **two location attempts per eligible player**, sampling X and Z offsets in the **−64 to +64 square**, then resolving the heightmap and spawn space. That is not a guaranteed pair of NPCs or a circular 64-block radius.
- Biome-pool membership, placement, collision, normal mob checks and Forge’s spawn hook can reject the attempt.
- The source begins with a 24,000-tick cooldown, delays its probability check above 12,000, then uses a changing one-in-N check. It resets the cooldown and adds 3,600 per accepted spawn. This is not a fixed “a trader appears every X minutes” promise.
- A weight of one is a **relative pool weight**, not a 1% spawn chance. Modpack changes and the full eligible pool matter.

## Structure-linked shops

These routes join released template contents → declared jigsaw-pool references → source structure roots → released biome starts → explicit dimension structure settings. All 28 trader-bearing templates were linked. The graph is an **over-approximation**: connector compatibility, assembly depth and terrain placement are not simulated, so a listed piece is not guaranteed in every generated structure.

| Trader | Structure candidate | Declared dimension / biome |
|---|---|---|
| [Abyssal Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:abyssal_lottoman) | Abyssal Lotto Hut (`aoa3:abyssal_lotto_hut`) | `aoa3:abyss` / `aoa3:abyssal_plains` |
| [Baron Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:baron_lottoman) | Baron House (`aoa3:baron_house`) | `aoa3:barathos` / `aoa3:barren_grounds` |
| [Boreic Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:boreic_lottoman) | Drowned Lotto Stand (`aoa3:drowned_lotto_stand`) | `aoa3:lborean` / `aoa3:coral_fields` |
| [Candied Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:candied_lottoman) | Candy Lotto Platform (`aoa3:candy_lotto_platform`) | `aoa3:candyland` / `aoa3:candy_hills` |
| [Celevian Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:celevian_lottoman) | Celevian Lotto Balloon (`aoa3:celevian_lotto_balloon`) | `aoa3:celeve` / `aoa3:celevian_highlands` |
| [Creeponia Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:creeponia_lottoman) | Creeponian Lotto Stand (`aoa3:creeponian_lotto_stand`) | `aoa3:creeponia` / `aoa3:creepoid_forest` |
| [Crystal Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:crystal_lottoman) | Crystal Lotto Overlook (`aoa3:crystal_lotto_overlook`) | `aoa3:crystevia` / `aoa3:crystevian_caverns` |
| [Dustopian Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:dustopian_lottoman) | Lotto Cage (`aoa3:lotto_cage`) | `aoa3:dustopia` / `aoa3:dustopian_forest` |
| [Explosives Expert](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:explosives_expert) | Explosives Tower (`aoa3:explosives_tower`) | `aoa3:creeponia` / `aoa3:creepoid_forest` |
| [Floro Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:floro_lottoman) | Lotto Sky Flower (`aoa3:lotto_sky_flower`) | `aoa3:gardencia` / `aoa3:floral_islands` |
| [Golden Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:golden_lottoman) | Iro Pillar (`aoa3:iro_pillar`) | `aoa3:iromine` / `aoa3:iromine` |
| [Gorb Arms Dealer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:gorb_arms_dealer) | Gorb Village (`aoa3:gorb_village`) | `aoa3:mysterium` / `aoa3:fungal_caverns` |
| [Gorb Engineer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:gorb_engineer) | Gorb Village (`aoa3:gorb_village`) | `aoa3:mysterium` / `aoa3:fungal_caverns` |
| [Haunted Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:haunted_lottoman) | Haunted Lotto Rock (`aoa3:haunted_lotto_rock`) | `aoa3:greckon` / `aoa3:greckon_mountains` |
| [Lelyetian Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:lelyetian_lottoman) | Lelyetian Tower (`aoa3:lelyetian_tower`) | `aoa3:lelyetia` / `aoa3:lelyetian_plains` |
| [Lelyetian Trader](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:lelyetian_trader) | Lelyetian Tower (`aoa3:lelyetian_tower`) | `aoa3:lelyetia` / `aoa3:lelyetian_plains` |
| [Lunar Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:lunar_lottoman) | Stranded Lottoman (`aoa3:stranded_lottoman`) | `aoa3:lunalus` / `aoa3:asteroid_belt` |
| [Mystic Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:mystic_lottoman) | Mystic Lotto Shroom (`aoa3:mystic_lotto_shroom`) | `aoa3:mysterium` / `aoa3:fungal_caverns` |
| [Precasian Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:precasian_lottoman) | Jungle Lotto Hut (`aoa3:jungle_lotto_hut`) | `aoa3:precasia` / `aoa3:precasian_tall_forest` |
| [Primordial Merchant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:primordial_merchant) | Dustopian Village (`aoa3:dustopian_village`) | `aoa3:dustopia` / `aoa3:dustopian_forest` |
| [Primordial Spellbinder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:primordial_spellbinder) | Dustopian Village (`aoa3:dustopian_village`) | `aoa3:dustopia` / `aoa3:dustopian_forest` |
| [Primordial Wizard](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:primordial_wizard) | Dustopian Village (`aoa3:dustopian_village`) | `aoa3:dustopia` / `aoa3:dustopian_forest` |
| [Professor](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:professor) | Professors Lab (`aoa3:professors_lab`) | `aoa3:iromine` / `aoa3:iromine` |
| [Rocky Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:rocky_lottoman) | Deep Lotto Shelter (`aoa3:deep_lotto_shelter`) | `aoa3:deeplands` / `aoa3:cavern_depths` |
| [Runic Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:runic_lottoman) | Runic Tower (`aoa3:runic_tower`) | `aoa3:runandor` / `aoa3:runic_cliffs` |
| [Shyre Archer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:shyre_archer) | Archer Outpost (`aoa3:archer_outpost`) | `aoa3:shyrelands` / `aoa3:shyre_remnants` |
| [Shyrelands Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:shyrelands_lottoman) | Shyre Lotto Bunker (`aoa3:shyre_lotto_bunker`) | `aoa3:shyrelands` / `aoa3:shyre_remnants` |
| [Toy Merchant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:toy_merchant) | Toy Tower (`aoa3:toy_tower`) | `aoa3:celeve` / `aoa3:celevian_highlands` |
| [Twinkling Lottoman](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:twinkling_lottoman) | Floating Lotto Fountain (`aoa3:floating_lotto_fountain`) | `aoa3:haven` / `aoa3:haven` |
| [Zal Grocer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:zal_grocer) | Zal Ship (`aoa3:zal_ship`) | `aoa3:lunalus` / `aoa3:asteroid_belt` |
| [Zal Herbalist](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:zal_herbalist) | Zal Ship (`aoa3:zal_ship`) | `aoa3:lunalus` / `aoa3:asteroid_belt` |
| [Zal Spellbinder](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:zal_spellbinder) | Zal Ship (`aoa3:zal_ship`) | `aoa3:lunalus` / `aoa3:asteroid_belt` |
| [Zal Vendor](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:zal_vendor) | Zal Ship (`aoa3:zal_ship`) | `aoa3:lunalus` / `aoa3:asteroid_belt` |

## Vox Pond crates: break the correct block

| Block reference | Trader produced by its player-break hook | Candidate structure |
|---|---|---|
| <img src="https://herbertofury.github.io/Advent-of-Ascension/previews/trader-block-1.16.5-vox_crate.webp" width="96" height="96" alt="Vox Crate"> Vox Crate | Toxic Lottoman | Vox Lotto Outpost |
| <img src="https://herbertofury.github.io/Advent-of-Ascension/previews/trader-block-1.16.5-vox_store_crate.webp" width="96" height="96" alt="Vox Store Crate"> Vox Store Crate | Store Keeper | Destroyed Store; three template variants contain the crate |

Both inspected hooks run on the server and check that the player’s **main-hand item has zero Silk Touch level**. The hook creates the relevant trader at the crate location and finalizes it with event spawn reason. The Toxic Lottoman uses a +0.5 Y offset; Store Keeper uses the block Y. This describes the player-destruction callback, not arbitrary explosions, automation or a guarantee that every block-breaking mod preserves it.

Silk Touch suppresses this spawn path. Do not silently substitute an ordinary chest or assume every similarly textured block works. The two blocks have distinct IDs: `aoa3:vox_crate` and `aoa3:vox_store_crate`.

## Still unresolved: Skill Master

The class, trades, renderer and registration exist, but this scan found no matching special-spawner declaration, embedded entity in the 258 released templates, or direct creation call comparable to the two Vox crate hooks. That is **missing acquisition evidence**, not proof the NPC is impossible to obtain. Keep its natural acquisition route open for further investigation and in-game validation.

## Restocking differs between releases

The inspected **1.16.5** `TraderRestockGoal.canUse()` checks alive, not currently trading, `canRestock()` and `allowedToRestock()`. Its start step still checks `shouldRestock()`. It does **not contain the nearby-player 24-block check** documented in the inspected **1.21.1** goal. Do not apply that modern rule to this historical build without checking the actual modpack. Other AI and inherited rules can still affect restocking.

## Evidence and reproduction

- [44-identity location ledger](https://herbertofury.github.io/Advent-of-Ascension/trader-locations-1.16.5.json)
- [29 source/released special-spawner matches](https://herbertofury.github.io/Advent-of-Ascension/trader-special-spawns-1.16.5.json)
- [258-template NBT scan; 28 contain trader entities](https://herbertofury.github.io/Advent-of-Ascension/trader-structure-templates-1.16.5.json)
- [Pool/structure/biome/dimension links and resource hashes](https://herbertofury.github.io/Advent-of-Ascension/trader-location-graph-1.16.5.json)
- [Source special spawner](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/world/spawner/TraderSpawner.java) · [Source spawn registration and predicates](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/common/registration/AoAEntitySpawns.java)
- [Vox Crate hook](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/block/functional/utility/VoxCrate.java) · [Vox Store Crate hook](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/block/functional/utility/VoxStoreCrate.java)

NBT is read as data; no Minecraft or Java classes are executed. Only relevant IDs, template-local positions and hashes are retained in the extracted template ledger; full entity NBT and UUIDs are not republished. Source-derived block art: **Tslat and contributors**. No world-seed, natural-spawn frequency or complete Enderloom gameplay certification is claimed.
