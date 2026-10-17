[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Weapon references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Later historical comparison](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Gun-Constructor-References)

# Historical guns: constructor inputs and recoil · 1.12.2

**Minecraft 1.12.2 / AoA 3.3.6.** This guide joins 78 direct gun registrations to their released item constructors and exact historical localization cards. These are inspected inputs, not measured final damage, DPS, ammunition behavior or a complete gun-family simulation.

![Four historical gun source-model previews with exact constructor inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/gun-constructor-inputs-1.12.2.webp)

## Read the item card

1. Open a gun below. Its card selects the 1.12.2 release and exact historical localization entry.
2. Expand **1.12.2 gun inputs · damage, timing and durability**.
3. Compare the damage, firing-delay, durability and recoil arguments. These are four literal values supplied by the released registration method.
4. Read the configuration and subclass limits before choosing a weapon. The linked recipe and drop searches are separate acquisition references, not promises that every registered item is obtainable in Survival.

Panels build only when opened, reuse the selected-release inventory data and make no additional stat requests. Reopening a panel does not rebuild its contents. Modern 1.21.1 components and the later historical schema remain separate.

## Recoil differs from later releases

The inspected 1.12.2 **getRecoil() returns the stored recoil field**. Its base getRecoilForShot method calls that getter. Do not insert the later 1.16.5/1.20.1 base getter's approximately 0.35 value into this edition.

This establishes the selected base methods, not every subclass override or complete shot path. Enchantments and other shot processing can modify the value before the client uses it. No units such as degrees are invented for this constructor argument.

## AoA hardcoreMode changes the base damage getter

The released base getDamage method multiplies its stored damage by **1.25 when AoA's hardcoreMode configuration is enabled**, otherwise by 1. This configuration branch is separate from Minecraft world difficulty or the world's Hardcore selection.

A constructor damage argument is therefore not always the getter's result, and neither is automatically the health removed by a projectile hit. Target defenses, enchantments, subclasses, projectile behavior and other mods need their own checks. Do not calculate an authoritative DPS ranking by dividing these raw inputs.

## Exact-release comparison

Each linked name opens its own source-model portrait and input panel. Tick intervals are registration arguments, not guaranteed real-time shot cadence under server load.

