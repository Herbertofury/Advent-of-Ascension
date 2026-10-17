# Fish food and cooking · 1.16.5 and 1.20.1

Choose the exact release before using a recipe or nutrition value. This reference checks AoA 3.6.11 for Minecraft 1.16.5 and AoA 3.7.1 for Minecraft 1.20.1. It does not certify an Enderloom merge or runtime compatibility.

## A useful migration rule

Both inspected releases have 27 selected fish foods and 63 explicit cooking recipes. Their nutrition/modifier values match the checked 1.21.1 release for these same 27 IDs. Historical 1.12.2 cooked-species healing values must not be carried forward.

- Twenty inputs become generic Cooked Fish: 6 hunger, saturation modifier 0.85, with no AoA HealingFood callback.
- Raw Rainbowfish becomes Cooked Rainbowfish: 6 hunger, modifier 0.85, maximum extra healing 5 health points scaled by pre-meal missing hunger.
- Jamfish has 5 hunger and modifier 0.5.
- Chocaw, Jamfish, Parapiranha and Skelecanth have no matching cooking resources in either inspected artifact. Pack-added recipes remain possible.

## Cooking walkthrough

1. Select your Minecraft release in the recipe browser linked below.
2. Choose one of the 21 listed raw inputs. Raw Rainbowfish keeps its distinct output; the other twenty converge on Cooked Fish.
3. Use a fueled furnace/smoker or a suitable lit campfire. Each recipe produces one item.
4. Check your hunger before choosing healing food. Cooked Rainbowfish requests 5 × min((20 − pre-meal hunger) / 6, 1) health points. At hunger 19 this is about 0.8333 health, not five. Actual healing is limited by missing health and hooks.

| Method | Cook time | Nominal duration at 20 TPS | Recipe XP |
|---|---:|---:|---:|
| Furnace | 200 ticks | 10 seconds | 3.0 |
| Smoker | 100 ticks | 5 seconds | 3.0 |
| Campfire | 600 ticks | 30 seconds | 3.0 |

Durations are recipe parameters, not measured machine throughput. XP collection and custom machinery can behave differently.

## Effects: distinguish source labels from released fields

The corresponding pinned source labels the three requests Speed (Jamfish), Conduit Power (Cooked Fish) and Luck (Cooked Rainbowfish). Released suppliers independently confirm 600 ticks and probability 1. Their inspected EffectBuilder defaults use amplifier 0, ambient false, particles and icon enabled. The evidence retains the released SRG field names; their registry identities have not been independently remapped in this pass. Labels below are explicitly source-declared.

| Food | Source-declared request | 1.16.5 released field | 1.20.1 released field |
|---|---|---|---|
| Jamfish | Speed | field_76424_c | f_19596_ |
| Cooked Fish | Conduit Power | field_205136_C | f_19592_ |
| Cooked Rainbowfish | Luck | field_188425_z | f_19621_ |

## Minecraft 1.16.5

![Release-specific fish food portraits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/fish-food-overview-1.16.5.webp)

