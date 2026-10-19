# Crafting and recipes

[1.20.1 Infusion Table walkthrough: station recipe, separate ingredient slots and Ginger Blaster](Infusion-Table-Crafting-1.20.1)

[Make frames before Infusion: Frame Bench workflow and eight armor-set shopping lists](Frame-Bench-and-Armor-Infusion-1.21.1)

**See the ingredients, keep the version straight.** Recipes are extracted from official AoA release artifacts and paired with rendered item/block previews. This reference preserves conditional integration recipes and custom serializer fields instead of pretending every recipe is a crafting-table grid.

## Explore recipes

[Open the illustrated Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html).

- Select the exact Minecraft generation first.
- Search by item name, ingredient ID, tag or recipe ID.
- Use **Link to this exact recipe** on a card to share that one definition and release. General text search remains a broader substring search; for example Sharpness II and III can share a prefix.
- Edit the search, click an ingredient or use Reset to leave an exact-recipe selection. An unavailable recipe stays empty in another release instead of silently substituting a different one.
- Filter by crafting, stonecutting, cooking, infusion, imbuing, upgrade kits and other recipe types.
- Click an ingredient to find definitions mentioning it.
- Expand source details for the exact artifact path, SHA-256, conditions and serializer-specific fields.
- Expand ingredient tags to inspect known alternatives. External loader/modpack tag membership can be unresolved; it is labelled rather than guessed.

| Minecraft | Official AoA release | Recipe-definition records |
|---|---|---:|
| 1.21.1 | 3.7.16.1 | 1,532 |
| 1.20.1 | 3.7.1 | 1,781 |
| 1.16.5 | 3.6.11 | 2,296 |
| 1.12.2 | 3.3.6 | 1,228 |

**6,837 definition records** does not mean 6,837 distinct crafted items. Alternate recipes, optional-mod recipes and runtime-defined serializers are included. The legacy `_factories` metadata file is excluded from the recipe count.

## From a weapon recipe to using it

In the [Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2), historical weapon recipe cards now include a **How to: Use historical … weapons** link. Crafting is only the first step: the linked guides explain the relevant ammunition, rune costs, firing or draw timing, revenge targets, melee inputs and special exceptions.

- **256 recipe cards cover 255 weapon outputs across all 13 historical weapon families.** Alternate Grenade recipes remain separate cards.
- Infusion and upgrade recipes keep their existing workstation instructions alongside the weapon usage link.
- These usage links apply to **1.12.2 / AoA 3.3.6**. Selecting another release never substitutes a historical weapon guide for that release's behavior.
- A missing recipe does **not** mean a weapon is unobtainable. Drops, trades and other acquisition paths are separate evidence; the [weapon reference library](Weapon-Reference-Library) also includes weapons without a matching recipe definition.

All previous recipe-guide links are retained. The browser uses a compact inline lookup, with no additional network request or inventory scan for these links.

[Weapons without a recipe: checked historical trader purchases and upgrades](Buying-Weapons-and-Trader-Upgrades-1.12.2) cover 29 offers, including 18 weapon IDs absent from the recipe-output and creature-loot indexes.

## Illustrated walkthroughs

- [Historical Infusion crafting and enchanting · 1.12.2](Infusion-Table-Crafting-and-Enchanting-1.12.2): 386 definitions, separate base slot, 37 enchantment families and checked XP defaults.

- [Imbuing Chamber enchanting · 1.21.1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Imbuing-Chamber-Enchanting-1.21.1): Power Stones, focus combinations, skill requirements, durability and immediate target insertion.

- [Infusion Table crafting · 1.21.1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1): station recipe, separate base slot, repeated ingredients and result preservation.
- [Staff batteries and charging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Batteries-and-Charging): the dynamic charging workflow.
- [Historical first portal · 1.16.5](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-Walkthrough-1.16.5): shapeless rune preparation and exact frame materials.
- [First portal and Precasia · 1.12.2](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2): historical IDs and six distinct sapling ingredients.

[Your first portal](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-Walkthrough) follows material gathering, rune crafting, exact frame layout, activation and troubleshooting for 1.21.1 / 3.7.16.1.

![Power rune crafting reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/power-rune-recipe-1.21.1.webp)

## Important differences between recipe systems

### Shaped crafting

The grid shows the declared pattern. Blank cells remain blank. The output count is shown on the result. Where a recipe supports normal crafting-grid offsets, the diagram uses its top-left presentation; it is not a new positioning restriction.

### Shapeless crafting

Ingredient order is not significant. Repeated ingredients still matter. An ingredient's alternatives are not a list of additional required items.

### Cooking and stonecutting

These use their declared recipe type rather than a fabricated 3×3 layout. Cooking ticks and experience are retained from the definition. They are data values; this documentation does not promise a measured real-time duration under server lag or modpack changes.

### Infusion and upgrade kits

Infusion can include a base item in addition to the ingredient list. Upgrade recipes specify input and kit separately. Consult the exact fields before treating them as interchangeable stations or assuming item consumption behavior.

### Imbuing

