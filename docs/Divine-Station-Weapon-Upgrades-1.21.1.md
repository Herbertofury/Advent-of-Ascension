# Divine Station weapon upgrades · Minecraft 1.21.1

**Version:** released AoA 3.7.16.1. This guide covers **36 shipped upgrade recipe definitions**, using **18 upgrade ingredients: 17 named kits plus Weapon Parts**. Their presence in the archive does not prove every station, weapon or kit is obtainable in a stock Survival world. No station-output crafting recipe was found by this audit; check the actual pack's acquisition additions.

[Recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&type=aoa3%3Aupgrade_kit) · [Items and blocks](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&q=upgrade_kit)

## 1. Match the weapon and upgrade ingredient

This is a **Divine Station** recipe type, not a promise that placing two items in an ordinary crafting grid will work.

1. Check the exact input weapon in the route list below. A related-looking weapon or one from another release is insufficient.
2. Put the input weapon in the station's **first input slot**, on the left.
3. Put the specified kit or Weapon Parts in the **second input slot**, in the middle.
4. Read the output preview on the right before taking it. The menu searches the upgrade recipe type with these two positional inputs.
5. Compare the resulting weapon's details and components. Do not spend a valuable customized item until the exact pack's preservation policy is tested.

The inspected crafting-result slot applies the recipe's remaining-items path and removes one item from each occupied input as it processes a completed craft. Quick-move, cancellation, external events and altered remainder behavior still require actual target-build tests.

## 2. Understand what carries over

**The base recipe does not copy the input weapon.** Its assembly method returns a copy of the configured output stack. It does not read input damage, enchantments, custom name, battery/stored-cast data or other input components to transfer them.

All 36 inspected output declarations contain an item ID and count of one; none explicitly declares transferred input components. This is different from a repair operation that copies your existing item and changes only damage.

The parent menu also fires a crafting event, and datapacks/mod integrations can change results. Therefore this is a **base-recipe behavior finding, not a claim of unconditional component loss in every modpack**. Inspect the preview and test a disposable sample. If the restoration intentionally preserves selected components, implement an explicit compatibility policy rather than blindly carrying the old weapon's stats into a different weapon type.

An “upgrade” name also does not prove that every statistic improves. Compare ammunition, firing behavior, resource costs and the actual output's stats before choosing a route.

## 3. Illustrated route catalog

These are source-model item illustrations, not proposed TaCZ replacement models or in-game screenshots. Each row shows input weapon + required ingredient → configured output.

### Routes 1–6

![Six named upgrade routes with input, ingredient and output pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/upgrade-kit-routes-1.21.1-1.webp)

| Input weapon | Upgrade ingredient | Output weapon | Definition |
|---|---|---|---|
| Wither Cannon | Abyssal Upgrade Kit | Bulb Cannon | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_bulb_cannon) |
| Power Ray | Abyssal Upgrade Kit | Death Ray | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_death_ray) |
| Alacrity Bow | Ancient Upgrade Kit | Ancient Bow | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_ancient_bow) |
| Discharge Cannon | Ancient Upgrade Kit | Ancient Discharger | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_ancient_discharger) |
| Spirit Shower | Apoco Upgrade Kit | Apoco Shower | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_apoco_shower) |
| Overshot | Clown Upgrade Kit | Clownershot | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_clownershot) |

### Routes 7–12

![Six named upgrade routes with input, ingredient and output pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/upgrade-kit-routes-1.21.1-2.webp)

| Input weapon | Upgrade ingredient | Output weapon | Definition |
|---|---|---|---|
| Monster | Darkly Upgrade Kit | Dark Beast | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_dark_beast) |
| Wrecker | Darkly Upgrade Kit | Darkener | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_darkener) |
| RPG | Floro Upgrade Kit | Floro RPG | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_floro_rpg) |
| Iro Rifle | Floro Upgrade Kit | Floro Rifle | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_floro_rifle) |
| MK | Fungal Upgrade Kit | MK-Fung | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_mk_fung) |
| Flaming Fury | Golden Upgrade Kit | Golden Fury | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_golden_fury) |

### Routes 13–18

![Six named upgrade routes with input, ingredient and output pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/upgrade-kit-routes-1.21.1-3.webp)

| Input weapon | Upgrade ingredient | Output weapon | Definition |
|---|---|---|---|
| Boulder Bomber | Golden Upgrade Kit | Golder Bomber | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_golder_bomber) |
| Red Rocket | Haunted Upgrade Kit | Purple Punisher | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_purple_punisher) |
| Roulette | Haunted Upgrade Kit | Skullette | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_skullette) |
| Blood Iron | Light Upgrade Kit | Light Iron | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_light_iron) |
| Soul Spark | Light Upgrade Kit | Light Spark | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_light_spark) |
| Lunar Greatblade | Light Upgrade Kit | Millennium Greatblade | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_millennium_greatblade) |