[Open the 1.16.5 meal planner](https://herbertofury.github.io/Advent-of-Ascension/fish-food-planner.html?v=1.16.5) · [Browse items](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5)

| Food | Hunger | Saturation modifier |
|---|---:|---:|
| [Blue Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ablue_gemtrap) | 2 | 0.2 |
| [Candlefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acandlefish) | 2 | 0.2 |
| [Charred Char](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acharred_char) | 2 | 0.2 |
| [Chocaw](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Achocaw) | 6 | 0.65 |
| [Crimson Skipper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acrimson_skipper) | 2 | 0.2 |
| [Crimson Stripefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acrimson_stripefish) | 2 | 0.2 |
| [Dark Hatchetfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Adark_hatchetfish) | 2 | 0.2 |
| [Green Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Agreen_gemtrap) | 2 | 0.2 |
| [Ironback](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aironback) | 2 | 0.2 |
| [Jamfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ajamfish) | 5 | 0.5 |
| [Parapiranha](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aparapiranha) | 2 | 0.2 |
| [Pearl Stripefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apearl_stripefish) | 2 | 0.2 |
| [Purple Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apurple_gemtrap) | 2 | 0.2 |
| [Razorfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arazorfish) | 2 | 0.2 |
| [Red Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ared_gemtrap) | 2 | 0.2 |
| [Reeftooth](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Areeftooth) | 2 | 0.2 |
| [Rocketfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arocketfish) | 2 | 0.2 |
| [Sailback](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asailback) | 2 | 0.2 |
| [Sapphire Strider](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asapphire_strider) | 2 | 0.2 |
| [White Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Awhite_gemtrap) | 2 | 0.2 |
| [Yellow Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ayellow_gemtrap) | 2 | 0.2 |
| [Turquoise Stripefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aturquoise_stripefish) | 2 | 0.2 |
| [Violet Skipper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aviolet_skipper) | 2 | 0.2 |
| [Raw Rainbowfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Araw_rainbowfish) | 3 | 0.85 |
| [Skelecanth](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askelecanth) | 1 | 0.1 |
| [Cooked Fish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acooked_fish) | 6 | 0.85 |
| [Cooked Rainbowfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acooked_rainbowfish) | 6 | 0.85 |

### Exact cooking routes

| Input | Output | Recipes |
|---|---|---|
| Blue Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_blue_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_blue_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_blue_gemtrap) |
| Candlefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_candlefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_candlefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_candlefish) |
| Charred Char | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_charred_char) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_charred_char) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_charred_char) |
| Crimson Skipper | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_crimson_skipper) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_crimson_skipper) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_crimson_skipper) |
| Crimson Stripefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_crimson_stripefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_crimson_stripefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_crimson_stripefish) |
| Dark Hatchetfish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_dark_hatchetfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_dark_hatchetfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_dark_hatchetfish) |
| Green Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_green_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_green_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_green_gemtrap) |
| Ironback | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_ironback) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_ironback) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_ironback) |
| Pearl Stripefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_pearl_stripefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_pearl_stripefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_pearl_stripefish) |
| Purple Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_purple_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_purple_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_purple_gemtrap) |
| Razorfish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_razorfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_razorfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_razorfish) |
| Red Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_red_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_red_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_red_gemtrap) |
| Reeftooth | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_reeftooth) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_reeftooth) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_reeftooth) |
| Rocketfish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_rocketfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_rocketfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_rocketfish) |
| Sailback | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_sailback) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_sailback) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_sailback) |
| Sapphire Strider | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_sapphire_strider) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_sapphire_strider) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_sapphire_strider) |
| Turquoise Stripefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_turquoise_stripefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_turquoise_stripefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_turquoise_stripefish) |
| Violet Skipper | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_violet_skipper) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_violet_skipper) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_violet_skipper) |
| White Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_white_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_white_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_white_gemtrap) |
| Yellow Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_fish_from_yellow_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_fish_from_yellow_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_fish_from_yellow_gemtrap) |
| Raw Rainbowfish | Cooked Rainbowfish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acampfire_cooked_rainbowfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Acooking_cooked_rainbowfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&recipe=aoa3%3Asmoking_cooked_rainbowfish) |

