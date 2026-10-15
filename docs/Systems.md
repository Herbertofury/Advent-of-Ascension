[Home](README.md) · [Versions](Version-Matrix.md) · [Worlds](Dimensions.md) · [Systems](Systems.md) · [Progress](Progress.md)

# Systems guide · the complete gameplay chain

| System | Player experience | What the complete project must preserve |
|---|---|---|
| Exploration & realm access | Discover routes into distinct worlds | Keys/portals, conditions, return travel and save-safe dimension identity |
| Skills & abilities | Progress through actual activities | XP, unlocks, formulas, display, commands and multiplayer authority |
| Combat & equipment | Use each weapon family and fight varied enemies | Damage rules, ammunition/resources, charge/reload, AI, effects and loot |
| Boss encounters | Earn access, survive mechanics, receive rewards | Summoning/arenas, phases, resets, multiplayer and repeatability |
| Economy & NPCs | Trade, obtain specialist resources and interact | Spawn conditions, profession/trade data, prices, inventories and persistence |
| Crafting & processing | Turn discoveries into equipment/progression | Recipes, tags, stations, fuels/input validation and automation semantics |
| World generation | Explore recognizable realms and structures | Biomes, features, structures, spawn tables, terrain and deterministic settings |
| Player presentation | Understand state through the Advent GUI and feedback | HUD, icons, bestiary/lore, sounds, particles, localization and accessibility |
| Saves & networking | Return to an intact world and play with others | IDs, NBT/components, synchronization, migration and restart behavior |
| Integrations | Coexist with the intended modpack | Exact dependency closure, optional-mod presence/absence and renderer behavior |

## Do not mistake a registry census for the game

A creature needs behavior, rendering, audio, drops and spawning. A weapon needs its damage/resource/animation loop. A realm needs a working travel and progression loop. The machine census helps find gaps, but cannot independently prove any of these chains.

## What “ultimate” means here

The accepted historical union remains the minimum. Modern redesigns should improve presentation and behavior without silently deleting legacy identity or mechanics. New optional variants must be named and documented as project additions, not attributed to upstream. Every improvement is paired with compatibility and equivalent-work performance checks.

Use [Content Specification](Content-Specification.md) as the detailed record contract and [Roadmap](Roadmap.md) for completion gates.


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](Sources-and-Credits.md). Source presence is not target runtime proof.
