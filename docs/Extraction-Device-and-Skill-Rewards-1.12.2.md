# Historical Extraction: lava, bowls and skill rewards

**Minecraft 1.12.2 / AoA 3.3.6.** This is the historical lava-powered Extraction Device loop. Do not substitute the modern skill's qualifying-block and smelting rules. The walkthrough is based on selected released classes and recipes; live-game restoration acceptance remains separate.

[Historical first expedition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Modern skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) · [Armor acquisition across releases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Across-Versions)

![Historical Extraction Device setup, filled state and two bowls](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/extraction-device-workflow-1.12.2.webp)

## Craft the device and a bowl

The recipe links show the exact historical grids with item images. Stone Bowl uses **Ancient Rock**, not ordinary stone or cobblestone.

| Output | Exact shaped recipe ingredients | Open illustrated recipe |
|---|---|---|
| Extraction Device | 6 Stone Bricks (metadata 0), 1 Iron Trapdoor, 1 Glass, 1 Hopper | [Recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aextraction_device) |
| Stone Bowl | 7 Ancient Rock, 1 Gold Ingot | [Recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Astone_bowl) |
| Diamond Bowl | 7 Diamonds, 1 Gold Ingot | [Recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Adiamond_bowl) |

The device grid places Stone Bricks down both outside columns, then Iron Trapdoor / Glass / Hopper down the center. Each bowl recipe leaves the top-center slot empty, puts Gold Ingot in the center and fills the other seven positions with its named material.

The released Stone Bowl registration supplies **100 base durability**; Diamond Bowl supplies **750**. Both are instances of `InfusionBowl`, which the device checks. The Diamond Bowl's Pixon harvest amount and harvest-level modifier are not called by this device interaction: do not promise extra Extraction loot rolls from those values.

## Build one safe extraction cycle

1. Place the empty Extraction Device with **replaceable space directly below it**, inside ordinary build bounds. Do not fill that space with a solid floor block.
2. Put a **lava source directly above** the device. The selected update and neighbor-change paths accept vanilla lava/flowing-lava block classes only when their metadata is zero. Non-source flowing lava does not pass that check.
3. On the server, the eligible empty device changes to its filled variant and removes the lava block above. The lava is consumed at this fill step; it is not an endlessly reusable source.
4. Use a Stone or Diamond Bowl on the filled device. A valid cycle changes it back to empty **before** the success roll.
5. Unless the equipment helper reports the full Extraction armor set, the cycle also requests **Obsidian directly below**. Clear that obstruction before another ordinary cycle. Full Extraction armor suppresses this placement, but does not skip the initial space check.
6. Refill with a new lava source and repeat as desired. Keep lava enclosed away from valuable builds and creatures.

The selected block drop returns the empty Extraction Device, and its silk-harvest override returns false. Do not assume breaking a filled device preserves its stored lava.

## Know which outcome spends what

| Outcome | Device / lava | Bowl wear | XP and loot |
|---|---|---|---|
| Empty device | No cycle starts | None in selected branch | None |
| Filled device, wrong item | No extraction branch | None | None |
| Filled device, bowl, blocked space below | Filled state retained by selected branch | None | No-space feedback |
| Valid cycle, success gate fails | Device already emptied; stored lava spent; ordinary Obsidian placement already requested | No selected durability call | No selected XP or loot call |
| Valid cycle, success gate passes | Device emptied; same ordinary Obsidian placement behavior | Requests 1 durability damage outside Creative | One loot-table roll and skill XP request |

**Passing the gate is not a guaranteed item.** The loot pool contains an empty result. Bowl wear and XP occur in the success branch even when its loot selection produces no useful item. The selected device method does not multiply the pool rolls for the Diamond Bowl.

The space test also accepts an out-of-build-height position through an OR branch. That is a restoration test target, not recommended setup: the later block writes are not checked for success by this method. Use a normal, clear position and test failure recovery in a copied world before automating or porting the system.

## Success chance uses integer division

The released gate compares an integer roll from 0 through 99 against:

`pow((102 - effectiveLevel) / 6, 1.34)`

The division happens as **integer division before exponentiation**. The following exact passing-roll counts come from enumerating all 100 possible rolls in an independent model, not measured gameplay:

| Effective Extraction level | Passing rolls out of 100 |
|---:|---:|
| 1 | 58 |
| 5 | 58 |
| 10 | 62 |
| 25 | 72 |
| 50 | 83 |
| 75 | 93 |
| 90 | 97 |
| 95 | 99 |
| 96 | 99 |
| 97 | 100 |
| 100 | 100 |

The ordinary `getLevel` helper caps effective level at **100**. Higher display/vanity levels do not feed a negative base into this caller's power expression. When skills are disabled, the helper returns 100; the XP helper then returns without granting XP. That configuration difference is important when comparing tests.

At effective level 97 the success gate passes all 100 rolls, but the separate loot pool still has an empty entry. Do not advertise “guaranteed loot at 97.”

## Reward ladder

![All historical Extraction reward entries with their level conditions and weights](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/extraction-reward-ladder-1.12.2.webp)

