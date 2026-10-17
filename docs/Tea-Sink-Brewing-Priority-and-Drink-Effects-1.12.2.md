# Tea Sink brewing, priority and drink effects · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** Make the sink and cups, fill it, then choose the tea by controlling which ingredients you carry. This is the historical system; the [1.21.1 Tea Sink guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Tea-Sink-Brewing-and-Ingredient-Priority-1.21.1) is kept separate.

## Craft the equipment

![Exact Tea Sink and Cup crafting patterns](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/tea-sink-and-cup-recipes-1.12.2.webp)

- **Tea Sink:** five `plankWood` Ore Dictionary ingredients, one Iron Ingot and one Cauldron, in the pictured pattern. [Open the exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ablocks%2Ffunctional%2Futility%2Ftea_sink).
- **Cups:** three Ivory in the pictured V shape produce **three Cups**. [Open the exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fmisc%2Fcup).
- Achony Planks are shown as a representative: their released declaration passes `plankWood` to the registration helper. Actual Ore Dictionary membership depends on the active Forge environment. The recipe does not demand that particular wood.
- Gather **Tea Shreddings** from the Tea crop; use the [crop planting/harvesting guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2) and [seed acquisition reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Finding-Seeds-and-Starting-a-Farm-1.12.2) for that stage.

The recipe browser now labels Ore Dictionary ingredients explicitly instead of showing an unnamed ingredient. It does not invent a complete runtime list of alternatives.

## Fill and brew

![Empty and full sink states, held cup and tea ingredient priority](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/tea-sink-priority-1.12.2.webp)

1. Place the Tea Sink. Use a **Water Bucket on the empty sink**. On the server, the non-Creative branch consumes the held bucket stack by one and gives or drops an empty Bucket; the sink switches to its full state.
2. Hold a **Cup in the hand used to interact**. The full sink also checks for a Tea Shreddings stack in the player inventory before attempting a brew.
3. For **Fungal Tea**, carry Mystic Shrooms. This is checked first.
4. For **Natural Tea**, remove accessible Mystic Shrooms and carry a Nature Melon Slice. This branch is checked only when the Mystic Shrooms lookup fails.
5. For plain **Tea**, remove both additives from the helper’s accessible inventory and carry Tea Shreddings.
6. A successful ordinary Survival brew consumes one Tea Shreddings, one Cup and, for an additive tea, one of the selected additive. It gives or drops one finished drink, plays the use sound, then makes the depletion roll.

The additive helper checks held main hand, offhand, main inventory and armor inventory in its one-item search. Merely moving an additive to the other hand is therefore not a reliable way to select the lower-priority tea. These steps describe normal matching items and successful server callbacks; modified inventory behavior needs separate testing.

### Ingredient priority at a glance

| Accessible Mystic Shrooms | Accessible Nature Melon Slice | Ordinary Survival result |
|---|---|---|
| Yes | Either | Fungal Tea |
| No | Yes | Natural Tea |
| No | No | Tea |

All three rows still require a full sink, the held Cup and the outer Tea Shreddings inventory check. The sink does not provide a menu to choose between all three while carrying every ingredient.

## Water is random-use, not seven fixed charges

After each successful brew, the released code draws `nextInt(7)` and empties the sink when the result is zero. That is a **1/7 depletion roll per successful brew**, including the brew that produced the drink.

Under an independent, unchanged random-draw model, the expected number of drinks before depletion is seven. A sink can drain after the first drink or last longer than seven; about **34%** remain full after seven successful brews. No exact seven-cup capacity is stored here.

Refill an empty sink with another Water Bucket. The empty/full transition preserves its facing. The released block’s pick/drop methods return the empty Tea Sink item, and Silk Harvest is disabled; do not expect breaking it to retain the full state.

## Drink effects and returned Cups

![Three teas with exact requested effects and durations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/tea-effects-and-cup-returns-1.12.2.webp)

| Drink | Regeneration request | Resistance request | Container returned by server callback |
|---|---|---|---|
| Tea | Level II, 50 ticks | Level I, 130 ticks | One Cup |
| Fungal Tea | Level IV, 75 ticks | Level I, 60 ticks | One Cup |
| Natural Tea | Level I, 50 ticks | Level II, 150 ticks | One Cup |

Effect amplifier values are zero-based in the code; the table shows player-facing levels. At 20 ticks per second, those durations are 2.5/6.5 seconds for Tea, 3.75/3 seconds for Fungal Tea, and 2.5/7.5 seconds for Natural Tea. Tick lag can change elapsed wall-clock time.

All three are marked always edible and use the drink action. Each has **zero configured hunger** and a 0.5 saturation modifier; zero hunger means no saturation addition in the vanilla food comparison. These are effect drinks, not ordinary meals. Their server food callback gives or drops one Cup.

Do not convert a Regeneration duration into a guaranteed total heal without checking tick phase, existing effects, health cap and hooks. Nor should “Natural” be read as universally stronger: it requests longer, higher-level Resistance but lower-level Regeneration than the other teas.

## Creative mode differs

The shared `findInventoryItem` helper returns true early for Creative players. Once the full-sink, held-Cup and outer Tea Shreddings gates pass, its first additive lookup can therefore select **Fungal Tea even without Mystic Shrooms**. The ordinary Survival ingredient-priority table should not be used to predict that Creative branch.

The sink explicitly skips Cup consumption in Creative, and the helper’s early return skips ingredient consumption. The successful-brew depletion roll still exists. This is a checked source path, not an in-game reproduction or a claim that a current restoration must retain every historical quirk.

## Troubleshooting and restoration checks

- **Wrong tea:** inspect both hands and accessible inventory for higher-priority additives.
- **No brew:** distinguish full/empty state, the actually used hand and the outer Tea Shreddings gate. The activation method returns true even on some no-op paths, so a successful interaction return alone is not proof of a produced drink.
- **Unexpected depletion:** a first-cup drain is allowed by the source roll.
- **Missing drink or returned Cup:** the helper uses give-or-drop behavior. Test full inventory, pickup ownership and server/client synchronization rather than promising direct slot insertion.
- **Migration:** preserve empty/full state and facing intentionally; test survival/creative selection separately. The additive branches do not separately check the return value of the subsequent Tea Shreddings consumption call, so unusual inventory compatibility deserves a targeted test.
- This walkthrough checks released methods, source-derived diagrams and 64 bounded selection cases. It does not certify runtime compatibility, resource migration or game performance.

## Evidence

- [Released Tea Sink, helper, tea and recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tea-sink-evidence-1.12.2.json).
- [Artwork provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tea-art-evidence-1.12.2.json).
- [Historical fish cooking and hunger-scaled healing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cooking-Fish-and-Hunger-Scaled-Healing-1.12.2), [furnace conversions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Furnace-Recipes-and-Material-Recycling-1.12.2), and [modern tea brewing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Tea-Sink-Brewing-and-Ingredient-Priority-1.21.1).
- Original AoA art and mechanics by Tslat and contributors; vanilla references by Mojang. Original documentation compositions; no game or mod code was executed.
