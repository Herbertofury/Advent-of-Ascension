# Mining and Ore Generation · 1.21.1

**Release:** AoA 3.7.16.1. This guide reads the released resources, with source-backed biome-selector interpretation. It is not a measured mining-speed study or proof that every retained dimension is reachable in a particular pack.

![Twelve released ore block models](https://herbertofury.github.io/Advent-of-Ascension/previews/mining-ore-overview-1.21.1.webp)

The overview uses released static block models, including their coplanar ore overlays. The documentation renderer composites matching binary-alpha layers in model order; runtime lighting and shader parity remain outside this reference.

## Start here

1. **Choose the correct release.** Old AoA ore-height charts are not interchangeable with these 1.21.1 resources.
2. **Match the biome selector before choosing a height.** Large Jade features require Overworld-tagged beach/river biomes; large Runium requires an Overworld-tagged magical biome. A familiar-looking landscape is not proof of tag membership.
3. **Bring the right tool.** Limonite is directly tagged as needing a stone tool; Jade and Runium variants need iron; Emberstone needs diamond. These are released tag memberships, not a guarantee for every custom tool implementation.
4. **Check both the block and its recipe uses.** Use the linked inventory and recipe searches below. The mined resource may differ from the ore block, and Silk Touch, Fortune, explosion conditions and custom loot functions can change the result.
5. **Treat placement attempts as attempts.** Count values and the configured size parameter do not guarantee veins or ore blocks per chunk. Host blocks, height bounds, air exposure and later modifiers matter.

## Practical routes

- **Limonite:** the small feature uses Y 0 through top − 10 in Overworld-tagged biomes. The larger feature requires underground-tagged Overworld biomes plus lush/wet tags or Dripstone Caves.
- **Jade:** the large feature is aimed at beach/river-tagged Overworld biomes. The smaller feature excludes those tags and spans Y −40 through Y 10.
- **Runium:** the large Overworld feature selects magical-tagged biomes. The smaller one excludes dead-tagged biomes. Nether Runium selects Nether-tagged biomes that are magical-tagged or Warped Forest.
- **Emberstone:** the Nether-tagged feature samples bottom + 3 through bottom + 32. Keep that relative notation when using custom dimension heights.
- **Precasia:** Bone Fragments have normal and shallow placements. The shallow one is explicitly listed in Precasian Deadlands and Tar Pits. Precasian Quartz is explicitly listed only in Precasian Volcano in this resource scan.
- **Barathos resources:** Baronyte, Blazium and Varsium have explicit biome and dimension JSON references. This documents those resources; it does not certify current survival entry, complete dimension gameplay or local Enderloom implementation.

## Read the chart correctly

- `if_all`: every listed biome/tag condition must match. `if_any`: at least one must match when present. `excluding`: any match rejects the biome. These are biome selectors, not strict dimension identity checks.
- **bottom/top** remain relative height anchors. No assumed conversion to absolute Y is applied. Some configured ranges may extend beyond buildable terrain and are not promises of reachable ore.
- **uniform/trapezoid** describe the height provider. An omitted plateau remains the provider default, not a measured best mining layer.
- **size** is the configured feature parameter, not guaranteed vein size. `scattered_ore` is identified separately.
- These **33 feature records** include ordinary stone, gravel and tuff geology. They are not 33 unique minerals. All 33 have explicit resource bindings in the inspected artifact.

## Complete placed-feature chart

| Feature | Height provider | Count / rarity filter | Size | Type |
|---|---|---|---|---|
| [baronyte_ore](#baronyte-ore) | trapezoid: Y 80 → Y 90 | uniform 1–3 attempts | 6 | minecraft:ore |
| [blazium_ore](#blazium-ore) | uniform: bottom +0 → bottom +30 | uniform 1–3 attempts | 3 | minecraft:scattered_ore |
| [bone_fragments_ore](#bone-fragments-ore) | uniform: bottom +12 → Y 35 | 5 attempts | 12 | minecraft:ore |
| [gravel_ore](#gravel-ore) | uniform: bottom +0 → top − 0 | 14 attempts | 33 | minecraft:ore |
| [high_altitude_andesite_ore](#high-altitude-andesite-ore) | uniform: Y 64 → Y 128 | rarity chance parameter 6 | 64 | minecraft:ore |
| [high_altitude_diorite_ore](#high-altitude-diorite-ore) | uniform: Y 64 → Y 128 | rarity chance parameter 6 | 64 | minecraft:ore |
| [high_altitude_granite_ore](#high-altitude-granite-ore) | uniform: Y 64 → Y 128 | rarity chance parameter 6 | 64 | minecraft:ore |
| [low_altitude_andesite_ore](#low-altitude-andesite-ore) | uniform: Y 0 → Y 60 | 2 attempts | 64 | minecraft:ore |
| [low_altitude_diorite_ore](#low-altitude-diorite-ore) | uniform: Y 0 → Y 60 | 2 attempts | 64 | minecraft:ore |
| [low_altitude_granite_ore](#low-altitude-granite-ore) | uniform: Y 0 → Y 60 | 2 attempts | 64 | minecraft:ore |
| [ore_emberstone](#ore-emberstone) | uniform: bottom +3 → bottom +32 | uniform 1–4 attempts | 5 | minecraft:ore |
| [ore_jade_large](#ore-jade-large) | trapezoid: bottom +5 → Y 0; plateau 5 | uniform 4–8 attempts | 12 | minecraft:ore |
| [ore_jade_small](#ore-jade-small) | trapezoid: Y -40 → Y 10; plateau 5 | uniform 0–3 attempts | 5 | minecraft:ore |
| [ore_limonite_large](#ore-limonite-large) | uniform: bottom +10 → Y 50 | uniform 5–10 attempts | 14 | minecraft:ore |
| [ore_limonite_small](#ore-limonite-small) | uniform: Y 0 → top − 10 | uniform 30–60 attempts | 8 | minecraft:ore |
| [ore_nether_runium](#ore-nether-runium) | uniform: bottom +5 → bottom +125 | uniform 5–10 attempts | 6 | minecraft:ore |
| [ore_runium_large](#ore-runium-large) | uniform: bottom +5 → Y 45 | uniform 1–4 attempts | 7 | minecraft:ore |
| [ore_runium_small](#ore-runium-small) | uniform: bottom +5 → Y 30 | uniform 0–2 attempts | 4 | minecraft:ore |
| [precasian_buried_lapis_ore](#precasian-buried-lapis-ore) | uniform: bottom +0 → Y 64 | 4 attempts | 7 | minecraft:ore |
| [precasian_copper_ore](#precasian-copper-ore) | trapezoid: Y -16 → Y 112 | 16 attempts | 10 | minecraft:ore |
| [precasian_gold_ore](#precasian-gold-ore) | trapezoid: Y -64 → Y 32 | 4 attempts | 9 | minecraft:ore |
| [precasian_high_altitude_iron_ore](#precasian-high-altitude-iron-ore) | uniform: Y 80 → Y 384 | 90 attempts | 9 | minecraft:ore |
| [precasian_iron_ore](#precasian-iron-ore) | uniform: Y -24 → Y 56 | 10 attempts | 9 | minecraft:ore |
| [precasian_lapis_ore](#precasian-lapis-ore) | trapezoid: Y -32 → Y 32 | 2 attempts | 7 | minecraft:ore |
| [precasian_low_altitude_gold_ore](#precasian-low-altitude-gold-ore) | uniform: Y -64 → Y -48 | uniform 0–1 attempts | 9 | minecraft:ore |
| [precasian_low_altitude_iron_ore](#precasian-low-altitude-iron-ore) | uniform: bottom +0 → Y 72 | 10 attempts | 9 | minecraft:ore |
| [precasian_low_altitude_redstone_ore](#precasian-low-altitude-redstone-ore) | trapezoid: bottom -32 → bottom +32 | uniform 0–1 attempts | 8 | minecraft:ore |
| [precasian_quartz_ore](#precasian-quartz-ore) | trapezoid: Y 10 → Y 150 | uniform 8–12 attempts | 14 | minecraft:ore |
| [precasian_redstone_ore](#precasian-redstone-ore) | uniform: bottom +0 → Y 15 | 4 attempts | 8 | minecraft:ore |
| [precasian_small_iron_ore](#precasian-small-iron-ore) | uniform: Y -24 → Y 56 | 10 attempts | 4 | minecraft:ore |
| [shallow_bone_fragments_ore](#shallow-bone-fragments-ore) | trapezoid: bottom +80 → Y 55 | uniform 2–4 attempts | 12 | minecraft:ore |
| [tuff_ore](#tuff-ore) | uniform: bottom +0 → Y 0 | 2 attempts | 64 | minecraft:ore |
| [varsium_ore](#varsium-ore) | uniform: Y 99 → Y 145 | uniform 1–3 attempts | 6 | minecraft:ore |

## Individual features and destinations

### baronyte ore

**Bindings:** `aoa3:barathos_flats`, `aoa3:barren_oasis`, `aoa3:the_burning_pits`, `aoa3:the_spears`

**Output blocks:** [aoa3:baronyte_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:baronyte_ore)

**Direct tool tags:** `aoa3:baronyte_ore`: `mineable/pickaxe`, `needs_diamond_tool`

**Host predicates:** `[{"block":"aoa3:baron_stone","predicate_type":"minecraft:block_match"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=baronyte_ore)

**Dimension JSON references:** `aoa3:barathos`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/baronyte_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:survives_explosion"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:baronyte_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/baronyte_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/baronyte_ore.json`

</details>

### blazium ore

**Bindings:** `aoa3:the_burning_pits`

**Output blocks:** [aoa3:blazium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:blazium_ore)

**Direct tool tags:** `aoa3:blazium_ore`: `mineable/pickaxe`, `needs_diamond_tool`

**Host predicates:** `[{"block":"aoa3:hellstone","predicate_type":"minecraft:block_match"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=blazium_ore)

**Dimension JSON references:** `aoa3:barathos`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/blazium_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:survives_explosion"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:blazium_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/blazium_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/blazium_ore.json`

</details>

### bone fragments ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:bone_fragments_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:bone_fragments_ore), [aoa3:deepslate_bone_fragments_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_bone_fragments_ore)

**Direct tool tags:** `aoa3:bone_fragments_ore`: `mineable/pickaxe`, `needs_iron_tool`; `aoa3:deepslate_bone_fragments_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.3.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=bone_fragments_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/bone_fragments_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:inverted",
          "term": {
            "condition": "minecraft:match_tool",
            "predicate": {
              "predicates": {
                "minecraft:enchantments": [
                  {
                    "enchantments": "minecraft:silk_touch",
                    "levels": {
                      "min": 1
                    }
                  }
                ]
              }
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:chestbone_fragment"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:legbone_fragment"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:skullbone_fragment"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:footbone_fragment"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:match_tool",
          "predicate": {
            "predicates": {
              "minecraft:enchantments": [
                {
                  "enchantments": "minecraft:silk_touch",
                  "levels": {
                    "min": 1
                  }
                }
              ]
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:bone_fragments_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`data/aoa3/loot_table/blocks/deepslate_bone_fragments_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:inverted",
          "term": {
            "condition": "minecraft:match_tool",
            "predicate": {
              "predicates": {
                "minecraft:enchantments": [
                  {
                    "enchantments": "minecraft:silk_touch",
                    "levels": {
                      "min": 1
                    }
                  }
                ]
              }
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:chestbone_fragment"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:legbone_fragment"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:skullbone_fragment"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            }
          ],
          "name": "aoa3:footbone_fragment"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:match_tool",
          "predicate": {
            "predicates": {
              "minecraft:enchantments": [
                {
                  "enchantments": "minecraft:silk_touch",
                  "levels": {
                    "min": 1
                  }
                }
              ]
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:deepslate_bone_fragments_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/bone_fragments_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/bone_fragments_ore.json`

</details>

### gravel ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:gravel](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:gravel)

**Direct tool tags:** `minecraft:gravel`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=gravel)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/gravel_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/gravel_ore.json`

</details>

### high altitude andesite ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:andesite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:andesite)

**Direct tool tags:** `minecraft:andesite`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=andesite)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/high_altitude_andesite_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/andesite_ore.json`

</details>

### high altitude diorite ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:diorite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:diorite)

**Direct tool tags:** `minecraft:diorite`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=diorite)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/high_altitude_diorite_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/diorite_ore.json`

</details>

### high altitude granite ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:granite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:granite)

**Direct tool tags:** `minecraft:granite`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=granite)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/high_altitude_granite_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/granite_ore.json`

</details>

### low altitude andesite ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:andesite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:andesite)

**Direct tool tags:** `minecraft:andesite`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=andesite)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/low_altitude_andesite_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/andesite_ore.json`

</details>

### low altitude diorite ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:diorite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:diorite)

**Direct tool tags:** `minecraft:diorite`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=diorite)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/low_altitude_diorite_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/diorite_ore.json`

</details>

### low altitude granite ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:granite](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:granite)

**Direct tool tags:** `minecraft:granite`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=granite)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/low_altitude_granite_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/granite_ore.json`

</details>

### ore emberstone

**Bindings:** if_all: `#minecraft:is_nether`

**Output blocks:** [aoa3:emberstone_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:emberstone_ore)

**Direct tool tags:** `aoa3:emberstone_ore`: `mineable/pickaxe`, `needs_diamond_tool`

**Host predicates:** `[{"block":"minecraft:netherrack","predicate_type":"minecraft:block_match"}]`

**Air-exposure discard parameter:** 0.75.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=emberstone_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/emberstone_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:emberstone_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:raw_emberstone"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/ore_emberstone.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_emberstone.json`

</details>

### ore jade large

**Bindings:** if_all: `#minecraft:is_overworld`; if_any: `#minecraft:is_beach`, `#minecraft:is_river`

**Output blocks:** [aoa3:deepslate_jade_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_jade_ore), [aoa3:jade_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:jade_ore)

**Direct tool tags:** `aoa3:deepslate_jade_ore`: `mineable/pickaxe`, `needs_iron_tool`; `aoa3:jade_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=deepslate_jade_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/deepslate_jade_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:deepslate_jade_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:jade"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`data/aoa3/loot_table/blocks/jade_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:jade_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:jade"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/ore_jade_large.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_jade_large.json`

</details>

### ore jade small

**Bindings:** excluding: `#minecraft:is_beach`, `#minecraft:is_river`; if_all: `#minecraft:is_overworld`

**Output blocks:** [aoa3:deepslate_jade_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_jade_ore), [aoa3:jade_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:jade_ore)

**Direct tool tags:** `aoa3:deepslate_jade_ore`: `mineable/pickaxe`, `needs_iron_tool`; `aoa3:jade_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=deepslate_jade_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:deepslate_jade_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Loot for `aoa3:jade_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/ore_jade_small.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_jade_small.json`

</details>

### ore limonite large

**Bindings:** if_all: `#minecraft:is_overworld`, `#c:is_underground`; if_any: `#c:is_lush`, `#c:is_wet`, `minecraft:dripstone_caves`

**Output blocks:** [aoa3:deepslate_limonite_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_limonite_ore), [aoa3:limonite_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:limonite_ore)

**Direct tool tags:** `aoa3:deepslate_limonite_ore`: `mineable/pickaxe`, `needs_stone_tool`; `aoa3:limonite_ore`: `mineable/pickaxe`, `needs_stone_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=deepslate_limonite_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/deepslate_limonite_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:deepslate_limonite_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:raw_limonite"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`data/aoa3/loot_table/blocks/limonite_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:limonite_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:raw_limonite"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/ore_limonite_large.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_limonite_large.json`

</details>

### ore limonite small

**Bindings:** if_all: `#minecraft:is_overworld`

**Output blocks:** [aoa3:deepslate_limonite_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_limonite_ore), [aoa3:limonite_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:limonite_ore)

**Direct tool tags:** `aoa3:deepslate_limonite_ore`: `mineable/pickaxe`, `needs_stone_tool`; `aoa3:limonite_ore`: `mineable/pickaxe`, `needs_stone_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=deepslate_limonite_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:deepslate_limonite_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Loot for `aoa3:limonite_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/ore_limonite_small.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_limonite_small.json`

</details>

### ore nether runium

**Bindings:** if_all: `#minecraft:is_nether`; if_any: `#c:is_magical`, `minecraft:warped_forest`

**Output blocks:** [aoa3:nether_runium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:nether_runium_ore)

**Direct tool tags:** `aoa3:nether_runium_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"block":"minecraft:netherrack","predicate_type":"minecraft:block_match"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=nether_runium_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/nether_runium_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:nether_runium_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:runium_chunk"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/ore_nether_runium.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_nether_runium.json`

</details>

### ore runium large

**Bindings:** if_all: `#minecraft:is_overworld`; if_any: `#c:is_magical`

**Output blocks:** [aoa3:deepslate_runium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_runium_ore), [aoa3:runium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:runium_ore)

**Direct tool tags:** `aoa3:deepslate_runium_ore`: `mineable/pickaxe`, `needs_iron_tool`; `aoa3:runium_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=deepslate_runium_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/deepslate_runium_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:deepslate_runium_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:runium_chunk"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

`data/aoa3/loot_table/blocks/runium_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:runium_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "aoa3:runium_chunk"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/ore_runium_large.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_runium_large.json`

</details>

### ore runium small

**Bindings:** excluding: `#c:is_dead`; if_all: `#minecraft:is_overworld`

**Output blocks:** [aoa3:deepslate_runium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_runium_ore), [aoa3:runium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:runium_ore)

**Direct tool tags:** `aoa3:deepslate_runium_ore`: `mineable/pickaxe`, `needs_iron_tool`; `aoa3:runium_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=deepslate_runium_ore)

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:deepslate_runium_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Loot for `aoa3:runium_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/ore_runium_small.json`  
Configured: `data/aoa3/worldgen/configured_feature/ore_runium_small.json`

</details>

### precasian buried lapis ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_lapis_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_lapis_ore), [minecraft:deepslate_lapis_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_lapis_ore)

**Direct tool tags:** `aoa3:precasian_lapis_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_lapis_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 1.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_lapis_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/precasian_lapis_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:inverted",
          "term": {
            "condition": "minecraft:match_tool",
            "predicate": {
              "predicates": {
                "minecraft:enchantments": [
                  {
                    "enchantments": "minecraft:silk_touch",
                    "levels": {
                      "min": 1
                    }
                  }
                ]
              }
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            },
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:ore_drops",
              "function": "minecraft:apply_bonus"
            },
            {
              "function": "minecraft:explosion_decay"
            }
          ],
          "name": "minecraft:lapis_lazuli"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:match_tool",
          "predicate": {
            "predicates": {
              "minecraft:enchantments": [
                {
                  "enchantments": "minecraft:silk_touch",
                  "levels": {
                    "min": 1
                  }
                }
              ]
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:precasian_lapis_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/precasian_buried_lapis_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_buried_lapis_ore.json`

</details>

### precasian copper ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_copper_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_copper_ore), [minecraft:deepslate_copper_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_copper_ore)

**Direct tool tags:** `aoa3:precasian_copper_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_copper_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_copper_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/precasian_copper_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:precasian_copper_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "minecraft:raw_copper"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/precasian_copper_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_copper_ore.json`

</details>

### precasian gold ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_gold_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_gold_ore), [minecraft:deepslate_gold_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_gold_ore)

**Direct tool tags:** `aoa3:precasian_gold_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_gold_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.5.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_gold_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/precasian_gold_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:precasian_gold_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "minecraft:raw_gold"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/precasian_gold_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_buried_gold_ore.json`

</details>

### precasian high altitude iron ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_iron_ore), [minecraft:deepslate_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_iron_ore)

**Direct tool tags:** `aoa3:precasian_iron_ore`: `mineable/pickaxe`, `needs_stone_tool`; `minecraft:deepslate_iron_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_iron_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/precasian_iron_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:precasian_iron_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "minecraft:raw_iron"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/precasian_high_altitude_iron_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_iron_ore.json`

</details>

### precasian iron ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_iron_ore), [minecraft:deepslate_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_iron_ore)

**Direct tool tags:** `aoa3:precasian_iron_ore`: `mineable/pickaxe`, `needs_stone_tool`; `minecraft:deepslate_iron_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_iron_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:precasian_iron_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/precasian_iron_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_iron_ore.json`

</details>

### precasian lapis ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_lapis_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_lapis_ore), [minecraft:deepslate_lapis_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_lapis_ore)

**Direct tool tags:** `aoa3:precasian_lapis_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_lapis_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_lapis_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:precasian_lapis_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/precasian_lapis_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_lapis_ore.json`

</details>

### precasian low altitude gold ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_gold_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_gold_ore), [minecraft:deepslate_gold_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_gold_ore)

**Direct tool tags:** `aoa3:precasian_gold_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_gold_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.5.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_gold_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:precasian_gold_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/precasian_low_altitude_gold_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_buried_gold_ore.json`

</details>

### precasian low altitude iron ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_iron_ore), [minecraft:deepslate_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_iron_ore)

**Direct tool tags:** `aoa3:precasian_iron_ore`: `mineable/pickaxe`, `needs_stone_tool`; `minecraft:deepslate_iron_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_iron_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:precasian_iron_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/precasian_low_altitude_iron_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_iron_ore.json`

</details>

### precasian low altitude redstone ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_redstone_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_redstone_ore), [minecraft:deepslate_redstone_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_redstone_ore)

**Direct tool tags:** `aoa3:precasian_redstone_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_redstone_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_redstone_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/precasian_redstone_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:inverted",
          "term": {
            "condition": "minecraft:match_tool",
            "predicate": {
              "predicates": {
                "minecraft:enchantments": [
                  {
                    "enchantments": "minecraft:silk_touch",
                    "levels": {
                      "min": 1
                    }
                  }
                ]
              }
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            },
            {
              "enchantment": "minecraft:fortune",
              "formula": "minecraft:uniform_bonus_count",
              "function": "minecraft:apply_bonus",
              "parameters": {
                "bonusMultiplier": 1
              }
            },
            {
              "function": "minecraft:explosion_decay"
            }
          ],
          "name": "minecraft:redstone"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:match_tool",
          "predicate": {
            "predicates": {
              "minecraft:enchantments": [
                {
                  "enchantments": "minecraft:silk_touch",
                  "levels": {
                    "min": 1
                  }
                }
              ]
            }
          }
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:precasian_redstone_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/precasian_low_altitude_redstone_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_redstone_ore.json`

</details>

### precasian quartz ore

**Bindings:** `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_quartz_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_quartz_ore)

**Direct tool tags:** `aoa3:precasian_quartz_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_quartz_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/precasian_quartz_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "predicates": {
                      "minecraft:enchantments": [
                        {
                          "enchantments": "minecraft:silk_touch",
                          "levels": {
                            "min": 1
                          }
                        }
                      ]
                    }
                  }
                }
              ],
              "name": "aoa3:precasian_quartz_ore"
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops",
                  "function": "minecraft:apply_bonus"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": "minecraft:quartz"
            }
          ]
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/precasian_quartz_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_quartz_ore.json`

</details>

### precasian redstone ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_redstone_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_redstone_ore), [minecraft:deepslate_redstone_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_redstone_ore)

**Direct tool tags:** `aoa3:precasian_redstone_ore`: `mineable/pickaxe`, `needs_iron_tool`; `minecraft:deepslate_redstone_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_redstone_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:precasian_redstone_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/precasian_redstone_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_redstone_ore.json`

</details>

### precasian small iron ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [aoa3:precasian_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:precasian_iron_ore), [minecraft:deepslate_iron_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:deepslate_iron_ore)

**Direct tool tags:** `aoa3:precasian_iron_ore`: `mineable/pickaxe`, `needs_stone_tool`; `minecraft:deepslate_iron_ore`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=precasian_iron_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:precasian_iron_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/precasian_small_iron_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/precasian_small_iron_ore.json`

</details>

### shallow bone fragments ore

**Bindings:** `aoa3:precasian_deadlands`, `aoa3:precasian_tar_pits`

**Output blocks:** [aoa3:bone_fragments_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:bone_fragments_ore), [aoa3:deepslate_bone_fragments_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:deepslate_bone_fragments_ore)

**Direct tool tags:** `aoa3:bone_fragments_ore`: `mineable/pickaxe`, `needs_iron_tool`; `aoa3:deepslate_bone_fragments_ore`: `mineable/pickaxe`, `needs_iron_tool`

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"minecraft:stone_ore_replaceables"},{"predicate_type":"minecraft:tag_match","tag":"minecraft:deepslate_ore_replaceables"}]`

**Air-exposure discard parameter:** 0.3.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=bone_fragments_ore)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

Loot for `aoa3:bone_fragments_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Loot for `aoa3:deepslate_bone_fragments_ore` is shown under its earlier feature above; the hashed extraction retains this binding.

Placed: `data/aoa3/worldgen/placed_feature/shallow_bone_fragments_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/bone_fragments_ore.json`

</details>

### tuff ore

**Bindings:** `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`

**Output blocks:** [minecraft:tuff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=minecraft:tuff)

**Direct tool tags:** `minecraft:tuff`: 

**Host predicates:** `[{"predicate_type":"minecraft:tag_match","tag":"c:stones"}]`

**Air-exposure discard parameter:** 0.0.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=tuff)

**Dimension JSON references:** `aoa3:precasia`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

No matching AoA-owned block loot resource in this record.

Placed: `data/aoa3/worldgen/placed_feature/tuff_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/tuff_ore.json`

</details>

### varsium ore

**Bindings:** `aoa3:barathos_flats`, `aoa3:barren_oasis`, `aoa3:the_spears`

**Output blocks:** [aoa3:varsium_ore](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:varsium_ore)

**Direct tool tags:** `aoa3:varsium_ore`: `mineable/pickaxe`, `needs_diamond_tool`

**Host predicates:** `[{"block":"aoa3:baron_stone","predicate_type":"minecraft:block_match"}]`

**Air-exposure discard parameter:** 0.75.

[Find crafting and processing uses](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=varsium_ore)

**Dimension JSON references:** `aoa3:barathos`.

<details><summary>Bundled block loot and source paths</summary>

Loot is shown as structured evidence, not flattened into an unconditional drop promise. Vanilla loot resources outside this AoA artifact are not included.

`data/aoa3/loot_table/blocks/varsium_ore.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": {
        "type": "minecraft:uniform",
        "max": 0.0,
        "min": 0.0
      },
      "conditions": [
        {
          "condition": "minecraft:survives_explosion"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "aoa3:varsium_ore"
        }
      ],
      "rolls": 1.0
    }
  ]
}
```

Placed: `data/aoa3/worldgen/placed_feature/varsium_ore.json`  
Configured: `data/aoa3/worldgen/configured_feature/varsium_ore.json`

</details>

## Evidence and remaining validation

[Download the full hashed extraction](https://herbertofury.github.io/Advent-of-Ascension/ore-generation-evidence-1.21.1.json). The extraction keeps placed/configured JSON hashes, biome/modifier bindings, direct tool tags and bundled block loot.

- Resolve final biome/tag membership with the actual modpack and enabled data packs.
- Test fresh chunks and dimension reachability on the intended build. Existing chunks do not establish newly generated distribution.
- Measure representative seed samples before claiming optimal Y, expected yield, rarity or guaranteed veins.
- Compare local Enderloom generation against this released baseline before marking a port complete.

Related: [Inventory Explorer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Recipe Explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1) · [Boss token preparation](Boss-Entry-and-Token-Preparation-1.21.1).
