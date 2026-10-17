# Shotguns, cannons and snipers: choose a loadout with the right numbers

[Direct gun defaults](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Statistics-and-Ammunition-1.21.1) · [Ammunition and pouch precautions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ammunition-and-Void-Pouch-1.21.1) · [Weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Divine-Station-Weapon-Upgrades-1.21.1)

![Six released shotgun, cannon and sniper model examples](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/wrapped-gun-statistics-overview-1.21.1.webp)

**Exact scope:** Minecraft 1.21.1, AoA 3.7.16.1. This guide covers 94 released registrations: 17 shotguns, 50 cannons and 27 snipers. Their wrapper defaults, callback instructions and registration factories were read separately and joined by registered ID. Together with the direct-gun guide, 172 modern weapons have expandable stat panels beside their model previews. These are released component defaults, not measured combat outcomes.

## Prepare a loadout

1. Choose a weapon in the tables below and open its model card.
2. Expand its released-defaults panel. Check the ammunition ID and whether it came from the family default or an explicit override.
3. Follow the ammo reference into the item browser or recipe search. Check acquisition and costs before leaving base.
4. For shotguns, compare pellet count and spread as well as the damage input. For snipers, compare scope symbols and zoom modifiers. Cannons need a separate understanding of their projectile and explosion behavior.
5. Inspect the upgrade recipe and component-preservation warning before upgrading a valuable stack.

The panels are created only when expanded. They reuse the selected release’s inventory data and make no additional network request for statistics.

## Family defaults and exceptions

| Family | Count | Default ammunition | Released default firing mode |
|---|---:|---|---|
| Shotguns | 17 | Spreadshot (`aoa3:spreadshot`) | Semi-auto |
| Cannons | 50 | Cannonball (`aoa3:cannonball`) | Semi-auto |
| Snipers | 27 | Metal Slug (`aoa3:metal_slug`) | Semi-auto |

All 94 extracted callbacks retain semi-auto mode. Several replace ammunition, including Discharge Capsule, Grenade, Balloon, vanilla Carrot and vanilla Cobblestone. The tables and panels preserve those overrides. Do not copy Limonite Bullet or full-auto defaults from the direct-gun family into these weapons.

## Shotgun damage: the important distinction

The released base `AoAShotgun.createFiringContext` applies `multiplyDamage(1 / pelletCount)` and sets a lifespan input of 4. The configured damage input therefore must not be labelled damage per pellet. It also is not a guaranteed total when every pellet lands: special subclasses, collision, target defenses, components and effects still need checking. Pellet spread and knockback values are modifiers, not measured angles or distances.

## Sniper scope: a symbol, not a magnification promise

The released sniper builder starts with `AoASniper.BASIC_SCOPE` and zoom-strength modifier 1. Explicit scope and zoom overrides are preserved. A symbolic scope reference is not a verified texture preview, and the zoom modifier is not a measured optical magnification.

## Cannon damage: investigate the projectile too

A damage input alone cannot describe blast radius, explosion damage, special effects or block interaction. Use these numbers to identify the configured weapon, then test its actual projectile behavior in the matching release. This documentation does not certify world safety or runtime balance.

## Shotgun references

| Weapon | Damage input | Interval (ticks) | Durability | Ammunition | Family detail |
|---|---:|---:|---:|---|---|
| [Abyssro](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aabyssro) | 37 | 46 | 1100 | `aoa3:spreadshot` | 12 pellets; spread 0.3 |
| [Amplifier](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aamplifier) | 45 | 56 | 1100 | `aoa3:spreadshot` | 30 pellets; spread 0.2 |
| [Blast Barrel](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablast_barrel) | 39 | 62 | 740 | `aoa3:spreadshot` | 18 pellets; spread 0.4 |
| [Blue Barrel](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablue_barrel) | 43.5 | 54 | 1120 | `aoa3:spreadshot` | 18 pellets; spread 0.4 |
| [Boulder](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aboulder) | 46 | 58 | 1080 | `aoa3:spreadshot` | 24 pellets; spread 0.4 |
| [Brown Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abrown_blaster) | 18 | 54 | 300 | `aoa3:spreadshot` | 18 pellets; spread 0.4 |
| [Demolisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ademolisher) | 34 | 58 | 730 | `aoa3:spreadshot` | 24 pellets; spread 0.4 |
| [Destruction Shotgun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adestruction_shotgun) | 31.5 | 56 | 690 | `aoa3:spreadshot` | 18 pellets; spread 0.4 |
| [Discharge Shotgun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adischarge_shotgun) | 0 | 55 | 160 | `aoa3:discharge_capsule` | 24 pellets; spread 0 |
| [Gimmick](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agimmick) | 45 | 68 | 800 | `aoa3:spreadshot` | 60 pellets; spread 0.2 |
| [Ginger Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aginger_blaster) | 35 | 60 | 720 | `aoa3:spreadshot` | 30 pellets; spread 0.4 |
| [Long Shot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Along_shot) | 31 | 54 | 730 | `aoa3:spreadshot` | 12 pellets; spread 0.2 |
| [Mechyro](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amechyro) | 26 | 46 | 720 | `aoa3:spreadshot` | 12 pellets; spread 0.3 |
| [Purity Shotgun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apurity_shotgun) | 42 | 56 | 1090 | `aoa3:spreadshot` | 18 pellets; spread 0.4 |
| [Purple Punisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apurple_punisher) | 41 | 52 | 1120 | `aoa3:spreadshot` | 12 pellets; spread 0.785 |
| [Red Rocket](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ared_rocket) | 23 | 52 | 500 | `aoa3:spreadshot` | 12 pellets; spread 0.785 |
| [Vivo](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avivo) | 21 | 36 | 710 | `aoa3:spreadshot` | 18 pellets; spread 0.3 |

