# Modern Skill Unlocks

[Skills and progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

## What this page proves

This is a complete table of the default ability records in the ten skill data files at the pinned **1.21 source snapshot**. All ten files have now been compared with **AoA 3.7.16.1 for Minecraft 1.21.1** and match semantically, covering **201 records**. This is not a promise that every system is finished in every release. Add-ons/data packs and server configuration may change these values. Ability parameters are reported as stored; cumulative effects, resource affordability and conditional activation depend on their implementation.

[Pinned upstream source](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills). AoA is created by Tslat and contributors.

## Reading the milestones

- A level restriction grants permission for the listed action; it does not spawn the item or supply a recipe ingredient.
- `base_value` and `per_level_mod` are ability parameters, not a guarantee of a final effective bonus or probability.
- Attribute operation numbers are stored implementation data; do not add percentages together without following the ability/attribute logic.
- Empty default ability lists are reported directly. They do not by themselves prove that no XP hooks, future work or other behavior exists.

## Source-level progression behavior

The inspected AoASkill implementation begins at level 1 with zero XP and cycle 0. Its ordinary level accessor caps the visible/effective level at 100, while the alternate accessor exposes the underlying level. The setter bounds stored levels to 0–1000; the positive-XP path stops at 1000. Configured global and skill XP multipliers are applied, Nowhere applies a 0.5 multiplier, and positive cycles apply a factor of three times the cycle count. Cycling is gated on at least level 100 and fewer than ten cycles. These statements describe the pinned source and must be reconciled with the actual deployed artifact.

## Default ability records

### Alchemy

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/alchemy.json) · XP modifier: **1.0** · Default ability records: **0**

The default ability list is empty in this snapshot. For Alchemy, Artifice and Creation, the inspected Java skill classes are also thin constructor wrappers. Faunamancy has event-driven XP logic despite its empty ability list. Do not mark these four systems equally complete merely because all four have registrations.

### Artifice

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/artifice.json) · XP modifier: **1.0** · Default ability records: **0**

The default ability list is empty in this snapshot. For Alchemy, Artifice and Creation, the inspected Java skill classes are also thin constructor wrappers. Faunamancy has event-driven XP logic despite its empty ability list. Do not mark these four systems equally complete merely because all four have registrations.

### Creation

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/creation.json) · XP modifier: **1.0** · Default ability records: **0**

The default ability list is empty in this snapshot. For Alchemy, Artifice and Creation, the inspected Java skill classes are also thin constructor wrappers. Faunamancy has event-driven XP logic despite its empty ability list. Do not mark these four systems equally complete merely because all four have registrations.

### Dexterity

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/dexterity.json) · XP modifier: **1.0** · Default ability records: **10**

| Level | Ability | Stored parameters |
|---:|---|---|
| 5 | attribute modification | `attribute=minecraft:generic.movement_speed`; `base_value=0.0`; `operation=1`; `per_level_mod=0.002` |
| 15 | fall damage reduction | `base_value=0.0`; `max_height=10`; `min_height=0`; `per_level_mod=0.0085` |
| 25 | jump boost | `base_value=0.25`; `per_level_mod=0.004` |
| 40 | attribute modification | `attribute=minecraft:generic.movement_speed`; `base_value=0.05`; `operation=1`; `per_level_mod=0.0` |
| 50 | attribute modification | `attribute=neoforge:swim_speed`; `base_value=0.0`; `operation=1`; `per_level_mod=0.003` |
| 60 | fall damage reduction | `base_value=0.0`; `max_height=2147483647`; `min_height=11`; `per_level_mod=0.005` |
| 70 | jump boost | `amplify_lateral_velocity=True`; `base_value=0.25`; `per_level_mod=0.0` |
| 80 | attribute modification | `attribute=minecraft:generic.movement_speed`; `base_value=0.05`; `operation=1`; `per_level_mod=0.0` |
| 90 | double jump | `energy_consumption=20.0` |
| 100 | level restriction | `restricted_id=aoa3:helm_of_the_dextrous`; `restrictions=["equip"]` |

### Extraction

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/extraction.json) · XP modifier: **1.0** · Default ability records: **14**

