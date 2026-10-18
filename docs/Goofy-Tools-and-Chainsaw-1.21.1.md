# Goofy tools and the Chainsaw

**Minecraft 1.21.1 · AoA 3.7.16.1.** These implementations exist in the inspected archive; their acquisition is not established by a shipped crafting recipe. Do not mistake a registered item or source implementation for a tested survival reward.

![Goofy tool repair periods and the Chainsaw log effect](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/goofy-chainsaw-overview-1.21.1.webp)

[Other special pickaxes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Pickaxes-Charging-and-Mining-Safety-1.21.1) · [Mining and ores](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mining-and-Ore-Generation-1.21.1) · [Item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1)

## The four tools

| Tool | Preview | Exact item |
|---|---|---|
| Goofy Pickaxe | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/goofy-chainsaw-goofy_pickaxe.webp" width="64" alt="Goofy Pickaxe"> | [Item card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:goofy_pickaxe) |
| Goofy Axe | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/goofy-chainsaw-goofy_axe.webp" width="64" alt="Goofy Axe"> | [Item card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:goofy_axe) |
| Goofy Shovel | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/goofy-chainsaw-goofy_shovel.webp" width="64" alt="Goofy Shovel"> | [Item card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:goofy_shovel) |
| Chainsaw | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/goofy-chainsaw-chainsaw.webp" width="64" alt="Chainsaw"> | [Item card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:chainsaw) |

## Goofy tools: repairing one durability at a time

Each of the three Goofy tools has the same inventory-tick rule. It runs only on the server and only when the stack is damaged. At an eligible boundary, damage decreases by one. For a player entity, the method also broadcasts inventory-menu changes.

| Callback state | Boundary period | Nominal time at 20TPS |
|---|---|---|
| selected flag is true | 120 world ticks | 6 seconds |
| selected is false and reported slot is below 9 | 200 world ticks | 10 seconds |
| other reported slot | 280 world ticks | 14 seconds |

These are **world-time modulo boundaries**, not a fresh countdown from the moment the item takes damage or moves slots. The first eligible callback can repair sooner than a full period. Lag changes wall-clock timing. The callback must actually run; this does not promise repairs in arbitrary chests or unloaded storage.

For ordinary main-inventory use, this explains the selected/hotbar/other-slot distinction. Do not extend that explanation to an exact offhand rate without testing the target loader. The unmodified Minecraft1.21.1 inventory tick loop uses indices within each compartment, not a universal global slot number; the selected flag and slot parameters must be interpreted in the actual callback context.

## Configured tier inputs

| Tier | Base speed | Durability | Damage builder input | Enchantment value |
|---|---:|---:|---:|---:|
| Goofy | 8 | 1500 | 0 | 15 |
| Chainsaw | 18 | 2500 | 9 | 0 |

The inspected builder converts the damage input to a tier bonus by subtracting one. These are tier configuration values, not universal final combat damage. Both tiers choose an empty repair ingredient through noRepair(); that does not by itself prove that every enchantment or external repair system is impossible.

## Chainsaw: brief log-mining effect, not whole-tree felling

On a server-side mineBlock callback, the Chainsaw plays its use sound. If the block is an AoA LogBlock or matches Minecraft's LOGS tag, it requests a **10-tick Haste effect at level30**. The bundled EffectBuilder converts level30 to **amplifier29**, with ambient presentation, hidden particles and hidden effect icon.

At nominal20TPS, ten ticks is half a second. Actual effect admission, stronger existing effects, loader hooks and other mods still need testing. This is not a guaranteed final mining speed.

The selected callback contains no recursive tree traversal. Do not advertise whole-tree felling based on the item's name. Its hurtEnemy override plays a server-side sound and requests main-hand item damage, but the complete wear-per-hit contract also depends on callers. The shield-disabling override returns false and the use-animation value is NONE.

## Acquisition and data boundaries

The exact-ID resource scan found seven tag resources and no recipe references for these four IDs. The three Goofy tools are in the hidden-from-recipe-viewers tag. The resources also place the tools in relevant pickaxe/axe/shovel/mining/melee/durability categories.

This is not proof that the items are unobtainable through all code-side rewards, commands or modpacks. An actual acquisition route must be established before presenting them as craftable survival equipment.

## What was checked, and what remains

The evidence records six AoA class selections, two exact tier-assignment segments, the bundled effect-builder methods, a separately identified vanilla inventory callback, seven data resources and **384 deterministic repair-policy cases**. No game was executed.

Still test real inventory/offhand behavior, multiplayer synchronization, repair-menu interactions, enchantments, logs supplied by other mods, effect replacement and actual acquisition. Do not convert these source observations into a no-lag or compatibility guarantee.

[Machine-readable evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/goofy-chainsaw-evidence-1.21.1.json) · [AoA source pin](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16)

AoA artwork and implementations: Tslat and contributors. Comparison layout and inspection tooling: this documentation project.
