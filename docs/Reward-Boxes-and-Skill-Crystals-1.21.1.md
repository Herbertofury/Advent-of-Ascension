# Reward boxes and Skill Crystals · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** Rune Boxes, Shiny Boxes, Crystal Boxes, Gem Bags and Treasure Boxes have different reward tables. This guide shows all **53 entries across the five tables**, explains rolls versus item counts, and helps you use Skill Crystals without mistaking their level threshold.

![Five reward containers and their different numbers of reward types](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reward-box-overview-1.21.1.webp)

[Fishing Cage guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Cage-Walkthrough-1.21.1) · [Skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) · [Loot Reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Loot-Tables-and-Global-Modifiers-1.21.1)

## Open a box safely

1. Make room in your inventory and stand somewhere dropped overflow can be collected safely.
2. Hold the box and use it. The server generates the matching gift-table loot and gives it through AoA's inventory helper.
3. Outside Creative, the checked box-use methods consume **one box**, not the whole held stack.
4. Inspect the result before opening more. Random rolls can repeat the same reward; a panel of possible items does not mean the box gives every pictured item.

The inventory helper attempts insertion and can drop overflow. This is not guaranteed protected storage in a full inventory. These are in-game items, and this guide concerns their shipped game rules only.

## Where the inspected resources reference them

- **Rune Box and Shiny Box:** both occur in the checked [Fishing Cage catch table](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Cage-Walkthrough-1.21.1).
- **Crystal Box, Gem Bag and Treasure Box:** referenced by the shipped `water_default` hauling-spawn pool.
- **Crystal Box, Shiny Box and Treasure Box:** referenced by `precasia_water`.

The latter are AoA hauling-pool definitions, not a claim that an ordinary vanilla rod always uses them or that every listed reward is available at every skill level. Their entries have their own level, weight and luck parameters. Follow the target release's fishing equipment and pool-selection rules. This resource scan does not establish a guaranteed acquisition route or exclude code-generated sources.

## Read rolls, weights and stack counts separately

- A **roll** selects an entry from a pool.
- A **weight** is relative to the other eligible entries, not a percentage by itself.
- A **count** is how many items the selected entry awards.
- Several rolls can select the same item. The final inventory can merge matching stacks.
- All five inspected tables have zero bonus rolls. Pack changes and applicable loot modifiers can still change the final outcome.

## Rune Box

One roll selects one of 14 equally weighted rune types, then awards 5–10 of that rune. It does not award 5–10 of every rune. Under this unmodified base pool, each type has a conditional 1/14 share.

![Rune Box complete reward item reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/rune-box-rewards-1.21.1.webp)

| Selected reward | Base weight | Count per selected entry |
|---|---:|---:|
| Wind Rune | 100 | 5–10 |
| Fire Rune | 100 | 5–10 |
| Water Rune | 100 | 5–10 |
| Wither Rune | 100 | 5–10 |
| Energy Rune | 100 | 5–10 |
| Lunar Rune | 100 | 5–10 |
| Kinetic Rune | 100 | 5–10 |
| Distortion Rune | 100 | 5–10 |
| Poison Rune | 100 | 5–10 |
| Strike Rune | 100 | 5–10 |
| Power Rune | 100 | 5–10 |
| Storm Rune | 100 | 5–10 |
| Life Rune | 100 | 5–10 |
| Compass Rune | 100 | 5–10 |

## Shiny Box

The pool makes 2–5 rolls. Each selected entry has a base count of one ingot. Repeated ingot types are possible.

![Shiny Box complete reward item reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/shiny-box-rewards-1.21.1.webp)

| Selected reward | Base weight | Count per selected entry |
|---|---:|---:|
| Iron Ingot | 75 | 1 |
| Gold Ingot | 60 | 1 |
| Netherite Ingot | 55 | 1 |
| Limonite Ingot | 80 | 1 |
| Shyrestone Ingot | 10 | 1 |
| Varsium Ingot | 50 | 1 |
| Mystite Ingot | 35 | 1 |
| Lyon Ingot | 35 | 1 |
| Ghoulish Ingot | 20 | 1 |
| Ghastly Ingot | 20 | 1 |
| Emberstone Ingot | 50 | 1 |
| Elecanium Ingot | 20 | 1 |
| Blazium Ingot | 50 | 1 |
| Baronyte Ingot | 50 | 1 |
| Skeletal Ingot | 50 | 1 |
| Lunar Ingot | 20 | 1 |

## Crystal Box

One roll selects one Skill Crystal. The weights total 460; Giant has weight 10, not a 10% chance. Read the use rules below before spending crystals.