| Level | Ability | Stored parameters |
|---:|---|---|
| 6 | bonus mining result | `base_value=0.4`; `per_level_mod=0.0` |
| 10 | hard block speed increase | `base_value=0.0`; `per_level_mod=0.02` |
| 16 | bonus smelt result | `base_value=0.5`; `per_level_mod=0.0` |
| 25 | harvest speed boost | `cost_reduction_per_level=0.0135`; `energy_drain_per_tick=1.7`; `speed_boost=2.5` |
| 32 | bonus mining result | `base_value=0.4`; `per_level_mod=0.0` |
| 39 | bonus crafting output | `base_value=0.5`; `per_level_mod=0.0`; `tag=minecraft:planks` |
| 48 | bonus smelt result | `base_value=0.5`; `per_level_mod=0.0` |
| 55 | auto enchant crafting | `enchantments={"minecraft:fortune":3,"minecraft:unbreaking":3}` |
| 62 | bonus crafting output | `base_value=0.5`; `item=minecraft:torch`; `per_level_mod=0.0` |
| 74 | auto harvesting trash | No additional parameters in this record |
| 82 | bonus smelt result | `base_value=0.5`; `per_level_mod=0.0` |
| 89 | bonus mining result | `base_value=0.4`; `per_level_mod=0.0` |
| 96 | rare table harvesting chance | `base_value=0.001`; `per_level_mod=0.0` |
| 100 | level restriction | `restricted_id=aoa3:helm_of_the_treasurer`; `restrictions=["equip"]` |

### Farming

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/farming.json) · XP modifier: **1.0** · Default ability records: **14**

| Level | Ability | Stored parameters |
|---:|---|---|
| 8 | fertilise farmland | No additional parameters in this record |
| 16 | block conversion | `interaction_item=minecraft:wheat_seeds`; `radius=1`; `replacement_block=minecraft:mossy_cobblestone`; `target_block=minecraft:cobblestone` |
| 24 | level restriction | `restricted_id=aoa3:green_manure`; `restrictions=["interact_with","place_block"]` |
| 29 | level restriction | `restricted_id=aoa3:magic_marang_crop`; `restrictions=["place_block"]` |
| 35 | breeding bonus | `base_value=0.1`; `per_level_mod=0.002` |
| 44 | dryad sprite spawn | `base_value=0.00075`; `per_level_mod=8e-05` |
| 49 | harvest replant | `base_value=0.1`; `per_level_mod=0.003` |
| 57 | hoe area harvest | `base_radius=1`; `levels_per_radius_increase=20`; `per_block_hoe_damage=1` |
| 60 | block conversion | `interaction_item=aoa3:mushroom_spores`; `radius=4`; `replacement_block=minecraft:mycelium`; `target_block=minecraft:grass_block` |
| 66 | no trampling | No additional parameters in this record |
| 74 | level restriction | `restricted_id=aoa3:trilliad_crop`; `restrictions=["place_block"]` |
| 86 | level restriction | `restricted_id=aoa3:thorny_plant_crop`; `restrictions=["place_block"]` |
| 92 | level restriction | `restricted_id=aoa3:dryads_blessing`; `restrictions=["equip"]` |
| 100 | level restriction | `restricted_id=aoa3:helm_of_the_dryad`; `restrictions=["equip"]` |

### Faunamancy

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/faunamancy.json) · XP modifier: **1.0** · Default ability records: **0**

The default ability list is empty in this snapshot. For Alchemy, Artifice and Creation, the inspected Java skill classes are also thin constructor wrappers. Faunamancy has event-driven XP logic despite its empty ability list. Do not mark these four systems equally complete merely because all four have registrations.

### Hauling

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/hauling.json) · XP modifier: **1.0** · Default ability records: **11**

| Level | Ability | Stored parameters |
|---:|---|---|
| 8 | fishing xp boost | `base_value=1.0`; `per_level_mod=0.0` |
| 15 | level restriction | `restricted_id=aoa3:hauling_rod`; `restrictions=["equip"]` |
| 25 | fishing trap spawn | `base_value=0.05875`; `per_level_mod=-0.00035` |
| 31 | level restriction | `restricted_id=aoa3:fishing_cage`; `restrictions=["equip"]` |
| 45 | hauling rod pull strength | `base_value=0.0`; `per_level_mod=0.0025` |
| 54 | level restriction | `restricted_id=aoa3:thermally_insulated_rod`; `restrictions=["equip"]` |
| 60 | hauling glowing fish | No additional parameters in this record |
| 69 | level restriction | `restricted_id=aoa3:light_rod`; `restrictions=["equip"]` |
| 77 | hauling rod pull damage | `base_value=3.0`; `per_level_mod=0.0` |
| 86 | hauling resupply | `base_value=0.075`; `per_level_mod=0.0` |
| 100 | level restriction | `restricted_id=aoa3:helm_of_the_trawler`; `restrictions=["equip"]` |

