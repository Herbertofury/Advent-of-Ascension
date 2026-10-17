[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Skills](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Worlds](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Historical fishing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2)

# Runation: Rune Shrines, input runes and safe conversion

> **Historical release: Minecraft 1.12.2 / AoA 3.3.6.** The values below come from the selected released classes and recipe resources. They do not describe the later Rune Post/Randomizer system or certify an Enderloom restoration.

## Read this before spending a stack

**Check the northeast post first.** If the first checked position does not contain a Rune Post, using an accepted input rune on the shrine enters a practice branch. Outside Creative, that branch consumes the entire held stack, gives no output runes, and requests only two Runation XP per input rune. A later missing or mismatched post follows a different branch and does not perform normal conversion.

A water bucket used directly on a Rune Post has another special action: it removes the post and gives a Pure Water Stone. Do not use it casually while preparing a working shrine.

## From ore to usable input runes

![Ordinary and charged Runium ore-to-chunk-to-rune recipe flows](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/runation-input-rune-recipes-1.12.2.webp)

1. Obtain Runium Ore or Charged Runium Ore. The selected released Overworld generator places ordinary Runium attempts at Y = 5 + nextInt(128), or 5–132, subject to its configuration and terrain replacement. This is an attempt range, not guaranteed ore at every height.
2. Smelt the ore into its matching chunk. The inspected code-side registration supplies one chunk and a 2.0 furnace-experience parameter. Furnace XP is distinct from Runation skill XP.
3. Shapeless-craft one Runium Chunk into **16 Unpowered Runes**, or one Charged Runium Chunk into **16 Charged Runes**.
4. Split the input stack if you only want to spend a few. Shrine conversion works on the whole held stack.

[Exact Unpowered Rune recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fmisc%2Funpowered_rune) · [Exact Charged Rune recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fmisc%2Fcharged_rune)

Charged Runium is referenced by the selected Deeplands decorator: attempts use Deeplands Stone as the replacement target and an offset of 70–114 on Y relative to the supplied base position. Configuration controls the count and vein-size arguments. This scoped method inspection is not a complete worldgen-distribution guarantee.

The two input-rune recipes exist as JSON. No ordinary Rune Shrine crafting recipe was found in the selected recipe-resource scan; code-side or pack additions must be checked separately. Do not turn the coordinate diagram into a promise that survival players can craft and move every post.

## Find and inspect the shrine

The selected Overworld generation method has a configured Wind Rune Shrine chance. It requires sampled surface height at least 95 and an air check near the proposed structure, then attempts generation 30 blocks above that surface, with the base Y capped at 240. This is why searching ordinary low terrain is a poor match for that particular generator path. The air check uses the unclamped offset while the placement argument is capped; verify high-world boundaries in game.

Other shrine types have the structure declaration contexts listed in the tier table below. A named structure class and its realm folder are useful references, but are not by themselves a complete natural-generation or safe-travel proof.

### Exact post positions

![Four identical Rune Posts at exact offsets above a Rune Shrine](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/runation-shrine-layout-1.12.2.webp)

Take the shrine block as (0, 0, 0), with east = +X and south = +Z. The code checks four positions at **Y +2**:

| Check | Offset from shrine |
|---|---|
| First, northeast | (+3, +2, −3) |
| Northwest | (−3, +2, −3) |
| Southeast | (+3, +2, +3) |
| Southwest | (−3, +2, +3) |

All four must be the **same Rune Post block identity**. Similar color is not enough, and a mixed set does not combine rune types. The diagram projects X/Z positions from above: it does not place the posts at the shrine’s floor height.

## Choose the tier and correct input

![Fourteen released Rune Post tiers and their output rune items](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/runation-rune-tier-catalog-1.12.2.webp)

| Output rune | Declared Runation level | Base XP per input | Input required | Structure declaration context |
|---|---:|---:|---|---|
| [Wind Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WindRune.name) | 0 | 4 | Unpowered Rune sufficient | Overworld |
| [Fire Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FireRune.name) | 8 | 7 | Unpowered Rune sufficient | Nether |
| [Water Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WaterRune.name) | 15 | 10 | Unpowered Rune sufficient | L’Borean |
| [Poison Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonRune.name) | 22 | 14 | Unpowered Rune sufficient | Vox Ponds |
| [Wither Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherRune.name) | 30 | 15 | Unpowered Rune sufficient | Abyss |
| [Lunar Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarRune.name) | 32 | 20 | Charged Rune | Lunalus |
| [Energy Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EnergyRune.name) | 36 | 22 | Unpowered Rune sufficient | Iromine |
| [Strike Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.StrikeRune.name) | 42 | 24 | Unpowered Rune sufficient | Haven |
| [Storm Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.StormRune.name) | 49 | 30 | Charged Rune | Greckon |
| [Kinetic Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KineticRune.name) | 54 | 32 | Charged Rune | Gardencia |
| [Power Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PowerRune.name) | 59 | 40 | Unpowered Rune sufficient | Barathos |
| [Compass Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CompassRune.name) | 63 | 45 | Charged Rune | Celeve |
| [Distortion Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DistortionRune.name) | 65 | 50 | Charged Rune | Mysterium |
| [Life Rune](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LifeRune.name) | 72 | 56 | Charged Rune | Precasia |

