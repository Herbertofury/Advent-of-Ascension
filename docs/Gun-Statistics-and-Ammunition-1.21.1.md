# Gun statistics and ammunition: read the registered defaults

[Open the illustrated item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Ammo preparation and pouch precautions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ammunition-and-Void-Pouch-1.21.1) · [Weapon upgrade routes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Divine-Station-Weapon-Upgrades-1.21.1) · [Historical 1.16.5 / 1.20.1 inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Gun-Constructor-References)

![Six gun models with their ammunition and default-stat examples](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/gun-statistics-overview-1.21.1.webp)

**Coverage:** 78 direct `GunProperties.of` registrations in Minecraft 1.21.1 / AoA 3.7.16.1. The values were read from released class instructions and joined through their released registration factories. This is not a complete weapon census: [94 wrapped shotguns, cannons and snipers now have their own guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Shotgun-Cannon-and-Sniper-Statistics-1.21.1); bows, staves and other families remain separate work.

## How to use the numbers

1. Open an item below to see its existing model image and recipe/drop links.
2. Expand **Released gun defaults · damage, timing and ammo**.
3. Check the ammo before preparing a loadout. Several guns use a different item or a tag rather than the default Limonite Bullet.
4. Compare the configured damage, interval and durability without mistaking them for measured combat performance.
5. Read special weapon behavior and upgrade/component warnings before treating two similar stat lines as identical weapons.

The panel is built only when expanded. Its data arrives with the selected inventory release; it does not add a scan, manifest request or separate stats download to every card. Existing per-release caching and lazy images remain in place.

## What each field means

| Field | Meaning and limits |
|---|---|
| Damage input | Value supplied to the registered gun-stat component. It is not guaranteed final health loss, damage per second or a number of hearts. |
| Shot interval | Configured tick interval. Tick rate, charging/animation logic, firing mode and special behavior can affect actual throughput. |
| Durability | Literal value passed by the released registration factory when creating the item properties. Actual wear per action and enchantment behavior are separate. |
| Fire mode | Released full-auto default or explicit semi-auto override. This alone does not certify input handling or animation timing. |
| Recoil modifier | A configured modifier, not an angle in degrees. |
| Unholster-time modifier | A configured modifier, not a duration in seconds. |
| Ammunition | Released default or explicit builder override. Tag-based ammunition depends on active tag data and is not a fixed universal list. |

The underlying machine-readable evidence preserves the released floating-point values. Display values are rounded to six significant digits for readability. A player's current stack may have changed components; this static atlas does not inspect that stack. No DPS leaderboard is inferred by dividing these fields.

## Ammunition differences worth noticing

Most covered builders inherit Limonite Bullet ammunition, but the override is important when present:

- Apoco Rifle and Discharge Rifle explicitly reference Discharge Capsules.
- Several heavier-looking guns, including Heat Wave and Hot Shot, reference Metal Slugs.
- Chilli Chugger references Chilli.
- Shoe Flinger references vanilla Leather Boots; Wart Gun references vanilla Nether Wart.
- Dart Gun and Gardener reference `NeoForge Tags.Items.SEEDS`. The table preserves that symbolic tag identity without inventing its current membership or equating every seed-like mod item with a valid ingredient.

These are registration defaults. They do not replace testing consumption, Creative behavior, ammo-pouch interactions, projectile effects or mod compatibility. The ammo-pouch guide records a separate released storage-rejection risk.

## All 78 covered registrations

Each weapon name opens its exact-release illustrated item card. “Damage” and “ticks” retain the limited meanings above. Fire mode and the two modifiers are available in the expandable card panel and evidence file.

