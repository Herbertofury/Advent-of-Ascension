# Find a drop, choose a target, make something useful

[Open Find a Drop](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html) · [Bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html) · [Recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html)

## 1. Start with the item you need

Choose your exact Minecraft release and search the item's displayed name or registry ID in Find a Drop. Expand the creature associations, then open a creature to inspect its loot panel. Nested dimension/world tables are followed, so a shared world drop can legitimately appear under many creatures.

A listed association means the item occurs in an inspected table path. It does not promise that every listed creature drops it under every condition. Modern entries are matched entity-named resources; runtime table selection and overrides have not all been verified.

## 2. Check the creature before leaving home

In the bestiary, open **Where to find / Spawn declarations** and check the release, dimension and biome evidence. A tag or selector is not a guaranteed location. If no route is established, do not interpret that as a natural spawn or search blindly.

Read the base attributes and bring appropriate equipment, ammunition or runes, food and a retreat route. These are extracted base values, not an encounter difficulty score. Boss summoning, special protections and runtime modifiers need their own encounter instructions.

## 3. Read the loot panel correctly

| Panel field | Practical meaning |
|---|---|
| Item picture | A release-specific base model reference; explicit metadata variants have separate appearances. Potion/NBT colours may remain runtime-dependent. |
| Base stack | The count expression for a selected item entry, before additional functions. It is not the quantity guaranteed per kill. |
| Weight | Relative selection input within a pool, not a percentage. Other entries, conditions, quality and luck can matter. |
| Empty entry | A valid outcome with no item from that entry. |
| Looting / conditional | Inspect the exact function or condition before relying on an enchantment or kill method. |
| Nested table | A second table, often shared by a dimension or group. Follow it and use Previous table to return. |
| Missing binding | This browser has not established the table path; it does not prove there are no drops. |

A raw count expression can contain a negative lower bound. For example, legacy Amphibiyte Lung uses -1 to 1 followed by a Looting count function. That is source data, not an instruction that a player receives a negative item stack. The browser does not simulate the full loot engine, so it preserves the expression rather than inventing a final distribution.

## Worked example: Amphibiyte Lung

**Minecraft 1.12.2 · AoA 3.3.6.** [Find the item](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=amphibiyte_lung), then open [Amphibiyte](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aamphibiyte).

![Amphibiyte source-model reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-AmphibiyteModel.png)

The entry's portrait is reused only through the recorded cross-version source-model mapping. Its loot panel separately exposes the Overworld table, the lung pool and the mob-specific pool. Do not combine their weights into a single made-up drop percentage. Use **Find recipe references** beside the lung to see recipes that use or produce that registry ID in the same release.

## Worked example: Water Runes and random fish

**Minecraft 1.12.2 · AoA 3.3.6.** [Search Water Rune](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.12.2&q=water_rune), then inspect [Amphibior](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aamphibior).

Its mob-specific pool contains a Water Rune entry with a base count expression of 4–18. The same pool also contains an empty outcome and other items; 4–18 runes are not promised on each kill. Its fish entry uses a random-metadata function. Expand the four client model references to distinguish Raw Fish, Raw Salmon, Clownfish and Pufferfish.

The [pinned SetRandomMetadata source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/library/loot/functions/SetRandomMetadata.java) chooses from the item's SEARCH-tab subitems when the item has subtypes. The model gallery is a reference catalogue, not an independently verified list of every possible runtime outcome.

## 4. Turn the drop into progress

Use the release-preserving recipe link. Check whether the item is an ingredient or output, the crafting station, quantity, full pattern and any conditional recipe fields. A search match is not always a crafting recipe: loot-only or custom-code acquisition may need a separate guide.

If the recipe search is empty, keep the item and check the version before deciding it is useless. Trades, activation, progression and other non-recipe uses are not all indexed yet.

## If your result differs

- Confirm both Minecraft and AoA versions, plus the item's full ID.
- Check datapacks, global loot modifiers and other mods.
- Distinguish natural, summoned and spawner-born creatures where conditions apply.
- Inspect conditions, nested pools and function order.
- Report the creature, item, release and observed kill method. One unsuccessful kill is not proof that a table entry is broken.

This guide is grounded in extracted release tables and the linked pinned source. It is not a live-game drop-rate experiment.
