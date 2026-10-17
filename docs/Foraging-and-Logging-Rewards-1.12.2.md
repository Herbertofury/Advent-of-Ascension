# Historical Foraging and Logging: harvest rewards and XP

**Minecraft 1.12.2 / AoA 3.3.6.** These historical skills add conditional rewards to eligible harvest events. Foraging is not simply modern Mining, and Logging is not a guaranteed multiplier on every log stack.

[Historical first expedition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Anima training and fragments](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) · [Historical Extraction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2)

![All twelve historical Foraging reward entries with levels and XP requests](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/foraging-reward-ladder-1.12.2.webp)

## Start with eligible harvesting

The shared `HarvestDropsEvent` handler returns for a missing harvester or Forge `FakePlayer`. Its skill branches run server-side after the selected special-tool hook. Other mods can still change harvesting, drops, event order and world behavior.

| Skill | Selected block check | What this does not establish |
|---|---|---|
| Foraging | Vanilla Stone, Netherrack, End Stone, or an AoA `StoneBlock` instance | Not every stone-looking block or every ore |
| Logging | A `BlockLog` instance | Not every modded object tagged/named as wood |

The handler's earlier plant branch handles Anima candidates separately. The selected Foraging/Logging branches do not require a named tool or explicitly reject Silk Touch, but the underlying block still has its own harvest behavior. Do not treat material appearance or a tag added by another mod as proof of the Java-class check.

## Foraging: one reward gate, with an extra Netherrack check

Eligible non-Netherrack blocks go directly to the Foraging gate. Netherrack first requires an additional `nextBoolean()` success. A passed gate adds the loot table's results to the harvest event. If the equipment helper reports the **full Foraging set**, it calls that loot table a second time.

That is another roll, not a guaranteed identical item duplicate. The selected handler does not directly grant Foraging XP merely for breaking the block; its reward entries call the XP function described below.

| Effective Foraging level | Ordinary eligible-block gate | Netherrack combined gate |
|---|---|---|
| 1–19 | 1 in 65 | 1 in 130 |
| 20–39 | 1 in 55 | 1 in 110 |
| 40–59 | 1 in 48 | 1 in 96 |
| 60–79 | 1 in 36 | 1 in 72 |
| 80–100 | 1 in 29 | 1 in 58 |

These are random gate probabilities under the selected branches. They are **not the probability of receiving a particular item**, nor a guarantee that downstream harvest processing will retain and spawn every returned drop.

### Foraging reward table

The table has one pool, one roll and twelve item entries. Quantities are declared ranges; the XP column is the base request from that entry's `aoa3:grant_xp` function.

| Reward | Required effective level | Quantity | Base weight | Quality | Skill XP request |
|---|---:|---|---:|---:|---:|
| Coal | None | 1–3 | 100 | 0 | 20 |
| Scrap Metal | None | 1 | 100 | 0 | 20 |
| Gold Nugget | None | 1–2 | 100 | 0 | 20 |
| Ender Pearl | 15 | 1–2 | 100 | 0 | 100 |
| Gunpowder | 20 | 1–16 | 100 | 0 | 150 |
| Iron Ingot | 35 | 1–3 | 100 | 0 | 650 |
| Experience Bottle | 50 | 1–4 | 100 | 0 | 1000 |
| Diamond | 65 | 1–2 | 100 | 0 | 3550 |
| Small Skill Crystal | 70 | 1–2 | 100 | 0 | 4000 |
| Rosite Ingot | 85 | 1 | 100 | 0 | 10100 |
| Gold Coin | 90 | 1 | 100 | 0 | 19800 |
| Occult Pickaxe | 90 | 1 | 10 | 5 | 30000 |

## Logging: the passed gate splits into two branches

Once the Logging gate passes, a separate `nextBoolean()` chooses:

- **Loot-table branch:** adds one table result; the full Logging set adds a second table call.
- **Log-copy branch:** searches the current drop list for the first stack whose item equals the harvested log block's item. If found, copies it and sets the additional stack count to one, or **two only when effective level is greater than 50**. It also requests Logging XP using `(float) pow(level, 1.65) × 3`.

If no matching log item exists in the drop list, the selected copy branch does not add a replacement and does not make that XP request. It is not “double every stack,” and the full set does not add another copy operation in this branch. The copied stack is based on the first matching item's data; the code does not multiply its original count.

| Effective Logging level | Gate | Loot branch after both rolls | Copy branch after both rolls |
|---|---|---|---|
| 1–19 | 1 in 25 | 1 in 50 | 1 in 50 |
| 20–39 | 1 in 20 | 1 in 40 | 1 in 40 |
| 40–59 | 1 in 16 | 1 in 32 | 1 in 32 |
| 60–79 | 1 in 12 | 1 in 24 | 1 in 24 |
| 80–100 | 1 in 9 | 1 in 18 | 1 in 18 |

At level **50**, the copy count is still one. It becomes two at **51**. These branch probabilities still precede matching-drop requirements or weighted table selection.

![All nine historical Logging reward entries and the separate log-copy branch](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/logging-reward-ladder-1.12.2.webp)

### Logging reward table

