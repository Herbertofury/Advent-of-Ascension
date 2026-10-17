# Daylight threats: Ancient Golem and Bomb Carrier

**Minecraft 1.21.1 · AoA 3.7.16.1.** Daylight is not a universal safe period in AoA. These two monsters use the day-monster spawn helper. This guide explains their checked defaults, what to watch for and what their loot tables actually promise.

![Ancient Golem and Bomb Carrier comparison using source-model portraits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/overworld-day-hazards-1.21.1.webp)

## A practical first encounter

1. Identify the creature before approaching. An Ancient Golem is not the village's ordinary Iron Golem.
2. Keep a retreat route. Avoid accepting a close-range hit merely to inspect its model or drops.
3. For a Bomb Carrier, watch the thrown projectile as well as the creature. Move away from the impact area and avoid fighting beside valuable builds.
4. For an Ancient Golem, plan around its high armor/toughness and knockback resistance. Water is not a reliable drowning trap: its fluid-drowning override returns false.
5. Read the actual loot pool before committing to a fight. Neither monster guarantees every illustrated reward.

These are cautious planning suggestions based on the behavior below, not a tested combat strategy, guaranteed escape distance or claim that a shield blocks every attack.

## Ancient Golem: armored melee threat

| Released attribute-builder input | Value |
|---|---:|
| Maximum health | 50 |
| Movement speed | 0.15 |
| Melee strength | 15 |
| Knockback resistance | 1 |
| Attack knockback | 5 |
| Armor / toughness | 20 / 40 |
| Follow / aggro range | 40 / 16 |

These are declared inputs before difficulty, effects, equipment and mod hooks. “15 melee strength” is not a promise of exactly 15 health lost on every hit. The source defines pre-attack time 1 and swing duration 11; those values alone do not establish the complete AI attack cadence.

Its idle target task includes the nearest visible attackable player and rejects allied targets. It should not be presented as an automatically friendly village guardian because of its appearance. Its `canDrownInFluidType` override returns false; that is not immunity to every fluid-related damage type.

[Ancient Golem bestiary and drops](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:ancient_golem) · [Rotate its source model](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:ancient_golem)

## Bomb Carrier: the projectile stat is not the explosion stat

The declared monster attributes are 23 health, 0.3 movement speed, 2 projectile damage, 12 follow range and 8 aggro range. Its custom ranged attack creates a Bomb Carrier Dynamite projectile, offsets it from the thrower, aims toward the target and compensates for gravity.

The dynamite's block-hit and entity-hit callbacks both request an explosion at the hit location on the server. Do not describe it as a harmless thrown item that always waits for a normal placed-TNT fuse.

The checked explosion definition passes:

| Explosion builder input | Value |
|---|---:|
| radius | 3 |
| entityDamage | 8 |
| blockDamage | 8.5 |

The monster's **2 projectile-damage attribute is not the explosion's 8 entityDamage input**. Neither is a measured final-damage result. Radius 3 is a configuration input, not a certified safe-distance boundary, and blockDamage 8.5 does not mean 8.5 blocks are destroyed.

AoA's explosion builder supplies its griefing check. It first rejects block damage when the properties do not damage blocks; for a player/player-owned source it checks destructive-weapon physics, otherwise it delegates to the platform's mob-griefing check. The external explosion library, game rules, permissions and other mods still affect the final result. Test protection behavior on a disposable world rather than trusting a valuable build.

[Numbered loot details and spawn selectors](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:bomb_carrier) · [Rotate Bomb Carrier](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:bomb_carrier)

[Compare spawn checks for all 18 Overworld monster entries](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Overworld-Spawn-Checks-1.21.1). Their bestiary cards now include the same release-specific panels.

## Where the spawn evidence applies

| Creature | Biome selector | Natural Overworld height gate | Spawn-pool entry |
|---|---|---|---|
| Ancient Golem | Overworld plus at least one of the village-desert/plains/savanna/snowy/taiga or woodland-mansion biome tags; excludes `c:no_mob_spawns` | Y ≥ 65 | Weight 15, group 1–1 |
| Bomb Carrier | Overworld plus Badlands, Eroded Badlands or `c:is_cave`; excludes `c:no_mob_spawns` and `c:is_snowy` | Y ≥ 55 | Weight 10, group 1–1 |

