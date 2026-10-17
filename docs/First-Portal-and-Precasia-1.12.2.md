# First portal and Precasia · 1.12.2

**For Minecraft 1.12.2 / AoA 3.3.6.** This is a historical starter route checked against released recipes, selected class behavior and pinned source. Use it for this edition; do not substitute modern recipes, item IDs or archaeology instructions.

[Visual tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.12.2) · [Historical galleries](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Galleries) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

## Your expedition shopping list

Prepare ordinary survival equipment first: food, armor, tools, lighting, spare blocks and a safe home. Then collect:

- **13 Ancient Rock** for the frame, plus **1 extra Ancient Rock** if crafting the Power rune
- **One each** of the Space, Direction, Reality and Travel carved runes
- **7 Unpowered Runes** and **1 Eye of Ender** for the Power rune
- A **Worn Book**, used to obtain a Blank Realmstone
- For the illustrated Precasia route: one each of the **six vanilla sapling types**

Keep a free inventory slot before the Traveller exchange, and record your base coordinates before leaving.

## 1. Find the Traveller and recover frame materials

The pinned source places a Corrupted Traveller inside the Ruined Teleporter Frame structure. The ordinary Overworld structure attempt chooses a **base Y of 10–19**; the structure places the Traveller four blocks above that base. Those are source generation coordinates, not a guarantee that a particular cave or chunk contains a Traveller.

The default structure chance setting is 130, but terrain checks and generation context still matter. It does not mean that every 130th chunk contains one. Another village-population hook also exists, so this guide does not reduce the entire world-generation process to one global probability.

If a pack sets `ruinedTeleporterFrameSpawnChance` to zero, the inspected spawn registration adds a separate natural-spawn entry for the Traveller. Do not spend hours searching for disabled structures without checking the pack's configuration. This is a configuration-dependent source route, not a guaranteed spawn at your location.

Recover Ancient Rock and useful carved runes from ruins where available. Do not assume the old and modern world-generation systems place identical structures.

## 2. Exchange one food for the Worn Book

Open the Traveller's exchange and place **one ordinary food item directly into the input**. Leave room in your own inventory for the book.

This edition checks whether the item is an `ItemFood`. Its released exchange code only consumes the food after inserting the Worn Book into your inventory succeeds. If your inventory is full and nothing happens, free a slot and try again. Do not assume that every modded edible item uses the same old food class, or that shift-click is a bulk-exchange feature.

Use the Worn Book. If the checked inventory search finds no Blank Realmstone, the server gives you one. The book is retained by this use path. Keep it for obtaining another blank after converting the one you hold; this is not a claim to search every modded storage container.

## 3. Make the Power rune

Craft **one Runium Chunk into 16 Unpowered Runes**, using the shipped **shapeless** recipe. Then use this exact crafting-table pattern:

| Unpowered Rune | Eye of Ender | Unpowered Rune |
|---|---|---|
| Unpowered Rune | Ancient Rock | Unpowered Rune |
| Unpowered Rune | Unpowered Rune | Unpowered Rune |

It produces one Carved Rune of Power. The historical registry ID is **`aoa3:carved_rune_power`**. Newer documentation often uses `carved_rune_of_power`; that is not this recipe's output ID.

Keep the spare nine Unpowered Runes from the chunk conversion for other uses. A stonecutter conversion is a later-version instruction, not the recipe described here.

## 4. Finish the four other rune types

The pinned loot-loading hook adds a carved-rune pool to these **11 vanilla chest tables**:

- Abandoned mineshaft
- Desert pyramid, igloo chest and jungle temple
- Simple dungeon and spawn bonus chest
- Stronghold corridor, crossing and library
- Village blacksmith
- Woodland mansion

This is the historical list. Do not copy the 1.16.5 list containing later structures such as shipwrecks or pillager outposts into a 1.12.2 search plan. Chest contents remain random; duplicates do not replace a missing rune type. Pack loot edits can change the result.

## 5. Build the frame

