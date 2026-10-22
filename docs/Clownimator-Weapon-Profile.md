# Clownimator · three red flags, one sniper identity

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and proposed visuals. No native upgrade acceptance.**

## Current selected concept · 22 October 2026

![Clownimator selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-clean-hero-concept-v6.png)

Clean three-pole hero with obsolete transition panels removed. Corrected gameplay direction: each pole owns paired cloth halves that split into an aperture; poles rise/lower until all three apertures align, then restore idle. Focused appearance retained; replacement integrated transition art and native implementation remain open.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Aclownimator). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

Dedicated supplemental studies (partial design candidates, not implemented features):

- [Focused appearance reference ONLY; lower side transition superseded](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-ribbon-focused-view-study-v2.png).
- [Geometry-guided three-pole alignment study; full weapon transition and cloth physics remain open](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-split-flag-alignment-study-v1.png).

## What the original does

Clownimator uses **Metal Slugs** and **SCOPE_3**. Its special damage hook checks whether the target is living and its **maximum health is strictly below 75**. Only then does it multiply the incoming bullet-damage multiplier by **1.15**, before delegating to the inherited damage path.

This is not a check of current remaining health, a 75% health threshold or an automatic finishing move. A high-maximum-health target does not become eligible merely because it is injured; exactly 75 is outside the condition. Native attributes, other mods and damage defenses still affect actual results.

| Released input | Value |
|---|---:|
| Damage | 49.5 |
| Durability | 545 |
| Firing delay | 95 ticks, nominally 4.75 seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.035 |
| Ammunition | Inherited Metal Slug |
| Scope | SCOPE_3 |
| Firing sound | Medium sniper, long variant |

Constructor inputs and a conditional multiplier are not a measured final-damage result. The three top ornaments are not evidence of a three-projectile shot or three functional barrels. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Clownimator.java) · [Pinned evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/clownimator-released-evidence.json).

## Preserve its original identity

![Released Clownimator sprite on a neutral alpha-composited background](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-original-preview.png)

Keep the compact silver/charcoal body, red-and-pale-silver front/rear panels, short dark muzzle, gray rear grip, long dark upper sight and three red dorsal flag shapes. The owner-reviewed upgrade direction uses red fabric flags on black poles, fixed in one front-to-back row along the barrel. They are visual identity anchors, not a reason to add extra shots; this does not claim cloth simulation exists in the released sprite.

## Upgrade route

![Decimator and Clown Upgrade Kit produce Clownimator](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-clownimator.webp)

**Decimator + Clown Upgrade Kit → Clownimator.** The bundled Divine Station recipe establishes the upgrade relationship. It does not by itself prove a maker, workshop or exact dimension of manufacture. Preserve legitimate customization during upgrades without duplicating items or copying incompatible properties. [Divine upgrade atlas](Divine-Station-Upgrade-Atlas).

## Earlier preserved art: fabric flags and ribbon-sight concept

![Clownimator concept with fixed inline flagpoles and a converging ribbon-sight variant](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-inline-ribbon-concept-v4.png)

[Compare the released original with the current concept](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Aclownimator).

The three red textile flags remain tethered to black poles in a longitudinal row along the barrel. The sight variant gathers the cloth into one open aiming shape without moving the poles sideways. The aiming center must stay stable and clear; flutter belongs outside the aperture, not in the authoritative shot direction.

**Required gameplay attachment, still pending integration:** equipped by default on eligible flagged clown weapons, removable, and able to preserve an explicit off state across switching, re-equipping and save/reload. Off must retain a usable aiming view. The converging-ribbon animation is an optional sight variant, with reduced-motion support, interruption recovery and multiplayer synchronization still to verify. It must not silently change Metal Slug costs, source scope behavior, damage conditions or firing cadence.

**Status:** concept panels exist. Native cloth/rendering, attachment UI and persistence, networking, real hand fit, sight alignment and equivalent-work performance are not accepted. The earlier rigid-crown treatment is retained below as a past concept, not the current design target.

### Earlier premium treatment (v2), preserved

![Revised Clownimator concept with one rear grip and three red crowns](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-concept-v2.png)

V2 removes the incorrect forward grip and puts the single hand grip behind the trigger in both main views. Three folding red metal crowns, red enamel and pale metal preserve the original’s carnival identity. Crown folding is a proposed inspection flourish; the sight line, folding sweep, actual hands and first-person proportions still need tests. Neither the hinge drawing nor an open painted guard is a completed mechanism/clearance result.

<details><summary>Retained V1: rejected grip arrangement</summary>

![Earlier Clownimator concept with grip incorrectly ahead of the trigger](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clownimator-concept-v1.png)

The hanging forward grip and ambiguous rear control arrangement do not pass hand-layout review. Retained for the crown/material direction only.

</details>


## Complete feature plan

- **Shape/materials:** original-fit and premium treatments with purposeful red enamel, pale metal and charcoal surfaces; exact concept/model comparisons, UVs, normals and small-scale readability.
- **Motion:** equip, idle, movement, aim, firing/recovery, optional reload, inspection and interrupt recovery. Flag flutter and ribbon convergence are proposed cosmetic motion with fixed roots, explicit clearances and a stable aiming opening, not another attack.
- **Parts/variants:** optic casings, removable flag/ribbon sight variants, restrained shroud modules and grip skins. Any new shot behavior requires its own declared damage, resource, cadence and server authority.
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

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](Effective-Recoil-Routing-1.20.1).