### Routes 19–24

![Six named upgrade routes with input, ingredient and output pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/upgrade-kit-routes-1.21.1-4.webp)

| Input weapon | Upgrade ingredient | Output weapon | Definition |
|---|---|---|---|
| Dark Destroyer | Lunar Upgrade Kit | Moon Destroyer | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_moon_destroyer) |
| Fireborne Sword | Nether Upgrade Kit | Candlefire Sword | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_candlefire_sword) |
| Hot Shot | Nether Upgrade Kit | Heat Wave | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_heat_wave) |
| Bayonette Rifle | Nether Upgrade Kit | Nethenette Rifle | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_nethenette_rifle) |
| Nethengeic Slugger | Precasian Upgrade Kit | Precasian Slugger | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_precasian_slugger) |
| Tommy | Precasian Upgrade Kit | Tiger Tommy | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_tiger_tommy) |

### Routes 25–30

![Six named upgrade routes with input, ingredient and output pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/upgrade-kit-routes-1.21.1-5.webp)

| Input weapon | Upgrade ingredient | Output weapon | Definition |
|---|---|---|---|
| Striker Staff | Predator Upgrade Kit | Lightning Staff | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_lightning_staff) |
| Minigun | Predator Upgrade Kit | Predigun | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_predigun) |
| Demolisher | Rocky Upgrade Kit | Boulder | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_boulder) |
| Proton | Rocky Upgrade Kit | Fragment | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_fragment) |
| Mint Magnum | Seaside Upgrade Kit | Aqua Magnum | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_aqua_magnum) |
| Predatious Bow | Seaside Upgrade Kit | Atlantic Bow | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_atlantic_bow) |

### Routes 31–36

![Six named upgrade routes with input, ingredient and output pictures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/upgrade-kit-routes-1.21.1-6.webp)

| Input weapon | Upgrade ingredient | Output weapon | Definition |
|---|---|---|---|
| Brown Blaster | Seaside Upgrade Kit | Blue Barrel | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_blue_barrel) |
| Balloon Bomber | Seaside Upgrade Kit | Water-Balloon Bomber | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_water_balloon_bomber) |
| Big Blast | Smiley Upgrade Kit | Blissful Blast | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_blissful_blast) |
| Haunter Rifle | Smiley Upgrade Kit | Happy Haunter | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_happy_haunter) |
| Minigun | Weapon Parts | Megagun | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_megagun) |
| Stampede | Weapon Parts | Roulette | [Inspect](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=aoa3%3Aupgrade_kit_roulette) |

## 4. Choose branches deliberately

Minigun has two distinct routes in these files: **Weapon Parts → Megagun** and **Predator Upgrade Kit → Predigun**. The required ingredient selects the branch; there is no automatic “best” output.

Another sequence spans multiple recipes: **Stampede + Weapon Parts → Roulette**, followed by **Roulette + Haunted Upgrade Kit → Skullette**. Each step is its own configured output and its own component-preservation check. Do not assume the second stage is a free continuation of the first.

For kit acquisition, use the versioned loot/trade references and your installed recipe viewer. A kit's name does not prove it drops from a similarly named dimension boss. This page does not invent missing recipes or acquisition routes.

## Troubleshooting

| Symptom | Check |
|---|---|
| Nothing appears | Correct station, exact input weapon in slot 0 and required ingredient in slot 1. |
| You swapped the two inputs | The matcher is positional; restore the weapon-left / kit-middle order. |
| A similarly named weapon fails | These 36 definitions use exact item ingredients. |
| A name or enchantment does not appear in the preview | The base recipe copies the configured output, not the input weapon. |
| You cannot craft the station or kit | Acquisition is not established merely by these upgrade definitions; inspect pack additions. |
| Your result differs from this page | Check the release, datapack overrides and crafting-event integrations. |
| The output is not better for your build | Compare actual weapon mechanics and costs rather than treating the word upgrade as a universal DPS guarantee. |

## Relationship to the optional weapon overhaul

These are native AoA item-conversion recipes. The [optional weapon presentation overhaul](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) is a separate planned feature with reversible models/animations and optional reload behavior. A gallery image here does not certify that a TaCZ remodel or integration has been implemented.

## Restoration acceptance

[All 36 recipe hashes and selected released menu/recipe methods](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/upgrade-kit-evidence-1.21.1.json) · [Illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/upgrade-kit-art-evidence-1.21.1.json) · [Source findings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes).

Test vanilla and modified input components, wrong kit, wrong slot order, quick move, full inventory, canceled or changed crafting events, preview refresh and deliberate preservation rules. Confirm active registry entries and acquisition routes in the exact restoration build. No game mod code was executed and no private Enderloom upgrade behavior is certified.

AoA models, textures, names and systems are by Tslat and contributors. The galleries and route analysis are original documentation work.