A biome's “has_structure” tag is not a test that an actual village or mansion stands nearby. Likewise, a cave biome selector does not prove the creature appears in every underground cavity.

The common day-monster helper adds non-Peaceful difficulty, its day-phase predicate, the dimension's monster block-light limit, a valid spawn block and a difficulty-scaled chance check. Bomb Carrier adds a further 1-in-5 check. **Weight 15 is not a 15% encounter chance**, and these gates cannot be multiplied into a guaranteed world-wide spawn rate without the rest of the spawning system.

The helper's “natural” category includes NATURAL, CHUNK_GENERATION, REINFORCEMENT, STRUCTURE and PATROL in the pinned source. Some predicates, including the height/day/chance gates, bypass their checks for other spawn reasons. The Overworld height gate also does not impose the same minimum in a different dimension. Commands, spawners, datapacks and mod overrides require separate evaluation.

The day predicate compares `getTimeOfDay(1)` with `< 0.25` or `> 0.75`; both exact boundary values are excluded. This is a source predicate, not a fixed wall-clock schedule.

## Illustrated loot pools

The fractions below describe selection weight **per roll in the named pool**, assuming unchanged entries and no luck-related weight changes. They are not an overall chance per kill. Count functions, Looting, other pools and global modifiers remain separate. An empty entry can win.

### Ancient Golem

| Reward | Pool | Selection weight | Pool rolls |
|---|---|---|---|
| No item from this roll | loot | 75/245 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-iron_ingot.webp" width="44" height="44" alt="Iron Ingot"> Iron Ingot | loot | 100/245 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-armour_plating.webp" width="44" height="44" alt="Armour Plating"> Armour Plating | loot | 10/245 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-power_core.webp" width="44" height="44" alt="Power Core"> Power Core | loot | 20/245 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-poppy.webp" width="44" height="44" alt="Poppy"> Poppy | loot | 40/245 | 2 |

### Bomb Carrier

| Reward | Pool | Selection weight | Pool rolls |
|---|---|---|---|
| No item from this roll | loot | 50/118 | 1–2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-gunpowder.webp" width="44" height="44" alt="Gunpowder"> Gunpowder | loot | 20/118 | 1–2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-tnt.webp" width="44" height="44" alt="TNT"> TNT | loot | 5/118 | 1–2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-flint.webp" width="44" height="44" alt="Flint"> Flint | loot | 30/118 | 1–2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-torn_cloth.webp" width="44" height="44" alt="Torn Cloth"> Torn Cloth | loot | 10/118 | 1–2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-silver_coin.webp" width="44" height="44" alt="Silver Coin"> Silver Coin | loot | 3/118 | 1–2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-bone.webp" width="44" height="44" alt="Bone"> Bone | bones | 1/1 | 1 |
| No item from this roll | torch | 10/11 | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/day-hazard-loot-torch.webp" width="44" height="44" alt="Torch"> Torch | torch | 1/11 | 1 |

Ancient Golem's main pool rolls twice. Its iron entry has a 1–5 base count and a separate Looting count function. A Power Core's 20/245 selection weight is per roll; it is not guaranteed by defeating one golem.

Bomb Carrier's main pool rolls 1–2 times. Bones are a separate one-roll pool with a 0–2 base count, so selecting the bone entry does not guarantee a positive unmodified count. Torches are another separate pool, with an empty weight of 10 and torch weight of 1. Use the linked bestiary's full loot detail for exact count and enchantment functions.

## Source checks and limits

- [Released classes, four resource files, 40 height cases and 14 day-phase cases](https://herbertofury.github.io/Advent-of-Ascension/overworld-day-hazards-evidence-1.21.1.json)
- [Portrait and loot-icon extraction evidence](https://herbertofury.github.io/Advent-of-Ascension/overworld-day-hazards-art-evidence-1.21.1.json)
- [Beginner walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Beginner-Walkthrough) · [Combat index](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bosses-and-Combat) · [Loot conditions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Finding-and-Using-Mob-Drops)

This is static source/archive analysis. No Minecraft classes were executed and no target-build combat, spawning, block-protection or damage test is claimed. Original AoA creature/item artwork belongs to Tslat and contributors; vanilla item artwork is from Minecraft. Layout and analysis are original documentation work.