### Imbuing

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/imbuing.json) · XP modifier: **1.0** · Default ability records: **139**

| Level | Ability | Stored parameters |
|---:|---|---|
| 1 | imbuing level restriction | `recipe_id=aoa3:imbuing_bane_of_arthropods` |
| 1 | imbuing level restriction | `recipe_id=aoa3:imbuing_luck_of_the_sea` |
| 2 | imbuing level restriction | `recipe_id=aoa3:imbuing_lure` |
| 3 | imbuing level restriction | `recipe_id=aoa3:imbuing_blast_protection` |
| 5 | imbuing level restriction | `recipe_id=aoa3:imbuing_efficiency` |
| 7 | imbuing level restriction | `recipe_id=aoa3:imbuing_knockback` |
| 8 | imbuing level restriction | `recipe_id=aoa3:imbuing_protection` |
| 9 | imbuing level restriction | `recipe_id=aoa3:imbuing_sharpness` |
| 10 | imbuing level restriction | `recipe_id=aoa3:imbuing_impaling` |
| 10 | imbuing level restriction | `recipe_id=aoa3:imbuing_luck_of_the_sea_ii` |
| 10 | imbuing level restriction | `recipe_id=aoa3:imbuing_riptide` |
| 10 | imbuing level restriction | `recipe_id=aoa3:imbuing_sweeping_edge` |
| 12 | imbuing level restriction | `recipe_id=aoa3:imbuing_bane_of_arthropods_ii` |
| 12 | imbuing level restriction | `recipe_id=aoa3:imbuing_form` |
| 13 | imbuing level restriction | `recipe_id=aoa3:imbuing_fortune` |
| 13 | imbuing level restriction | `recipe_id=aoa3:imbuing_projectile_protection` |
| 14 | imbuing level restriction | `recipe_id=aoa3:imbuing_blast_protection_ii` |
| 14 | imbuing level restriction | `recipe_id=aoa3:imbuing_respiration` |
| 14 | imbuing level restriction | `recipe_id=aoa3:imbuing_smite` |
| 15 | imbuing level restriction | `recipe_id=aoa3:imbuing_depth_strider` |
| 15 | imbuing level restriction | `recipe_id=aoa3:imbuing_fire_protection` |
| 15 | imbuing level restriction | `recipe_id=aoa3:imbuing_lure_ii` |
| 16 | imbuing level restriction | `recipe_id=aoa3:imbuing_knockback_ii` |
| 16 | imbuing level restriction | `recipe_id=aoa3:imbuing_shell` |
| 17 | imbuing level restriction | `recipe_id=aoa3:imbuing_fire_aspect` |
| 17 | imbuing level restriction | `recipe_id=aoa3:imbuing_protection_ii` |
| 18 | imbuing level restriction | `recipe_id=aoa3:imbuing_feather_falling` |
| 18 | imbuing level restriction | `recipe_id=aoa3:imbuing_looting` |
| 18 | imbuing level restriction | `recipe_id=aoa3:imbuing_sharpness_ii` |
| 19 | imbuing level restriction | `recipe_id=aoa3:imbuing_efficiency_ii` |
| 19 | imbuing level restriction | `recipe_id=aoa3:imbuing_sever` |
| 20 | imbuing level restriction | `recipe_id=aoa3:imbuing_riptide_ii` |
| 20 | imbuing level restriction | `recipe_id=aoa3:imbuing_soul_speed` |
| 21 | imbuing level restriction | `recipe_id=aoa3:imbuing_form_ii` |
| 21 | imbuing level restriction | `recipe_id=aoa3:imbuing_quick_charge` |
| 21 | imbuing level restriction | `recipe_id=aoa3:imbuing_smite_ii` |
| 22 | imbuing level restriction | `recipe_id=aoa3:imbuing_control` |
| 22 | imbuing level restriction | `recipe_id=aoa3:imbuing_respiration_ii` |
| 22 | imbuing level restriction | `recipe_id=aoa3:imbuing_sweeping_edge_ii` |
| 23 | imbuing level restriction | `recipe_id=aoa3:imbuing_loyalty` |
| 24 | imbuing level restriction | `recipe_id=aoa3:imbuing_fire_protection_ii` |
| 24 | imbuing level restriction | `recipe_id=aoa3:imbuing_impaling_ii` |
| 24 | imbuing level restriction | `recipe_id=aoa3:imbuing_luck_of_the_sea_iii` |
| 24 | imbuing level restriction | `recipe_id=aoa3:imbuing_recharge` |
| 25 | imbuing level restriction | `recipe_id=aoa3:imbuing_bane_of_arthropods_iii` |
| 25 | imbuing level restriction | `recipe_id=aoa3:imbuing_flame` |
| 25 | imbuing level restriction | `recipe_id=aoa3:imbuing_lure_iii` |
| 25 | imbuing level restriction | `recipe_id=aoa3:imbuing_power` |
| 25 | imbuing level restriction | `recipe_id=aoa3:imbuing_punch` |
| 25 | imbuing level restriction | `recipe_id=aoa3:imbuing_sharpness_iii` |
| 26 | grindstone curses removal | No additional parameters in this record |
| 26 | imbuing level restriction | `recipe_id=aoa3:imbuing_blast_protection_iii` |
| 26 | imbuing level restriction | `recipe_id=aoa3:imbuing_fire_aspect_ii` |
| 26 | imbuing level restriction | `recipe_id=aoa3:imbuing_piercing` |
| 26 | imbuing level restriction | `recipe_id=aoa3:imbuing_shell_ii` |
| 27 | imbuing level restriction | `recipe_id=aoa3:imbuing_depth_strider_ii` |
| 27 | imbuing level restriction | `recipe_id=aoa3:imbuing_feather_falling_ii` |
| 27 | imbuing level restriction | `recipe_id=aoa3:imbuing_projectile_protection_ii` |
| 27 | imbuing level restriction | `recipe_id=aoa3:imbuing_sever_ii` |
| 28 | imbuing level restriction | `recipe_id=aoa3:imbuing_efficiency_iii` |
| 29 | imbuing level restriction | `recipe_id=aoa3:imbuing_archmage` |
| 29 | imbuing level restriction | `recipe_id=aoa3:imbuing_fortune_ii` |
| 30 | imbuing level restriction | `recipe_id=aoa3:imbuing_looting_ii` |
| 30 | imbuing level restriction | `recipe_id=aoa3:imbuing_soul_speed_ii` |
| 30 | imbuing level restriction | `recipe_id=aoa3:imbuing_unbreaking` |
| 31 | imbuing level restriction | `recipe_id=aoa3:imbuing_channeling` |
| 31 | imbuing level restriction | `recipe_id=aoa3:imbuing_loyalty_ii` |
| 31 | imbuing level restriction | `recipe_id=aoa3:imbuing_protection_iii` |
| 32 | imbuing level restriction | `recipe_id=aoa3:imbuing_sweeping_edge_iii` |
| 33 | imbuing level restriction | `recipe_id=aoa3:imbuing_aqua_affinity` |
| 33 | imbuing level restriction | `recipe_id=aoa3:imbuing_fire_protection_iii` |
| 33 | imbuing level restriction | `recipe_id=aoa3:imbuing_quick_charge_ii` |
| 34 | imbuing level restriction | `recipe_id=aoa3:imbuing_bane_of_arthropods_iv` |
| 34 | imbuing level restriction | `recipe_id=aoa3:imbuing_piercing_ii` |
| 35 | imbuing level restriction | `recipe_id=aoa3:imbuing_blast_protection_iv` |
| 35 | imbuing level restriction | `recipe_id=aoa3:imbuing_feather_falling_iii` |
| 35 | imbuing level restriction | `recipe_id=aoa3:imbuing_impaling_iii` |
| 35 | imbuing level restriction | `recipe_id=aoa3:imbuing_respiration_iii` |
| 35 | imbuing level restriction | `recipe_id=aoa3:imbuing_swift_sneak` |
| 36 | imbuing level restriction | `recipe_id=aoa3:imbuing_control_ii` |
| 36 | imbuing level restriction | `recipe_id=aoa3:imbuing_punch_ii` |
| 36 | imbuing level restriction | `recipe_id=aoa3:imbuing_thorns` |
| 37 | imbuing level restriction | `recipe_id=aoa3:imbuing_depth_strider_iii` |
| 37 | imbuing level restriction | `recipe_id=aoa3:imbuing_power_ii` |
| 37 | imbuing level restriction | `recipe_id=aoa3:imbuing_riptide_iii` |
| 37 | imbuing level restriction | `recipe_id=aoa3:imbuing_smite_iii` |
| 38 | imbuing level restriction | `recipe_id=aoa3:imbuing_form_iii` |
| 38 | imbuing level restriction | `recipe_id=aoa3:imbuing_projectile_protection_iii` |
| 39 | imbuing level restriction | `recipe_id=aoa3:imbuing_archmage_ii` |
| 39 | imbuing level restriction | `recipe_id=aoa3:imbuing_frost_walker` |
| 39 | imbuing level restriction | `recipe_id=aoa3:imbuing_recharge_ii` |
| 40 | imbuing level restriction | `recipe_id=aoa3:imbuing_bane_of_arthropods_v` |
| 40 | imbuing level restriction | `recipe_id=aoa3:imbuing_efficiency_iv` |
| 40 | imbuing level restriction | `recipe_id=aoa3:imbuing_protection_iv` |
| 40 | imbuing level restriction | `recipe_id=aoa3:imbuing_soul_speed_iii` |
| 41 | imbuing level restriction | `recipe_id=aoa3:imbuing_unbreaking_ii` |
| 42 | imbuing level restriction | `recipe_id=aoa3:imbuing_shell_iii` |
| 42 | imbuing level restriction | `recipe_id=aoa3:imbuing_swift_sneak_ii` |
| 43 | imbuing level restriction | `recipe_id=aoa3:imbuing_fortune_iii` |
| 43 | imbuing level restriction | `recipe_id=aoa3:imbuing_loyalty_iii` |
| 44 | imbuing level restriction | `recipe_id=aoa3:imbuing_looting_iii` |
| 44 | imbuing level restriction | `recipe_id=aoa3:imbuing_smite_iv` |
| 45 | imbuing level restriction | `recipe_id=aoa3:imbuing_multishot` |
| 45 | imbuing level restriction | `recipe_id=aoa3:imbuing_sharpness_iv` |
| 45 | imbuing level restriction | `recipe_id=aoa3:imbuing_thorns_ii` |
| 46 | imbuing level restriction | `recipe_id=aoa3:imbuing_sever_iii` |
| 47 | imbuing level restriction | `recipe_id=aoa3:imbuing_feather_falling_iv` |
| 48 | imbuing level restriction | `recipe_id=aoa3:imbuing_quick_charge_iii` |
| 49 | imbuing level restriction | `recipe_id=aoa3:imbuing_control_iii` |
| 49 | imbuing level restriction | `recipe_id=aoa3:imbuing_fire_protection_iv` |
| 50 | imbuing level restriction | `recipe_id=aoa3:imbuing_swift_sneak_iii` |
| 51 | imbuing level restriction | `recipe_id=aoa3:imbuing_piercing_iii` |
| 51 | imbuing level restriction | `recipe_id=aoa3:imbuing_projectile_protection_iv` |
| 52 | imbuing level restriction | `recipe_id=aoa3:imbuing_impaling_iv` |
| 54 | imbuing level restriction | `recipe_id=aoa3:imbuing_power_iii` |
| 55 | imbuing level restriction | `recipe_id=aoa3:imbuing_efficiency_v` |
| 56 | imbuing level restriction | `recipe_id=aoa3:imbuing_frost_walker_ii` |
| 56 | imbuing level restriction | `recipe_id=aoa3:imbuing_recharge_iii` |
| 57 | imbuing level restriction | `recipe_id=aoa3:imbuing_archmage_iii` |
| 57 | imbuing level restriction | `recipe_id=aoa3:imbuing_sharpness_v` |
| 58 | imbuing level restriction | `recipe_id=aoa3:imbuing_thorns_iii` |
| 59 | imbuing level restriction | `recipe_id=aoa3:imbuing_intervention` |
| 59 | imbuing level restriction | `recipe_id=aoa3:imbuing_unbreaking_iii` |
| 60 | imbuing level restriction | `recipe_id=aoa3:imbuing_silk_touch` |
| 62 | imbuing level restriction | `recipe_id=aoa3:imbuing_infinity` |
| 62 | imbuing level restriction | `recipe_id=aoa3:imbuing_sever_iv` |
| 62 | imbuing level restriction | `recipe_id=aoa3:imbuing_smite_v` |
| 66 | imbuing level restriction | `recipe_id=aoa3:imbuing_impaling_v` |
| 68 | imbuing level restriction | `recipe_id=aoa3:imbuing_brace` |
| 69 | imbuing level restriction | `recipe_id=aoa3:imbuing_piercing_iv` |
| 70 | imbuing level restriction | `recipe_id=aoa3:imbuing_power_iv` |
| 70 | imbuing level restriction | `recipe_id=aoa3:imbuing_sever_v` |
| 73 | imbuing level restriction | `recipe_id=aoa3:imbuing_recharge_iv` |
| 74 | enchant entity equipment | No additional parameters in this record |
| 82 | imbuing level restriction | `recipe_id=aoa3:imbuing_power_v` |
| 85 | imbuing level restriction | `recipe_id=aoa3:imbuing_recharge_v` |
| 92 | enchant container contents | No additional parameters in this record |
| 97 | imbuing level restriction | `recipe_id=aoa3:imbuing_mending` |
| 100 | level restriction | `restricted_id=aoa3:helm_of_the_ritualist`; `restrictions=["equip"]` |

