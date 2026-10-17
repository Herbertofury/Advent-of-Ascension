# Historical fishing, Hauling and reward boxes

**Minecraft 1.12.2 / AoA 3.3.6.** Use the normal fishing workflow, then distinguish the outer fishing category from its Hauling reward table. This guide covers all 20 fish entries, 13 treasure entries, and the level-scaled Rune Box and Treasure Box contents.

[Historical first expedition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Anima fragments](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) · [Foraging and Logging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2) · [Modern Hauling rods, a different release](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hauling-Rods-and-Fishing-Pools-1.21.1)

![Exact vanilla 1.12.2 Fishing Rod recipe with three sticks and two string](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-fishing-rod-recipe-1.12.2.webp)

## Start fishing in the historical release

1. Craft a Fishing Rod with **3 Sticks and 2 String**, using the exact vanilla 1.12.2 grid above.
2. Fish using the normal rod-and-water workflow. Do not import modern AoA custom-rod or Fishing Cage requirements into this historical route.
3. Expect the outer category selection to happen before the inner fish or treasure reward selection.
4. As effective Hauling increases, additional entries become eligible. Their weight is not their overall chance per cast.
5. Save useful boxes if you want their level-scaled table-call counts to increase before opening them. Catch eligibility and opening behavior are separate rules.

This is released-data preparation, not a measured fishing-speed benchmark or certification of every modded rod.

## How AoA changes the fishing tables

The selected loot-table loading handler replaces/merges the two vanilla child tables:

| Loaded vanilla child table | AoA resource |
|---|---|
| `minecraft:gameplay/fishing/fish` | `aoa3:skills/hauling/fish` |
| `minecraft:gameplay/fishing/treasure` | `aoa3:skills/hauling/treasure` |

The helper loads the AoA table, unfreezes its pools, copies existing pools whose name is **not `main`**, then sets the replacement table. It does not preserve the original `main` pool. Another mod's changes inside that original main pool may therefore differ from a separate added pool; table-load order and modpack overrides require compatibility testing.

The inspected vanilla 1.12.2 outer fishing resource has one category roll:

| Category | Base weight | Quality |
|---|---:|---:|
| Junk | 10 | −2 |
| Treasure | 5 | 2 |
| Fish | 85 | −1 |

These are the unmodified outer resource values, not a claim that every installed pack retains them. Luck-sensitive quality and the subsequent child selection mean an inner weight must not be reported as an unconditional catch percentage.

## Fish rewards and XP

![Twenty historical fish entries, including all four vanilla metadata variants](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-fish-catches-1.12.2.webp)

The fish table has one pool and one roll. All listed entries default to one item. “Required level” is the explicit entry condition; the entity-context requirement below is additional.

| Fish | Required effective Hauling | Base weight | Base Hauling XP request |
|---|---:|---:|---:|
| Raw Fish | No explicit level condition | 100 | 15 |
| Raw Salmon | No explicit level condition | 30 | 70 |
| Clownfish | No explicit level condition | 10 | 75 |
| Pufferfish | No explicit level condition | 26 | 75 |
| Raw Fingerfish | No explicit level condition | 20 | 85 |
| Raw Pearl Stripefish | 3 | 19 | 100 |
| Raw Limefish | 5 | 18 | 130 |
| Raw Sailback | 9 | 17 | 180 |
| Raw Golden Gullfish | 14 | 16 | 250 |
| Raw Turquoise Stripefish | 18 | 15 | 380 |
| Raw Violet Skipper | 30 | 14 | 600 |
| Raw Rocketfish | 35 | 13 | 840 |
| Raw Crimson Stripefish | 42 | 12 | 1090 |
| Raw Crimson Skipper | 56 | 11 | 1900 |
| Raw Sapphire Strider | 61 | 10 | 2420 |
| Raw Candlefish | 65 | 9 | 3010 |
| Raw Dark Hatchetfish | 74 | 8 | 5260 |
| Raw Ironback | 79 | 7 | 7800 |
| Raw Rainbowfish | 90 | 6 | 11950 |
| Raw Razorfish | 98 | 5 | 18030 |

### The entity-context condition matters for modded hooks

The AoA fish entries contain `aoa3:match_entity_id` for target `this` without an explicit `id`. Its serializer defaults the expected ID to the string **`null`**. The selected condition returns true when the target is absent or has no registry ID; otherwise it compares the actual ID string with that expected value.

