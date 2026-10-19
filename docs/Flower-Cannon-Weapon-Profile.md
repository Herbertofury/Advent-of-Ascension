# Flower Cannon

> AoA 3.7.1 / Minecraft 1.20.1 source baseline. Proposed artwork is not an in-game capture, finished model or native acceptance.

## What it does

Flower Cannon fires a Flower Ball using the inherited Cannonball ammunition. Its impact hook requests **Weakness I for 200 ticks**, nominally ten seconds at 20 ticks per second. The shared heavy cannon attack must report success before that hook runs; the target must be living. Immunities and other effect handling can still prevent or alter application.

| Stored input | Value |
|---|---:|
| Damage argument | 14.5 |
| Durability argument | 510 |
| Firing-delay argument | 23 ticks |
| Recoil argument, rounded | 0.21 |
| Projectile maximum age | 120 ticks |
| Piercing argument | 0 |
| Projectile gravity | 0.1 |
| Projectile damage multiplier | 1 |
| Effect request | Weakness I, 200 ticks |

The bundled EffectsLib level defaults to 1 and becomes Minecraft amplifier 0. These are source arguments, not measured final damage or guaranteed status application. Shared cannon handling adjusts attack input for armor/toughness before its heavy-attack helper. Firing sound is `ITEM_BALL_CANNON_FIRE`.

[Named weapon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/FlowerCannon.java) · [Released hashes and evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/flower-cannon-released-evidence.json).

## Released identity and premium concept

![Original Flower Cannon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/flower-cannon-original-preview.png)

Preserve the bright yellow front rim, compact leafy-green body and green lower silhouette. The infusion ingredients support its botanical identity, but do not prove a particular origin dimension, maker, living-weapon biology or manufacturing story.

![Revised botanical concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/flower-cannon-concept-v2.png)

The redesign elaborates the yellow petals and layered green surfaces. A first [retained concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/flower-cannon-concept-v1.png) placed the guard too far forward from the rear grip. The revision moves the single guard beside the grip and removes the misleading middle loop. Final scale, hand fit, leaf-tip clearance and animated poses still need a real blockout and rig.

The glossy leaf material is a concept direction. The world-fit version must preserve readable texture detail without excessive shine; a higher-detail option may retain more of the concept's surface work.

## Illustrated infusion recipe

![Flower Cannon infusion ingredients](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/flower-cannon-infusion.webp)

Place a Cannon Frame in the Infusion Table's base-input slot. Use seven ingredient slots: Small Green Petal, Rosid Root, Sticky Slime, Dandelion, two separate Limonite-ingot tag entries and one Jade-gem tag entry. Ingredient order is flexible; keep the two unused slots empty. The pictured ingot/gem are tag examples, not an exhaustive list of valid substitutes.

[Open the exact recipe card](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Ainfusion_flower_cannon) · [Station and progression guide](Cannon-Progression-and-Recipes-1.20.1).

This recipe omits an explicit infusion_level, so the inspected item-recipe factory defaults to Imbuing requirement 1. Creative mode and limited-crafting rules are handled by the container. Effective datapacks and tags may change availability.

## Projectile and impact presentation

![Released dark cannonball texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/flower-cannon-projectile-preview.png)

Despite the projectile's name, the renderer registration uses the ordinary dark cannonball texture. It adds **green Flickering Sparkler particles**, requesting eight per render invocation at projectile Y + 0.3. This is asset/code evidence, not captured flight footage.

The upgrade should preserve a readable discrete projectile and distinguish a hit from successful Weakness application. Optional petal trails, pollen rings or leaf-shaped impact accents are new cosmetic proposals, not original healing, area damage or plant growth. The shared render-rate emission concern belongs to [Particle Emission and Frame Time](Particle-Emission-and-Frame-Time); any replacement needs native visual calibration and frame-time measurements.

## Full-feature completion checklist

- [ ] Original flight and entity/block impact captures in the target release
- [ ] Hand blockout, guard clearance and leaf-tip collision checks through every animation
- [ ] World-fit and premium texture/material variants
- [ ] Equip, idle, aim, firing, inspect and optional reload/recharge animations
- [ ] Original ammo, cadence, damage path and Weakness-gating parity
- [ ] Cosmetic petal crowns, jade sights, smooth vine grips and earned botanical charms
- [ ] Clearly balanced alternate barrels with visible matching behavior and resource costs
- [ ] Craftable variants, skins, decals, glowing/animated stickers and custom emblems
- [ ] Projectile, tracer, impact and confirmed-kill effect customization
- [ ] Native export, offhand, turret, multiplayer and mod-compatibility checks
- [ ] Particle budgets, mip behavior, LODs, memory and frame-time tests

A seed scatter, focused beam or chain effect would be new gameplay, requiring its own resource and balance contract. Keep cosmetic pollen separate from gameplay debuffs, and offer reduced-particle/bloom options.
