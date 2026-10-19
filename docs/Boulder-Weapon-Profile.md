# Boulder: four pellets beneath a stone-like silhouette

**AoA 3.7.1 / Minecraft 1.20.1 · released-source profile and concept proposal · no accepted native upgrade.**

## What it actually does

Boulder is a **four-pellet Spreadshot shotgun**, registered directly with `BaseShotgun`. There is no dedicated Boulder subclass in this release. Its shared firing path consumes/validates ammunition, then creates the pellet loop with `LimoniteBulletEntity`, age input 4, multiplier input 1 and piercing input 0.

Despite the name, this is not evidence that it fires large boulders, explodes terrain or shares Boulder Bomber's mechanics. Likewise, **Boulder Dash** is a different item: matching a substring in a recipe is insufficient provenance.

| Released field | Value / boundary |
|---|---|
| Registry ID | `aoa3:boulder` |
| Stored damage input | 11.5; not guaranteed final damage |
| Pellets | 4 |
| Durability | 1080 |
| Delay | 58 ticks; nominally 2.9 seconds at 20 TPS |
| Recoil input | 0.5; not camera degrees |
| Knockback input | Approximately 0.4; not measured distance |
| Ammunition | Spreadshot |
| Fire mode | Non-automatic |
| Sound selector | Medium long shotgun firing sound |

There is no Purity/Destruction-style shared boosted-shot roll in this base firing implementation. Four projectiles do not guarantee four successful hits or a fixed aggregate damage number. Enchantments, shared attack behavior and target immunity remain relevant.

## Original appearance

![Actual released Boulder sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/boulder-original-preview.png)

Preserve the short chunky charcoal body, stepped gray upper blocks, muted crimson lower structures and angled crimson grip. Stone-like armor is a visual interpretation of those anchors and the Rocky upgrade association. The source recipe alone does not establish a canonical maker, dimension-origin story or literal granite construction.

## Illustrated upgrade route

| Input | Kit | Result |
|---|---|---|
| ![Demolisher](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-demolisher-sprite.png) | ![Rocky Upgrade Kit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-rocky-upgrade-kit-sprite.png) | ![Boulder](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/boulder-original-preview.png) |
| Demolisher | Rocky Upgrade Kit | Boulder |

1. Obtain Demolisher and a Rocky Upgrade Kit in the exact pack/version. Their acquisition routes need separate confirmation.
2. Use the shipped `aoa3:upgrade_kit` route described in the [Divine Station guide](Divine-Station-Weapon-Upgrades-1.20.1), not an ordinary crafting-grid arrangement.
3. Check preservation of enchantments, names and any new customization data before upgrading a valuable weapon. Unverified data transfer must not be promised.

The exact source is `data/aoa3/recipes/upgrade_kit_boulder.json`. The images above are actual packaged textures enlarged without adding painted details. Recipes for Boulder Dash and Boulder Bomber are intentionally excluded from this weapon's evidence.

## Revised concept

![Boulder upgraded concept, not in-game](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/boulder-concept-v2.png)

The first concept incorrectly showed oversized rock projectiles and a harsh stone palm-contact surface. Revision two uses four smaller pellet markers and a contoured crimson grip insert. The stylized trajectories, dust and material treatments are proposals, not captures of the original projectile renderer. Physical hand reach and all model/animation acceptance remain open.

The optional inspection lifts and reseats one armor slab. That is a newly proposed cosmetic flourish, not a released levitation ability. It must remain independent from firing and authoritative gameplay.

## Complete feature plan

- **Fire and recoil:** heavy, readable four-pellet discharge with a short bounded flash; separate weapon-body motion from camera feedback so integration cannot accidentally double recoil.
- **Projectile and impact:** preserve original default projectile behavior; optional trails and surface-specific dust/sparks/decals. No terrain destruction inferred from stone styling.
- **Animation set:** equip, idle, aim, fire, optional reload, inspect, interruption and third-person versions. Any moving slab needs swept-volume and hand/attachment clearance checks.
- **Attachment ideas:** compact quarry-style sight, protective muzzle ring, alternate foregrip, cushioned red grip and armor-shell treatments. Precision and scatter conversions need explicit new costs, pellet count and handling rules.
- **Craftable variants:** distinct recognizable parts and recipes; a future rock-projectile conversion would be a separately balanced new mode, never silently relabeled original behavior.
- **Customization:** gameplay-earned charms and their explicit bonuses; skins; static, animated and emissive stickers; custom emblems; configurable projectile/tracer/impact and finisher effects. Preserve original concepts and alternatives.
- **Reload policy:** optional according to chosen ammunition mode; do not impose an unrequested magazine system on original mode.
- **Visual modes:** coherent Minecraft/TaCZ-fit and higher-detail concept-fidelity materials with the same source silhouette. Include reduced-effects and accessibility options.
- **Performance:** bounded effect lifetimes, pooled particles, decal limits and LOD testing. No performance guarantee before representative native benchmarks.

## Required acceptance

- [ ] Record the original projectile in flight and on entity/block impact in this release.
- [ ] Validate the four-pellet ammo and damage path in-game, including missed/immune targets.
- [ ] Approve concept-to-model silhouette, grip comfort and both texture modes.
- [ ] Check all animation sweeps, hands, sights, charms and attachment combinations.
- [ ] Validate native export, multiplayer, interrupted animation and save/reload behavior.
- [ ] Implement and assess every required effects/customization family, without silent omissions.
- [ ] Measure representative frame-time, memory and dense-combat effects budgets.

[Complete weapon standard](Weapon-Completeness-Standard) · [Machine-readable evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/boulder-source-evidence.json) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
