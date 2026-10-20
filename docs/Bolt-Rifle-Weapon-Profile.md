# Bolt Rifle · ochre body and charcoal optic

**AoA 3.7.1 / Minecraft 1.20.1 · released-source profile and partial concept. Native upgrade and final-art gates remain open.**

## Original behavior

Bolt Rifle is a **Metal Slug sniper** using the inherited **SCOPE_1** overlay. The inspected subclass changes its firing sound to the metallic long sniper variant; it does not declare a special impact effect. Its name does not establish lightning damage, crossbow bolts, a native manual bolt-cycling mechanic or a reload requirement.

| Released input | Value |
|---|---:|
| Damage input | 30 |
| Durability | 100 |
| Firing delay | 100 ticks; nominally five seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.06 |
| Ammunition | Metal Slug |
| Scope texture | SCOPE_1, inherited |
| Firing sound | Metallic sniper, long variant |

Inputs are not final damage measurements. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/BoltRifle.java) · [Released class/recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bolt-rifle-released-evidence.json).

## Recognizable identity

![Original Bolt Rifle sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bolt-rifle-original-preview.png)

Keep the warm ochre/golden-brown body, descending rear stock, short gray muzzle, dark gray upper assembly and raised charcoal optic with small blue accents. The proposed wood-like finish is a visual interpretation. Planks in the recipe do not establish a particular timber species, maker or origin dimension.

## Seven-slot infusion

![Bolt Rifle infusion diagram](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bolt-rifle-infusion.webp)

Start with **Sniper Frame**. Add **three separate iron-ingot-tag ingredients**, one diamond-gem-tag ingredient, one gunpowder-tag ingredient and **two separate planks-tag ingredients**. Keep all seven occupied slots. The middle arrangement is order-independent.

Baobab Planks are illustrated as an example: they are explicitly listed in this release’s `minecraft:planks` item tag. That does not make Baobab mandatory. Other tag members may work, subject to the loaded datapacks. This is a reconstructed recipe diagram, not native screen footage. [Infusion Table tutorial](Infusion-Table-Crafting-1.20.1).

## Premium concept

![Bolt Rifle premium concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bolt-rifle-concept-v1.png)

The study adds richer golden-brown panels, gray metal framing and a restrained blue optic while retaining a compact forward muzzle. It remains an interpretation rather than an accepted game model. The stock-neck hand placement, full grip room, opposite-side consistency, trigger clearance and moving poses need actual hand/model tests. Painted details are not functional parts or implemented animation.

## Full upgrade direction

- **Materials:** Minecraft-fit and premium concept-directed textures, consistent roughness, deliberate wear, clean UVs and distance readability.
- **Modules:** wood/finish choices, optic housings, fore-end shapes, stock/grip handling options and compatible earned charms. Label balance changes explicitly.
- **Conversions:** optional stylized energy-pulse or other alternate barrels may be separately crafted. Default Metal Slug behavior remains documented; lightning is not implied by the name.
- **Animation:** equip, idle, aim, fire, recovery, locomotion, optional reload and inspect with interruption recovery. A proposed cycling flourish must not silently alter the original cooldown or ammunition contract.
- **Effects:** original projectile/impact capture, custom muzzle/tracer/impact options, temporary decals, reduced-effects settings and confirmed-kill-only finishers.
- **Crafting and personalization:** attachment recipes, salvage, transferable effects, skins, charms, glowing/animated stickers, personal emblems, named builds and migration.
- **Qualification:** hands, attachment motion, multiplayer authority, TaCZ/turret support, resource conservation, startup cost and equivalent-scene performance.

## Acceptance gates

- [ ] Capture original native projectile, impact, SCOPE_1 and firing sound
- [ ] Verify all seven infusion ingredients and alternative tag members in-game
- [ ] Complete attachment, conversion, inspection and effects concept sheets
- [ ] Model and texture both presentation modes with complete hand/pose clearance
- [ ] Implement native features, compatibility, save migration and multiplayer checks
- [ ] Measure frame times, loading/memory and accessible reduced-effects behavior

[Weapon overhaul](Weapon-Overhaul) · [Completeness standard](Weapon-Completeness-Standard)

Original identity/assets: Tslat and contributors. New proposals remain separate from released mechanics and lore.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
