# Divine Station weapon upgrades · Minecraft 1.20.1

**Released AoA 3.7.1: 70 recipe definitions, 19 ingredients (18 named upgrade kits plus Weapon Parts).** This is the version-specific reference for the first TaCZ-upgrade target. The [1.21.1 guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Divine-Station-Weapon-Upgrades-1.21.1) has a different catalog; do not interchange their routes.

## How to use the station

1. Match the exact input weapon and ingredient in a route below.
2. Place the weapon in the **left input**, and its kit or Weapon Parts in the **middle input**.
3. Read the **right-hand output preview** before taking it. These are Divine Station recipes, not ordinary crafting-grid recipes.
4. Completing a craft processes one item from each occupied input, with the recipe's remaining-item handling.
5. Test valuable customized weapons on a disposable copy first. Check name, damage/durability, enchantments and mod-specific data before spending your main item.

The inventory's input indices are 0 and 1; menu slot 0 is the result. Integrations must not confuse these two indexing schemes. Quick-move, cancellation, external crafting events and altered remainders still need native pack tests.

## What carries over?

The inspected base recipe assembles a **copy of its configured output stack**. It does not itself copy the input weapon's NBT, name, enchantments, durability or added attachment data. All 70 output definitions specify one item, with no explicit input-data transfer.

The parent result slot fires a Forge crafting event. Other integrations can alter behavior, so this finding does not prove unconditional data loss in every modpack. Our attachment/charms bridge needs a deliberate transfer policy: preserve compatible user customization, validate incompatible parts, and never silently transplant an old weapon's complete gameplay state into a different type.

An upgrade's name also does not guarantee every stat improves. Compare ammo, resource cost and behavior, not only damage.

## Availability and version limits

Recipe presence is not proof that every weapon, kit or the station is obtainable in stock Survival. This archive scan found the station's block self-drop but no crafting recipe declaring the station as its output. Acquisition additions and restrictions must be checked in the actual pack. This guide is a shipped-data/bytecode audit, not an in-game walkthrough completion claim.

## Illustrated route catalog

Each row shows the released input sprite + required ingredient → output sprite. These are source-derived reference diagrams, not proposed TaCZ models or game screenshots. Animated source textures show their first configured frame. Art credit: Tslat and Advent of Ascension contributors.

### Routes 1–7

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-1.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Mechyro | Abyssal Upgrade Kit | Abyssro | `aoa3:upgrade_kit_abyssro` |
| Wither Cannon | Abyssal Upgrade Kit | Bulb Cannon | `aoa3:upgrade_kit_bulb_cannon` |
| Power Ray | Abyssal Upgrade Kit | Death Ray | `aoa3:upgrade_kit_death_ray` |
| Boom Cannon | Ancient Upgrade Kit | Ancient Bomber | `aoa3:upgrade_kit_ancient_bomber` |
| Alacrity Bow | Ancient Upgrade Kit | Ancient Bow | `aoa3:upgrade_kit_ancient_bow` |
| Discharge Cannon | Ancient Upgrade Kit | Ancient Discharger | `aoa3:upgrade_kit_ancient_discharger` |
| Abominator | Ancient Upgrade Kit | Iominator | `aoa3:upgrade_kit_iominator` |

### Routes 8–14

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-2.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Mechanical Assault Rifle | Apoco Upgrade Kit | Apoco Assault Rifle | `aoa3:upgrade_kit_apoco_assault_rifle` |
| Discharge Rifle | Apoco Upgrade Kit | Apoco Rifle | `aoa3:upgrade_kit_apoco_rifle` |
| Spirit Shower | Apoco Upgrade Kit | Apoco Shower | `aoa3:upgrade_kit_apoco_shower` |
| Overshot | Clown Upgrade Kit | Clownershot | `aoa3:upgrade_kit_clownershot` |
| Decimator | Clown Upgrade Kit | Clownimator | `aoa3:upgrade_kit_clownimator` |
| Pulse Cannon | Clown Upgrade Kit | Clowno-Pulse | `aoa3:upgrade_kit_clowno_pulse` |
| Monster | Darkly Upgrade Kit | Dark Beast | `aoa3:upgrade_kit_dark_beast` |

