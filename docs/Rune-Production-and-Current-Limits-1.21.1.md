# Rune production and current limits · Minecraft 1.21.1

**Version:** released AoA 3.7.16.1 for Minecraft 1.21.1. This guide separates two verified input recipes from registered station behavior whose survival acquisition still needs checking in the actual pack. It does not import the older Runation progression into the modern game.

[Item and block browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&q=rune) · [Recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=rune) · [Historical 1.16.5 handbook](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rune-Production-and-Randomizer-1.16.5)

![Two stonecutting recipes, example Rune Post and Rune Randomizer, with acquisition limits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/rune-input-workflow-1.21.1.webp)

## 1. Prepare the right input

| Stonecutter input | Output | Post generation factor |
|---|---|---|
| 1 Runium Chunk | 16 Unpowered Runes | 1 rune per submitted input |
| 1 Charged Runium Chunk | 16 Charged Runes | 2 runes per submitted input |

These are two released **stonecutting** recipes. A crafting-grid arrangement from another release is not interchangeable. Charged Runes also appear in Carved Rune of Power recipes; keep portal-building stock separate from experimentation.

No direct crafting recipe for a Rune Post or Rune Randomizer was found in this release's recipe directory. Their registration, textures and block-drop tables alone do not establish that a player can naturally obtain them. Check your exact pack's world generation, custom recipes or administrative provision before committing resources. This page does not certify structure placement or a complete survival acquisition route.

For a battery-enabled staff, runes are ingredients in its version-specific charging recipe. Follow [Staff batteries and charging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Batteries-and-Charging) to match the required rune types and costs. These stations do not themselves attach a battery or grant the old Runation skill.

## 2. If your pack provides a Rune Post

1. Pick the post matching the rune you want. Fourteen registered post mappings are listed below.
2. Leave the block directly above it non-motion-blocking. A motion-blocking block triggers the blocked-shrine feedback and prevents the inspected conversion path.
3. **Split off only the input you want to spend.** Using a RuneSource submits the entire held stack, not one item. Survival consumes that whole stack immediately; Creative retains it.
4. Wait for the scheduled conversion. Its internal countdown budget is `20 × (3 + floor(output count / 10))` ticks, processed in five-tick steps after an initial scheduled call. This is not a guaranteed wall-clock duration or proof of persistence across unload/restart.
5. Collect the spawned rune item entities above the post. The code sets no pickup delay and no gravity. Setting the thrower does not by itself prove exclusive owner-only pickup.

A stack of 16 Unpowered Runes targets 16 output runes; 16 Charged Runes targets 32. Post type determines which rune, rather than a weighted random pool.

### Batch-size warning: the final stack is calculated from the total

The inspected released task constructs each output stack with `min(64, count)`, while its loop continues until the accumulated spawned count reaches the target. It does not use the remaining count for the final stack.

| Submitted inputs | Intended target | Stack quantities constructed by the inspected loop |
|---|---:|---|
| 32 Charged Runes | 64 | 64 |
| 33 Charged Runes | 66 | 64 + 64 |
| 40 Charged Runes | 80 | 64 + 64 |
| 63 Charged Runes | 126 | 64 + 64 |
| 64 Charged Runes | 128 | 64 + 64 |

This is an exact bytecode-supported arithmetic finding, **not a live-game reproduction or a guarantee that all entities are accepted into the world**. Until the target build is tested, use small batches whose target is at most 64. Restoration work should use the remaining count for the final stack and test conservation at 64, 66, 80, 126 and 128 outputs.

## 3. Understand the Rune Randomizer before spending the last input

Unlike a post, the inspected Randomizer consumes **one** Unpowered or Charged Rune per interaction outside Creative, then asks the `misc/rune_randomizer` loot table for items.

- Charged-input pool: 14 equally weighted rune types.
- Unpowered-input pool: 8 equally weighted rune types.
- Each eligible pool has one base roll; its selected entry produces 1–3 of that rune.
- Both pools have luck-dependent bonus-roll fields. At zero luck this leaves the single base roll. Do not interpret the equal entry weights as an unconditional chance per click when pool conditions may fail.

**Important:** the pool conditions inspect the player's equipped/held items **after** the submitted stack was reduced. They are not given an immutable copy of the submitted input. No equipment slot is specified, so the condition examines all equipment slots, including both hands.

Independent state examples, matching that ordering:

| Before clicking | Equipped state after consumption | Eligible pool conditions |
|---|---|---|
| Last Unpowered Rune, no other rune equipped | Neither type remains | Neither pool |
| 2 Unpowered Runes, no other rune equipped | 1 Unpowered Rune remains | Unpowered |
| Last Charged Rune, no other rune equipped | Neither type remains | Neither pool |
| Last Unpowered Rune, Charged Rune in other hand | Charged Rune remains | Charged |
| 2 Charged Runes, Unpowered Rune in other hand | Both types remain | Both |

These are source/bytecode and independent state-model findings, not an in-game loot test. They explain why a simple “Charged always yields one of fourteen” claim would be misleading. Avoid testing with your last valuable input or a different rune source in your other hand. A corrected implementation should choose the intended pool from the submitted input snapshot, then consume it consistently.

## 4. Recognize the output types

![Fourteen named rune images, marking the eight types in both randomizer input pools](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/rune-output-reference-1.21.1.webp)

| Rune / matching post | Unpowered pool | Charged pool |
|---|:---:|:---:|
| Compass | — | Yes |
| Distortion | — | Yes |
| Energy | Yes | Yes |
| Fire | Yes | Yes |
| Kinetic | — | Yes |
| Life | — | Yes |
| Lunar | — | Yes |
| Poison | Yes | Yes |
| Power | Yes | Yes |
| Storm | — | Yes |
| Strike | Yes | Yes |
| Water | Yes | Yes |
| Wind | Yes | Yes |
| Wither | Yes | Yes |

## Troubleshooting

- **Nothing happens at a post:** verify the input is Unpowered/Charged, clear the block above it, and confirm your pack actually exposes the inspected station implementation.
- **Your full stack disappeared:** whole-stack submission is the inspected post behavior. A Randomizer is a different one-input interaction.
- **No Randomizer reward from the last item:** check the post-consumption equipment condition described above; do not keep feeding valuable items to diagnose it.
- **A new world has no obvious post recipe or structure:** acquisition is unresolved here. A resource browser entry is not a survival guarantee.
- **Runes do not charge your modern staff:** check battery attachment, stored-cast data, capacity and the exact rune-cost set in the [staff charging guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Batteries-and-Charging).

## Evidence and restoration acceptance

[Recipes, selected released method bytes, source hashes and independent cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/rune-production-evidence-1.21.1.json) · [Original illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/rune-art-evidence-1.21.1.json) · [Source findings and repair targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes).

Acceptance still needs actual target-build tests for post acquisition, blocked space, whole-stack consumption, Creative behavior, final-stack conservation, item-spawn rejection, both hands, final Randomizer input, luck, player departure, chunk unload and save/reload. No private Enderloom patch, performance improvement or runtime parity is claimed.

AoA models, textures and systems are by Tslat and contributors. The diagrams and analysis are original documentation work built from pinned official resources; they are not gameplay screenshots.
