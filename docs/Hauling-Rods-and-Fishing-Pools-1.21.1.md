# Hauling rods and fishing pools · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** AoA hauling rods use their own bobber states and biome/fluid catch pools. Cast into the right fluid, wait for a catch, then use the rod to reel it close enough to land. Repeatedly canceling an unhooked cast does not complete a catch.

![Four hauling rod item previews with durability, fluid roles and default skill requirements](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-rods-overview-1.21.1.webp)

[Hauling skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) · [Passive Fishing Cage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Cage-Walkthrough-1.21.1) · [Reward boxes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.21.1)

## Choose equipment and check the skill gate

| Tool | Stock durability | Fluid | Shipped Hauling equip requirement | Main distinction |
|---|---:|---|---|---|
| Hauling Rod | 400 | Water | 15 | Basic AoA hauling bobber |
| Thermally Insulated Rod | 400 | Lava | 54 | Lava bobber and fire-protected landed catch-item entities |
| Light Rod | 160 | Water | 69 | Twice the base pulling-strength method's result |
| Golden Rod | 280 | Water | No entry for this item in the inspected Hauling skill file | Adds 3 to the rod's luck modifier; doubles returned loot-stack quantities through the checked helper; longer validity range |
| Fishing Cage | 15 | Water | 31 | Separate grounded-water trap with three catch slots |

These are the inspected default skill-file records, not a promise that another pack retains them. **An equip requirement is not a recipe and does not grant the item.** In particular, reaching Hauling 69 does not automatically award a Light Rod.

The Golden Rod's special bobber accepts an owner distance up to 64 blocks in the inspected validity check; the ordinary hauling bobber uses 32. Those values are **validity limits**, not a guarantee that every cast travels that far or that every modded terrain layout supports it.

## Craft the basic rod, then the lava upgrade

![Shapeless Hauling Rod recipe and Thermally Insulated Rod upgrade ingredients](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/hauling-rod-recipes-1.21.1.webp)

### Hauling Rod

Combine, shapelessly:

- 1 vanilla Fishing Rod
- 1 Charcoal, not an automatic Coal substitute
- 1 Limonite Nugget
- 1 item matching `c:ingots/iron`

Output: **1 Hauling Rod**. Four ingredients fit the player's 2×2 crafting grid.

### Thermally Insulated Rod

Combine, shapelessly:

- 1 Hauling Rod
- **4 Magma Creams in separate ingredient slots**
- **2 Netherite Scraps in separate ingredient slots**

Output: **1 Thermally Insulated Rod**. Seven ingredient entries require the larger crafting grid. The recipe consumes the input rod. These are ordinary preset-output recipes; do not assume the result preserves an input rod's enchantments, name or custom components. Use an expendable plain rod when preparing the upgrade unless your exact pack documents a preservation change.

### Advanced rod acquisition

The released Shiny Squid loot table includes the Golden Rod in its `extra` pool: one base roll, Golden Rod weight 1 among total weight 157. That is a conditional **1/157 share of the unmodified extra pool**, not a guaranteed kill reward or a chance of finding a Shiny Squid. See the [modern bestiary](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Bestiary-Portraits) and [Loot Reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Loot-Tables-and-Global-Modifiers-1.21.1).

The inspected JSON reference scan found the Light Rod's skill restriction and item/enchantment tags, but no acquisition recipe or loot entry. This does not prove no code-based route exists. **Light Rod acquisition remains unresolved here; no invented crafting recipe is provided.**

## Cast, wait, hook and land

1. Hold the correct rod and cast into water, or lava with the thermal rod. Ordinary water bobbers are discarded in lava.
2. Keep the rod available in hand and stay within its owner-distance limit. The validity path checks that the owner is alive and still holding the same item type.
3. Let the bobber enter its fluid state. A bobber stuck against terrain is a separate state and does not provide the same fishing loop.
4. Wait for a catch to approach and become hooked. AoA can spawn a creature or item from its hauling pool; the initial timer is not the entire landing process.
5. Use the rod to reel the hooked catch toward you. The inspected landing branch requires bobber-to-player squared distance **at most 9**, equivalent to three blocks.
6. Collect the resulting items safely. The normal rod throws catch items toward the player rather than guaranteeing direct inventory insertion.

Using the rod while no catch is hooked can discard the existing bobber. Stay reasonably still once a fish is hooked: the source starts a 1,200-tick hook timer and subtracts additional time when it detects player movement. This is not a promise of a full minute in every situation. Existing-entity hooking uses a different state and event path; hooking an arbitrary nearby entity is not equivalent to a completed generated fish catch.

Thermal landed catch-item entities explicitly resist fire-tagged damage in their source override. This does not grant the player fire resistance or certify every modded hazard. Fish from a safe platform; keep a clear retrieval route.

## Improve the fishing spot

