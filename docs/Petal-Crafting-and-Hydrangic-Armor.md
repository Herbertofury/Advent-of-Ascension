# Petal Crafting and Hydrangic Armor

Combine five petal colors, then use the station for a random Hydrangic armor piece. **Choose your release first:** the interaction survives in newer archives even where the old acquisition resources do not. This page separates a documented historical route from retained modern code.

![Historical five-color Petals recipe and random armor station workflow](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-workflow-1.16.5.webp)

## Release check

| Inspected release | Five-color Petals recipe | Petal entity-loot references | Garden Castle evidence |
|---|---|---|---|
| Minecraft 1.16.5 / AoA 3.6.11 | Present | Six tables | Configured structure, Floral Islands start list, Gardencia placement settings and castle template |
| Minecraft 1.20.1 / AoA 3.7.1 | Present | Five tables | Castle template retained; no linking Garden Castle worldgen JSON found in this scan |
| Minecraft 1.21.1 / AoA 3.7.16.1 | Not found in inspected recipe resources | None found in inspected loot resources | Castle template and station interaction retained; no linking worldgen JSON found |

In 1.21.1 the five small petals and combined Petals are also explicitly listed in `c:hidden_from_recipe_viewers`. This does not mean the item or station class was deleted. It does mean the old recipe-and-drop walkthrough should not be silently presented as a verified modern survival route. Datapacks, restoration work and the private current candidate can differ.

## 1. Reach Gardencia in the historical route

