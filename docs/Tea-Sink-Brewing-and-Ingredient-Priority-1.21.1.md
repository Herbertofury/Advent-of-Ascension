# Tea Sink brewing and ingredient priority · Minecraft 1.21.1

**Version:** released AoA 3.7.16.1. A Tea Sink draws ingredients from your inventory when you use a Cup on a filled sink. There is no menu where you explicitly pick a tea flavor. The inspected release has two selection pitfalls, described below before you spend ingredients.

[Crafting and recipes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes) · [Crop growing and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Farming-Soils-and-Harvesting-1.21.1) · [Recipe search](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=tea_sink)

![Tea Sink and three-Cup shaped recipes, plus a static filled-sink reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/tea-sink-and-cup-recipes-1.21.1.webp)

## 1. Craft the station and Cups

The Tea Sink recipe uses **five items from the planks tag, one Iron Ingot and one Cauldron**. Follow the shaped arrangement in the illustration: planks down the left edge and across the bottom, Iron Ingot above the Cauldron in the middle column. The unused upper-right slots stay empty.

The Cup recipe uses **three Ivory** in a shallow V and produces **three Cups**. The pictured Oak Planks are one representative tag member, not the only allowed plank choice. Find Ivory through the current pack's loot/trade routes rather than replacing it with an ordinary bone.

Place the sink, then use a **Water Bucket** on it while it is empty. The inspected Survival path consumes one Water Bucket, gives back an empty Bucket and sets the filled state. Creative does not consume the bucket. Filling preserves the facing direction.

## 2. Prepare Tea Shreddings

Grow Tea from Tea Seeds using the farming guide's ordinary-crop rules. The released block-loot table selects Tea Shreddings at **age 7**; an immature crop instead uses the seed alternative. A separate mature-only pool provides Tea Seeds with a Fortune-aware bonus function. Do not break immature plants expecting the finished brewing ingredient.

Tea Shreddings must actually be found in your inventory for the brewing path, including in Creative. A picture of the crop, Tea Seeds or a tea drink does not substitute for the shreddings item.

## 3. Decide which inventory ingredients the sink will see

Hold a **Cup**, keep Tea Shreddings available, and inspect your carried additives before using the filled sink.

![Normal Tea, Fungal Tea and the released melon-return branch, with Creative-selection warning](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/tea-sink-selection-1.21.1.webp)

In the inspected Survival implementation:

| Ingredients found in inventory | Output selected | Additional ingredient consumed |
|---|---|---|
| No Mystic Shrooms and no Nature Melon Slice | Tea | None |
| Mystic Shrooms, with or without melon | Fungal Tea | 1 Mystic Shrooms |
| Nature Melon Slice, without shrooms | **Nature Melon Slice** | 1 Nature Melon Slice |

Every successful Survival brew also consumes **one Cup and one Tea Shreddings**. The searches inspect hands and inventory compartments; putting an additive in a different ordinary inventory slot does not opt it out. Store unwanted additives outside your inventory before brewing. Mystic Shrooms have priority over Nature Melon Slice.

### The melon branch does not produce Natural Tea in this inspected release

Natural Tea exists as a registered drink item. However, the selected released Tea Sink method loads **NATURE_MELON_SLICE** into the output variable after consuming that same additive. It has no NATURAL_TEA field reference. This means the inspected path consumes a Cup and Tea Shreddings while returning a melon slice, rather than making the expected tea.

This is a released-code finding with an independent state model, **not a live-game reproduction or a claim that your private Enderloom build still has it**. Avoid this branch until the actual candidate is checked. The intended repair should explicitly choose Natural Tea and verify all input/output quantities, not merely rename the tooltip.

### Creative selection behaves differently

Creative passes zero as the additive-consumption amount. The inventory helper immediately returns true for a non-positive amount **before checking whether the additive exists**. Consequently, after the Cup and Tea Shreddings prerequisites pass, the first additive branch selects **Fungal Tea even without Mystic Shrooms**.

A Creative demonstration therefore cannot validate the Survival no-additive or melon paths. Test the modes separately. The repair should separate “is this additive present?” from “how many should Creative consume?”

## 4. Drink, recover the Cup and refill when needed

Tea, Fungal Tea and Natural Tea each declare a Cup crafting remainder and a stack size of one. Their inspected consumption methods return the crafting remainder outside Creative. This is the source-defined cup-recovery path; unusual inventory/container mods still need in-game verification.

Their default food definitions include regeneration and resistance effects with different configured parameters. Read the exact target build's tooltip and effect display rather than treating all three drinks as identical healing potions. This page does not certify effect duration or stacking under another modpack.

After a successful brew, the sink calls its **one-in-seven depletion helper**. It may empty after an early brew; it is not a counter that guarantees exactly seven cups. Refill an empty sink with a Water Bucket. Creative still enters the depletion check in the inspected method.

## Troubleshooting

| Symptom | Check |
|---|---|
| Filled sink refuses interaction | Hold a Cup and carry actual Tea Shreddings. |
| Empty sink does nothing with a Cup | Fill it with a Water Bucket first. |
| You keep getting Fungal Tea | Remove Mystic Shrooms from your inventory; also distinguish Creative from Survival. |
| You get a melon slice instead of Natural Tea | This matches the inspected melon-output branch; stop spending Cups and shreddings on it. |
| Moving an additive to another slot did not help | The helper searches more than the active hotbar slot. Put it in external storage. |
| Water disappears before seven drinks | Depletion is chance-based, not a fixed-use counter. |
| Tea Seeds do not brew | Grow and harvest the mature crop for Tea Shreddings. |

## Evidence and restoration checklist

[Recipes, mature-crop loot, released methods and eight independent selection cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tea-sink-evidence-1.21.1.json) · [Image provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tea-art-evidence-1.21.1.json) · [Source findings and repair targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes).

Before marking the implementation repaired, test no additive, each additive, both additives, offhand and main inventory placement, missing Cup/shreddings, full inventory, Creative versus Survival, water refill/depletion, and Cup return after drinking. Verify the exact candidate's effect values and probability helper separately. No gameplay patch or performance claim is made here.

AoA artwork and systems are by Tslat and contributors; the vanilla recipe references are by Mojang/Microsoft. These are original source-model diagrams, not screenshots of a running game.
