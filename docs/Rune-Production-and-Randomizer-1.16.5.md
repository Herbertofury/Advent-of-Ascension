# Rune Production and Randomizer Handbook · 1.16.5

**AoA 3.6.11 / Minecraft 1.16.5.** Historical workflow only; do not substitute this for modern staff batteries or assume the same mechanics in newer releases.

![Fourteen Rune Posts and their outputs](https://herbertofury.github.io/Advent-of-Ascension/previews/rune-post-output-guide-1.16.5.webp)

## Make the input runes

| Released crafting recipe | Result |
|---|---|
| 1 Runium Chunk, shapeless | 16 Unpowered Runes |
| 1 Charged Runium Chunk, shapeless | 16 Charged Runes |

[Unpowered Rune recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=unpowered_rune) · [Charged Rune recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=charged_rune). These are the actual bundled recipe outputs, not guessed ratios.

## Choose a specific rune with a Rune Post

1. Locate the post for the rune you want. The table below is the source registration mapping; it is not a claim that every post has a crafting recipe.
2. Keep the block immediately above the post free of material that blocks motion. This is the checked obstruction rule; it is not a requirement for an entirely empty column.
3. Split your input stack to the amount you intend to spend. **Outside Creative, a successful use consumes the entire held RuneSource stack.**
4. Use that stack on the post. Unpowered Rune has generation factor 1; Charged Rune has factor 2. The requested output is stack size multiplied by the factor.
5. Wait for the scheduled particle/output sequence. The source ticker starts at `20 × (3 + floor(requested_count / 10))` and decreases in five-tick steps. This is tick scheduling, not a measured real-time duration.
6. The task creates owner-associated item entities above the post, with no pickup delay and no gravity. Runtime pickup rules and server performance still apply.

### Output mappings

| Post | Output |
|---|---|
| [Compass Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:compass_rune_post) | [Compass Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:compass_rune) |
| [Distortion Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:distortion_rune_post) | [Distortion Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:distortion_rune) |
| [Energy Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:energy_rune_post) | [Energy Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:energy_rune) |
| [Fire Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:fire_rune_post) | [Fire Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:fire_rune) |
| [Kinetic Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:kinetic_rune_post) | [Kinetic Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:kinetic_rune) |
| [Life Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:life_rune_post) | [Life Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:life_rune) |
| [Lunar Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:lunar_rune_post) | [Lunar Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:lunar_rune) |
| [Poison Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:poison_rune_post) | [Poison Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:poison_rune) |
| [Power Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:power_rune_post) | [Power Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:power_rune) |
| [Storm Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:storm_rune_post) | [Storm Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:storm_rune) |
| [Strike Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:strike_rune_post) | [Strike Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:strike_rune) |
| [Water Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:water_rune_post) | [Water Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:water_rune) |
| [Wind Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:wind_rune_post) | [Wind Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:wind_rune) |
| [Wither Rune Post](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3:wither_rune_post) | [Wither Rune](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=aoa3:wither_rune) |

## Use the Rune Randomizer carefully

The randomizer accepts Unpowered or Charged Rune and consumes **one** outside Creative, unlike the post’s full-stack use. Its loot table then selects conditional pools by what the player is holding.

| Pool | Matching held item | Candidate rune types | Bundled count provider |
|---|---|
| powered_runes | Charged Rune | Compass, Distortion, Energy, Fire, Kinetic, Life, Lunar, Poison, Power, Storm, Strike, Water, Wind, Wither | Uniform 1–3 per selected entry |
| unpowered_runes | Unpowered Rune | Energy, Fire, Poison, Power, Strike, Water, Wind, Wither | Uniform 1–3 per selected entry |

All listed entry weights are 100. The unpowered pool declares bonus rolls, but this call builds its gift context with luck 0. The conditions have no fixed hand field: the HoldingItem implementation checks both hand slots. Do not read the table as an unconditional guaranteed result from every click.

## Two issues to preserve in the Enderloom backlog

### 1. Output stack remainder bug

The released `RuneCreationTask.run` bytecode supplies the total requested count to `Math.min(64, count)` for **each** emitted stack. It does not subtract the amount already emitted. For a requested count of 66, the loop constructs 64 + 64 rather than 64 + 2. This is reachable in the normal arithmetic with 33 Charged Runes.

The standalone regression harness checks counts 1–128 against a proposed remainder-aware loop. This proves the arithmetic difference and matches the released operands; it is not an in-game reproduction or an applied mod fix.

- [ ] Use the remaining quantity for each stack: `min(max_stack_size, requested - emitted)`.
- [ ] Test boundary counts 1, 32, 63, 64, 65, 66, 127 and 128; the normal charged-input cases include 64, 66, 126 and 128.
- [ ] Check output conservation, stack-size limits, owner assignment and scheduled cancellation/lifecycle behavior in-game.

### 2. Randomizer consumes before its loot condition checks the hands

The released method shrinks the input before generating loot. The loot condition then reads the current hands. Consuming the last matching rune can leave no matching held rune for its pool; holding different rune types in both hands can also make selection depend on both hands rather than only the consumed item. These are source/artifact-backed regression risks, with runtime reproduction still pending.

- [ ] Capture the consumed input identity before shrinking the stack, and use it explicitly to choose the intended pool.
- [ ] Test single-item and multi-item stacks, both interaction hands, matching and differing offhand items, and Creative versus Survival.
- [ ] Check that a successful consumption yields the intended result exactly once and that both pools cannot activate accidentally.
- [ ] Avoid treating a remainder or mixed-hand quirk as intended balancing when porting the mechanic.

## Troubleshooting

- **Post reports blocked:** inspect the material of the block directly above it.
- **Wrong rune:** check the post’s output mapping, not just its appearance.
- **Whole stack vanished:** that is the post’s explicit non-Creative consumption path. Split inputs first.
- **Unexpected output total above 64:** use the remainder regression target above; do not silently document the inflated amount as the intended conversion rate.
- **Randomizer spent the last rune without the expected result:** preserve the exact hand contents, game mode and input count for the consume-before-condition test.

## Evidence

[Source hashes, released method bytes, loot/recipe JSON and 128 arithmetic cases](https://herbertofury.github.io/Advent-of-Ascension/rune-workflow-audit-1.16.5.json). Source registrations identify 14 posts. The artifact checks explicitly verify the Math.min operand sequence and shrink-before-loot call order. No game code was executed or modified.

Related: [Historical realmstone progression](Realmstone-Progression-Walkthrough-1.16.5) · [Modern staff batteries](Staff-Batteries-and-Charging) · [Recipe Explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5).