The result may be an enchantment rather than a fixed item stack. Aspect foci, power source, required Imbuing level and enchantment level remain visible in the source fields. Do not read a blank item output as a broken recipe.

### Dynamic recipes

Some serializers compute their inputs or outputs at runtime, such as staff charging. The explorer labels these as dynamic; a data-only reader cannot establish every accepted inventory combination. Completing bespoke interactive demonstrations for those serializers remains follow-up work.

## Modpack and legacy cautions

- Datapacks and mods can override the bundled recipes and ingredient tags. Your installed pack's final loaded data is authoritative.
- Conditional integration recipes only activate when their conditions are met. An entry in this reference is not proof that an optional mod is installed.
- Legacy item metadata matters. Unknown nonzero metadata does not receive a misleading generic icon.
- Some built-in/entity-rendered vanilla ingredients still have text fallbacks. An unknown picture does not mean the ingredient is absent.
- Model images show source assets. They do not certify in-game renderer parity, target-platform compatibility or an Enderloom conversion.

## Provenance and performance

The browser loads one version's compact data shard at a time and initially renders 60 matching cards, adding more on request. Item icons reuse the atlas sheets instead of issuing a separate image request per recipe. No background rescan of your mods or game files is needed.

The source artifacts and checksums are documented in [Sources and credits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sources-and-Credits) and the repository's artifact evidence. Models/textures are by **Tslat and contributors**. The explorer, diagrams and explanatory text are independently produced documentation.

## Legacy metadata-aware ingredient previews

The 1.12.2 recipe explorer distinguishes 28 explicit vanilla item variants: sixteen dyes, six saplings, three wool colors, charcoal, coarse dirt and dandelion. Each uses its matching official item model and texture rather than showing the default variant for every metadata value. Wildcard metadata is labeled **Any variant**, and unsupported variants keep a readable fallback. The full 6,837-card construction suite and targeted dye/name/wildcard checks passed after this update. These are UI/data tests, not a replacement for in-game crafting validation.


## Repair equipment

[Illustrated Mending Table walkthrough](Mending-Table-and-Repair-Materials-1.21.1): station recipe, Repair Dust versus Compound, timed Solution conversion and the released stale-preview precaution.

## Modern rune inputs and station limits

[Illustrated 1.21.1 rune-production guide](Rune-Production-and-Current-Limits-1.21.1): two stonecutting recipes, fourteen rune references, whole-stack post behavior and Randomizer equipment-condition pitfalls. Station survival acquisition remains unverified; do not substitute the historical Runation route.

## Cooking with Ashfern

[Illustrated Ashfern cooking guide for 1.21.1](Ashfern-Cooking-and-Food-Preparation-1.21.1): two occupied input slots, 25 checked AoA food routes, six outputs and the difference between an edible input and an edible result. Includes twenty named fish previews and recipe-matching troubleshooting.

## Tea Sink brewing

[Tea Sink recipes and ingredient-priority guide for 1.21.1](Tea-Sink-Brewing-and-Ingredient-Priority-1.21.1): craft the sink and Cups, harvest Tea Shreddings, manage automatic additive selection and avoid the released melon-return branch. Creative selection is checked separately.

## Infused Press storage and piston control

[Infused Press operating reference for 1.21.1](Infused-Press-Compression-and-Piston-Control-1.21.1): nine-stack matching, downward piston layout, one-tier decompression, comparator limitations and high-tier serialization checks. Station acquisition and actual piston timing remain separately unverified.

## Divine Station weapon upgrades

[All 70 illustrated 1.20.1 upgrade routes](Divine-Station-Weapon-Upgrades-1.20.1), covering 18 named kits plus Weapon Parts. This separate catalog uses released AoA3.7.1 data and checks the output-template/NBT transfer limitation. Every matching 1.20.1 recipe-browser card now links to this version-specific guide.

[All 36 illustrated 1.21.1 upgrade routes](Divine-Station-Weapon-Upgrades-1.21.1), covering 17 named kits plus Weapon Parts. Check positional inputs and the configured-output component policy before upgrading customized weapons. Active acquisition remains pack-specific.

## Original trophies and gold crafting

[Gold Trophy recipe and elite progression guide for 1.21.1](Trophies-Gold-Crafting-and-Elite-Encounters-1.21.1): nine original normal trophies of one valid entity ID, first-record preservation and the distinction between collected originals and spawn-egg decorations.

## Historical furnace conversions

[All 56 Java-registered furnace recipes](Furnace-Recipes-and-Material-Recycling-1.12.2) now have input/output pictures and exact browser links: 29 ores, four bone fragments, sixteen fish, five meats and two recycling steps. Their documentation-assigned link IDs are clearly labeled and are not original in-game recipe IDs. The previous 1,172 definitions are preserved.


## Historical tea and Ore Dictionary ingredients

[Tea Sink brewing and drink effects](Tea-Sink-Brewing-Priority-and-Drink-Effects-1.12.2) covers the two equipment recipes, three tea branches and survival/creative differences. The 34 Ore Dictionary ingredient occurrences in the historical recipe data now display their actual symbolic names, including plankWood, instead of an unnamed item. Membership is supplied by the active Forge environment and is not invented by this index.

