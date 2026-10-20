# Aqua Cannon · cobalt body, dark shot and recovery

**AoA 3.7.1 / Minecraft 1.20.1 · source/renderer study and partial concept. Native captures and final-art acceptance remain open.**

## What the original actually does

Aqua Cannon consumes **Cannonballs** and creates a **Heavy Blue Cannonball** projectile. Its impact-damage override first invokes the shared cannon damage path, then requests **2 health points of healing for the shooter** when the target is a living entity. Two health points are nominally one heart; healing events and maximum health still apply.

This is not percentage life steal. The subclass does not check whether the preceding damage attempt succeeded before making that healing request. The helper only calls healing for a living, alive shooter whose health is above zero and below maximum. Canceled damage, invulnerable targets, friendly targets and full-health shooters therefore need explicit regression tests. Any change to require confirmed damage must be a separately approved behavior change, not a silent reinterpretation of the original.

| Released input | Value |
|---|---:|
| Damage input | 14 |
| Durability | 300 |
| Firing delay | 35 ticks; nominally 1.75 seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.21 |
| Ammunition | Cannonball |
| Projectile maximum-age argument | 120 ticks |
| Piercing argument | 0 |
| Projectile gravity override | 0.1 |
| Healing request | 2 health points to shooter, subject to the conditions above |
| Firing sound | Ball cannon |

The final projectile constructor argument `0` is **piercing**, not gravity. The projectile supplies a damage multiplier of 1.0 to the shared bullet constructor. Neither the name nor the blue effects establish a water jet or an underwater-only bonus.

Shared cannon handling also adjusts the attack input by `1 + (armor × 1.5 + toughness × 0.5) / 100` for living targets, then calls the heavy-attack helper. Knockback and shield handling are conditional on that shared attack reporting success. These are source rules, not measured final damage after all game systems.

[Named Aqua Cannon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/AquaCannon.java) · [Shared cannon path](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/BaseCannon.java) · [Released evidence and class hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/aqua-cannon-released-evidence.json).

## Original visuals, not invented footage

![Original Aqua Cannon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/aqua-cannon-original-preview.png)

Retain the short chunky blue barrel/body, pale blue collar bands, teal top/rear accents and distinct teal grip. Decorative waves in the upgrade are new styling, not proof of an origin dimension, maker or liquid-powered mechanism.

![Released cannonball texture asset](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/aqua-cannon-projectile-preview.png)

The renderer registration supplies the ordinary dark `cannonshots/cannonball.png` texture. The Heavy Blue renderer adds blue **SPARKLER** particles. The image above is the released texture asset enlarged for inspection; it is not a screenshot of flight or impact.

### Performance-sensitive original behavior

The inspected renderer contains a loop requesting **eight sparkler particles per render invocation**. That is not eight particles per game tick. At an illustrative 60 invocations per second it would request 480 particles per second for one projectile, before engine filtering; multiple render passes, visibility, settings and frame rates can change actual behavior.

The upgrade should separate time-based emission from drawing, calibrate the desired appearance against a chosen reference capture, and measure costs with many visible projectiles. Preserve the dark projectile core and readable blue trail. A stable emission budget is a proposed optimization, not an already tested FPS improvement or proof of identical visuals at every original frame rate.

[A small time-based emission prototype and native acceptance plan](Particle-Emission-and-Frame-Time) now accompany this finding. The headless scheduler is not installed in the mod and does not establish visual or FPS parity.

## Acquisition is version-specific

No direct Aqua Cannon recipe/loot item reference was found in this inspected 1.20.1 data-JSON set. That does not prove the item is unobtainable through every code, trade or modded route.

The archived **AoA 3.6.11 / Minecraft 1.16.5** recipe index records shapeless restoration using **Waterlogged Aqua Cannon + Sponge**. This older recipe is not evidence that the same recipe works in 1.20.1. Acquisition of the waterlogged input is a separate question.

![Historical 1.16.5 restoration recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/aqua-cannon-historical-restoration.webp)

[Historical recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/aqua-cannon-historical-recipe-evidence.json) · [1.12.2 declogging guide, a separate historical system](Declogging-Waterlogged-Weapons-1.12.2).

## Premium body and feedback concepts

![Aqua Cannon body concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/aqua-cannon-concept-v1.png)

![Proposed muzzle, flight, impact and recovery cues](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/aqua-cannon-effects-concept-v1.png)

These are proposed presentations. The dark core stays recognizable, while the illustrated watery streaks, surface ripple and rear recovery flourish are new optional cosmetics. They do not establish water damage, extinguishing, a liquid jet or a guaranteed heal. A recovery cue must reflect the actual healing result, not merely a collision callback.

The concept’s heavier collar count, hand reach, opposite-side continuity and trigger clearance still require model review. No generated image is an in-game acceptance result.

## Remaining complete feature plan

- Minecraft-fit and premium textures; inspectable materials, UVs, readable LODs and measured cost.
- Collar/shroud, grip and handling variants, earned charms, skins and personal emblems.
- Optional alternate barrels with explicitly separate resource, hit and healing rules.
- Equip, idle, aim, fire, recovery, optional reload and inspect animations with interruption-safe hand placement.
- Configurable tracers/projectiles, impacts, expiring decals, confirmed-kill finishers and reduced-effects options.
- Attachment recipes, salvage/effect transfer, named builds, migration and multiplayer authority.
- TaCZ/turret compatibility, healing cancellation and repeated-hit tests; no speculative automated self-healing through turret integrations.

## Acceptance gates

- [ ] Capture original native projectile flight, impact, sound and healing outcomes
- [ ] Test canceled damage/healing, immunity, target type and full-health boundaries
- [ ] Verify current-version acquisition separately from historical restoration
- [ ] Complete attachment, conversion and inspection concept sheets
- [ ] Build both material modes and all hand/animation/effect features
- [ ] Qualify networking, TaCZ/turrets, migration and equivalent-scene performance

[Armory](Weapon-Overhaul) · [Completeness standard](Weapon-Completeness-Standard)

Original AoA identity/assets: Tslat and contributors. New concepts and optimizations remain separate from released behavior.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
