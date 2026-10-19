# Mecha Cannon: orange cannonball and mechanical craft lineage

**AoA 3.7.1 / Minecraft 1.20.1. Source-backed profile and revised concept candidate. No accepted native upgrade.**

## What the weapon does

Mecha Cannon uses the shared non-automatic cannon behavior with **Cannonball ammunition**. Its subclass selects **OrangeCannonballEntity** and the dedicated Mecha Cannon firing sound. The inspected projectile implements HardProjectile and returns 0.1 from its gravity method. Orange presentation does not establish an explosion, fire damage, burning, armor penetration or block destruction.

| Released input | Value and interpretation |
|---|---|
| ID | `aoa3:mecha_cannon` |
| Stored damage | 26.5; not guaranteed final damage |
| Durability | 525 |
| Delay | 42 ticks, nominally 2.1 seconds at 20 TPS |
| Recoil input | Approximately 0.15; not camera degrees |
| Ammunition | Cannonball |
| Firing | Non-automatic |
| Projectile | OrangeCannonballEntity |
| Constructor inputs | Age 120, multiplier 1, piercing 0 |
| Gravity-method return | 0.1; native trajectory is not measured here |
| Sound selector | ITEM_MECHA_CANNON_FIRE |

The inherited BaseCannon impact path calls the heavy-gun attack helper and, on successful damage, has scaled knockback and shared impact handling. Its damage calculation also reads target attributes. Do not present stored damage as a universal hit result. The inspected subclass and orange projectile add no unique explosion method; later changes to shared classes or datapacks need separate review.

## Original silhouette

![Actual released Mecha Cannon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mecha-cannon-original-preview.png)

Keep the squat dark tube, orange/ochre bands and structural ribs, gray rear extension and small red accent. The brass/enamel treatment and decorative gearing in the new design are interpretations, not official material or maker claims. Preserve this identity beside the related Mechyro without turning every mechanical weapon into the same long rifle.

## Crafting tutorial with actual ingredient images

Combine **Incomplete Mecha Cannon ×1 + Power Core ×1 + Mecha Gear ×1** using the released standard shapeless recipe. Slot arrangement does not matter.

| Incomplete Mecha Cannon | Power Core | Mecha Gear |
|---|---|---|
| ![Incomplete Mecha Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-incomplete-mecha-cannon-sprite.png) | ![Power Core](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-power-core-sprite.png) | ![Mecha Gear](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-mecha-gear-sprite.png) |

These are extracted released textures enlarged with nearest-neighbor sampling, not generated ingredient illustrations. The packaged Iro Crate block loot table includes Incomplete Mecha Cannon among six incomplete mechanical weapons in its non-Silk-Touch one-roll pool. The separate Silk Touch pool returns the crate. This does not itself prove where crates spawn or that the historical progression path is available in a current world; that requires version-specific gameplay verification.

## Proposed upgrade art

![Revised Mecha Cannon concept with separated flight and impact moments](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mecha-cannon-concept-v2.png)

The first draft lacked a clear trigger guard and implied wall excavation. The revised candidate restores an open guard and shows a localized impact against intact stone. “Flight” and “Impact” show successive moments of one projectile, not a two-projectile attack. These are proposed effects, never evidence of the original in-game projectile appearance.

The main hero and Minecraft-friendly treatment are two visual directions. Moving-hand ergonomics, attachment clearances and exact concept-to-mesh fidelity still need review. The large central gold loop is an exterior design element, not a verified functional mechanism.

## Complete feature plan

- **Fire/recovery:** one readable orange projectile per original shot, deliberate recoil and settle, timed muzzle flash and sound. Avoid uncontrolled screen shake and obscuring particles.
- **Projectile/impact:** configurable visual treatments, surface-specific sparks/dust and bounded decals. No terrain destruction or elemental damage merely because an effect looks fiery.
- **Inspect:** optional decorative gear movement and light response; clean interruption into aiming or firing, no free ammo or resource changes.
- **Craftable modules:** alternate muzzle, optic, support/handling assemblies and visible core housing. Major gameplay conversions get explicit recipes, resource costs and balance profiles.
- **Original-inspired alternate concepts:** compact high-control muzzle, elaborate power-core shell and a longer precision cannon conversion. Keep the original projectile preset available; proposed new behavior is separately specified and tested.
- **Customization:** gameplay-earned charms, skins, static/animated/glowing stickers, custom emblems and optional finisher/projectile/tracer/impact effects. Each effect needs multiplayer and accessibility limits.
- **Animation completeness:** equip, idle, aim, fire, recovery, inspection and interruption transitions. Reload remains optional and follows the actual configured resource model, rather than inventing mandatory magazines.
- **Performance:** pooled particles, bounded effect lifetime, sensible LODs and shared cached assets; measure startup and frame-time cost in native tests.

## Required QA

Capture the actual original projectile in flight and on impact; verify resource consumption, successful/blocked damage, target attributes and knockback; review normal/slim hands throughout the animation set; test all attachment combinations; validate mesh topology, UVs and material export; run native TaCZ/TML and multiplayer tests. No gate is passed by concept art or a static render.

## Sources

[Machine-readable exact-release evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mecha-cannon-source-evidence.json) · [Related Mechyro profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mechyro-Weapon-Profile) · [Versioned weapon baselines](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/conventional-weapon-baselines-1.20.1.json)
