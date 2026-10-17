# Furnace recipes and material recycling · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** The inspected RecipeRegister method adds **56 furnace conversions in Java**: 29 ores, four bone fragments, sixteen fish, five meats and two recycling steps. They are now included in the illustrated recipe browser alongside the previous 1,172 definitions.

[Browse all 56 furnace conversions](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&type=minecraft%3Asmelting). Every card has ingredient and result pictures, an exact link, the registered experience value and its source reference.

## How to use these recipes

1. Place the listed input in a furnace and provide suitable fuel. These declarations pass one output ItemStack, so the documented conversion is one input to one output.
2. Wait for the active furnace implementation to complete the operation and collect the result. The AoA registration supplies input, result and XP; it does not locally override fuel or cook time.
3. Check the exact input name. A crystal ore block, a loose crystal item and a gemstone are different objects. The six newly resolved ore icons use the checked ore-block models.
4. Treat XP values as registration inputs. They do not certify how a custom furnace, hopper extraction or a modified runtime awards experience.

The recipe links use documentation-assigned IDs beginning aoa3:documented_smelting/. These identify code registrations for browsing; they are **not original in-game recipe IDs**. Do not paste them into a recipe command or a script expecting native registered recipe names.

## Useful distinctions

- **Skeletal Ingot:** Chestbone, Footbone, Legbone and Skullbone Fragments each independently smelt into one ingot. This is not a four-fragment combined recipe.
- **Recycling:** Rusted Iron Ingot → Scrap Metal → Iron Nugget. Both arrows are separate furnace operations, and the last result is a nugget, not a full ingot. Each step registers XP 1.
- **Crystals:** Blue, Green, Purple, Red, White and Yellow Crystal Ores produce their matching Gemstones. The ore’s picture is not a loose crystal-item picture.
- **Food:** The sixteen cooked fish have a separate [hunger-scaled healing callback](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cooking-Fish-and-Hunger-Scaled-Healing-1.12.2). Do not infer the same effect for every cooked meat.
- **Mining:** A smelting recipe does not describe the block’s natural mining drop, required tool, world generation or Fortune behavior. Those are separate questions.

## Illustrated conversion reference

Each image contains the exact named input/output pairs in that group. Open a recipe link beneath it for a larger per-item preview and searchable ingredients. No game screenshots or furnace timing are fabricated.

### Ores · sheet 1

![Named furnace input and output pairs: Ores](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-ores-1.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Amethyst Ore | Amethyst ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Famethyst_ore) |
| Baronyte Ore | Baronyte Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fbaronyte_ore) |
| Blazium Ore | Blazium Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fblazium_ore) |
| Bloodstone Ore | Bloodstone ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fbloodstone_ore) |
| Charged Runium Ore | Charged Runium Chunk ×1 | 2 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fcharged_runium_ore) |
| Crystallite Ore | Crystallite ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fcrystallite_ore) |
| Elecanium Ore | Elecanium Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Felecanium_ore) |
| Emberstone Ore | Emberstone Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Femberstone_ore) |

### Ores · sheet 2

![Named furnace input and output pairs: Ores](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-ores-2.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Gemenyte Ore | Gemenyte ×1 | 2 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fgemenyte_ore) |
| Ghastly Ore | Ghastly Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fghastly_ore) |
| Ghoulish Ore | Ghoulish Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fghoulish_ore) |
| Jade Ore | Jade ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fjade_ore) |
| Jewelyte Ore | Jewelyte ×1 | 2 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fjewelyte_ore) |
| Limonite Ore | Limonite Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Flimonite_ore) |
| Lyon Ore | Lyon Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Flyon_ore) |
| Mystite Ore | Mystite Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fmystite_ore) |

### Ores · sheet 3

![Named furnace input and output pairs: Ores](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-ores-3.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Ornamyte Ore | Ornamyte ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fornamyte_ore) |
| Rosite Ore | Rosite Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Frosite_ore) |
| Runium Ore | Runium Chunk ×1 | 2 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Frunium_ore) |
| Sapphire Ore | Sapphire ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fsapphire_ore) |
| Blue Gemstone Ore | Blue Gemstones ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fblue_crystal_ore) |
| Green Gemstone Ore | Green Gemstones ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fgreen_crystal_ore) |
| Purple Gemstone Ore | Purple Gemstones ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fpurple_crystal_ore) |
| Red Gemstone Ore | Red Gemstones ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fred_crystal_ore) |

### Ores · sheet 4