Follow the [1.16.5 Gardencia Realmstone route](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#gardencia). Bring your combat supplies, food, an exit plan and free inventory slots. The historical Floral Islands biome includes Garden Castle in its structure-start list. Gardencia’s generator specifies spacing 32 and separation 12 for that structure; these are structure-placement parameters, not “one castle every 32 blocks.”

The retained castle template measures **27 × 23 × 21** and contains the Petal Crafting Station at template-local **(13, 12, 13)**. This describes where the station sits inside that template, not a universal world coordinate. The matching historical template pool explicitly selects that castle asset.

## 2. Collect all five colors

You need one **Small Blue Petal**, **Small Green Petal**, **Small Orange Petal**, **Small Purple Petal** and **Small Red Petal** for each combined Petals item. The historical creature-table references below provide a planning starting point.

| Historical 1.16.5 creature | Petal entries in its relevant pool | Pool rolls |
|---|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ArchvineModel-thumb.webp" width="90" height="90" alt="Archvine historical 1.16.5 model"> [Archvine](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:archvine) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_red_petal.webp" width="44" height="44" alt="Small Red Petal"> Small Red Petal · 10/120 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_green_petal.webp" width="44" height="44" alt="Small Green Petal"> Small Green Petal · 10/120 weight | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CarrotopModel-thumb.webp" width="90" height="90" alt="Carrotop historical 1.16.5 model"> [Carrotop](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:carrotop) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_orange_petal.webp" width="44" height="44" alt="Small Orange Petal"> Small Orange Petal · 20/120 weight | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-FlowerfaceModel-thumb.webp" width="90" height="90" alt="Flowerface historical 1.16.5 model"> [Flowerface](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:flowerface) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_purple_petal.webp" width="44" height="44" alt="Small Purple Petal"> Small Purple Petal · 10/120 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_blue_petal.webp" width="44" height="44" alt="Small Blue Petal"> Small Blue Petal · 10/120 weight | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-PodPlantModel-thumb.webp" width="90" height="90" alt="Pod Plant historical 1.16.5 model"> [Pod Plant](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:pod_plant) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_red_petal.webp" width="44" height="44" alt="Small Red Petal"> Small Red Petal · 10/210 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_green_petal.webp" width="44" height="44" alt="Small Green Petal"> Small Green Petal · 10/210 weight | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-SunnyModel-thumb.webp" width="90" height="90" alt="Sunny historical 1.16.5 model"> [Sunny](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:sunny) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_green_petal.webp" width="44" height="44" alt="Small Green Petal"> Small Green Petal · 20/120 weight | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-VinocorneModel-thumb.webp" width="90" height="90" alt="Vinocorne historical 1.16.5 model"> [Vinocorne](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3:vinocorne) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_purple_petal.webp" width="44" height="44" alt="Small Purple Petal"> Small Purple Petal · 34/430 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_red_petal.webp" width="44" height="44" alt="Small Red Petal"> Small Red Petal · 34/430 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_blue_petal.webp" width="44" height="44" alt="Small Blue Petal"> Small Blue Petal · 34/430 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_green_petal.webp" width="44" height="44" alt="Small Green Petal"> Small Green Petal · 34/430 weight<br><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-small_orange_petal.webp" width="44" height="44" alt="Small Orange Petal"> Small Orange Petal · 34/430 weight | 1–2; bonus-roll input 1.0 |

Weights are **per eligible pool selection**, not a promise per kill. Empty entries and other items remain in the denominators. Other pools, luck, global modifiers and runtime eligibility are not flattened into a single guaranteed drop rate. Vinocorne is a boss-table reference, not a normal-spawn shortcut. Follow each exact-version bestiary/drop entry for the wider context.

For 1.20.1, Archvine, Carrotop, Flowerface, Pod Plant and Sunny still have petal loot-table references; no Vinocorne petal-table reference was found there. Retained tables alone do not establish that those modern creatures/worlds are fully implemented.

## 3. Craft one combined Petals item

Put the **five distinct small petals** together in any arrangement in a crafting grid. The 1.16.5 and 1.20.1 shapeless recipes each define one combined Petals output; they do not substitute five of a single color.

- [Exact 1.16.5 recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3%3Ashapeless_craft_petals)
- [Exact retained 1.20.1 recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=aoa3%3Ashapeless_craft_petals)

## 4. Use the station, then check what you received

Use the combined **Petals** item on the **Petal Crafting Station**. The inspected non-creative payment path consumes **one Petals item**, then selects one of four Hydrangic pieces. It is an interaction with the block, not a four-choice armor-selection GUI.

| Possible historical output | Exact 1.16.5 item |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-hydrangic_boots.webp" width="44" height="44" alt="Hydrangic Boots"> Hydrangic Boots | [Open item](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:hydrangic_boots) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-hydrangic_legs.webp" width="44" height="44" alt="Hydrangic Legs"> Hydrangic Legs | [Open item](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:hydrangic_legs) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-hydrangic_chestplate.webp" width="44" height="44" alt="Hydrangic Chestplate"> Hydrangic Chestplate | [Open item](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:hydrangic_chestplate) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/petal-crafting-icon-1.16.5-hydrangic_helmet.webp" width="44" height="44" alt="Hydrangic Helmet"> Hydrangic Helmet | [Open item](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:hydrangic_helmet) |

**Duplicates are possible. Four uses do not guarantee the four different pieces.** The 1.16.5 and 1.20.1 methods use a four-way random switch; the 1.21.1 method passes four items to a selection helper. No deterministic order or guaranteed completion count is promised.

Leave space to collect the result. The modern inventory helper first tries inventory insertion, then uses a dropped-item fallback targeted to the player. Its boolean return is not a simple “the item vanished” signal. Full-inventory delivery, cancellation by other mods and reconnect still need testing in the actual target build.

### Watch the old leggings ID

The historical 1.16.5 inventory ID is **`aoa3:hydrangic_legs`**. The inspected 1.20.1 and 1.21.1 IDs use **`aoa3:hydrangic_leggings`**. Documentation links preserve that difference. Porting a save needs an explicit migration/alias decision; do not blindly rename registry entries or claim that migration already works.

## 5. Understand the modern farming effect

The modern Hydrangic effect is handled outside the armor class: it checks a ServerPlayer wearing the full set, a placed CropBlock and a successful bonemeal application. It then requests growth effects and armor damage. [Read the source-reviewed Hydrangic entry](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1#hydrangic). This modern behavior description is not a claim that the older release has identical hooks or that planting always matures a crop instantly.

## Restoration and test checklist

- Establish the target release’s actual Gardencia access, castle generation and petal sources before advertising a complete survival route.
- Restore or intentionally redesign missing acquisition resources; do not expose hidden ingredients without deciding progression.
- Verify one-unit consumption, creative behavior, all four random outcomes, duplicates and full-inventory delivery.
- Preserve historical item identities through an explicit save migration plan.
- Test the full-set planting bonus and durability handling on copied saves. Template retention and static recipe presence are not runtime certification.

## Evidence and credits

- [Three-release interaction, loot, recipe, template and delivery evidence](https://herbertofury.github.io/Advent-of-Ascension/petal-crafting-evidence.json)
- [Historical diagram and item-image hashes](https://herbertofury.github.io/Advent-of-Ascension/petal-crafting-art-evidence.json)
- [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Gardencia in the worlds guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions)

AoA item, block and creature artwork: Tslat and contributors. Diagram and extraction tools are original documentation work. All diagram item images are from **1.16.5**; modern acquisition differences are stated separately. No Java/game code was executed for this analysis.