| Gun and portrait | Damage input | Delay input · ticks | Durability input | Recoil input |
|---|---:|---:|---:|---:|
| [Abominator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Abominator.name) | 10.5 | 12 | 1180 | 3 |
| [Apoco Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ApocoAssaultRifle.name) | 22.5 | 24 | 1480 | 6 |
| [Apoco Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ApocoRifle.name) | 10 | 24 | 1490 | 6 |
| [Aqua Magnum](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AquaMagnum.name) | 7.5 | 8 | 1520 | 4 |
| [Artifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Artifact.name) | 19 | 20 | 1500 | 3 |
| [Baronator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Baronator.name) | 12 | 20 | 620 | 3 |
| [Bayonette Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BayonetteRifle.name) | 12.5 | 20 | 630 | 4 |
| [Big Top](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BigTop.name) | 12.5 | 16 | 920 | 4 |
| [Blood Iron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BloodIron.name) | 24.5 | 32 | 870 | 14 |
| [Chain Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ChainWrecker.name) | 6 | 8 | 960 | 2 |
| [Chilli Chugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ChilliChugger.name) | 12 | 16 | 890 | 2 |
| [Clownershot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Clownershot.name) | 8 | 16 | 1470 | 7 |
| [Construct](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Construct.name) | 9.5 | 12 | 910 | 4 |
| [Coral Clogger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralClogger.name) | 33 | 40 | 500 | 15 |
| [Core Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoreRifle.name) | 7.5 | 12 | 630 | 3 |
| [Crystal Carver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystalCarver.name) | 12 | 16 | 870 | 5 |
| [Cyclone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Cyclone.name) | 9.5 | 12 | 1100 | 3 |
| [Darkener](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Darkener.name) | 11.5 | 12 | 1510 | 7 |
| [Dart Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DartGun.name) | 10 | 20 | 360 | 0.2 |
| [Destruction Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DestructionRifle.name) | 12.5 | 20 | 610 | 5 |
| [Discharge Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DischargeRifle.name) | 5 | 24 | 570 | 6 |
| [Draco](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Draco.name) | 15 | 16 | 1390 | 2 |
| [Dragilator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Dragilator.name) | 6.5 | 8 | 1120 | 4 |
| [Dustometer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Dustometer.name) | 21 | 24 | 1180 | 7 |
| [Echo Gull](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EchoGull.name) | 17.5 | 28 | 580 | 6 |
| [Electinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Electinator.name) | 6.5 | 8 | 1120 | 4 |
| [Flame Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FlameWrecker.name) | 7.5 | 8 | 1530 | 2 |
| [Flaming Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FlamingFury.name) | 20.5 | 28 | 860 | 4 |
| [Floro Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FloroRifle.name) | 15 | 16 | 1500 | 4 |
| [Flower's Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FlowersFury.name) | 13 | 16 | 1100 | 5 |
| [Frosticator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Frosticator.name) | 6.5 | 8 | 1120 | 4 |
| [Gardener](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Gardener.name) | 7 | 12 | 630 | 2 |
| [Gauge Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GaugeRifle.name) | 22.5 | 36 | 590 | 8 |
| [Germinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Germinator.name) | 6.5 | 8 | 1120 | 4 |
| [Golden Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoldenFury.name) | 26 | 28 | 1520 | 4 |
| [Happy Haunter](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HappyHaunter.name) | 11.5 | 12 | 1510 | 3 |
| [Haunter Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HaunterRifle.name) | 11 | 12 | 1420 | 3 |
| [Heat Wave](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HeatWave.name) | 23.5 | 24 | 1470 | 5 |
| [Hiver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Hiver.name) | 11.5 | 12 | 1490 | 4 |
| [Hot Shot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HotShot.name) | 14.5 | 24 | 580 | 5 |
| [Hunter's Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HuntersRifle.name) | 21.5 | 28 | 900 | 4 |
| [Iominator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Iominator.name) | 11.5 | 12 | 1500 | 3 |
| [Ion Revolver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IonRevolver.name) | 9.5 | 12 | 930 | 3 |
| [Iro Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IroRifle.name) | 12.5 | 16 | 910 | 4 |
| [Krilinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Krilinator.name) | 15 | 20 | 900 | 4 |
| [Light Iron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LightIron.name) | 30.5 | 32 | 1470 | 14 |
| [Lunar Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarAssaultRifle.name) | 11.5 | 12 | 1430 | 5 |
| [Mechanical Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechanicalAssaultRifle.name) | 18.5 | 24 | 940 | 6 |
| [Megagun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Megagun.name) | 4 | 4 | 1530 | 3 |
| [Miasma](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Miasma.name) | 9 | 12 | 940 | 3 |
| [Minigun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Minigun.name) | 2.5 | 4 | 670 | 3 |
| [Mint Magnum](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MintMagnum.name) | 6 | 8 | 900 | 4 |
| [MK](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MK.name) | 14.5 | 16 | 1240 | 3 |
| [MK-Fung](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MKFung.name) | 15 | 16 | 1490 | 3 |
| [Nethenette Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethenetteRifle.name) | 18.5 | 20 | 1500 | 4 |
| [Nethengeic Slugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethengeicSlugger.name) | 22.5 | 32 | 780 | 9 |
| [Overshot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Overshot.name) | 6.5 | 16 | 990 | 7 |
| [Precasian Slugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrecasianSlugger.name) | 29.5 | 32 | 1490 | 9 |
| [Predator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Predator.name) | 25.5 | 28 | 1480 | 6 |
| [Predigun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Predigun.name) | 4 | 4 | 1530 | 3 |
| [Pulsator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Pulsator.name) | 25 | 28 | 1190 | 6 |
| [Purity Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityRifle.name) | 18 | 20 | 1200 | 3 |
| [Rocker Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RockerRifle.name) | 10 | 16 | 630 | 6 |
| [Roulette](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Roulette.name) | 22.5 | 24 | 1470 | 8 |
| [Shoe Flinger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShoeFlinger.name) | 24 | 24 | 400 | 7 |
| [Skullette](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Skullette.name) | 23.5 | 24 | 1580 | 8 |
| [Skullifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Skullifact.name) | 19.5 | 20 | 1570 | 3 |
| [Spectacle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Spectacle.name) | 11 | 16 | 880 | 3 |
| [Spine Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpineGun.name) | 11.5 | 12 | 1510 | 7 |
| [Squad Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SquadGun.name) | 10.5 | 12 | 1210 | 7 |
| [Stampede](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Stampede.name) | 12 | 24 | 300 | 8 |
| [Stormer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Stormer.name) | 15 | 20 | 900 | 3 |
| [Sublimus](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Sublimus.name) | 11 | 12 | 1530 | 5 |
| [Tiger Tommy](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TigerTommy.name) | 11.5 | 12 | 1490 | 7 |
| [Tommy](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Tommy.name) | 6 | 12 | 330 | 7 |
| [Vile Vanquisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VileVanquisher.name) | 11 | 16 | 930 | 3 |
| [Wart Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WartGun.name) | 16.5 | 28 | 580 | 1 |
| [Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Wrecker.name) | 9.5 | 12 | 920 | 7 |

## Scope and next checks

- The 78 entries are direct constructors from the gun package in the inspected registration method. Shotguns, snipers, cannons, archerguns and other weapon families are not silently counted here.
- Exact registry strings and localization keys come from the released item constructors. The explorer still labels its overall historical inventory as a resource/localization catalog rather than claiming a full runtime registry census.
- Ammunition costs, firing-mode rules, projectile damage and unique gun effects are not established by these four inputs alone.
- Runtime accuracy, compatibility, animation, sound and optional TaCZ remodelling remain separate work. These references do not require a reload mechanic for weapons whose original resources work differently.

[Released registration windows, constructor identities and base-method evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-gun-inputs-1.12.2.json) · [Image crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gun-input-art-evidence-1.12.2.json).
