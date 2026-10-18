# Weapon art provenance across released versions

The original reference must say which release it comes from. A familiar name does not guarantee that its art, holding transform or behavior stayed unchanged.

## Current source check

The official default branch was rechecked at 2026-10-18 21:46 UTC: branch 1.21, commit 7919b5fe48599e6105c5740937ce36c36ef21d16. The production release listing returned 3.7.16.1 for Minecraft 1.21.1. All 46 cached changelog files were hash-verified against the unchanged source receipt; the GitHub tag/release lists were empty. This is a source check, not a native build promotion.

## Exact asset comparison

For the 228 first-target weapon IDs, compare released AoA 3.7.1 / Minecraft 1.20.1 against AoA 3.7.16.1 / Minecraft 1.21.1:

- All 228 direct item models were found in both archives.
- 104 have byte-identical model JSON; the remainder require parent/transform/override review.
- 193 have matching direct texture references and decoded pixels. The other 35 require artwork review, including Baronator and Iominator.
- Decoded comparison normalizes fully transparent RGB, so file encoding or invisible RGB alone does not cause the visible-pixel classification.
- Apoco Assault Rifle and Discharge Shotgun have identical direct model and texture bytes across these two lanes.
- Soul Storm keeps the same direct sprite, but its model parent changes from item/gun to item/small_gun. Same texture does not mean unchanged held presentation.

## Canonical-design consequences

Keep release-specific originals alongside the concept. Review later art explicitly before choosing a canonical interpretation. Preserve owner-approved concepts and distinct historical designs; do not silently overwrite them because a newer file exists. Newer is not automatically better, and matching IDs or images do not prove equivalent gameplay.

The source comparison resolves direct model textures only. Inherited models, overrides, dynamic renderers, shader behavior, resources and weapon code need their own review. No complete native weapon is accepted by this report.

[Versioned comparison data](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-texture-version-comparison.json) · [Reproducer and current-source receipts](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-art-version-study.zip)
