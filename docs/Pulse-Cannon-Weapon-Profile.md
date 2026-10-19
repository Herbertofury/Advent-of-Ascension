# Pulse Cannon: make space while firing

**AoA 3.7.1 / Minecraft 1.20.1. Source-grounded concept candidate; no accepted native upgrade.**

## What it does

Pulse Cannon combines an inherited cannonball shot with a separate **nearby-hostile repulsion effect around the shooter when firing**. The inspected firing-effects override calls its parent first, queries living entities using the hostile-mob predicate in the shooter's bounding box inflated by 2.5, then calls the push-away helper with input 0.75.

That is not an impact-centered explosion, not a guaranteed 2.5-block spherical radius, and not proof of a 0.75-block displacement. Keep the shot, shooter-centered pulse and any proposed decorative shockwave distinct.

| Released input | Value / boundary |
|---|---|
| Registry ID | `aoa3:pulse_cannon` |
| Damage constructor input | 26; final damage depends on native paths |
| Durability constructor input | 510 |
| Firing delay | 42 ticks, nominally 2.1 seconds at 20 TPS |
| Constructor recoil | 0.15; not camera degrees |
| Ammunition | Cannonball inherited from BaseCannon |
| Projectile | CannonballEntity inherited from BaseCannon |
| Projectile constructor inputs | Age 120, piercing 0 |
| Nearby query | Shooter AABB inflated by 2.5; hostile-mob predicate |
| Push-away helper input | 0.75; not measured final motion |
| Sound | ITEM_SHADOW_BLASTER_FIRE |

## Original identity

![Actual released sprite, nearest-neighbor enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pulse-cannon-original-preview.png)

The actual sprite has a compact charcoal frame, large rectangular forward opening, magenta/purple rails and housings, bright horizontal pink accent, stepped upper blocks and an angled rear grip. Those landmarks should remain recognizable in both Minecraft-fit and concept-faithful visual treatments. The new concept's panel construction and energy materials are interpretations; this study establishes no official manufacturer or dimension origin.

## Crafting and upgrade lineage

The released infusion recipe uses **Cannon Frame** as its input, with **Purple Druse, Red Druse, Power Core, Unstable Gunpowder and two iron-ingot tag entries**, producing Pulse Cannon. It is an `aoa3:infusion` recipe, not a vanilla grid.

**Pulse Cannon + Clown Upgrade Kit → Clowno-Pulse** through the released upgrade-kit recipe. Preserve the parent/child distinction when offering attachments or craftable alternatives.

## New concept candidate

![Pulse Cannon concept with proposed shot and defensive-pulse visuals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pulse-cannon-concept-v1.png)

The rectangular muzzle and paired structural rails remain prominent, with purposeful dark surfaces and restrained magenta lighting. The sheet includes a shroud option, angular sight and two different effect studies. It is not an in-game capture or a completed implementation.

Before model approval, shorten any excessive elongation against the source silhouette and refine explicit trigger/guard geometry, comfortable real hand placement and the support grip. A polished image cannot certify hand clearance. The illustrated defensive pulse omits the holder for clarity; its eventual visual origin must follow the shooter, not a dropped gun or projectile impact.

The debris and pink ring are proposals. They must not create terrain damage, additional entity damage, or changed push range without an explicit gameplay attachment and server-authoritative implementation.

## Complete feature direction

- **Shot and feedback:** one readable cannonball launch, a brief rectangular muzzle pulse, weighty recoil/recovery and a short fading trail. Preserve the separate defensive effect.
- **Pulse presentation:** a bounded shooter-centered wave at valid firing time, with reduced-flash/reduced-motion options. Cosmetic rings should not imply a precise spherical hit boundary the source does not use.
- **Attachments:** open-frame versus shrouded muzzle, adjustable angular sight, supported grip, pulse visualization module and optional resource-service housing. Show functional values and conflicts instead of treating geometry as implementation.
- **Inspection:** sequential magenta panel activation, a contained rectangular field test, then exact neutral-pose restoration; cancellation must clean up all effects.
- **Reload/service:** optional, appropriate to Cannonball accounting. No hidden new magazine requirement or duplicated ammo.
- **Customization and progression:** separate skins, earned functional charms, stickers/emblems, projectile/trail/impact/decal/finisher options, dismantling rules and craftable alternates.
- **Native animation:** equip, idle, aim, movement, fire, recovery, inspect and any service transitions with actual wide/slim player arms and swept clearances.
- **Performance:** bounded pulse/projectile effects, stable startup and frame-time budgets, exact-version dependency qualification and no repeated scans.

## Tests that matter for this weapon

- [ ] Capture the original shot and pulse in the pinned game build.
- [ ] Confirm effect ordering, valid firing conditions, projectile count and resource conservation.
- [ ] Test query corners versus face-center positions; do not replace the source AABB with a sphere accidentally.
- [ ] Check friendly entities, hostile predicate edge cases, bosses, knockback resistance and protected environments.
- [ ] Verify multiplayer authority and avoid applying the push once per render pass or once per client.
- [ ] Test saves, upgrades, attachments, interrupted animation, actual materials and equivalent-work performance.

[Source receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pulse-cannon-source-evidence.json) · [Mandatory complete weapon standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).

Original AoA identity and assets: Tslat and contributors. New concept generated with the built-in image tool. All native and final art acceptance gates remain open.
