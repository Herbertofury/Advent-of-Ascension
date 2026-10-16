# Signs and hanging signs · 1.21.1

**15 world-model presentations across 12 block identities**, using Baobab, Lucalus and Stranglewood. The two ceiling-hanging variants are states of the same block. These blank sign models complement their ordinary inventory icons.

Geometry is read symbolically from the official Minecraft 1.21.1 sign-layer factories; wood textures come from AoA 3.7.16.1. The AoA source registers vanilla sign block classes with its own wood types. No game or JVM was launched.

## Baobab

![Baobab sign forms](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-signs-baobab.webp)

Full-size views: [Standing sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-baobab-standing.webp) · [Wall sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-baobab-wall.webp) · [Wall hanging sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-baobab-hanging_wall.webp) · [Ceiling · unattached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-baobab-hanging_ceiling.webp) · [Ceiling · attached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-baobab-hanging_attached.webp)

Block IDs: `aoa3:baobab_sign`, `aoa3:baobab_wall_sign`, `aoa3:baobab_hanging_sign`, `aoa3:baobab_wall_hanging_sign`.

## Lucalus

![Lucalus sign forms](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-signs-lucalus.webp)

Full-size views: [Standing sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-lucalus-standing.webp) · [Wall sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-lucalus-wall.webp) · [Wall hanging sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-lucalus-hanging_wall.webp) · [Ceiling · unattached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-lucalus-hanging_ceiling.webp) · [Ceiling · attached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-lucalus-hanging_attached.webp)

Block IDs: `aoa3:lucalus_sign`, `aoa3:lucalus_wall_sign`, `aoa3:lucalus_hanging_sign`, `aoa3:lucalus_wall_hanging_sign`.

## Stranglewood

![Stranglewood sign forms](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-signs-stranglewood.webp)

Full-size views: [Standing sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-stranglewood-standing.webp) · [Wall sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-stranglewood-wall.webp) · [Wall hanging sign](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-stranglewood-hanging_wall.webp) · [Ceiling · unattached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-stranglewood-hanging_ceiling.webp) · [Ceiling · attached](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-sign-stranglewood-hanging_attached.webp)

Block IDs: `aoa3:stranglewood_sign`, `aoa3:stranglewood_wall_sign`, `aoa3:stranglewood_hanging_sign`, `aoa3:stranglewood_wall_hanging_sign`.

## Visibility rules and source evidence

- Standing signs show the stick; wall signs hide it.
- Wall hanging signs show the support plank and normal chains.
- Ceiling hanging signs hide the plank. The attached state selects the V-chain plane; the unattached state selects the normal chain parts.
- The source uses a no-cull cutout render type. The documentation adapter preserves opaque artwork from both coincident planar faces; otherwise transparent opposite UVs can make chains disappear. A synthetic red/blue cutout fixture was verified from both sides.

[AoA sign group registrations](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/block/group/SignBlockGroup.java) · [AoA wood types](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/block/AoABlockSets.java) · [Block registration](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/block/AoABlocks.java) · [Factory hashes, official mapping provenance and cutout test](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sign-reference-evidence-1.21.1.json)

Wall forms intentionally have no separate inventory item in the inspected registration code; they use the corresponding ordinary/hanging item and drops. Missing inventory geometry for those block-only IDs is not itself a missing in-world appearance.

## What these pictures do not certify

Each form is fitted to its own camera framing, so the sheet is not a world-scale comparison. Text, glow ink, orientation, waterlogging, interactions and game lighting are not reproduced. These are source-backed visual references, not in-game screenshots or proof of target-platform conversion. Source classes and artifact hashes are version-specific.

Vanilla model geometry: Mojang. AoA wood artwork and registrations: Tslat and contributors. Independent documentation rendering.

[Visual atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Visual-Atlas) · [Render coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage)