## Cannon references

| Weapon | Damage input | Interval (ticks) | Durability | Ammunition | Family detail |
|---|---:|---:|---:|---|---|
| [Ancient Bomber](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aancient_bomber) | 23.5 | 28 | 855 | `aoa3:grenade` | Check projectile / explosion separately |
| [Ancient Discharger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aancient_discharger) | 0 | 20 | 850 | `aoa3:discharge_capsule` | Check projectile / explosion separately |
| [Aqua Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aaqua_cannon) | 14 | 35 | 300 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Balloon Bomber](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aballoon_bomber) | 12.5 | 24 | 505 | `aoa3:balloon` | Check projectile / explosion separately |
| [Big Blast](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abig_blast) | 28 | 60 | 550 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Blast Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablast_cannon) | 17 | 27 | 510 | `aoa3:grenade` | Check projectile / explosion separately |
| [Blissful Blast](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablissful_blast) | 33.5 | 60 | 835 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Bomb Launcher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abomb_launcher) | 23 | 27 | 840 | `aoa3:grenade` | Check projectile / explosion separately |
| [Boom Boom](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aboom_boom) | 18.5 | 36 | 390 | `aoa3:grenade` | Check projectile / explosion separately |
| [Boom Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aboom_cannon) | 17.5 | 28 | 510 | `aoa3:grenade` | Check projectile / explosion separately |
| [Boulder Bomber](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aboulder_bomber) | 18.5 | 62 | 475 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Bozo Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abozo_blaster) | 12.5 | 20 | 505 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Bulb Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abulb_cannon) | 25 | 30 | 860 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Carrot Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acarrot_cannon) | 10 | 16 | 520 | `minecraft:carrot` | Check projectile / explosion separately |
| [Clown Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aclown_cannon) | 22.5 | 32 | 570 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Clowno-Pulse](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aclowno_pulse) | 35.5 | 42 | 845 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Coral Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoral_cannon) | 12 | 15 | 300 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Discharge Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adischarge_cannon) | 0 | 20 | 400 | `aoa3:discharge_capsule` | Check projectile / explosion separately |
| [Energy Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aenergy_cannon) | 18.5 | 25 | 610 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Erebon Stickler](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aerebon_stickler) | 35 | 48 | 750 | `aoa3:grenade` | Check projectile / explosion separately |
| [Floro RPG](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afloro_rpg) | 18 | 50 | 830 | `aoa3:grenade` | Check projectile / explosion separately |
| [Flower Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aflower_cannon) | 14.5 | 23 | 510 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Fungal Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afungal_cannon) | 19.5 | 23 | 850 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Ghast Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aghast_blaster) | 20 | 28 | 600 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Ghoul Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aghoul_cannon) | 25.5 | 34 | 590 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Giga Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agiga_cannon) | 25.5 | 30 | 700 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Golder Bomber](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agolder_bomber) | 26 | 62 | 840 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Hive Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahive_blaster) | 20.5 | 24 | 850 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Hive Howitzer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahive_howitzer) | 13 | 24 | 375 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Iro Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Airo_cannon) | 25.5 | 36 | 580 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Jack Funger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajack_funger) | 17 | 20 | 860 | `minecraft:cobblestone` | Check projectile / explosion separately |
| [Jack Rocker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajack_rocker) | 10.5 | 20 | 400 | `minecraft:cobblestone` | Check projectile / explosion separately |
| [Luxon Stickler](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aluxon_stickler) | 35 | 48 | 750 | `aoa3:grenade` | Check projectile / explosion separately |
| [Mecha Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_cannon) | 26.5 | 42 | 525 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Mini Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amini_cannon) | 15 | 30 | 415 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Missile Maker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amissile_maker) | 0 | 60 | 495 | `aoa3:grenade` | Check projectile / explosion separately |
| [Moon Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amoon_cannon) | 21 | 25 | 855 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Pluton Stickler](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apluton_stickler) | 35 | 48 | 750 | `aoa3:grenade` | Check projectile / explosion separately |
| [Predatorian Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apredatorian_blaster) | 23.5 | 28 | 845 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Pulse Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apulse_cannon) | 26 | 42 | 510 | `aoa3:cannonball` | Check projectile / explosion separately |
| [RPG](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arpg) | 8 | 50 | 320 | `aoa3:grenade` | Check projectile / explosion separately |
| [Selyan Stickler](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aselyan_stickler) | 35 | 48 | 750 | `aoa3:grenade` | Check projectile / explosion separately |
| [Shadow Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashadow_blaster) | 15 | 24 | 515 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Shyre Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashyre_blaster) | 25.5 | 30 | 850 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Smile Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asmile_blaster) | 20.5 | 24 | 840 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Super Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asuper_cannon) | 18.5 | 30 | 510 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Ultra Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aultra_cannon) | 22.5 | 30 | 605 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Vox Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avox_cannon) | 15 | 26 | 440 | `aoa3:cannonball` | Check projectile / explosion separately |
| [Water-Balloon Bomber](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awater_balloon_bomber) | 20.5 | 24 | 855 | `aoa3:balloon` | Check projectile / explosion separately |
| [Wither Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awither_cannon) | 17 | 30 | 460 | `aoa3:cannonball` | Check projectile / explosion separately |

