# Melee weapons: separate tier inputs from property-helper routing

[Open the item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Repair preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1) · [Vulcanes and Rage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-and-Rage-1.21.1)

![Eight released melee models illustrating distinct tier and property-helper paths](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/melee-property-overview-1.21.1.webp)

**Scope:** 68 released melee registrations in Minecraft 1.21.1 / AoA 3.7.16.1: 34 swords, 29 Greatblade-family items including Pluton Scythe, and five mauls. Their tier definitions, registration factories and straight-line property-helper calls are traced separately. The resulting panel is a source reference, not a measured combat benchmark.

Together with the other weapon-family panels, every one of the **411 registrations in the inspected released `AoAWeapons` class** has a reference panel. This is a bounded registration census, not proof of every runtime item, addon weapon or gameplay mechanic.

## Choose and inspect a weapon

1. Open a weapon below to see its source-model preview and exact-version recipe/drop links.
2. Expand **Melee properties · tier inputs and actual helper routing**.
3. Compare durability and enchantability, then inspect the damage and speed fields as separate inputs.
4. Check the normal tier repair ingredient. Follow an archive-declared repair member when present; active tags can differ in a modpack.
5. Read any routing warning before treating the displayed tier number as a final character stat.
6. In the actual target build, compare the equipped main-hand attributes, cooldown behavior and an ordinary hit before testing special effects.

## What the fields mean

- **Tier damage input:** the number supplied to AoA’s tier builder.
- **Stored tier damage bonus:** the released builder stores the damage input minus one. This is a separate intermediate value.
- **Extra damage argument:** the value eventually passed into the selected attribute-building helper after its overload chain.
- **Attack-speed argument:** a modifier argument, not seconds or measured attacks per second. Negative and positive values are preserved as released.
- **Durability and enchantability inputs:** tier defaults, not a promise about every enchanted or modified stack.

The sword path also delegates to a Minecraft/NeoForge attribute overload. The guide does not silently substitute the unpatched vanilla client implementation for that loader-specific path. Player base attributes, modifiers, cooldown strength, criticals, target defenses and subclass effects are outside these simple input columns.

## Why tool-tier speed needs special care

Some melee registrations reuse a tool tier. Its stored speed may describe a tool property rather than the intended combat modifier. Emberstone, Jade and Limonite swords explicitly supply a sword-speed override. Skeletal Sword explicitly supplies an extra damage argument of 1 and a speed argument of -2.

The inspected Rock-Pick Sword and Troll-Basher Axe factories instead forward their stored tool-tier speed 9.5 into the selected melee property helper. That positive input is retained, not “corrected” by assumption. Verify intended design and actual equipped attributes before changing it.

## Registered property inputs

### Sword family

