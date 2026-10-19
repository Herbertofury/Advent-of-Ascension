# Coral Cannon

> AoA 3.7.1 / Minecraft 1.20.1 source baseline. Concept art is a redesign proposal. No upgraded native build or final-art acceptance is claimed.

## What it actually does

Coral Cannon launches a Heavy Blue Cannonball using Cannonball ammunition. After calling shared cannon impact handling, it requests **1 health point of healing for the shooter** when the target is a living entity. The subclass does not check whether that damage was accepted before requesting healing. The shared helper still requires the shooter to be alive and between zero and maximum health.

It is a faster, lower-per-shot-damage counterpart to Aqua Cannon in the inspected registration. Its name does not establish a water jet, coral-spawning attack, origin dimension or underwater bonus.

| Stored input | Coral Cannon | Aqua Cannon |
|---|---:|---:|
| Damage argument | 12 | 14 |
| Durability argument | 300 | 300 |
| Firing delay, ticks | 15 | 35 |
| Recoil argument, rounded | 0.35 | 0.21 |
| Healing request per qualifying impact | 1 health point | 2 health points |

These are constructor and hook values, not measured final damage, guaranteed healing, or sustained native DPS. Shared cannon handling scales its attack input by `1 + (armor × 1.5 + toughness × 0.5) / 100` for living targets before calling its heavy-attack helper. Other game systems can affect the outcome.

The projectile constructor uses maximum age 120 ticks and piercing value 0. The projectile class supplies damage multiplier 1 and gravity 0.1. The final constructor argument is piercing, not gravity. Firing sound: `ITEM_HIGH_CANNON_FIRE`.

[Coral Cannon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/CoralCannon.java) · [Released class hashes and evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/coral-cannon-released-evidence.json) · [Aqua comparison](Aqua-Cannon-Weapon-Profile).

## Original identity and upgrade concept

![Original released sprite enlarged without smoothing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/coral-cannon-original-preview.png)

Preserve the short orange-red muzzle, cobalt horizontal body and vivid magenta branching accents and lower supports. The reef-like sculpting below elaborates that palette and shape; it is new visual storytelling, not verified lore about a maker, biome or crafting material.

![Coral Cannon concept study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/coral-cannon-concept-v1.png)

The concept has strong palette continuity and a complete trigger loop. The branching foregrip still needs a hand blockout and clearance review. Its heavy organic surface detail must be translated deliberately into both an in-world texture style and an optional high-detail presentation. This is not a finished mesh.

## Projectile and effects

![Released cannonball texture, not a flight capture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/coral-cannon-projectile-preview.png)

The shared Heavy Blue renderer uses the ordinary dark cannonball texture plus blue Sparkler particles. It requests eight particles per render invocation, making emission demand render-rate dependent. See [Particle Emission and Frame Time](Particle-Emission-and-Frame-Time) for a tested headless scheduling prototype and its explicit native/visual qualification limits.

Proposed effects keep the discrete dark core readable: a short blue muzzle glint, restrained trailing motes, and a compact impact sparkle. A healing cue should indicate actual health gained, rather than promise healing on every impact. A death effect must require a confirmed kill. Optional coral shards, reef-ring impacts and pearlescent tracers are customization proposals, not original behavior.

## Crafting, provenance and lore

No direct `aoa3:coral_cannon` reference was found in the inspected release's data JSON files. That does not prove the item is unobtainable: code-defined acquisition, older versions and external data require separate investigation. No recipe or origin dimension is invented here. Historical acquisition belongs in a clearly versioned section once verified.

## Full-feature production checklist

- [ ] Native original flight and impact captures, including underwater behavior
- [ ] Hand-fit blockout; no branches, trigger or attachments intersect hands or controls
- [ ] Distinct world-fit and high-detail materials with readable surface hierarchy
- [ ] Idle, equip, aim, fire, inspect and optional reload/recharge animations
- [ ] Preserve original ammo and healing semantics in the baseline mode
- [ ] Optional cosmetic coral crown, pearl sight and smooth reef-grip attachments
- [ ] Gameplay-changing barrel variants with explicit resource costs and balance tests
- [ ] Earned charms, decals, animated/glowing stickers and custom emblems
- [ ] Projectile, tracer, impact and confirmed-kill effect customization
- [ ] Craftable variants with documented recipes and progression
- [ ] Native export, offhand, multiplayer, turret and compatibility checks
- [ ] Particle budgets, texture memory, LODs and frame-time measurements

Any beam, spread or chain-lightning variant would be a new gameplay mode. Its visible barrel, firing behavior, ammunition/resource use and damage must agree; it must not silently replace the original single-projectile baseline.
