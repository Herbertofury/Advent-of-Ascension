[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Skills](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Pixon harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2) · [Recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion)

# Historical Infusion Table: crafting and enchanting

> **Minecraft 1.12.2 / AoA 3.3.6.** This guide checks all 386 shipped Infusion recipe resources and selected released matching, output and container methods. It does not describe the modern 1.21.1 station or certify an Enderloom port.

## Start with the right interaction

Craft the table using the [illustrated starter recipe](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2#craft-the-starter-kit). Use it with an empty hand or a non-Infusion-Stone item to open the crafting interface. Holding an Infusion Stone instead enters the separate whole-stack conversion action.

The crafting area has **one separate base-item slot on the left**, a **3×3 ingredient area**, and an output slot on the right. It is not a normal ten-ingredient crafting grid: the base and ingredient area have different matching rules.

![Released Infusion GUI texture with Alacrity Boots and Sharpness II examples](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infusion-crafting-layout-1.12.2.webp)

## Two complete examples

### Craft Alacrity Boots

1. Put a **Boots Frame** in the separate left slot.
2. Put one **Armour Plating**, **Padded Cloth**, **Crystallite**, **Sapphire**, and **Floating Stone** into five separate ingredient slots. Their positions within the 3×3 area are interchangeable.
3. Keep the other four ingredient slots empty. The selected recipe defaults to **Infusion level 1**.
4. Take the **Alacrity Boots** from the result slot. The selected take-handler consumes one from each occupied input slot, including the base slot.

[Inspect the illustrated recipe and source fields](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Farmour%2Falacrity%2Falacrity_boots). The output is a copy of the recipe’s declared result; arbitrary custom name, damage or NBT from the base item is not automatically inherited by this transformation branch.

### Apply Sharpness II

1. Reach **Infusion level 10** and put compatible equipment in the separate left slot. The diagram uses an ordinary Iron Sword as an example.
2. Put **two Damage Enhancers in two distinct ingredient slots**, plus **one Glistening Power Stone** in a third slot.
3. Leave the other ingredient slots empty. A stack of two enhancers in one slot does not satisfy two ingredient entries.
4. The existing Sharpness level must be below II, the enchantment must apply to the input item, and its other enchantments must pass mutual compatibility checks.
5. Take the modified equipment from the result slot. This path starts from a copy of the input stack and replaces/adds the selected enchantment level.

[Inspect the Sharpness II recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Fimbuing%2Fsharpness_ii). JEI presents an enchanted book as the recipe’s display symbol, but the table’s actual result is the compatible input equipment with the enchantment applied. It is not a recipe for generating that display book.

## Ingredient-slot rules that prevent failed recipes

- The base item must be present in slot 0. Transformation recipes compare its item identity and metadata; metadata 32767 is treated as a wildcard by the selected matcher.
- Slots 1–9 form the ingredient area. The matcher counts **occupied slots**, not the total number of items across stacks.
- The occupied count must exactly equal the number of recipe ingredient entries. Extra unrelated items block matching.
- Simple ingredients are matched through the recipe-item helper with one item credited per occupied slot; non-simple ingredients use Forge’s matcher.
- There must be 1–9 ingredient entries in the parsed recipe. The base item does not count toward those nine.
- The table verifies the player’s Infusion requirement before exposing an output, with Creative bypassing that skill gate. Limited-crafting recipe-book rules are also checked.

## What the released catalog contains

| Branch | Shipped definitions | Browse |
|---|---:|---|
| Item transformations | 251 | [All transformations](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=infusion%2Finfusing%2F) |
| Enchantment applications | 135 across 37 enchantment IDs | [All enchantments](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=infusion%2Fimbuing%2F) |

Transformation recipes divide into **126 armor**, **99 weapon**, **21 slab**, **4 block**, and **1 miscellaneous** definitions. Declared/default Infusion requirements across the complete catalog range from 1 to 97. A recipe definition does not establish that every ingredient, output or downstream ability is available in a particular modpack.

### Enchantment levels and Infusion requirements

Each entry below reads “enchantment level → required Infusion level.” Open the group to inspect the ingredient images and exact JSON for its recipes. This is the shipped table catalog, not a promise that every listed level is compatible with every item or configuration.

| Enchantment ID | Level → Infusion requirement | Recipes |
|---|---|---|
| `aoa3:archmage` | 1 → 70; 2 → 80; 3 → 89 | [View 3](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Aarchmage) |
| `aoa3:brace` | 1 → 61 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Abrace) |
| `aoa3:control` | 1 → 17; 2 → 34; 3 → 51; 4 → 72 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Acontrol) |
| `aoa3:crush` | 1 → 24; 2 → 37; 3 → 49; 4 → 61 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Acrush) |
| `aoa3:form` | 1 → 20; 2 → 31; 3 → 46; 4 → 63 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Aform) |
| `aoa3:intervention` | 1 → 97 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Aintervention) |
| `aoa3:recharge` | 1 → 9; 2 → 25; 3 → 38; 4 → 51; 5 → 63; 6 → 79 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Arecharge) |
| `aoa3:sever` | 1 → 12; 2 → 22; 3 → 32; 4 → 42; 5 → 52; 6 → 80 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Asever) |
| `aoa3:shell` | 1 → 20; 2 → 40; 3 → 70 | [View 3](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=aoa3%3Ashell) |
| `minecraft:aqua_affinity` | 1 → 39 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aaqua_affinity) |
| `minecraft:bane_of_arthropods` | 1 → 5; 2 → 11; 3 → 19; 4 → 27; 5 → 36; 6 → 45 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Abane_of_arthropods) |
| `minecraft:blast_protection` | 1 → 4; 2 → 9; 3 → 17; 4 → 26 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Ablast_protection) |
| `minecraft:depth_strider` | 1 → 19; 2 → 27; 3 → 37 | [View 3](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Adepth_strider) |
| `minecraft:efficiency` | 1 → 11; 2 → 23; 3 → 34; 4 → 47; 5 → 62; 6 → 87 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aefficiency) |
| `minecraft:feather_falling` | 1 → 6; 2 → 13; 3 → 21; 4 → 29 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Afeather_falling) |
| `minecraft:fire_aspect` | 1 → 1; 2 → 10 | [View 2](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Afire_aspect) |
| `minecraft:fire_protection` | 1 → 5; 2 → 10; 3 → 18; 4 → 26 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Afire_protection) |
| `minecraft:flame` | 1 → 22 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aflame) |
| `minecraft:fortune` | 1 → 15; 2 → 30; 3 → 45; 4 → 70; 5 → 85 | [View 5](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Afortune) |
| `minecraft:frost_walker` | 1 → 55; 2 → 65 | [View 2](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Afrost_walker) |
| `minecraft:infinity` | 1 → 62 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Ainfinity) |
| `minecraft:knockback` | 1 → 21; 2 → 39; 3 → 65; 4 → 78 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aknockback) |
| `minecraft:looting` | 1 → 18; 2 → 30; 3 → 45; 4 → 71 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Alooting) |
| `minecraft:luck_of_the_sea` | 1 → 13; 2 → 27; 3 → 40; 4 → 76 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aluck_of_the_sea) |
| `minecraft:lure` | 1 → 4; 2 → 18; 3 → 39; 4 → 62; 5 → 78 | [View 5](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Alure) |
| `minecraft:mending` | 1 → 97 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Amending) |
| `minecraft:power` | 1 → 1; 2 → 15; 3 → 25; 4 → 35; 5 → 45; 6 → 75 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Apower) |
| `minecraft:projectile_protection` | 1 → 8; 2 → 22; 3 → 30; 4 → 34 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aprojectile_protection) |
| `minecraft:protection` | 1 → 1; 2 → 19; 3 → 33; 4 → 47 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aprotection) |
| `minecraft:punch` | 1 → 19; 2 → 37; 3 → 63; 4 → 76 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Apunch) |
| `minecraft:respiration` | 1 → 15; 2 → 23; 3 → 37; 4 → 59 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Arespiration) |
| `minecraft:sharpness` | 1 → 1; 2 → 10; 3 → 20; 4 → 30; 5 → 40; 6 → 70 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Asharpness) |
| `minecraft:silk_touch` | 1 → 44 | [View 1](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Asilk_touch) |
| `minecraft:smite` | 1 → 7; 2 → 15; 3 → 21; 4 → 30; 5 → 37; 6 → 46 | [View 6](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Asmite) |
| `minecraft:sweeping` | 1 → 21; 2 → 31; 3 → 44; 4 → 68 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Asweeping) |
| `minecraft:thorns` | 1 → 36; 2 → 50; 3 → 65 | [View 3](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Athorns) |
| `minecraft:unbreaking` | 1 → 16; 2 → 32; 3 → 48; 4 → 83 | [View 4](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion&q=minecraft%3Aunbreaking) |