![Historical 1.12.2 portal with five distinct carved runes and thirteen Ancient Rock blocks](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/first-portal-1.12.2.webp)

The outside is **5 blocks wide and 6 blocks tall**. Leave a **3 × 4 clear opening**, with the Power rune at the bottom center. The source checks 13 Ancient Rock blocks and all four distinct non-power rune types; duplicate types are rejected. The diagram is one valid arrangement.

For a simple first build, use clear air inside the opening. Do not fill it with decorative solid blocks and expect activation to hollow it out for you.

## 6. Craft the historical Precasia Realmstone

![Six distinct vanilla saplings and a Blank Realmstone make the historical Precasia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/precasia-sapling-recipe-1.12.2.webp)

At a crafting table, combine:

1. Oak sapling
2. Spruce sapling
3. Birch sapling
4. Jungle sapling
5. Acacia sapling
6. Dark Oak sapling
7. Blank Realmstone

This is **shapeless**, so their grid positions do not matter. Their types do: the released recipe requires `minecraft:sapling` metadata **0, 1, 2, 3, 4 and 5**, each once. Six oak saplings are not equivalent. Modded saplings are not automatically accepted by these exact vanilla item-and-metadata ingredients.

The result is one Precasia Realmstone. This is a crafting route, not the modern jungle-archaeology route.

## 7. Activate, then travel carefully

Use the destination Realmstone on the frame's **Power rune**. If the frame is rejected, check the size, empty interior, block names and four distinct rune types before spending more materials. Clicking the side facing into the opening is a useful way to avoid an orientation mistake.

A **Blank Realmstone** has a separate deactivation behavior when used on the Power rune of a lit portal. Do not use the blank as the destination key.

Before entering, put irreplaceable items away, take supplies, record your departure coordinates and plan to test the return route. Recipe and frame checks do not certify safe travel in every modpack or restored build.

## Common mistakes, quickly fixed

| Problem | Check |
|---|---|
| Food exchange does nothing | Ordinary `ItemFood`, input placement, free inventory slot, proximity to living Traveller |
| Book does not give another blank | Existing Blank Realmstone already found by its inventory search |
| Precasia recipe fails | All six different vanilla saplings, plus the blank; no substituted modded sapling |
| Power rune recipe search finds the wrong item | Historical output ID is `carved_rune_power` |
| Four carved runes still fail | Four distinct types, not four copies of one type |
| Portal shuts off instead of opening | Blank Realmstone used rather than destination stone |
| Ruins seem absent | Confirm structure configuration and explore appropriate newly generated terrain; no guaranteed search radius |

## 8. Turn the first return trip into a useful next session

You do not need to unlock every dimension before making progress. Pick one objective and bring back its exact ingredient, drop or resource. This is a suggested learning order, not an extra quest requirement imposed by the mod.

### A. Confirm your return route before carrying valuables

On the first visit, mark the arrival point, keep enough ordinary supplies to retreat and verify that you can get home. Store spare materials at your base. Portal construction evidence does not establish a safe spawn position, a chunk-loading guarantee or protection from another mod's travel changes.

**Ready to continue:** you have returned once and can explain how to reach your home storage again. If travel fails, diagnose the exact destination and release before crafting another set of portal parts.

### B. Choose one creature and one reward

Open the [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2), filter the dimension, and inspect a creature's location evidence and loot. A dimension association is not a guaranteed spawn coordinate. A loot entry's weight is not automatically its per-kill drop percentage.

Check [Hunter requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2) before selecting a Hunter-gated target. Server overrides can change the displayed defaults. Kill XP and ordinary loot have separate checks: a pet can receive credit through a route that does not satisfy the ordinary player-drop gate.

**Ready to continue:** you know the target, the desired item, its relevant conditions and whether your Hunter level is sufficient. If the target is inaccessible, choose a lower-level objective rather than assuming that better weapon damage bypasses its gate.

### C. Give your equipment a repeatable supply route

