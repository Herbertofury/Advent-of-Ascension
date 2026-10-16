# Portal support and preparation · 1.20.1

**Pinned release: Minecraft 1.20.1 / AoA 3.7.1.** This page helps distinguish an incomplete frame from a destination that this stock release does not connect to a portal. It does not certify the user's separately modified Enderloom build.

![Nether, Nowhere and Precasia Realmstones have non-null portal references in the inspected release; nineteen others do not](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/portal-support-1.20.1.webp)

[Visual tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.20.1) · [Version matrix](Version-Matrix) · [Current implementation acceptance](Runtime-Acceptance-Checklist)

## Start here: what message did you get?

| What happens | What it means in the inspected release | Next step |
|---|---|---|
| The game says the dimension is still in development | The selected Realmstone's portal reference is null; the rejection occurs **before** frame validation | Check the support list below; repeatedly rebuilding the frame cannot create the missing portal reference |
| The game suggests something is missing | The activation path reached frame checking and received an invalid result | Check frame dimensions, opening, distinct runes and clicked Power rune |
| The portal remains lit and no longer needs the key | Existing-portal result | Do not treat this as an unimplemented-destination message |
| A realm appears in a resource list or creative inventory | Presence alone says nothing conclusive about ordinary portal access | Check the released constructor wiring and the exact build you run |

The diagnostic wording above is paraphrased. Packs may translate, replace or alter it.

## Which Realmstones have portal references?

The released `AoAItems.class` contains **22 inspected destination Realmstone constructor lambdas**. Exactly three supply an actual portal field:

| Realmstone | Released portal field | Scope of this finding |
|---|---|---|
| Nether | `NETHER_PORTAL` | Portal reference present |
| Nowhere | `NOWHERE_PORTAL` | Portal reference present |
| Precasia | `PRECASIA_PORTAL` | Portal reference present |

The other **19 pass null**:

Abyss, Barathos, L'Borean, Candyland, Celeve, Creeponia, Crystevia, Deeplands, Dustopia, Gardencia, Greckon, Haven, Iromine, Lelyetia, Lunalus, Mysterium, Runandor, Shyrelands and Vox Ponds.

A non-null reference is a narrower result than “the whole dimension works.” It does not prove safe arrival, a complete return route, functioning structures, all mobs, progression, multiplayer or save migration. Those still need gameplay acceptance testing.

Conversely, a null reference describes **this stock 3.7.1 activation route**. A custom implementation can replace it. Do not use this list to dismiss verified work in a different build.

## Why the dimension files can mislead you

This JAR contains dimension JSON resources named Barathos, Deeplands, L'Borean, Lelyetia, Nowhere, Precasia and Precasia Backup. Some names therefore appear in the archive even though their destination Realmstone passes null.

These are different layers:

1. An item or localized name can exist.
2. A dimension resource can exist.
3. A Realmstone can have a usable portal reference.
4. A portal can activate and transfer a player.
5. The destination and its return/progression loop can actually work.

Do not mark all five complete from evidence for the first one. “Precasia Backup” is a resource name in this inspection, not a recommended player destination or an instruction to teleport there.

## Prepare the Power rune with the correct recipe

The release defines a shaped recipe using **7 Unpowered Runes, 1 Ancient Rock and 1 Eye of Ender**:

| Unpowered Rune | Eye of Ender | Unpowered Rune |
|---|---|---|
| Unpowered Rune | Ancient Rock | Unpowered Rune |
| Unpowered Rune | Unpowered Rune | Unpowered Rune |

There is a separate all-Charged-Rune variant with the same Eye of Ender and Ancient Rock layout. Follow one exact recipe. These definitions do not establish that arbitrary mixtures of the two rune types work.

**Use a stonecutter:** one Runium Chunk produces **16 Unpowered Runes** in this 1.20.1 release. The historical 1.16.5 shapeless-crafting instruction is not interchangeable with this recipe. Likewise, do not assume every additional modern 1.21.1 recipe variant exists here.

Use the [Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html) with **1.20.1 selected** to inspect the exact resource and its ingredients. Modpack recipe changes should be checked in the actual game.

## Nowhere is not a free early-game shortcut

The shipped shapeless Nowhere Realmstone recipe requires all six of:

- One item matching the Forge shulker-box tag
- Nether Star
- Void Scales
- Recovery Compass
- Redstone Lamp
- Blank Realmstone

The tag allows compatible tagged items rather than asserting that one particular colored box is mandatory. Ingredient acquisition and final travel safety are separate from the recipe's existence. Use an empty expendable box when testing a recipe; do not risk stored valuables based on a documentation assumption about crafting remainders.

This page does not transplant the 1.16.5 realmstone acquisition checklist into 1.20.1. A matching item name is insufficient evidence that an old acquisition trigger survived unchanged.

## Practical troubleshooting order

1. Record the Minecraft version, AoA filename and any pack-specific build identifier.
2. Match the failure to the diagnostic table before changing blocks.
3. If the destination is one of the nineteen null-reference entries in the stock release, stop spending materials on repeated frame reconstructions for that stone.
4. If the destination has a reference, check the frame and your actual installed recipe/tag overrides.
5. Back up the save before testing an unverified custom portal or migration. Keep your departure coordinates and test the return journey with expendable equipment.
6. Report the build, destination, exact feedback and whether activation, arrival or return failed. “The portal is broken” hides the distinction needed to fix it.

## What the restoration needs to prove

For each restored destination, track these separately:

- [ ] Realmstone item and intended survival acquisition
- [ ] Non-null portal registration and correct target dimension
- [ ] Frame validation and activation feedback
- [ ] Safe arrival and reliable return
- [ ] Structures, biome content, entities and loot
- [ ] Progression prerequisites and unlocks
- [ ] Save/reload, multiplayer and migration acceptance
- [ ] Measured performance with the restored content enabled

## Evidence

[Released-class and recipe audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/portal-support-evidence-1.20.1.json) records all 22 exact constructor-lambda shapes, class hashes, portal-field/null values, the early rejection branch and the recipe resources. The audit rejects unexpected bytecode shapes rather than guessing at them. No game was launched for this inspection.

The later upstream `1.20` source snapshot available to this documentation uses different registration APIs. This finding therefore relies on the **actual 3.7.1 released classes**, rather than assuming that a similarly named branch is the binary's exact source. Resource and code evidence are not full runtime certification.

Original diagram uses release-matched AoA item previews. AoA artwork and systems are by Tslat and contributors. Official game/mod binaries are not redistributed by this page.
