# Infusion Table crafting · 1.21.1

[Make frames before Infusion: Frame Bench workflow and eight armor-set shopping lists](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

**Minecraft 1.21.1 / AoA 3.7.16.1.** Build the station, put the base in the correct slot, and match repeated ingredients without confusing stack size with occupied slots. The inspected release supplies **62 `aoa3:infusion` recipe definitions**. This count describes bundled recipes, not proof that every material is obtainable in an unfinished dimension.

[Recipe Observatory: this release](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1) · [Crafting overview](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes) · [Tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.21.1)

## 1. Craft the station

![Infusion Table recipe with four amethyst-tag ingredients, Ancient Rock, Enchanting Table and Crafting Table](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infusion-table-recipe-1.21.1.webp)

At an ordinary crafting table, use:

| Amethyst-gem tag item | Ancient Rock | Amethyst-gem tag item |
|---|---|---|
| Empty | Enchanting Table | Empty |
| Amethyst-gem tag item | Crafting Table | Amethyst-gem tag item |

The total is **four items matching `c:gems/amethyst`, one Ancient Rock, one Enchanting Table and one Crafting Table**, producing one Infusion Table. The pictured amethyst shard represents the tag; the final loaded tag in your pack determines accepted items.

This is the modern recipe. Do not substitute the historical wool/infusion-stone recipe merely because the workstation has the same name.

## 2. Understand the ten input slots

The checked menu has:

- **One separate base slot on the left**, index 0
- **Nine ingredient slots** in the middle grid
- **One result slot on the right**

The recipe's `base` belongs in the left slot. Its `ingredients` belong in the nine-slot grid. The grid ingredients are matched without a shaped pattern, but their number and multiplicity still matter.

There is no furnace-style fuel slot in this menu. In the checked crafting path, matching inputs produces an available result; taking that result performs the craft. This is not a timed smelting recipe.

## 3. Try the Bolt Rifle layout

![Sniper Frame in the base slot and seven separately occupied ingredient slots produce the Bolt Rifle](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infusion-slot-layout-1.21.1.webp)

The [released Bolt Rifle recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=bolt_rifle) needs:

| Position | Requirement |
|---|---|
| Separate base slot | One Sniper Frame |
| Ingredient slots 1–3 | Three iron-ingot tag entries, in **three separate slots** |
| Another ingredient slot | One diamond-gem tag entry |
| Another ingredient slot | One gunpowder tag entry |
| Two other ingredient slots | Two plank-tag entries, in **two separate slots** |
| Remaining two ingredient slots | Empty |

Their order within the middle grid can vary. The illustration is an easy layout to copy, not a new shaped-recipe requirement. Iron ingot, diamond, gunpowder and oak-plank pictures are representative tag examples.

### Why a stack of three iron does not replace three slots

For ordinary ingredients, the released matcher accounts for **one item per occupied ingredient slot**. A stack of three iron in one slot contributes one matching slot, not the three separate recipe entries. Split it across three slots first. The same rule applies to the two plank entries.

You can keep more than one item in a required slot for later crafts, but that does not fill a different required slot. Extra unrelated occupied slots also stop an exact recipe match. Start with one of each required entry while troubleshooting.

## 4. Take the result and check the remainders

The checked result-slot handler removes **one item from each occupied input slot**, including the base, and then handles crafting remainders. The base is therefore not a permanently installed mold in this generic recipe path.

If a recipe uses a container item, its crafting remainder can return to the slot, combine where compatible, go to your inventory, or drop if inventory insertion fails. Do not leave valuable remainders unattended, and test automation separately rather than assuming it behaves exactly like a normal player craft.

The Blast Chiller recipe is a useful example: its ingredients include a Water Bucket. The infusion recipe requests the standard crafting remainder instead of declaring every input disposable with no return. Exact custom container behavior can be changed by other mods.

## 5. Do not assume base-item data is inherited

The generic infusion recipe produces **a copy of the recipe-defined output**. Its assembly method does not copy arbitrary data from the input base into that result.

A custom name, enchantment, durability value or other component on a specially modified base therefore should not be assumed to carry through. The bundled recipes mostly use construction frames; this warning matters particularly for datapacks or extensions that let you use customized bases. Inspect the actual result before committing an irreplaceable item.

A different upgrade serializer can have different preservation rules. Check its own recipe type and implementation rather than applying this generic infusion behavior to every workstation.

## What the 62 bundled recipes use as their base

| Base family | Recipe definitions |
|---|---:|
| Gun Frame | 12 |
| Boots Frame | 8 |
| Chestplate Frame | 8 |
| Helmet Frame | 8 |
| Leggings Frame | 8 |
| Blaster Frame | 5 |
| Sniper Frame | 5 |
| Shotgun Frame | 4 |
| Cannon Frame | 3 |
| Metal-rod tag | 1 |

All inspected ingredient lists contain between one and nine entries. The table is a resource inventory, not an acquisition guide for every frame or material. Use the selected-release recipe search and item references to follow the preparation chain.

## Troubleshooting an empty result

1. **Check the station and recipe type.** A normal crafting-table recipe, infusion recipe and imbuing recipe are not automatically interchangeable.
2. **Check the separate base slot.** Putting the base in the middle grid does not satisfy slot 0.
3. **Split repeated ingredients.** Three repeated entries require three occupied slots, even if one stack contains enough total items.
4. **Remove extras.** Keep unused grid slots empty.
5. **Check tags, components and pack overrides.** A similar name or texture does not guarantee an ingredient match.
6. **Check the release.** Use 1.21.1 / 3.7.16.1 instructions with that build, not a historical recipe card.
7. **Try a single craft first.** Confirm output and remainder behavior before shift-click batches or automation.

## Evidence and limits

[Infusion workstation evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/infusion-workstation-evidence-1.21.1.json) contains the 62 released recipe resources, station recipe, selected menu/recipe/result-slot method evidence and source hashes. Exact narrow assertions check ten inputs, one-item ingredient accounting, output copying and one-item removal. Source interpretation uses [7919b5fe48599e6105c5740937ce36c36ef21d16](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16).

The diagrams are original explanatory layouts using release-matched model resources. They are not game screenshots; the Enchanting Table picture excludes its animated book. AoA artwork is by Tslat and contributors, vanilla artwork by Mojang/Microsoft. This is documentation and static code evidence, not an executed crafting test or proof of the private Enderloom build.
