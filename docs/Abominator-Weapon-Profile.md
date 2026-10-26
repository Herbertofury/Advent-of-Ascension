# Abominator — original weapon and premium concept

**Baseline: Minecraft 1.20.1 / AoA 3.7.1. New artwork and transformations are proposals, not a playable completed weapon.**

## What it is and does

Abominator is a purple, silver and graphite automatic gun using AoA's shared BaseGun behavior. Its released class forwards its four constructor inputs to BaseGun and overrides the firing sound with `ITEM_GUN_GENERIC_FIRE_1`; it does not define a unique projectile, extra explosion or soul beam in that class. The inherited baseline is the Limonite-bullet gun path. Its supernatural-looking art must not be mistaken for evidence that the original fires magic beams.

The source sprite has a short projecting dark muzzle, strong silver horizontal stripe, repeated purple accents above the body, a downward dark section and a large purple rear silhouette with a silver inset. Preserve that recognizable identity in the premium model.

## Released baseline inputs

| Property | Released registration / class evidence |
|---|---|
| Item | `aoa3:abominator` |
| Base damage input | 2.625 |
| Durability input | 4720 |
| Firing delay input | 3 ticks |
| Recoil input | approximately 0.8; not a claim of degrees |
| Firing sound | `ITEM_GUN_GENERIC_FIRE_1` |
| Special override in Abominator class | Firing sound only |

These are base inputs, not measured final damage or effective DPS. Armor, effects, target rules and real firing timing need runtime verification. Inherited behavior is documented with the shared gun-family evidence; lack of a class-local override is not proof that every inherited interaction has been tested.

## How to obtain it in this release

The released `infusion_abominator.json` uses one Gun Frame as its input and six ingredient entries: one Ghoulasm, two `forge:ingots/ghastly`, two `forge:ingots/ghoulish` and one `forge:ingots/iron`. This is an AoA infusion recipe, not a vanilla crafting-grid layout. Tag entries may accept multiple matching items.

The released `upgrade_kit_iominator.json` converts Abominator into Iominator using an Ancient Upgrade Kit. That existing upgrade remains distinct from our proposed modular parts.

## Premium concept exploration

![Abominator original-inspired concept and alternate barrels](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abominator-concept-exploration-v1.png)

The small pixel inset inside the generated concept is an illustrative reconstruction, not an exact source extraction. The actual source sprite is shown separately below. The concept establishes a direction; hand fit, ammunition/feed presentation, moving parts and reload clearance remain unaccepted. Do not export it as a mechanically validated final model.

![Actual released Abominator sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abominator-original-sprite.png)

### Interactive loadout design workbench

[Open the Abominator workbench](https://herbertofury.github.io/Advent-of-Ascension/abominator-workbench.html). Choose original-inspired or proposed conversion directions, matching resource-adapter drafts, sights, finishes, charms, emblems and presentation profiles. Contradictory resource contracts block design export; reduced presentation resolves decorative choices explicitly. Shared links and JSON exports contain design selections only. No account, uploaded save or game-state changes are involved.

![Concept-only Abominator loadout UI, captured in a browser](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abominator-loadout-workbench-study-v1.png)

This is an actual browser UI preview, not a Minecraft screenshot or a rendered assembly of the chosen parts. The hero artwork remains the preserved magazine-corrected concept. Source values are pinned to 1.20.1 / AoA 3.7.1 and labeled as constructor inputs, not measured damage or DPS. Conversion projectile behavior, cost, damage, timing, unlocks and native compatibility remain unspecified or unverified. The exported manifest is explicitly non-installable.

The build/crafting/UI category now has initial partial UI evidence. All fourteen dedicated-sheet groups have at least one partial candidate, not a complete customization package. Full crafting recipes, option geometry, animation, audio and native QA remain open.

### Planned identity-specific barrel transformations

- **Violet Needle:** a focused purple energy bolt conversion with a precise, readable trail. It requires a declared projectile/resource adapter rather than merely repainting native bullets and claiming a new effect.
- **Abyss Choir:** a split-prism fantasy pulse pattern. Projectile count, damage and cost must match the chosen assembly and visible discharge pattern.
- **Dusk Bloom:** an expanding arcane ring shot with explicit collision shape and per-target hit rules.
- **Original-inspired ballistic mode:** retain the baseline Limonite-bullet behavior with upgraded animation, sound presentation and optional muzzle/tracer styling.

New conversions may deliberately increase output or add effects. Original mode remains separately selectable and documented. Preserve all concept versions; no proposed conversion has native acceptance yet.

## Full acceptance work still required

- [ ] Verify actual original in-flight bullet and entity/block impact footage in this release.
- [ ] Design a comfortable usable grip and believable ammunition/feed presentation without clipping.
- [ ] Create the editable native-compatible model, textures and complete animation set.
- [ ] Validate every attachment, sight, charm and decal across the entire animation envelope.
- [ ] Implement and test functional conversions, accurate tooltips and resource ownership.
- [ ] Verify sound, recoil, multiplayer, saves and measured performance.

[Released class evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/abominator-released-class-evidence.json) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades) · [Charm and effects customization](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
