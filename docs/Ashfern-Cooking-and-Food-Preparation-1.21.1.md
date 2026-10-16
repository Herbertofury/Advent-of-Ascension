# Ashfern cooking and food preparation · Minecraft 1.21.1

**Version:** released AoA 3.7.16.1. Ashfern is a crafting ingredient that asks the current smelting recipe system what an edible input should become. It is not a furnace block, and its small custom recipe declaration has no single fixed output.

[Grow Ashfern on the right support](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Farming-Soils-and-Harvesting-1.21.1) · [Search the recipe atlas](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=ashfern) · [Fishing and catch pools](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hauling-Rods-and-Fishing-Pools-1.21.1)

![Ashfern plus five named foods, with all five corresponding smelting results](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ashfern-cooking-workflow-1.21.1.webp)

## 1. Grow or obtain Ashfern

Ashfern Seeds use exact **Basalt** support in the inspected crop implementation. Polished Basalt, another basalt-looking block or ordinary farmland is not automatically equivalent. Follow the farming guide's light, maturity and harvest instructions; the seed and harvested Ashfern item have different jobs.

Keep some harvested Ashfern for cooking. The custom cooking recipe does not plant seeds or operate on the standing crop.

## 2. Use two separate occupied ingredient slots

1. Put **Ashfern** in one crafting-input slot.
2. Put one kind of food you want to transform in another slot. A normal player's 2×2 crafting grid has sufficient area for the recipe's dimension check.
3. Leave other ingredient slots empty. The matcher requires exactly **two occupied ingredient entries**, not exactly two individual items across stack counts.
4. Check the output preview before taking it. It comes from the selected smelting recipe for that food in the current recipe manager.
5. Take the intended result using ordinary crafting. This recipe path does not operate a furnace timer or require a fuel slot. Do not assume it awards the furnace recipe's XP merely because it borrows its result.

The arrangement is shapeless. Two occupied Ashfern slots fail; two food slots without Ashfern fail; adding a third occupied ingredient slot fails. A larger stack in one valid slot does not count as several occupied entries, but this is not a promise that one operation transforms the entire stack.

## 3. Check what “eligible food” actually means

The matcher checks that the non-Ashfern input exposes food properties and has a matching **smelting** recipe with a non-empty result. A smoking-only recipe is insufficient for this lookup. An edible item with no matching smelting recipe is also insufficient.

The output itself is **not required to be food**. Parapiranha is a useful example: its shipped smelting result is **Hardened Parapiranha**. Conversely, Hydrone has a smelting recipe that produces iron but is registered as a miscellaneous item in the inspected source. Its furnace recipe alone does not make it an eligible Ashfern food input.

Datapacks and other mods can change food components, recipes and which result is selected. The source registration checks and released recipe files below describe a bounded stock reference, not all possible modpack combinations.

## 4. Twenty fish share the Cooked Fish result

![Twenty named fish with shipped recipes producing Cooked Fish](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ashfern-fish-inputs-1.21.1.webp)

Each of these has a direct food registration in the pinned source and an explicit released smelting recipe producing **1 Cooked Fish**:

- Blue Gemtrap, Green Gemtrap, Purple Gemtrap, Red Gemtrap, White Gemtrap and Yellow Gemtrap
- Candlefish, Charred Char, Crimson Skipper and Crimson Stripefish
- Dark Hatchetfish, Ironback, Pearl Stripefish and Razorfish
- Reeftooth, Rocketfish, Sailback, Sapphire Strider, Turquoise Stripefish and Violet Skipper

Do not use their shared cooked result to infer identical raw effects, acquisition locations or Hauling requirements. Those belong to their own fish and catch-pool records.

## 5. Five other explicit AoA routes

| Edible input | Released smelting result borrowed by the recipe |
|---|---|
| Raw Charger Shank | 1 Cooked Charger Shank |
| Raw Giant Lizard Meat | 1 Cooked Giant Lizard Meat |
| Raw Halycon Beef | 1 Cooked Halycon Beef |
| Raw Rainbowfish | 1 Cooked Rainbowfish |
| Parapiranha | 1 Hardened Parapiranha |

Together with the twenty fish, this page covers **25 explicit AoA input routes and six distinct outputs**. This is not a complete vanilla-food or modded-food list. Inspect a candidate's actual food component and smelting recipe rather than guessing from its name.

## Why the result slot is empty

| Symptom | Check |
|---|---|
| Seeds plus food do nothing | Use harvested Ashfern, not Ashfern Seeds. |
| You supplied three useful ingredients | Exactly two occupied input entries are required. |
| The item cooks in a smoker but fails here | The implementation specifically looks up a smelting recipe. |
| An ore or Hydrone smelts but fails here | The input must also expose food properties. |
| An edible item fails | A non-empty matching smelting result is required too. |
| Your modpack produces a different result | Recipe/datapack overrides can change the selected recipe; read the preview. |
| The web recipe card has no fixed output | This is a dynamic custom recipe. Follow the input's smelting route instead of expecting a universal result. |

## Evidence and compatibility limits

The match method uses the supplied level; the inspected assembly method obtains the server's **Overworld** before looking up the smelting result. It returns an empty stack if that level is unavailable and copies the selected output. This deserves exact-build testing for client recipe previews, custom dimensions and altered server lifecycle. It is not evidence that all such scenarios currently fail.

[Released recipes, class hashes, selected method bytes and input-registration checks](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/ashfern-cooking-evidence-1.21.1.json) · [Illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/ashfern-art-evidence-1.21.1.json).

The 25-route list deliberately includes only explicit AoA item ingredients with direct food registrations found by this audit. Custom food subclasses, tag ingredients, vanilla recipes and other mods need their own verification. No game mod code was executed; no private Enderloom runtime behavior or performance gain is certified.

AoA models, textures and systems are by Tslat and contributors. The recipe illustrations are original source-derived documentation, not in-game screenshots.
