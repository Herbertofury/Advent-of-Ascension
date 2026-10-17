# Precasia habitats: height gates and special spawn branches

**Minecraft 1.21.1 · AoA 3.7.16.1.** Use this alongside the [Precasia Realmstone route](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Precasia-Realmstone-Walkthrough) and [first-portal preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-Walkthrough). It covers seven monster spawn-rule paths, not every creature or encounter in Precasia.

![Seven Precasia creature height predicates, not a map of spawn density or safe zones](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/precasia-height-gates-1.21.1.webp)

## Plan an expedition, not just a biome search

Before entering, prepare a return route, food, spare equipment and free inventory space. In the bestiary, choose 1.21.1 and a creature, then expand **Spawn checks · released 1.21.1 defaults**. Read its biome list and spawn pool together with the conditions.

The listed seven use the **day-or-night monster helper**: non-Peaceful difficulty, the dimension's monster block-light limit and a valid spawn block. It does not impose the separate day-phase predicate used by the Overworld day-monster profile. Their additional gates can still reject an attempt.

The diagram shows only height-related branches. It is cropped to Y−20 through 80; applicable bands continue outside that plotted range. A shaded band does not guarantee a spawn, and an unshaded band does not make a place safe from other creatures or existing mobs.

## Quick reference

| Creature | Extra height/custom gate in Precasia | Extra random input | Biome entries found |
|---|---|---|---|
| [Attercopus](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:attercopus) | Two branches split at Y=50; see below | 0.05, or 0.05 × effective difficulty by branch | caves, desert, forest, jungle, ocean, plains, river, savannah, shore, tall forest |
| [Dunkleosteus](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:dunkleosteus) | Y ≤ 55 | 0.05 × effective difficulty | ocean |
| [Meganeuropsis](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:meganeuropsis) | Y ≥ 65 | 0.05 × effective difficulty | jungle |
| [Scolopendis](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:scolopendis) | Y ≤ 50 | 1 in 40 | caves |
| [Smilodon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:smilodon) | Y ≥ 60 | 0.1 × effective difficulty | forest, jungle, plains, savannah, tall forest |
| [Spinoledon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:spinoledon) | Y ≥ 60 OR Y ≤ −13 | 0.05 × effective difficulty | caves, forest, jungle, plains, savannah, tall forest |
| [Veloraptor](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:veloraptor) | Y ≥ 60 | 0.1 × effective difficulty | desert, forest, jungle, plains, savannah, tall forest |

The ordinary minimum/maximum helper bounds are inclusive and apply to its natural-spawn category in the specified dimension. The two custom branches below need separate interpretation. Random inputs are rejection thresholds, not overall encounter percentages. Spawn-pool weight and group size remain available in each card's exact spawn declarations.

## Attercopus: the same biome list can hide very different gates

In the custom predicate:

- **Outside Precasia:** this custom predicate returns true. That alone does not create a natural spawn entry or bypass the common helper.
- **In Precasia at Y ≤ 50:** a non-natural reason passes this custom branch; a helper-classified natural attempt requires a random float below 0.05.
- **In Precasia above Y 50:** the biome must be Precasian Desert, sky-darkening must be at least 4, and the random value must be below 0.05 × local effective difficulty. This upper branch does **not** have the lower branch's natural-reason bypass.

Examples of the custom gate alone:

| Context | Result |
|---|---|
| Precasia, Y 50, natural reason, random 0.049 | Pass |
| Precasia, Y 50, natural reason, random 0.05 | Fail at the stated threshold |
| Precasia, Y 50, non-natural reason | Pass this custom branch |
| Precasia, Y 51, non-desert biome | Fail, even for a non-natural reason |
| Precasia, Y 51, desert, sky-darkening 3 | Fail |
| Precasia, Y 51, desert, sky-darkening 4, difficulty 1, random 0.049 | Pass this custom branch |

This explains why a biome loot/spawn resource listing Attercopus does not prove an unrestricted surface population there. These are source-value predicate examples, not executed spawning tests or a clock-time conversion for sky-darkening.

## Spinoledon: two separate altitude bands

Its custom condition accepts **Y ≥ 60 OR Y ≤ −13** in Precasia. Thus −13 and 60 pass; −12 through 59 fail that height condition. It does not call the helper's natural-spawn test inside this custom height condition, so do not describe it as automatically bypassed by every non-natural reason.

A separate difficulty-scaled chance gate still comes earlier in its builder. Outside Precasia, the dimension-dependent custom condition passes, but that does not establish natural spawning in another dimension. Commands, spawners and other mods can use different pathways.

## Remaining boundaries

- Dunkleosteus: ordinary maximum-height helper at 55, plus difficulty factor 0.05; the inspected biome entry is Precasian Ocean. Do not infer exact underwater depth from its name or the height value alone.
- Meganeuropsis: minimum 65, difficulty factor 0.05; inspected entry is Precasian Jungle.
- Scolopendis: maximum 50 and random threshold 0.025, shown as 1 in 40; inspected entry is Precasian Caves.
- Smilodon and Veloraptor: minimum 60, difficulty factor 0.1; their biome lists differ.

The helper's natural category includes NATURAL, CHUNK_GENERATION, REINFORCEMENT, STRUCTURE and PATROL in the pinned source. Its ordinary dimension-scoped height/chance predicates differ from the explicit custom conditions above. [Read the common helper explanation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Overworld-Spawn-Checks-1.21.1#spawn-reasons-and-dimension-scope).

## Evidence and boundaries

- [Seven released class selections, ten biome resources, 320 Attercopus cases and 28 Spinoledon cases](https://herbertofury.github.io/Advent-of-Ascension/precasia-habitat-evidence-1.21.1.json)
- [Illustration source hashes](https://herbertofury.github.io/Advent-of-Ascension/precasia-habitat-art-evidence-1.21.1.json)
- [Bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1) · [Beginner walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Beginner-Walkthrough)

The arithmetic cases isolate custom predicates and do not execute Minecraft classes. They do not establish spawn frequency, exact collision/fluid placement, mob movement, AI safety or modpack compatibility. Creatures without these seven inspected paths, including special/event encounters, are not assigned invented natural-spawn rules. AoA portraits: Tslat and contributors.
