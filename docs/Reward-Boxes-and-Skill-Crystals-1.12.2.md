# Historical reward boxes and Skill Crystals

**Minecraft 1.12.2 / AoA 3.3.6.** Inspect the complete contents of Fish Case, Weapons Case, Crystal Box, Gem Bag and Shiny Box, then check exactly which skill a crystal will target. These five resources contain **77 reward entries**.

**[Open the Skill Crystal Planner](https://herbertofury.github.io/Advent-of-Ascension/skill-crystal-planner.html)** to enter displayed levels and inspect the selected target and base XP request. It runs locally in the page and does not read or change game files.

[Historical fishing and Rune/Treasure Boxes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2) · [Foraging and Logging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2) · [Historical Extraction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2) · [Modern boxes and crystals, a separate release](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.21.1)

![Four historical Skill Crystals, their Crystal Box weights and XP divisors](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-crystal-box-rewards-1.12.2.webp)

## Know what you are opening

| Container | Declared base rolls | Entries | Main distinction |
|---|---|---:|---|
| Fish Case | 1, plus bonus-roll range 0–1 | 16 | Cooked fish, count 1–8 per selected entry; some quality values are luck-sensitive |
| Weapons Case | 1 | 12 | Throwable/consumable weapons and ammunition |
| Crystal Box | 1 | 4 | One of four Skill Crystal sizes |
| Gem Bag | 7–15 | 21 | Realm tokens, despite its name |
| Shiny Box | 1–4 | 24 | Minerals and ingots; quality affects selection |

The five selected item handlers use **item-on-block interaction**, call the loot helper once, then shrink one container outside Creative. The shared helper supplies the player and luck. The table itself can make multiple rolls; do not confuse one helper call with one reward item.

Repeated rolls can select the same entry. Base weights are relative selection inputs, not a promise of every reward or an unconditional acquisition percentage. Other mods and data overrides can change the tables or intercept interaction.

Rune Box and Treasure Box use additional Hauling-scaled helper loops and are covered in the [historical fishing guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2#opening-rune-boxes-and-treasure-boxes). Do not apply those loops to these five handlers.

## Skill Crystals: eligible minimum, not lowest skill overall

The server-side crystal right-click selects the **lowest displayed skill level that is at least 15**. It is not a free choice of skill, and it skips skills below 15 rather than raising them to 15.

The selector starts with no target, walks the released skill enumeration and replaces the target only for a **strictly lower** eligible level. Ties therefore keep the first skill in this order:

Alchemy, Anima, Augury, Butchery, Creation, Engineering, Expedition, Extraction, Foraging, Hauling, Hunter, Infusion, Innervation, Logging, Runation.

If the lowest eligible displayed level is at least 1000, or no skill qualifies, it returns no target. In that branch the selected caller sends failure feedback and does not shrink the crystal.

| Example displayed levels | Selected result |
|---|---|
| Every skill at 14 | No target |
| Hauling at 15, all others at 1 | Hauling |
| Anima, Augury and Hunter tied at 15, others at 1 | Anima |
| Logging at 999, all others at 1 | Logging |
| Every skill at 1000 | No target |

**[Try these cases in the planner](https://herbertofury.github.io/Advent-of-Ascension/skill-crystal-planner.html).** Invalid or incomplete levels are rejected rather than silently interpreted as a different character build.

### Crystal size and base XP

| Crystal | Crystal Box base weight | XP divisor |
|---|---:|---:|
| Giant Skill Crystal | 1 | 4 |
| Large Skill Crystal | 4 | 8 |
| Medium Skill Crystal | 13 | 12 |
| Small Skill Crystal | 28 | 15 |

After choosing the target by **displayed** level, the caller requests:

`getXpRequiredForNextLevel(effectiveTargetLevel) / crystalDivisor`

The effective getter caps at 100. A displayed vanity level such as 999 can still be selected, but the request uses effective level 100. Do not describe the result as a fixed fraction of the next vanity level. The planner shows the base request, not final XP after buffs or configuration.

### The fourth XP flag does not guarantee “ignore bonuses”

The crystal passes `false, true` to the two boolean XP arguments. Although the fourth parameter is named `ignoreXpBuffs` in the pinned source, the inspected released XP method does **not read that parameter**. For the natural-XP branch used here, it still goes through the XP-buff path.

The selected buff helper multiplies by the configured global XP modifier, the stored global modifier and a matching skill modifier when present. Do not infer behavior solely from a parameter name or promise crystals ignore all bonuses.

### Skills-disabled configuration deserves care

If an eligible displayed target exists while skills are disabled, the shared XP helper returns without awarding skill XP. The crystal caller can still continue to shrink the item outside Creative. This is a **code-derived consumption test target**, not a reproduced live loss report. Avoid spending valuable crystals while changing skill configuration until the target setup is tested.

With no eligible target, the caller does not shrink the crystal. Creative skips the selected shrink. The method returns an action result labelled PASS even after its server work; that label alone does not prove nothing happened.

The selector includes Augury in its enumeration, but Augury must already have displayed level 15 or higher to qualify. This does not supply the missing below-15 training loop described in the [Ascension Shrine reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Augury-and-Ascension-Shrine-1.12.2).

## Fish Case: cooked fish and luck-sensitive quality

![All sixteen historical Fish Case rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-fish-case-rewards-1.12.2.webp)

The resource requests one base roll with a bonus-roll range of 0–1. The helper supplies player luck, so this is not a fixed guarantee of exactly two rolls. Every selected entry requests 1–8 of its cooked fish. There are no per-entry Hauling level conditions in this selected case table, unlike the raw fishing-catch table.

| Reward | Quantity per selection | Base weight | Quality |
|---|---|---:|---:|
| Fingerfish | 1–8 | 1 | 0 |
| Pearl Stripefish | 1–8 | 1 | 0 |
| Limefish | 1–8 | 1 | 0 |
| Sailback | 1–8 | 1 | 0 |
| Golden Gullfish | 1–8 | 1 | 0 |
| Turquoise Stripefish | 1–8 | 1 | 0 |
| Violet Skipper | 1–8 | 1 | 0 |
| Rocketfish | 1–8 | 1 | 0 |
| Crimson Stripefish | 1–8 | 1 | 0 |
| Crimson Skipper | 1–8 | 1 | 0 |
| Sapphire Strider | 1–8 | 1 | 0 |
| Candlefish | 1–8 | 1 | 1 |
| Dark Hatchetfish | 1–8 | 1 | 1 |
| Ironback | 1–8 | 1 | 1 |
| Rainbowfish | 1–8 | 1 | 1 |
| Razorfish | 1–8 | 1 | 1 |

## Weapons Case: ammunition and consumable weapons

![All twelve historical Weapons Case rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-weapons-case-rewards-1.12.2.webp)

The selected table has one roll and twelve equal-weight entries. It is not a random full-gun catalog. Quantity ranges apply after an entry is selected.

| Reward | Quantity per selection | Base weight | Quality |
|---|---|---:|---:|
| Goo Ball | 5–15 | 1 | 0 |
| Vulkram | 5–15 | 1 | 0 |
| Hellfire | 5–15 | 1 | 0 |
| Chakram | 5–15 | 1 | 0 |
| Slice Star | 5–15 | 1 | 0 |
| Grenade | 5–15 | 1 | 0 |
| Cannonball | 8–40 | 1 | 0 |
| Limonite Bullet | 16–55 | 1 | 0 |
| Metal Slug | 8–40 | 1 | 0 |
| Spreadshot | 5–15 | 1 | 0 |
| Pop Shot | 8–40 | 1 | 0 |
| Holly Arrow | 8–40 | 1 | 0 |

## Gem Bag: realm tokens

![All twenty-one historical Gem Bag token rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-gem-bag-rewards-1.12.2.webp)

The historical Gem Bag requests **7–15 rolls** from 21 equal-weight token entries. Each entry has the ordinary single-item count. Multiple rolls can repeat a token type; opening a bag does not grant one of every realm's token.

| Reward | Quantity per selection | Base weight | Quality |
|---|---|---:|---:|
| Abyss Tokens | 1 | 1 | 0 |
| Baron Tokens | 1 | 1 | 0 |
| Borean Tokens | 1 | 1 | 0 |
| Candyland Tokens | 1 | 1 | 0 |
| Celeve Tokens | 1 | 1 | 0 |
| Creeponia Tokens | 1 | 1 | 0 |
| Crystevia Tokens | 1 | 1 | 0 |
| Deeplands Tokens | 1 | 1 | 0 |
| Dustopia Tokens | 1 | 1 | 0 |
| Gardencia Tokens | 1 | 1 | 0 |
| Greckon Tokens | 1 | 1 | 0 |
| Haven Tokens | 1 | 1 | 0 |
| Iromine Tokens | 1 | 1 | 0 |
| Lelyetia Tokens | 1 | 1 | 0 |
| Lunar Tokens | 1 | 1 | 0 |
| Mysterium Tokens | 1 | 1 | 0 |
| Nether Tokens | 1 | 1 | 0 |
| Precasian Tokens | 1 | 1 | 0 |
| Runandor Tokens | 1 | 1 | 0 |
| Shyrelands Tokens | 1 | 1 | 0 |
| Vox Ponds Tokens | 1 | 1 | 0 |

## Shiny Box: minerals and ingots

![All twenty-four historical Shiny Box material rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-shiny-box-rewards-1.12.2.webp)

The selected resource requests **1–4 rolls**. Its first six entries have weight 50 and no quality adjustment; the remaining eighteen have weight 1 and quality 1. Player luck can therefore affect the relative selection, and these are not 24 equal chances.

| Reward | Quantity per selection | Base weight | Quality |
|---|---|---:|---:|
| Amethyst | 1 | 50 | 0 |
| Jade | 1 | 50 | 0 |
| Limonite Ingot | 1 | 50 | 0 |
| Sapphire | 1 | 50 | 0 |
| Rosite Ingot | 1 | 50 | 0 |
| Rusted Iron Ingot | 1 | 50 | 0 |
| Shyrestone Ingot | 1 | 1 | 1 |
| Crystallite | 1 | 1 | 1 |
| Bloodstone | 1 | 1 | 1 |
| Ornamyte | 1 | 1 | 1 |
| Gemenyte | 1 | 1 | 1 |
| Jewelyte | 1 | 1 | 1 |
| Shyregem | 1 | 1 | 1 |
| Varsium Ingot | 1 | 1 | 1 |
| Mystite Ingot | 1 | 1 | 1 |
| Lyon Ingot | 1 | 1 | 1 |
| Ghoulish Ingot | 1 | 1 | 1 |
| Ghastly Ingot | 1 | 1 | 1 |
| Emberstone Ingot | 1 | 1 | 1 |
| Elecanium Ingot | 1 | 1 | 1 |
| Blazium Ingot | 1 | 1 | 1 |
| Baronyte Ingot | 1 | 1 | 1 |
| Skeletal Ingot | 1 | 1 | 1 |
| Lunar Ingot | 1 | 1 | 1 |

## Useful acquisition links

- [Historical fishing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2#treasure-catches) lists Fish Case, Weapons Case and Crystal Box as conditional treasure entries at Hauling 50, 70 and 94 respectively.
- [Historical Extraction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2#reward-ladder) includes Gem Bag at effective level 80 and Shiny Box at 85.
- [Historical Logging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2#logging-reward-table) includes Gem Bag at effective level 50.

These are checked acquisition references, not an exhaustive list of every chest, trade, command or modpack route. Catch/drop-entry requirements are not automatically minimum opening levels in the selected handlers.

## Restoration and regression checklist

- [ ] Test all five item-on-block handlers, Creative/Survival, full inventory and interaction interception.
- [ ] Verify all 77 reward entries, quantity ranges, base rolls, bonus-roll range and quality under representative luck values.
- [ ] Confirm Crystal Box weights separately from the later crystal's XP divisor.
- [ ] Crystal target selection: below 15, exactly 15, ties, mixed eligible/ineligible skills, 999 and 1000.
- [ ] Keep displayed-level selection separate from effective-level XP calculation; test vanity-level behavior.
- [ ] Verify the fourth XP flag and actual modifier path before documenting “no bonuses.”
- [ ] Skills-disabled state with and without an eligible target; prevent unwanted consumption in a redesigned implementation.
- [ ] Decide deliberately how unavailable skills participate in restored progression; show the selected target before spending valuable items if adding QoL.
- [ ] Dedicated-server handling, one-time payment and bounded work; no repeated full inventory/world scans for a simple selection.

## Evidence and limits

Sixteen selected released methods, four crystal constructor bindings, all five reward resources and the released 15-skill enumeration support this page. Five independent selector examples and the planner's level/size checks are documentation tests, not game tests. All 77 reward entries have exact source-item crops.

- [Released box, crystal and selector evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/legacy-boxes-crystals-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/legacy-boxes-crystals-art-evidence-1.12.2.json)
- [Pinned Skill Crystal source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/item/misc/SkillCrystal.java)
- [Pinned selector source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/utils/player/PlayerUtil.java)
