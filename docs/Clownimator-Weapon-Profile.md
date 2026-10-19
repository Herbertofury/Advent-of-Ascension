# Clownimator · three red crowns, one sniper identity

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and proposed visuals. No native upgrade acceptance.**

## What the original does

Clownimator uses **Metal Slugs** and **SCOPE_3**. Its special damage hook checks whether the target is living and its **maximum health is strictly below 75**. Only then does it multiply the incoming bullet-damage multiplier by **1.15**, before delegating to the inherited damage path.

This is not a check of current remaining health, a 75% health threshold or an automatic finishing move. A high-maximum-health target does not become eligible merely because it is injured; exactly 75 is outside the condition. Native attributes, other mods and damage defenses still affect actual results.

| Released input | Value |
|---|---:|
| Damage | 49.5 |
| Durability | 545 |
| Firing delay | 95 ticks, nominally 4.75 seconds at 20 TPS |
| Recoil modifier | Approximately 0.035 |
| Ammunition | Inherited Metal Slug |
| Scope | SCOPE_3 |
| Firing sound | Medium sniper, long variant |

Constructor inputs and a conditional multiplier are not a measured final-damage result. The three top ornaments are not evidence of a three-projectile shot or three functional barrels. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Clownimator.java) · [Pinned evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/clownimator-released-evidence.json).

## Preserve its original identity

![Released Clownimator sprite on a neutral alpha-composited background](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-original-preview.png)

Keep the compact silver/charcoal body, red-and-pale-silver front/rear panels, short dark muzzle, gray rear grip, long dark upper sight and three red folded crown-like shapes. Treat the red shapes as distinctive visual anchors, not a reason to add extra shots.

## Upgrade route

![Decimator and Clown Upgrade Kit produce Clownimator](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-clownimator.webp)

**Decimator + Clown Upgrade Kit → Clownimator.** The bundled Divine Station recipe establishes the upgrade relationship. It does not by itself prove a maker, workshop or exact dimension of manufacture. Preserve legitimate customization during upgrades without duplicating items or copying incompatible properties. [Divine upgrade atlas](Divine-Station-Upgrade-Atlas).

## Proposed premium treatment

![Revised Clownimator concept with one rear grip and three red crowns](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-concept-v2.png)

V2 removes the incorrect forward grip and puts the single hand grip behind the trigger in both main views. Three folding red metal crowns, red enamel and pale metal preserve the original’s carnival identity. Crown folding is a proposed inspection flourish; the sight line, folding sweep, actual hands and first-person proportions still need tests. Neither the hinge drawing nor an open painted guard is a completed mechanism/clearance result.

<details><summary>Retained V1: rejected grip arrangement</summary>

![Earlier Clownimator concept with grip incorrectly ahead of the trigger](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-concept-v1.png)

The hanging forward grip and ambiguous rear control arrangement do not pass hand-layout review. Retained for the crown/material direction only.

</details>

## Complete feature plan

- **Shape/materials:** original-fit and premium treatments with purposeful red enamel, pale metal and charcoal surfaces; exact concept/model comparisons, UVs, normals and small-scale readability.
- **Motion:** equip, idle, movement, aim, firing/recovery, optional reload, inspection and interrupt recovery. Crown folding/bobbing is proposed cosmetic motion with explicit clearances, not another attack.
- **Parts/variants:** optic casings, crown ornament sets, restrained shroud modules and grip skins. Any new shot behavior requires its own declared damage, resource, cadence and server authority.
- **Feedback:** original/new flight and impact captures, selectable muzzle/tracer/projectile/surface impact treatments, expiring decals and confirmed-kill finishers. Conditional feedback must follow the actual confirmed rule rather than assuming a wounded target qualifies.
- **Personalization:** earned charms, gameplay bonuses only when declared, static/animated/glowing stickers, custom emblems, skins and effect selections.
- **Progression:** all module recipes, salvage, returns and upgrade/save conservation; optional reload-off behavior preserves native resource rules.
- **Compatibility/performance:** original fallback, TaCZ/turret qualification, multiplayer and attribute-mod tests; bounded game-time presentation and measured startup/memory/frame-time comparisons.

## Acceptance gates

- [ ] Native original shot, scope, sound, resource and impact captures
- [ ] Health-threshold boundary and modded-attribute tests
- [ ] Complete attachment, inspection, projectile, impact and finisher concepts
- [ ] Faithful mesh, both texture modes, real hands and moving clearances
- [ ] Native animation, multiplayer, migration and compatibility qualification
- [ ] Equivalent-scene performance and reduced-motion/effects options

[Weapon standard](Weapon-Completeness-Standard) · [Armory](Weapon-Overhaul)

Original AoA identity and assets: Tslat and contributors. Proposed materials, ornaments and effects remain separate from released mechanics. No native or final-art acceptance is promoted.
