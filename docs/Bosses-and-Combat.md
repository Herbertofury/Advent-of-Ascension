[Home](README.md) · [Versions](Version-Matrix.md) · [Worlds](Dimensions.md) · [Systems](Systems.md) · [Progress](Progress.md)

# Bosses, combat & equipment

## Version-specific encounter identity

The modern monster registry contains declarations for Smash, Nethengeic Wither, King BamBamBam, Tyrosaur and Skeletron, including elite variants, plus Wounded Tyrosaur. The [Bestiary](Bestiary.md) links exact declarations and records the broader legacy roster. Declaration is not proof of a complete arena, spawn route or reward loop.

A legacy boss and a redesigned same-name boss may have materially different mechanics. Keep their dossiers separate until the accepted merge decision specifies which behavior, art, drops and progression each target must preserve.

## Encounter dossier

- Source version, ID/aliases, boss/elite/variant relationship.
- Entry route, summoning requirements, arena and reset conditions.
- Health/defense/damage/immunities with the exact difficulty/config basis.
- Attacks, telegraphs, cooldowns, movement, phases and counters.
- Multiplayer targeting/scaling, ownership and disconnect behavior.
- Models, animation, sound, particles, hitboxes and camera effects.
- Loot, advancement/progression rewards, repeatability and failure recovery.
- Test evidence: summon, engage every phase, defeat, receive rewards, save/reload and repeat.

## Equipment families

Catalog melee weapons, ranged weapons, ammunition/resource systems, armour, tools and utility items with source-era distinctions. The [Item Atlas](Items-Atlas.md) is the name-evidence index, not a guarantee of obtainability.

The 3.7.1 changelog is an example of why behavior matters: selected blasters moved into a hitscan trial, and cannon damage treatment changed. An old projectile-only implementation with the same item ID would not automatically reproduce that release. Keep charge behavior, resources, particles, server/client responsibilities and damage formulas in the equipment record.

## No-loss balance policy

Do not buff every weapon or flatten every encounter to make the mod feel newer. Preserve the selected baseline first; record intentional balance changes separately and test against the full progression curve. No disabled AI, missing effects or simplified boss phase may masquerade as a performance optimization.


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](Sources-and-Credits.md). Source presence is not target runtime proof.
