# Registered blocks and items · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** This focused repair adds **34 previously omitted entries** and corrects **six crystal-block previews** that had been matched to loose crystal items. It checks 40 model-backed declarations and preserves existing links. It does not claim a complete runtime registry.

## Find the right object

1. Select 1.12.2 in the [Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2).
2. Use the exact declaration ID below when similar names collide. Blue Crystal can describe a loose item, a world block or a plant; those models are not interchangeable.
3. Open the entry’s recipe search to inspect the actual version-specific recipe definitions. A search with no result is not proof an object is unobtainable; generation, trades and custom callbacks are separate acquisition paths.
4. For slabs, the picture below is the inventory half slab. The released helper also registers a double slab with a double_ prefix and no separate inventory item. Do not invent a second craftable item from that helper block.

## What was corrected

The six existing Blue/Green/Purple/Red/White/Yellow Crystal block cards retain their localization-based entry links, but now point to the declared *_crystal_block models. Their original gallery-sheet regions were corrected as well. The six loose crystal item cards remain unchanged. Exact registry aliases now work in inventory searches and entry URLs.

The new material references cover seven stones, six gemstone ores, four slabs, four stairs, two Archaic Streams, three carved runes, the Candycane block, four Mega Rune Fragment colors, the Candy Cane food item and two music discs. Matching art does not make the Candycane block and Candy Cane food the same registry object.

## Illustrated declaration directory

The images are static renders of the released item-model resources. Generated flat artwork remains a pixel-extruded item study; transparency, animation, resource packs and live renderer parity are not certified.

### Sheet 1

![Named released models, sheet 1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/registered-inventory-1.12.2-1.webp)

| Object | Declared item/block ID | What to know |
|---|---|---|
| [Abyssal Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aabyss_stone) | `aoa3:abyss_stone` | Newly indexed source-model reference. |
| [Crystevian Rock](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acrystevia_stone) | `aoa3:crystevia_stone` | Newly indexed source-model reference. |
| [Dustopian Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Adustopia_stone) | `aoa3:dustopia_stone` | Newly indexed source-model reference. |
| [Gardencian Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agardencia_stone) | `aoa3:gardencia_stone` | Newly indexed source-model reference. |
| [Iro Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Airomine_stone) | `aoa3:iromine_stone` | Newly indexed source-model reference. |
| [Lelyetian Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Alelyetia_stone) | `aoa3:lelyetia_stone` | Newly indexed source-model reference. |
| [Precasian Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ahigh_precasia_stone) | `aoa3:high_precasia_stone` | Newly indexed source-model reference. |
| [Blue Gemstone Ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ablue_crystal_ore) | `aoa3:blue_crystal_ore` | Newly indexed source-model reference. |
| [Green Gemstone Ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agreen_crystal_ore) | `aoa3:green_crystal_ore` | Newly indexed source-model reference. |
| [Purple Gemstone Ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Apurple_crystal_ore) | `aoa3:purple_crystal_ore` | Newly indexed source-model reference. |

### Sheet 2

![Named released models, sheet 2](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/registered-inventory-1.12.2-2.webp)

| Object | Declared item/block ID | What to know |
|---|---|---|
| [Red Gemstone Ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ared_crystal_ore) | `aoa3:red_crystal_ore` | Newly indexed source-model reference. |
| [White Gemstone Ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Awhite_crystal_ore) | `aoa3:white_crystal_ore` | Newly indexed source-model reference. |
| [Yellow Gemstone Ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ayellow_crystal_ore) | `aoa3:yellow_crystal_ore` | Newly indexed source-model reference. |
| [Mysterium Black Bricks Slab](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ablack_mysterium_bricks_slab) | `aoa3:black_mysterium_bricks_slab` | Half-slab inventory item; double slab is a separate world-state block. |
| [Mysterium Green Bricks Slab](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agreen_mysterium_bricks_slab) | `aoa3:green_mysterium_bricks_slab` | Half-slab inventory item; double slab is a separate world-state block. |
| [Shyre Wall Slab](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Awhite_shyre_bricks_slab) | `aoa3:white_shyre_bricks_slab` | Half-slab inventory item; double slab is a separate world-state block. |
| [Shyre Wall Slab](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ayellow_shyre_bricks_slab) | `aoa3:yellow_shyre_bricks_slab` | Half-slab inventory item; double slab is a separate world-state block. |
| [Mysterium Black Bricks Stairs](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ablack_mysterium_bricks_stairs) | `aoa3:black_mysterium_bricks_stairs` | Newly indexed source-model reference. |
| [Mysterium Green Bricks Stairs](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agreen_mysterium_bricks_stairs) | `aoa3:green_mysterium_bricks_stairs` | Newly indexed source-model reference. |
| [Shyre White Bricks Stairs](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Awhite_shyre_bricks_stairs) | `aoa3:white_shyre_bricks_stairs` | Newly indexed source-model reference. |

### Sheet 3

![Named released models, sheet 3](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/registered-inventory-1.12.2-3.webp)

