# Destruction Shotgun: a shared boosted-shot roll

**AoA 3.7.1 / Minecraft 1.20.1. Source-backed profile and revised concept candidate. No accepted native upgrade.**

## What the weapon actually does

Destruction Shotgun is a **three-pellet Spreadshot weapon**. Its custom firing method rolls `oneInNChance(5)` once, before the pellet loop. The resulting boolean is shared by all three spawned pellets: each receives a damage multiplier input of **1.5 when selected, otherwise 1.0**. The released tooltip describes a 20% chance to deal 50% extra damage with a shot.

That is a shot-level roll, not three independent critical rolls. Preserve the shared decision when networking or adding visual feedback. Do not reroll it for each render pass, pellet trail or client. This class does not add an explosion hook: its name and gunpowder recipe are not evidence of explosive impact behavior.

| Released field | Value and boundary |
|---|---|
| ID | `aoa3:destruction_shotgun` |
| Stored damage input | 10.5; not guaranteed final damage |
| Pellet count | 3 |
| Durability | 690 |
| Delay | 56 ticks, nominally 2.8 seconds at 20 TPS |
| Recoil input | Approximately 0.45; not camera degrees |
| Knockback input | Approximately 0.4; not measured displacement |
| Ammunition | Spreadshot |
| Loop projectile | LimoniteBulletEntity, age input 4, piercing 0 |
| Shared boosted-shot input | One `oneInNChance(5)` result; multiplier 1.5 or 1.0 |
| Mode / sound | Non-automatic; heavy long shotgun sound selector |

Actual damage still depends on the shared attack path, enchantments, immunity and hit handling. Three pellets do not establish guaranteed 31.5 or 47.25 total damage. Native tests must confirm the observable frequency and behavior of the boosted shot.

## Original appearance and design anchors

![Actual released Destruction Shotgun sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/destruction-shotgun-original-preview.png)

Preserve three dominant swept crimson upper forms, warm orange inserts, charcoal lower frame, gray rear connector and red grip heel. The newly engraved metal and articulated inspection fins are proposed interpretations. The source does not establish an official maker, armor material or destructive laser mechanism.

## Infusion and upgrade tutorial

The released **AoA infusion** recipe uses a **Shotgun Frame** as input, plus:

- Hardened Confetti Ball ×1
- Unstable Gunpowder ×1
- Two ingredients matching `forge:ingots/emberstone`
- Two ingredients matching `forge:ingots/iron`

| Shotgun Frame input | Hardened Confetti Ball | Unstable Gunpowder | Emberstone ingot example |
|---|---|---|---|
| ![Shotgun Frame](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-shotgun-frame-sprite.png) | ![Hardened Confetti Ball](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-hardened-confetti-ball-sprite.png) | ![Unstable Gunpowder](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-unstable-gunpowder-sprite.png) | ![Emberstone ingot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-emberstone-ingot-sprite.png) |

These are actual released textures enlarged without painting new details. The pictured Emberstone ingot is a confirmed packaged tag member; a modpack may provide other valid members. This is not a standard crafting-grid arrangement. Iron imagery and the native infusion interface remain to be captured.

The separate upgrade-kit recipe is **Destruction Shotgun + Fungal Upgrade Kit → Purity Shotgun**. Do not infer a complete dimension-origin story or current-world acquisition route solely from those materials or filenames.

## Revised concept

![Destruction Shotgun proposed upgrade with shorter flashes and revised control placement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/destruction-shotgun-concept-v2.png)

The first draft's trigger was too far from the grip and its muzzle streaks looked like continuous beams. The second brings the controls rearward and shortens the flashes. Final hand fit and exact source-to-model fidelity are still unaccepted. The two visual muzzle openings are an interpretation, not a new projectile-count claim: original mode remains three pellets in total.

The brighter boosted-shot panel is proposed feedback for the existing shared roll. It does not add fire damage, burning or an explosion. The pixel-style treatment is concept art, separate from the actual released sprite above.

## Complete feature plan

- **Shot feedback:** normal and boosted visual states driven by the authoritative shot decision, with readable three-pellet trails, bounded muzzle flash and distinct optional audio accents.
- **Impact:** surface-aware sparks/dust and bounded decals. Preserve shared vanilla/AoA environmental rules; never infer terrain damage from the weapon name.
- **Inspection:** slight articulation of the three primary fins, then a clean return to idle; interruption must never produce a free boosted shot or reroll gameplay.
- **Modules and variants:** removable optic, muzzle protection, fin treatments, grip/handling modules and separately balanced precision/scatter conversions. New critical-chance or multiplier upgrades require explicit costs and server-side rules; they are not part of the original baseline.
- **Customization:** craftable variants, gameplay-earned charms, skins, static/animated/emissive stickers, custom emblems, configurable projectile/tracer/impact/finisher effects and reduced-effects options.
- **Visual treatments:** coherent Minecraft/TaCZ-fitting and higher-detail concept-fidelity versions, retaining the same source anchors.
- **Animations:** equip, idle, aim, fire, recovery, inspect, interruptions and optional reload only where the selected resource model supports it.
- **Performance:** pooled particles, bounded lifetimes, shared materials and suitable LODs; benchmark startup, frame-time and server work under equal conditions.

## QA still required

Original in-game projectile and impact capture; one-roll-per-shot and shared-pellet outcome tests; ammo, enchantment, immunity and final-damage checks; normal/slim hand and swept attachment clearance; full animation/material/export implementation; native TaCZ/TML, multiplayer, save/load, progression and compatibility testing. Static concepts and source contracts do not pass native gates.

[Exact-release evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/destruction-shotgun-source-evidence.json) · [Baseline inventory](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/conventional-weapon-baselines-1.20.1.json) · [Complete weapon requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
