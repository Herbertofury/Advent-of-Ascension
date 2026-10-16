# Loot Tables and Global Modifiers · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** A mob’s named table is only part of the loot story. Blocks, chests, item rewards, global modifiers and code-side drops can all matter.

## Open the complete inspected resource index

[**Browse loot resources and modifier conditions**](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1)

The index contains **1,315 table resources**: 1,314 in the AoA namespace and one bundled Minecraft-namespace Wither override. It also includes the **25 modifier definitions** listed in the shipped global-modifier registration file. These are **1,340 reference records**, not 1,340 guaranteed obtainable rewards.

| Reference group | Records |
|---|---:|
| Block tables | 1,166 |
| Entity tables, including the Wither override | 91 |
| World tables | 24 |
| Miscellaneous tables | 14 |
| Item reward tables | 7 |
| Other reward tables | 6 |
| Structure tables | 4 |
| Archaeology tables | 2 |
| Advancement table | 1 |
| Registered global modifiers | 25 |

There are base image references for **1,472 item IDs**. Seventeen additional current-version image references close gaps in the existing atlases, including a separately verified neutral Wither Skeleton Skull model. Component-specific appearances, animation and runtime renderer states are not certified by these pictures.

## Use it in three steps

1. **Search an item or rule.** Try `ivory`, `silk touch`, `raw limonite`, `nether star`, or an exact resource ID. Exact item references rank ahead of merely similar block names.
2. **Choose the kind of evidence.** Filter block drops, structures, world tables or global modifiers. The vanilla-namespace override has its own visible label.
3. **Expand the conditions.** Each pool shows its rolls, entries, declared weights, operations and exact condition arguments. Follow nested-table links rather than assuming the nested reward is unconditional.

Item names link to other indexed loot references for that item, and item entries also link to recipe search. The inventory explorer now links **1,173 exact-ID block/item resources** directly; other 1.21.1 entries open a contextual resource search. The older mob-only finder remains available and clearly labeled.

## Example 1: Limonite Ore is not always the same drop

| Ore-block reference | Raw-material reference |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/loot-guide-icon-1.21.1-aoa3-limonite_ore.webp" width="112" height="112" alt="Limonite Ore"> | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/loot-guide-icon-1.21.1-aoa3-raw_limonite.webp" width="96" height="96" alt="Raw Limonite"> |

The inspected resource uses an **alternatives** entry. One child is the ore block, gated by a tool predicate requiring Silk Touch level at least one. The other is Raw Limonite, with Fortune’s ore-drop operation and explosion decay. Do not read the two children as a guaranteed pair of outputs.

[Inspect the exact Limonite Ore table](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=aoa3%3Ablocks%2Flimonite_ore) · [Mining and tool requirements](Mining-and-Ore-Generation-1.21.1)

A loot resource does not itself prove that a given tool can harvest the block. Harvest requirements, game rules and other handlers remain separate checks.

## Example 2: Ivory comes through a global modifier

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/loot-guide-icon-1.21.1-aoa3-ivory.webp" width="96" height="96" alt="Ivory">

The shipped `misc_ivory` modifier declares one Ivory and a random gate of **0.33333334**, plus an entity-type condition covering **Hoglin, Zoglin, Ravager or Goat**. That is why looking only at AoA entity-named tables can miss this acquisition reference. The numeric gate is not a universal “all mobs drop Ivory” rule.

[Inspect the Ivory modifier and all its conditions](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=modifier%3Aaoa3%3Amisc_ivory)

