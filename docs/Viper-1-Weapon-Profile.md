# Viper-1 · warm armor, dark optics and poison

**AoA 3.7.1 / Minecraft 1.20.1 · released-source profile and partial concept study. Native and final-art acceptance remain open.**

## What it actually does

Viper-1 is a **Metal Slug sniper** with **SCOPE_2**. Its impact-effect hook requests **Poison II for 60 ticks**, nominally three seconds at 20 TPS, when the target is a living entity. The bundled EffectsLib uses a one-based level: `level(2)` becomes Minecraft amplifier `1`. It is not Poison III.

This is an effect request, not guaranteed poisoning through immunities, event cancellation or other mods. The inspected class does not replace Metal Slugs with venom ammunition or add a cloud attack. Optional new effects must not silently change that contract.

| Released input | Value |
|---|---:|
| Damage | 30 |
| Durability | 185 |
| Delay | 89 ticks, nominally 4.45 seconds at 20 TPS |
| Recoil modifier | Approximately 0.06 |
| Ammunition | Metal Slug |
| Scope | SCOPE_2 |
| Impact request | Poison II, 60 ticks, living targets |
| Sound | Metallic sniper, long variant |

These inputs are not measured final damage or native visual evidence. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Viper1.java) · [Released evidence and library hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/viper-1-released-evidence.json).

## Original identity and crafting

![Released Viper-1 sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/viper-1-original-preview.png)

Retain the charcoal upper body, muted reddish-brown lower/front and rear sections, gray caps and muzzle, central dark grip and raised optic with red accents. Poison does not justify replacing its recognizable original colors with an all-green snake novelty.

![Viper-1 six-slot infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/viper-1-infusion.webp)

Infuse **Sniper Frame** with **two Dense Rocks**, Jungle Thorns, **two separate iron-ingot-tag ingredients** and one gunpowder-tag ingredient. Preserve all six occupied slots. The middle placement is order-independent; icons for tags show example members. These ingredients do not establish a specific maker, dimension of manufacture or extra lore. [Infusion Table tutorial](Infusion-Table-Crafting-1.20.1).

## Proposed premium treatment

![Viper-1 warm red-brown and graphite concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/viper-1-concept-v1.png)

The proposal uses warm layered panels, graphite framing, gray edges and restrained red optic accents. A small optional green status accent is separate from the default appearance. The open trigger guard and rear grip look coherent in the painted views, but actual hand clearance, opposite-side construction and all moving poses still require model/native review.

## Full feature plan

- **Presentation:** faithful Minecraft-fit and premium material modes, meaningful roughness/detail, clean UVs and distance-readable shapes.
- **Modules:** optic housing, shroud, grip and handling alternatives; earned charms with declared bonuses and collision-safe placement.
- **Conversions:** any venom-themed alternate projectile, beam or cloud must be a separately balanced opt-in module with explicit resource and hit rules. Default Metal Slug behavior stays documented.
- **Animation:** equip, idle, locomotion, aim, confirmed fire, recovery, optional reload and inspection with interruption recovery.
- **Feedback:** original/new projectile and impact captures, muzzle/tracer choices, expiring surface decals and confirmed-kill finishers; cosmetic status glows do not prove poison applied.
- **Crafting/customization:** attachment recipes, skins, stickers, animated/glowing emblems, salvage, effect transfer and saved-build migration.
- **Qualification:** effect immunity/cancellation, repeated hits, multiplayer authority, TaCZ/turret integration, reduced effects and measured startup/frame-time/memory costs.

## Acceptance gates

- [ ] Original native projectile, scope, sound and poison evidence
- [ ] Poison level/duration, immunity and event-cancellation regressions
- [ ] Complete attachment, conversion, inspection and effects concepts
- [ ] Faithful model, both texture modes and full hand/attachment clearance
- [ ] Native animations, multiplayer, migration and compatibility checks
- [ ] Equivalent-scene performance and accessibility checks

[Armory](Weapon-Overhaul) · [Weapon completeness standard](Weapon-Completeness-Standard)

Original identity/assets belong to Tslat and contributors. New art and implementation proposals remain separate from released mechanics.
