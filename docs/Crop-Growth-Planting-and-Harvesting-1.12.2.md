# Crop growth, planting and harvesting · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** Sixteen itemless world crops, all **128 age-state references**, and their checked planting/produce links. These blocks are not missing collectible items: their seeds or edible planting items place them in the world.

## Start a farm without mixing up the items

1. **Find the planting item in the directory below.** Fourteen crops use a separate SeedsItem. Eye Bulb and Mystic Shrooms use the same ItemSeedFood object for planting and produce. Keep enough planting stock before eating or selling it.
2. **Prepare farmland and an empty space above it.** The checked AoA seed constructors pass the crop and vanilla farmland to their inherited seed-item implementation. Start with ordinary accessible farmland and use the seed on its upper face. Exact Forge placement hooks, permissions and other mods can affect success.
3. **Compare the picture with ages 0–7.** Age7 is mature. Do not treat the varying illustrations as an eight-second timer; random ticks, light, soil and hooks affect growth. These are static world-model studies with an explicit angled camera, not in-game screenshots.
4. **Use a mature crop to harvest without replanting.** The AoA activation handler calculates drops on the server, processes the Forge harvesting callback, spawns accepted stacks and resets the crop to its default age 0. The mature activation returns true; an immature activation returns false.
5. **Reserve seeds and inspect the actual result.** The extra-seed loop is random, and harvest hooks can change or suppress drops. Fortune is the higher enchantment level of your main-hand and off-hand held items, not their sum.
6. **For bonemeal, expect a request for 1–3 growth stages.** The AoA override uses nextInt(3)+1. The inherited growth clamp and Forge/modpack hooks still matter; it is not a guarantee of instant maturity.

## Crop and planting-item directory

| Crop world block | Planting item | Linked produce | Extra-seed attempts before Fortune |
|---|---|---|---:|
| [Bubble Berries](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Abubble_berry_crop) | [bubble_berry_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=bubble_berry_seeds) | [bubble_berries](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=bubble_berries) | 3 |
| [Chilli](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Achilli_crop) | [chilli_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=chilli_seeds) | [chilli](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=chilli) | 3 |
| [Eye Bulb](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aeye_bulb_crop) | [eye_bulb](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=eye_bulb) | [eye_bulb](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=eye_bulb) | 1 |
| [Floracles](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Afloracles_crop) | [floracle_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=floracle_seeds) | [floracle_sticks](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=floracle_sticks) | 3 |
| [Goldicaps](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agoldicaps_crop) | [goldicap_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=goldicap_seeds) | [goldicap_petals](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=goldicap_petals) | 3 |
| [Heart Fruit](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aheart_fruit_crop) | [heart_fruit_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=heart_fruit_seeds) | [heart_fruit](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=heart_fruit) | 1 |
| [Holly Tops](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aholly_tops_crop) | [holly_top_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=holly_top_seeds) | [holly_top_petals](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=holly_top_petals) | 3 |
| [Lunacrike](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Alunacrike_crop) | [lunacrike_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=lunacrike_seeds) | [lunacrike](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=lunacrike) | 3 |
| [Luna Globe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aluna_globe_crop) | [luna_globe_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=luna_globe_seeds) | [luna_globe](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=luna_globe) | 3 |
| [Lunalip](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Alunalon_crop) | [lunalon_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=lunalon_seeds) | [lunalons](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=lunalons) | 3 |
| [Magic Marang](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amagic_marang_crop) | [magic_marang_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=magic_marang_seeds) | [magic_marang](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=magic_marang) | 1 |
| [Mystic Shrooms](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amystic_shroom_crop) | [mystic_shrooms](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=mystic_shrooms) | [mystic_shrooms](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=mystic_shrooms) | 1 |
| [Rosidons](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Arosidon_crop) | [rosidon_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=rosidon_seeds) | [rosidons](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=rosidons) | 3 |
| [Tea](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Atea_crop) | [tea_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=tea_seeds) | [tea_shreddings](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=tea_shreddings) | 3 |
| [Thorny Plant](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Athorny_plant_crop) | [thorny_plant_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=thorny_plant_seeds) | [thorny_petals](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=thorny_petals) | 3 |
| [Trilliads](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Atrilliad_crop) | [trilliad_seeds](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=trilliad_seeds) | [trilliad_leaves](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&q=trilliad_leaves) | 3 |

