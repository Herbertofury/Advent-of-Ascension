[Home](README.md) · [Versions](Version-Matrix.md) · [Worlds](Dimensions.md) · [Systems](Systems.md) · [Progress](Progress.md)

# Skills & player progression

[![Advent GUI reference](https://static.wikia.nocookie.net/adventofascension_gamepedia/images/f/fb/Advent_GUI.png/revision/latest/scale-to-width-down/1200?cb=20230814094025)](https://adventofascension.fandom.com/wiki/Skills)

*Upstream Advent GUI reference, hosted by the official community wiki. Tslat and wiki contributors credited. The image is illustrative of that source generation, not a current-build test.*

## Source-observed skill families

| Skill | 1.16.5 active declaration | Modern active declaration | Detailed acceptance focus |
|---|---|---|---|
| Alchemy | No | Yes | Actual activity/XP/reward data and implementation; registration alone insufficient |
| Artifice | No | Yes | Actual activity/XP/reward implementation and its historical relationship |
| Creation | No | Yes | Summoning/creation semantics, ownership and persistence where implemented |
| Dexterity | Yes | Yes | Movement-related activity accounting, XP and ability effects |
| Extraction | Yes | Yes | Resource acquisition hooks, eligible blocks/actions and reward accounting |
| Farming | Yes | Yes | Crop/activity conditions, reward rules and anti-duplicate handling |
| Faunamancy | No | Yes | Creature interaction/sacrifice conditions in the inspected implementation |
| Hauling | Yes | Yes | Fishing/activity rewards and progression state |
| Imbuing | No | Yes | Real activity/XP/reward implementation beyond the registry entry |
| Innervation | Yes | Yes | Combat contribution, kill credit and progression rewards |

The inspected modern Alchemy, Artifice, Creation and Imbuing classes are thin constructors over the shared skill base. That is not enough to certify full gameplay; inspect their data, events and consumers. Other inspected classes expose specific event hooks. The shared base carries level/XP/cycle state and NBT/synchronization behavior. Keep server-authoritative state, client display and migration separate.

## Historical systems must not disappear

Older names such as Expedition belong to a distinct historical design. The official removed-feature record places its removal in the 1.16.5-3.6 public-alpha transition. Do not assume Dexterity is a byte-for-byte replacement or discard earlier rewards simply because the names changed. Build an explicit old-skill → modern-skill/retained-variant mapping from the accepted source union.

## Required detailed record

XP sources and eligibility; formulas and multipliers; level caps/cycles; unlock thresholds; ability effects; UI icons/tooltips; commands/configuration; death handling; save/restart; multiplayer sync; migration of old XP/levels; regression tests for duplicate rewards and invalid actions. Formula values must come from the selected release, not a mixed-era web table.

A visible skill icon is not a completed progression system. Each activity and unlock must be exercised in the target game.


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](Sources-and-Credits.md). Source presence is not target runtime proof.
