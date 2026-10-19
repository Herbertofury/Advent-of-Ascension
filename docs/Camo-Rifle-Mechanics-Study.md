# Camo Rifle · selected-slot camouflage contract

**Source-only study · AoA 3.7.1 / Minecraft 1.20.1. Upgrade artwork is pending; this page does not add an illustrated concept or certify a native upgrade.**

## What the released weapon does

The Camo Rifle is a **Metal Slug sniper** using **SCOPE_2**. Its inventory-tick override requests **five ticks of Invisibility** for the holder only when all four conditions hold:

1. Execution is on the server side.
2. The item is selected.
3. The holder reports the shift key down.
4. The holder is a living entity.

Five ticks is nominally 0.25 seconds at 20 TPS, refreshed by eligible inventory ticks. This is not a five-second effect, an on-hit effect, or a permanent invisibility switch. The selected-slot condition must not be broadened to every inventory copy or assumed to include an offhand-only copy. The class does not explicitly remove all invisibility when a condition stops; preserve other sources of the effect.

| Released input | Value |
|---|---:|
| Damage | 31.5 |
| Durability | 150 |
| Delay | 84 ticks, nominally 4.2 seconds |
| Recoil modifier | Approximately 0.06 |
| Ammunition | Metal Slug |
| Scope | SCOPE_2 |
| Sound | Metallic sniper, long variant |
| Holder effect request | Invisibility, five ticks per eligible inventory tick |

Source inputs are not measured final damage, visibility or performance. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/CamoRifle.java) · [Pinned evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/camo-rifle-released-evidence.json).

## Preserve the original appearance

![Released Camo Rifle sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/camo-rifle-original-preview.png)

Keep the forest-green camouflage, long gray barrel, dark central grip, broad rear silhouette with negative space, raised optic and blue lens accents. No particular manufacturer or dimension of origin is established by the inspected class and recipe.

## Crafting tutorial

![Camo Rifle infusion ingredients](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/camo-rifle-infusion.webp)

Place **Sniper Frame** in the base slot. Supply **two Jungle Thorns**, **Grass** (`minecraft:grass` in this version), one iron-ingot-tag ingredient and one leaves-tag ingredient. The center order is flexible; both thorn slots remain required. Baobab Leaves are a verified member of the released item leaves tag and illustrate that slot. Grass and leaves use untinted reference art here; a native-color capture remains a presentation improvement. [Full Infusion Table tutorial](Infusion-Table-Crafting-1.20.1).

## Upgrade requirements

- Keep the four-part server/selection/shift/living gate explicit in any adapter.
- Keep the short refresh duration; never convert it to a long permanent effect silently.
- Do not remove invisibility granted by potions, other equipment or other mods when switching away.
- Treat ghosting, optical shimmer and inspect effects as client presentation proposals until tested. Held gear, armor and attachments may remain visible under vanilla rules; do not promise full optical camouflage from this source alone.
- Retain the complete weapon feature checklist: both texture modes, faithful concepts/model, attachments and functional conversions, optional reload, inspections, original/new projectiles and impacts, decals, finishers, charms, skins, emblems, crafting/salvage and migration.
- Keep cosmetic work bounded to relevant holders and visible items. Avoid introducing inventory-wide scans or unconditional new per-frame effects; measure any actual optimization with equivalent gameplay.

## Native test matrix

| Case | Source expectation to verify |
|---|---|
| Server, selected, shift held, living holder | Requests five ticks of invisibility |
| Client only | No request from this branch |
| Unselected inventory copy | No request |
| Shift released | No new request |
| Nonliving holder | No request |
| Offhand-only copy | Do not assume selected status; test exact engine callback |
| Other invisibility source active | Preserve its ownership/duration semantics |
| Slot switch, death, reconnect, dimension change | No sticky new camouflage state |

- [ ] Obtain and review upgrade concept artwork
- [ ] Capture original native visibility, held items, scope, sound and projectile behavior
- [ ] Capture native-colored crafting icons
- [ ] Test all selection, shift, multiplayer and existing-effect cases
- [ ] Build complete model, materials, attachments, animations and feedback
- [ ] Verify performance, accessibility and compatibility without feature loss

[Armory](Weapon-Overhaul) · [Weapon completeness standard](Weapon-Completeness-Standard)
