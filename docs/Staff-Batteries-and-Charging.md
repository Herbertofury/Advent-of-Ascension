# Staff batteries and charging: why the recipe has no fixed output

[Recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=arcanum_battery) · [Exact staff rune costs and materials planner](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Rune-Costs-and-Preparation-1.21.1) · [Beginner guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Beginner-Walkthrough)

**Scope:** the pinned 1.21 implementation, with recipe declarations, staff tag and item pictures checked in the released Minecraft 1.21.1 / AoA 3.7.16.1 archive. This is source-guided instruction, not a new live-game test. Older releases may use different components and rules.

![Battery attachment with source item pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/staff-battery-walkthrough.webp)

## What you are making

Battery attachment produces a modified copy of the staff you supplied. It is not one fixed staff item. The small recipe JSON only declares the custom recipe type, so a static JSON-only recipe browser cannot truthfully supply one universal output.

The released `aoa3:staves` tag includes Fire Staff, used in the illustration. Eligibility still depends on the input staff's stored-cast state and the current tag definitions.

## 1. Attach the battery

1. Obtain an Arcanum Battery and a staff eligible for attachment. Check the release's recipe search for the battery's acquisition recipe rather than assuming the attachment recipe creates a battery.
2. Place the staff and battery in separate crafting-input slots. The operation is shapeless; the illustration is not a mandatory left-to-right pattern.
3. Leave unrelated ingredients out. The implementation requires exactly the two occupied ingredient entries.
4. Inspect the output. The implementation copies the staff and gives it a stored-spell-casts component initialized to **0**. Attaching a battery does not preload casts.
5. Take the result only when it is the staff you intended to modify. Keep a backup of valuable worlds before testing unfamiliar mod combinations.

A staff whose existing stored-cast value is nonnegative is rejected by this attachment implementation. Do not repeatedly add batteries expecting automatic capacity stacking.

## 2. Charge the prepared staff

1. Check that the staff has both stored-casts data and staff-stat data.
2. Read that staff's rune requirements. Different staves can require different rune types and quantities.
3. Put the staff and the required rune items into the crafting input. Supply at least the configured cost of each required rune type.
4. Remove unrelated rune types or other ingredients. The implementation compares the set of supplied item types with the staff's rune-cost set.
5. Inspect the output's charge count, then take it. The assembly method increments stored casts once per completed operation; it does not convert an entire stack into that many casts in one step.
6. Repeat as needed while observing the displayed result and remaining ingredients. A staff already at its defined maximum is rejected.

The remaining-items method is designed to return excess runes after paying one cast's cost. Crafting-grid and modpack behaviour still need live validation; do not promise a bulk-shift-click result that has not been tested.

## Why nothing appears in the output slot

| Symptom | Check |
|---|---|
| Battery attachment fails | Is the item in the current staves tag? Does it already have a nonnegative stored-cast value? Are there exactly two ingredient entries? |
| Charging fails immediately | Does the staff carry both required data components? Is stored-cast count negative or already at its maximum? |
| You supplied plenty of runes but it still fails | Are all required rune types present, and are there any extra types that do not belong? The recipe checks types as well as counts. |
| The web recipe card has no fixed output | This is a dynamic custom recipe. The staff's copied data determines the output. |
| A different mod's staff is rejected | A similar name or texture is insufficient. Tag membership and the relevant components are required. |

## A second dynamic example: Ashfern cooking

The inspected Ashfern recipe accepts two occupied input entries: one Ashfern and one food item with a nonempty smelting recipe result. It looks up the smelting output rather than hardcoding one dish. A food-looking ingredient without food properties, an already-cooked item without a smelting result, or an unrelated extra ingredient can fail the match.

Use the currently installed recipe viewer to confirm the exact input/output pair. This guide does not invent a universal Ashfern cooking output or a furnace recipe for the custom crafting operation.

## Evidence

- [Battery attachment implementation](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/recipe/ArcanumBatteryAttachRecipe.java)
- [Staff charging and remainder handling](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/recipe/StaffChargingRecipe.java)
- [Battery recipe-viewer integration](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/integration/jei/recipe/arcanumbatteryattach/ArcanumBatteryAttachRecipeExtension.java)
- [Ashfern matching and assembly](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/recipe/AshfernCookingRecipe.java)

Release resources inspected: `data/aoa3/recipe/arcanum_battery_attaching.json`, `data/aoa3/recipe/staff_charging.json`, `data/aoa3/tags/item/staves.json`. Source links are pinned rather than silently following a changing branch.