## Seed yield: what the code actually promises

The local getDrops method first delegates its base quantity and chosen item to inherited crop behavior. Once mature, it performs **Fortune + (dropsSeeds ? 3 : 1)** extra attempts. Each succeeds when **nextInt(2 × maxAge) ≤ age**. With the inherited maximum age 7, that is eight accepted values out of fourteen, or **4/7 per attempt**, before the external harvesting callback and spawn-chance filter.

The misleading edge case is the dropsSeeds=false flag: **it still allows one extra attempt at Fortune 0**. Eye Bulb, Heart Fruit, Magic Marang and Mystic Shrooms use that false flag. It does not mean “never drops planting items.” Conversely, a base of three attempts does not mean three guaranteed seeds.

The mature activation passes initial chance 1 to Forge’s harvesting callback and compares each returned stack with the callback’s resulting chance. It then resets the crop. Other mods can change the list or chance, so the reset must not be documented as proof that you received every item. The subsequent placement callback’s return value is ignored by this local method; event interactions need live testing.

The separate dropBlockAsItemWithChance override forwards Fortune+1 to its superclass. That statement describes this override only; it is not proof that every harvesting or breaking route reaches it. The right-click path calls getDrops directly with the max-of-two-hands Fortune value.

## Growth and environment limits

The shipped vanilla 1.12.2 BlockCrops comparison has maximum age 7 and checks light above the crop against 9 in its random-tick growth path. Its growth probability also depends on the inherited soil/neighbor growth factor. This study retains those vanilla method hashes for comparison, but **does not claim an unpatched vanilla client JAR is the exact Forge runtime implementation**. Forge patches, server rules and other mods require separate verification. No fixed growth time is promised.

## All sixteen growth strips

Each strip shows the exact released age 0–7 model references. Some adjacent ages reuse identical-looking textures; those legitimate repeats are retained rather than replaced with invented growth art. Cutout planes are rendered from an angled documentation camera with backface culling.

### Bubble Berries

![Bubble Berries, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-bubble_berry_crop.webp)

World block: `aoa3:bubble_berry_crop`. Plant `aoa3:bubble_berry_seeds`; linked produce `aoa3:bubble_berries`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Abubble_berry_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Abubble_berry_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Abubble_berry_seeds)

### Chilli

![Chilli, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-chilli_crop.webp)

World block: `aoa3:chilli_crop`. Plant `aoa3:chilli_seeds`; linked produce `aoa3:chilli`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Achilli_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Achilli_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Achilli_seeds)

### Eye Bulb

![Eye Bulb, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-eye_bulb_crop.webp)

World block: `aoa3:eye_bulb_crop`. Plant `aoa3:eye_bulb`; linked produce `aoa3:eye_bulb`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aeye_bulb_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aeye_bulb) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Aeye_bulb)

### Floracles

![Floracles, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-floracles_crop.webp)

World block: `aoa3:floracles_crop`. Plant `aoa3:floracle_seeds`; linked produce `aoa3:floracle_sticks`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Afloracles_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Afloracle_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Afloracle_seeds)

### Goldicaps

![Goldicaps, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-goldicaps_crop.webp)

World block: `aoa3:goldicaps_crop`. Plant `aoa3:goldicap_seeds`; linked produce `aoa3:goldicap_petals`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Agoldicaps_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Agoldicap_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Agoldicap_seeds)

### Heart Fruit

![Heart Fruit, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-heart_fruit_crop.webp)

World block: `aoa3:heart_fruit_crop`. Plant `aoa3:heart_fruit_seeds`; linked produce `aoa3:heart_fruit`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aheart_fruit_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aheart_fruit_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Aheart_fruit_seeds)

### Holly Tops

![Holly Tops, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-holly_tops_crop.webp)