Before choosing a rune-consuming weapon, follow [Runation inputs and shrine layout](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runation-Rune-Shrines-and-Inputs-1.12.2). Check the exact required post, input type and level. The historical practice branch can consume the accepted stack without producing runes; an incomplete layout is not a harmless preview.

For a companion, compare [minion abilities](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Minion-Abilities-and-Choosing-Companions-1.12.2), then inspect its [slab recipe and Creation cost](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Creation-Minions-Slabs-and-Forge-1.12.2). Summoning and sacrificing at the forge are different actions. Summoning payment precedes the checked spawn attempt, so first test one affordable slab in a clear, safe area.

**Ready to continue:** you can replenish your chosen consumable, or have a reliable fallback. You are not relying on a rare item you cannot replace just to test an unfamiliar interaction.

### D. Train a skill through its checked action

Use the [15-skill historical training map](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Skill-Training-and-Availability-1.12.2) to select a working action and open its detailed guide. Do not spend resources trying to train a retained skill merely because its icon or armor tooltip exists. The scoped audits distinguish normal training routes from inactive or unresolved ones.

[Expedition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Expedition-Sprinting-Bonuses-and-Falls-1.12.2) explains eligible sprint timing and travel bonuses. [Butchery and Innervation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2) explains temporary combat pickups and why a pickup does not necessarily belong only to the player who caused it.

**Ready to continue:** you can name the action, eligibility conditions and expected kind of XP. If the expected gain is absent, check the server skill settings and the guide's gates before repeating an expensive action.

### E. Keep vanilla XP separate from skill XP

If your vanilla XP bar stops increasing while carrying an Exp Flask, consult [historical flask storage and recovery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Exp-Flask-Storage-and-Recovery-1.12.2). The first matching flask in the inspected inventory order captures eligible orbs. Holding a different one does not necessarily select the deposit target.

The flask's storage is not an AoA skill-level bank or death-insurance system. Its survival acquisition remains unresolved in the inspected scope, so it is an optional troubleshooting topic here, not a required starter item.

## Choose a next-session goal

| If you enjoyed… | A concrete next goal | Check before spending materials |
|---|---|---|
| Exploring | Choose one new realmstone route below | Exact trigger, location, input and consumption warning |
| Fighting | Select one eligible Hunter target and desired drop | Level, kill attribution, spawn evidence and loot conditions |
| Crafting | Produce the correct runes for one chosen weapon | Shrine layout, accepted input and output rules |
| Companions | Make and test one affordable minion slab | Ability, level, resource cost, spawn space and local ownership cap |
| Progression | Complete one verified skill-training action | Skill availability, server settings and callback conditions |

## Recovery checklist after an unsuccessful trip

- **No expected loot:** distinguish the random table from player-credit and Hunter eligibility checks. More attempts will not repair a failed eligibility condition.
- **No expected skill XP:** confirm that the action trains that particular skill, and that the skill system is enabled. Vanilla orb XP is a different system.
- **A crafting input disappeared:** inspect the workstation's consumption and failure ordering before retrying with a full stack.
- **A summon did not appear:** stop bulk attempts; inspect local ownership limits, valid spawn space and the guide's spawn-result warning.
- **An item or destination exists only in another release's guide:** switch the reference to 1.12.2. Similar names do not establish equivalent recipes or mechanics.

## Continue to the other destinations

[All 23 historical realmstone routes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-and-Challenges-1.12.2) compares the acquisition checks, exact recipes and item-consumption warnings for your next expedition.

## Evidence and limits

[Recipe and class evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/starter-portal-evidence-1.12.2.json) records exact released resources, sapling metadata ingredients, the successful-inventory-insertion food guard, book lookup and source frame coordinates. Source interpretation is pinned to [29dd8a8a20642ee182b851e34ef58b65f68e68bf](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf). Only the specified bytecode paths were independently checked; this is not a complete source/binary equivalence proof or live-game test.

Original diagrams use the matching 1.12.2 AoA and vanilla models/textures. AoA artwork belongs to Tslat and contributors; vanilla artwork belongs to Mojang/Microsoft. No original game/mod binaries are redistributed here.
