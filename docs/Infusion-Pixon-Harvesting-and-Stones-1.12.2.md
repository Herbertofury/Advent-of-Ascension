[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.12.2) · [Skills](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Extraction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2)

# Infusion: Pixon harvesting and stone conversion

> **Historical guide: Minecraft 1.12.2 / AoA 3.3.6.** The bowl, harvest tables and conversion rules below were checked in the released JAR. They are not the modern 1.21.1 Infusion Table system or proof that an Enderloom restoration has passed game tests.

## The short route

1. Craft a **Stone Bowl** with seven Ancient Rock and one Gold Ingot. It can harvest a Glistening Pixon from Infusion level 1.
2. Look for the **green particle creature** in a suitable Overworld biome. Use the bowl on the Pixon; hitting it with a weapon is not the intended harvest action.
3. Each completed harvest iteration selects an Infusion Stone or rarer Power Stone and requests the associated Infusion XP. Keep your early Glistening Infusion Stones: their separate table-conversion requirement is level 5.
4. Craft an **Infusion Table** with three wool, two Ancient Rock, one ingredient accepted by the infusionStone ore-dictionary entry, and three obsidian. The green stone in the diagram is an example of that ingredient.
5. Once you meet the stone conversion level, use a held stack of Infusion Stones directly on the table. **The whole held stack is processed in one action.** Split it first if you only want to spend a few.
6. Save Power Stones for the historical table’s crafting recipes. Use the table with a different held item or an empty hand to open its crafting interface.

### Craft the starter kit

![Exact historical Stone Bowl, Diamond Bowl and Infusion Table recipes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infusion-starter-recipes-1.12.2.webp)

| Tool | Base durability | Maximum iterations per accepted use | Added Pixon level requirement |
|---|---:|---:|---:|
| [Stone Bowl](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.StoneBowl.name) | 100 | 1 | +0 |
| [Diamond Bowl](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DiamondBowl.name) | 750 | 5 | +10 |

The Diamond Bowl is a faster batch tool, but it adds ten to the harvesting requirement and wears once per iteration. It does not guarantee five rewards if the Pixon runs out of health. These bowl parameters do not give extra rolls in the separate [Extraction Device](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2).

## Identify the Pixon and plan the journey

![Eight historical Pixon particle colors shown with their source atlas cells](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infusion-pixon-particle-references-1.12.2.webp)

These are exact released sprite cells with bootstrap-linked renderer colors. The game uses particle effects instead of a solid creature body. The reference sheet deliberately does not invent a 3D mesh or pretend to reproduce randomized brightness, size, motion or lifetime.

| Pixon | Released spawn-entry biome fields / context | Stone Bowl level | Diamond Bowl level |
|---|---|---:|---:|
| [Glistening Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglistening_pixon) | Overworld pool; pinned-source generic-biome selector | 1 | 11 |
| [Gleaming Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agleaming_pixon) | Runandor | 10 | 20 |
| [Ambient Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aambient_pixon) | Haven, Runandor, Candyland, Shyrelands | 20 | 30 |
| [Glaring Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglaring_pixon) | Lelyetia | 25 | 35 |
| [Glowing Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglowing_pixon) | Lborean | 40 | 50 |
| [Shining Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashining_pixon) | Abyss | 60 | 70 |
| [Radiant Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aradiant_pixon) | Dustopia | 72 | 82 |
| [Blooming Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ablooming_pixon) | Mysterium | 81 | 91 |

**Spawn declarations are not guaranteed encounter locations.** Configuration, biome eligibility and placement checks still apply. The released Glistening override requires dimension 0. The shared Pixon check rejects flat worlds and compares the block state at the entity position with the biome’s top block before calling its spawn permission check. That placement detail deserves a game test; this guide does not silently replace it with a more convenient “block underneath” rule.

The released ordinary spawn entries use weight 12 for the seven dimensional types, and weight 30 for Glistening in the inspected Overworld entry. Declared group bounds are 1–3 except Shining’s 1–1. These are pool inputs, not a probability of finding one per chunk. Ambient explicitly lists Haven, Runandor, Candyland and Shyrelands.

## Harvest rewards and XP

![Sixteen Pixon harvest rewards with separate harvesting and conversion values](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/infusion-pixon-rewards-1.12.2.webp)

Each of the eight selected harvest tables has one pool roll: its Infusion Stone has weight 30 and its Power Stone has weight 1, with no quality modifier or empty entry in these stock resources. Thus, conditional on a call to the unchanged selected table, the two weights divide the selection 30:1. This is not an overall natural-spawn or per-minute yield.

| Pixon | Infusion Stone harvest XP request | Power Stone harvest XP request | Convert stone from level | Conversion base XP per stone |
|---|---:|---:|---:|---:|
| Glistening Pixon | 10 | 15 | 5 | 8 |
| Gleaming Pixon | 30 | 45 | 15 | 16 |
| Ambient Pixon | 40 | 60 | 20 | 20 |
| Glaring Pixon | 70 | 105 | 30 | 40 |
| Glowing Pixon | 200 | 300 | 45 | 85 |
| Shining Pixon | 350 | 525 | 60 | 150 |
| Radiant Pixon | 700 | 60 | 70 | 220 |
| Blooming Pixon | 900 | 1350 | 80 | 300 |

**Radiant exception:** its Power Stone entry requests **60 XP**, while the paired Infusion Stone entry requests **700 XP**. Those are the actual selected resource values. Do not “correct” the smaller number to match the other tiers without an explicit design decision and tests.

