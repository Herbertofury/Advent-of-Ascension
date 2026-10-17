[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Versions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Worlds](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Systems](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Systems) · [Progress](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Progress)

# Skills & player progression

[![Advent GUI reference](https://static.wikia.nocookie.net/adventofascension_gamepedia/images/f/fb/Advent_GUI.png/revision/latest/scale-to-width-down/1200?cb=20230814094025)](https://adventofascension.fandom.com/wiki/Skills)

*Upstream Advent GUI reference, hosted by the official community wiki. Tslat and wiki contributors credited. The image is illustrative of that source generation, not a current-build test.*

<!-- checked-skill-guides-start -->
## Choose a checked walkthrough

### Historical 1.12.2 / AoA 3.3.6

These guides explain the selected historical release. Read each guide’s limits before treating a retained definition as a working training action.

| Topic | Walkthrough covers |
|---|---|
| [Hunter](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2) | 71 illustrated defaults, level and XP sorting, attack permission and separate drop eligibility |
| [Butchery and Innervation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2) | Combat eligibility, temporary pickups, Rage, health and displayed-level XP |
| [Runation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runation-Rune-Shrines-and-Inputs-1.12.2) | Four-post layout, fourteen rune tiers, input preparation and practice warnings |
| [Infusion crafting and enchanting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-and-Enchanting-1.12.2) | 386 recipes, separate base slot, 37 enchantment families and actual XP defaults |
| [Extraction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2) | Lava device, bowl recipes, success gate, 23 loot entries |
| [Anima](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) | Plant eligibility, temporary stones, fragment growth and distinct XP formulas |
| [Soul Tablets / Anima](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Tablets-Effects-and-Ownership-1.12.2) | 17 tablet effects, recipes, Soul costs and ownership/reload limits |
| [Foraging and Logging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2) | Break-action gates, 21 reward entries and the extra-log branch |
| [Augury](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Augury-and-Ascension-Shrine-1.12.2) | Inactive released shrine distinguished from retained definitions and older source |
| [Hauling](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2) | Rod recipe, catches, box rewards and Forge fishing-hook context |
| [Infusion](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2) | Eight Pixons, bowl requirements, harvest XP and whole-stack stone conversion |
| [Skill Crystals and boxes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.12.2) | 77 reward entries, lowest eligible skill selection and interactive planner |

[Plan a Skill Crystal target](https://herbertofury.github.io/Advent-of-Ascension/skill-crystal-planner.html) · [Filter the historical tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.12.2)

### Modern 1.21.1

Start with [modern skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1), [ability unlocks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Skill-Unlocks), and [Skill Master / Archaic Token progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1). Historical and modern Infusion Table pages describe different release systems; choose the page matching the game version.

Coverage remains open for historical skill systems without a checked training walkthrough. The source-family overview below is a declaration map, not a claim that every training action or cross-version restoration is finished.
<!-- checked-skill-guides-end -->

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
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sources-and-Credits). Source presence is not target runtime proof.
