# Hive Blaster — bronze, amber and a heavy cannonball

**AoA 3.7.1 / Minecraft 1.20.1 · released-file baseline and original upgrade concepts · native upgraded weapon not accepted.**

## What the original does

Hive Blaster is a non-fully-automatic cannon using the native Cannonball ammunition family. It fires `HiveBallEntity`, which follows an arcing path. Its recognizable appearance is a broad cylindrical front, dark brown body, copper bands and upright tubes, an amber-colored chamber and a charcoal grip.

The inspected weapon/projectile classes do **not** summon bees or apply a honey effect. They inherit the shared heavy-cannon impact path: a living target's armor and toughness adjust the raw multiplier before the heavy-gun attack, and a successful hit reaches knockback and the blocking-player shield-disable path. The shared base impact-effect hook is empty for this weapon. Bee swarms and sticky resin are optional new design ideas, not original behavior.

## Baseline inputs

| Property | Released input / behavior |
|---|---|
| Item | `aoa3:hive_blaster` |
| Base damage input | 20.5; not final damage against every target |
| Durability input | 850 |
| Firing delay input | 24 ticks; nominally 1.2 seconds at 20 TPS |
| Stored recoil constructor input | approximately 0.2; not an effective camera angle |
| Ammunition | Cannonball |
| Automatic mode | BaseCannon returns false |
| Projectile | `HiveBallEntity` |
| Lifespan / damage-multiplier / piercing inputs | 120 / 1.0 / 0 |
| Gravity return | approximately 0.1 |
| Firing sound | `ITEM_SHADOW_BLASTER_FIRE` |

The shared cannon multiplier includes `1 + (armor × 1.5 + armorToughness × 0.5) / 100`, followed by the native heavy-gun damage system. The rest of that pipeline, target state and other mods still matter.

## Original projectile and performance-sensitive behavior

![Nearest-neighbor enlargement of the released cannonball texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannonball-texture-preview-1.20.1.png)

[Unmodified projectile texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-original-projectile.png).

The registered renderer uses this ordinary cannonball texture and adds flickering sparkler requests across **eight iterations per render invocation**. Its colors alternate between the `YELLOW` constant and RGB `(223,153,0)`. Particle constructor inputs include scale 1 and age modifier 3; the latter is not a verified three-second lifetime.

The renderer holds a counter initialized to 12 and a toggle. It decrements the counter inside the render-loop iterations and resets it when switching the color. That state is stored on the renderer, not the projectile. Do not assume the color cycle is a per-projectile game-time clock, and do not present render-call counts as measured particles per second.

For the upgrade, separate presentation timing from render passes. Evaluate a bounded game-time emission or ribbon/atlas solution while preserving the amber/yellow character. Test several visible projectiles, paused time, high refresh rates and extra shader passes. No FPS improvement is claimed until the replacement is measured and visually compared.

## Acquisition

The released recipe is **Shadow Blaster + Lelyetian Upgrade Kit → Hive Blaster**, using `aoa3:upgrade_kit`. The recipe's presence does not by itself establish how every ingredient is obtainable in every modpack or version.

## Original identity and proposed premium versions

![Nearest-neighbor enlargement of the released Hive Blaster sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-sprite-preview.png)

[Unmodified original sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-original-sprite.png).

![Original premium concept exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-concept-exploration-v2.png)

- **Amber Crucible:** the closest silhouette to the original. A heavy bronze cannon, readable amber chamber and purposeful copper vents. The conventional Cannonball path must remain understandable in the final loading model.
- **Swarm Crown:** honeycomb-shaped armor and spectral insect motifs. A real damaging swarm would be a separately defined functional module with explicit ownership, targeting, resource cost and spawn limits; decorative insects alone grant no attacks.
- **Resin Bloom:** articulated amber petal plates and an optional resin-pulse branch. Any slowing, lingering field or splash damage needs its own declared server behavior and compatibility tests.

The concept shows proposed projectiles and impacts. It is not a native screenshot or proof that the models animate correctly. Its small pixel inset is labeled as an inspired reconstruction; the separate original image above is exact. [Earlier concept v1 retained](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-concept-exploration-v1.png).

### Additional attachment and inspection ideas

- Vent crowns that visibly articulate during discharge/recovery, with optional amber, smoky-bronze and honeycomb finishes.
- A spherical-breech presentation or optional recharge treatment, without imposing mandatory reloads on every upgrade.
- Earned bee/amber charms with declared gameplay bonuses, plus static, glowing or animated decals.
- A harmless inspection in which a tiny spectral insect circles the vents and returns to the chamber. It must not consume Cannonballs, spawn a real attacking entity or modify health.

## Acceptance still required

- [ ] Capture the original flight, amber/yellow particles, block impact and entity impact in the exact release.
- [ ] Preserve heavy-cannon target, shield and knockback behavior in original mode.
- [ ] Model the breech, grip, vents and attachments with real hand/clearance checks.
- [ ] Keep multi-projectile effects independent of renderer instance state and repeated shader passes.
- [ ] Validate all proposed swarm/resin gameplay modules separately from cosmetics.
- [ ] Test native import, animation interruption, networking, saves, shader/Vulkan compatibility and actual frame/tick costs.

[Audit tool and original concept prompts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-audit-tool-v1.zip) · [Released class/renderer/recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-released-evidence.json) · [Weapon research standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard) · [Customization](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization)

Original AoA assets and identity: Tslat and contributors. New concept exploration was generated with the built-in image tool.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
