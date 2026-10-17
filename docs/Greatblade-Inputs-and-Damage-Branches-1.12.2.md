[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

# Historical greatblades: inputs and variable damage branches

**Minecraft 1.12.2 / AoA 3.3.6.** All 29 direct greatblade registrations are checked. This includes Shyre Sword and the deity scythes because their released classes belong to the greatblade group.

## Inputs, speed and reach

The damage column is the registration input, not a final health delta. The base damage getter applies AoA's hardcore multiplier of 1.25 when enabled, and the later attack path includes additional target, effect and enchantment logic.

A zero speed argument is a sentinel for the released default **−3.2400001287460327**. The table rounds the resolved modifier for readability; the exact value and raw argument are retained in the evidence. It is not an attacks-per-second value.

The base reach getter returns **5**, and its attribute setup uses a difference from 3.5. This is a code input, not a measured universal five-block hit guarantee across targets, servers and compatibility layers.

## All 29 registered greatblades

| Greatblade and portrait | Damage input | Durability input | Speed modifier |
|---|---:|---:|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-baron_greatblade.webp" alt="Baron Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Baron Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronGreatblade.name) | 19.5 | 1200 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-bloodlurker.webp" alt="Bloodlurker source-model portrait" width="72" height="72" loading="lazy"><br> [Bloodlurker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Bloodlurker.name) | 21 | 1350 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-candy_blade.webp" alt="Candy Blade source-model portrait" width="72" height="72" loading="lazy"><br> [Candy Blade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyBlade.name) | 23 | 1450 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-coral_greatblade.webp" alt="Coral Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Coral Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralGreatblade.name) | 24.5 | 1800 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-cotton_crusher.webp" alt="Cotton Crusher source-model portrait" width="72" height="72" loading="lazy"><br> [Cotton Crusher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CottonCrusher.name) | 24 | 1600 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-creepoid_greatblade.webp" alt="Creepoid Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Creepoid Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CreepoidGreatblade.name) | 19 | 1080 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-crystal_greatblade.webp" alt="Crystal Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Crystal Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystalGreatblade.name) | 22 | 1480 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-erebon_scythe.webp" alt="Erebon Scythe source-model portrait" width="72" height="72" loading="lazy"><br> [Erebon Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ErebonScythe.name) | 19 | 1750 | -3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-gods_greatblade.webp" alt="God's Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [God's Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GodsGreatblade.name) | 29.5 | 2000 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-goofy_greatblade.webp" alt="Goofy Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Goofy Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoofyGreatblade.name) | 22 | 1300 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-haunted_greatblade.webp" alt="Haunted Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Haunted Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HauntedGreatblade.name) | 22 | 1370 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-knights_guard.webp" alt="Knight's Guard source-model portrait" width="72" height="72" loading="lazy"><br> [Knight's Guard](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KnightsGuard.name) | 26.5 | 2050 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-lelyetian_greatblade.webp" alt="Lelyetian Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Lelyetian Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LelyetianGreatblade.name) | 18.5 | 1100 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-lunar_greatblade.webp" alt="Lunar Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Lunar Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarGreatblade.name) | 25 | 1850 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-luxon_scythe.webp" alt="Luxon Scythe source-model portrait" width="72" height="72" loading="lazy"><br> [Luxon Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LuxonScythe.name) | 17.5 | 1750 | -2.8 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-lyonic_greatblade.webp" alt="Lyonic Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Lyonic Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicGreatblade.name) | 20 | 1500 | -3.1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-millennium_greatblade.webp" alt="Millennium Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Millennium Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MillenniumGreatblade.name) | 26.5 | 2050 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-noxious_greatblade.webp" alt="Noxious Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Noxious Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NoxiousGreatblade.name) | 23 | 1580 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-pluton_scythe.webp" alt="Pluton Scythe source-model portrait" width="72" height="72" loading="lazy"><br> [Pluton Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PlutonScythe.name) | 19 | 1750 | -3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-primordial_greatblade.webp" alt="Primordial Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Primordial Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrimordialGreatblade.name) | 25.5 | 1900 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-rosidian_greatblade.webp" alt="Rosidian Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Rosidian Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianGreatblade.name) | 22.5 | 1470 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-royal_greatblade.webp" alt="Royal Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Royal Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RoyalGreatblade.name) | 19 | 1130 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-runic_greatblade.webp" alt="Runic Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Runic Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicGreatblade.name) | 24.5 | 1800 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-selyan_scythe.webp" alt="Selyan Scythe source-model portrait" width="72" height="72" loading="lazy"><br> [Selyan Scythe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SelyanScythe.name) | 19 | 1750 | -3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-shroomic_greatblade.webp" alt="Shroomic Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Shroomic Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShroomicGreatblade.name) | 21.5 | 1300 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-shyre_sword.webp" alt="Shyre Sword source-model portrait" width="72" height="72" loading="lazy"><br> [Shyre Sword](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShyreSword.name) | 26 | 2000 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-subterranean_greatblade.webp" alt="Subterranean Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Subterranean Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SubterraneanGreatblade.name) | 21.5 | 1160 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-tidal_greatblade.webp" alt="Tidal Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Tidal Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TidalGreatblade.name) | 24 | 1750 | -3.24 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-underworld_greatblade.webp" alt="Underworld Greatblade source-model portrait" width="72" height="72" loading="lazy"><br> [Underworld Greatblade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UnderworldGreatblade.name) | 18.5 | 1050 | -3.24 |