[Released registration, helper and recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/intermediate-fish-evidence-1.16.5.json). Source pin: [e97502da8bdd](https://github.com/Tslat/Advent-Of-Ascension/tree/e97502da8bdd6081b6acc4635f03296d3e2e69a0).

## Minecraft 1.20.1

![Release-specific fish food portraits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/fish-food-overview-1.20.1.webp)

[Open the 1.20.1 meal planner](https://herbertofury.github.io/Advent-of-Ascension/fish-food-planner.html?v=1.20.1) · [Browse items](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1)

| Food | Hunger | Saturation modifier |
|---|---:|---:|
| [Blue Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ablue_gemtrap) | 2 | 0.2 |
| [Candlefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acandlefish) | 2 | 0.2 |
| [Charred Char](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acharred_char) | 2 | 0.2 |
| [Chocaw](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Achocaw) | 6 | 0.65 |
| [Crimson Skipper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acrimson_skipper) | 2 | 0.2 |
| [Crimson Stripefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acrimson_stripefish) | 2 | 0.2 |
| [Dark Hatchetfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Adark_hatchetfish) | 2 | 0.2 |
| [Green Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Agreen_gemtrap) | 2 | 0.2 |
| [Ironback](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aironback) | 2 | 0.2 |
| [Jamfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ajamfish) | 5 | 0.5 |
| [Parapiranha](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aparapiranha) | 2 | 0.2 |
| [Pearl Stripefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apearl_stripefish) | 2 | 0.2 |
| [Purple Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apurple_gemtrap) | 2 | 0.2 |
| [Razorfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arazorfish) | 2 | 0.2 |
| [Red Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ared_gemtrap) | 2 | 0.2 |
| [Reeftooth](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Areeftooth) | 2 | 0.2 |
| [Rocketfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arocketfish) | 2 | 0.2 |
| [Sailback](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asailback) | 2 | 0.2 |
| [Sapphire Strider](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asapphire_strider) | 2 | 0.2 |
| [White Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Awhite_gemtrap) | 2 | 0.2 |
| [Yellow Gemtrap](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ayellow_gemtrap) | 2 | 0.2 |
| [Turquoise Stripefish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aturquoise_stripefish) | 2 | 0.2 |
| [Violet Skipper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aviolet_skipper) | 2 | 0.2 |
| [Raw Rainbowfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Araw_rainbowfish) | 3 | 0.85 |
| [Skelecanth](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askelecanth) | 1 | 0.1 |
| [Cooked Fish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acooked_fish) | 6 | 0.85 |
| [Cooked Rainbowfish](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acooked_rainbowfish) | 6 | 0.85 |

### Exact cooking routes

| Input | Output | Recipes |
|---|---|---|
| Blue Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_blue_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_blue_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_blue_gemtrap) |
| Candlefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_candlefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_candlefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_candlefish) |
| Charred Char | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_charred_char) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_charred_char) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_charred_char) |
| Crimson Skipper | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_crimson_skipper) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_crimson_skipper) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_crimson_skipper) |
| Crimson Stripefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_crimson_stripefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_crimson_stripefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_crimson_stripefish) |
| Dark Hatchetfish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_dark_hatchetfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_dark_hatchetfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_dark_hatchetfish) |
| Green Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_green_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_green_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_green_gemtrap) |
| Ironback | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_ironback) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_ironback) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_ironback) |
| Pearl Stripefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_pearl_stripefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_pearl_stripefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_pearl_stripefish) |
| Purple Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_purple_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_purple_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_purple_gemtrap) |
| Razorfish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_razorfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_razorfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_razorfish) |
| Red Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_red_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_red_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_red_gemtrap) |
| Reeftooth | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_reeftooth) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_reeftooth) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_reeftooth) |
| Rocketfish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_rocketfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_rocketfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_rocketfish) |
| Sailback | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_sailback) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_sailback) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_sailback) |
| Sapphire Strider | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_sapphire_strider) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_sapphire_strider) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_sapphire_strider) |
| Turquoise Stripefish | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_turquoise_stripefish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_turquoise_stripefish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_turquoise_stripefish) |
| Violet Skipper | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_violet_skipper) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_violet_skipper) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_violet_skipper) |
| White Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_white_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_white_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_white_gemtrap) |
| Yellow Gemtrap | Cooked Fish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_fish_from_yellow_gemtrap) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_fish_from_yellow_gemtrap) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_fish_from_yellow_gemtrap) |
| Raw Rainbowfish | Cooked Rainbowfish | [campfire cooking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acampfire_cooked_rainbowfish) · [smelting](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Acooking_cooked_rainbowfish) · [smoking](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Asmoking_cooked_rainbowfish) |

[Released registration, helper and recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/intermediate-fish-evidence-1.20.1.json). Source pin: [85d6beba07e3](https://github.com/Tslat/Advent-Of-Ascension/tree/85d6beba07e3a09032834dcf79b5a01f411092c3).

## Related guides

- [Historical species-specific fish healing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cooking-Fish-and-Hunger-Scaled-Healing-1.12.2)
- [Modern 1.21.1 fish food and cooking](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Fish-Food-Cooking-and-Healing-1.21.1)

Original AoA artwork and behavior by Tslat and contributors. All checks here read archive resources and class instructions without executing game or mod code.