Harvest XP comes from the selected loot function; conversion XP is a different later action. Final XP may change through configuration and skill modifiers. Do not add the two amounts unless both actions actually happen.

### What happens during one use?

- The server checks positive Pixon health, the shared next-harvest tick, the held bowl type, and the Pixon requirement plus the bowl modifier. Creative bypasses the level check.
- Every iteration wears the bowl by one outside Creative, generates the harvest table once, and reduces Pixon health by `7 − nextInt(6)`: **2–7 health**, rather than a fixed seven.
- A recognized full Infusion armor set makes a **second independent table call per iteration**. That is a second selection, not a clone of the first reward. Its XP function is evaluated too.
- The shared base attribute setup chooses maximum health `15 + nextInt(30)`, or **15–44** before other modifications. The batch loop stops when health is no longer positive.
- If the Pixon survives the interaction path, its next eligible tick becomes current world time plus **8–39 ticks**. At a healthy 20 ticks/second that corresponds to 0.4–1.95 seconds, not a guaranteed real-time delay under lag.
- The cooldown update also follows the insufficient-level branch. Repeatedly clicking below the requirement is not a way to bypass the gate.
- Successful Overworld daytime harvesting requests Luxon tribute equal to **4 × completed iterations**. Two armor rolls do not double the iteration count.

## Converting a held stack safely

The table uses the stone’s own conversion level, which can differ from its Pixon’s harvesting level. Glistening can be harvested at level 1 but converted from level 5; Radiant conversion unlocks at 70 although harvesting that Pixon requires 72 with the Stone Bowl.

For an eligible stack of N Infusion Stones:

1. Request `stone base XP × N` Infusion XP.
2. Roll once per input stone for a Power Stone: **1 in 100** ordinarily, or **1 in 33** with a recognized full Infusion set.
3. Outside Creative, replace the entire held stack with the successful Power Stones, or empty the hand if none succeeded. Zero Power Stones does not mean the conversion failed to spend the input.

For example, 64 eligible Glistening Infusion Stones request 512 base XP. Their expected ordinary Power Stone count is 0.64, but the actual count can be zero or another result. It is not a guaranteed one-for-one upgrade. Creative retains its held input and routes the generated result through the item-give helper.

Holding an Infusion Stone below its conversion level does not open the crafting GUI in this branch. Switch to an empty hand or another item if you meant to craft instead.

The skill armor declares level 100 and a 0.3 Infusion XP modifier when its full-set callback is active. The extra harvest call and changed conversion denominator are separate effects from that XP modifier.

## Troubleshooting and restoration tests

| Symptom / case | What to check |
|---|---|
| Bowl does nothing | Correct item, server-side interaction, positive Pixon health, cooldown, and the bowl-adjusted level gate |
| Diamond Bowl works on fewer tiers than expected | Its additional requirement is +10; it does not remove the tier gate |
| Stones disappear with no Power Stone | Whole-stack conversion consumes eligible inputs even when every 1-in-100 or 1-in-33 roll misses |
| Green stone cannot convert at level 1 | Harvesting and conversion have distinct thresholds; keep training through harvest XP until 5 |
| No table crafting screen | An Infusion Stone routes to conversion first; use another held item or empty hand |
| Blank solid-mob preview | Pixons use particles; use the color/sprite reference instead of a fabricated model |
| Bowl breaks during a Diamond batch | The selected loop does not re-check stack emptiness after wear; test this boundary before claiming perfect durability behavior |
| Multiplayer harvesting or restart | Cooldown is entity-shared in the selected field; verify competing users, serialization and tick continuity in game |
| Disabled skills | Shared level and XP configuration handling can differ; verify consumption, feedback and rewards before using valuable stacks |

### Maintainer acceptance checklist

- [ ] Test level just below / exactly at each of the sixteen bowl-adjusted requirements.
- [ ] Verify cooldown after successful and rejected use; confirm no duplicate client/server rewards.
- [ ] Test health 1–7 with Diamond batches, Creative, armor, and a bowl with one durability remaining.
- [ ] Test conversion at each threshold with stack sizes 1, 2 and 64, both hands, Creative and no successful Power Stone rolls.
- [ ] Confirm Infusion armor recognition, two independent harvest rolls, XP modifiers and 1-in-33 conversion behavior.
- [ ] Reproduce Radiant’s unusual XP values and decide deliberately whether a restoration preserves or changes them.
- [ ] Test spawn placement, flat-world behavior, configuration and all declared dimensional biome entries.
- [ ] Validate renderer effects in the real client without treating the static sprite reference as parity proof.

## Sources and exact scope

[Released method/resource evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/infusion-harvesting-evidence-1.12.2.json) · [Renderer and sprite evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pixon-visual-evidence-1.12.2.json) · [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/infusion-harvesting-art-evidence-1.12.2.json)

35 selected released gameplay methods, ten item constructor bindings, eight spawn constructor windows, eight complete harvest tables, three exact recipes and 264 independent health-step checks support this guide. Eight released renderer factories and six rendering/particle methods support the sprite reference. Static analysis does not replace game acceptance.

[Pinned official source](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source) provides readable context; the selected released binary and resources determine the values above. AoA: Tslat and contributors. Vanilla recipe assets: Mojang. Original documentation and diagrams for this repository.

[Modern 1.21.1 Infusion Table crafting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1) · [Historical fishing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2) · [Skill Crystal planner](https://herbertofury.github.io/Advent-of-Ascension/skill-crystal-planner.html) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
