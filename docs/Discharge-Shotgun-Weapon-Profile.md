# Discharge Shotgun — a close-range explosive scattercaster

**Baseline: AoA 3.7.1 / Minecraft 1.20.1. Released-file analysis and upgrade concepts; native upgraded weapon not yet accepted.**

## What it actually does

Discharge Shotgun fires a four-projectile burst of `DischargeShotEntity` after one ammunition check using Discharge Capsules. It is not fully automatic. Its identity is a compact black/red body, broad front, silver dorsal fins with red accents and a rear grip. The upgrade should retain that recognizable silhouette while making its capsule, moving fins, recoil and impact feedback feel deliberate and powerful.

Its **base-damage constructor input is zero, but it is not harmless**: damage is routed through explosion behavior. The impact call chain contains an important distinction that a conversion must not flatten away.

- On an ordinary entity hit with a valid weapon and living owner, the shared bullet handler first calls the weapon's impact method, which requests an explosion with strength input **2.5**. It then calls the projectile's entity-impact method, which requests another explosion with strength input **1.8**.
- On a block impact, the projectile's block-impact method requests the **1.8** explosion.
- These are separate source-level calls. Do not add the strengths into a made-up “4.3 radius” or multiply them into a guaranteed final-damage figure. Damage immunity, other entities, event handlers and actual runtime behavior need testing.
- The helper uses the projectile entity's coordinates. The supplied hit-vector argument is not used by these overrides to position the explosion.
- Block damage is controlled by the destructive-weapon/mob-griefing rule path. A spectacular cosmetic impact must not bypass those permissions.

This existing two-stage entity-hit path is different from an accidental duplicate network callback. Preserve and test the original mode before making an explicitly declared upgraded behavior change.

## Verified baseline inputs

| Property | Released input / behavior |
|---|---|
| Item | `aoa3:discharge_shotgun` |
| Base damage input | 0; explosions supply the attack behavior |
| Pellets | 4 projectile spawn attempts per accepted burst |
| Durability input | 160 |
| Firing-delay input | 55 ticks; nominally 2.75 seconds at 20 TPS |
| Knockback constructor input | 0 |
| Stored recoil constructor input | 13, not degrees or the effective camera kick |
| Effective recoil caveat | Inspected inherited getter returns 0.35; its shot calculation uses 1 for zero base damage before multiplying by that getter |
| Ammunition | Discharge Capsule; ammunition checked before the pellet loop |
| Projectile | `DischargeShotEntity` |
| Lifespan parameter | 4, with an `age > lifespan` discard check after the superclass tick; not an exact four-tick range guarantee |
| Projectile damage-multiplier / piercing inputs | 1.0 / 0 |
| Gravity return | 0 |
| Fire sound | `ITEM_GUN_SHOTGUN_HEAVY_FIRE_LONG` |

The shared spread factor is `0.1 × pelletCount × (1 − 0.15 × Form enchantment level)`. This is a spread input, not an angle in degrees. Other firing eligibility, ammunition/enchantment and cooldown behavior still belongs to the native pipeline.

## Actual original visuals

![Nearest-neighbor enlargement of the released weapon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-sprite-preview.png)

[Unmodified sprite bytes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-original-sprite.png).

![Nearest-neighbor enlargement of the released orange projectile texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-projectile-preview.png)

The renderer registration resolves to `TexturedProjectileRenderer` using this orange projectile texture. The red crystalline trails and red impacts in the concept below are proposed upgrades. Actual original in-flight and impact screenshots remain to be captured in game.

## Premium upgrade exploration

![Three original upgrade concepts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-concept-exploration-v2.png)

- **A · Core Discharge Scattercaster:** closest to the compact original silhouette. A visible fictional capsule seat and silver fins communicate charge, discharge and recovery.
- **B · Capacitor Crown:** articulated dorsal armor and red energy accents, with a distinct fin-opening inspection and restrained reactive stages.
- **C · Modular Breacher:** a flared emission assembly supporting alternate spread modules and a visibly different front silhouette.

The generated sprite inset is a reconstruction; the separate original above is the actual source. The effect vignettes are visual proposals and do not specify damaging pellet count. Comfortable hand/trigger clearance, capsule extraction and moving-fin envelopes still require actual models and animation QA. [Earlier v1 concept retained](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-concept-exploration-v1.png); v2 corrects C's cropped grip.

### Attachment and play ideas

- **Focus Choke:** a tighter deliberate discharge pattern, with the corresponding mechanical front visible.
- **Scatter Crown:** extra discharge channels and an explicitly defined multishot/damage upgrade. Resolve projectile count, ammunition policy and hit behavior on the server.
- **Pulse Chamber:** a distinct energy-pulse branch with its own collision and impact contract; do not silently substitute it for original explosions.
- **Capsule Cradle:** an optional visible loading/recharge presentation. Reloading remains optional rather than being imposed on every AoA upgrade.
- **Reactive fins and earned charms:** fins reveal brighter red seams through progression; charms can grant declared bonuses. Cosmetic sparks during inspection cannot damage mobs or detonate capsules.
- **Skins/effects:** preserve an original-inspired black/red/silver option, then offer unlockable materials, decals, trails and impact treatments without hiding targets.

## Acquisition evidence

A scan of this release's `data/aoa3` JSON files found no direct `aoa3:discharge_shotgun` reference. This does not prove there is no code-driven, creative, external-pack or other acquisition route. Do not invent a crafting recipe or label a historical route as current without verifying it.

## Acceptance checklist

- [ ] Capture original flight, entity impact and block impact in the exact release.
- [ ] Test both entity-hit explosion stages, final damage, immunity behavior and environmental rules.
- [ ] Test single ammo check versus the four-projectile burst and all relevant enchantments.
- [ ] Build the model, capsules, fins, comfortable hands and interruption-safe animations.
- [ ] Make every functional module's appearance agree with its declared projectile/resource behavior.
- [ ] Validate native export, multiplayer, saved builds, combat-mod compatibility and measured frame/tick costs.

[Released class and asset evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-released-evidence.json) · [Repeatable audit tool and concept prompts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-audit-tool-v1.zip) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades)

Original AoA assets and identity: Tslat and contributors. Concept work: original project exploration generated with the built-in image tool.
