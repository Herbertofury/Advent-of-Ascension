# Staff rune costs: prepare supplies before casting

[Battery attachment and charging](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Batteries-and-Charging) · [Rune production](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rune-Production-and-Current-Limits-1.21.1) · [Weapon repairs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1)

![Fourteen labelled source-model rune inputs used by released staff registrations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/staff-rune-preparation-1.21.1.webp)

**Scope:** 57 released staff registrations in Minecraft 1.21.1 / AoA 3.7.16.1. All rune IDs and counts are read from the released stat builders and joined through the released item factories. Fourteen rune types occur across these inputs. This is an undiscounted component reference, not a guarantee of final payment or spell damage.

## Plan a trip or a charging session

1. Open your staff below. Its card keeps the source-model preview and the matching release’s recipe/drop links.
2. Expand **Staff rune costs · plan your spell supplies**.
3. Choose 1, 10, 64 or 100 planned casts. The illustrated list multiplies each required rune count by that number; rune names link to their own item and recipe references.
4. Use those totals as a materials estimate. Stored charges, Creative mode, buffs and altered stack components can change the actual casting payment.
5. If using an Arcanum Battery, follow the separate attachment guide first. Attaching initializes stored casts at zero; it does not provide free spells.
6. Charge one operation at a time and inspect the result and returned ingredients. Each assembled charging result increments stored casts once. The planner is not a bulk-crafting action or a promise about shift-click behavior.

For example, Amber Staff’s released requirement is four Energy Runes and one Kinetic Rune per undiscounted cast. Planning ten yields 40 Energy Runes and ten Kinetic Runes. Keep different rune types separate and do not add unrelated ingredients to the charging recipe.

## How the base staff pays for a cast

The released base method checks Creative/infinite-material behavior first. A positive stored-cast count is decremented and returns success. Otherwise it delegates rune payment to the item utility, with the caller able to allow buffs. The staff’s preconditions are checked before the payment filter in its normal use path.

The charging recipe separately requires the stored-casts and staff-stat components, checks the allowed capacity, matches the required set of item types and requires sufficient counts. Extra unrelated types can reject the recipe even if enough of the correct runes are present. The displayed totals do not override those checks.

## Why some damage inputs are zero

Twenty-two of these registrations explicitly set the damage field. The other 35 retain the released builder default of zero. This does **not** mean those staves have no effect: their individual cast implementations may create utility, movement, environmental or other special behavior. A component number is not a complete spell description or a final hit-damage prediction.

## All 57 staff requirements

