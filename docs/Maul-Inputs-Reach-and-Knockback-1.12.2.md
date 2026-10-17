[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

# Historical mauls: damage, speed, reach and knockback inputs

**Minecraft 1.12.2 / AoA 3.3.6.** All five direct maul registrations are checked, including their boxed Float/Double constructor arguments and the WeaponSpeed enum reference.

## Inputs are not measured outcomes

All five registrations use **WeaponSpeed.THIRD = −3.46667** as the speed modifier. That is not a negative firing rate or a duration in seconds. Damage inputs pass through the base getter's optional AoA hardcore multiplier of 1.25 and the later attack pipeline.

Knockback is a configured input, not a promise of that many blocks of travel. Target resistance, motion, terrain, effects and later attack logic still matter. The base reach getter returns **4**; its attribute setup uses a difference from 3.5, which is not by itself a certified hit distance.

## All five registered mauls

| Maul and portrait | Damage input | Durability input | Speed modifier | Knockback input |
|---|---:|---:|---:|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-coralstone_maul.webp" alt="Coralstone Maul source-model portrait" width="72" height="72" loading="lazy"><br> [Coralstone Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralstoneMaul.name) | 26.5 | 1600 | -3.46667 | 3.6 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-crystal_maul.webp" alt="Crystal Maul source-model portrait" width="72" height="72" loading="lazy"><br> [Crystal Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystalMaul.name) | 23.5 | 1400 | -3.46667 | 3.1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-electron_maul.webp" alt="Electron Maul source-model portrait" width="72" height="72" loading="lazy"><br> [Electron Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ElectronMaul.name) | 25 | 1500 | -3.46667 | 3.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-horizon_maul.webp" alt="Horizon Maul source-model portrait" width="72" height="72" loading="lazy"><br> [Horizon Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HorizonMaul.name) | 23 | 1300 | -3.46667 | 3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-vulcammer_maul.webp" alt="Vulcammer Maul source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcammer Maul](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VulcammerMaul.name) | 28 | 1750 | -3.46667 | 3.5 |

![Selected historical melee source-model portraits, with deliberately distinct input labels](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/melee-inputs-1.12.2.webp)

## Cooldown, wear and attack behavior still need context

The base maul class has its own attack and effect path, rather than simply being a sword with a large displayed number. Its capability-backed cooldown handoff, knockback handling, target types and item wear should be tested together when restoring or remodeling it.

The five table rows are checked inputs. This page does not yet provide a complete review of each maul's subclass effect or a runtime comparison of knockback distance.

## Practical and restoration checklist

1. Keep the release and family fixed when comparing inputs. A material bonus and a direct damage field are different quantities.
2. Use the linked item portrait and exact same-release recipe/drop searches for acquisition; registration alone does not prove Survival availability.
3. Compare normal and AoA-hardcore settings, cooldown states, target defenses, attributes and enchantments independently.
4. Test the actual hit, effect, wear and synchronization path before claiming final damage, DPS, range or compatibility.
5. Retain each weapon's identity in optional animated remodels; do not replace these mechanics with generic firearm rules.

[Released registrations, material definitions, speed constants and selected behavior methods](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-melee-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/melee-art-evidence-1.12.2.json).