![Crystal Box complete reward item reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crystal-box-rewards-1.21.1.webp)

| Selected reward | Base weight | Count per selected entry |
|---|---:|---:|
| Giant Skill Crystal | 10 | 1 |
| Large Skill Crystal | 40 | 1 |
| Medium Skill Crystal | 130 | 1 |
| Small Skill Crystal | 280 | 1 |

## Gem Bag

The pool makes 1–4 rolls, each awarding one selected gem/mineral item before modifiers. Four rolls do not guarantee four different types.

![Gem Bag complete reward item reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/gem-bag-rewards-1.21.1.webp)

| Selected reward | Base weight | Count per selected entry |
|---|---:|---:|
| Diamond | 50 | 1 |
| Emerald | 35 | 1 |
| Lapis Lazuli | 85 | 1 |
| Prismarine Crystals | 70 | 1 |
| Nether Quartz | 75 | 1 |
| Amethyst Shard | 60 | 1 |
| Jade | 40 | 1 |

## Treasure Box

One roll selects a reward entry. Several entries then choose a stack count. A Utopian armour entry awards its one listed piece, not the complete set.

![Treasure Box complete reward item reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/treasure-box-rewards-1.21.1.webp)

| Selected reward | Base weight | Count per selected entry |
|---|---:|---:|
| Copper Coin | 75 | 4–10 |
| Silver Coin | 50 | 1 |
| Limonite Ingot | 50 | 3–7 |
| Bottle o' Enchanting | 30 | 3–10 |
| Magic Mending Compound | 5 | 1–3 |
| Magic Repair Dust | 10 | 1 |
| Gold Coin | 6 | 1 |
| Diamond | 10 | 2–8 |
| Utopian Helmet | 5 | 1 |
| Utopian Chestplate | 5 | 1 |
| Utopian Leggings | 5 | 1 |
| Utopian Boots | 5 | 1 |

## Skill Crystals: which skill receives the XP?

A Skill Crystal does **not** let you freely choose a skill in the inspected use path. It chooses the lowest-level eligible skill whose level is **at least 15 and below 1,000**. Skills below 15 are skipped, even if they are your absolute lowest skill.

Examples:

| Your skill levels in the example | Result |
|---|---|
| 1 and 14 | No eligible skill; the failure branch does not consume the crystal. |
| 1, 15 and 30 | The level-15 skill is selected, not level 1. |
| 14, 80 and 16 | The level-16 skill is selected. |
| 999 and 1,000 | The level-999 skill is selected. |
| All at 1,000 | No eligible skill. |

Equal eligible levels retain the first skill encountered by the source iteration. Do not promise an alphabetical tie-break or a stable player-controlled choice.

### Crystal sizes

| Crystal | Source fraction of the selected level's XP requirement |
|---|---:|
| Small | 1/15, about 6.67% |
| Medium | 1/12, about 8.33% |
| Large | 1/8, 12.5% |
| Giant | 1/4, 25% |

The helper multiplies the XP requirement for the selected skill's current level by the fraction. This is **not a fraction of the XP still missing from its progress bar**, and it is not a fixed number of levels. The call requests XP-buff ignoring; the complete event/configuration path still matters when testing a modpack.

After the eligible-skill branch runs, one crystal is consumed unless the player has infinite materials. When no skill meets the threshold, a message is sent and that branch does not shrink the held stack. A crystal can therefore be saved until a skill reaches level 15.

## Common misunderstandings

| What happened | Explanation |
|---|---|
| Rune Box gave only one rune type | Its one roll selects a type; 5–10 is that type's stack count. |
| Shiny Box produced repeated ingots | Multiple rolls do not mean unique selections. |
| Crystal did not train my level-1 skill | Below-15 skills are excluded from selection. |
| Treasure Box did not give an armour set | Each Utopian piece is a separate entry in a one-roll pool. |
| My expected percentage did not match | Base weight is not a percentage; count, rolls, eligibility and modifiers are separate. |
| Items landed on the ground | Leave room for output; inventory overflow can be dropped by the helper. |

## Evidence and scope

[Released tables and class evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/reward-boxes-evidence-1.21.1.json) includes all five tables, selected method bytes, one-box consumption checks, four crystal denominator constants and six independent selection cases. [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/reward-box-art-evidence-1.21.1.json) records the original overview and all five complete reward panels.

Primary pinned source: [SkillCrystal](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/SkillCrystal.java) and [PlayerUtil](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/util/PlayerUtil.java). Static evidence and independent cases are **not live-game drop-rate tests or certification of the private Enderloom build**. AoA artwork and systems: Tslat and contributors; vanilla references: Mojang/Microsoft.