The table has one pool, one roll and nine item entries. Fragmented Anima Stone appears here at effective Logging **40**, earlier than its historical Extraction level-60 entry. It remains a conditional weighted reward, not a guaranteed fragment per log.

| Reward | Required effective level | Quantity | Base weight | Quality | Skill XP request |
|---|---:|---|---:|---:|---:|
| Stick | None | 1–16 | 100 | 0 | 15 |
| Apple | None | 1–4 | 100 | 0 | 25 |
| Tea Seeds | 10 | 1–2 | 100 | 0 | 40 |
| Experience Bottle | 20 | 3–9 | 100 | 0 | 90 |
| Fragmented Anima Stone | 40 | 1–2 | 100 | 0 | 360 |
| Gem Bag | 50 | 1–3 | 100 | 0 | 500 |
| Medium Skill Crystal | 90 | 1–2 | 100 | 0 | 6200 |
| Rosite Ingot | 95 | 1 | 100 | 0 | 9500 |
| Occult Axe | 95 | 1 | 10 | 0 | 15000 |

## XP belongs to the selected reward or copy branch

The `aoa3:grant_xp` function reads the context's player and calls the shared skill-XP helper with the entry's configured amount. It returns the item stack unchanged. A count range such as 1–3 Coal does not itself multiply the function's XP field: the listed value is the request from that function invocation.

Both tables have a `killed_by_player` pool condition. This name does **not** mean you must kill a creature while mining or logging. The released AoA helper supplies the player to the loot-context builder. The checked vanilla condition tests that context player field, and the vanilla serializer defaults its inverse flag to false. The selected builder, constructor, getter and condition methods are retained in the evidence.

Neither table contains an explicit empty entry, but eligibility, luck, later event processing and modpack overrides remain separate from the displayed weights. Occult Pickaxe has base weight 10 and quality 5; Occult Axe has weight 10 with no quality field in the selected table. Do not turn all weights into fixed percentages or assume the two tools share the same luck adjustment.

The full-set armor callbacks add/remove a **0.3 modifier for their matching skill's XP** and declare level 100 as their requirement. This modifier is separate from the extra table call. The effective-level getter caps at 100, while higher displayed vanity levels are stored separately; skills-disabled configuration and XP helpers can change observed training.

## Pluton tribute differs between the two skills

Both selected branches request `11 − effectiveLevel / 10`, with integer division:

| Effective level examples | Base tribute request |
|---|---:|
| 1–9 | 11 |
| 10–19 | 10 |
| 50–59 | 6 |
| 90–99 | 2 |
| 100 | 1 |

- **Foraging:** the request is inside the passed loot-gate branch and requires **dimension 0 and daytime**.
- **Logging:** the request follows either passed-gate branch and requires **dimension 0**, with no matching daytime check in this selected branch. It can be reached even when the copy branch found no matching log stack.

These are requested deltas. Shared deity helpers, equipment and configuration can affect the final stored tribute; do not promise these exact final gains in every setup.

## Practical training plan

1. Choose the correct historical release and use naturally appropriate blocks: ordinary eligible stone for Foraging, actual log-class blocks for Logging.
2. Expect many harvests with no bonus. Compare the gate table before assuming the feature is broken.
3. For a specific reward, check its level condition as well as the gate. A Diamond requires Foraging 65; a Logging Gem Bag requires Logging 50.
4. For Anima fragments, compare Logging 40 and Extraction 60 with your available materials and skill progress. The routes have different gates, costs and loot pools.
5. Keep ordinary harvest drops available when investigating Logging's copy branch; a mod that replaces or removes the log-item drop can change its result.
6. At full-set unlock, test extra table calls and XP modifiers separately. Do not infer identical output stacks from “another roll.”

This is a source-based preparation route, not a benchmark establishing the fastest XP farm in your modpack.

## Restoration checklist

- [ ] Real player versus missing harvester/FakePlayer; custom harvest tools and server/client branches.
- [ ] Each eligible stone/log class, a visually similar ineligible block, and Netherrack's additional gate.
- [ ] Gate thresholds at levels 19/20, 39/40, 59/60 and 79/80.
- [ ] Logging copy at 50/51; no matching log drop, multiple matching stacks and modded metadata/NBT.
- [ ] Full/partial armor: separate the second table invocation from XP modifiers and from log-copy behavior.
- [ ] Loot condition context, selected entry quantity, XP-function invocation and luck-sensitive quality.
- [ ] Pluton day/night and dimension differences, skill configuration and shared tribute modifiers.
- [ ] Harvest cancellation and downstream drop changes; avoid awarding duplicate XP when restoring hooks.
- [ ] Dedicated-server correctness and profiling before claiming compatibility or zero performance impact.

## Evidence

This page uses **16 selected AoA methods, six vanilla loot-context/condition methods, two complete reward resources and 100 independent gate/threshold model rows**. All 21 reward entries have exact historical image crops. No Minecraft, server or mod was executed.

- [Released method, loot and gate evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/foraging-logging-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/foraging-logging-art-evidence-1.12.2.json)
- [Pinned upstream harvest handler](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/event/PlayerEvents.java)
- [Foraging utility](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/utils/skills/ForagingUtil.java)
- [Logging utility](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/utils/skills/LoggingUtil.java)
