# Frame Bench and armor Infusion: from scrap to a matching set

[Armor preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Materials-and-Set-Preparation-1.21.1) · [Infusion Table walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1) · [Worn armor gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Worn-Armor-Gallery-1.21.1)

**Minecraft 1.21.1 / AoA 3.7.16.1.** The missing step between Scrap Metal and armor is the **Frame Bench**. Its ten choices are implemented by its menu, not ten ordinary recipe JSON files. This walkthrough also covers the **32 bundled armor Infusion recipes**, grouped into eight complete sets. It does not claim that all 48 registered sets are craftable this way.

![Shapeless recipes for the Frame Bench and Scrap Metal](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/frame-bench-crafting-1.21.1.webp)

## 1. Make the bench and Scrap Metal

- **Frame Bench:** one Crafting Table + one Iron Axe + one Shears, in a shapeless recipe. Use spare tools; do not assume an enchanted or valuable tool will be preserved by this ingredient recipe. [Exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Acrafting_shapeless_frame_bench)
- **Scrap Metal:** one ingredient matching `#c:ingots/iron` + one matching `#c:nuggets/gold` + one Limonite Nugget → one Scrap Metal. Tags keep their active-pack meaning; the diagram's iron and gold icons are examples, not a fixed member list. [Exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Acrafting_shapeless_scrap_metal)
- **One full armor-frame set:** prepare four Scrap Metal. Crafting those four requires four accepted iron ingots, four accepted gold nuggets and four Limonite Nuggets, before the additional Infusion ingredients below.

Scrap Metal also appears in loot declarations, but the shapeless recipe gives a direct preparation route without treating an uncertain loot roll as guaranteed. Its separate smelting recipe produces an Iron Nugget, not a frame.

## 2. Select and take the frame you need

![The ten Frame Bench choices in their released three-four-three row order](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/frame-bench-selections-1.21.1.webp)

1. Place the bench and interact with an empty hand to open the supported menu path.
2. Put Scrap Metal in the single input slot. The input slot predicate checks that exact item, not a general metal tag.
3. Click the desired frame button. The initial selection is Crossbow Frame, so check the output before taking it.
4. Take the output. The selected output callback consumes one unit from input slot 0. Four different armor frames require four separate output takes; this is not a four-piece output bundle.
5. Change selection for the next piece. The armor row is Helmet, Chestplate, Leggings, Boots. The other six choices are weapon frames.
6. Close normally when done. The shared menu delegates remaining-input cleanup to `clearContainer`; do not treat the bench as persistent storage. Full-inventory, shift-click, disconnect and repeated-click behavior still require exact-build testing.

| Selector row | Choices, left to right |
|---|---|
| Top | Crossbow Frame · Blaster Frame · Cannon Frame |
| Middle | Helmet Frame · Chestplate Frame · Leggings Frame · Boots Frame |
| Bottom | Gun Frame · Shotgun Frame · Sniper Frame |

## 3. Move to the Infusion Table

Build and use the [Infusion Table](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1). Put the correct frame in its base slot, then supply the recipe's additional ingredients in the input arrangement expected by that station. **Repeated ingredient entries are separate required units/slots; putting several units into one occupied slot does not automatically satisfy several ingredient positions.** Check the output before taking it.

The eight lists below are shopping totals for **one helmet, one chestplate, one leggings and one boots recipe**. They exclude the four frame inputs and the materials used to craft those frames. They also exclude the workstation itself. A list is preparation arithmetic, not a bulk-crafting command or an assertion that all materials are obtainable in every unfinished world.

