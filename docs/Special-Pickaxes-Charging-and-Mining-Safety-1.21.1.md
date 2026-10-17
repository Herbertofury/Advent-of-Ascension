# Special pickaxes: charging, drops and mining safety

**Minecraft 1.21.1 · AoA 3.7.16.1.** Choose the effect you need, then check acquisition separately. Eight special implementations remain in the inspected archive; this scan found shipped output recipes for four of them. A retained class or item picture does not prove a complete survival route.

![Eight special pickaxes and their distinct effects](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-overview-1.21.1.webp)

## Recipes and availability

![Four exact shaped patterns with tag ingredients and explicitly labeled example icons](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-recipes-1.21.1.webp)

The pictured tag members are examples from included tag data. The # placeholders keep external membership unresolved rather than inventing a substitute. In particular, the Skeletal pattern accepts the active `aoa3:precasian_bone` tag, not just the pictured Chestbone Fragment. Its inspected local members are Chestbone, Footbone, Legbone and Skullbone Fragments.

| Tool | Shipped output recipe in this scan |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-gemcracker.webp" width="54" height="54" alt="Gemcracker source-model item"> [Gemcracker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:gemcracker) | [Open exact shaped recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&recipe=aoa3:crafting_shaped_gemcracker) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-pickmax.webp" width="54" height="54" alt="Pickmax source-model item"> [Pickmax](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:pickmax) | [Open exact shaped recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&recipe=aoa3:crafting_shaped_pickmax) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-emberstone_pickaxe.webp" width="54" height="54" alt="Emberstone Pickaxe source-model item"> [Emberstone Pickaxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:emberstone_pickaxe) | [Open exact shaped recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&recipe=aoa3:crafting_shaped_emberstone_pickaxe) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-occult_pickaxe.webp" width="54" height="54" alt="Occult Pickaxe source-model item"> [Occult Pickaxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:occult_pickaxe) | No output recipe found; acquisition remains separate |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-energistic_pickaxe.webp" width="54" height="54" alt="Energistic Pickaxe source-model item"> [Energistic Pickaxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:energistic_pickaxe) | No output recipe found; acquisition remains separate |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-soulstone_pickaxe.webp" width="54" height="54" alt="Soulstone Pickaxe source-model item"> [Soulstone Pickaxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:soulstone_pickaxe) | No output recipe found; acquisition remains separate |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-skeletal_pickaxe.webp" width="54" height="54" alt="Skeletal Pickaxe source-model item"> [Skeletal Pickaxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:skeletal_pickaxe) | [Open exact shaped recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&recipe=aoa3:crafting_shaped_skeletal_pickaxe) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-pickaxe-ornamyte_pickaxe.webp" width="54" height="54" alt="Ornamyte Pickaxe source-model item"> [Ornamyte Pickaxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:ornamyte_pickaxe) | No output recipe found; acquisition remains separate |

Four absent output recipes do not prove the items are unobtainable. Loot, trade, commands, datapacks and restoration work are separate routes that need their own evidence. Use the [ore guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mining-and-Ore-Generation-1.21.1) for mining-tier and deposit references; special behavior does not bypass tool-tier requirements automatically.

## Energistic: charge before expecting the speed bonus

- The charge component defaults to 0; maximum charge is 2000.
- At least 5 charge is required for the bonus. If the ordinary tool speed is not exactly 1, the charged implementation returns three times that base speed.
- Using the tool on the server transfers up to 20 Spirit into it, limited by available Spirit and remaining charge capacity.
- Mining an eligible block subtracts 5 charge with forced clamping at 0. The speed test and charge subtraction are distinct: a partially charged tool with 4 charge receives no bonus, but that eligible mine call can still drain its remaining 4.

| Before | Ordinary speed | Returned speed input | Charge after mine callback |
|---|---:|---:|---:|
| Charge 0 | 8 | 8 | 0 |
| Charge 4 | 8 | 8 | 0 |
| Charge 5 | 8 | 24 | 0 |
| Charge 6 | 8 | 24 | 1 |
| Charge 2000 | 1 | 1 | 2000 |

At charge 1999 with 20 Spirit, the modeled transfer is only 1. At charge 0 with 3 Spirit, it is 3, still below the bonus threshold. These are input arithmetic examples, not measured block-breaking times. Tool tier, hardness, effects, enchantments and durability still matter.

## Pickmax: a volume, not just a flat mining face

The inspected mine callback considers the **26 neighbors in a 3×3×3 cube** around the original block, excluding its center. This is not merely the eight neighbors of a flat 3×3 face.

The extra-harvest branch requires server-side execution, a player who is not a FakePlayer, and an original state tagged as stone or cobblestone. Each neighbor must also carry one of those tags and pass a destroy-progress ratio comparison. It then calls the shared extra-harvest helper.

That helper checks interaction permission and a cancellable server block-break hook before removal. This is useful protection integration, not a guarantee that every claim/protection mod works. The Pickmax override itself has no crouching bypass, so do not assume sneak disables the area effect.

Keep valuable stone/cobblestone builds away from testing. The ratio reads the current center position's world state during the callback; its timing and actual neighbor-removal outcomes need target-build testing. No guarantee of 26 successful breaks, exact durability cost or claim-mod compatibility is made here.

