# Legacy attribute field guide · 1.12.2

[Open the Bestiary Observatory](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html)

**485 source-mapped entities · 2,221 resolved literal getter values.** Search by creature name, registry ID or source class; filter by source category; sort by base health or melee value. Each card includes a source-model portrait where available and expandable getter provenance.

## What is measured

The reader inspects the official AoA 3.3.6 class files without launching Minecraft or a JVM. It follows the artifact's actual superclass names and accepts only a single literal numeric return, optionally with a supported numeric widening conversion. A nonliteral or abstract override stops resolution; the reader does not incorrectly substitute a parent value. Each result identifies its declaring class, SHA-256, method descriptor and inheritance depth.

The fields cover max-health, melee, projectile, armour/armor, movement-speed and knockback-resistance getters. Spawn-chance-factor getters are included in the detailed evidence, without treating a factor as a percentage. If differently named armour or movement getters disagree, the interface reports multiple getters rather than silently choosing one. Missing, nonliteral and zero are distinct states.

[Full artifact getter evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-attribute-getters-1.12.2.json) · [Compact viewer data](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bestiary-data-1.12.2.json)

## Base values are not final in-game attributes

Configuration, difficulty logic, attribute modifiers and encounter state can change actual results. For example, [AoAMeleeMob](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/base/AoAMeleeMob.java) applies hardcore-mode multipliers of 2× max health, 1.5× melee damage and 1.25× armour in its attribute setup. This example must not be blindly applied to every unrelated base class.

Movement values are attribute scalars, not travel speed in blocks per second. Projectile getters may be dynamic. A source category such as `mobs` or `animals` is a code organization label, not a complete spawn biome or behavioral classification.

## Verified examples

- [Creep Cow](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/animals/EntityCreepCow.java): literal base-health getter 20 and movement getter 0.2 in the artifact.
- [Shadow](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/mobs/overworld/EntityShadow.java): literal base-health getter 0.5. It has no invented body portrait; its card links to the particle/invisible-body explanation.
- All 485 cards passed construction tests. Search, health sorting, pagination and missing/nonliteral/conflicting-getter cases were tested locally. Deployed browser verification is recorded separately below when complete.

## Performance and scope

The viewer loads one approximately 240 KB data file and builds a search index once. It initially creates 36 cards, with more on request; images load lazily. Repeated filtering does not rescan game files or refetch the evidence dataset. The larger provenance JSON remains available separately for inspection.

These records cover source-mapped entities with the selected getter methods. They do not certify a complete runtime entity registry, final stats, spawn probabilities, AI, loot chances, converted gameplay or multiplayer behavior. Portraits remain version-scoped reference renders.

[Cross-version bestiary](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bestiary) · [Historical visual atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Atlas-1.12.2)