### Innervation

[Source data](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/data/aoa3/player/skills/innervation.json) · XP modifier: **1.0** · Default ability records: **13**

| Level | Ability | Stored parameters |
|---:|---|---|
| 1 | attribute modification | `attribute=minecraft:generic.max_health`; `base_value=0.0`; `operation=0`; `per_level_mod=0.3` |
| 10 | one shot damage limiter | `health_restore_amount=1.0`; `min_activation_health=0.0` |
| 19 | potion duration reducer | `match_effects=["minecraft:slowness","minecraft:mining_fatigue","minecraft:weakness","minecraft:blindness","minecraft:nausea"]`; `modifier=0.5` |
| 25 | attribute modification | `attribute=minecraft:generic.max_health`; `base_value=10.0`; `operation=0`; `per_level_mod=0.0` |
| 36 | bow damage increase | `modifier=1.2`; `require_full_charge=True` |
| 44 | innervation mob lure | `lured_damage_modifier=0.25`; `on_hit_drain=30.0`; `per_tick_spirit_drain=0.4` |
| 50 | attribute modification | `attribute=minecraft:generic.max_health`; `base_value=10.0`; `operation=0`; `per_level_mod=0.0` |
| 59 | innervation dodge | `energy_cost=30.0` |
| 65 | vulcane damage increase | `min_rage=0.0`; `modifier=1.5` |
| 77 | double drops chance | `base_value=0.1`; `per_level_mod=0.00147` |
| 85 | attribute modification | `attribute=minecraft:generic.max_health`; `base_value=10.0`; `operation=0`; `per_level_mod=0.0` |
| 91 | stun strike | `energy_cost=30.0`; `stun_duration=40` |
| 100 | level restriction | `restricted_id=aoa3:helm_of_the_warrior`; `restrictions=["equip"]` |

## Why Imbuing needs a data-aware audit

The Java Imbuing skill wrapper is small, but the default data contains recipe-level restrictions. Reviewing only the class body would miss those gates. The table above preserves each recipe ID and level so a conversion can test recipes individually.

## Acceptance tests for Enderloom

1. Load every skill and ability type with its data serializer; fail on missing IDs instead of silently dropping records.
2. Test immediately below, at and above each listed unlock level.
3. Verify the exact intended action (equip, place, interact, recipe) and preserve the server-side authority.
4. Check XP events, multipliers, cycling and persistence across disconnect, reload and version migration.
5. Test stacking and resource costs with other mods and configuration overrides.
6. Do not award completion from registration counts or UI icons alone.

Total default ability records documented: **201**.

## Practical training guide and released-data check

[How to train each supported skill, common blockers, full-stack Energy Stone consumption and cycling cautions](Skill-Training-Walkthrough-1.21.1). [Released data comparison with hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/modern-skill-artifact-comparison.json).
