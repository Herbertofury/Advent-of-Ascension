# Bayonette SR · jade, violet and close-range utility

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept. Native and final-art acceptance remain open.**

## Original behavior: ranged and melee are separate

Bayonette SR is a **Metal Slug sniper** with inherited **SCOPE_1**, plus a main-hand melee attribute modifier. Its ranged damage input is **33**. The melee modifier is **+9 attack damage**, using an additive modifier in the main-hand equipment slot; the tooltip prints **10 attack damage**. Do not add nine to every bullet or claim a guaranteed ten damage after armor, attack strength, effects and other modifiers.

| Released input | Value |
|---|---:|
| Ranged damage input | 33 |
| Durability | 300 |
| Firing delay | 86 ticks; nominally 4.3 seconds at 20 TPS |
| Recoil modifier | Approximately 0.06 |
| Ammunition | Metal Slug |
| Scope | SCOPE_1, inherited |
| Firing sound | Medium sniper, long variant |
| Main-hand melee attribute | +9, additive |

The melee `hurtEnemy` callback requests **one durability damage** and broadcasts a main-hand break event when broken. This is a durability request through the normal item mechanism; enchantments and other systems may affect the result. Offhand behavior does not gain the main-hand attribute automatically.

[Named implementation](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/BayonetteSR.java) · [Released-class, recipe and tag evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bayonette-sr-released-evidence.json).

## Original appearance and infusion

![Original Bayonette SR sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bayonette-sr-original-preview.png)

Preserve the stepped teal body panels, violet upper/rear shapes and optic, pale gray front assembly and lower silver blade silhouette. The new material treatment does not establish undocumented jade construction, a particular maker or an origin dimension.

![Bayonette SR six-slot infusion](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bayonette-sr-infusion.webp)

Infuse **Sniper Frame** with Mushroom Spores, an Iron Sword, **two separate Mystite-ingot-tag ingredients**, one amethyst-gem-tag ingredient and one gunpowder-tag ingredient. Preserve all six occupied slots. Mystite Ingot is verified in AoA’s ingredient tag; Amethyst Shard is the example in [Forge’s 1.20.1 amethyst tag](https://github.com/MinecraftForge/MinecraftForge/blob/1.20.1/src/generated/resources/data/forge/tags/items/gems/amethyst.json). Loaded datapacks may change tag membership. The diagram is reconstructed, not a native capture. [Infusion Table guide](Infusion-Table-Crafting-1.20.1).

## Premium visual study

![Bayonette SR jade-violet concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bayonette-sr-concept-v1.png)

The concept retains a distinct pale lower-front blade, teal shell, purple framing and closed trigger guard. The enhanced faceted blade and optic illumination are artistic proposals. Grip/stock clearance, aim alignment, blade clipping against held-item animations, view consistency and attachment intersections still require actual geometry and native tests.

## Complete feature plan

- **Materials:** faithful Minecraft-fit and premium concept-directed modes; preserve the jade/violet/silver identity through UV, wear and LOD work.
- **Modules:** separate visual shrouds, optics, grips, stock treatments and earned charms. Any melee bonus must be an explicit balanced gameplay module.
- **Optional conversions:** fantasy energy-edged or alternate ranged modules may be explored separately. Do not silently combine the +9 melee attribute with ranged damage.
- **Animations:** equip, idle, aim, ranged fire/recovery, melee swing, movement, optional reload and inspection. Validate interruption recovery and switching between melee and ranged states.
- **Effects:** baseline ranged flight/impact and melee feedback capture; optional muzzle, tracer, impact, decal and confirmed-kill finishers; reduced-effects controls.
- **Crafting/customization:** attachment recipes, salvage/effect transfer, skins, stickers, animated/glowing emblems, charms, named builds and save migration.
- **Integration:** main/offhand attributes, durability/enchantment behavior, duplicate modifiers, TaCZ/turrets, multiplayer authority and measured performance.

## Acceptance gates

- [ ] Capture original native ranged and melee behavior, scope, sound and impact
- [ ] Test main/offhand attribute changes, durability, break events and enchantments
- [ ] Verify infusion slots and tag-member alternatives in-game
- [ ] Complete attachment, inspection, conversion and effects concept sheets
- [ ] Model both texture modes and validate hands/blade clearance through all poses
- [ ] Qualify native integration, multiplayer, migration and performance

[Armory](Weapon-Overhaul) · [Completeness standard](Weapon-Completeness-Standard)

Original AoA identity/assets: Tslat and contributors. New art and mechanics remain separate from released facts.