## Emberstone: smelts drops, with different XP arithmetic

Its loot callback requires a non-air block, nonempty generated loot and effective tool speed above 1. For each existing loot stack with a matching smelting recipe, it copies that recipe's result and multiplies the result count by the original stack count.

The experience call receives **the recipe XP cast to an integer**, once for that matched stack. It is not multiplied by the input stack count in this callback. For example, 0.7 becomes 0 and 2.5 becomes 2 before the experience-spawn call. Do not promise the same XP behavior as manually smelting that whole stack in a furnace.

A drop with no matching smelting recipe stays unchanged. Recipe-manager selection, tag changes and other loot modifiers can alter the actual result.

## Gemcracker: the first eligible drop matters

The loot callback requires a non-air ore-tagged block, nonempty loot and tool speed above 1. It inspects the **first** loot stack. It does not boost that stack when it is the mined block's own item or belongs to the raw-materials item tag.

For an eligible primary stack, it asks for an additional amount of `1 + RandomUtil.numberUpTo(currentCount)`, using the shared stack-growth helper. That helper either grows the original stack or returns additional bounded stacks when the addition would exceed its maximum stack size. Other stacks in the loot list are not all independently multiplied.

The external random helper's endpoint semantics are not inferred here, so this guide does not invent an exact multiplier or probability distribution. Silk-Touch-like block drops and raw-metal drops can take different branches because of the identity/tag checks.

## Soulstone: Spirit-funded stone drops

This callback requires stone/cobblestone tags, usable tool speed, nonempty loot and a ServerPlayer in the loot context. It prefers a loot stack whose item equals the mined block's item; otherwise it selects the first stack.

If the 5-Spirit consumption succeeds, it doubles that selected stack's count. It does not double every output stack or every ore. Unlike Gemcracker's shared overflow helper, this path directly sets the doubled count; unusual high-count loot and other modifiers should be tested for delivery/stack handling rather than assumed safe.

## Skeletal: bonus bones are conditional

After the non-air, nonempty-loot and tool-speed gates, it invokes `oneInNChance(10)`. On success, a 50-bound random choice selects a bone fragment at 0, Bone Meal below 10, or Bone otherwise. The fragment branch chooses among Skullbone, Chestbone, Legbone and Footbone Fragments.

This records the inspected branch structure. Exact random-helper probabilities are not asserted without the external implementation. The bonus is appended to the existing loot rather than replacing the entire list.

## Ornamyte: hard-block speed input

When the block's default destroy-time value is at least 50, this override returns ten times the ordinary tool efficiency. Otherwise it leaves that efficiency unchanged.

That threshold is not a promise of instant mining, correct drops from every block or permission to break unbreakable blocks. It does not replace the rest of Minecraft's harvesting, tool-tier and hardness rules.

## Occult: temporary ore outlines, with bounded initial scans

Use activates a client-side block scan. Each coordinate loop starts at integer truncation of position−4 and ends before integer truncation of position+4. It collects ore-tagged states and submits an outline batch with deadline `GlobalEvents.tick + 150`.

This is a box-like scan, not a spherical four-block radius. Truncation toward zero makes fractional positions crossing the coordinate origin asymmetric: the checked examples visit 343, 392, 448 or 512 positions. The maximum in this range model is 512 positions per activation.

The renderer appends batches and removes expired entries by tick. It also rechecks retained block states on odd ticks. Repeated activations can leave overlapping batches until expiration; the inspected add method does not deduplicate them. That is a profiling and regression-test target, not a measured FPS loss or a fix already implemented.

## Why a loot effect might not trigger

The shipped global modifier list includes `aoa3:loot_modifying_items`, with an empty condition list in its own resource. The modifier selects the loot-context tool when present, or a held item from a living attacker in the fallback branch, then invokes the interface only for a matching item type.

The block helper verifies required block-loot parameters; otherwise it returns an air state. The tool-specific checks above can therefore decline non-block or incomplete contexts. A tooltip alone is not proof that every chest, entity or custom loot event receives the effect.

## Test and restoration checklist

- Verify exact acquisition separately for the four tools without an output recipe found here.
- Test 0/4/5 charge boundaries, charging near capacity and zero/low Spirit on copied saves.
- Test Pickmax on expendable terrain, with creative/survival modes, protection hooks and nearby valuable blocks.
- Compare Emberstone item counts and XP with real recipe overrides.
- Test modified large loot stacks and delivery for Gemcracker/Soulstone.
- Profile repeated Occult activations, expiration and renderer compatibility; do not claim a measured performance improvement from this inspection.

[Fourteen released class selections, four recipes and 414 bounded arithmetic/coordinate cases](https://herbertofury.github.io/Advent-of-Ascension/special-pickaxe-evidence-1.21.1.json) · [Image and recipe-pattern evidence](https://herbertofury.github.io/Advent-of-Ascension/special-pickaxe-art-evidence-1.21.1.json)

Original AoA item art: Tslat and contributors. Source-model crops and explanatory recipe diagrams are not game screenshots. No Java/game code was executed, and runtime mining, economy, compatibility and performance certification remain separate.
