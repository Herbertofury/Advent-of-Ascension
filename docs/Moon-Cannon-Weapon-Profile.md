# Moon Cannon

[Weapon overview](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Original-to-concept gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Identity first

The Moon Cannon is an energy-assisted cannon with a distinctive forked magenta muzzle, three bright neck bands and a rounded dark chamber with raised pink details. Its released description says it converts a portion of damage into energy damage. The new design preserves that visual language instead of turning it into a generic rifle.

![Original released Moon Cannon sprite](moon-cannon-original.png)

## Premium concept study

![Moon Cannon premium concept and proposed attachment study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moon-cannon-concept-v1.png)

**Concept art only. Native upgraded weapon acceptance remains open.** The crescent attachment and ion impact panel are proposed upgrades/cosmetics. They do not establish original area damage, terrain destruction, or an implemented attachment. Generated side views require reconciliation before modeling; the depicted grip and trigger are not hand-clearance proof.

## What the released weapon actually does

Pinned source: **AoA 3.7.1, Minecraft 1.20.1**. [Source evidence](moon-cannon-source-evidence.json).

| Property | Inspected release |
|---|---|
| Registered damage input | 21 |
| Durability | 855 |
| Firing delay | 25 ticks |
| Constructor recoil input | 0.18; not a measured rendered kick |
| Base ammunition | Cannonball, inherited from BaseCannon |
| Automatic fire | No, inherited BaseCannon return |
| Projectile | MoonShotEntity; age parameter 120, piercing parameter 0 |
| Damage routing | 75% heavy-gun helper and 25% energy-projectile helper |
| Upgrade recipe | Energy Cannon + Lunar Upgrade Kit → Moon Cannon |
| Firing sound reference | ITEM_ENERGY_CANNON_FIRE |

The two damage factors operate on the adjusted damage input. Living-target attribute scaling and the downstream helpers matter, so this is **not a guarantee of 21 final health damage**. The energy attack is attempted after the heavy attack branch even when that heavy helper rejects its attack. Preserve this ordering, including the conditional knockback behavior; do not combine the calls into an assumed equivalent single hit.

The packaged upgrade recipe is a verified lineage. It does not prove an invented manufacturer, planetary origin, or material lore. Native acquisition and balance still need in-game verification for the selected pack.

## Proposed animation and feel

- Distinct cannon cadence: short rearward impulse, slower weighty settling and a sequential neck-band pulse.
- Forked emitter briefly converges its glow toward the projectile origin; solid geometry must retain clearance.
- Optional inspection exposes a cosmetic chamber diagnostic, then restores every moving component before firing resumes.
- Optional reload presentation must preserve the original cannonball cost and support the no-reload option.
- Sound layers follow the native fire event once; no duplicate damage or ammo use from animation callbacks.

## Attachment and crafting studies

| Proposed component | Player-facing role | Required safeguards |
|---|---|---|
| Crescent focusing shroud | More focused visual discharge and an optional precision tradeoff | Explicit stat tuning; visible geometry and projectile origin stay aligned |
| Stabilizing rear brace | Reduced cosmetic sway / separately balanced handling | Real player-arm clearance and both handedness settings |
| Lunar lens sight | Pink aim reticle with a readable non-bloom center | Keep target visibility and accessibility settings |
| Resonance charm | Earned cosmetic plus explicitly described progression bonus | No hidden stacking or duplication when salvaged |
| Alternate neck assembly | Deliberate delivery variant, not arbitrary extra damage from decorative rings | Separate recipe, declared behavior, ammo/resource and multiplayer tests |

## Full feature acceptance checklist

- [ ] Original sprite, versioned behavior and concept comparison approved
- [ ] Faithful model in both world-fitting and premium visual modes
- [ ] Independent moving parts, clean topology/UVs and readable materials
- [ ] Real native wide/slim arms, grip, trigger and support-hand clearance
- [ ] Idle, equip, fire, recovery, aim, inspect and optional reload animations
- [ ] Muzzle, projectile/tracer, impact, decals and optional defeat effects
- [ ] Audio timing, interruptions and reduced-effects settings
- [ ] Crafting, attachment swaps, salvage, charms, skins and stickers
- [ ] Native performance, server authority, saves and compatibility tests

Original projectile flight and impact captures are still required. The concept illustration is not a substitute for that evidence.
