# Your first expedition and portal · 1.16.5

**For Minecraft 1.16.5 / AoA 3.6.11.** Recipes and rules below are checked against that release and its pinned source. A modpack can override them. This is a source-checked walkthrough, not a claim that a particular Enderloom build has passed a live playthrough.

[Visual tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.16.5) · [Historical realmstone routes](Realmstone-Progression-Walkthrough-1.16.5) · [Historical rune production](Rune-Production-and-Randomizer-1.16.5)

## What you are building

![A 5 by 6 portal frame with 13 Ancient Rock blocks, five distinct carved runes and a 3 by 4 opening](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/first-portal-1.16.5.webp)

A working frame needs **13 Ancient Rock blocks**, **one each** of the Carved Runes of Power, Space, Direction, Reality and Travel, and an appropriate destination Realmstone. Its outside measures **5 blocks wide × 6 high**; the clear opening is **3 × 4**. The Power rune is the bottom-middle block.

Use the illustrated arrangement as a reliable construction plan. Four copies of one decorative rune do not substitute for the four different rune types. Keep the opening clear rather than treating the illustration as a solid wall.

## 1. Establish a safe base

Gather food, tools, armor, building blocks and lighting before searching underground. Leave valuables at home and write down your return location. AoA's bundled getting-started entry recommends finding the underground ruined teleporter and its Corrupted Traveller; it does not give a guaranteed coordinate or search radius.

Treat exploration as a search, not a promise that digging a prescribed number of blocks will find the structure. Recover Ancient Rock from the ruined frame as appropriate. Keep enough for the portal **and one additional block for the Power rune recipe** if crafting it yourself.

## 2. Trade food for the Worn Book

Interact with a living Corrupted Traveller without sneaking to open its exchange. Place **one food item directly into the input** and collect the Worn Book. The checked exchange tests for food properties and consumes one food for the book. Start with a normal vanilla food; custom modded food may behave differently.

Do not assume shift-clicking or inserting a large stack is a bulk-trading shortcut. Stay close to the Traveller while using the interface.

Use the Worn Book to obtain a **Blank Realmstone** when you do not already have one in the inventory searched by the implementation. The checked use path retains the book. Keep it: after turning a blank into a destination stone, you can use the book again for another blank. This is not a promise to search every modded backpack recursively.

## 3. Prepare the Power rune

![The historical Power rune crafting grid and shapeless Runium Chunk conversion](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/power-rune-recipe-1.16.5.webp)

First craft **1 Runium Chunk → 16 Unpowered Runes**. In this release that conversion is **shapeless crafting**. Do not follow a newer-version stonecutter instruction.

At a crafting table, use:

| Unpowered Rune | Eye of Ender | Unpowered Rune |
|---|---|---|
| Unpowered Rune | Ancient Rock | Unpowered Rune |
| Unpowered Rune | Unpowered Rune | Unpowered Rune |

This consumes **7 Unpowered Runes + 1 Eye of Ender + 1 Ancient Rock** and produces **1 Carved Rune of Power**. One Runium Chunk supplies more than the seven runes needed for this recipe.

## 4. Collect the other four rune types

Space, Direction, Reality and Travel runes appear in the release's extra chest-loot table. The registered modifier targets these vanilla chest tables:

- Abandoned mineshaft; buried treasure; igloo chest
- Jungle temple; desert pyramid; pillager outpost; ruined portal
- Shipwreck **treasure** chest; simple dungeon; spawn bonus chest
- Stronghold corridor, crossing and library
- **Big** underwater ruin chest
- Village **temple** chest

These are exact table selectors, not every village, shipwreck or underwater chest. Packs can replace loot or modifier behavior. A qualifying chest can still give no rune, or a duplicate of one you already own.

The added rune table has one roll: each of the four runes has weight 100 and the empty entry has weight 150. Thus each rune is 2/11 **within that eligible extra-table roll**, not a universal chance for every chest in the world. Collect all four types before assembling the finished frame.

## 5. Choose a destination using historical rules

A Blank Realmstone is a starting material, not an activated destination key. Follow the [1.16.5 realmstone walkthrough](Realmstone-Progression-Walkthrough-1.16.5), which separates the historical acquisition conditions for 22 routes.

For example, the historical Precasia route uses the six-sapling crafting recipe shown there. Do not substitute the modern Precasia archaeology route. Choose a destination you are equipped to survive, not merely the first stone you can acquire.

## 6. Assemble and activate

1. Build the frame shown above on stable ground with space to approach it safely.
2. Count the 13 Ancient Rock blocks and check all five distinct runes.
3. Clear the entire 3 × 4 interior.
4. Use your **destination Realmstone on the Power rune**. If orientation causes trouble, click the face looking into the portal opening.
5. Confirm that the portal actually lights before entering. Keep food, spare blocks and a record of your departure location ready.

The checked normal activation branch does not directly consume the destination Realmstone, but pack overrides can differ. Do not throw away the stone or your Worn Book after your first journey.

**Blank Realmstone caution:** using a blank on the Power rune is a separate deactivation path when a portal is present above it. It is not how you select a destination.

## Troubleshooting before rebuilding

| Symptom | Check first |
|---|---|
| No Blank Realmstone from the book | Is a blank already in the inventory searched by the book? Have you actually used the book? |
| Traveller exchange is unavailable | Traveller alive, not sneaking, close enough, normal food placed directly in the input |
| Frame will not light | Correct outer size, clear opening, 13 Ancient Rock, Power at bottom center, four distinct other runes |
| You have four runes but still fail | Check names: duplicates do not satisfy missing Space/Direction/Reality/Travel types |
| Clicking produces no useful result | Destination stone rather than a blank; click the Power rune's portal-facing side |
| Portal turns off | Check whether you used a Blank Realmstone |
| Modern guide gives the wrong recipe | Keep this release selected; 1.16.5 Runium conversion is shapeless crafting |
| Expected chest never yields a rune | Verify the exact chest-table category; ordinary randomness and pack loot overrides still apply |

## Before crossing: quick checklist

- [ ] Shelter and return coordinates recorded
- [ ] Food, armor, tools, spare blocks and lighting prepared
- [ ] Worn Book kept safely
- [ ] Correct historical destination Realmstone obtained
- [ ] Frame count and empty interior verified
- [ ] Destination's hazards and progression prerequisites reviewed

Continue with [realmstone progression](Realmstone-Progression-Walkthrough-1.16.5), [finding traders](Finding-Traders-1.16.5), or [finding useful mob drops](Finding-and-Using-Mob-Drops).

## Evidence and limitations

The [machine-readable audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/starter-portal-evidence-1.16.5.json) records released guide/recipe/loot resources, class checks and hashes. Source interpretation is pinned to [e97502da8bdd6081b6acc4635f03296d3e2e69a0](https://github.com/Tslat/Advent-Of-Ascension/tree/e97502da8bdd6081b6acc4635f03296d3e2e69a0), particularly CorruptedTravellerContainer, WornBook, CarvedRuneOfPower, AoAPortalFrame and RollExtraTablesLootModifier. Class checks corroborate the narrow food-consumption/book paths; they are not an exhaustive bytecode equivalence proof of every source statement.

Illustrations use release-matched AoA models/textures and the matching vanilla Eye of Ender, composed into original instructional diagrams. AoA assets belong to their respective creators; vanilla assets belong to Mojang/Microsoft. No game binaries are redistributed here. Runtime behavior, private Enderloom changes, server permissions and other mods still require in-game acceptance testing.