Global modifiers operate on generated loot, and later modifiers can further change the result. Their registration order therefore matters. AoA’s bundled registration uses `replace: false`; a modpack’s effective data stack still needs checking. [NeoForge’s version-matched modifier documentation](https://docs.neoforged.net/docs/1.21.1/resources/server/loottables/glm/).

## Example 3: world bonuses have extra gates

The shipped `world_tables` modifier requires a player kill, AoA’s hostile-entity predicate, and the absence of the matching `NeoForgeData` spawner flag. Its explicit map contains **four** worlds:

| Dimension | Extra table reference |
|---|---|
| Overworld | `aoa3:worlds/overworld` |
| Nether | `aoa3:worlds/nether` |
| Barathos | `aoa3:worlds/barathos` |
| Precasia | `aoa3:worlds/precasia` |

The source and released event code write `aoa3_spawned_by_spawner = true` for spawn types recognized by the spawner predicate, and also for children in the mob-split event. This can suppress **this extra world-table reward**; it does not mean the mob’s ordinary loot table becomes empty.

The inspected handler also requires an entity context, a mapped dimension and a nonempty entity-context table. It rolls that table through the raw-generation method rather than blindly re-entering the global modifier chain.

[World-modifier conditions and mappings](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=modifier%3Aaoa3%3Aworld_tables) · [Released hook checks](https://herbertofury.github.io/Advent-of-Ascension/world-loot-hook-evidence-1.21.1.json)

### Looking for coins or portal runes?

The Overworld world-table resource includes Copper Coins and the carved runes of **Direction, Reality, Space and Travel**, alongside empty choices and other supplies. The Power rune is not among those four listed rune entries. Conditions and random selection still apply; a qualifying kill is not a guaranteed coin or rune.

[Inspect the Overworld world table](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=aoa3%3Aworlds%2Foverworld) · [Portal construction and Power rune recipe](First-Portal-Walkthrough) · [Trading alternatives](Trading-and-Traders-1.21.1)

There are 24 world-table files in the archive, but this modifier’s explicit map does **not** activate all 24. Other callers may exist; file presence alone is not an activation proof.

## Example 4: a missing table entry is not always a missing drop

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/loot-guide-icon-1.21.1-minecraft-nether_star.webp" width="96" height="96" alt="Nether Star">

AoA supplies a `minecraft:entities/wither` table override with additional reward pools. That resource does not list a Nether Star. It would be wrong to conclude from that omission alone that AoA removed Nether Stars.

The checked **vanilla 1.21.1 WitherBoss custom-death-loot method separately calls a Nether Star spawn**, then applies extended lifetime when the returned item entity is nonnull. The vanilla table itself has no pools. This code-side reference is shown separately in the viewer, rather than falsely inserted into the table’s declared outputs. Engine callback gates and mod hooks can still change an actual modpack outcome.

[Wither override plus separate code note](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=minecraft%3Aentities%2Fwither) · [Exact vanilla method evidence](https://herbertofury.github.io/Advent-of-Ascension/wither-code-drop-evidence-1.21.1.json)

## Read chest and item rewards without inventing certainty

The Precasian Lotto Hovel resource has a main pool with ten base rolls and a separate one-roll book-related pool. Empty entries, item weights, count operations and bonus-roll providers are retained in the viewer. This does not promise ten unique items, a particular weapon, or the book-related reward.

[Precasian Lotto Hovel loot](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=aoa3%3Astructures%2Fprecasia%2Fprecasian_lotto_hovel%2Fmain) · [Find the hovel](Finding-Traders-1.21.1) · [Item reward resources](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&category=items)

Weights describe relative selection among eligible choices. Conditions can remove choices, quality can interact with luck, and multiple rolls or functions can change the result. A displayed weight of 30 is not automatically a 30% final drop rate. [NeoForge loot-table concepts for 1.21.1](https://docs.neoforged.net/docs/1.21.1/resources/server/loottables/).

## What the viewer does not claim

- A resource matched by name is not a verified runtime method binding.
- Empty declared pools or no static modifier outputs do not prove that code cannot create loot.
- A nested-table reference is conditional evidence, not an unconditional reward bundle.
- Base item pictures do not prove metadata, custom names, potion effects, book contents or dynamic render states.
- Datapack priority, effective modifier ordering and other mods must be tested in the actual target installation.
- No in-game drop-rate, balance, performance or complete Enderloom compatibility certification is claimed.

The original normalized schema keeps source paths/hashes, conditions and operations for inspection. It is documentation, not a drop-in redistribution of the original resource files. Category facts and icon metadata load only when a reference is expanded; ordinary inventory startup does not fetch this extra catalog.

## Restoration acceptance targets

- [ ] Preserve Silk Touch, Fortune, explosion handling and block-state conditions when adapting loot.
- [ ] Preserve modifier ordering and the effective registration merge behavior.
- [ ] Test player-kill, hostile-entity and spawner/split-child gates independently from ordinary mob loot.
- [ ] Verify persistent-data serialization names against the predicate’s `NeoForgeData` path when porting loaders.
- [ ] Keep raw nested world-table rolls from accidentally applying the entire modifier chain recursively.
- [ ] Preserve code-side drops such as the Wither’s Nether Star when changing table resources or entity methods.
- [ ] Test effective datapacks, save/reload and native client/server behavior before closing the affected runtime checklist entries.

## Evidence and credits

[Extraction coverage and registration hashes](https://herbertofury.github.io/Advent-of-Ascension/loot-reference-extraction-proof-1.21.1.json) · [Index](https://herbertofury.github.io/Advent-of-Ascension/loot-reference-index-1.21.1.json) · [Item-image references](https://herbertofury.github.io/Advent-of-Ascension/loot-reference-icons-1.21.1.json) · [Exact-ID inventory links](https://herbertofury.github.io/Advent-of-Ascension/inventory-loot-reference-links-1.21.1.json)

AoA art and systems: **Tslat and contributors**. Vanilla art and code references: **Mojang**. Java/game classes are read as data; the documentation tools do not launch the game.
