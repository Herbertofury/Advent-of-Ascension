# Bulb Cannon

> Source baseline: AoA 3.7.1 / Minecraft 1.20.1. The redesign is concept art. Native upgraded weapon and final-art acceptance remain open.

## Identity and actual behavior

Bulb Cannon is a Cannonball-fed heavy projectile weapon with an impact effect that requests **Wither I for 160 ticks**, nominally eight seconds at 20 game ticks per second. This is not an unconditional application: the shared cannon attack must report success before its impact-effect hook runs, and the subclass requires a living target. Immunity and other effect handling remain relevant.

| Stored value | Released baseline |
|---|---:|
| Damage argument | 25 |
| Durability argument | 860 |
| Firing-delay argument | 30 ticks |
| Recoil argument, rounded | 0.15 |
| Projectile maximum age | 120 ticks |
| Piercing argument | 0 |
| Projectile gravity | 0.1 |
| Projectile damage multiplier | 1 |
| Effect request | Wither I, 160 ticks |

The bundled EffectsLib builder defaults to level 1 and subtracts one when constructing Minecraft's amplifier, yielding amplifier 0. A raw `1` level is therefore not Wither II. The shared cannon path scales attack input according to armor and toughness before its heavy-attack helper; the damage argument is not a guarantee of final health loss. Firing sound is `ITEM_WITHER_CANNON_FIRE`.

[Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/BulbCannon.java) · [Class hashes, bundled-library verification and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bulb-cannon-released-evidence.json).

## Original silhouette and design rationale

![Original Bulb Cannon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bulb-cannon-original-preview.png)

Retain the compact horizontal charcoal/burgundy body, segmented red lobes, low supports, rear grip and pale edge accents. Do not reinterpret the name as a household light bulb or replace its identity with a generic rifle.

![Revised abyssal upgrade concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bulb-cannon-concept-v2.png)

The crimson pod-like chambers and dark sculpted ribs elaborate the released silhouette. The Abyssal Upgrade Kit route is source-verified; a particular maker, material origin or biological manufacturing story is not. Those details remain optional design fiction until lore evidence supports them.

The [first concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bulb-cannon-concept-v1.png) is retained. Its underside ornament looked like a second trigger and the rear hand space was cramped. The revision removes that misleading control and opens the grip area. This is a visual correction, not a passed hand-rig collision test.

## Crafting and progression

![Wither Cannon plus Abyssal Upgrade Kit produces Bulb Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bulb-cannon-upgrade.webp)

The released `upgrade_kit_bulb_cannon.json` names Wither Cannon as input, Abyssal Upgrade Kit as the kit and Bulb Cannon as result. The diagram uses released item previews and is reconstructed from data; it is not a captured crafting screen. The released data provides two acquisition leads:

1. The bundled Wither entity loot table has one weapons-pool roll, choosing Wither Bow at weight 26 or Wither Cannon at weight 23. In that unmodified pool, the cannon selection share is 23/49, about 46.94%. This is a table calculation, not a guarantee that a modpack uses that exact effective table.
2. The Abyss world-loot table includes Abyssal Upgrade Kit in its dimension-specific pool: kit weight 1, Nightmare Flakes weight 20, empty weight 180. That is 1/201 per invocation of that pool. The table alone does not establish a per-mob-kill rate; eligible caller conditions and other loot modifiers still require verification.
3. With both items available, use the release's upgrade-kit recipe to obtain Bulb Cannon. Keep the Wither Cannon input and kit route distinct from infusion or ordinary shaped crafting.

[Released acquisition tables and hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bulb-cannon-acquisition-evidence.json). Check the active datapack/mod overrides when these drops do not match your world.

## Projectile, impact and presentation

![Released cannonball texture asset](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bulb-cannon-projectile-preview.png)

The Heavy Wither Ball renderer uses the ordinary cannonball texture with black Flickering Sparkler particles. It requests eight particles per render invocation. That draw-coupled emission pattern shares the optimization concern described in [Particle Emission and Frame Time](Particle-Emission-and-Frame-Time). No native flight or impact capture is supplied here.

A proposed upgrade may add a restrained dark trail, brief crimson muzzle pulse and an impact cue tied to confirmed effect application. Crimson pod glow is a presentation proposal, not proof that the original projectile is red, explosive or area-of-effect. Keep hit, status application and confirmed-kill feedback distinct.

## Full-feature plan and quality gates

- [ ] Capture original flight, entity impact and block impact in the target release
- [ ] Hand-rig and attachment clearance throughout idle, aim, firing and inspection
- [ ] World-fit textures plus optional high-detail materials
- [ ] Complete equip, idle, aim, fire, inspect and optional reload/recharge animations
- [ ] Preserve baseline ammunition, cadence, effect gating and resource costs
- [ ] Cosmetic rib crowns, low-profile sights, smooth grips and earned abyssal charms
- [ ] Explicitly balanced alternate barrels with visible behavior differences
- [ ] Unlockable skins, decals, glowing/animated stickers and custom emblems
- [ ] Custom projectile, tracer, impact and confirmed-kill effects
- [ ] Pictured craftable variants and upgrade routes
- [ ] Native export, offhand, turret and multiplayer compatibility
- [ ] Particle budgets, mip behavior, LODs, memory and frame-time measurements

A beam, scatter or chain-effect variant would be new gameplay and needs its own resource/balance tests. A visual bulb or extra barrel must correspond to actual behavior when sold as a functional upgrade. Optional effects must remain readable and accessible with reduced bloom/particles available.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
