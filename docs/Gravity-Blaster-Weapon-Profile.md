# Gravity Blaster · launch yourself, clear nearby hostiles

**Released baseline: Minecraft 1.20.1 / AoA 3.7.1. Upgrade status: concept and released-file study; no native upgraded weapon accepted.**

This Spirit-powered utility blaster launches its user upward while pushing and applying an energy attack to nearby hostile mobs. Its identity is a movement-and-space-clearing burst, not a conventional projectile gun. The tooltip says “Blasts the user upwards.”

![Actual released item sprite, enlarged without smoothing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gravity-blaster-original-sprite.png)

## Original contract

| Field | Released value or meaning |
|---|---|
| Registry ID | `aoa3:gravity_blaster` |
| Stored base damage | 4.0, passed into the energy-attack helper for each selected mob |
| Durability | 600 |
| Stored firing delay | 1 tick; not proof of effective spam frequency |
| Base charge field | 1 tick in the inherited constructor |
| Base Spirit cost | 120.0, before inherited modifiers/exemptions |
| Target volume | Shooter bounding box inflated by 2 on X/Z and 0 on Y |
| Target filter | Released `HOSTILE_MOB`: `Enemy` interface only |
| Target push helper | `pushEntityAway(shooter, mob, 0.5f)` |
| User movement | Adds `(0, 2, 0)` to velocity, and marks the entity for motion synchronization |
| Sound | `ITEM_GRAVITY_BLASTER_FIRE` |
| Flight projectile | None created by this firing override |

The target box is not a two-block sphere or an aim ray. The unchanged Y extent, entity bounding boxes, walls and vertical separation all matter. The override does not show a line-of-sight test. Do not promise a fixed jump height: starting velocity, collision, gravity, terrain and other mods determine the result. No fall-damage immunity is granted in this method.

### Important source-version difference

The named-source comparison at commit `85d6beba07e3a09032834dcf79b5a01f411092c3` adds angry `NeutralMob` entities to its hostile predicate. **The pinned released 1.20.1 class does not.** The release's predicate tests `Enemy` only. Preserve that distinction instead of silently changing targeting while upgrading visuals.

### Push is not Vortex Blaster's helper

The released helper adds the unnormalized center-to-target position difference to existing target velocity, scaled by `(1 − min(knockback resistance, 1)) × 0.5`. Full resistance returns without applying that push. It does not use the same `doScaledKnockback` path as [Vortex Blaster](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vortex-Blaster-Weapon-Profile), so do not copy Vortex's specific event/attribute behavior onto this weapon. The separate energy attack still runs after the push call; blocking the push alone is not proof that damage is blocked.

## Acquisition: released infusion recipe

Use the AoA infusion system with a **Blaster Frame** as the input and **four Floating Stones** as ingredients to produce one Gravity Blaster. This is the shipped `aoa3:infusion` recipe, not a standard crafting-table grid. Other progression prerequisites should be followed in the version-specific infusion tutorial.

| Infusion input | Ingredients | Result |
|---|---|---|
| ![Blaster Frame](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gravity-recipe-blaster_frame.png) 1 × Blaster Frame | ![Floating Stone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gravity-recipe-floating_stone.png) 4 × Floating Stone | 1 × Gravity Blaster |

## Upgrade concept

![Original generated upgrade concept and proposed inspect/VFX panels](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gravity-blaster-concept-v1.png)

The concept retains the compact silver/charcoal tool-like silhouette, broad drum, dark horizontal bands and enclosed rear handle. A restrained blue distortion field gives the imaginary Spirit mechanism depth. The inset pixel-style motif is part of the generated concept; the exact released sprite is shown separately above.

- **Default pulse:** drum rings compress, a brief pressure ripple appears, then rings relax. Tie this to a server-accepted use, with no cosmetic duplicate attack.
- **Inspect:** the chamber briefly reveals a suspended miniature distortion, then seals. Movement, firing, inventory changes and weapon swaps must interrupt safely.
- **Lift governor attachment:** proposed controllable low/high lift presets with clearly displayed effective Spirit cost. This changes gameplay and needs explicit balancing and server authority.
- **Grounding collar:** proposed nearby-space-clearing mode with reduced or disabled self-launch. Do not present it as baseline behavior.
- **Vector vanes:** proposed directional movement upgrade. Targeting, collision and resource rules must be explicit; it is not permission to ignore server movement validation.
- **Cosmetics:** brushed silver, dark ceramic, animated chamber markings, earned charms and pressure-ring palettes, with reduced-motion and low-particle settings.

No ballistic magazine is required for the default Spirit contract. Optional recharge choreography must not silently introduce ammunition or a reload cost that the original lacks.

## Native acceptance checklist

1. Compare unmodified original movement and target selection on flat ground, slopes, stairs, low ceilings, water and ledges. Record velocity and fall damage, not just apparent jump height.
2. Test `Enemy` mobs, calm/angry neutral mobs, pets, players and modded entities. Retain the pinned predicate unless a separately named upgrade changes it.
3. Test targets above/below the user, different hitbox sizes, obstruction, full/partial knockback resistance and damage cancellation. Verify push and damage independently.
4. Test held input, insufficient Spirit, modifiers, creative exemptions and server rejection. One accepted use must produce exactly one gameplay burst.
5. Check first/third-person hands, trigger reach, aiming, inspect interruption, swimming/flying and equipment swaps.
6. Measure frame-time impact with many simultaneous bursts; cap cosmetic rings and avoid per-frame allocations/scans. Test shader and renderer compatibility separately.

[Static evidence and exact hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gravity-blaster-source-evidence.json) · [Reproducible static audit tool](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gravity-blaster-study-tool-v1.zip)

Original AoA identity and sprite: Tslat and contributors. New concept is visual exploration, not a game screenshot, verified 3D model or real-world engineering plan.
