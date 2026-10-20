# Shyre Blaster · gold ribs and a cyan mineral heart

[Weapon overhaul](Weapon-Overhaul) · [Illustrated armory](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html) · [Cannon progression](Cannon-Progression-and-Recipes-1.20.1)

![Premium and world-fit Shyre Blaster proposals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shyre-blaster-concept-v1.png)

**AoA 3.7.1 / Minecraft 1.20.1.** Released-source profile and partial concept exploration. The art is not a playable model, an exported texture pack or proof of completed animations.

## Keep its unusual original shape

![Actual released Shyre Blaster sprite, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shyre-blaster-original-preview.png)

The sprite combines a golden stepped front body, bright cyan bands, a grey collar and a distinctive hollow gold/grey rear loop. The concept retains those identifying shapes instead of turning the weapon into a generic rifle. Sculpted gold surfaces, mineral inlays and the floating inspection gem are proposed refinements. Both detailed and world-fit treatments must remain recognizable as the same prop.

The recipe explicitly uses Shyrestone and Shyregem tags, which supports a mineral-themed direction. The inspected recipe and sprite do not establish a specific maker, ancient civilization or complete creation story. The material loot definitions alone do not prove a world-generation location or that every related dimension is playable in this release. Keep unverified lore separate from those source facts.

## It is registered as a cannon

Despite “Blaster” in the name, this item extends **BaseCannon**, not the Spirit-powered blaster firing branch. ShyreBlaster itself declares only its constructor and the **BIG_BLAST_FIRE** sound override.

| Stored registration input | Value |
|---|---:|
| Damage parameter | 25.5 |
| Durability | 850 |
| Firing delay | 30 ticks |
| Recoil | approximately 0.15 |
| Ammunition | Cannonball, inherited |
| Full automatic | False, inherited |

Shared cannon impact behavior adjusts its attack input using target armor/toughness and applies its successful-hit shield/knockback handling. The stored damage parameter is not guaranteed final damage or measured DPS. No unique blinding, beam, explosion, healing or gem-reward effect is declared by ShyreBlaster in this inspected implementation.

## Original projectile and visual comparison

![Extracted original cannonball texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shyre-blaster-projectile-preview.png)

BaseCannon creates **CannonballEntity** with maximum age 120, piercing value zero and damage multiplier 1. CannonballEntity has no gravity override here, so it inherits **BaseBullet's 0.0 gravity return**. Do not copy the 0.1 gravity of Water Balloon Bomber or the 0.05 gravity of Ghoul Cannon into this weapon merely because all three are cannons. This single parameter is not a full runtime trajectory proof.

The registered renderer is the ordinary **TexturedProjectileRenderer** using cannonball.png. It draws a camera-facing textured quad and does not contain a dedicated particle-emission loop. The cyan wake, muzzle ring, floating gem and dramatic stone-chip impact on the concept sheet are new presentation ideas. They are not evidence of the original renderer or terrain damage. Original in-flight and impact game footage remains required.

## Crafting: five ingredient slots, not five in one stack

![Reconstructed Shyre Blaster infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shyre-blaster-infusion.webp)

[Open the exact interactive recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Ainfusion_shyre_blaster)

1. Place a **Cannon Frame** in the Infusion Table's separate base slot.
2. Fill **two Shyrestone-ingot-tag slots**, **two Shyregem-tag slots**, and **one Gunpowder-tag slot**.
3. Leave four ingredient slots empty. Ingredient order is flexible, but a single stack does not stand in for repeated occupied slots.
4. Check the effective recipe and Imbuing requirements. The bundled recipe omits infusion_level; the inspected recipe factory defaults to level 1. Other versions or datapacks can differ.

The displayed tag items are examples. The bundled Shyrestone and Shyregem tags contain their corresponding AoA items, but pack changes may add alternatives. The diagram is reconstructed documentation, not a native crafting-screen capture.

## Distinctive customization proposals

- **Cyan mineral sight:** a restrained visual aiming cue that does not obscure targets. The original hollow rear loop remains visible.
- **Prism-ring shell:** a removable visual ring treatment. It must not imply a beam or damage multiplier unless a separately defined functional variant actually changes those rules.
- **Functional variants:** an explicitly crafted focused ray or split-prism shot could expand the fantasy identity, with declared damage, range, resource and handling tradeoffs. These are new designs, not baseline behavior.
- **Finishes:** polished gold, worn gold and Minecraft-fit textures, preserving the characteristic cyan/grey contrast and checking UV seams and bright surfaces under real lighting.
- **Earned charms and emblems:** gemstone charms, static or animated stickers and glow presets with declared sockets, bounded animation and optional perk rules.
- **Feedback customization:** muzzle pulse, tracer, impact decal and optional crystalline defeat effects. Cosmetic chips must not remove world blocks or bypass server death/reward logic.
- **Inspection:** a brief suspended-gem flourish inside the rear loop, then an unambiguous return to idle. Keep firing state and resources authoritative throughout interruption and weapon swaps.
- **Optional loading:** retain the original Cannonball contract by default; a more elaborate prop must not impose unrequested reload delays or grant free ammunition through animation events.

## Full production gates

- [ ] Build the actual canonical model and compare it against the original sprite and selected concept from all relevant views.
- [ ] Prove comfortable hand/guard clearance, rear-loop usability, attachment fit and moving-part separation with actual player hands.
- [ ] Finish equip, holster, idle, aim, firing/recovery, inspect and appropriate optional loading animations with interruption tests.
- [ ] Expand original-versus-proposed flight, muzzle, tracer, impact, decal and defeat-effect boards.
- [ ] Implement reversible skins, craftable variants, charms, stickers and handling parts with explicit gameplay differences.
- [ ] Capture and test the original cannon trajectory and impact behavior; preserve its inherited firing family and resource rules.
- [ ] Qualify native export, multiplayer, optional integrations and equivalent-work startup/frame-time performance.

## Evidence

[Structured registration, class, recipe and tag evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shyre-blaster-released-evidence.json) · [Pinned ShyreBlaster source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/ShyreBlaster.java) · [Shared cannon behavior](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/BaseCannon.java) · [Projectile class](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/entity/projectile/cannon/CannonballEntity.java) · [Resolved cannon gravity comparison](Cannon-Projectile-Behavior-1.20.1)

Original AoA identity and assets are credited to Tslat and contributors. No native upgraded weapon acceptance is promoted by this page.