World block: `aoa3:holly_tops_crop`. Plant `aoa3:holly_top_seeds`; linked produce `aoa3:holly_top_petals`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aholly_tops_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aholly_top_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Aholly_top_seeds)

### Lunacrike

![Lunacrike, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-lunacrike_crop.webp)

World block: `aoa3:lunacrike_crop`. Plant `aoa3:lunacrike_seeds`; linked produce `aoa3:lunacrike`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Alunacrike_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Alunacrike_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Alunacrike_seeds)

### Luna Globe

![Luna Globe, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-luna_globe_crop.webp)

World block: `aoa3:luna_globe_crop`. Plant `aoa3:luna_globe_seeds`; linked produce `aoa3:luna_globe`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Aluna_globe_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aluna_globe_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Aluna_globe_seeds)

### Lunalip

![Lunalip, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-lunalon_crop.webp)

World block: `aoa3:lunalon_crop`. Plant `aoa3:lunalon_seeds`; linked produce `aoa3:lunalons`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Alunalon_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Alunalon_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Alunalon_seeds)

### Magic Marang

![Magic Marang, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-magic_marang_crop.webp)

World block: `aoa3:magic_marang_crop`. Plant `aoa3:magic_marang_seeds`; linked produce `aoa3:magic_marang`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amagic_marang_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Amagic_marang_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Amagic_marang_seeds)

### Mystic Shrooms

![Mystic Shrooms, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-mystic_shroom_crop.webp)

World block: `aoa3:mystic_shroom_crop`. Plant `aoa3:mystic_shrooms`; linked produce `aoa3:mystic_shrooms`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Amystic_shroom_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Amystic_shrooms) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Amystic_shrooms)

### Rosidons

![Rosidons, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-rosidon_crop.webp)

World block: `aoa3:rosidon_crop`. Plant `aoa3:rosidon_seeds`; linked produce `aoa3:rosidons`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Arosidon_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Arosidon_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Arosidon_seeds)

### Tea

![Tea, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-tea_crop.webp)

World block: `aoa3:tea_crop`. Plant `aoa3:tea_seeds`; linked produce `aoa3:tea_shreddings`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Atea_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Atea_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Atea_seeds)

### Thorny Plant

![Thorny Plant, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-thorny_plant_crop.webp)

World block: `aoa3:thorny_plant_crop`. Plant `aoa3:thorny_plant_seeds`; linked produce `aoa3:thorny_petals`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Athorny_plant_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Athorny_plant_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Athorny_plant_seeds)

### Trilliads

![Trilliads, ages 0 through7](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/crop-stages-1.12.2-trilliad_crop.webp)

World block: `aoa3:trilliad_crop`. Plant `aoa3:trilliad_seeds`; linked produce `aoa3:trilliad_leaves`. [Inspect this crop](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=aoa3%3Atrilliad_crop) · [Search version-specific recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Atrilliad_seeds) · [Search trader offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&q=aoa3%3Atrilliad_seeds)

## Farming, skills and obtaining seeds

The item links and recipe/trader searches are navigation aids, not a claim that every seed has a recipe or a sale offer. Natural generation, creature drops and special acquisition callbacks must be checked individually. Source comments about where seeds drop are not used as proof of current availability.

For related mechanics, read [Anima training and fragments](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2), [Holy Sword tribute and the Gardener reward](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Holy-Sword-Tribute-and-Gardener-Rewards-1.12.2) and [historical trading](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trading-and-Traders-1.12.2). Their gates are separate from the basic crop harvest method.

## Evidence and remaining acceptance

- [Released crop, seed, produce and state evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/crop-study-evidence-1.12.2.json): 16 registrations, 128 states and 36 methods.
- [Earlier inventory/model identity repairs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Registered-Blocks-and-Items-1.12.2).
- Check multiplayer harvest synchronization, inventory/drop outcomes, Fortune on each hand, bonemeal at every age, Forge event cancellation/modification, farmland placement permissions and save/reload in the target game build.
- No live game test, runtime timing benchmark, universal seed-acquisition promise or merged Enderloom compatibility certification is implied.
- Original models, textures and systems by Tslat and AoA contributors; vanilla references by Mojang. Independent illustrated documentation.