## Above-cap enchanting still has rules

The selected released configuration declares **allowUnsafeInfusion = true by default**. That is a default declaration, not a reading of your installed configuration. When disabled, the parser rejects an above-maximum enchantment level, and result generation checks the cap again.

Enabling this option does **not** bypass every compatibility check. The selected result method still calls the enchantment’s item-applicability check and checks compatibility in both directions against each other enchantment already on the item. Matching also rejects an input that already has the chosen enchantment at an equal or greater level.

The recipe chooses a specific target level. It does not combine levels using an anvil-style addition rule. For example, the Sharpness II recipe writes level II when the eligible input is below II; it does not add two levels to an existing value.

## Does table crafting train Infusion?

**None of these 386 stock recipe JSON files declares infusion_xp.** The selected parser initializes minimum and maximum recipe XP to zero, and the result-slot callback only requests crafting XP when the recipe maximum is positive. Thus the inspected stock recipe path does not itself grant Infusion recipe XP.

This is separate from [Pixon harvesting and direct stone conversion](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2), which have their own checked XP paths. Other mod hooks or custom recipe additions may add behavior; do not use repeated stock table crafting as a guaranteed training method based only on the skill’s name.

For custom recipes using a min/max XP object, the inspected callback uses minimum plus a random integer below maximum−minimum when the two differ. The upper bound is exclusive in that branch. The parser first requests an object for infusion_xp, so a bare numeric field needs dedicated validation rather than assuming its later primitive check accepts it. No shipped recipe exercises that field.