The released table has **one pool, one roll, 23 entries**: 22 item entries and an empty entry. Level conditions use the player's effective Extraction level. Quantities below are the table's declared count ranges; entries with no count function use the ordinary single-item default.

| Reward | Minimum effective level | Quantity | Base weight | Quality |
|---|---:|---|---:|---:|
| Empty result | None | — | 100 | 0 |
| Coal | None | 1–4 | 100 | 0 |
| Flint | None | 1–4 | 100 | 0 |
| Holly Arrow | 5 | 3–9 | 100 | 0 |
| Blaze Powder | 10 | 1–4 | 100 | 0 |
| Limonite Ingot | 15 | 1–3 | 100 | 0 |
| Bone | 20 | 3–10 | 100 | 0 |
| Silver Coin | 25 | 1–2 | 100 | 0 |
| Emerald | 30 | 1 | 100 | 0 |
| Experience Bottle | 35 | 1–5 | 100 | 0 |
| Rosite Ingot | 40 | 1 | 100 | 0 |
| Blaze Rod | 45 | 1–4 | 100 | 0 |
| Limonite Bullet | 50 | 1–32 | 100 | 0 |
| Ink Sac | 55 | 1–10 | 100 | 0 |
| Fragmented Anima Stone | 60 | 1–4 | 100 | 0 |
| Magma Cream | 65 | 2–6 | 100 | 0 |
| Grenade | 70 | 1–8 | 100 | 0 |
| Diamond | 75 | 1–2 | 100 | 0 |
| Gem Bag | 80 | 1–2 | 100 | 0 |
| Shiny Box | 85 | 1–2 | 100 | 0 |
| Gold Coin | 90 | 1 | 100 | 0 |
| Magic Repair Dust | 95 | 1 | 100 | 0 |
| Occult Shovel | 95 | 1 | 10 | 5 |

Ink Sac is the historical `minecraft:dye` entry with data 0; it is not a generic promise of every dye color. Occult Shovel has weight 10 and quality 5, while the other selected entries have weight 100. The loot context supplies the player and luck. These values are **not unconditional percentages**, and newly eligible entries change the available selection pool.

## XP, armor and deity tribute

For a passed success gate, the device requests:

`getXpRequiredForNextLevel(effectiveLevel) / denominator(effectiveLevel)`

| Effective level | Denominator |
|---|---:|
| 1–2 | 5 |
| 3–8 | 10 |
| 9–16 | 20 |
| 17–25 | 35 |
| 26–40 | 60 |
| 41–60 | 90 |
| 61–75 | 150 |
| 76–98 | 300 |
| 99–100 | 500 |

This is a base XP request, not a promise of exactly that many cycles per displayed level. The XP helper applies modifiers and uses separate stored-level progression. Extraction armor declares a level-100 requirement; its full-set buff callback adds a **0.3 Extraction XP modifier**, removed by the corresponding removal callback. The device separately consults the full-set identity to suppress Obsidian placement. Equipment enforcement and final modifier composition need their own runtime checks.

In dimension 0, the success branch requests **+4 Pluton tribute**. Other helper/configuration effects can modify the final tribute result; this is not a universal +4 in every dimension.

## Troubleshooting

- **“No space”**: inspect the block directly below. Ordinary extraction can put Obsidian there after each valid cycle.
- **Lava flows past but the device stays empty**: check the block immediately above and whether it is actually source metadata 0.
- **The device emptied but I received nothing**: distinguish a failed success roll from the loot pool's empty entry. Lava expenditure precedes the roll.
- **Diamond Bowl did not increase rewards**: its extra Pixon harvesting parameters are a separate interaction path.
- **A level over 100 did not improve the gate**: the effective skill getter caps at 100 even when the display level is higher.
- **Creative behavior looks different**: bowl durability is skipped, but the selected world-state cycle is not skipped merely because the player is Creative.
- **Breaking the device lost its filled state**: the selected drop is the empty device and silk harvesting is disabled.

## Restoration checklist

- [ ] Empty/filled variants, source versus non-source lava, both hands and both bowl types.
- [ ] Blocked, replaceable and out-of-height space below; check every world-write result and recovery policy.
- [ ] Success/failure/empty-loot outcomes with inventory full and bowl nearly broken.
- [ ] Survival/Creative, skills enabled/disabled, effective versus vanity levels and XP modifiers.
- [ ] Full Extraction set, partial set and equipment changes; verify no stale XP modifier.
- [ ] Dedicated-server interactions and simultaneous attempts against one filled device.
- [ ] Save/reload the filled state and preserve stable block/item identifiers in any port.

## Evidence and limits

Nineteen selected released methods, two bowl constructor bindings, three recipe resources and the complete Extraction loot resource support this page. The arithmetic model enumerates 100 rolls for each effective level 1–100. Image crops retain their exact release-specific atlas provenance. No game or mod code was executed, and this page does not claim the Enderloom restoration is complete.

- [Released-method, recipe, loot and arithmetic evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/extraction-device-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/extraction-device-art-evidence-1.12.2.json)
- [Pinned upstream Extraction Device](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/block/functional/utility/ExtractionDevice.java)
- [Pinned upstream Extraction utilities](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/utils/skills/ExtractionUtil.java)