### Routes 15–21

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-3.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Wrecker | Darkly Upgrade Kit | Darkener | `aoa3:upgrade_kit_darkener` |
| Whimsy Winder | Darkly Upgrade Kit | Darkly Guster | `aoa3:upgrade_kit_darkly_guster` |
| RPG | Floro Upgrade Kit | Floro RPG | `aoa3:upgrade_kit_floro_rpg` |
| Iro Rifle | Floro Upgrade Kit | Floro Rifle | `aoa3:upgrade_kit_floro_rifle` |
| KA-500 | Floro Upgrade Kit | Floro500 | `aoa3:upgrade_kit_floro500` |
| Flower Cannon | Fungal Upgrade Kit | Fungal Cannon | `aoa3:upgrade_kit_fungal_cannon` |
| Jack Rocker | Fungal Upgrade Kit | Jack Funger | `aoa3:upgrade_kit_jack_funger` |

### Routes 22–28

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-4.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| MK | Fungal Upgrade Kit | MK-Fung | `aoa3:upgrade_kit_mk_fung` |
| Destruction Shotgun | Fungal Upgrade Kit | Purity Shotgun | `aoa3:upgrade_kit_purity_shotgun` |
| Blood Drainer | Fungal Upgrade Kit | Soul Drainer | `aoa3:upgrade_kit_soul_drainer` |
| Doom Bringer | Golden Upgrade Kit | Gold Bringer | `aoa3:upgrade_kit_gold_bringer` |
| Flaming Fury | Golden Upgrade Kit | Golden Fury | `aoa3:upgrade_kit_golden_fury` |
| Boulder Bomber | Golden Upgrade Kit | Golder Bomber | `aoa3:upgrade_kit_golder_bomber` |
| Red Rocket | Haunted Upgrade Kit | Purple Punisher | `aoa3:upgrade_kit_purple_punisher` |

### Routes 29–35

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-5.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Roulette | Haunted Upgrade Kit | Skullette | `aoa3:upgrade_kit_skullette` |
| Artifact | Haunted Upgrade Kit | Skullifact | `aoa3:upgrade_kit_skullifact` |
| Luna Blaster | Haunted Upgrade Kit | Skullo Blaster | `aoa3:upgrade_kit_skullo_blaster` |
| Shadow Blaster | Lelyetian Upgrade Kit | Hive Blaster | `aoa3:upgrade_kit_hive_blaster` |
| Clown Cracker | Lelyetian Upgrade Kit | Hive Cracker | `aoa3:upgrade_kit_hive_cracker` |
| Construct | Lelyetian Upgrade Kit | Hiver | `aoa3:upgrade_kit_hiver` |
| Mind Blaster | Light Upgrade Kit | Light Blaster | `aoa3:upgrade_kit_light_blaster` |

### Routes 36–42

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-6.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Blood Iron | Light Upgrade Kit | Light Iron | `aoa3:upgrade_kit_light_iron` |
| Soul Spark | Light Upgrade Kit | Light Spark | `aoa3:upgrade_kit_light_spark` |
| Lunar Greatblade | Light Upgrade Kit | Millennium Greatblade | `aoa3:upgrade_kit_millennium_greatblade` |
| Energy Cannon | Lunar Upgrade Kit | Moon Cannon | `aoa3:upgrade_kit_moon_cannon` |
| Dark Destroyer | Lunar Upgrade Kit | Moon Destroyer | `aoa3:upgrade_kit_moon_destroyer` |
| Mark Maker | Lunar Upgrade Kit | Moon Maker | `aoa3:upgrade_kit_moon_maker` |
| Fireborne Sword | Nether Upgrade Kit | Candlefire Sword | `aoa3:upgrade_kit_candlefire_sword` |

### Routes 43–49

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-7.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Chain Wrecker | Nether Upgrade Kit | Flame Wrecker | `aoa3:upgrade_kit_flame_wrecker` |
| Hot Shot | Nether Upgrade Kit | Heat Wave | `aoa3:upgrade_kit_heat_wave` |
| Bubble Horn | Nether Upgrade Kit | Hell Horn | `aoa3:upgrade_kit_hell_horn` |
| Bayonette Rifle | Nether Upgrade Kit | Nethenette Rifle | `aoa3:upgrade_kit_nethenette_rifle` |
| Nethengeic Slugger | Precasian Upgrade Kit | Precasian Slugger | `aoa3:upgrade_kit_precasian_slugger` |
| Squad Gun | Precasian Upgrade Kit | Spine Gun | `aoa3:upgrade_kit_spine_gun` |
| Tommy | Precasian Upgrade Kit | Tiger Tommy | `aoa3:upgrade_kit_tiger_tommy` |

