# Foliage Overlays and Default Tints

Precasian Grass and Stranglewood use layered faces. Their colored grass/vines are not separate geometry floating over the block: they are cutout textures on matching surfaces, with tint callbacks. A strict equal-depth documentation renderer can accidentally hide those layers.

## What these references show

- Ten released model resources across **1.20.1 and 1.21.1**, each in two presentations: **untinted source** and **vanilla default palette**.
- Six searchable inventory cards and their atlas crops now show the corrected default-palette reference. Horizontal helper models are documented separately, without inventing inventory entries.
- The AoA source delegates Precasian Grass coloring to vanilla grass, and Stranglewood/vine coloring to vanilla Acacia Leaves. The decoded default foliage RGB is **#48b518** in both releases.
- Grass uses the official colormap at temperature 0.5, downfall 1.0, pixel (127,127): **RGB (124,189,107), #7cbd6b**. The official class methods and colormap hashes are retained.
- Only faces with a declared tint index are colored. Untinted wood and soil pixels keep their original texture colors. Matching coplanar faces are composited in declared model order.

## 1.20.1

![Untinted and default-tinted foliage references for 1.20.1](https://herbertofury.github.io/Advent-of-Ascension/previews/1.20.1-foliage-overlay-reference.webp)

## 1.21.1

![Untinted and default-tinted foliage references for 1.21.1](https://herbertofury.github.io/Advent-of-Ascension/previews/1.21.1-foliage-overlay-reference.webp)

## Limits that matter

These are documentation renders, not in-game screenshots. The chosen palette is a defined default reference, not a promise that every biome has those colors. Runtime biome blending, lighting, resource-pack colormaps and shaders can change appearance. The horizontal model names do not imply that this neutral GUI camera reproduces every blockstate rotation.

The source registration and official default-color methods are inspected separately; this is not a proof of complete released callback equivalence or a live render test. Binary-alpha overlap and matching position/UV preconditions are asserted before compositing.

## Evidence and navigation

- [Model and palette evidence](https://herbertofury.github.io/Advent-of-Ascension/foliage-overlay-evidence.json)
- [Six exact atlas patches](https://herbertofury.github.io/Advent-of-Ascension/foliage-preview-repair-manifest.json)
- [Broader candidate audit](https://herbertofury.github.io/Advent-of-Ascension/coplanar-face-audit.json): includes aliases and templates; candidate totals are not unique broken items.
- [Ore overlay repairs](Coplanar-Ore-Preview-Repairs)
- [Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?q=stranglewood)
