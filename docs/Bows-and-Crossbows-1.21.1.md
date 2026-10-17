# Bows and crossbows: prepare, draw and charge

[Open the item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Gun ammunition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Statistics-and-Ammunition-1.21.1) · [Weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Divine-Station-Weapon-Upgrades-1.21.1) · [Repairing equipment](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1)

![Six released bow and crossbow models with configured damage and speed modifiers](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/archery-statistics-overview-1.21.1.webp)

**Scope:** 33 bows and 9 crossbows registered in Minecraft 1.21.1 / AoA 3.7.16.1. Values come from released stat-builder instructions joined to the released item registration factories. Source models are static documentation renders. Damage inputs and speed modifiers are not measured hit damage or wall-clock timings.

## Before leaving base

1. Open a weapon below and expand **Released archery defaults · damage, draw and charge**.
2. Inspect its recipe and mob-drop links in the same release. A search can legitimately have no result; a resource entry alone does not prove Survival acquisition.
3. Bring compatible arrows and check the ammunition selected in your actual loadout. The base AoA path delegates selection to the shooter’s projectile lookup, so special-arrow and mod interactions need checking.
4. Compare durability and draw/charge modifiers. A larger speed modifier accelerates the base charge calculation; it is not a duration in seconds.
5. Before using valuable ammunition, test a normal shot, a partial bow draw, a full draw and any enchantments in the matching game build.

## Bow draw: why “speed 2” does not mean two seconds

The released bow path calculates elapsed use ticks, multiplies by the stack’s draw-speed modifier, then truncates to an integer. Player shots next pass through the NeoForge arrow-loose hook. A negative hook result cancels; the inherited power calculation follows, and power below 0.1 returns without firing.

For example, 10 elapsed ticks with Speed Bow’s default modifier 2 produces charge input 20 before that hook. Shyregem Bow’s modifier is 3. These are charge-input examples, not promises about final power, impact damage or real-time latency. Stack components, subclasses, event handlers and game tick rate can affect the outcome.

## Crossbow loading: distinguish three different values

The released reload method starts with `1.25 / chargeSpeedModifier`, applies the enchantment charging-time hook, multiplies the result by 20 and floors to an integer. All nine extracted registrations have modifier 1. With an unchanged hook result, the base calculation is therefore 25 ticks.

- **Reload time** is the value used in the charge-power denominator.
- **Use duration** adds 3 ticks to that reload value. It must not be labelled the reload duration itself.
- **Release/loading** requires charge power at least 1, an uncharged stack, and successful projectile loading.

A loaded stack follows the shooting path when used. The charged-projectile component stores the selected projectile items. Enchantments and data components may change loading behavior; no wall-clock timing or cross-mod compatibility is certified here.

## Damage, ammunition and durability cautions

The shared firing helper sets base damage on an AbstractArrow, applies projectile modifications, creates projectiles and charges durability per nonempty projectile in its loop. Projectile count and spread pass through enchantment processing. This is why neither a damage field nor a default “one projectile” method is enough to promise a final hit total or a flat durability cost for every enchanted shot.

The base ammo lookup delegates to the shooter. An Infinity flag appearing in a calling method is not proof that every special arrow is free or that every empty-inventory case succeeds. Those combinations are explicit test targets, not assumptions in these tables.

## Bow reference table

| Weapon | Damage input | Draw-speed modifier | Durability |
|---|---:|---:|---:|
| [Alacrity Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aalacrity_bow) | 9.5 | 1 | 600 |
| [Ancient Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aancient_bow) | 22 | 1 | 1510 |
| [Atlantic Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aatlantic_bow) | 24.5 | 0.9 | 1480 |
| [Baron Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_bow) | 12 | 1.1 | 3000 |
| [Boreic Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aboreic_bow) | 14 | 1.3 | 1190 |
| [Daybreaker Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adaybreaker_bow) | 17.5 | 1 | 1180 |
| [Deep Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adeep_bow) | 15.5 | 0.85 | 700 |
| [Explosive Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aexplosive_bow) | 17 | 0.8 | 900 |
| [Haunted Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahaunted_bow) | 17 | 1 | 920 |
| [Ice Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aice_bow) | 8.5 | 1 | 580 |
| [Infernal Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ainfernal_bow) | 11.5 | 1 | 710 |
| [Justice Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajustice_bow) | 14.5 | 1 | 920 |
| [Lunar Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_bow) | 17.5 | 1 | 900 |
| [Mecha Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_bow) | 20.5 | 0.75 | 930 |
| [Nightmare Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anightmare_bow) | 13.5 | 1 | 890 |
| [Poison Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apoison_bow) | 15 | 1 | 950 |
| [Predatious Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apredatious_bow) | 14 | 0.9 | 690 |
| [Primordial Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aprimordial_bow) | 18.5 | 1 | 1350 |
| [Rosidian Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_bow) | 15.5 | 1 | 900 |
| [Runic Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arunic_bow) | 20.5 | 1 | 1320 |
| [Screamer Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ascreamer_bow) | 12 | 1 | 665 |
| [Shyregem Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashyregem_bow) | 7.5 | 3 | 1500 |
| [Skeletal Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_bow) | 8.5 | 1.5 | 720 |
| [Skydriver Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askydriver_bow) | 14.5 | 1 | 850 |
| [Slingshot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aslingshot) | 17 | 1 | 1200 |
| [Soulfire Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asoulfire_bow) | 23.5 | 0.75 | 1100 |
| [Spectral Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspectral_bow) | 12 | 1.3 | 900 |
| [Speed Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspeed_bow) | 8 | 2 | 930 |
| [Sunshine Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asunshine_bow) | 27 | 0.8 | 1530 |
| [Toxin Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atoxin_bow) | 14 | 0.85 | 900 |
| [Void Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avoid_bow) | 9 | 1.2 | 600 |
| [Weaken Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aweaken_bow) | 12.5 | 1 | 700 |
| [Wither Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awither_bow) | 13.5 | 1 | 835 |

## Crossbow reference table

| Weapon | Damage input | Charge-speed modifier | Durability |
|---|---:|---:|---:|
| [Coral Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoral_crossbow) | 17 | 1 | 1080 |
| [Lunar Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_crossbow) | 16.5 | 1 | 1100 |
| [Mecha Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_crossbow) | 15 | 1 | 930 |
| [Pyro Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apyro_crossbow) | 12 | 1 | 800 |
| [Rosidian Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_crossbow) | 14.5 | 1 | 900 |
| [Skeletal Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_crossbow) | 12.5 | 1 | 860 |
| [Spectral Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspectral_crossbow) | 15 | 1 | 1030 |
| [Troll's Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atrolls_crossbow) | 10.5 | 1 | 700 |
| [Viral Crossbow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aviral_crossbow) | 11 | 1 | 780 |

## Evidence and acceptance checklist

[Released builder, registration and 16 behavior-method records](https://herbertofury.github.io/Advent-of-Ascension/archery-statistics-evidence-1.21.1.json) · [Illustration provenance](https://herbertofury.github.io/Advent-of-Ascension/archery-statistics-art-evidence-1.21.1.json).

The exact archive is `AoA3-1.21.1-3.7.16.1.jar`; class hashes and instruction bytes are retained. Models and mechanics belong to Tslat and contributors. No game classes were executed to create this reference.

For runtime acceptance, test ordinary and special arrows, empty ammunition, Infinity, projectile-count modifiers, partial/full draws, crossbow loading versus firing, durability at breakage, client/server consistency and modified stack components. Preserve saves and original items. Results from another Minecraft/AoA release are not a substitute for this build.
