[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Versions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Worlds](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Systems](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Systems) · [Progress](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Progress)

# Version atlas · choosing the complete source set

![Version lineage](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/version-lineage.svg)

## Recommended roles

| Minecraft / AoA | Role in this project | What it does not establish |
|---|---|---|
| 1.7.10 historical branch | Archaeology for early mechanics, IDs and content absent from later branches | Modern loader compatibility or a safe direct save upgrade |
| 1.12.2 / 3.3.6 (latest listed on Modrinth) | Intermediate lineage and additional historical behavior evidence | Every feature from earlier 1.12 builds; removed content needs earlier commits/releases |
| 1.16.5 / 3.6.11 | Main legacy breadth reference for the older dimension/content generation | All earlier skill systems, all newer redesigns, or every realm being normally accessible |
| 1.20.1 / 3.7.1 | Modern Forge-era source/reference release | The complete legacy dimension roster |
| 1.21.1 / 3.7.16.1 | Latest listed upstream release in the reviewed official metadata; NeoForge | A complete restoration or a Forge 1.20.1 binary |

**For ordinary play with broad older realm content:** the 1.16.5 legacy release is the relevant reference. **For the latest overhauled content:** use the version-matched 1.21.1 release and dependencies. **For the owner’s complete AoA:** use a reconciled source/content union and a verified target build. Installing those incompatible JARs together will not merge their features.

[Official versions/downloads](https://modrinth.com/mod/adventofascension/versions) · [Exact filenames, release metadata and published hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/release-evidence.json).

## Source signals measured in this review

| Observation | 1.16.5 branch | 1.20 branch | 1.21 branch |
|---|---:|---:|---:|
| Active living-entity declarations in inspected mob/animal/NPC registries | 419 | 285 | 83 |
| Skill registry declarations | 5 | 10 | 10 |
| Dimension JSON files | 21 | 10 | 10 |
| Item-name localization keys | 1,495 | 1,353 | 1,162 |
| Block-name localization keys | 1,201 | 1,188 | 1,209 |

These counts measure **different source signals**, not playable-content totals. Commented-out registry declarations were excluded. Dimension keys and data files can remain when a realm is not supported for survival. Localization can outlive removed content. A registered skill can have only a thin class while its deeper implementation remains elsewhere or incomplete. Never turn these counts into a completion percentage.

## What changed between generations

The official wiki distinguishes legacy dimensions from the newer overhaul. Its reviewed front page identifies Overworld/Nether content as complete in the modern scope and Nowhere/Precasia as playable but still incomplete in some areas. That does not certify all historical realms for modern releases. The 3.6 line also changed the skill design, so 1.16.5 is not a universal snapshot of all earlier mechanics.

A concrete modern example: the 3.7.1 changelog records Precasia advancement changes, a Nowhere arena, and a blaster hitscan trial affecting named weapons. It also explicitly distinguishes an added nest asset from actually placing it in the game. Our records must preserve that distinction.

## Merge policy

For every same-ID old/new pair: compare appearance, AI, stats, drops, progression role, save shape and API dependencies. Choose retained behavior or an explicit supported variant. Do not silently overwrite old content with a newer same-name object. Record approved aliases and migration transforms. Earlier removed features require their own source-era evidence before inclusion.

**Primary target:** continue the target accepted by the active Enderloom conversion session. A source reference for 1.20.1 does not prove the current local job is targeting it. Do not restart or retarget that job from this documentation alone.


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sources-and-Credits). Source presence is not target runtime proof.

## Released 1.20.1 renderer gap audit

AoA 3.7.1 contains 186 temporary-renderer assignments referencing 181 distinct entity fields; 173 of those targets are in the inspected living-entity roster. Five named NPC renderer fields instead reference Primordial Banker in the released binary, while the pinned source has corrected targets. [Exact evidence and restoration checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Renderer-Gaps-1.20.1). Registration and asset presence must not be treated as proof of a complete playable port.
