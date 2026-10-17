[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Historical skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Skill-Training-and-Availability-1.12.2) · [Modern Exp Flask guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Exp-Flask-Storage-and-Recovery-1.21.1)

# Historical Exp Flask: storing and reclaiming vanilla experience

> Minecraft 1.12.2 / AoA 3.3.6. Selected released callbacks and independent float32 arithmetic support this guide. It is not a save-safety or modpack compatibility certification.

![Actual empty and filled flask textures with capture and withdrawal rules](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/exp-flask-storage-and-use-1.12.2.webp)

## Why your experience bar may stop increasing

The historical Exp Flask intercepts eligible **vanilla XP orb pickups** while it is in the inspected player inventory. It stores the orb’s point value, cancels normal pickup, sets the orb’s value to zero and removes the orb entity.

Those are vanilla experience points, not AoA skill XP and not a number of player levels. The enchanting-level bar and an AoA skill level are separate systems. The selected code does not expose a player action that deposits already-earned experience from the bar into the flask.

[Open the historical Exp Flask item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExpFlask.name).

## Reclaim stored XP

1. Identify which flask actually has stored XP. A filled appearance means the selected capability value is positive; it is not a precise amount gauge.
2. Hold that flask and use it. The server right-click path rejects a missing capability or a nonpositive stored value, otherwise it sets the active hand.
3. Keep using it to withdraw points on eligible server using-ticks. It uses a drinking action and a maximum use duration of 100 ticks.
4. Watch the stored amount and vanilla XP level. The withdrawal rate depends on the player’s current vanilla experience level and can change as points are awarded.
5. If it empties, the selected using-tick method resets the active hand. The flask item itself is retained; this path does not consume the bottle.
6. To stop the selected automatic collection route, remove all matching flasks from the searched player inventory paths. Modded backpacks and external storage are outside this inspected search.

At healthy 20 TPS, 100 ticks is approximately five seconds. This is an item-use duration declaration, not a guarantee of exactly 100 award callbacks or a fixed total withdrawal. Releasing use, server timing and other mods can change the actual sequence.

## Which flask receives an orb?

The lookup returns the first matching item in this order:

1. Main inventory, in its list order.
2. Armor inventory.
3. Offhand inventory.

The pickup callback obtains the stack at that index. Holding a different flask does not override an earlier match in main inventory. With several flasks, check all their stored values before concluding that XP disappeared.

The handler requires server side and a positive orb value. It does not require the flask to be selected or actively used. The inspected lookup does not scan arbitrary nested containers or every modded accessory slot.

## Withdrawal rate

For ordinary nonnegative player levels, the requested rate is:

`1 + floor(vanilla experience level / 15)`

The method takes the smaller of that rate and stored value, converts it to an integer, awards that integer through player.addExperience, then subtracts it from the stored float.

| Player vanilla level | Requested points per eligible use tick |
|---|---:|
| 0–14 | 1 |
| 15–29 | 2 |
| 30–44 | 3 |
| 45–59 | 4 |
| 60–74 | 5 |
| 75–89 | 6 |
| 90–104 | 7 |

A flask with fewer points can supply only the remaining integer amount. Because awarding XP can increase the player’s level, do not multiply one initial rate by the use duration and call that an exact whole-session prediction.

## Empty and filled appearances

The model override uses the `filled` property: missing capability or a value ≤0 returns 0; a positive value returns 1. The two released item models select their corresponding empty/filled textures. The image above shows the actual texture pixels enlarged for inspection.

The tooltip casts the stored value to an integer and uses a formatted point count, with a derived vanilla-level estimate at sufficient stored XP. That display is not a separate exact integer ledger.

## Persistence and transfer

Storage uses the historical serializable item capability with a **float** value. Its provider serializes to NBTTagFloat and restores that float. The share-tag methods use the AdventMiscStackCapability field to synchronize the value.

This establishes the selected persistence/synchronization path, not a guarantee that every transfer, copy, death, inventory replacement or other mod preserves it. Test save/reload, dropping and picking up the flask, chest transfer, reconnect and modded inventory handling with a small known amount before relying on a valuable stored balance.

No death-insurance behavior is established by these selected methods. Do not assume that the flask or its balance is protected from ordinary item loss just because it stores XP.

## Important failure and precision limits

### Missing capability can lose an intercepted orb

The pickup callback calls addExp, then cancels pickup and removes the orb. The addExp helper silently does nothing if the capability is missing and does not return a success result to the pickup handler. Therefore the inspected ordering does not guarantee rollback if a broken or incompatible flask lacks its capability.

The use-start path checks for a missing capability, but some later tooltip/share-tag/using-tick paths dereference it directly. Test capability failure and item replacement during use instead of assuming all paths safely ignore a damaged stack.

### Float storage is not an exact unlimited bank

The setter stores the provided float without an explicit clamp in the inspected implementation. That is not evidence of unlimited exact integer capacity. Float32 spacing grows with magnitude.

| Independent arithmetic example | Stored result | Meaning |
|---|---:|---|
| 16,777,216 stored + 1 XP | 16,777,216 | The increment can round away |
| 16,777,218 stored + 1 XP | 16,777,220 | Rounding can increase by 2 for a 1-point input |
| 16,777,218 stored − a 1-point withdrawal | 16,777,216 | Stored balance can decrease by 2 for that request |
| 33,554,432 stored − a 1-point withdrawal | 33,554,432 | That subtraction can round back to the same balance |

These examples reproduce the selected float arithmetic, not a measured live farming exploit or a guarantee of an entire withdrawal session. Player level and subsequent withdrawal size can change as XP is awarded. A restored implementation should choose an exact, validated storage representation and an explicit supported range.

A fractional positive value below 1 is another edge case: the appearance can be filled while the integer withdrawal becomes zero and leaves the fractional value unchanged. Ordinary inspected deposits add integer orb values, so this is primarily a modified/corrupt-state or integration test rather than an asserted normal acquisition path.

## Acquisition is unresolved in the inspected survival routes

The artifact contains the Exp Flask class and empty/filled model definitions. The scoped search found no exp_flask recipe or loot-table JSON match. Direct named EXP_FLASK field references appeared only in item registration and the XP-pickup handler.

This does not rule out every generic integration or external pack recipe. It does mean this guide will not invent a historical crafting recipe or copy the newer edition’s acquisition instructions. A restored build needs a verified obtainable route before claiming a complete survival loop.

## Compatibility and restoration tests

- Test first-match selection with two flasks in different main slots and offhand.
- Test positive/zero-value orbs, a missing capability and full or unusual inventory states.
- Compare stored points, tooltip count and filled appearance before and after every transfer.
- Test use cancellation, final-point withdrawal, level transitions at 14/15, 29/30 and 44/45, and a flask emptied during use.
- Test large balances around float32 precision boundaries and reject invalid negative/nonfinite custom values in any replacement implementation.
- Check Mending and other XP-pickup listeners in the real target Forge/modpack event order. This guide does not infer that interaction solely from the AoA callback.
- Keep vanilla XP withdrawal separate from AoA skill XP modifiers and training rules.

## Evidence

[23 released methods, 63 one-tick withdrawal models and 18 deposit models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/exp-flask-evidence-1.12.2.json) · [Texture provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/exp-flask-art-evidence-1.12.2.json)

No Java or Minecraft code was executed. AoA textures and systems: Tslat and contributors. [Pinned source context](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source).

[Modern Exp Flask differences](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Exp-Flask-Storage-and-Recovery-1.21.1) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