| Weapon | Tier damage input | Extra damage argument | Speed argument | Durability | Enchantability |
|---|---:|---:|---:|---:|---:|
| [Baron Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_sword) | 12 | 0 | -2.4 | 1975 | 15 |
| [Bloodfury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abloodfury) | 13 | 0 | -2.2 | 1990 | 11 |
| [Bloodstone Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abloodstone_sword) | 15 | 0 | -2.4 | 1990 | 11 |
| [Candlefire Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acandlefire_sword) | 18 | 0 | -2.4 | 2985 | 15 |
| [Caramel Carver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acaramel_carver) | 16.5 | 0 | -2.4 | 2400 | 15 |
| [Coralstorm Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoralstorm_sword) | 9 | 0 | -2.4 | 1800 | 15 |
| [Creepified Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acreepified_sword) | 14.5 | 0 | -2.4 | 2090 | 15 |
| [Crystallite Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystallite_sword) | 15 | 0 | -2.3 | 2310 | 12 |
| [Emberstone Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aemberstone_sword) | 12 | 0 | -2.4 | 2050 | 12 |
| [Explochron Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aexplochron_sword) | 16 | 0 | -2.4 | 2360 | 15 |
| [Faunamancer's Blade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afaunamancers_blade) | 4 | 0 | -0.8 | 280 | 20 |
| [Fireborne Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afireborne_sword) | 13 | 0 | -2.4 | 1995 | 15 |
| [Guardian's Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aguardians_sword) | 16 | 0 | -2.4 | 2420 | 15 |
| [Harvester Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aharvester_sword) | 18.5 | 0 | -2.4 | 2550 | 15 |
| [Holy Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aholy_sword) | 1 | 0 | 0.8 | 2500 | 18 |
| [Illusion Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aillusion_sword) | 15.5 | 0 | -2.4 | 2300 | 15 |
| [Jade Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajade_sword) | 7.5 | 0 | -2.4 | 950 | 12 |
| [Legbone Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alegbone_sword) | 12.5 | 0 | -2.4 | 2020 | 15 |
| [Light's Way](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alights_way) | 8.5 | 0 | -0.8 | 2900 | 12 |
| [Limonite Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alimonite_sword) | 6.5 | 0 | -2.4 | 176 | 3 |
| [Nethengeic Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anethengeic_sword) | 15 | 0 | -2.4 | 2120 | 15 |
| [Primal Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aprimal_sword) | 14 | 0 | -2.4 | 2060 | 15 |
| [Rock-Pick Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arock_pick_sword) | 13 | 0 | 9.5 | 2100 | 15 |
| [Rockbasher Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arockbasher_sword) | 17 | 0 | -2.4 | 2430 | 15 |
| [Rosidian Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_sword) | 16.5 | 0 | -2.4 | 2430 | 15 |
| [Runic Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arunic_sword) | 18.5 | 0 | -2.4 | 2690 | 15 |
| [Shadow Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashadow_sword) | 18 | 0 | -2.4 | 2585 | 15 |
| [Shroomus Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashroomus_sword) | 16 | 0 | -2.4 | 2295 | 15 |
| [Skeletal Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_sword) | 10 | 1 | -2 | 1900 | 12 |
| [Supremacy Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asupremacy_sword) | 15.5 | 0 | -2.4 | 2270 | 15 |
| [Sweet Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asweet_sword) | 16 | 0 | -2.4 | 2360 | 15 |
| [Troll-Basher Axe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atroll_basher_axe) | 13 | 0 | 9.5 | 1800 | 15 |
| [Ultraflame](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aultraflame) | 16 | 0 | -2.4 | 2350 | 15 |
| [Void Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avoid_sword) | 11.5 | 0 | -2.4 | 1750 | 11 |

### Greatblade family

| Weapon | Tier damage input | Extra damage argument | Speed argument | Durability | Enchantability |
|---|---:|---:|---:|---:|---:|
| [Baron Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_greatblade) | 20.5 | 0 | -3.24 | 1200 | 13 |
| [Bloodlurker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abloodlurker) | 22 | 0 | -3.24 | 1350 | 13 |
| [Candy Blade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acandy_blade) | 24 | 0 | -3.24 | 1450 | 13 |
| [Coral Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoral_greatblade) | 25.5 | 0 | -3.24 | 1800 | 13 |
| [Cotton Crusher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acotton_crusher) | 25 | 0 | -3.24 | 1600 | 13 |
| [Creepoid Greataxe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acreepoid_greataxe) | 20 | 0 | -3.24 | 1080 | 13 |
| [Crystal Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystal_greatblade) | 23 | 0 | -3.24 | 1480 | 13 |
| [Erebon Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aerebon_scythe) | 20 | 0 | -3 | 1750 | 13 |
| [God's Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agods_greatblade) | 30.5 | 0 | -3.24 | 2000 | 13 |
| [Goofy Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agoofy_greatblade) | 23 | 0 | -3.24 | 1300 | 13 |
| [Haunted Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahaunted_greatblade) | 27 | 0 | -3.24 | 1875 | 13 |
| [Knight's Guard](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aknights_guard) | 27.5 | 0 | -3.24 | 2050 | 13 |
| [Lelyetian Ranseur](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alelyetian_ranseur) | 19.5 | 0 | -3.24 | 1100 | 13 |
| [Lunar Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_greatblade) | 13.5 | 0 | -3.24 | 1850 | 13 |
| [Luxon Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aluxon_scythe) | 18.5 | 0 | -2.8 | 1750 | 13 |
| [Lyonic Bardiche](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alyonic_bardiche) | 20 | 0 | -3.1 | 1420 | 13 |
| [Millennium Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amillennium_greatblade) | 14.25 | 0 | -3.24 | 2050 | 13 |
| [Noxious Partizan](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anoxious_partizan) | 24 | 0 | -3.24 | 1580 | 13 |
| [Pluton Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apluton_scythe) | 20 | 0 | -3 | 1750 | 13 |
| [Primordial Glaive](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aprimordial_glaive) | 26.5 | 0 | -3.24 | 1900 | 13 |
| [Rosidian Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_greatblade) | 23.5 | 0 | -3.24 | 1470 | 13 |
| [Royal Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aroyal_greatblade) | 20 | 0 | -3.24 | 1130 | 13 |
| [Runic Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arunic_greatblade) | 25.5 | 0 | -3.24 | 1800 | 13 |
| [Selyan Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aselyan_scythe) | 20 | 0 | -3 | 1750 | 13 |
| [Shroomic Bardiche](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashroomic_bardiche) | 22.5 | 0 | -3.24 | 1300 | 13 |
| [Shyre Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashyre_sword) | 27 | 0 | -3.24 | 2000 | 13 |
| [Subterranean Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asubterranean_greatblade) | 22.5 | 0 | -3.24 | 1160 | 13 |
| [Tidal Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atidal_greatblade) | 25 | 0 | -3.24 | 1750 | 13 |
| [Underworld Glaive](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aunderworld_glaive) | 19.5 | 0 | -3.24 | 1050 | 13 |

### Maul family

| Weapon | Tier damage input | Extra damage argument | Speed argument | Durability | Enchantability |
|---|---:|---:|---:|---:|---:|
| [Coralstone Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoralstone_maul) | 26.5 | -3.46667 | 0 | 1600 | 8 |
| [Crystal Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystal_maul) | 23.5 | -3.46667 | 0 | 1400 | 8 |
| [Electron Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aelectron_maul) | 25 | -3.46667 | 0 | 1500 | 8 |
| [Horizon Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahorizon_maul) | 23 | -3.46667 | 0 | 1300 | 8 |
| [Vulcammer Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avulcammer_maul) | 28 | -3.46667 | 0 | 1750 | 8 |

## Eight normal repair-tag references

Sixty selected tiers supply an empty normal repair ingredient. That does not mean every repair mechanism is impossible: custom recipes, the Mending Table, enchantments or integrations need their own checks.

| Weapon | Released tag reference | Member declared by this archive |
|---|---|---|
| [Baron Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_sword) | `#c:ingots/baronyte` | [aoa3:baronyte_ingot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaronyte_ingot) |
| [Bloodstone Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abloodstone_sword) | `#c:gems/bloodstone` | [aoa3:bloodstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abloodstone) |
| [Crystallite Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystallite_sword) | `#c:gems/crystallite` | [aoa3:crystallite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystallite) |
| [Emberstone Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aemberstone_sword) | `#c:ingots/emberstone` | [aoa3:emberstone_ingot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aemberstone_ingot) |
| [Jade Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajade_sword) | `#c:gems/jade` | [aoa3:jade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajade) |
| [Light's Way](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alights_way) | `#c:ingots/shyrestone` | [aoa3:shyrestone_ingot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashyrestone_ingot) |
| [Limonite Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alimonite_sword) | `#c:ingots/limonite` | [aoa3:limonite_ingot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alimonite_ingot) |
| [Skeletal Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_sword) | `#c:ingots/skeletal` | [aoa3:skeletal_ingot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_ingot) |

Tag membership is not frozen by this table. The evidence records the released tag initializer, namespace helper and resource JSON; active datapacks can extend or replace those definitions.

## Maintainer regression target: Maul overload argument order

All five selected Maul factories call the two-argument `baseProperties(tier, knockback)` overload. The released forwarding chain supplies nominal Maul speed approximately -3.46667 and a zero damage-modifier input, then a later overload forwards argument positions into `createAttributes` differently. The resulting selected call receives **extra damage argument approximately -3.46667 and speed argument 0**, with the registered knockback and reach input 0.5 retained.

This is a concrete static call trace, not an in-game reproduction or an applied fix. Test each maul’s equipped damage/speed/knockback/reach, attack cadence and shield behavior in the exact target build. If correcting the overload chain, keep its signature and argument meaning consistent throughout and preserve unrelated special effects. Do not replace the values with intended-looking numbers in documentation before the code and tests establish them.

## Maintainer regression target: Pluton Scythe’s helper overload

The selected registration requests the one-argument `PlutonScythe.baseProperties(tier)` signature. Method resolution finds the inherited `AoAGreatblade` implementation, whose own forwarding calls remain in the Greatblade helper chain. The separate two-argument Pluton Scythe helper that adds a Luck modifier is not reached by this inspected factory path.

Do not claim the two-argument helper’s Luck addition merely because that method exists. Confirm the intended default attributes and test the registered item, its special melee effect and any modified-stack path. Other systems may supply Luck independently; this finding does not claim a player can never have it.

## Acceptance checklist

- Check all 68 exact registered IDs, family classification and relevant repair tags.
- Compare tier inputs, property-helper arguments and actual main-hand attributes separately.
- Test tool-tier reuse and explicit speed overrides without normalizing away positive values.
- Test Maul overload routing, special knockback behavior and reach.
- Test Pluton Scythe’s registered default construction separately from directly calling its alternate helper.
- Test normal repairs, custom repairs, enchantments, damage state, multiplayer and modified components.

[Released registration/property traces, helper method bytes and repair-tag resources](https://herbertofury.github.io/Advent-of-Ascension/melee-property-evidence-1.21.1.json) · [Source-model illustration provenance](https://herbertofury.github.io/Advent-of-Ascension/melee-art-evidence-1.21.1.json).

Archive: `AoA3-1.21.1-3.7.16.1.jar`. The restricted expression reader does not execute Java or resolve a live registry. Existing 420-field extraction remained byte-identical after adding the symbolic primitive-load support needed for these helpers. AoA models and mechanics are credited to Tslat and contributors. No private Enderloom runtime fix is claimed.
