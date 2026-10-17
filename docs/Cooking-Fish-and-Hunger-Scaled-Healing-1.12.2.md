# Cooking fish and hunger-scaled healing · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** This guide checks all sixteen raw/cooked fish pairs registered in the inspected release: 32 food declarations, sixteen furnace conversions and the shared HealingFood callback.

[Open the interactive fish meal planner](https://herbertofury.github.io/Advent-of-Ascension/fish-food-planner.html). It calculates the source-rule request from your hunger and saturation; it does not inspect or change a running game.

## From catch to meal

1. Obtain a raw fish through the [historical fishing and Hauling system](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2). That guide separates the outer catch categories from the level-conditioned fish table.
2. Put one raw fish in a furnace and supply suitable fuel. The released registration requests one matching cooked fish and a smelting experience value of **3.0** for each of these sixteen conversions. This is the registered recipe value, not a claim about custom furnace automation, hook-modified XP or collection behavior.
3. Check your missing hunger before eating. Cooked fish use the extra healing callback; the raw BasicFood items do not.
4. Finish the normal food-use action. The cooked callback samples hunger **before** ordinary consumption, then requests scaled healing afterward. Actual restored health still depends on missing health and gameplay hooks.

These furnace conversions are registered in Java code. Absence from an archive’s crafting-recipe JSON list is not evidence that they are unavailable.

## Read the numbers correctly

- **Hunger points:** two points equal one full food-bar icon. Food restoration is capped at 20.
- **Saturation modifier:** a multiplier, not a direct number of saturation points. The inspected vanilla comparison adds 2 × the food’s hunger value × its modifier, capped by the new hunger level.
- **Healing points:** two points equal one heart. The maximum below requires enough missing hunger and enough missing health; it is not guaranteed every time you eat.
- **No instant revival:** the helper skips dead entities, entities at zero health, and entities already at maximum health.

### Worked example: Rainbowfish

Rainbowfish provides 9 hunger points with a 0.85 saturation modifier and a configured maximum extra healing of 10 health points (5 hearts).

| Hunger before eating | Missing hunger | Hunger restored | Extra healing request |
|---:|---:|---:|---:|
| 11 or less | 9 or more | 9 | 10 health points / 5 hearts |
| 15 | 5 | 5 | about 5.5556 health points / 2.7778 hearts |
| 19 | 1 | 1 | about 1.1111 health points / 0.5556 hearts |
| 20 | 0 | 0 | 0; explanatory boundary, normal use can be refused |

The callback uses **maximum healing × min((20 − hunger before eating) ÷ food hunger, 1)**. Its float arithmetic is reproduced in the planner and the 336 bounded cases. It does not use the number of hunger points missing after the meal.

At hunger 19 with zero saturation, the vanilla comparison requests about 15.3 saturation from Rainbowfish even though only one hunger point fits. Saturation uses the full configured food value and is then capped; the special healing calculation instead scales by the missing-hunger fraction. These are deliberately separate calculations.

## Sixteen illustrated cooking pairs

The pictures are source-atlas crops composed into original recipe diagrams. They are not screenshots or a simulation of furnace timing. Table modifiers are rounded for readability; exact float values are in the evidence.

| Raw → cooked picture | Hunger raw → cooked | Saturation modifier raw → cooked | Maximum cooked healing |
|---|---:|---:|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-candlefish.webp" width="380" height="190" alt="Raw Candlefish to Candlefish"><br>Candlefish | 1 → 6 | 0.2 → 0.7 | 7 health points / 3.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-crimson_skipper.webp" width="380" height="190" alt="Raw Crimson Skipper to Crimson Skipper"><br>Crimson Skipper | 1 → 5 | 0.15 → 0.6 | 6 health points / 3 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-crimson_stripefish.webp" width="380" height="190" alt="Raw Crimson Stripefish to Crimson Stripefish"><br>Crimson Stripefish | 1 → 4 | 0.1 → 0.5 | 5 health points / 2.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-dark_hatchetfish.webp" width="380" height="190" alt="Raw Dark Hatchetfish to Dark Hatchetfish"><br>Dark Hatchetfish | 2 → 7 | 0.2 → 0.75 | 8 health points / 4 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-fingerfish.webp" width="380" height="190" alt="Raw Fingerfish to Fingerfish"><br>Fingerfish | 1 → 1 | 0 → 0.2 | 1 health points / 0.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-golden_gullfish.webp" width="380" height="190" alt="Raw Golden Gullfish to Golden Gullfish"><br>Golden Gullfish | 2 → 2 | 0.1 → 0.4 | 3 health points / 1.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-ironback.webp" width="380" height="190" alt="Raw Ironback to Ironback"><br>Ironback | 3 → 8 | 0.3 → 0.8 | 9 health points / 4.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-limefish.webp" width="380" height="190" alt="Raw Limefish to Limefish"><br>Limefish | 1 → 1 | 0.15 → 0.35 | 2 health points / 1 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-pearl_stripefish.webp" width="380" height="190" alt="Raw Pearl Stripefish to Pearl Stripefish"><br>Pearl Stripefish | 1 → 1 | 0.05 → 0.35 | 1 health points / 0.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-rainbowfish.webp" width="380" height="190" alt="Raw Rainbowfish to Rainbowfish"><br>Rainbowfish | 3 → 9 | 0.85 → 0.85 | 10 health points / 5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-razorfish.webp" width="380" height="190" alt="Raw Razorfish to Razorfish"><br>Razorfish | 3 → 9 | 0.3 → 0.85 | 10 health points / 5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-rocketfish.webp" width="380" height="190" alt="Raw Rocketfish to Rocketfish"><br>Rocketfish | 1 → 4 | 0.15 → 0.5 | 5 health points / 2.5 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-sailback.webp" width="380" height="190" alt="Raw Sailback to Sailback"><br>Sailback | 1 → 2 | 0.1 → 0.4 | 2 health points / 1 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-sapphire_strider.webp" width="380" height="190" alt="Raw Sapphire Strider to Sapphire Strider"><br>Sapphire Strider | 2 → 6 | 0.2 → 0.65 | 6 health points / 3 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-turquoise_stripefish.webp" width="380" height="190" alt="Raw Turquoise Stripefish to Turquoise Stripefish"><br>Turquoise Stripefish | 1 → 2 | 0.15 → 0.4 | 4 health points / 2 hearts |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/healing-fish-1.12.2-violet_skipper.webp" width="380" height="190" alt="Raw Violet Skipper to Violet Skipper"><br>Violet Skipper | 1 → 3 | 0.2 → 0.5 | 4 health points / 2 hearts |

## Choose according to the missing hunger

Rainbowfish and Razorfish share the largest configured healing ceiling in this sixteen-fish set, 10 health points, and both restore 9 hunger points. That does not make them the universal best use of a rare catch. When only one hunger point is missing, Turquoise Stripefish requests 4 × 1/2 = **2 health points**, while Rainbowfish requests 10 × 1/9 ≈ **1.1111**. Limefish also requests 2 health points with its one-point food value. Acquisition, stack supply, health cap and other food effects all matter.

This comparison covers these fish only. It does not rank every AoA food, certify potion interactions, or recommend using food at full hunger.

## Restoration and testing boundaries

- Verify actual food-use eligibility and hooks in the target Forge build; the inspected vanilla ItemFood methods are comparison evidence, not the complete patched runtime.
- The AoA HealingFood override and healing helper have no explicit local server-side guard. Check authoritative health updates and client prediction rather than concluding that healing is applied twice.
- Keep pre-meal hunger sampling when preserving historical behavior. Replacing it with post-meal hunger would change the intended fraction.
- Preserve exact raw/cooked identities, sixteen Java-registered smelts and the difference between saturation modifier and saturation amount.
- Test nearly-full hunger, low health, full health, zero health, altered maximum health and modded food/healing hooks before claiming runtime parity.

## Sources and related guides

- [Released food, furnace and healing evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/healing-fish-evidence-1.12.2.json).
- [Sixteen paired illustration receipts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/healing-fish-art-evidence-1.12.2.json).
- [Meal calculator](https://herbertofury.github.io/Advent-of-Ascension/fish-food-planner.html), [fishing and Hauling](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2), [crop harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2).
- Original item art and mechanics by Tslat and AoA contributors; vanilla comparison by Mojang. No game or mod code was executed.

## Compare modern fish food behavior

[Modern fish food, cooking and healing · 1.21.1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Fish-Food-Cooking-and-Healing-1.21.1) documents 27 foods and 63 cooking recipes. Generic Cooked Fish and Cooked Rainbowfish have distinct effect and healing behavior; historical per-fish healing values must not be carried across releases.