| Staff | Undiscounted rune inputs per cast | Damage input | Durability |
|---|---|---:|---:|
| [Amber Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aamber_staff) | 4 × Energy Rune + 1 × Kinetic Rune | 0 | 900 |
| [Aquatic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aaquatic_staff) | 1 × Kinetic Rune + 4 × Water Rune + 2 × Wind Rune | 20 | 1220 |
| [Atlantic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aatlantic_staff) | 1 × Distortion Rune + 2 × Energy Rune + 2 × Storm Rune | 0 | 1250 |
| [Baron Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_staff) | 3 × Power Rune + 2 × Wind Rune | 24 | 1200 |
| [Candy Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acandy_staff) | 3 × Kinetic Rune + 2 × Storm Rune | 0 | 950 |
| [Celestial Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acelestial_staff) | 1 × Compass Rune + 2 × Energy Rune + 2 × Lunar Rune | 22 | 1150 |
| [Concussion Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aconcussion_staff) | 4 × Power Rune + 4 × Storm Rune | 0 | 1150 |
| [Coral Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoral_staff) | 8 × Kinetic Rune + 2 × Water Rune | 0 | 950 |
| [Crystal Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystal_staff) | 2 × Distortion Rune + 5 × Life Rune | 0 | 1230 |
| [Crystik Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acrystik_staff) | 2 × Distortion Rune + 1 × Life Rune + 1 × Water Rune | 0 | 1140 |
| [Cryston Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acryston_staff) | 2 × Distortion Rune + 4 × Energy Rune | 0 | 1240 |
| [Destruction Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adestruction_staff) | 2 × Energy Rune + 2 × Power Rune | 0 | 1170 |
| [Ember Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aember_staff) | 1 × Fire Rune + 1 × Kinetic Rune + 1 × Wind Rune | 0 | 1400 |
| [Everfight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aeverfight_staff) | 4 × Kinetic Rune + 4 × Power Rune | 0 | 1050 |
| [Evermight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aevermight_staff) | 2 × Distortion Rune + 4 × Power Rune | 0 | 1050 |
| [Fire Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afire_staff) | 2 × Fire Rune + 2 × Wind Rune | 10 | 850 |
| [Firefly Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afirefly_staff) | 1 × Fire Rune + 2 × Strike Rune + 2 × Wind Rune | 22 | 1230 |
| [Firestorm Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afirestorm_staff) | 1 × Compass Rune + 2 × Fire Rune + 2 × Lunar Rune | 32 | 990 |
| [Fungal Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afungal_staff) | 5 × Distortion Rune + 2 × Life Rune | 0 | 1130 |
| [Ghoul Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aghoul_staff) | 1 × Distortion Rune + 2 × Life Rune + 2 × Wind Rune | 29 | 400 |
| [Haunter's Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahaunters_staff) | 4 × Energy Rune + 4 × Wind Rune | 26 | 1225 |
| [Hive Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahive_staff) | 10 × Energy Rune + 2 × Life Rune | 0 | 1130 |
| [Joker Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajoker_staff) | 4 × Kinetic Rune + 4 × Wind Rune | 0 | 300 |
| [Lightning Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alightning_staff) | 1 × Compass Rune + 4 × Storm Rune + 4 × Strike Rune | 0 | 1070 |
| [Lightshine](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alightshine) | 2 × Distortion Rune + 3 × Life Rune + 3 × Power Rune | 0 | 700 |
| [Lunar Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_staff) | 1 × Compass Rune + 2 × Lunar Rune | 32 | 1250 |
| [Lyonic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alyonic_staff) | 1 × Energy Rune + 1 × Strike Rune + 1 × Wind Rune + 2 × Wither Rune | 0 | 1100 |
| [Mecha Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_staff) | 1 × Distortion Rune + 1 × Power Rune + 2 × Wind Rune | 0 | 1110 |
| [Meteor Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ameteor_staff) | 1 × Compass Rune + 2 × Kinetic Rune + 2 × Lunar Rune | 28 | 1190 |
| [Moonlight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amoonlight_staff) | 1 × Compass Rune + 2 × Kinetic Rune + 2 × Lunar Rune | 0 | 1130 |
| [Nature Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anature_staff) | 2 × Energy Rune + 4 × Life Rune | 0 | 1450 |
| [Nightmare Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anightmare_staff) | 1 × Compass Rune + 2 × Lunar Rune + 2 × Poison Rune | 28 | 1200 |
| [Noxious Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anoxious_staff) | 2 × Poison Rune + 2 × Storm Rune + 2 × Wind Rune | 7 | 1210 |
| [Phantom Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aphantom_staff) | 2 × Distortion Rune + 2 × Wind Rune | 24 | 1060 |
| [Poison Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apoison_staff) | 2 × Poison Rune + 2 × Wind Rune | 10 | 850 |
| [Power Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apower_staff) | 2 × Power Rune + 2 × Wind Rune | 16 | 1010 |
| [Primordial Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aprimordial_staff) | 2 × Wind Rune + 2 × Wither Rune | 30 | 1230 |
| [Reef Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Areef_staff) | 2 × Energy Rune + 1 × Water Rune | 0 | 1230 |
| [Rejuvenation Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arejuvenation_staff) | 2 × Energy Rune + 4 × Life Rune | 0 | 870 |
| [Rosidian Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_staff) | 1 × Life Rune + 2 × Water Rune + 3 × Wind Rune | 21 | 1180 |
| [Runic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arunic_staff) | 5 × Distortion Rune | 0 | 1000 |
| [Shadowlord Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashadowlord_staff) | 2 × Life Rune + 10 × Wither Rune | 0 | 1200 |
| [Show Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashow_staff) | 3 × Compass Rune + 3 × Power Rune | 0 | 900 |
| [Shyre Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashyre_staff) | 3 × Distortion Rune + 3 × Energy Rune | 0 | 1380 |
| [Sky Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asky_staff) | 1 × Energy Rune + 2 × Kinetic Rune + 2 × Wind Rune | 0 | 1480 |
| [Striker Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Astriker_staff) | 2 × Strike Rune | 0 | 850 |
| [Sun Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asun_staff) | 2 × Fire Rune + 3 × Lunar Rune + 1 × Storm Rune | 0 | 960 |
| [Surge Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asurge_staff) | 1 × Energy Rune + 4 × Power Rune | 0 | 1270 |
| [Tangle Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atangle_staff) | 2 × Poison Rune + 1 × Storm Rune + 2 × Wind Rune | 18 | 1140 |
| [Ultimatum Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aultimatum_staff) | 8 × Distortion Rune + 5 × Life Rune + 3 × Power Rune | 0 | 750 |
| [Underworld Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aunderworld_staff) | 1 × Compass Rune + 3 × Kinetic Rune | 10 | 1140 |
| [Warlock Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awarlock_staff) | 2 × Kinetic Rune + 3 × Power Rune | 0 | 1050 |
| [Water Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awater_staff) | 2 × Water Rune + 2 × Wind Rune | 10 | 850 |
| [Web Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aweb_staff) | 4 × Distortion Rune + 4 × Energy Rune | 0 | 1420 |
| [Wind Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awind_staff) | 3 × Wind Rune | 10 | 850 |
| [Wither Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awither_staff) | 2 × Wind Rune + 2 × Wither Rune | 10 | 850 |
| [Wizard's Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awizards_staff) | 3 × Distortion Rune + 3 × Life Rune + 3 × Power Rune | 0 | 800 |

## Checks before trusting a valuable loadout

- Test a successful cast and a failed precondition; check whether resources changed in each case.
- Compare an unmodified staff, a battery with positive charges, a battery at zero and a staff with a configured maximum.
- Check ordinary charging, repeated crafting and returned excess runes in the actual modpack. Documentation tests do not certify inventory behavior in-game.
- Check special staff subclasses, payment buffs, modified data components and client/server synchronization separately.
- A missing acquisition recipe is not filled with an invented crafting route. Follow the item browser’s exact-version evidence.

[Released staff builder, registration and behavior evidence](https://herbertofury.github.io/Advent-of-Ascension/staff-statistics-evidence-1.21.1.json) · [Rune illustration provenance](https://herbertofury.github.io/Advent-of-Ascension/staff-rune-art-evidence-1.21.1.json).

Exact archive: `AoA3-1.21.1-3.7.16.1.jar`. The evidence records class hashes and instruction bytes. No Java game classes were executed. Models, textures and mechanics are credited to Tslat and contributors; the reference layout and static renders are independent documentation work.
