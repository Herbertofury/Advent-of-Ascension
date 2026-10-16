# Farming, soils and harvesting · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** A practical planting guide based on released resources, selected class checks and pinned source. It covers how the inspected crops behave once you have their planting items. It does not claim that every seed has a complete survival acquisition route in every pack.

![Ashfern on basalt, Magic Marang below haunted leaves, and Green Manure on farmland](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/farming-soil-reference-1.21.1.webp)

[All growth-stage pictures](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crops-and-Growth-Stages) · [Multi-block plant states](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Multi-State-Block-References) · [Tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.21.1)

## Build three small test beds first

1. **Ordinary crops:** prepare farmland, lighting and access paths. Keep spare planting items before harvesting your last plant.
2. **Ashfern:** use **Basalt**, not farmland. Keep the crop brightly lit.
3. **Magic Marang:** make room **under Haunted Leaves or Haunted Eyes Leaves**, rather than planting it on the ground.

Test one plant and a full harvest/replant cycle before scaling up an automated farm. Tool actions, fake players, right-click harvest mods and custom loot can take different paths from the player-breaking behavior documented here.

## Planting-item reference

The inspected registration maps 17 crop blocks to these planting items. Thirteen use the ordinary AoA crop class; the four special cases are explained below.

| Crop | Planting item | Family |
|---|---|---|
| Ashfern | Ashfern Seeds | Basalt-supported |
| Bubble Berries | Bubble Berry Seeds | Ordinary farmland |
| Chilli | Chilli Seeds | Ordinary farmland |
| Eye Bulbs | Eye Bulb itself | Ordinary farmland |
| Floracles | Floracle Seeds | Ordinary farmland |
| Goldicaps | Goldicap Seeds | Ordinary farmland |
| Heart Fruit | Heart Fruit Seeds | Ordinary farmland |
| Lunacrike | Lunacrike Seeds | Ordinary farmland |
| Luna Globes | Luna Globe Seeds | Ordinary farmland |
| Lunalons | Lunalon Seeds | Ordinary farmland |
| Magic Marangs | Magic Marang itself | Hanging crop |
| Mystic Shrooms | Mystic Shrooms themselves | Ordinary farmland |
| Rosidons | Rosidon Seeds | Ordinary farmland |
| Tea | Tea Seeds | Ordinary farmland |
| Trilliads | Trilliad Seeds | Ordinary farmland |
| Green Manure | Green Manure Seeds | Soil-improvement crop |
| Thorny Plant | Thorny Plant Seeds | Three-block special plant |

Eye Bulbs and Mystic Shrooms do not have to be replaced with a fictional separate seed item. Keep some of the actual planting item for the next cycle. Find the item in the [Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html) with the correct release selected; use its recipe/drop links where available rather than assuming a creative-inventory entry proves obtainability.

## Ordinary crops: recognize maturity before harvesting

The ordinary crop class inherits vanilla's **maximum age 7**. Its eight visual ages are useful progress markers, but a screenshot alone does not prove a crop's loot conditions. The released tables check maturity explicitly.

For example, Bubble Berries have an age-7 produce branch and a separate mature seed pool. Breaking an immature plant follows the seed branch instead. Fortune, explosion decay and other modifiers are separate from maturity; do not assume a fixed number of drops from the appearance alone.

Use the [growth gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crops-and-Growth-Stages) to compare ages and the [loot reference](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html) to inspect the actual block table. Keep light and adequate growing space. This page does not promise a fixed number of real-time minutes, especially on servers with changed random ticks or growth hooks.

## Ashfern: basalt and light

Ashfern overrides the usual soil rule with an exact **Basalt block** check. A block that merely looks like basalt, including a different basalt variant, is not automatically accepted.

Its ordinary survival check requires enough brightness or sky visibility; the world-generation path has a separate lighting workaround. Do not interpret that generation exception as permission to grow it in a dark player-built room. Use good lighting rather than relying on the plant's mature glow to grow the next immature crop.

![Ashfern age-model reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-growth-ashfern_crop.webp)

## Magic Marang: placement is stricter than survival

The crop block's support check recognizes leaves above it, but the **planting item's released placement method explicitly permits Haunted Leaves or Haunted Eyes Leaves** before delegating to normal placement validation. Ordinary oak leaves therefore should not be recommended as an equivalent planting surface.

Leave the crop position below the leaves free. Its random-growth path checks brightness of at least 9 and loaded nearby terrain. Its growth calculation also considers neighboring supports and same-crop crowding, so a completely packed canopy should not be advertised as automatically fastest.

The released loot table produces Magic Marang at **age 7**. The crop's non-creative **player-destroy** override replants a mature crop at **age 0** after the normal destruction/drop path. This is a break-to-harvest behavior, not a verified right-click harvest feature. Breaking it early does not use that mature replant branch. Automation must be tested separately.

