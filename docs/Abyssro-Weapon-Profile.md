# Abyssro: compact two-pellet shotgun

**AoA 3.7.1 / Minecraft 1.20.1. Source-backed identity and revised concept candidate; no accepted native upgrade.**

## Current selected concept · 22 October 2026

![Abyssro selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abyssro-eyes-pump-concept-v3.png)

New crimson/graphite sci-fi study adds the requested drum, pump fore-end and eye motifs. Eye-sight panels propose iris opening into a clear aperture. The prior concept remains an alternate. Static concept only; no native animation, feeding or hand-fit acceptance.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Aabyssro). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

Dedicated supplemental studies (partial design candidates, not implemented features):

- [Eye watch, dilation, clear magical zoom view and blink return; static animation intent](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abyssro-living-eye-sight-study-v1.png).

## What it does

Abyssro is registered directly as a configured **BaseShotgun**, not a separate Abyssro-specific class. Its baseline uses **Spreadshot ammunition and two pellets**. The inspected firing loop creates LimoniteBulletEntity instances, while the auxiliary projectile-factory method returns a MetalSlugEntity for the shared ammo/effects path. Looking only at that factory would misidentify the actual loop-spawned projectiles.

| Released input | Value / boundary |
|---|---|
| ID | `aoa3:abyssro` |
| Configured class | BaseShotgun |
| Stored base damage | 18.5; not guaranteed combined damage |
| Pellet count | 2 |
| Durability | 1,100 |
| Fire delay | 46 ticks, nominally 2.3 seconds at 20 TPS |
| Stored knockback factor | Approximately 0.3; not measured displacement |
| Stored recoil input | Approximately 0.2; not camera degrees |
| Ammunition | Spreadshot |
| Firing mode | BaseShotgun returns non-automatic |
| Loop-created pellet | LimoniteBulletEntity, age input 4, multiplier 1, piercing 0 |
| Spread expression | `0.1 × pelletCount × (1 − 0.15 × FORM level)`; not a measured angle or range |

The shared firing method first requests ammo/effects-path data, aborts if unavailable, then creates the pellet loop and calls firing effects. Native tests must confirm exact net consumption, enchantment behavior, collision/immunity handling and final damage. Two configured pellets do not justify advertising a guaranteed 37-damage hit.

## Actual original appearance

![Actual released Abyssro sprite, nearest-neighbor enlargement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abyssro-original-preview.png)

The source has a compact dark upper barrel, pale upper/lower structural pieces, dark crimson body, red accent and a short rear structure with a pale inset. Preserve that compact identity rather than making another long generic rifle. The new ivory/ceramic and lacquer material interpretation is not an official material attribution.

## Upgrade and origin evidence

**Mechyro + Abyssal Upgrade Kit → Abyssro** through the released `aoa3:upgrade_kit` recipe. The packaged `worlds/abyss.json` loot data references the upgrade kit, which supports an **Abyss-associated upgrade lineage**. It does not establish an official maker, exact manufacturing story or prove that every packaged loot entry is active in a running world.

The source-linked [origin index](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-origin-data-index-1.20.1.json) and [weapon baseline](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/conventional-weapon-baselines-1.20.1.json) retain exact-version evidence. Do not carry this recipe or behavior into another AoA release without reconciliation.

## Earlier preserved art: concept

![Abyssro concept candidate with two-pellet effect and two visual treatments](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abyssro-concept-v2.png)

The first draft was too elongated and added an arbitrary large hanging box. The revision removes that box and clarifies the grip/guard. The final compactness, hand space and exact source-to-concept proportions remain review gates. Both visual-treatment miniatures are artwork, not native renders.

The red shot trails and impact styling are proposals. The source pellet class does not establish a magical red projectile appearance. Preserve the two-pellet baseline; a converter that changes count or shot type must be explicit, balanced and server-authoritative.

## Full feature plan

- **Feedback:** brief deep-red muzzle flash, two readable pellet cues, powerful short recoil and recovery. Avoid oversized glowing projectiles obscuring targets.
- **Attachments:** wide shaped shroud, ivory open sight, grip/support options and carefully designed shot converters. Record changed pellet count, spread, resources and effective values together.
- **Optional service:** appropriate to Spreadshot accounting. A decorative magazine cannot silently impose a new reload/resource system.
- **Inspect:** a restrained red accent wake-up and tactile support/receiver check; all transforms return correctly on interruption.
- **Customization:** Minecraft-fit and concept-faithful texture options, earned charms, skins, stickers/emblems and independently selectable muzzle, projectile, trail, impact, decal and finisher effects.
- **Dismantling and variants:** preserve donor identity, effect conflicts, upgrade lineage, attachment compatibility and saved-build migration.
- **Native animation:** actual player hands, comfortable trigger clearance, equip/idle/movement/aim/fire/recovery/inspect and any optional service state.
- **Performance:** bounded effects and projectile work; preserve startup/frame budgets with measured equivalent workloads and no repeated scans.

## Acceptance checklist

- [ ] Exact-release original firing, flight, impact and resource captures.
- [ ] Validate pellet count, FORM/SHELL interactions, immunity and final damage in-game.
- [ ] Source-proportion comparison and concept refinement before geometry approval.
- [ ] Editable model, deliberate textures, rig, real hands and swept clearance.
- [ ] Native renderer, multiplayer authority, recipes, progression, save/load and compatibility.
- [ ] Actual frame-time/startup and effects-budget measurements.

[Source receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abyssro-source-evidence.json) · [Mandatory full weapon standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).

Original AoA identity and assets: Tslat and contributors. New concept generated with the built-in image tool. Final art and native gameplay acceptance remain open.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](Effective-Recoil-Routing-1.20.1).