![Named furnace input and output pairs: Ores](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-ores-4.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| White Gemstone Ore | White Gemstones ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fwhite_crystal_ore) |
| Yellow Gemstone Ore | Yellow Gemstones ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fyellow_crystal_ore) |
| Shyregem Ore | Shyregem ×1 | 5 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fshyregem_ore) |
| Shyrestone Ore | Shyrestone Ingot ×1 | 2 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fshyrestone_ore) |
| Varsium Ore | Varsium Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fvarsium_ore) |

### Bone fragments · sheet 1

![Named furnace input and output pairs: Bone fragments](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-bone-fragments-1.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Chestbone Fragment | Skeletal Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fchestbone_fragment) |
| Footbone Fragment | Skeletal Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Ffootbone_fragment) |
| Legbone Fragment | Skeletal Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Flegbone_fragment) |
| Skullbone Fragment | Skeletal Ingot ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fskullbone_fragment) |

### Fish · sheet 1

![Named furnace input and output pairs: Fish](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-fish-1.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Raw Candlefish | Candlefish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_candlefish) |
| Raw Crimson Skipper | Crimson Skipper ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_crimson_skipper) |
| Raw Crimson Stripefish | Crimson Stripefish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_crimson_stripefish) |
| Raw Dark Hatchetfish | Dark Hatchetfish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_dark_hatchetfish) |
| Raw Fingerfish | Fingerfish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_fingerfish) |
| Raw Golden Gullfish | Golden Gullfish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_golden_gullfish) |
| Raw Ironback | Ironback ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_ironback) |
| Raw Limefish | Limefish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_limefish) |

### Fish · sheet 2

![Named furnace input and output pairs: Fish](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-fish-2.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Raw Pearl Stripefish | Pearl Stripefish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_pearl_stripefish) |
| Raw Rainbowfish | Rainbowfish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_rainbowfish) |
| Raw Razorfish | Razorfish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_razorfish) |
| Raw Rocketfish | Rocketfish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_rocketfish) |
| Raw Sailback | Sailback ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_sailback) |
| Raw Sapphire Strider | Sapphire Strider ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_sapphire_strider) |
| Raw Turquoise Stripefish | Turquoise Stripefish ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_turquoise_stripefish) |
| Raw Violet Skipper | Violet Skipper ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_violet_skipper) |

### Meat · sheet 1

![Named furnace input and output pairs: Meat](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-meat-1.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Raw Charger Shank | Charger Shank ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_charger_shank) |
| Raw Chimera Chop | Chimera Chop ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_chimera_chop) |
| Raw Furlion Chop | Furlion Chop ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_furlion_chop) |
| Raw Halycon Beef | Halycon Beef ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_halycon_beef) |
| Raw Ursa Meat | Ursa Meat ×1 | 3 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fraw_ursa_meat) |

### Recycling · sheet 1

![Named furnace input and output pairs: Recycling](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/furnace-conversions-1.12.2-recycling-1.webp)

| Input | Result | Registered XP | Exact recipe |
|---|---|---:|---|
| Rusted Iron Ingot | Scrap Metal ×1 | 1 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Frusted_iron_ingot) |
| Scrap Metal | Iron Nugget ×1 | 1 | [Open](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Adocumented_smelting%2Fscrap_metal) |

## Coverage and preservation

All 56 calls in the inspected registerRecipes method were checked against pinned source expressions and released bytecode. Input/output identities retain their source field names; 107 non-vanilla identity references also have matching registry-name literals in the relevant declaration or constructor. The vanilla Iron Nugget field is matched through the pinned source expression and released call window.

The previous 1,172 recipe records and 2,553 icon records are preserved. Six crystal-ore icons were added from checked inventory declarations. The historical release now contains **1,228 indexed definitions**, and the four-release browser contains **6,837 definitions**. This remains an archive/source index, not a claim that every runtime-modified recipe in a particular pack is represented.

## Evidence

- [All 56 registration windows and source cross-checks](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/furnace-registration-evidence-1.12.2.json).
- [Preservation and added-icon proof](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/furnace-recipe-integration-proof-1.12.2.json).
- [Diagram provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/furnace-art-evidence-1.12.2.json).
- [Food planner](https://herbertofury.github.io/Advent-of-Ascension/fish-food-planner.html), [registered item/block distinctions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Registered-Blocks-and-Items-1.12.2), [historical fishing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2).
- Original AoA assets and mechanics by Tslat and contributors; vanilla assets by Mojang. Original documentation compositions, with no game or mod execution.