Consequently, a custom hook supplied as `this` with a non-null registered ID can change eligibility. The 16 AoA fish entries carry this as an **entry condition**. The four vanilla fish entries instead put it on their **Hauling XP function**, so failing it does not itself remove those vanilla entries but can skip their skill XP. Do not reduce this to “all modded rods fail”; the actual hook/context identity is what these methods inspect.

Forge is important here: its official 1.12.x fishing patch supplies the player and hook to the loot context, creates `ItemFishedEvent` from the generated results and checks cancellation before spawning the normal catch list. This is a checked upstream patch reference, not verification of an installed Forge binary. [Official Forge fishing patch](https://raw.githubusercontent.com/MinecraftForge/MinecraftForge/1.12.x/patches/minecraft/net/minecraft/entity/projectile/EntityFishHook.java.patch)

## Treasure catches

![Thirteen historical treasure catch entries and their skill requirements](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-treasure-catches-1.12.2.webp)

The treasure child table also has one pool and one roll. The images are base item references; enchantment and durability functions are described below rather than falsely rendered as a specific random outcome.

| Treasure entry | Required effective Hauling | Base weight | Base Hauling XP request |
|---|---:|---:|---:|
| Waterlily | No explicit level condition | 100 | 50 |
| Name Tag | No explicit level condition | 90 | 80 |
| Saddle | No explicit level condition | 90 | 80 |
| Bow | No explicit level condition | 95 | 70 |
| Fishing Rod | No explicit level condition | 85 | 100 |
| Book | No explicit level condition | 70 | 150 |
| Old Boot | No explicit level condition | 1 | No XP function |
| Rune Box | 25 | 50 | 1000 |
| Fish Case | 50 | 50 | 8000 |
| Weapons Case | 70 | 40 | 15000 |
| Treasure Box | 85 | 30 | 30000 |
| Crystal Box | 94 | 20 | 50000 |
| Tidal Greatblade | 95 | 10 | 55000 |

- Bow and Fishing Rod use `set_damage` with a 0–0.25 parameter range, followed by level-30 enchanting with treasure enchantments allowed. The checked vanilla damage function uses **one minus the sampled value** when calculating item damage, so this is not a promise of a nearly pristine item with only 0–25% damage.
- The Book entry also applies the level-30 enchanting function with treasure enchantments allowed. Level 30 is the enchantment-generation input, not “enchantment tier 30.”
- Old Boot has no `grant_xp` function in this selected table.
- These XP amounts are requests through the skill helper. Configuration, effective-level checks and XP modifiers remain separate.

The Hauling armor class declares level 100 and full-set callbacks adding/removing a 0.3 Hauling XP modifier. That is not evidence of an extra fish roll in the selected fishing handler.

## L'Borean: Call of the Drake is a separate event bonus

The selected `ItemFishedEvent` handler checks the configured L'Borean dimension and a **1-in-10 random gate**. On success, it constructs a Call of the Drake item at the hook and assigns motion toward the player.

It directly calls the world spawn method rather than adding the item to the event's ordinary catch list, and does not check the spawn return value. Treat cancellation ordering, custom hooks and rejected item spawning as compatibility tests. This gate is not the same thing as an inner fish-table weight, and this page does not claim a guaranteed usable boss summon from every tenth cast.

## Opening Rune Boxes and Treasure Boxes

Both selected items use their server-side **item-on-block interaction**. They call the loot helper repeatedly, then shrink the held box stack by one outside Creative. The helper supplies the player and luck to the table generation and delivers the resulting stacks.

Their loop bounds re-read effective Hauling as the loop runs. With the inspected stock box tables, no Hauling XP function changes that level during opening. A custom table that changes the skill could affect remaining iterations, so test modified rewards separately.

The counts below are **table calls**, not guaranteed unique reward types or a fixed total number of individual items. The skill getter caps effective level at 100; displayed vanity levels are not additional tiers in these helpers.

### Rune Box table calls

| Effective Hauling | Calls per box use |
|---|---:|
| 1–15 | 1 |
| 16–25 | 3 |
| 26–35 | 5 |
| 36–55 | 8 |
| 56–65 | 11 |
| 66–75 | 15 |
| 76–85 | 17 |
| 86–95 | 19 |
| 96–100 | 21 |

### Treasure Box table calls

| Effective Hauling | Calls per box use |
|---|---:|
| 1–10 | 1 |
| 11–25 | 2 |
| 26–40 | 3 |
| 41–55 | 4 |
| 56–70 | 5 |
| 71–85 | 6 |
| 86–95 | 7 |
| 96–100 | 8 |

The fishing treasure table requires Hauling 25 for a Rune Box entry and 85 for a Treasure Box entry. Those are **catch-entry conditions**; the selected box-use methods do not contain the same minimum-opening-level checks. Other acquisition routes or mods may provide boxes earlier.

## Rune Box contents

![All fourteen historical Rune Box rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-rune-box-rewards-1.12.2.webp)

Each table call has one roll, fourteen equally weighted entries and no listed count function. It selects one rune from the following set; repeated calls can select the same rune again.

Wind Rune, Fire Rune, Water Rune, Wither Rune, Energy Rune, Lunar Rune, Kinetic Rune, Distortion Rune, Poison Rune, Strike Rune, Power Rune, Storm Rune, Life Rune, Compass Rune.

## Treasure Box contents

![All fifteen historical Treasure Box rewards with quantity ranges](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-treasure-box-rewards-1.12.2.webp)

Each table call has one roll. These are separate from the outer fishing treasure-category entries.

| Reward | Quantity per selected entry | Base weight |
|---|---|---:|
| Copper Coin | 4–10 | 50 |
| Silver Coin | 1 | 30 |
| Limonite Ingot | 3–7 | 50 |
| Tea | 2–5 | 30 |
| Holly Top Petals | 8–32 | 40 |
| Experience Bottle | 3–10 | 30 |
| Rosite Ingot | 2–6 | 40 |
| Fragmented Anima Stone | 1–6 | 20 |
| Magic Repair Dust | 1 | 10 |
| Gold Coin | 1 | 10 |
| Diamond | 2–8 | 10 |
| Utopian Helmet | 1 | 5 |
| Utopian Chestplate | 1 | 5 |
| Utopian Leggings | 1 | 5 |
| Utopian Boots | 1 | 5 |

A Treasure Box is therefore another historical reference for Fragmented Anima Stone and Utopian armor pieces. It does not guarantee a complete armor set, a specific fragment count or different armor pieces from repeated rolls.

This page documents these two level-scaled boxes. The [complete remaining reward-box guide and Skill Crystal Planner](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.12.2) covers Fish Case, Weapons Case, Crystal Box, Gem Bag and Shiny Box; their contents are separate resources, not the Treasure Box table.

## Troubleshooting and restoration tests

- [ ] Verify actual Forge build/context behavior and the rod's hook entity class/registry ID.
- [ ] Confirm the outer category table separately from fish/treasure child tables; inspect other mods' main versus non-main pools.
- [ ] Test each Hauling level boundary, vanilla fish metadata 0–3 and conditional XP independently from item eligibility.
- [ ] Compare normal hooks, absent `this`, unregistered targets and a registered custom hook target.
- [ ] Check enchanted/damaged treasure outcomes and Old Boot's missing XP function without inventing bonuses.
- [ ] L'Borean bonus, event cancellation before/after AoA handling and failed item spawn.
- [ ] Rune/Treasure Box thresholds, item-on-block use, Survival/Creative, full inventory and custom reward tables.
- [ ] Verify that repeated box calls preserve intended reward probabilities and do not duplicate XP/payment through extra hooks.
- [ ] Dedicated-server behavior, compatibility and profiling before claiming complete restoration or zero performance impact.

## Evidence and scope

Eighteen selected AoA methods, four complete reward resources with **62 entries**, the vanilla rod recipe and category table, two vanilla loot-function methods and an official Forge branch patch support this guide. The 100-row box-call model is independent arithmetic. No Minecraft/game/server/mod was executed.

- [Released methods, tables, recipe and Forge-reference provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hauling-fishing-evidence-1.12.2.json)
- [Image provenance, including vanilla fish metadata variants](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hauling-fishing-art-evidence-1.12.2.json)
- [Pinned upstream fishing-table injection](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/common/registration/LootSystemRegister.java)
- [Pinned upstream Hauling thresholds](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/utils/skills/HaulingUtil.java)

## Cook and use your catch

[Compare all sixteen raw/cooked fish pairs and use the meal planner](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cooking-Fish-and-Hunger-Scaled-Healing-1.12.2). The shared cooked-fish healing callback scales its request by missing hunger before eating; the configured maximum is not guaranteed every meal.
