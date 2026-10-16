# Infused Press compression and piston control · Minecraft 1.21.1

**Version:** released AoA 3.7.16.1. This is a source/bytecode-backed operating reference for packs that provide the Infused Press. The released recipe directory contains its two custom compression serializers, but this audit found **no recipe whose output is the station itself**. Registration and an item preview do not establish a stock Survival acquisition route.

[Crafting reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes) · [Custom recipe definitions](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=infused_press) · [Station resource card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ainfused_press)

## What it stores

The press combines **nine full, matching stacks** into one Compressed Item. The stored component contains a copy of the original stack and its compression tier. Higher tiers combine nine matching packets from the same previous tier.

![Nine full 64-item stacks represented as 576 stored items, with a separate max-stack-16 example](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infused-press-contents-diagram-1.21.1.webp)

The block icon inside the explanatory packet identifies its **contents**. It is not a verified image of the generic Compressed Item's runtime renderer. That item can carry different contents and cannot honestly be represented by one universal cobblestone preview.

| Original item's maximum stack size | Tier 1 | Tier 2 | Tier 3 |
|---|---:|---:|---:|
| 64 | 576 | 5,184 | 46,656 |
| 16 | 144 | 1,296 | 11,664 |

These low-tier arithmetic examples follow `maximum stack size × 9^tier`. They are not a promise of unlimited safe tiers; see the serialization warning below.

## 1. Arrange the piston above the press

![Source-derived vertical layout showing downward piston base two blocks above the press and a head space between them](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infused-press-piston-layout-1.21.1.webp)

The inspected neighbor-update path requires:

- The changed neighbor position is **one block above the press** and the reported neighbor block is a piston head.
- The piston base or moving-piston state is **two blocks above the press**.
- That state's facing direction is **DOWN**.

The normal-piston-base branch calls compression; the moving-piston branch calls decompression. These correspond to the intended extension/retraction cycle, but actual event order, modded pistons and redstone timing still need live verification in the target build.

Use a controllable signal while learning the mechanism. A quick pulse can make it appear that compression did nothing if the reverse operation runs before you remove the result. Keep the piston-head space clear and collect a compressed output before retracting when you want to keep it packed.

## 2. Load nine valid stacks

Open the press and use its **3×3 input grid**. Leave the separate output slot empty.

For ordinary items:

1. Fill all nine input slots.
2. Each stack must be stackable and at least its current maximum stack size. Normal unstackable equipment is rejected by this branch.
3. Use the same item **and the same components** in every slot. Matching names or textures alone are insufficient.
4. Trigger the compression branch and inspect the resulting stored item before moving valuable materials into long-term storage.

The successful block-entity path writes the assembled result into slot 9 and clears all nine inputs. This is whole-grid storage, not a one-item-per-slot crafting payment.

For already-compressed items, all nine must carry valid compressed-item data and match the same item/components and compression tier. Mixed contents or tiers do not combine just because every icon is called “Compressed Item.”

## 3. Decompress deliberately

1. Empty all nine input slots.
2. Put one valid Compressed Item in the separate output slot. The menu permits positive-tier compressed data there.
3. Trigger the decompression path associated with the piston cycle.
4. Inspect the nine restored stacks before collecting them.

At tier 1, assembly returns a copy of the stored original stack; the block entity places a copy into each of the nine input slots. At a higher tier, each restored slot receives one packet from the previous tier. Decompression goes down **one tier at a time** rather than exploding every nested tier at once.

The implementation copies stored stacks/components. That is evidence of intended preservation, not proof that every mod's dynamic components survive every version migration. Test a small, replaceable sample first.

## 4. Interpret comparator output carefully

- An occupied output slot produces signal **15**.
- Otherwise the signal is the number of input slots holding a full ordinary stack or a Compressed Item, from **0 to 9**.

A signal of 9 is **not proof that compression will succeed**. The comparator does not perform the recipe's full same-item/same-components validation. Nine individually full stacks of different materials can still count to 9 while failing the recipe.

This guide does not certify hopper, pipe or third-party automation capability behavior. Validate insertion, output extraction and piston sequencing together before building an unattended storage loop.

## High-tier warning: the negative-count guard does not enforce the saved-data limit

The stored component's codec allows compression tiers **1 through 18**. The inspected compression matcher checks a computed next-tier count for negativity. Its count helper uses floating-point exponentiation, rounding and signed-long multiplication.

Those are different constraints. An independent signed-long model gives:

- For maximum-stack-64 contents, the tier-18 calculation wraps negative, so the inspected negative guard rejects that next tier.
- For maximum-stack-16 contents, the tier-19 calculation wraps to a **positive** value, so negativity alone would not reject it, even though tier 19 lies outside the codec's 1–18 range.

The selected released method bytes confirm the arithmetic and the codec boundary; the examples are **independent calculations, not a live save/load failure reproduction**. Do not treat a positive tooltip count as proof that an extreme-tier packet can be saved safely.

Restoration work should enforce the supported tier range before assembly and use checked integer quantity arithmetic. Test accepted tiers, the first rejected tier, custom maximum-stack sizes, component serialization and client synchronization before exposing extreme compression to valuable items.

## Troubleshooting

| Symptom | Check |
|---|---|
| Compression does nothing | Nine occupied inputs, full ordinary stacks, identical item/components and empty output. |
| Comparator says 9 but nothing compresses | It counts qualifying slots, not full recipe equality. |
| The result immediately becomes nine stacks again | Check the retraction/reverse phase and remove the packet before cycling back. |
| Decompression refuses | Empty all nine input slots and supply valid positive-tier compressed data in output. |
| Damaged or renamed items do not combine | Their components may differ; ordinary unstackable items also fail. |
| No station recipe appears | No station-output recipe was found in this inspected release; check the pack's actual acquisition additions. |
| The web recipe card has no fixed ingredient/output picture | Both operations compute their result from stored contents. A generic recipe JSON cannot specify one fixed material. |

## Evidence and acceptance

[Released methods, custom declarations and eight quantity/overflow cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/infused-press-evidence-1.21.1.json) · [Diagram provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/infused-press-art-evidence-1.21.1.json) · [Restoration findings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes).

No game code was executed for this reference. Exact piston timing, automation, break/drop behavior, closed/open menu synchronization, save/load and private Enderloom behavior remain runtime acceptance work. The diagrams use AoA artwork by Tslat and contributors and vanilla references by Mojang/Microsoft.