| Weapon / illustrated card | Damage input | Interval ticks | Durability | Ammunition reference |
|---|---:|---:|---:|---|
| [Abominator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aabominator) | 2.625 | 3 | 4720 | `aoa3:limonite_bullet` |
| [Apoco Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aapoco_assault_rifle) | 5.625 | 6 | 5920 | `aoa3:limonite_bullet` |
| [Apoco Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aapoco_rifle) | 2.5 | 6 | 5960 | `aoa3:discharge_capsule` |
| [Aqua Magnum](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aaqua_magnum) | 2.0625 | 2 | 6080 | `aoa3:limonite_bullet` |
| [Artifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aartifact) | 10 | 5 | 6000 | `aoa3:limonite_bullet` |
| [Baronator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaronator) | 3 | 5 | 2480 | `aoa3:limonite_bullet` |
| [Bayonette Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abayonette_rifle) | 3.4375 | 5 | 2520 | `aoa3:limonite_bullet` |
| [Big Top](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abig_top) | 3.125 | 4 | 3680 | `aoa3:limonite_bullet` |
| [Blood Iron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablood_iron) | 6.125 | 8 | 3480 | `aoa3:metal_slug` |
| [Chain Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Achain_wrecker) | 1.5 | 2 | 3840 | `aoa3:limonite_bullet` |
| [Chilli Chugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Achilli_chugger) | 3 | 4 | 3560 | `aoa3:chilli` |
| [Clownershot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aclownershot) | 2 | 4 | 5880 | `aoa3:limonite_bullet` |
| [Construct](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aconstruct) | 2.375 | 3 | 3640 | `aoa3:limonite_bullet` |
| [Coral Clogger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoral_clogger) | 9.075 | 10 | 2000 | `aoa3:metal_slug` |
| [Core Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acore_rifle) | 1.875 | 3 | 2520 | `aoa3:limonite_bullet` |
| [Crystal Carver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystal_carver) | 3 | 4 | 3480 | `aoa3:limonite_bullet` |
| [Cyclone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acyclone) | 2.375 | 3 | 4400 | `aoa3:limonite_bullet` |
| [Darkener](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adarkener) | 2.875 | 3 | 6040 | `aoa3:limonite_bullet` |
| [Dart Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adart_gun) | 4.675 | 5 | 4520 | `NeoForge Tags.Items.SEEDS` |
| [Destruction Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adestruction_rifle) | 3.125 | 5 | 2440 | `aoa3:limonite_bullet` |
| [Discharge Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adischarge_rifle) | 1.25 | 6 | 2280 | `aoa3:discharge_capsule` |
| [Draco](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adraco) | 3.75 | 4 | 5560 | `aoa3:limonite_bullet` |
| [Dragilator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adragilator) | 1.625 | 2 | 4480 | `aoa3:limonite_bullet` |
| [Dustometer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adustometer) | 5.25 | 6 | 4720 | `aoa3:limonite_bullet` |
| [Echo Gull](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aecho_gull) | 4.375 | 7 | 2320 | `aoa3:limonite_bullet` |
| [Electinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aelectinator) | 1.625 | 2 | 4480 | `aoa3:limonite_bullet` |
| [Flame Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aflame_wrecker) | 1.875 | 2 | 6120 | `aoa3:limonite_bullet` |
| [Flaming Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aflaming_fury) | 5.125 | 7 | 3440 | `aoa3:limonite_bullet` |
| [Floro Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afloro_rifle) | 3.75 | 4 | 6000 | `aoa3:limonite_bullet` |
| [Flower's Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aflowers_fury) | 3.25 | 4 | 4400 | `aoa3:limonite_bullet` |
| [Frosticator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afrosticator) | 1.625 | 2 | 4480 | `aoa3:limonite_bullet` |
| [Gardener](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agardener) | 1.75 | 3 | 2520 | `NeoForge Tags.Items.SEEDS` |
| [Gauge Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agauge_rifle) | 5.625 | 9 | 2360 | `aoa3:metal_slug` |
| [Germinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agerminator) | 1.625 | 2 | 4480 | `aoa3:limonite_bullet` |
| [Golden Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agolden_fury) | 6.5 | 7 | 6080 | `aoa3:limonite_bullet` |
| [Happy Haunter](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahappy_haunter) | 2.875 | 3 | 6040 | `aoa3:limonite_bullet` |
| [Haunter Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahaunter_rifle) | 2.75 | 3 | 5680 | `aoa3:limonite_bullet` |
| [Heat Wave](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aheat_wave) | 6.05 | 6 | 5880 | `aoa3:metal_slug` |
| [Hiver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahiver) | 2.875 | 3 | 5960 | `aoa3:limonite_bullet` |
| [Hot Shot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahot_shot) | 3.9875 | 6 | 2320 | `aoa3:metal_slug` |
| [Hunter's Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahunters_rifle) | 5.9125 | 7 | 3600 | `aoa3:limonite_bullet` |
| [Iominator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aiominator) | 2.875 | 3 | 6000 | `aoa3:limonite_bullet` |
| [Ion Revolver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aion_revolver) | 2.6125 | 3 | 3720 | `aoa3:limonite_bullet` |
| [Iro Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Airo_rifle) | 3.125 | 4 | 3640 | `aoa3:limonite_bullet` |
| [Krilinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Akrilinator) | 3.75 | 5 | 3600 | `aoa3:limonite_bullet` |
| [Light Iron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alight_iron) | 7.625 | 8 | 5880 | `aoa3:metal_slug` |
| [Lunar Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_assault_rifle) | 2.875 | 3 | 5720 | `aoa3:limonite_bullet` |
| [MK](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amk) | 3.625 | 4 | 4960 | `aoa3:limonite_bullet` |
| [MK-Fung](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amk_fung) | 3.75 | 4 | 5960 | `aoa3:limonite_bullet` |
| [Mechanical Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amechanical_assault_rifle) | 4.625 | 6 | 3760 | `aoa3:limonite_bullet` |
| [Megagun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amegagun) | 1 | 1 | 6120 | `aoa3:limonite_bullet` |
| [Miasma](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amiasma) | 2.25 | 3 | 3760 | `aoa3:limonite_bullet` |
| [Minigun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aminigun) | 0.625 | 1 | 2680 | `aoa3:limonite_bullet` |
| [Mint Magnum](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amint_magnum) | 1.65 | 2 | 3600 | `aoa3:limonite_bullet` |
| [Nethenette Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anethenette_rifle) | 5.0875 | 5 | 6000 | `aoa3:limonite_bullet` |
| [Nethengeic Slugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anethengeic_slugger) | 6.1875 | 8 | 3120 | `aoa3:metal_slug` |
| [Overshot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aovershot) | 1.625 | 4 | 3960 | `aoa3:limonite_bullet` |
| [Precasian Slugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aprecasian_slugger) | 8.1125 | 8 | 5960 | `aoa3:metal_slug` |
| [Predator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apredator) | 6.375 | 7 | 5920 | `aoa3:limonite_bullet` |
| [Predigun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apredigun) | 1 | 1 | 6120 | `aoa3:limonite_bullet` |
| [Pulsator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apulsator) | 6.25 | 7 | 4760 | `aoa3:limonite_bullet` |
| [Purity Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apurity_rifle) | 4.5 | 5 | 4800 | `aoa3:limonite_bullet` |
| [Rocker Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arocker_rifle) | 2.5 | 4 | 2520 | `aoa3:limonite_bullet` |
| [Roulette](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aroulette) | 6.1875 | 6 | 5880 | `aoa3:limonite_bullet` |
| [Shoe Flinger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashoe_flinger) | 6 | 6 | 1600 | `minecraft:leather_boots` |
| [Skullette](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askullette) | 6.4625 | 6 | 6320 | `aoa3:limonite_bullet` |
| [Skullifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askullifact) | 10 | 5 | 6280 | `aoa3:limonite_bullet` |
| [Spectacle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspectacle) | 2.75 | 4 | 3520 | `aoa3:limonite_bullet` |
| [Spine Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspine_gun) | 2.875 | 3 | 6040 | `aoa3:limonite_bullet` |
| [Squad Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asquad_gun) | 2.625 | 3 | 4840 | `aoa3:limonite_bullet` |
| [Stampede](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Astampede) | 3.3 | 6 | 1200 | `aoa3:limonite_bullet` |
| [Stormer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Astormer) | 8 | 5 | 3600 | `aoa3:limonite_bullet` |
| [Sublimus](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asublimus) | 2.75 | 3 | 6120 | `aoa3:limonite_bullet` |
| [Tiger Tommy](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atiger_tommy) | 2.875 | 3 | 5960 | `aoa3:limonite_bullet` |
| [Tommy](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atommy) | 1.5 | 3 | 1320 | `aoa3:limonite_bullet` |
| [Vile Vanquisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avile_vanquisher) | 2.75 | 4 | 3320 | `aoa3:limonite_bullet` |
| [Wart Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awart_gun) | 4.5375 | 7 | 2320 | `minecraft:nether_wart` |
| [Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awrecker) | 2.375 | 3 | 3680 | `aoa3:limonite_bullet` |

## Evidence and next coverage

[Pinned stat definitions](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/item/AoAItemStats.java) · [Weapon registrations](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/item/AoAWeapons.java) · [Gun property builder](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/library/builder/item/GunProperties.java).

[Released builder/registration evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gun-statistics-evidence-1.21.1.json) · [Six-model illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gun-statistics-art-evidence-1.21.1.json).

The extraction parses static expressions without loading or executing Java game classes. It follows each selected registration's bootstrap-linked item factory, checks its stat-field reference and literal durability, and keeps the selected builder calls. Shared default ammunition and firing mode are checked in the released builder constructor. Unsupported categories are left out instead of filled with guessed numbers.

Further coverage should independently resolve wrapped builders, subclass-specific effects, enchantments, damage types, ammo consumption and exact-build tests. Preserve the distinction between a configured component, an executable item and measured gameplay. Optional TaCZ presentation/reload plans do not change this native-stat evidence.

AoA item models and mechanics: Tslat and contributors. Original independent reference layout and explanations.
