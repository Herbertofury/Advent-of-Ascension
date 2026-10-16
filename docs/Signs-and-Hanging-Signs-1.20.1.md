# Signs and hanging signs · Minecraft 1.20.1

**AoA 3.7.1 · 15 presentations across 12 block identities.** This closes the six wall-only inventory-reference gaps without inventing separate wall-sign inventory items.

The official Minecraft 1.20.1 layer factories were decoded independently. Their five resulting geometry/visibility forms exactly match the separately verified 1.21.1 geometry. The hanging-sign visibility method also matches instruction-for-instruction after official class-name normalization, with field mappings checked; the standing-sign stick predicate was inspected directly. All six AoA wood textures are byte-identical between the two inspected artifacts.

Only after these checks were the existing render images reused. This is exact asset/geometry reuse, not an assumption that adjacent Minecraft versions behave the same. Source hashes and comparisons are included below.

## Baobab

![baobab sign forms](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-signs-baobab.webp)

[Standing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-baobab-standing.webp) · [Wall](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-baobab-wall.webp) · [Wall hanging](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-baobab-hanging_wall.webp) · [Ceiling, unattached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-baobab-hanging_ceiling.webp) · [Ceiling, attached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-baobab-hanging_attached.webp)

## Lucalus

![lucalus sign forms](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-signs-lucalus.webp)

[Standing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-lucalus-standing.webp) · [Wall](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-lucalus-wall.webp) · [Wall hanging](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-lucalus-hanging_wall.webp) · [Ceiling, unattached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-lucalus-hanging_ceiling.webp) · [Ceiling, attached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-lucalus-hanging_attached.webp)

## Stranglewood

![stranglewood sign forms](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-signs-stranglewood.webp)

[Standing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-stranglewood-standing.webp) · [Wall](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-stranglewood-wall.webp) · [Wall hanging](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-stranglewood-hanging_wall.webp) · [Ceiling, unattached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-stranglewood-hanging_ceiling.webp) · [Ceiling, attached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-sign-stranglewood-hanging_attached.webp)

## Limits and restoration checks

- These are blank, static, object-space sign models with documentation lighting.
- Text layout, glowing ink, wax, interaction, world placement transforms, waterlogging and actual runtime render parity have not been tested here.
- The two ceiling hanging variants are states of one block, not additional item identities.
- Wall forms use the corresponding ordinary or hanging sign item; an absent independent inventory model does not imply missing in-world geometry.
- The released SignBlockGroup references vanilla wall/ceiling sign classes and its no-item policy. The pinned source snapshot is supplementary context, not a substitute for the released class check.

[Official factory, visibility, texture and registration evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sign-reference-evidence-1.20.1.json) · [1.21.1 sign reference](Signs-and-Hanging-Signs-1.21.1) · [Inventory resolution ledger](Inventory-Preview-Resolution-Ledger).

Geometry conventions by Mojang; AoA wood artwork by Tslat and contributors. Original files are not bundled as a mod; these are derived documentation references.
