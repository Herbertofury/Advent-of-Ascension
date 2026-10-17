# Performance switches and progression safety · 1.21.1

**Minecraft 1.21.1 · AoA 3.7.16.1.** Two server settings can look attractive when a pack is slow, but both change gameplay behavior. Neither belongs in a “same features, same behavior, free FPS” preset.

![Two switches and the gameplay behavior they change](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/performance-switches-and-gameplay-1.21.1.webp)

## Quick decision table

| Server key | Released default | Inspected effect when true | Preserve behavior? |
|---|---|---|---|
| general_settings.disableSkills | false | generateSkillsMap returns an empty skill-instance map | No: it changes progression functionality and risks stored progress |
| general_settings.fastProjectileCalculations | false | shootingAtTarget skips its initial aiming ray trace | No: it changes target-point selection and can affect aiming accuracy |

These are server gameplay settings, not the client HUD controls. This guide does not change either value or recommend enabling them for an established world.

## disableSkills: follow the branch, not the misleading sentence

The released config description contains a contradictory sentence about setting this flag false to disable skills. The actual inspected consumer builds skill instances only when **disableSkills is false**. With the flag true, it returns the newly created empty map.

The default false therefore permits skill-instance generation. Do not invert the meaning based on the description’s first sentence.

### Why progression requires extra care

The player Stats object initializes its skill map from that generator. Its load method iterates existing instances to apply stored skill data. Its save method writes the skills section only when the map is nonempty.

Consequently, with an empty map, this path does not reconstruct saved skill instances and does not write their entries into a fresh output tag. The bundled setting warning also says that disabling skills can lose stored levels and XP for players who log in.

The evidence includes 26 conditional map/fresh-save cases. This does not claim that every modpack’s complete persistence lifecycle was executed, or that a particular private save has already lost data. It does establish that the flag is a gameplay/progression change and is unsuitable as a reversible cosmetic toggle.

**To hide the skills display, use its HUD toggle or presentation settings instead.** See [Controls and HUD](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Controls-HUD-and-Client-Settings-1.21.1). Hiding the display and disabling the skill system are separate actions.

## fastProjectileCalculations: what the shortcut omits

In the inspected shootingAtTarget helper:

1. A projectile without a living shooter falls back to the straight-shooting helper.
2. For a living shooter, it creates a far target point from the shooter’s eye position and look direction. The distance uses velocity multiplied by the shot context’s lifespan, or 120 when no context is supplied.
3. With fastProjectileCalculations=false, it runs an aiming ray trace from the eye toward that point, filtering through the projectile’s canHitEntity predicate, and replaces the aim point with the trace result.
4. With the flag true, that ray-trace step is skipped.
5. It builds a direction from the projectile’s current position to the chosen aim point, applies a directional fallback when necessary, and calls shoot with the supplied velocity and inaccuracy.

This concerns **initial aiming/convergence**, not a blanket removal of projectile collision detection, every projectile tick, or all AoA weapon mechanics. Different weapons can use other helpers and additional behavior.

### A labeled geometry example

Suppose a straight-line projectile starts 0.5 units to the side of the eye line, the intended target plane is 5 units away, and the far aim point is 120 units away. A ray aimed directly at the near eye-line target converges to lateral position zero there. A ray aimed at the far point is still about **0.479 units** to the side at the near plane.

| Lateral starting offset | Near target distance | Far aim distance | Illustrative lateral position at the near plane |
|---:|---:|---:|---:|
| 0.25 | 5 | 120 | about 0.240 |
| 0.50 | 5 | 120 | about 0.479 |
| 1.00 | 5 | 120 | about 0.958 |

The illustration uses offset × (1 − near distance / far distance). The nine bounded geometry cases omit gravity, spread, hitboxes, movement and external hooks. They are **not measured weapon hit rates**. Their purpose is to explain why skipping target-point selection can change behavior even if the projectile still collides normally.

## A no-loss optimization workflow

1. Keep the released gameplay defaults while collecting a baseline.
2. Separate startup/loading time, server tick time, client frame time and short frame-time spikes. A higher average FPS does not prove improved worst-case smoothness.
3. Use the same world, route, entities, view distance, mod list and warm/cold-cache conditions for comparisons.
4. Profile the actual slow path before changing algorithms. A config name or comment is not a benchmark result.
5. Prefer removing duplicated work, unnecessary allocation and repeated scans while retaining outcomes. Validate targeting, skill data and multiplayer synchronization after any code change.
6. Keep a known-good save/build for rollback before experimental persistence changes. Do not toggle off progression on the only copy of an established world.
7. Report measured improvements alongside feature, correctness and compatibility checks. This documentation has not measured an FPS or loading-time gain.

Client choices such as reducing screen shake or changing XP-feedback presentation can improve comfort, but they also are not automatically performance gains. Choose them for the presentation you want, then measure separately.

## Restoration acceptance checklist

- [ ] Correct the disableSkills description so its wording matches the released branch polarity.
- [ ] If temporary skill suspension is a product goal, preserve dormant progression explicitly instead of relying on an empty active-instance map.
- [ ] Test save/load and re-enable behavior with real target-build saves before calling the switch reversible.
- [ ] Compare close, far, moving and off-axis targets before replacing aiming calculations.
- [ ] Keep projectile collision and initial aiming checks conceptually separate in tests.
- [ ] Benchmark any replacement under a representative modpack and retain the user’s no-feature-loss requirement.

These are proposed improvements and test requirements. They are not implemented engine changes or a claim that the private Enderloom build has these defects.

## Evidence

- [Two released config windows, five consumer methods and bounded models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/performance-tradeoff-evidence-1.21.1.json)
- [Diagram receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/performance-tradeoff-art-evidence-1.21.1.json)
- [Pinned skill-map generator](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/data/server/AoASkillsReloadListener.java)
- [Pinned projectile aiming helper](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/projectile/base/WeaponProjectile.java)

Static release inspection and original documentation models only; no Minecraft or mod code was executed.
