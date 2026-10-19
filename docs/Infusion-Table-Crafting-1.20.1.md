# Infusion Table crafting · 1.20.1

**Minecraft 1.20.1 / AoA 3.7.1.** A practical, release-specific walkthrough checked against the packaged recipes and released menu/recipe bytecode. This release contains **353 bundled `aoa3:infusion` definitions**, including crafting and enchanting paths. That count does not prove every ingredient is obtainable in survival.

[Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1) · [Crafting overview](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes) · [Modern 1.21.1 guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1)

## 1. Make the workstation

![Released 1.20.1 station recipe: wool across the top, Ancient Rock around an Infusion Stone in the middle, obsidian across the bottom](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/infusion-table-recipe-1.20.1.webp)

At an ordinary crafting table, arrange:

| Wool-tag item | Wool-tag item | Wool-tag item |
|---|---|---|
| Ancient Rock | Infusion-Stone-tag item | Ancient Rock |
| Obsidian | Obsidian | Obsidian |

Total: **3 wool, 2 Ancient Rock, 1 eligible Infusion Stone and 3 obsidian**, producing one Infusion Table. The red wool and Ambient Infusion Stone in the illustration are examples of tag members.

The packaged `aoa3:infusion_stone` item tag accepts Ambient, Blooming, Glaring, Gleaming, Glistening, Glowing, Radiant or Shining Infusion Stone. Use one of them, not all eight. Other installed data packs can change the final tag contents.

**Version trap:** the checked 1.21.1 release has a different station recipe. Do not mix its amethyst/enchanting-table recipe with this 1.20.1 walkthrough.

## 2. Put the base on the left

Open the placed Infusion Table. Its checked input layout has:

- One separate base slot on the left, input index 0
- Nine ingredient slots in the middle
- One output slot on the right

The recipe JSON calls the base `input` in this release. Put that item in the separate left slot. Put the listed `ingredients` in the middle grid. Their middle-grid order can vary; the diagram below is one easy arrangement, not an additional shaped pattern.

There is no furnace-style fuel slot in this checked menu. Do not put a fuel item into a spare ingredient slot while trying to match an ordinary infusion recipe.

## 3. Make a Ginger Blaster

![Shotgun Frame in the left base slot; two Sour Gummies in separate slots, Spreadshot, sugar, iron and a gingerbread item in the middle; Ginger Blaster output](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/infusion-ginger-layout-1.20.1.webp)

| Where | What to put there |
|---|---|
| Separate base slot | 1 Shotgun Frame |
| Two separate middle slots | 1 Sour Gummy in each |
| Another middle slot | 1 Spreadshot |
| Another middle slot | 1 Sugar |
| Another middle slot | 1 item matching `forge:ingots/iron` |
| Another middle slot | 1 item matching `forge:gingerbread` |
| Remaining three middle slots | Empty |

The packaged gingerbread tag contains **Gingerbread Cookie OR Gingerbread Wing**. Either can fill that one slot; both are not required. The image uses the Cookie and a normal Iron Ingot as representative tag members.

### Two Gummies means two slots

The released matcher counts occupied ingredient slots and compares that count with the number of ingredient entries. For simple ingredients, it contributes at most one item from each occupied slot to the matching calculation.

A stack of two Sour Gummies in one slot therefore does **not** replace two separate Gummy entries. Split it. You may keep a larger stack in each correct slot for repeated crafting, but each stack still occupies only one required slot. Remove unrelated items from the three unused cells.

[Browse this released recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=ginger_blaster) · [Ginger Blaster design and original behavior](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ginger-Blaster-Weapon-Profile)

## 4. Check Imbuing and take the result

The checked menu consults **Imbuing** and the recipe's infusion-level requirement. Do not assume a guide for the historical Infusion skill describes this release's menu gate.

For ordinary crafting, the released factory defaults to requirement **1** and XP range **0–0** when those fields are omitted. Ginger Blaster's packaged recipe omits them. Its recipe therefore does not establish an Imbuing XP-training loop. Other recipes can specify different requirements and rewards; inspect their exact release definitions.

Taking the result uses the checked generic crafting-slot handler: it removes **one item from every occupied input slot**, including the left base, and processes crafting remainders. The Shotgun Frame is consumed; it is not a permanent mold. Remainders may return to slots, merge, enter your inventory or drop when insertion fails. Test unusual modded ingredients and automation separately.

### Protect named or modified input weapons

The ordinary recipe assembly branch returns a copy of the recipe's declared output. It does not, in that method, copy arbitrary input NBT into the result. Do not assume an upgrade preserves a custom name, enchantments, third-party attachments or other data. Use an unmodified test item or a copied test world first. The enchanting branch is a separate code path and should not be generalized to every crafting upgrade.

## 5. If the result stays empty

1. Confirm Minecraft **1.20.1** and the exact AoA release. Pack recipes may override the bundled ones.
2. Put the Shotgun Frame in the separate base slot, not the middle grid.
3. Use six occupied middle slots, including two separate Sour Gummy slots. Leave three empty.
4. Check the final iron and gingerbread tags. A similarly named item is not automatically a tag match.
5. Check Imbuing requirements and any recipe-book restrictions your pack enables.
6. Remove optional extras and test one craft with plain inputs before automating or repeating it.
7. If another mod changes recipes or inventory handling, record the complete mod/data-pack versions and reproduce on a disposable copy.

## Evidence and limits

The diagrams are documentation compositions from source-derived item/block previews, **not in-game screenshots**. Bytecode review covers `InfusionTableContainer`, `InfusionRecipe`, its `Factory`, and `SlotCraftingMod`. Recipe definitions and tag members come from the pinned `AoA3-1.20.1-3.7.1-all.jar`.

[Source evidence and exact recipes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/infusion-tutorial-evidence-1.20.1.json)

JAR SHA-256: `f417ecb337d4a3b2aebec559a9262d8a86cc93ee7910f4eea64108bff063193a`.

This guide has source/data checks; a native game walkthrough, pack-specific tag verification and automation acceptance remain open. Availability, balance and unrelated custom recipe behavior are not certified by the recipe count.
