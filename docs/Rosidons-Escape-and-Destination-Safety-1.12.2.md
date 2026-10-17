# Rosidons escape and destination safety · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** Rosidons is an always-edible crop product that requests a vertical teleport at your current X/Z coordinates. It is not a checked route home, a dimension-changing item, or a guarantee of a safe landing.

![Rosidons two-air-cell and three-air-cell destination comparison](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/rosidons-escape-column-study-1.12.2.webp)

## Before relying on it

1. Obtain Rosidon Seeds through the [checked seed-acquisition references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Finding-Seeds-and-Starting-a-Farm-1.12.2), then grow and harvest the Rosidon crop using the [historical farming guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2).
2. Plan for an upward relocation in the same X/Z column, not a return to your spawn or a search for nearby open ground. The callback keeps your original floating-point X/Z coordinates.
3. Finish the food-use action. Rosidons has zero hunger and zero saturation modifier, with the always-edible flag enabled; its purpose is the extra action rather than nutrition.
4. In the configured Ancient Cavern or Immortallis dimensions, the server callback reports a dimension-failure message and returns without requesting a teleport.
5. Elsewhere, the helper computes a height. A result of zero reports a no-height failure. A nonzero result requests `setPositionAndUpdate(current X, height + 2, current Z)`.

The local callback has no refund path for these failures. The normal food-completion path still handles consumption; check the target build's actual stack behavior before treating a failed use as free. The server guard prevents the local client branch from selecting a destination.

## Which height is used?

| Dimension branch | Height source | Important boundary |
|---|---|---|
| Configured Deeplands | Scan downward from Y121 | Uses the special exact-air test below |
| Nether, dimension −1 | Scan downward from Y128 | Uses the special exact-air test below |
| Configured Crystevia | Scan downward from Y127 | Uses the special exact-air test below |
| Other allowed dimensions | `world.getHeight(integer X, integer Z)` | No additional safety search in the inspected helper |

The special scan starts at its listed height and continues while Y is greater than zero. It remembers consecutive blocks whose block identity is exactly `Blocks.AIR`. When it reaches a non-air block after at least two consecutive air cells, it returns that non-air block's Y. It does not inspect a player's bounding box or require that the non-air block is safe solid ground.

For the special scan, an X or Z whose absolute integer value exceeds 30,000,000 returns zero. The ordinary-height branch returns before that explicit check. Exceptions inside the helper return zero. These are local branch facts, not a full account of the world's own boundary handling.

## Why two air cells can still be insufficient

The helper and the caller use different reference points:

- Suppose a full solid floor is at Y40, with air at Y41 and Y42 and a roof at Y43.
- The helper accepts that two-cell air run and returns **40**.
- Rosidons requests the player's feet at **42**, because the caller adds two.
- A modeled standing body 1.8 blocks tall reaches **43.8**, overlapping the full-solid roof in this simplified example.

With three air cells above the same floor, this particular vertical body model clears the roof. That is not a general safety proof: neighboring columns, body width, fluids, hazards, supports, collision shapes, modded dimensions and changed player sizes are not modeled.

The inspection includes the released Rosidons/helper methods and a vanilla player-sizing comparison. The 72 solid/air column cases are original bounded models. **No live teleport, collision or damage test was run, and this does not establish that the current Enderloom build has the same behavior.**

## Negative-coordinate mismatch

Rosidons casts X and Z to Java integers before calling the height helper. A cast truncates toward zero; selecting the containing block normally floors the coordinate.

| Player coordinate | Integer used for the helper | Floor of the coordinate |
|---:|---:|---:|
| −2.9 | −2 | −3 |
| −0.9 | 0 | −1 |
| −0.1 | 0 | −1 |
| 0.9 | 0 | 0 |
| 1.9 | 1 | 1 |

The teleport still uses the original floating-point coordinates. At negative fractional positions, the checked column can therefore differ from the column containing the player. The source does not add a neighboring-column or final-body clearance check to resolve that mismatch.

## Restoration test checklist

- [ ] Verify the target build's callback before changing it; preserve intended dimension restrictions and ordinary food behavior.
- [ ] Use consistent block-coordinate conversion for scanning and destination validation, including negative X/Z.
- [ ] Validate the actual destination bounding box, collision shapes, support and dangerous fluids/blocks before moving the player.
- [ ] Cover two-cell cavities, taller rooms, overhangs, surface foliage, Nether ceilings, altered dimensions and world boundaries.
- [ ] Check server authority, failure feedback and consumption/refund behavior, including Creative and food-hook interactions.
- [ ] Bound any expanded search and avoid unnecessary chunk generation or large synchronous scans. Measure worst-case work rather than assuming a safety check is free.

The existing special scan is bounded by its fixed start height, but that alone does not establish safe placement. Improving safety should not silently change the item's destination rules or introduce world-generation stalls.

## Evidence and related tools

- [Released methods, 72 column cases and 12 coordinate cases](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/rosidons-escape-evidence-1.12.2.json)
- [Diagram and source-item provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/rosidons-art-evidence-1.12.2.json)
- [Open the Rosidons item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Rosidons.name)
- [Source findings and restoration work](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes)

Original item artwork and mechanics by Tslat and AoA contributors. The geometry diagram is an original documentation model, not an in-game screenshot.
