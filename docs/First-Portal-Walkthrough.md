# Your first portal: an illustrated walkthrough

**Pinned edition: Minecraft 1.21.1 / Advent of Ascension 3.7.16.1.** Build from the instructions for your installed release. A frame working in one release does not make every historical destination available in another.

## 1. Prepare before travelling

Establish shelter, food, armour and a reliable return route. The official getting-started entry points you toward ruined teleporter frames and the Corrupted Traveller deep underground. Ancient Rock can be scavenged from these structures. Treat exploration as the first objective; this guide does not invent a crafting recipe for Ancient Rock.

## 2. Gather the frame

You need **13 Ancient Rock**, **one Power rune**, and **one each of the Space, Direction, Reality and Travel runes**. Duplicate runes cannot replace missing types.

For the four non-power runes, the pinned Overworld loot table includes rare weighted entries. Its global loot modifier applies to player kills of hostile entities and excludes entities marked as spawner-born by AoA. This is a chance-based acquisition route, not a guarantee from any particular kill.

## 3. Make the Power rune

![Illustrated Power rune crafting recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/power-rune-recipe-1.21.1.webp)

The pictured recipe uses **seven Unpowered Runes**, **one Ancient Rock**, and **one Eye of Ender**. In a crafting table, put the Eye at top centre and Ancient Rock at centre; fill the seven remaining slots with Unpowered Runes.

The artifact also defines separate variants using Charged Runes and/or the `c:ender_pearls` ingredient tag. Follow one exact variant; a mixture of charged and unpowered runes is not specified by these patterns.

### Where do the small runes come from?

- Stonecutting one **Runium Chunk** produces **16 Unpowered Runes**.
- Stonecutting one **Charged Runium Chunk** produces **16 Charged Runes**.
- Normal, deepslate and Nether Runium Ore are in the iron-tool requirement tag. Charged Runium Ore is in the diamond-tool requirement tag.
- Their loot definitions produce the corresponding chunks, with Fortune handling. Silk Touch instead returns the ore block.

## 4. Build the frame

![Illustrated five-by-six portal frame](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/first-portal-1.21.1.webp)

Build the **5-wide, 6-tall outer rectangle** with a **3-wide, 4-tall clear opening**. Put the Power rune in the bottom-centre position. The diagram gives a valid arrangement for the four other distinct runes. The official frame validation accepts those four in other frame positions; keep the required counts and types.

## 5. Activate and choose a supported destination

Use the appropriate **Realmstone** on the frame's Power rune. Consult the [version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) and [worlds guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) before investing in a destination: modern releases do not automatically include all legacy realms.

## If it does not activate

1. Confirm your actual Minecraft and AoA versions against this guide.
2. Count the outside dimensions and clear the opening.
3. Check that the Power rune is bottom centre, not another rune with a similar appearance.
4. Confirm exactly one each of the other four rune types. Four copies of one type are not equivalent.
5. Check the selected destination and Realmstone against that release's support.
6. Check whether the modpack overrides recipes, tags or progression. Compare its in-game recipe viewer with the pinned reference before changing your world.

## Why version labels matter

The Infusion Table is a good example: in 1.21.1 its recipe uses the amethyst-gem tag, Ancient Rock, an Enchanting Table and a Crafting Table. The 1.20.1 and 1.16.5 versions instead use wool, Ancient Rock, an infusion-stone tag and obsidian. The 1.12.2 Power rune also has a different item ID. Never silently transplant an older recipe into a modern walkthrough.

## Evidence and credits

These instructions are an original summary checked against the official **AoA3-1.21.1-3.7.16.1.jar**:

- `assets/aoa3/patchouli_books/aoa_essentia/en_us/entries/getting_started.json`
- `assets/aoa3/patchouli_books/aoa_essentia/en_us/entries/the_portal.json`
- `data/aoa3/recipe/crafting_shaped_carved_rune_of_power.json` and its three charged-rune/pearl variants
- `data/aoa3/recipe/stonecutting_unpowered_rune_from_runium_chunk.json`
- `data/aoa3/recipe/stonecutting_charged_rune_from_charged_runium_chunk.json`
- `data/aoa3/loot_table/worlds/overworld.json` and `data/aoa3/loot_modifiers/world_tables.json`
- Vanilla-namespaced iron/diamond tool requirement tags supplied by the mod
- [Pinned upstream portal validation source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/world/teleporter/AoAPortalFrame.java)

[Official download](https://modrinth.com/mod/adventofascension/version/vIo8vp51). Models and textures by **Tslat and contributors**; the illustrated layouts are independently generated documentation showcases. This guide is artifact/source-checked, not a new in-game test receipt or proof of Enderloom conversion.