![Magic Marang age-model reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-growth-magic_marang_crop.webp)

## Green Manure: turn a harvest into better soil

Plant Green Manure on farmland and let it reach **age 7**. Its mature destruction method turns the supporting farmland into **Fertilised Farmland with `well_fertilised=true`**, preserving the previous moisture value. Breaking it before maturity does not meet that conversion condition.

The mature seed drop uses its own Fortune-aware table. Green Manure is specifically excluded from the fertilised-soil yield modifier, so do not assume repeatedly harvesting it earns the ordinary crop bonus too.

![Green Manure age-model reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-growth-green_manure.webp)

### What the fertilised-soil bonus actually does

For a qualifying mature crop with nonempty generated loot directly above supported Fertilised Farmland:

| Soil before the qualifying harvest | Added amount | Soil afterward |
|---|---|---|
| Well-fertilised | **+2 to each non-planting-item loot stack** | Ordinary Fertilised Farmland |
| Ordinary Fertilised Farmland | **+1 to each non-planting-item loot stack** | Vanilla farmland |

Moisture is preserved during these transitions. These are extra stack counts, not a percentage multiplier or a claim that the crop grows twice as fast.

The modifier skips items matching the crop's clone/planting item. That matters for crops where produce and planting item are the same, such as Eye Bulbs or Mystic Shrooms. **The soil transition is outside that per-stack skip**, so a qualifying harvest can spend fertilisation even when every generated stack is skipped. Do not assume every crop benefits equally.

Fertilised Farmland also overrides trampling behavior, but still applies ordinary fall damage to the landing entity. “Protected soil” does not mean “safe to jump from any height.”

## Thorny Plant: allow three blocks of height

Thorny Plant uses a special multi-block class with **three parts**, **five stages per part**, and a global age range **0–14**. Its visuals need both the age and height properties; use the [multi-state gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Multi-State-Block-References), not a single age-only picture.

- Leave enough room for the upper parts.
- Its checked bonemeal age increase is **one**, not a promise of instant maturity.
- Keep its farmland at **Y=0 or above** for this stock implementation. The released survival scan stops before reading positions below Y=0; a deep negative-height farm is a specific test target for a changed build.
- Its final growth path spawns Thorny Plant Sprouts. Give it a separated area rather than treating it as an ordinary quiet food crop.

No ordinary `blocks/thorny_plant_crop` loot JSON was found in this release's inspected resources. That absence is not a proof that no code or external modifier can yield anything, but this guide will not invent a normal fruit-and-seed harvest for it.

## Living Growth is not an ordinary crop

Living Growth appears in the age-model gallery because it has staged visuals. It is a separate block class using scheduled growth behavior, not one of the 17 crop registrations above. The inspected source's terminal Vinocorne-spawning branch is commented out. A complete-looking stage sheet does not prove that a boss-summoning loop is enabled.

Keep ordinary farming, special growth blocks and restoration acceptance separate. Do not spend rare items on a supposed boss-summoning recipe solely because its model appears in the atlas.

## Quick troubleshooting

| Symptom | First check |
|---|---|
| Ashfern will not stay planted | Exact Basalt support and adequate light |
| Marang will not place | Use Haunted Leaves or Haunted Eyes Leaves, with room beneath |
| Marang disappears when harvested | Was it age 7, and was this an ordinary non-creative player break? |
| Green Manure did not improve soil | Mature age 7 and supporting farmland |
| Fertiliser seems used without extra produce | Does the dropped item match the planting item and get skipped? |
| Thorny Plant fails deep underground | Supporting farmland below Y=0 is outside the checked survival scan |
| A farm grows slowly | Lighting, loaded area, crowding, hooks and server tick settings; no universal speed guarantee |
| A stage gallery suggests an unavailable mechanic | Inspect registration and code behavior, not just model presence |

## Evidence and testing boundary

[Crop, loot and method evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/farming-evidence-1.21.1.json) joins the 17 source registrations to 16 released crop loot resources and records selected class hashes/method bodies, the registered fertilised-soil modifier, exact Marang placement branch, vanilla age-7 method and multi-block floor guard. Source interpretation is pinned to [7919b5fe48599e6105c5740937ce36c36ef21d16](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16).

Only the stated narrow assertions were mechanically checked. Source interpretation and documentation models are not a live-game farming benchmark, full modpack compatibility proof or certification of the private Enderloom build. AoA models/textures are credited to Tslat and contributors; vanilla references to Mojang/Microsoft.

## Dryad Sprite encounters

The [illustrated Dryad Sprite walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dryad-Sprite-Farming-Encounter-1.21.1) covers the Farming-44 spawn ability, all six exact hoe matches, ownership, short unresolved-sprite lifetime and conditional reward pools. Prepare the correct tools before harvesting: a wrong hoe discards the sprite, and ordinary-looking crop harvest actions do not all necessarily use the required block-break event.