![Selected historical melee source-model portraits, with deliberately distinct input labels](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/melee-inputs-1.12.2.webp)

## Eight checked damage-argument overrides

These are pre-attack calculations. They are not guarantees of final damage after the remainder of the combat path.

| Greatblade | Selected override |
|---|---|
| Goofy Greatblade | Adds `nextGaussian() × 5` to a float-converted damage getter. A Gaussian is not a fixed ±5 interval. |
| Lelyetian Greatblade | Multiplies the getter by 1.25 for the checked flying-creature helper's match; otherwise returns the getter. |
| Lunar Greatblade | Uses the incoming method argument as the lower endpoint and its stored maxDmg as the other endpoint. See the tooltip distinction below. |
| Millennium Greatblade | Uses the same incoming-argument formula, with maxDmg initialized from the raw constructor damage. |
| Primordial Greatblade | Adds a piecewise amount based on a living target's maximum health; nonliving targets delegate to the base path. |
| Shroomic Greatblade | Multiplies the getter by 1.3 when the attacker has the checked Poison effect. |
| Shyre Sword | Uses getter −4 plus the light helper result divided by 15 and multiplied by 9. The light lookup is a separate helper. |
| Underworld Greatblade | Adds 5 to the incoming base argument for a living target with the UNDEAD creature attribute. |

### Lunar and Millennium: do not copy the tooltip minimum blindly

Their constructors keep a half-damage `baseDmg` field for the tooltip, but the selected attack method reads the **same-named parameter**, not that stored minimum field. The method computes `randomFloat × (maxDmg − incomingBase) + incomingBase`, then performs float conversion.

In the ordinary unmodified normal-mode example where the caller passes 25 for Lunar and the stored maximum is 37.5, the calculation starts from 25, not the tooltip field 12.5. Millennium's corresponding registration input is 26.5 and its constructor maximum is 39.75. These are expression examples, not measured hits. Configuration at construction and later getter values can differ, so test hardcore/config transitions explicitly.

### Primordial's piecewise extra term

For a living target with maximum health H, the selected additional term is:

- H ≤ 100: H / 50
- 100 < H ≤ 300: H / 100
- 300 < H ≤ 1000: H / 250
- H > 1000: min(H / 300, 5)

The boundaries are not monotonic: H=100 gives 2, while H=101 gives 1.01. Preserve and test the released formula instead of silently smoothing it or assuming every increase in target maximum health increases this term.

## Practical and restoration checklist

1. Keep the release and family fixed when comparing inputs. A material bonus and a direct damage field are different quantities.
2. Use the linked item portrait and exact same-release recipe/drop searches for acquisition; registration alone does not prove Survival availability.
3. Compare normal and AoA-hardcore settings, cooldown states, target defenses, attributes and enchantments independently.
4. Test the actual hit, effect, wear and synchronization path before claiming final damage, DPS, range or compatibility.
5. Retain each weapon's identity in optional animated remodels; do not replace these mechanics with generic firearm rules.

[Released registrations, material definitions, speed constants and selected behavior methods](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-melee-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/melee-art-evidence-1.12.2.json).
