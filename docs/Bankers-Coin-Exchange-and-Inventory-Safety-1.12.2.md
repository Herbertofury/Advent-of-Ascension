# Bankers, coin exchange and inventory safety · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** Five banker NPC types select the same BANKER interface. Their EMPTY→EMPTY trader entries are placeholders; the real currency conversion is implemented by a dedicated six-lane container. This guide documents that interface rather than inventing free trades.

![Labeled source banker layout and six currency conversions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/banker-layout-and-conversions-1.12.2.webp)

## Use the exchange interface

1. Approach a living banker and open its exchange screen. The container’s interaction check requires its stored player to remain within squared distance 64, equivalent to 8 blocks in the ordinary distance metric. GUI target lookup is a separate nearby-entity step.
2. **Manually place the matching coin into the chosen input slot.** The first three lanes combine 20 smaller coins into one larger coin; the other three split one larger coin into 20 smaller coins. Realm tokens are not accepted by these four-coin lanes.
3. Wait for the output preview, then take the complete result into sufficient empty inventory space. A combine lane needs at least 20 input coins; a split lane needs one.
4. **Check both balances.** The released output callback charges a fixed 20 or 1 input coins and rebuilds its preview. The static partial-transfer risk below is a reason to avoid nearly-full-inventory shift-taking until that path is verified in the target build.
5. Close the screen when finished. On the server, the close handler sends the input inventory through inherited container cleanup. The generated output previews are not persistent bank storage or an additional owned balance.

## Six lanes, one shared system

| Input | Output | Direction |
|---|---|---|
| 20 × Copper Coin | 1 × Silver Coin | Combine |
| 20 × Silver Coin | 1 × Gold Coin | Combine |
| 20 × Gold Coin | 1 × Lunaver Coin | Combine |
| 1 × Silver Coin | 20 × Copper Coin | Split |
| 1 × Gold Coin | 20 × Silver Coin | Split |
| 1 × Lunaver Coin | 20 × Gold Coin | Split |

The conversion ratio is **20:1 at each adjacent tier**, not 100:1. Under these declared rates, one Silver equals 20 Copper, one Gold equals 400 Copper, and one Lunaver equals 8000 Copper. These equivalences describe the inspected conversion logic; they do not price realm tokens or guarantee access to a banker.

## Which NPCs use it?

| Banker | Shared interface |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/inherited-creep_banker-thumb.webp" width="64" height="64" alt="Creep Banker"><br>[Creep Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3:creep_banker) | The same six-lane BANKER container |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/e602a41dae558842b0eaadee-thumb.webp" width="64" height="64" alt="Lelyetian Banker"><br>[Lelyetian Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3:lelyetian_banker) | The same six-lane BANKER container |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/38f8d5fdec6187de4f21eeeb-thumb.webp" width="64" height="64" alt="Primordial Banker"><br>[Primordial Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3:primordial_banker) | The same six-lane BANKER container |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/inherited-shyre_banker-thumb.webp" width="64" height="64" alt="Shyre Banker"><br>[Shyre Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3:shyre_banker) | The same six-lane BANKER container |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/63cbb47076c8a02a49ee8901-thumb.webp" width="64" height="64" alt="Zal Banker"><br>[Zal Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3:zal_banker) | The same six-lane BANKER container |

These are five NPC appearances of the same conversion mechanism, not thirty unique market offers. Their spawning/despawning and realm access are separate from the shared conversion logic.

## Shift-click behavior worth knowing

The player-inventory quick-move loop only tries banker inputs that already contain a matching item. It skips empty input slots. If your first coin will not shift into an empty lane, place it manually rather than assuming the exchange is broken.

The inspected ranges use end-exclusive bounds. The container has twelve banker slots, twenty-seven main-inventory slots and nine hotbar slots, but its quick-move destinations omit the final hotbar slot in two paths and the final main-inventory slot in another:

| Route | Passed range | Excluded destination slot |
|---|---|---|
| Banker slots → player inventory | [12,47) | Container slot 47, the last hotbar slot |
| Main inventory → hotbar fallback | [39,47) | Container slot 47 |
| Hotbar → main inventory fallback | [12,38) | Container slot 38, the last main-inventory slot |

This is a source-level range finding against the inspected inherited merge contract. It is not a claim that normal manual placement into those slots is unavailable. Forge patches and target-build behavior still require verification.

## Partial-output value-loss candidate

**Static finding, not a reproduced in-game defect:** the quick-move path can call the output slot’s onTake after a partial successful merge. That callback ignores the transferred count, subtracts its fixed input charge, then recomputes the output preview.

In the bounded model, splitting one Silver into twenty Copper while only one Copper fits moves one Copper, charges the full Silver, and clears the old remainder when the input becomes empty. Nineteen Copper-equivalent units are then missing from that modeled transaction. With space for the full twenty, the same modeled exchange conserves value.

The evidence includes 252 input/capacity cases; 54 exhibit this partial-output pattern. These are original arithmetic models tied to inspected callbacks, not 252 Minecraft game tests. The vanilla merge comparison does not prove that every Forge/modpack hook uses identical behavior.

A prudent target-build test should cover normal pickup, right-click pickup, shift-click, partial destination stacks, full inventories, repeated exchanges, closing, disconnecting and multiplayer synchronization. Do not mark the current owner-local build defective or fixed solely from this older released implementation.

## GUI target safety

All five bankers request the BANKER enum. The server-side GUI branch constructs ContainerBankerTrade with the nearby-target lookup result without a local null check; the constructor then reads the banker’s display name. The client branch does check for null. An absent/stale target is therefore a separate source-level null-dereference candidate to validate and guard in a restoration. No crash was induced here.

## Compare prices using the checked ratio

The checked historical offers list **one Silver Coin for five Grenades** at Gorb Arms Dealer, versus **five Copper Coins for one Grenade** at Explosives Expert. At the banker’s 20:1 ratio, those nominal costs are four versus five Copper per Grenade. This arithmetic comparison assumes access to both conversion and the relevant offers; it does not promise simultaneous stock, NPC availability or a universal discount. [Compare Grenade offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Agrenade).

## Restoration acceptance checklist

- [ ] Compare the current implementation with these released 3.3.6 methods before assigning an active defect.
- [ ] Preserve all four currency identities and all six conversion directions.
- [ ] Ensure partial output delivery cannot charge for an undelivered remainder; reject an incomplete bundle or account for paid leftovers correctly.
- [ ] Check every inventory boundary, including container slots 38 and 47.
- [ ] Handle empty, removed, out-of-range or stale GUI target entities safely on the server.
- [ ] Verify input cleanup, disconnect/reconnect, ordinary and modified clicks, packet ordering and multiplayer behavior in the target game.
- [ ] Require before/after value conservation and measured performance without changing existing capabilities.

## Evidence

- [Released container, anonymous-slot, banker and GUI-route receipts; 252 scoped models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/banker-exchange-evidence-1.12.2.json).
- [Source-layout diagram provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/banker-diagram-evidence-1.12.2.json).
- [Historical trading handbook](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trading-and-Traders-1.12.2) · [Weapon buying and upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Buying-Weapons-and-Trader-Upgrades-1.12.2).
- AoA artwork and systems by Tslat and contributors; vanilla reference methods by Mojang. This is independent static documentation, not a game screenshot or runtime acceptance report.
