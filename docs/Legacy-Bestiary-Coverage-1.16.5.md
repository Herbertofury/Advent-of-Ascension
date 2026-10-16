# Illustrated bestiary coverage: Minecraft 1.16.5

**AoA 3.6.11 resources · pinned 1.16.5 source roster.** Every one of the 419 inspected living-entity entries now has an appearance classification. The field guide includes 409 body portraits, eight particle reference grids, and explicit explanations for the two entries without a fixed body image.

[Browse the complete inspected roster](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5) · [Find an item’s creature-table references](https://herbertofury.github.io/Advent-of-Ascension/drop-finder.html?v=1.16.5) · [Crafting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5)

## What the pictures mean

| Classification | Count | What you can inspect |
|---|---:|---|
| Source-mapped body portrait | 409 | A static geometry/texture reference linked to renderer evidence |
| Particle-only Pixon reference | 8 | All eight released sprite frames with the registered tint |
| Intentionally invisible | 1 | Shadow's empty source render method |
| Dynamic player skin | 1 | Doppelganger's runtime skin selection and layer behaviour |

These counts describe this inspected roster, not every miscellaneous entity or projectile in the game. A portrait does not certify animation, collision, spawn availability, multiplayer behaviour or a restored Enderloom implementation.

## Inspect changing appearances

Open **Source appearances** on the relevant card:

- [Cotton Candor](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Acotton_candor): six phase texture references.
- [Crystocore](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Acrystocore): six phase texture references.
- [Blue Rune Templar](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Ablue_rune_templar), with matching galleries on the green, red and yellow entries: active and disabled textures.
- [Dryad Sprite](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Adryad_sprite): Wood, Stone, Iron, Gold, Diamond and Netherite textures.

A shown phase is an example, not a claim about which phase is active in your world. The gallery does not simulate state transitions.

## Why Shadow and Doppelganger have no fixed portrait

[Shadow](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Ashadow) uses an intentionally empty render method and no texture. Drawing an invented shadow monster would misrepresent the source.

[Doppelganger](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Adoppelganger) uses the local client's player skin and includes armour, held-item and arrow layers. There is no single fixed AoA texture that represents every encounter. The source link on its card identifies the selection method.

## Pixons are particles, not missing models

[Ambient Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Aambient_pixon) and the other seven variants use Flickering Sparkler particles. Their reference grids show the released sprite frames with the registered colour, before randomized brightness, size and lifetime.

![Ambient Pixon source sprite references](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-particle-ambient_pixon.webp)
![Radiant Pixon source sprite references](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-particle-radiant_pixon.webp)

The checkerboard helps distinguish white and black source tints. It is a documentation background, not a world effect. The runtime particle multiplies brightness by a random factor and varies size/lifetime; the grid is not a recorded animation.

## Vanilla-backed bodies

Some NPCs and mobs deliberately use Minecraft humanoid or cow geometry with AoA textures. The new references reconstruct the official 1.16.5 constructors through a restricted symbolic reader, without running Minecraft code. Humanoid references use the selected 64×32 or 64×64 texture layout. Creep Cow also applies the exact constant body rotation assigned by the official Quadruped animation method, avoiding a misleading upright constructor-only body.

Shiny Squid's nine-part source formula and released texture were checked against the modern source study. Its image omits runtime tentacle movement, body rotations and fullbright lighting. Other portraits likewise omit equipment and animated poses unless a page explicitly says otherwise.

## Evidence and credits

- [Coverage ledger](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-portrait-coverage-1.16.5.json)
- [Direct renderer joins](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-portrait-join-results.json)
- [Additional shared Java models](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-portrait-join-results-v2.json)
- [Custom phase and texture mappings](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-custom-portrait-results.json)
- [Vanilla-backed renderer mappings](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-vanilla-portrait-results.json)
- [Particle assets and registered colours](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/legacy-particle-reference-evidence.json)

AoA models and textures: Tslat and contributors. Vanilla geometry: Mojang. These are independent documentation renders, not generated concept art or live-game screenshots.