The timer calculation starts from source bounds of 40 and 700 ticks, then changes them using the spot's modifier. When the modifier is below 0.9, both bounds are stretched with separate divisors; otherwise the maximum is divided by the modifier. Therefore **“2–35 seconds per catch” is not a reliable universal claim**.

### Water rods

- The bobber counts nearby matching **source-fluid blocks**, using its bounding box inflated by `(3, 2, 3)`. It does not simply count the visible surface area of the entire lake.
- At 50 or fewer matching blocks the modifier is halved; below 15 it is halved again. A tiny pool can be substantially worse.
- Ocean, river and swamp tags feed the beneficial-biome tag; dead, dry and hot tags feed the detrimental one. Actual tag contents and multiple matching modifiers matter.
- Temperature, precipitation and actual rain at the bobber also affect the calculation.
- Nearby players inside the bobber's bounding box inflated by five reduce the modifier by 10% each, capped at five counted players. The query is a box, not an exact five-block spherical radius.
- The source adds a lure-dependent contribution, but it does not remove all other spot penalties.

### Lava rod

The thermal bobber has its own calculation: a smaller source-fluid query inflated by `(2, 1, 2)`, temperature and precipitation factors, a 50/15 source-block penalty, and lava-specific biome tags. Dead/dry/hot tags are beneficial; ocean/river/swamp tags are detrimental.

**Any player found in its five-inflated-box query multiplies the thermal modifier by 0.2.** The source does not explicitly exclude the owner. Avoid standing immediately beside the bobber while waiting, without moving so far that you invalidate it or put yourself at risk. This is source-derived placement advice, not a measured catch-rate benchmark.

## Understand biome pools and skill eligibility

Six released definitions were inspected, totaling **66 entry records**:

| Definition | Fluid | Role | Entry count |
|---|---|---|---:|
| `water_default` | Water | Normal fallback | 19 |
| `precasia_water` | Water | Listed Precasian biomes | 16 |
| `barathos_water` | Water | Listed Barathos biomes | 9 |
| `lava_default` | Lava | Normal fallback | 10 |
| `water_traps_default` | Water | Declared trap fallback | 6 |
| `lava_traps_default` | Lava | Declared trap fallback | 6 |

Normal selection first checks the fluid's biome-specific map, then its default. An entry's `hauling_level_req`, weight and luck modifier affect selection. An entry may be a spawned entity or an item stack; it is not necessarily the final item dropped when that creature is landed. A historical dimension's pool file does not prove the full dimension is playable in this release.

The [complete evidence file](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hauling-rods-evidence-1.21.1.json) preserves all 66 records, exact biome lists and the four fishing-benefit/detriment tags. Do not mix these pools with the separate Fishing Cage loot table or vanilla fishing loot.

### Important trap-dispatch finding

The checked released `getTrapsPoolForLocation` method calls the **normal `getPoolForBiome`**, despite a separate `getTrapsPoolForBiome` implementation existing. Its bytes are identical to the ordinary location wrapper. The FishingTrapSpawn ability calls that trap-named location wrapper.

Consequently, the six-entry trap files alone do not establish that this ability actually uses them through that path. This is a **verified static routing mismatch**, not an in-game reproduction or a claim that the current private Enderloom build is fixed or affected. A repair should dispatch to the trap-biome lookup and verify water/lava, biome overrides, defaults, player eligibility and event cancellation in the exact target build.

## Troubleshooting

| Symptom | Check |
|---|---|
| Crafted rod or cage will not equip/use normally | Check the shipped skill requirement and your pack's requirement settings. Crafting is not an unlock bypass. |
| Water rod disappears in lava | Use the thermal rod for lava. |
| Bobber keeps vanishing | Holding-item, owner-distance, terrain collision, canceled/repeated use and owner-alive checks are distinct causes. |
| Nothing lands after the initial wait | A generated catch still has to reach the bobber, hook and be reeled within landing distance. |
| Small pond feels slow | Source-fluid count penalties and biome/weather/player proximity affect the timer. |
| Lava fishing is unexpectedly slow | Check nearby-player penalty, source-fluid volume and thermal biome/temperature factors. |
| Golden Rod did not appear after a Shiny Squid kill | It is a low-weight entry, not a guaranteed reward. |
| Trap behavior does not match the trap JSON | Inspect the released dispatch mismatch before trusting those files as runtime proof. |

## Evidence and limits

[Resource and released-class evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hauling-rods-evidence-1.21.1.json) records the recipes, skill data, pools, selected methods, four durability constructors, trap caller and four independent dispatch cases. [Illustration provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hauling-rod-art-evidence-1.21.1.json) records the official item-model inputs.

Primary pinned source: [HaulingRod](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/tool/misc/HaulingRod.java), [HaulingFishingBobberEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/misc/HaulingFishingBobberEntity.java), and [HaulingSpawnPool](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/skill/hauling/HaulingSpawnPool.java). No live catch-rate test, runtime repair or private-build certification is claimed. AoA artwork and systems: Tslat and contributors; vanilla references: Mojang/Microsoft.
