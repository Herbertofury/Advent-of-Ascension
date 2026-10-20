# Fungal Cannon — a heavy hit with a weakening effect

**Baseline: AoA 3.7.1 / Minecraft 1.20.1. Released-file evidence and original concept work; native upgraded weapon not yet implemented or accepted.**

## What it does

Fungal Cannon is a non-fully-automatic cannon using the native Cannonball ammunition family. It launches a `FungalBallEntity` and applies a Weakness effect to living targets through its successful impact path. Its three purple, blue and green mushroom-like top features, olive body and broad blue front are the recognizable visual anchors for the remodel.

The shared cannon code adjusts its raw damage multiplier using the target's armor and armor toughness before calling the native heavy-gun damage path. Successful impacts also reach the shared knockback behavior; a blocking player can have its shield disabled through that path. Final damage depends on the native damage system and other effects, so base inputs are not a promise of damage against every mob.

## Original baseline inputs

| Property | Verified input / behavior |
|---|---|
| Item | `aoa3:fungal_cannon` |
| Base damage input | 19.5 |
| Durability input | 850 |
| Firing delay input | 23 ticks |
| Recoil input | approximately 0.2; not degrees |
| Ammunition | Native `CANNONBALL` item through BaseCannon |
| Automatic mode | BaseCannon returns false for full automatic |
| Projectile | `FungalBallEntity`, maximum-age input 120, piercing input 0 |
| Projectile damage-multiplier input | 1.0 in its inherited constructor call; not launch speed |
| Gravity return | approximately 0.1 |
| Impact effect | Weakness builder with duration input 200 ticks |
| Firing sound | `ITEM_BALL_CANNON_FIRE` |

At a nominal 20 ticks per second, 200 ticks corresponds to ten seconds, but actual effect behavior and elapsed time need game testing. The raw cannon multiplier is multiplied by `1 + (armor × 1.5 + armorToughness × 0.5) / 100`; this is not a final-damage formula that skips the rest of the attack pipeline.

## Actual projectile versus proposed upgrade

![Nearest-neighbor enlargement of the released cannonball texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannonball-texture-preview-1.20.1.png)

[Unmodified projectile texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fungal-cannon-original-projectile.png).

The released renderer factory selects the ordinary cannonball texture shown above. Its custom renderer adds randomized green flickering, yellow, blue or purple sparkler requests across eight loop iterations. The generated mushroom-textured projectile and blooming mushroom-like impact below are proposed new presentation, not the original appearance. A cosmetic bloom must not create real blocks, mobs or extra damaging projectiles unless an installed functional module explicitly declares that behavior.

## Acquisition

The released upgrade recipe is **Flower Cannon + Fungal Upgrade Kit → Fungal Cannon** using `aoa3:upgrade_kit`. Preserve this native progression alongside optional modular upgrades. This is one verified acquisition path; a limited direct loot-text search is not proof that no other code-driven route can exist.

## Original identity and premium art

![Actual released Fungal Cannon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fungal-cannon-original-sprite.png)

![Fungal Cannon concept and proposed attachments](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fungal-cannon-concept-exploration-v1.png)

The small pixel-style inset inside the generated sheet is a reconstruction; the separate image above is the exact original. The concept's grip, trigger area and muzzle mechanisms need further modeling and hand-fit review. A beautiful image is not a validated reload or collision envelope.

### Proposed attachment family

- **Spore Mortar:** a heavy round fantasy projectile with a clearly readable arc and satisfying bounded impact.
- **Bloom Bell:** a broad petal-like emitter for an expanding pulse, with explicit collision and per-target hit rules.
- **Mycelium Fork:** split magical branches supporting deliberate multishot. Visible branches, projectile count, damage and ammunition policy must agree.
- **Lantern Cap:** a short glowing cap emitter for smaller bright pulses, with its own declared cadence and resource rules.

An optional inspection could have the three caps respond to each other with a bow and harmless lights. It cannot consume ammunition, apply Weakness or spawn gameplay entities. The blue mushroom charm is an original reward concept; its unlock and bonus are not implemented.

## Acceptance checklist

- [ ] Capture original cannonball flight and colored particles, entity impact, block impact and Weakness behavior in game.
- [ ] Preserve native resource ownership and shared cannon effects in original mode.
- [ ] Verify all upgraded projectile counts, hit eligibility, shield interactions and effect duration with relevant combat mods.
- [ ] Build the native-compatible model and complete inspect/firing/recovery animations with comfortable hands and no clipping.
- [ ] Bound mushroom lights, trails and impacts; keep target visibility and reduced-effect settings.
- [ ] Verify networking, saves, reload/resource options and measured frame/tick performance.

[Released class, renderer and recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fungal-cannon-released-evidence.json) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades) · [Customization](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization)


### Constructor-parameter correction

The inherited constructor’s `1.0` was previously mislabeled as a launch-speed argument. The released BaseBullet constructor assigns that float to `dmgMulti`; it is a damage multiplier. No projectile speed is inferred from this value.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
