# Fishing Cage walkthrough · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** A Fishing Cage is a reusable, finite-durability alternative to watching a fishing bobber. Make Chum, craft the cage, throw it into water so it settles on the bottom, then return to collect its catches. The owner must remain available in the same world for the checked catch path.

![Fishing Cage recipe, Chum crafting ingredients and deployment reminders](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/fishing-cage-recipe-1.21.1.webp)

[Hauling skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) · [Recipes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes) · [Loot conditions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Loot-Tables-and-Global-Modifiers-1.21.1)

## 1. Make the bait

Place **one raw-fish-tag item and one sword-tag item** into a crafting grid. The shipped `aoa3:tool_interaction` recipe accepts `c:foods/raw_fish` and `minecraft:swords`, producing **1 Chum**.

This is a crafting-grid recipe, not an instruction to attack a dropped fish. The first matching sword is returned with **one additional damage** when damageable, unless that reaches its maximum durability, in which case it breaks. A non-damageable matching tool is returned without damage. Tags and pack recipes can change accepted items. The 2×2 player grid has enough space for this two-ingredient recipe.

## 2. Craft the cage

| Empty | Wooden rod | Empty |
|---|---|---|
| Wooden rod | Chum | Wooden rod |
| Planks | Planks | Planks |

Total: **3 items matching `c:rods/wooden`, 3 matching `minecraft:planks`, and 1 Chum**. Output: one Fishing Cage. The stock item has **15 durability** and its ordinary enchanting-table/book checks reject enchantment.

## 3. Deploy somewhere that can catch

1. Choose water with a reachable bottom and room to retrieve the cage safely.
2. Use the held cage to throw it forward. The server spawns the cage entity and consumes the held item through AoA's item-use helper.
3. Let it settle. The fishing check requires **on ground and in water**; a cage still falling or floating above support does not pass that check.
4. Remain in the same world, and keep the area ticking. The catch code looks up the owner in that level; an offline owner or one in another dimension does not produce catches through this path.
5. Give cages space. A nearby-cage count within the source's five-block retrieval query adds another random gate; tightly stacking cages is not a simple linear speed upgrade.
6. Interact with your cage to retrieve its contents and, if durability remains, the cage item.

The source recognizes the owner's UUID. Ordinary retrieval is allowed to that owner, or when the entity has no recorded owner. This is not a claim that it implements every server protection mod's rules.

### Water flow and waiting

The initial fishing gate is a **1-in-5,000 random check per eligible call**. It is not a guaranteed 5,000-tick timer. A zero-flow `FlowingFluid` state has an additional fifty-fifty gate, and the other fluid branch has its own 1-in-10 check. Nearby cages add a further gate. Do not turn one constant into a promised minutes-per-catch rate.

The cage is not pushed by fluid through its inspected vanilla fluid-push override. Its own movement code still handles gravity and water motion. This page does not promise compatibility with every modded fluid or force system.

## 4. Understand capacity and wear

There are **three synchronized catch slots**. The checked stock loot table produces one base roll per successful generation. When the third slot is occupied, the cage stops further fishing checks until retrieved. Modified loot tables may behave differently.

**Important stock behavior: any non-empty retrieval counts the three-element storage array, not the number of occupied slots.** The released `getLoot()` allocates an array of length 3; the interaction adds that array length to wear and uses it for the Hauling time-budget multiplier.

| Occupied slots at retrieval | Wear added by the inspected interaction | Source XP time-budget multiplier |
|---|---:|---:|
| 0 | 0 | No catch XP branch |
| 1 | 3 | 3 |
| 2 | 3 | 3 |
| 3 | 3 | 3 |

Waiting for all three slots can therefore avoid spending the same wear on a partial load, when circumstances allow. A fresh 15-durability cage reaches its limit after five ordinary non-empty retrievals at this cost: **the fifth still delivers catches but does not return a reusable cage**. Existing damage and other paths can change that sequence.

The XP amount is calculated with AoA's level-dependent time-budget helper and the player's gain eligibility. The helper argument is not a flat 1,000 XP award, and the multiplier is not a promise of an exact final XP gain.

