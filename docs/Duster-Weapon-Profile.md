# Duster · dark brown panels and teal optic

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept. Native implementation and final artwork remain unaccepted.**

## Released behavior

Duster is a **Metal Slug sniper** with inherited **SCOPE_1**. The inspected subclass selects the metallic long sniper sound and does not declare a unique impact effect. Its name does not prove a dust cloud, sand projectile, armor debuff or spread attack.

| Released input | Value |
|---|---:|
| Damage input | 21 |
| Durability | 170 |
| Firing delay | 60 ticks; nominally three seconds at 20 TPS |
| Recoil modifier | Approximately 0.09 |
| Ammunition | Metal Slug |
| Scope | SCOPE_1, inherited |
| Sound | Metallic sniper, long variant |

This lower delay is a released input, not a claim about observed animation speed or damage per second. Armor, enchantments and other systems require separate tests. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Duster.java) · [Released evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/duster-released-evidence.json).

## Original identity

![Original Duster sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/duster-original-preview.png)

Keep the dark brown central/rear body, broad graphite fore-end and gray strip, hanging front silhouette, charcoal scope with teal ends and separate dark grip. The hanging shape’s functional purpose is not established by the sprite; the concept treats it as a visible support/handle detail. Leather-like surfaces are an interpretation consistent with the ingredient theme, not proof of maker or dimension lore.

## Six-slot infusion

![Duster infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/duster-infusion.webp)

Use **Sniper Frame** with **two iron-ingot-tag ingredients**, **two leather-tag ingredients**, one gunpowder-tag ingredient and one planks-tag ingredient. Preserve all six occupied slots; their middle-grid arrangement is order-independent. Baobab Planks are one verified example of the planks tag. Other displayed tag ingredients are examples, not mandatory identities.

The pictured leather comes from the project’s published 1.20.1 loot icon supplement. This diagram is reconstructed, not captured in-game. [Infusion Table tutorial](Infusion-Table-Crafting-1.20.1).

## Premium art study

![Duster dark brown and teal concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/duster-concept-v1.png)

The concept uses textured dark-brown panels, subdued metal and readable teal optic accents. It retains a front hanging detail and a closed trigger guard in both views. The forward housing is more elongated than the sprite and remains a proportion-review item. Hand reach, scope alignment, view consistency, real geometry and animation clearance still need qualification. A polished sheet alone is not final-art acceptance.

## Full feature direction

- **Presentation modes:** recognizable Minecraft-fit textures and premium detailed surfaces, with deliberate roughness, UV discipline and readable distance silhouettes.
- **Attachments:** optic shells, alternate fore-end profiles, stock/grip handling options, rear charms and configurable support detail. Clearly state any gameplay bonus.
- **Conversions:** separately crafted fantasy dust/pulse modules may be explored, but never represented as original behavior. Define ammunition, hit rules and costs explicitly.
- **Animations:** equip, idle, movement, aim, fire, recovery, optional reload and inspection; full hand room and interruption recovery.
- **Feedback:** original projectile/impact footage, muzzle/tracer/projectile choices, material-aware impact effects, expiring decals and confirmed-kill finishers.
- **Customization:** skins, stickers, animated/glowing emblems, earned charms, attachment recipes, salvage/effect transfer and saved-build migration.
- **Integration:** TaCZ/turrets, multiplayer authority, modded targets, resource conservation, reduced-effects mode and measured startup/frame-time/memory costs.

## Acceptance gates

- [ ] Capture original projectile, scope, firing sound and impact in the supported build
- [ ] Verify six-slot infusion and alternate tag-member behavior in-game
- [ ] Complete attachment, conversion, inspection and effects concepts
- [ ] Resolve proportions and validate hands/clearances across all moving poses
- [ ] Implement both material modes, native animations and compatibility tests
- [ ] Verify migration, performance and accessible reduced-effects controls

[Armory](Weapon-Overhaul) · [Completeness standard](Weapon-Completeness-Standard)

Original identity/assets: Tslat and contributors. New art and optional mechanics are proposals, separate from released behavior and lore.