### Embrodium

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-embrodium-1.21.1.webp" width="220" alt="Embrodium neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **1 ×** [Padded Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Apadded_cloth)
- **9 ×** [#c:ingots/blazium](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Fblazium) (active ingredient tag)
- **10 ×** [#c:ingots/varsium](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Fvarsium) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_embrodium_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_embrodium_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_embrodium_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_embrodium_boots)

### Hazmat

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hazmat-1.21.1.webp" width="220" alt="Hazmat neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **2 ×** [Padded Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Apadded_cloth)
- **11 ×** [Reinforced Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Areinforced_cloth)
- **1 ×** [minecraft:charcoal](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=minecraft%3Acharcoal)
- **7 ×** [#c:strings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Astrings) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_hazmat_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_hazmat_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_hazmat_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_hazmat_boots)

### Ice

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ice-1.21.1.webp" width="220" alt="Ice neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **18 ×** [Ice Crystal](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aice_crystal)
- **4 ×** [#c:ingots/iron](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Firon) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_ice_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_ice_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_ice_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_ice_boots)

### Infernal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-infernal-1.21.1.webp" width="220" alt="Infernal neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **4 ×** [Ice Crystal](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aice_crystal)
- **1 ×** [Padded Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Apadded_cloth)
- **8 ×** [minecraft:magma_cream](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=minecraft%3Amagma_cream)
- **8 ×** [#c:ingots/emberstone](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Femberstone) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_infernal_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_infernal_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_infernal_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_infernal_boots)

### Lyndamyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyndamyte-1.21.1.webp" width="220" alt="Lyndamyte neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **13 ×** [#c:ingots/emberstone](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Femberstone) (active ingredient tag)
- **11 ×** [#c:ingots/limonite](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Flimonite) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_lyndamyte_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_lyndamyte_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_lyndamyte_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_lyndamyte_boots)

### Skeletal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-skeletal-1.21.1.webp" width="220" alt="Skeletal neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **2 ×** [Chestbone Fragment](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Achestbone_fragment)
- **1 ×** [Footbone Fragment](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Afootbone_fragment)
- **2 ×** [Legbone Fragment](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Alegbone_fragment)
- **2 ×** [Padded Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Apadded_cloth)
- **1 ×** [Skullbone Fragment](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Askullbone_fragment)
- **6 ×** [#c:foods](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Afoods) (active ingredient tag)
- **12 ×** [#c:ingots/skeletal](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Fskeletal) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_skeletal_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_skeletal_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_skeletal_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_skeletal_boots)

### Void

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-void-1.21.1.webp" width="220" alt="Void neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **6 ×** [Void Scales](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Avoid_scales)
- **12 ×** [#c:ingots/iron](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Aingots%2Firon) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_void_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_void_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_void_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_void_boots)

### Wither

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-wither-1.21.1.webp" width="220" alt="Wither neutral armor-only source study">

**Bring:** one Helmet Frame, one Chestplate Frame, one Leggings Frame and one Boots Frame, plus:

- **5 ×** [Armour Plating](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aarmour_plating)
- **4 ×** [Padded Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Apadded_cloth)
- **4 ×** [Reinforced Cloth](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Areinforced_cloth)
- **6 ×** [Wither Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Awither_rune)
- **10 ×** [#c:gems/bloodstone](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=c%3Agems%2Fbloodstone) (active ingredient tag)

**Open the exact diagrams:** [Helmet](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_wither_helmet) · [Chestplate](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_wither_chestplate) · [Leggings](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_wither_leggings) · [Boots](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Ainfusion_wither_boots)

## Why a frame may be missing from a recipe search

`FrameBenchRecipe` is explicitly a recipe-display helper and returns a null serializer in this inspected release. The actual selection/output path is `FrameBenchMenu`: a fixed array of ten choices, the Scrap Metal input predicate, and the output-removal callback. The archive's `frame_bench_frame` tag contains those ten items, but the menu is not shown reading that tag to populate its choices. Adding an item to the tag alone is not demonstrated to add a new menu button.

The 32 recipes above are real bundled Infusion definitions. The distinction matters: a JSON-only recipe census would find their outputs but miss the menu-driven frame-making step.

## Other armor acquisition remains separate

The other armor registrations are not covered by these 32 recipe outputs. Some have loot-table entries, code-driven rewards, different systems or unresolved acquisition routes. **Absence from this recipe list is not proof that an item is unobtainable.** Keep the exact version and inspect the item's recipe, loot and trade links rather than copying an older release's recipe into this one.

## Restoration checks

- [ ] Validate selector bounds before storing or indexing a selected frame. The inspected `clickMenuButton` checks equality with the current selection, but contains no explicit range guard before the later array access. Ordinary UI buttons emit the ten known selections; this is a defensive acceptance target, not a reproduced gameplay crash.
- [ ] Test empty input, each of the ten choices, changing selection while input remains, output take, repeated take and shift-click.
- [ ] Test full inventory, normal close, disconnect and re-open without duplication or lost input.
- [ ] Keep the menu, client buttons, JEI display and any future data-driven options consistent. Avoid repeated whole-registry scans during ordinary clicks.

[Released menu methods, exact JSON recipes and full-set totals](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/frame-bench-and-armor-infusion-evidence-1.21.1.json) · [Illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/frame-bench-art-evidence-1.21.1.json)

These are static artifact and method checks, not in-game certification. AoA source assets and systems are credited to Tslat and contributors; vanilla item references to Mojang/Microsoft. Original documentation diagrams and source-joined shopping lists.
