# Movement and void-recovery utilities · 1.21.1

**Minecraft 1.21.1 · AoA 3.7.16.1.** These tools have different triggers. A Gravitator slows falling; a Distorting Artifact requests a fixed-height recovery teleport; a Floating Stone transforms a dropped item. None of those statements guarantees a safe landing in a custom dimension.

![Three utilities and their distinct limits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/void-utility-comparison-1.21.1.webp)

## Quick equipment check

| Item | Where it must be | Trigger | Declared result |
|---|---|---|---|
| [Gravitator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agravitator) | Selected main-hand stack or the exact offhand stack | Vertical velocity below −0.079 | Multiply vertical velocity by about 0.8; server also reduces fallDistance by 0.8 |
| [Distorting Artifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adistorting_artifact) | Hotbar slot 0–8 or the exact offhand stack | Server-side, damage below maximum, Y at/below the dimension’s minimum build height | Same X/Z, Y=257; sets fallDistance to −255; requests 40 ticks of Blindness for living users |
| [Floating Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afloating_stone) | A dropped item entity | Strictly below Y=−10 | Moves the item to Y=257 and replaces its stack with one Heavy Boulder |

The Distorting Artifact does not need to be the selected hotbar item. The Gravitator does. An artifact in ordinary storage slots is not equivalent to one in the hotbar. This reference describes the item's callback conditions; external inventory systems may dispatch ticks differently.

## Craft and prepare a Distorting Artifact

![Exact Distorting Artifact recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/distorting-artifact-recipe-1.21.1.webp)

1. Gather **4 Void Scales, 3 gems accepted by c:gems/bloodstone, and 1 Eye of Ender**. The supplied tag includes AoA Bloodstone; other packs can modify it.
2. Use the illustrated 3×3 pattern. The top-center slot is empty. The recipe produces one artifact.
3. Place it in the hotbar or offhand and check that its damage is below its configured maximum of 10.
4. Treat it as an emergency mechanism. Do not deliberately enter the void with valuable equipment to test it.

[Open the exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&recipe=aoa3%3Acrafting_shaped_distorting_artifact).

### What recovery does, and what remains unsafe

- The callback compares against **the current dimension’s minimum build height**, not a universal Y=0 threshold.
- It requests a teleport to **Y=257 at the same X and Z**, without changing dimensions.
- It assigns fallDistance −255. This is a stored field update, not a permanent fall-damage-immunity effect.
- Living users receive a Blindness request for 40 ticks, nominally two seconds at 20 TPS, marked ambient with particles hidden.
- Server players request one durability damage through AoA’s helper, which delegates to ItemStack.hurtAndBreak. Enchantments, game rules and hooks can change actual durability outcomes, so “exactly ten rescues” is not promised.
- No collision, roof clearance, support block, lava or custom-height landing search occurs in the inspected item callback. Recovery may place the user in an unsafe location or outside a custom dimension's intended play area.

## Use a Gravitator for descent control

Hold it selected or in the offhand. While vertical motion is below −0.079, its callback multiplies only the Y component by the float approximation of 0.8; horizontal velocity is unchanged by this operation. The server also multiplies accumulated fallDistance by 0.8. Motion updates elsewhere in the tick still apply.

It is **not powered flight, a fixed terminal-velocity guarantee, or unconditional fall-damage immunity**. The threshold is strict: exactly −0.079 does not enter this branch.

Configured durability is 1,500. During a qualifying server-side falling tick, the code calls oneInNChance(15) before requesting one durability damage. This is a per-qualifying-tick random gate, not a deterministic timer or lifetime.

The offhand path passes MAINHAND to the damage helper despite supplying the actual Gravitator stack. The helper still receives that stack; the discrepancy concerns break/equipment reporting. It is a target-build test case, not proof that the wrong held item is damaged.

### Haven-to-Lunalus realmstone branch

A separate branch checks for a non-Creative ServerPlayer in Haven, airborne, at a game time divisible by five, while the Gravitator is active. It finds a Blank Realmstone and may replace the selected matching inventory slot with a Lunalus Realmstone. InventoryUtil checks main hand, then offhand, then inventory compartments.

**The released downward scan is not a continuous vertical column.** It mutates one BlockPos and subtracts the increasing loop index from the already-mutated Y. Starting at Y=10, the checks are:

10, 9, 7, 4, 0, −5, −11, −18, −26, −35.

It skips intervening heights. Therefore, the current callback cannot be described as proving that every block below the player is empty. Eight bounded scan traces are retained in the evidence. Whether skipped solid blocks or below-height queries produce an observable progression error needs target-build testing.

The callback contains a Haven reference, but that alone does not establish that Haven is reachable and fully playable in this release or a particular merged pack. No Gravitator crafting recipe was found in the scoped recipe-resource scan; that is not a claim that all possible acquisition mechanisms were searched.

## Floating Stone → Heavy Boulder: protect your stack

This is an **item-entity transformation**, not a player rescue. Below Y=−10, the callback teleports the dropped item to Y=257 and installs a newly constructed stack containing exactly **one Heavy Boulder**.

Consequences of the inspected code:

- At exactly Y=−10, it does not transform. The comparison is strictly lower.
- There is no dimension check in this callback. The threshold is not tied to that dimension’s minimum build height.
- An input stack of 2, 16 or 64 is still replaced with one output. Input count and custom components are not copied into the new stack.
- The callback contains no local client/server guard and no safe destination search. Do not infer duplication from this alone; event dispatch and synchronization need game testing.
- If this behavior is retained in a target build, use a single item in a controlled test environment rather than risking a valuable stack.

The released Haven and Haven-passive loot resources reference Floating Stone. These are table references, not a claim about which live mobs or events invoke them, nor an unconditional per-kill drop chance. [Inspect the release-specific loot browser](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1).

## Restoration acceptance checklist

- [ ] Validate fixed-height teleports against each supported dimension's height, collision and hazard rules, using bounded work on the server.
- [ ] Test selected, unselected-hotbar, storage and offhand behavior independently.
- [ ] Verify durability/break callbacks in survival, Creative and enchanted-stack cases.
- [ ] Replace the Gravitator's cumulative-position scan with an explicitly bounded, intentional column test if the intended rule is “clear space below”; test skipped-height fixtures.
- [ ] Preserve intended stack counts and components during item transformation, or clearly document deliberate one-item conversion.
- [ ] Verify multiplayer synchronization and save/reload behavior before claiming the restored feature works.
- [ ] Profile only the relevant held-item/active conditions. Avoid adding full-inventory or world scans every tick.

These are proposed target-build checks, not claims that the user's private Enderloom build is defective or that fixes have already been implemented.

## Evidence and related guides

- [Released methods, registrations, resource hashes and bounded models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/void-utility-evidence-1.21.1.json)
- [Illustration source receipts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/void-utility-art-evidence-1.21.1.json)
- [Pinned original Gravitator source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/Gravitator.java)
- [Historical Rosidons escape behavior](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rosidons-Escape-and-Destination-Safety-1.12.2)
- [1.16.5 realmstone progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5)

Original AoA artwork and behavior by Tslat and contributors. Static archive inspection and documentation models only; no game or mod code was executed.
