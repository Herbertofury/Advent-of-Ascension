# Deadlock · crimson contours and a directional movement rule

**AoA 3.7.1 / Minecraft 1.20.1 · released-source profile and partial concept study. Native and final-art acceptance remain open.**

## What it actually does

Deadlock is a **Metal Slug sniper** with **SCOPE_3**. Its impact hook modifies the incoming bullet-damage factor using the target’s horizontal velocity components:

`factor = 1 + min(0.5, abs(targetVelocityX × targetVelocityZ × 50))`

This is **not a general speed measurement**. Movement along only X or only Z gets no bonus from this expression, regardless of its speed. Diagonal movement can receive a bonus capped at +50% to the incoming multiplier. Vertical movement does not enter this formula, and it reads the target’s movement, not the shooter’s. Preserve this unusual released behavior in the faithful mode; any direction-independent redesign must be an explicit optional variant.

| Released input | Value |
|---|---:|
| Damage | 25.5 |
| Durability | 120 |
| Delay | 90 ticks, nominally 4.5 seconds at 20 TPS |
| Recoil modifier | Approximately 0.09 |
| Ammunition | Metal Slug |
| Scope | SCOPE_3 |
| Sound | Metallic sniper, long variant |

These are source inputs, not measured final damage or range. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Deadlock.java) · [Released evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/deadlock-released-evidence.json).

| Target X / Z velocity inputs | Extra hook factor |
|---|---:|
| 0 / 0 | 1.0 |
| 0.1 / 0 | 1.0 |
| 0 / 0.1 | 1.0 |
| 0.05 / 0.05 | 1.125 |
| 0.1 / 0.1 | 1.5 |
| −0.1 / 0.1 | 1.5 |
| 1 / 1 | 1.5, capped |

The table evaluates the expression only. Armor, events, projectile processing, other mods and actual target motion require native tests.

## Original identity

![Released Deadlock sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/deadlock-original-preview.png)

Preserve the red stepped lower shell, black structural spine, gray muzzle and central grip, raised dark optic and red rear accent. The large red hooked rear silhouette is central to recognition. No specific dimension, maker or myth is established by the inspected class and recipe, so those remain unclaimed.

## Crafting

![Five-slot Deadlock infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/deadlock-infusion.webp)

Use **Sniper Frame** with one coal-tag ingredient, **two separate redstone-dust-tag ingredients**, one iron-ingot-tag ingredient and one gunpowder-tag ingredient. The middle arrangement is order-independent. Icons represent example tag members; the diagram’s coal illustration comes from the preserved 1.16.5 reference atlas, while the ingredient rules come from the pinned 1.20.1 recipe. [Infusion Table tutorial](Infusion-Table-Crafting-1.20.1).

## Proposed premium treatment

![Deadlock crimson and graphite upgrade concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/deadlock-concept-v1.png)

Layered red enamel and charcoal framing translate the original stepped shapes into a richer design. The rear grip sits behind the trigger, with an open smooth guard. The optic’s crimson indicator is a cosmetic proposal. This concept does not demonstrate a working scope, reload, hand fit, moving-target hit logic or final opposite-side construction.

## Full feature plan

- **Textures:** Minecraft-fit and premium appearances, purposeful wear, clean UVs/normals and readable red/black separation at distance.
- **Attachments:** optic housings, shroud variants, grip/handling options and earned charms with explicitly declared bonuses; preserve attachment clearance through all animations.
- **Functional variants:** a proposed direction-independent movement module must be opt-in, balanced and separately described. No silent correction of the original formula.
- **Animation:** equip, idle, locomotion, aim, fire, recovery, optional reload and an optic-status inspection with interruption handling.
- **Effects:** original/new flight and impact captures, customizable projectiles/tracers, muzzle effects, bounded surface impacts, expiring decals and confirmed-kill finishers.
- **Customization:** craftable modules, earned skins, stickers, animated/glowing emblems, salvage, effect transfer and saved-build migration.
- **Compatibility:** TaCZ, turrets, multiplayer authority, modded movement/teleports, event-modified damage, reduced effects and measured performance.

## Acceptance gates

- [ ] Capture original projectile, impact, sound and scope in game
- [ ] Test X-only, Z-only, diagonal, vertical, stationary and cap-boundary behavior
- [ ] Complete attachment, variant, inspection and effects concept boards
- [ ] Build faithful geometry, both texture modes and hand-fit evidence
- [ ] Pass native animations, interruption, multiplayer and migration tests
- [ ] Verify equivalent-scene startup, memory and frame-time costs

[Armory](Weapon-Overhaul) · [Weapon completeness standard](Weapon-Completeness-Standard)

Original identity/assets belong to Tslat and contributors. New art and implementation proposals are distinct from released mechanics.
