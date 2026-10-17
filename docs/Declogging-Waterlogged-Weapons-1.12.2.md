# Declogging waterlogged weapons

**Minecraft 1.12.2 · AoA 3.3.6.** The Declogging Table contains five checked conversion branches. This guide explains what the table does **if you already have a valid waterlogged item**. The input items have no direct references in this release’s bundled recipe/loot JSON scan; their normal survival acquisition remains unresolved.

## Restore an item

1. Locate an existing Declogging Table. The released Aquatic Castle structure places one at local authored offset **(20, 2, 17)**. That is a structure-relative placement, not a universal world coordinate.
2. Hold one of the five waterlogged items below in the hand used to activate the table. The handler uses the supplied hand rather than hard-coding the main hand.
3. Activate the table. On the server, the code constructs one fresh output stack and gives it to your inventory or drops it if insertion fails, then shrinks the waterlogged input by one and plays the table sound.
4. Check your inventory and nearby ground. Leave room before using rare inputs; the helper’s drop fallback is not protected storage.

No rune, fuel, timed progress bar or additional material is read by this activation branch. There is no Creative exemption around the input shrink in the checked method. A click returning “handled” is not proof of a conversion: the method also returns true when its conversion condition does not match.

| Waterlogged input | Restored output and usage guide | Conversion |
|---|---|---|
| Waterlogged Aqua Cannon | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-aqua_cannon.webp" width="88" height="88" alt="Aqua Cannon"><br>[Aqua Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cannon-Ammunition-and-Armor-Scaling-1.12.2) | 1 input → 1 fresh output |
| Waterlogged Coral Archergun | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-coral_archergun.webp" width="88" height="88" alt="Coral Archergun"><br>[Coral Archergun](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Archergun-Ammunition-and-Special-Effects-1.12.2) | 1 input → 1 fresh output |
| Waterlogged Coral Cannon | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-coral_cannon.webp" width="88" height="88" alt="Coral Cannon"><br>[Coral Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cannon-Ammunition-and-Armor-Scaling-1.12.2) | 1 input → 1 fresh output |
| Waterlogged Coral Clogger | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-coral_clogger.webp" width="88" height="88" alt="Coral Clogger"><br>[Coral Clogger](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2) | 1 input → 1 fresh output |
| Waterlogged Reefer | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-reefer.webp" width="88" height="88" alt="Reefer"><br>[Reefer](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blaster-Energy-Timing-and-Spark-Exceptions-1.12.2) | 1 input → 1 fresh output |

## What is preserved?

The activation branch creates a new ItemStack from the mapped output Item. It does not copy the input stack’s custom name, damage, enchantments or arbitrary NBT. Treat custom input data as non-preserved unless a separate mod explicitly changes this behavior.

The fixed-item switch handles indices 0 through 4. An unsupported index returns null. The five registered waterlogged items use valid indices, but an injected or modified item with another index is not covered by that guarantee.

## Finding the station

The Aquatic Castle build method places the table, and the L’Borean chunk-population method has an AquaticCastle generation call gated by its configured positive random bound and terrain check. This establishes a code path, not a promise that a particular explored chunk contains the castle.

The table constructor supplies hardness −1 and a very large resistance input. This is not an ordinary portable workstation recipe; use an existing placed table rather than assuming it can be mined and carried home. Actual break behavior, protections and modpack overrides require runtime checks.

## Important L’Borean generation-settings bug

The checked released bytecode tests **drownedLottoStandSpawnChance > 0**, but then passes **aquaticCastleSpawnChance** to Random.nextInt for the Drowned Lotto Stand branch. The default constructor values are 550 and 1700 respectively. The enabled flag and random bound therefore come from different settings.

- A positive stand setting with a non-positive castle setting can reach a non-positive Random.nextInt bound after the castle branch is skipped. That is a static exception path; it has not been reproduced in a running world here.
- With both settings positive, the stand’s random draw still uses the castle bound. Because this is an else-if chain with terrain tests, do not interpret either number as a complete independent structure probability.
- Do not assume disabling only castle generation is a safe workaround for this historical build. An implementation fix should use the positively checked stand setting as the stand’s own random bound.

### Restoration implementation checklist

- [ ] Use drownedLottoStandSpawnChance for its own random draw.
- [ ] Test castle/stand settings independently with zero, negative, one and normal positive values.
- [ ] Preserve terrain eligibility and else-if ordering unless intentionally redesigned.
- [ ] Test five valid conversion indices, invalid indices, both hands, full inventory, custom NBT and Creative input consumption.
- [ ] Establish the waterlogged input acquisition routes separately before advertising a complete survival loop.

## Sources and limits

[Released method evidence, hashes and configuration boundary](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/declogging-evidence-1.12.2.json) · [Acquisition atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Weapon-Acquisition-1.12.2)

This is static released-artifact analysis. No Minecraft world, player inventory or private Enderloom build was modified or executed. The suggested generation fix and test checklist are requirements, not claims of an implemented patch. Models and textures are by Tslat and contributors.
