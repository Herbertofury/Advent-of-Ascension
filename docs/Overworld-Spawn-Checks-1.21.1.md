# Overworld spawn checks: light, height and chance

**Minecraft 1.21.1 · AoA 3.7.16.1.** The bestiary now shows checked spawn-rule panels for all **18 creatures in this release's Overworld monster source group**. Open a creature card and expand **Spawn checks · released 1.21.1 defaults**. These rules supplement the biome selectors; they do not replace them.

## How to read a creature card

1. Choose 1.21.1, then find the creature in the [bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1).
2. Read its biome selectors, including exclusions. A biome tag is not necessarily a nearby structure or a physical cave.
3. Expand the spawn-check panel. Check its light/day profile and any Overworld height bound.
4. Treat chance values as additional rejection gates. A 1-in-15 predicate is not a claim that one in every fifteen monsters will be that creature.
5. Distinguish a natural encounter from a spawn egg, command, spawner or modpack-specific spawn system.

An absent added height bound means this particular builder does not add one. It does not mean all heights or every location are valid. Terrain, collision, biome, light, world rules and the wider spawning system still matter.

## Three profiles, not three encounter guarantees

- **Day phase:** the shared helper checks non-Peaceful difficulty, its day-phase condition, the dimension's monster block-light limit and the ordinary valid-spawn-block rule. It also adds a difficulty-scaled random check with factor 0.12.
- **Day or night:** the helper checks non-Peaceful difficulty, monster block light and the valid-spawn-block rule. It has no explicit day-phase condition. Chomper separately adds factor 0.1 for its difficulty-scaled random check.
- **Monster light:** the helper uses the ordinary monster light predicate rather than a dedicated only-at-night rule. A dark enough location and a qualifying spawn time are not interchangeable claims. Ghost and Void Walker use this profile here.

The difficulty predicate compares a random float with **factor × local effective difficulty**. “0.12” is not a universal 12% encounter rate. The actual float constants retain normal binary floating-point representation in the evidence; display labels use their source decimal values.

## Illustrated creature-by-creature reference

“Minimum” and “maximum” below are inclusive, apply to the Overworld height predicate, and are conditional on the helper's natural-spawn classification. “Extra random” excludes the shared/profile difficulty check.

| Creature | Profile | Added Overworld height | Extra random check |
|---|---|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-ancient_golem.png" width="72" height="72" loading="lazy" alt="Ancient Golem source-model portrait"> [Ancient Golem](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:ancient_golem) | Day phase | Minimum 65 | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-bomb_carrier.png" width="72" height="72" loading="lazy" alt="Bomb Carrier source-model portrait"> [Bomb Carrier](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:bomb_carrier) | Day phase | Minimum 55 | 1 in 5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-bush_baby.png" width="72" height="72" loading="lazy" alt="Bush Baby source-model portrait"> [Bush Baby](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:bush_baby) | Day phase | Minimum 65 | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-plains_charger.png" width="72" height="72" loading="lazy" alt="Charger source-model portrait"> [Charger](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:charger) | Day phase | None in this builder | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-chomper.png" width="72" height="72" loading="lazy" alt="Chomper source-model portrait"> [Chomper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:chomper) | Day or night | None in this builder | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-cyclops.png" width="72" height="72" loading="lazy" alt="Cyclops source-model portrait"> [Cyclops](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:cyclops) | Day phase | Minimum 55 | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-ghost.png" width="72" height="72" loading="lazy" alt="Ghost source-model portrait"> [Ghost](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:ghost) | Monster light | Maximum 0 | 1 in 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-goblin.png" width="72" height="72" loading="lazy" alt="Goblin source-model portrait"> [Goblin](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:goblin) | Day phase | None in this builder | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-king_charger.png" width="72" height="72" loading="lazy" alt="King Charger source-model portrait"> [King Charger](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:king_charger) | Day phase | None in this builder | 1 in 16 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-sasquatch.png" width="72" height="72" loading="lazy" alt="Sasquatch source-model portrait"> [Sasquatch](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:sasquatch) | Day phase | Minimum 55 | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-tree_spirit.png" width="72" height="72" loading="lazy" alt="Tree Spirit source-model portrait"> [Tree Spirit](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:tree_spirit) | Day phase | Minimum 55 | 1 in 10 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-void_walker.png" width="72" height="72" loading="lazy" alt="Void Walker source-model portrait"> [Void Walker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:void_walker) | Monster light | Maximum 0 | None in this builder |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-yeti.png" width="72" height="72" loading="lazy" alt="Yeti source-model portrait"> [Yeti](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:yeti) | Day phase | Minimum 45 | 1 in 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-ice_giant.png" width="72" height="72" loading="lazy" alt="Ice Giant source-model portrait"> [Ice Giant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:ice_giant) | Day phase | None in this builder | 1 in 15 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-leafy_giant.png" width="72" height="72" loading="lazy" alt="Leafy Giant source-model portrait"> [Leafy Giant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:leafy_giant) | Day phase | None in this builder | 1 in 15 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-sand_giant.png" width="72" height="72" loading="lazy" alt="Sand Giant source-model portrait"> [Sand Giant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:sand_giant) | Day phase | None in this builder | 1 in 15 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-stone_giant.png" width="72" height="72" loading="lazy" alt="Stone Giant source-model portrait"> [Stone Giant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:stone_giant) | Day phase | None in this builder | 1 in 15 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-wood_giant.png" width="72" height="72" loading="lazy" alt="Wood Giant source-model portrait"> [Wood Giant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:wood_giant) | Day phase | None in this builder | 1 in 15 |