## Sniper references

| Weapon | Damage input | Interval (ticks) | Durability | Ammunition | Family detail |
|---|---:|---:|---:|---|---|
| [Baron SSR](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_ssr) | 35 | 88 | 240 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Bayonette SR](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abayonette_sr) | 33 | 86 | 300 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Bolt Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abolt_rifle) | 30 | 100 | 100 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Camo Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acamo_rifle) | 31.5 | 84 | 150 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Clown Cracker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aclown_cracker) | 33.5 | 84 | 305 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Clownimator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aclownimator) | 49.5 | 95 | 545 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Crystaneer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystaneer) | 37.5 | 88 | 345 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Dark Beast](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adark_beast) | 50.5 | 96 | 560 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Deadlock](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adeadlock) | 25.5 | 90 | 120 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Decimator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adecimator) | 33 | 95 | 180 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Discharge Sniper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adischarge_sniper) | 10 | 24 | 540 | `aoa3:discharge_capsule` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Dual Sight](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adual_sight) | 38.5 | 91 | 350 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 2 |
| [Duster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aduster) | 21 | 60 | 170 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Floro500](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afloro500) | 37 | 70 | 550 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Head Hunter](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahead_hunter) | 41.5 | 92 | 380 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Hive Cracker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahive_cracker) | 44 | 84 | 555 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [KA-500](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aka_500) | 30 | 70 | 360 | `aoa3:metal_slug` | `AoASniper.AERIAL_SCOPE`; zoom 1 |
| [Mark Maker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amark_maker) | 36.5 | 70 | 530 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Mineral](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amineral) | 58.5 | 112 | 560 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Monster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amonster) | 38 | 96 | 250 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Moon Maker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amoon_maker) | 38.5 | 70 | 570 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Rosid Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosid_rifle) | 45.5 | 102 | 405 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Sabbath](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asabbath) | 44 | 97 | 450 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Sludge Sniper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asludge_sniper) | 37 | 87 | 350 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |
| [Sweet Tooth](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asweet_tooth) | 32.5 | 77 | 460 | `aoa3:metal_slug` | `AoASniper.BASIC_SCOPE`; zoom 1 |
| [Terminator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aterminator) | 53 | 112 | 470 | `aoa3:metal_slug` | `AoASniper.MOA_SCOPE`; zoom 1 |
| [Viper-1](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aviper_1) | 30 | 89 | 185 | `aoa3:metal_slug` | `AoASniper.CLASSIC_SCOPE`; zoom 1 |

## Evidence and remaining checks

[Released wrapper, callback, factory and base firing-context evidence](https://herbertofury.github.io/Advent-of-Ascension/wrapped-gun-statistics-evidence-1.21.1.json) includes class hashes and instruction bytes. The exact archive is `AoA3-1.21.1-3.7.16.1.jar`. Source models belong to Tslat and contributors; the overview is an original static documentation render, not an in-game screenshot or animation.

- Values retain raw floating-point inputs in evidence; tables display six significant digits.
- Scope is these three wrapper families, not all AoA weapons. Bows, staves and other types remain separate work.
- No DPS ranking, hit probability, explosion radius or real-time firing-rate claim is inferred from these values.
- Confirm subclass overrides, modified stacks, enchantments, multiplayer synchronization and actual ammo consumption in a matching game before using the table as a balance specification.
- Historical versions have their own constructor-input guide; no modern wrapper defaults are applied to them.