| Object | Declared item/block ID | What to know |
|---|---|---|
| [Shyre Yellow Bricks Stairs](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ayellow_shyre_bricks_stairs) | `aoa3:yellow_shyre_bricks_stairs` | Newly indexed source-model reference. |
| [Archaic Stream: Horizontal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aarchaic_stream_horizontal) | `aoa3:archaic_stream_horizontal` | Newly indexed source-model reference. |
| [Archaic Stream: Vertical](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aarchaic_stream_vertical) | `aoa3:archaic_stream_vertical` | Newly indexed source-model reference. |
| [Blue Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ablue_crystal_block) | `aoa3:blue_crystal_block` | Corrected existing crystal block picture; loose item unchanged. |
| [Green Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agreen_crystal_block) | `aoa3:green_crystal_block` | Corrected existing crystal block picture; loose item unchanged. |
| [Purple Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Apurple_crystal_block) | `aoa3:purple_crystal_block` | Corrected existing crystal block picture; loose item unchanged. |
| [Red Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ared_crystal_block) | `aoa3:red_crystal_block` | Corrected existing crystal block picture; loose item unchanged. |
| [White Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Awhite_crystal_block) | `aoa3:white_crystal_block` | Corrected existing crystal block picture; loose item unchanged. |
| [Yellow Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Ayellow_crystal_block) | `aoa3:yellow_crystal_block` | Corrected existing crystal block picture; loose item unchanged. |
| [Carved Rune of Empowering](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acarved_rune_empowering) | `aoa3:carved_rune_empowering` | Newly indexed source-model reference. |

### Sheet 4

![Named released models, sheet 4](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/registered-inventory-1.12.2-4.webp)

| Object | Declared item/block ID | What to know |
|---|---|---|
| [Carved Rune of Focus](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acarved_rune_focus) | `aoa3:carved_rune_focus` | Newly indexed source-model reference. |
| [Carved Rune of Power](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acarved_rune_power) | `aoa3:carved_rune_power` | Newly indexed source-model reference. |
| [Candycane](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acandycane) | `aoa3:candycane` | Newly indexed source-model reference. |
| [Mega Rune Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amega_rune_fragment_blue) | `aoa3:mega_rune_fragment_blue` | Newly indexed source-model reference. |
| [Mega Rune Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amega_rune_fragment_green) | `aoa3:mega_rune_fragment_green` | Newly indexed source-model reference. |
| [Mega Rune Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amega_rune_fragment_red) | `aoa3:mega_rune_fragment_red` | Newly indexed source-model reference. |
| [Mega Rune Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amega_rune_fragment_yellow) | `aoa3:mega_rune_fragment_yellow` | Newly indexed source-model reference. |
| [Candy Cane](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acandy_cane) | `aoa3:candy_cane` | Newly indexed source-model reference. |
| [Music Disc: Outlaw](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aoutlaw_disc) | `aoa3:outlaw_disc` | Music Disc; Firch - outlaw. Specific title is editorial; class uses the generic record translation key. |
| [Music Disc: Caverns](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Acaverns_disc) | `aoa3:caverns_disc` | Music Disc; c_enthusiast_x2 - caverns. Specific title is editorial; class uses the generic record translation key. |

## Why the names were easy to miss

These declarations use different localization labels and registry suffixes: AbyssalStone maps to abyss_stone, BlueGemstoneOre to blue_crystal_ore, and BlueMegaRuneFragment to mega_rune_fragment_blue. A name-only join misses them. Conversely, BlueCrystal appears in several resource categories, so selecting the first loose-item model gives a block the wrong picture. The repair records the declaration, helper, exact model path and archive hashes instead.

## Itemless crop state references

Sixteen additional declarations explicitly use registerItemlessBlock. They have blockstate resources but no ordinary item model. They are separate from these 40 inventory-model references. Their eight growth stages and harvest behavior are now covered in [the historical farming walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2):

 | Itemless crop declaration | Released label |
|---|---|
| `aoa3:bubble_berry_crop` | Bubble Berries |
| `aoa3:chilli_crop` | Chilli |
| `aoa3:eye_bulb_crop` | Eye Bulb |
| `aoa3:floracles_crop` | Floracles |
| `aoa3:goldicaps_crop` | Goldicaps |
| `aoa3:heart_fruit_crop` | Heart Fruit |
| `aoa3:holly_tops_crop` | Holly Tops |
| `aoa3:lunacrike_crop` | Lunacrike |
| `aoa3:luna_globe_crop` | Luna Globe |
| `aoa3:lunalon_crop` | Lunalip |
| `aoa3:magic_marang_crop` | Magic Marang |
| `aoa3:mystic_shroom_crop` | Mystic Shrooms |
| `aoa3:rosidon_crop` | Rosidons |
| `aoa3:tea_crop` | Tea |
| `aoa3:thorny_plant_crop` | Thorny Plant |
| `aoa3:trilliad_crop` | Trilliads |

These are world-block documentation candidates, not missing collectible inventory items. The dedicated walkthrough checks age-state models, seed linkage and the local harvest behavior while keeping live Forge/modpack acceptance separate.

## Evidence and acceptance

- [Exact declaration, helper and model receipts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/registered-inventory-evidence-1.12.2.json).
- [Inventory explorer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2) and [source/version coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage).
- Original models, textures and labels: Tslat and Advent of Ascension contributors. Minecraft model bases: Mojang. Independent source-derived documentation.
- Static regression checks verify the 40 joins, preserved crystal entry IDs, separate Candycane block/food identities, two generic-record translation cases and explicit exclusion of the 16 itemless crops. Runtime acquisition and rendering remain separate acceptance work.

## Historical crop growth references

[Planting and harvesting sixteen 1.12.2 crops](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2) now documents all 128 age-state models, seed/produce links and source-level harvest rules. These itemless world blocks have their own classified entries; they are not ordinary collectible inventory items.
