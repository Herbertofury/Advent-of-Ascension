# Historical Appearance Comparisons · 1.20.1

The 1.20.1 bestiary now offers a clearly separated **historical 1.16.5 appearance** for all **178 entries with a documented released-renderer gap**. This makes restoration research and version selection easier without passing an older model off as the current release.

## How to use it

1. Open a creature in the 1.20.1 bestiary.
2. Read its released-renderer warning first.
3. Expand **Compare historical 1.16.5 appearance · not the current renderer**.
4. Inspect the older source-derived portrait, then follow the historical creature entry or source registration if you need that release’s own statistics and spawn evidence.

Examples: [Airhead](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Aairhead) · [Alarmo](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Aalarmo).

## What the match means

- **Exact entity ID**, not a guessed visual resemblance or a fuzzy name match.
- The older portrait belongs to the separately documented 1.16.5 roster.
- An ID match does not prove identical models, textures, AI, attributes, loot, spawning, availability or migration safety.
- The current 1.20.1 portrait/reference count remains **107**. The **178 renderer gaps remain open**. No game code was repaired by adding these comparisons.
- Historical spawn rules and stats are not copied into the current creature’s fields.

## Loading behavior

The comparison metadata is carried in the selected 1.20.1 roster file. It does not fetch the whole 1.16.5 roster. Historical image elements are created only after the panel is expanded and are lazy-loaded. Reopening a panel does not recreate its contents.

Tests cover all 178 panels, the absence of images before expansion, explicit version labels, one-time panel construction, no extra release fetch, current portrait counts and renderer-warning preservation.

## Evidence and next steps

[Exact ID joins and historical source references](https://herbertofury.github.io/Advent-of-Ascension/historical-bestiary-comparisons-1.20.1.json).

For an actual restoration, use the [released renderer-gap audit](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Renderer-Gaps-1.20.1), identify the intended model/texture and registration target, adapt it to the target version, then validate it in-game. The historical reference is a starting point, not proof of a finished port.

## Inventory loading improvement

Separately, 66 corrected ore/foliage inventory cards now load standalone thumbnails of 2,830–24,646 bytes instead of full atlas images for their card pictures. Full atlas links remain available. This is a file-size reduction, not a measured startup/FPS claim. [Byte-size evidence](https://herbertofury.github.io/Advent-of-Ascension/direct-thumbnail-byte-budget.json).