## Troubleshooting

| Problem | Check |
|---|---|
| No output, ingredients appear correct | Base slot, exact occupied count, repeated ingredients split across slots, item metadata and skill level |
| The table consumes a held stone stack | You invoked the conversion interaction; use an empty hand to open crafting |
| Enchantment output missing | Input applicability, equal-or-higher existing level, mutual conflicts, configuration cap and skill gate |
| JEI shows a book but I get equipment | The book is a presentation symbol; the recipe mutates a copy of the compatible input |
| Custom name or other NBT disappears during transformation | Transformation returns a fresh declared output copy; it is distinct from enchanting the input copy |
| No Infusion XP after crafting | All 386 stock definitions omit the recipe-XP field |
| Interface closes or cannot be used | The block must still be the Infusion Table; the selected distance-squared limit is 64 from its center |

The selected container clears/returns its crafting inventory through the server-side close helper. Shift-click, full inventories, custom container-item remainders and disconnect boundaries still require game tests; this guide does not certify them through static inspection.

## Restoration acceptance checklist

- [ ] Exercise a simple transformation with the correct base, wrong base and wrong metadata.
- [ ] Test each ingredient count boundary, two identical ingredients in one stack versus two slots, and an extra occupied slot.
- [ ] Test the skill gate just below/at the recipe requirement, Creative and limited-crafting recipe-book rules.
- [ ] Test enchantment applicability, equal/higher existing levels, both directions of incompatibility and unsafe-level settings.
- [ ] Check name, damage, NBT and enchantments for transformation versus enchantment results.
- [ ] Test ordinary click, shift-click, stack counts, inventory-full results, container-item remainders, close and disconnect.
- [ ] Validate custom XP object parsing and exclusive upper bounds before enabling custom recipe XP.
- [ ] Verify all restored recipe groups in game and profile recipe lookup/startup cost without changing behavior.

## Evidence

[Full recipe and method evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/infusion-crafting-evidence-1.12.2.json) · [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/infusion-crafting-art-evidence-1.12.2.json) · [All illustrated recipe cards](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=aoa3%3Ainfusion)

The audit covers 21 released methods, all 386 recipe resources, 37 enchantment groups and independent occupied-slot examples. The annotated diagram uses the released GUI texture and actual container slot coordinates; it is not a gameplay screenshot. No game code was executed.

[Pinned official source](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source) is readable context; selected released bytes/resources determine this guide. AoA: Tslat and contributors. Vanilla assets: Mojang.

[Modern 1.21.1 Infusion Table](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1) · [Modern Imbuing Chamber](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Imbuing-Chamber-Enchanting-1.21.1) · [Historical skill guides](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