## Boundary examples

- Ancient Golem's added height predicate rejects Y=64 and accepts Y=65 for a natural Overworld attempt. Passing that predicate alone does not spawn the monster.
- Bomb Carrier's corresponding boundary is Y=55; Yeti's is Y=45.
- Ghost and Void Walker use **Y ≤ 0**, so Y=0 passes their added height predicate and Y=1 fails it for a natural Overworld attempt. Neither is an explicit “only at night” rule.
- King Charger adds a 1-in-16 random check; the five giant entries shown here each add 1-in-15. This does not rank their actual encounter frequency across different biomes.
- Chomper's day-or-night helper does not omit block-light or valid-spawn-block checks.

## Spawn reasons and dimension scope

In the pinned helper source, NATURAL, CHUNK_GENERATION, REINFORCEMENT, STRUCTURE and PATROL count as natural for these checks. Other reasons bypass the helper's day/height/random gates where their code explicitly does so. This does not bypass every rule: the remaining difficulty, light and block checks still have their own behavior.

A height restriction built with the Overworld key returns true for a different dimension rather than carrying the same minimum or maximum into that dimension. That does not create a natural spawn entry there. Biome and dimension registration remain separate.

The day-phase predicate uses `getTimeOfDay(1) < 0.25` or `> 0.75`; the exact 0.25 and 0.75 boundaries fail it. Do not translate this into an invented fixed real-time schedule.

## What the inspection guarantees

The extractor accepts only the recognized, straight-line builder instructions used by these 18 released methods. It stops on unsupported instructions instead of guessing a rule. Each record retains the class hash, method bytes, pinned source hash and decoded builder arguments. Other creature groups and older releases are not silently assigned these rules.

The bestiary uses the compact fields already included in its selected-release roster request. Opening the panel does not start an additional archive scan or data request. Existing portraits, biome selectors, loot and base-stat evidence remain unchanged.

- [All 18 exact method receipts and compact panel fields](https://herbertofury.github.io/Advent-of-Ascension/overworld-spawn-panel-evidence-1.21.1.json)
- [Daylight combat and illustrated drops](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Overworld-Daylight-Threats-1.21.1)
- [Beginner walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Beginner-Walkthrough) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

Static archive/source inspection and documentation-interface tests only. No Java or Minecraft code was executed. Natural spawning, modpack overrides and spawn-egg/command/spawner behavior still need target-build testing. AoA portraits: Tslat and contributors.