Wind’s stored requirement is **0**, so a normal starting skill level satisfies it. Six outputs require Charged Runes: Lunar, Storm, Kinetic, Compass, Distortion and Life. The other eight accept Unpowered Runes; the selected handler also accepts Charged Runes for those outputs, so using a more costly input does not automatically buy a better result.

Use the **central shrine**, not the post, while holding one of the two accepted input-rune items. Other held items return without rune conversion in the selected handler. The level gate uses the first post’s Runation requirement. Creative does not have an explicit bypass around that gate in this method.

## Output count, XP and armor

For a valid matching four-post structure and eligible held stack of N input runes:

- Ordinary output is N matching runes.
- A recognized full Runation armor set changes the output to 2 × N.
- The base Runation XP request remains `post XP × input count`; it is calculated from the held input count, not the doubled output count.
- The armor separately declares a 0.3 Runation XP modifier in its full-set callback and a level-100 equipment requirement. Final XP can change through those modifiers and configuration.
- Outside Creative, the hand receives at most 64 output runes; any remainder goes through the item-give-or-drop helper. The original held input is replaced.
- Creative retains its input and sends the output through the give helper in batches of at most 64.

Example: 64 Unpowered Runes at a valid Wind shrine request 256 base Runation XP. With the recognized full set, the output becomes 128 Wind Runes: 64 in the hand and 64 through the helper. The base XP calculation is still 64 × 4 before separate XP modifiers. The 128 arithmetic checks in the evidence cover input counts 1–64 with and without the set; they are not inventory or multiplayer game tests.

## Distinguish the failure branches

| Situation | Selected handler behavior |
|---|---|
| Wrong held item | Returns without rune conversion |
| First northeast position is not a Rune Post | Practice: whole held stack removed outside Creative, no output runes, 2 × input count base XP request |
| First post exists but level is too low | Insufficient-level feedback for a server player; no normal conversion |
| Charged-output tier with Unpowered Runes | Returns false before checking the remaining posts; no normal conversion |
| First post valid but a later post differs or is missing | No matching-structure conversion; does not enter the first-post-missing practice branch |
| Four identical eligible posts | Converts the entire accepted held stack |

“Practice” is not a harmless preview. Check with a small stack after confirming the layout, and reserve valuable Charged Runes for the tiers that need them.

### The water-bucket action

Using a Water Bucket on a Rune Post is handled by the post class itself. On the server it shrinks the held bucket stack by one outside Creative, gives a Pure Water Stone through the helper, and sets the post block to air. The selected method contains no replacement-empty-bucket grant. This is a deliberate interaction path to test, not a claim that a live bug was reproduced here. Removing the first northeast post can also change what a subsequent shrine use does.

## Troubleshooting

- If all posts appear present, measure the exact ±3 horizontal and +2 vertical offsets from the shrine block.
- If a high-tier shrine rejects you, check its stored level and whether its output requires Charged Runes.
- If XP arrives but the held runes vanish with no output, inspect the first northeast position for the practice branch.
- If armor seems to double items but not the displayed XP amount, distinguish base input-count XP from the separate armor/configuration modifier path.
- If output drops on the ground, test inventory capacity and the give-or-drop helper rather than assuming an item duplication or loss.
- If a shrine cannot be found, distinguish generator requirements, configuration and already-generated terrain from mere structure declarations.

## Restoration acceptance checklist

- [ ] Test all fourteen tiers at their threshold and just below it, with both input-rune types.
- [ ] Test each of the four missing-post positions separately; the first one intentionally reaches a different branch.
- [ ] Test mixed post identities, wrong Y offsets, wrong held items and both hands.
- [ ] Compare counts 1, 32, 33 and 64 with/without the recognized full armor set, including full inventory and Creative.
- [ ] Verify base XP, configuration modifiers, armor modifiers and disabled-skill behavior independently.
- [ ] Test the Water Bucket action in a disposable world, including bucket consumption, stone receipt, post removal and the next shrine use.
- [ ] Trace and test actual generation for every declared structure context, high-altitude Wind placement and custom terrain compatibility.
- [ ] Profile repeated interaction and world generation without changing accepted output or progression semantics.

## Sources and limits

[Released method/binding/recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/runation-shrine-evidence-1.12.2.json) · [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/runation-shrine-art-evidence-1.12.2.json)

31 selected released methods, fourteen post bindings, sixteen rune bindings, fourteen structure declarations, two recipe JSON files and 128 independent stack-split checks support this guide. Source-model crops identify the actual blocks/items; the layout diagram is not a complete structure render. No Java or Minecraft game code was executed.

[Official pinned source](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source) supplies readable context. Released artifact bytes determine the selected behavior. AoA assets and designs: Tslat and contributors. Original documentation and diagrams.

[Later 1.16.5 Rune Post and Randomizer handbook](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rune-Production-and-Randomizer-1.16.5) · [Skill guides](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