Empty retrieval returns the surviving cage outside Creative without catch-related wear. Creative handling differs; do not use Creative inventory behavior as a Survival duplication test.

## 5. Read the catch table correctly

Caught a Rune Box or Shiny Box? The [reward-box guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.21.1) shows every reward in its shipped table and explains how opening works.

![All eighteen Fishing Cage catch items with their table skill gates](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/fishing-cage-catches-1.21.1.webp)

The released table contains **18 entries**, one base roll, and no bonus rolls. The source passes **luck = 2 + owner luck**. Entry quality and level conditions affect eligibility/selection, so the following weights are not fixed percentages.

| Catch | Base weight | Quality | Required Hauling level in this table |
|---|---:|---:|---|
| Cod | 100 | −1 | No level condition |
| Salmon | 100 | −1 | No level condition |
| Tropical Fish | 80 | −1 | No level condition |
| Pufferfish | 60 | 0 | No level condition |
| Nautilus Shell | 20 | 1 | No level condition |
| Diamond | 30 | 0 | No level condition |
| Emerald | 10 | 2 | No level condition |
| Rune Box | 20 | 1 | No level condition |
| Shiny Box | 20 | 1 | No level condition |
| Sailback | 75 | 0 | 10 |
| Violet Skipper | 75 | 0 | 10 |
| Raw Rainbowfish | 30 | 2 | 10 |
| Armour Plating | 30 | 1 | No level condition |
| Chitin | 45 | 0 | No level condition |
| Chum | 55 | 0 | No level condition |
| Prismarine Slab | 40 | 0 | No level condition |
| Prismarine Crystals | 40 | 0 | No level condition |
| Tidal Greatblade | 1 | 3 | 75 |

“No level condition” describes this table entry, not a guarantee that every other restriction or modifier is absent. The player-level condition checks a player from the loot context; the cage supplies its owner as the attacking-entity context. No fighting is required to meet that context convention.

For item pictures and the full conditions, open the [Loot Reference](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html) and search for `fishing_cage_catches`, or find the item in the [Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1).

## Troubleshooting and safe recovery

| Problem | What to check |
|---|---|
| Nothing caught | It must be grounded in water, its owner must be present in that world, the area must tick, and the random gates must succeed. |
| Adding more cages does not scale | The local cage-density gate deliberately reduces each cage's chance. |
| Cannot collect someone else's cage | Owner UUID restriction is part of the normal interaction. |
| Cage stopped fishing | Its third catch slot may already be occupied. |
| Cage vanished after collection | At the durability limit, catches are delivered but the cage is not returned. |
| Enchanting fails | The stock cage explicitly rejects its ordinary enchantment checks. |
| Chum recipe fails | Use raw-fish and sword tags; cooked fish or a different tool is not automatically accepted. |

Avoid draining or breaking the cage's site as your routine collection method. The source has a separate grounded-out-of-water recovery branch and removal-time catch handling. Keep inventory room and retrieve deliberately. Full-inventory, unload/reload, protected-spawn rejection and removal behavior are explicit integration test targets; this guide does not claim they have all been validated in game.

## Evidence and restoration targets

[Release evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fishing-cage-evidence-1.21.1.json) includes the recipes, complete table, selected class bytes, 15-durability constructor and four independent array-length cases. [Illustration provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fishing-cage-art-evidence-1.21.1.json) records the official item-model inputs.

The count mismatch is a concrete restoration review target: decide whether wear and XP should use occupied slots, then test zero/one/two/three catches. Preserve save data and test inventory-full recovery and owner availability. Do not assume a duplication bug merely because both interaction and removal mention catch delivery: the inventory helper mutates referenced item stacks, so the complete transfer path needs examination.

Primary pinned implementation: [FishingCageEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/misc/FishingCageEntity.java). This is released-resource and code analysis with independent documentation checks, **not a live fishing benchmark or a certified fix in the private Enderloom build**. AoA artwork and systems: Tslat and contributors; vanilla references: Mojang/Microsoft.