### Routes 50–56

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-8.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Striker Staff | Predator Upgrade Kit | Lightning Staff | `aoa3:upgrade_kit_lightning_staff` |
| Pulsator | Predator Upgrade Kit | Predator | `aoa3:upgrade_kit_predator` |
| Ghast Blaster | Predator Upgrade Kit | Predatorian Blaster | `aoa3:upgrade_kit_predatorian_blaster` |
| Minigun | Predator Upgrade Kit | Predigun | `aoa3:upgrade_kit_predigun` |
| Demolisher | Rocky Upgrade Kit | Boulder | `aoa3:upgrade_kit_boulder` |
| Proton | Rocky Upgrade Kit | Fragment | `aoa3:upgrade_kit_fragment` |
| Terminator | Rocky Upgrade Kit | Mineral | `aoa3:upgrade_kit_mineral` |

### Routes 57–63

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-9.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Mint Magnum | Seaside Upgrade Kit | Aqua Magnum | `aoa3:upgrade_kit_aqua_magnum` |
| Predatious Bow | Seaside Upgrade Kit | Atlantic Bow | `aoa3:upgrade_kit_atlantic_bow` |
| Brown Blaster | Seaside Upgrade Kit | Blue Barrel | `aoa3:upgrade_kit_blue_barrel` |
| Orb-O-Cron | Seaside Upgrade Kit | Sea-O-Cron | `aoa3:upgrade_kit_seaocron` |
| Balloon Bomber | Seaside Upgrade Kit | Water-Balloon Bomber | `aoa3:upgrade_kit_water_balloon_bomber` |
| Big Blast | Smiley Upgrade Kit | Blissful Blast | `aoa3:upgrade_kit_blissful_blast` |
| Haunter Rifle | Smiley Upgrade Kit | Happy Haunter | `aoa3:upgrade_kit_happy_haunter` |

### Routes 64–70

![Input, ingredient and output for seven upgrade routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1-10.webp)

| Input weapon | Ingredient | Output weapon | Definition |
|---|---|---|---|
| Shadow Blaster | Smiley Upgrade Kit | Smile Blaster | `aoa3:upgrade_kit_smile_blaster` |
| Stormer | Weapon Parts | Artifact | `aoa3:upgrade_kit_artifact` |
| Blast Cannon | Weapon Parts | Bomb Launcher | `aoa3:upgrade_kit_bomb_launcher` |
| Discharge Rifle | Weapon Parts | Discharge Sniper | `aoa3:upgrade_kit_discharge_sniper` |
| KA-500 | Weapon Parts | Mark Maker | `aoa3:upgrade_kit_mark_maker` |
| Minigun | Weapon Parts | Megagun | `aoa3:upgrade_kit_megagun` |
| Stampede | Weapon Parts | Roulette | `aoa3:upgrade_kit_roulette` |

## Evidence and reproduction

- [Machine-readable routes, exact texture paths and hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/upgrade-kit-routes-1.20.1.json)
- [Reproducible diagram/index builder](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/upgrade-kit-study-1.20.1.zip)
- Source: [official released AoA 3.7.1 archive](https://cdn.modrinth.com/data/9qn2AQBc/versions/ADsBtG85/AoA3-1.20.1-3.7.1-all.jar)
- Inspected classes: UpgradeKitRecipe, DivineStationContainer, CustomResultSlot, and the JEI category/transfer mapping. The audit does not execute the mod.

### Remaining acceptance work

Test an unmodified weapon, named/enhanced weapon, attachment-bearing weapon, damaged weapon and unknown extension tags. Check ordinary take and quick-move, multiplayer synchronization, recipe-book restrictions, cancellation and crafting-event integrations. Document allowed transfers and unsupported fields before promoting an upgrade bridge to playable status.

## Every bundled upgrade, pictured

[Divine Station illustrated upgrade atlas](Divine-Station-Upgrade-Atlas) covers all 70 bundled upgrade-kit recipes, organized by 19 kit families, with exact base item, kit and output sprites. First frames are used for animated textures; diagrams are not native screenshots.
