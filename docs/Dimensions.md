[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Walkthrough library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html) · [Progress](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Progress)

# Worlds & travel atlas

Choose a release before planning an expedition. This atlas distinguishes **dimension code declarations, shipped data definitions, biome references and checked travel instructions**. None of those alone certifies a complete playable realm in the owner’s converted build.

[![Precasia community-wiki visual reference](https://static.wikia.nocookie.net/adventofascension_gamepedia/images/d/dd/Precasia.png/revision/latest/scale-to-width-down/1200?cb=20231007014020)](https://adventofascension.fandom.com/wiki/Precasia)

*Precasia reference hosted by the community wiki; AoA by Tslat, image credit to its contributors. This is not a screenshot of the owner’s converted build. Realmstone pictures below are explicitly 1.16.5 item studies, not images of the worlds themselves.*

## Start with the right travel guide

| Your release | Start here | Important boundary |
|---|---|---|
| 1.12.2 / 3.3.6 | [First portal and Precasia](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) | Code-era dimensions use configurable integer IDs; namespaced keys here are comparison labels. |
| 1.16.5 / 3.6.11 | [First portal](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-Walkthrough-1.16.5) · [22 realmstone routes and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5) | Follow the release-specific trigger and destination checks. |
| 1.20.1 / 3.7.1 | [Portal support and preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Portal-Support-and-Preparation-1.20.1) | Retained dimension files do not certify every travel/acquisition route. |
| 1.21.1 / 3.7.16.1 | [First portal](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-Walkthrough) · [Precasia archaeology](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Precasia-Realmstone-Walkthrough) · [Nowhere/Skill Master](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1) | Nowhere arenas and ordinary realm portals are different journeys. |

## What is actually present in the inspected releases

| Release | Evidence counted | What that count does not say |
|---|---|---|
| 1.12.2 | **22 released code declarations** | Not 22 validated survival routes; IDs and registration can be affected by configuration. |
| 1.16.5 | **21 dimension JSON definitions** | Not proof every legacy route remains active in a newer build. |
| 1.20.1 | **7 dimension JSON definitions**, including `precasia_backup` | Do not advertise the backup-named file as a seventh confirmed adventure destination. |
| 1.21.1 | **10 dimension JSON definitions** | Includes custom empty-generator definitions; presence does not mean a complete terrain/ecology loop. |

All selected **direct** dimension-type, named noise-settings and biome references resolve inside their respective inspected JARs. This checks those immediate resources only. It does not validate every configured feature, structure processor, custom generator codec or runtime event.

## Realm presence matrix

**Code** = released 1.12.2 declaration. **Data** = dimension JSON present. **—** = absent from that selected evidence category, not proof all related content was deleted.

| Realm | 1.12.2 code | 1.16.5 data | 1.20.1 data | 1.21.1 data |
|---|---|---|---|---|
| [Abyss](#abyss) | Code | Data | — | Data |
| [Ancient Cavern](#ancient-cavern) | Code | — | — | — |
| [Barathos](#barathos) | Code | Data | Data | Data |
| [Candyland](#candyland) | Code | Data | — | — |
| [Celeve](#celeve) | Code | Data | — | Data |
| [Creeponia](#creeponia) | Code | Data | — | — |
| [Crystevia](#crystevia) | Code | Data | — | Data |
| [Deeplands](#deeplands) | Code | Data | Data | Data |
| [Dustopia](#dustopia) | Code | Data | — | Data |
| [Gardencia](#gardencia) | Code | Data | — | — |
| [Greckon](#greckon) | Code | Data | — | — |
| [Haven](#haven) | Code | Data | — | — |
| [Immortallis](#immortallis) | Code | — | — | — |
| [Iromine](#iromine) | Code | Data | — | — |
| [L’Borean](#lborean) | Code | Data | Data | Data |
| [Lelyetia](#lelyetia) | Code | Data | Data | Data |
| [Lunalus](#lunalus) | Code | Data | — | — |
| [Mysterium](#mysterium) | Code | Data | — | — |
| [Nowhere](#nowhere) | — | Data | Data | Data |
| [Precasia](#precasia) | Code | Data | Data | Data |
| [Precasia backup resource](#precasia-backup-resource) | — | — | Data | — |
| [Runandor](#runandor) | Code | Data | — | — |
| [Shyrelands](#shyrelands) | Code | Data | — | — |
| [Vox Ponds](#vox-ponds) | Code | Data | — | — |

## Read world settings carefully

- **Dimension height and logical height** are separate fields. Neither is automatically the generator’s terrain height.
- **Bed/anchor flags** describe the shipped dimension type. Check the exact target world before relying on a respawn plan; this atlas has not run a sleep or death test.
- **Fixed time** is a declared time value, not a guarantee about every custom lighting, weather or shader effect.
- **Biome lists** are direct identifiers in the generator definition. Their count is not a sample of actual world distribution.
- Bestiary links are offered only where the current extracted roster has a matching dimension or documented arena route. An absent link does not mean an empty world.

## Realm dossiers

### Abyss

Comparison key: `aoa3:abyss`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-abyss.webp" width="160" height="160" alt="1.16.5 Abyss Realmstone source-item study">

**1.16.5 entry note:** Summon a Wither in the Nether while carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#abyss).

**1.12.2 declaration:** `DIM_ABYSS` selects `WorldProviderAbyss`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:abyssal_plains`.
- Dimension type: `aoa3:abyss`.
- Declared type fields: `logical_height=256`, `fixed_time=6000`, `has_skylight=false`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:abyssal_stone`, fluid `minecraft:air`, sea level `0`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:abyssal_valley`.
- Dimension type: `aoa3:abyss`.
- Declared type fields: `min_y=0`, `height=512`, `logical_height=319`, `has_skylight=false`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:abyssal_stone`, fluid `minecraft:water`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Aabyss) (10 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Aabyss) (9 dimension-tagged entries).

### Ancient Cavern

Comparison key: `aoa3:ancient_cavern`.

**1.12.2 declaration:** `DIM_ANCIENT_CAVERN` selects `WorldProviderAncientCavern`; its integer ID comes from configuration.

This historical code-era realm is outside the inspected 1.16.5 dimension JSON list. Keep its provider, encounters and progression dependencies as a distinct restoration task.

[Follow the historical entry, tribute and four-shrine walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2).

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Aancient_cavern) (0 dimension-tagged entries; 4 arena routes).

### Barathos

Comparison key: `aoa3:barathos`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-barathos.webp" width="160" height="160" alt="1.16.5 Barathos Realmstone source-item study">

**1.16.5 entry note:** Deliver the killing melee blow to a Husk with the Blank Realmstone in your main hand. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#barathos).

**1.12.2 declaration:** `DIM_BARATHOS` selects `WorldProviderBarathos`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:barren_grounds`.
- Dimension type: `aoa3:barathos`.
- Declared type fields: `logical_height=256`, `fixed_time=8000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:baron_stone`, fluid `minecraft:air`, sea level `0`.

#### 1.20.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (2): `aoa3:barathos_flats`, `aoa3:the_burning_pits`.
- Dimension type: `aoa3:barathos`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:baron_stone`, fluid `minecraft:air`, sea level `-64`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (4): `aoa3:barathos_flats`, `aoa3:barren_oasis`, `aoa3:the_burning_pits`, `aoa3:the_spears`.
- Dimension type: `aoa3:barathos`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `fixed_time=2000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:baron_stone`, fluid `minecraft:air`, sea level `-64`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Abarathos) (13 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Abarathos) (12 dimension-tagged entries) · [1.21.1 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&dimension=aoa3%3Abarathos) (3 dimension-tagged entries).

### Candyland

Comparison key: `aoa3:candyland`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-candyland.webp" width="160" height="160" alt="1.16.5 Candyland Realmstone source-item study">

**1.16.5 entry note:** Finish eating a Heart Fruit in Precasia while carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#candyland).

**1.12.2 declaration:** `DIM_CANDYLAND` selects `WorldProviderCandyland`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:candy_hills`.
- Dimension type: `aoa3:candyland`.
- Declared type fields: `logical_height=256`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:candied_dirt`, fluid `aoa3:candied_water`, sea level `63`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Acandyland) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Acandyland) (8 dimension-tagged entries).

### Celeve

Comparison key: `aoa3:celeve`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-celeve.webp" width="160" height="160" alt="1.16.5 Celeve Realmstone source-item study">

**1.16.5 entry note:** Kill a Lelyetian Warrior using player-attributed firework damage while carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#celeve).

**1.12.2 declaration:** `DIM_CELEVE` selects `WorldProviderCeleve`; its integer ID comes from configuration.

**Modern generator distinction:** the 1.21.1 definition uses `aoa3:empty` with the `aoa3:floating_big_top` biome. The generator name alone does not establish which structure/event systems complete the destination.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:celevian_highlands`.
- Dimension type: `aoa3:celeve`.
- Declared type fields: `logical_height=256`, `fixed_time=0`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:celevian_dirt`, fluid `minecraft:air`, sea level `0`.

#### 1.21.1 resource details

- Generator: `aoa3:empty`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:floating_big_top`.
- Dimension type: `aoa3:celeve`.
- Declared type fields: `min_y=0`, `height=512`, `logical_height=319`, `fixed_time=2000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=false`, `coordinate_scale=1.0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Aceleve) (11 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Aceleve) (13 dimension-tagged entries).

### Creeponia

Comparison key: `aoa3:creeponia`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-creeponia.webp" width="160" height="160" alt="1.16.5 Creeponia Realmstone source-item study">

**1.16.5 entry note:** Take a Creeper explosion hit with primed TNT nearby and a Blank Realmstone in inventory. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#creeponia).

**1.12.2 declaration:** `DIM_CREEPONIA` selects `WorldProviderCreeponia`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:creepoid_forest`.
- Dimension type: `aoa3:creeponia`.
- Declared type fields: `logical_height=256`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:creep_stone`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Acreeponia) (10 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Acreeponia) (13 dimension-tagged entries).

### Crystevia

Comparison key: `aoa3:crystevia`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-crystevia.webp" width="160" height="160" alt="1.16.5 Crystevia Realmstone source-item study">

**1.16.5 entry note:** Interact with a living Case Construct while holding the Deep Crystal block item. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#crystevia).

**1.12.2 declaration:** `DIM_CRYSTEVIA` selects `WorldProviderCrystevia`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:crystevian_caverns`.
- Dimension type: `aoa3:crystevia`.
- Declared type fields: `logical_height=128`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:crystallised_rock`, fluid `minecraft:air`, sea level `0`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:crystal_caverns`.
- Dimension type: `aoa3:crystevia`.
- Declared type fields: `min_y=0`, `height=384`, `logical_height=128`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:crystallised_rock`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Acrystevia) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Acrystevia) (9 dimension-tagged entries).

### Deeplands

Comparison key: `aoa3:deeplands`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-deeplands.webp" width="160" height="160" alt="1.16.5 Deeplands Realmstone source-item study">

**1.16.5 entry note:** Break an ore-tagged block at Y ≤ 5 while carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#deeplands).

**1.12.2 declaration:** `DIM_DEEPLANDS` selects `WorldProviderDeeplands`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `aoa3:caverns`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:cavern_depths`.
- Dimension type: `aoa3:deeplands`.
- Declared type fields: `logical_height=128`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:dense_stone`, fluid `minecraft:air`, sea level `0`.

#### 1.20.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:the_depths`.
- Dimension type: `aoa3:deeplands`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=128`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:dense_stone`, fluid `minecraft:lava`, sea level `-32`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:the_depths`.
- Dimension type: `aoa3:deeplands`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=128`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:dense_stone`, fluid `minecraft:lava`, sea level `-32`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Adeeplands) (10 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Adeeplands) (10 dimension-tagged entries).

### Dustopia

Comparison key: `aoa3:dustopia`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-dustopia.webp" width="160" height="160" alt="1.16.5 Dustopia Realmstone source-item study">

**1.16.5 entry note:** Activate the Shadow Altar with its Book of Shadows while Night Vision is active and you carry a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#dustopia).

**1.12.2 declaration:** `DIM_DUSTOPIA` selects `WorldProviderDustopia`; its integer ID comes from configuration.

[Prepare the historical eight-lamp shrine and five-phase boss chain](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Primordial-Five-Shrine-and-Phase-Guide-1.12.2).

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:dustopian_forest`.
- Dimension type: `aoa3:dustopia`.
- Declared type fields: `logical_height=256`, `fixed_time=0`, `has_skylight=false`, `has_ceiling=false`, `bed_works=false`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:darkened_rock`, fluid `minecraft:air`, sea level `0`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:the_silent_forest`.
- Dimension type: `aoa3:dustopia`.
- Declared type fields: `min_y=0`, `height=384`, `logical_height=319`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:darkened_rock`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Adustopia) (10 dimension-tagged entries; 5 arena routes) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Adustopia) (13 dimension-tagged entries).

### Gardencia

Comparison key: `aoa3:gardencia`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-gardencia.webp" width="160" height="160" alt="1.16.5 Gardencia Realmstone source-item study">

**1.16.5 entry note:** Drop a Blank Realmstone into a fully grown carrot crop in Precasia, then defeat the Primitive Carrotop it creates. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#gardencia).

**1.12.2 declaration:** `DIM_GARDENCIA` selects `WorldProviderGardencia`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:floral_islands`.
- Dimension type: `aoa3:gardencia`.
- Declared type fields: `logical_height=256`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:aromatic_stone`, fluid `minecraft:water`, sea level `66`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Agardencia) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Agardencia) (9 dimension-tagged entries).

### Greckon

Comparison key: `aoa3:greckon`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-greckon.webp" width="160" height="160" alt="1.16.5 Greckon Realmstone source-item study">

**1.16.5 entry note:** Interact with Elusive while holding Nightmare Flakes and carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#greckon).

**1.12.2 declaration:** `DIM_GRECKON` selects `WorldProviderGreckon`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:greckon_mountains`.
- Dimension type: `aoa3:greckon`.
- Declared type fields: `logical_height=256`, `fixed_time=0`, `has_skylight=false`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:greckon_stone`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Agreckon) (9 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Agreckon) (9 dimension-tagged entries).

### Haven

Comparison key: `aoa3:haven`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-haven.webp" width="160" height="160" alt="1.16.5 Haven Realmstone source-item study">

**1.16.5 entry note:** Kill a Flye with melee in Lelyetia while your player is at Y ≥ 120. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#haven).

**1.12.2 declaration:** `DIM_HAVEN` selects `WorldProviderHaven`; its integer ID comes from configuration.

[Prepare the historical Four Guardians altar and final-color rewards](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Four-Guardians-Altar-and-Rewards-1.12.2).

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `aoa3:floating_islands`.
- Direct biomes (1): `aoa3:haven`.
- Dimension type: `aoa3:haven`.
- Declared type fields: `logical_height=256`, `fixed_time=6000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:weightless_stone`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Ahaven) (10 dimension-tagged entries; 4 arena routes) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Ahaven) (8 dimension-tagged entries).

### Immortallis

Comparison key: `aoa3:immortallis`.

**1.12.2 declaration:** `DIM_IMMORTALLIS` selects `WorldProviderImmortallis`; its integer ID comes from configuration.

This historical code-era realm is outside the inspected 1.16.5 dimension JSON list. Keep its provider, encounters and progression dependencies as a distinct restoration task.

[Follow the historical nine-stage dungeon walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Immortallis-Dungeon-Walkthrough-1.12.2).

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Aimmortallis) (0 dimension-tagged entries; 4 arena routes).

### Iromine

Comparison key: `aoa3:iromine`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-iromine.webp" width="160" height="160" alt="1.16.5 Iromine Realmstone source-item study">

**1.16.5 entry note:** Use a Blank Realmstone on a Mineralization Station. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#iromine).

**1.12.2 declaration:** `DIM_IROMINE` selects `WorldProviderIromine`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:iromine`.
- Dimension type: `aoa3:iromine`.
- Declared type fields: `logical_height=256`, `fixed_time=6000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:irostone`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Airomine) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Airomine) (8 dimension-tagged entries).

### L’Borean

Comparison key: `aoa3:lborean`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-lborean.webp" width="160" height="160" alt="1.16.5 Lborean Realmstone source-item study">

**1.16.5 entry note:** Expose an eligible Gardencian creature to Candied Water, then kill it as a player while carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#lborean).

**1.12.2 declaration:** `DIM_LBOREAN` selects `WorldProviderLBorean`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:coral_fields`.
- Dimension type: `aoa3:lborean`.
- Declared type fields: `logical_height=128`, `has_skylight=true`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:coral_rock`, fluid `minecraft:water`, sea level `127`.

#### 1.20.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:lborean_deep`.
- Dimension type: `aoa3:lborean`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=384`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:coral_rock`, fluid `minecraft:water`, sea level `384`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:lborean_deep`.
- Dimension type: `aoa3:lborean`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=250`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:coral_rock`, fluid `minecraft:water`, sea level `384`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Alborean) (9 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Alborean) (7 dimension-tagged entries).

### Lelyetia

Comparison key: `aoa3:lelyetia`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-lelyetia.webp" width="160" height="160" alt="1.16.5 Lelyetia Realmstone source-item study">

**1.16.5 entry note:** Complete a fall whose event distance is greater than 25 blocks, carrying a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#lelyetia).

**1.12.2 declaration:** `DIM_LELYETIA` selects `WorldProviderLelyetia`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:lelyetian_plains`.
- Dimension type: `aoa3:lelyetia`.
- Declared type fields: `logical_height=256`, `fixed_time=6000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:lelyetian_stone`, fluid `minecraft:air`, sea level `0`.

#### 1.20.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:lelyetian_plains`.
- Dimension type: `aoa3:lelyetia`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:lelyetian_stone`, fluid `minecraft:air`, sea level `-64`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (1): `aoa3:lelyetian_plains`.
- Dimension type: `aoa3:lelyetia`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `has_skylight=false`, `has_ceiling=true`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:lelyetian_stone`, fluid `minecraft:air`, sea level `-64`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Alelyetia) (9 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Alelyetia) (9 dimension-tagged entries).

### Lunalus

Comparison key: `aoa3:lunalus`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-lunalus.webp" width="160" height="160" alt="1.16.5 Lunalus Realmstone source-item study">

**1.16.5 entry note:** Select a Gravitator and move airborne over the void in Haven while carrying a Blank Realmstone in the main inventory. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#lunalus).

**1.12.2 declaration:** `DIM_LUNALUS` selects `WorldProviderLunalus`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `aoa3:asteroids`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:asteroid_belt`.
- Dimension type: `aoa3:lunalus`.
- Declared type fields: `logical_height=256`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=false`, `bed_works=false`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `minecraft:stone`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Alunalus) (5 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Alunalus) (6 dimension-tagged entries).

### Mysterium

Comparison key: `aoa3:mysterium`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-mysterium.webp" width="160" height="160" alt="1.16.5 Mysterium Realmstone source-item study">

**1.16.5 entry note:** Kill a Creepird while your player has Poison and carries a Blank Realmstone. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#mysterium).

**1.12.2 declaration:** `DIM_MYSTERIUM` selects `WorldProviderMysterium`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:fungal_caverns`.
- Dimension type: `aoa3:mysterium`.
- Declared type fields: `logical_height=256`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:fungal_rock`, fluid `minecraft:air`, sea level `10`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Amysterium) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Amysterium) (8 dimension-tagged entries).

### Nowhere

Comparison key: `aoa3:nowhere`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-nowhere.webp" width="160" height="160" alt="1.16.5 Nowhere Realmstone source-item study">

**1.16.5 entry note:** Carry a Blank Realmstone and survive an attack from a Construct of Strength that has Strength active. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#nowhere).

**Arena distinction:** 1.16.5 references dimension type `aoa3:structure`; 1.20.1 declares `aoa3:single_block` with an air block; 1.21.1 declares `aoa3:empty`. Follow the [modern boss-entry guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) and [utility-lobby/token guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1) rather than assuming ordinary terrain exploration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:nowhere`.
- Dimension type: `aoa3:structure`.
- Declared type fields: `logical_height=0`, `fixed_time=6000`, `has_skylight=false`, `has_ceiling=true`, `bed_works=false`, `respawn_anchor_works=false`, `coordinate_scale=1.0`.
- Generator defaults: block `minecraft:air`, fluid `minecraft:air`, sea level `0`.

#### 1.20.1 resource details

- Generator: `aoa3:single_block`; biome source: `direct generator biome`.
- Direct biomes (1): `aoa3:nowhere`.
- Dimension type: `aoa3:nowhere`.
- Declared type fields: `min_y=0`, `height=2032`, `logical_height=319`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=false`, `bed_works=false`, `respawn_anchor_works=false`, `coordinate_scale=1.0`.

#### 1.21.1 resource details

- Generator: `aoa3:empty`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:nowhere`.
- Dimension type: `aoa3:nowhere`.
- Declared type fields: `min_y=0`, `height=2032`, `logical_height=319`, `fixed_time=18000`, `has_skylight=false`, `has_ceiling=false`, `bed_works=false`, `respawn_anchor_works=false`, `coordinate_scale=1.0`.

**Inspect the matching roster:** [1.21.1 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&dimension=aoa3%3Anowhere) (0 dimension-tagged entries; 10 arena routes).

### Precasia

Comparison key: `aoa3:precasia`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-precasia.webp" width="160" height="160" alt="1.16.5 Precasia Realmstone source-item study">

**1.16.5 entry note:** Craft a Blank Realmstone with one each of the six vanilla 1.16.5 saplings: oak, birch, spruce, jungle, acacia and dark oak. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#precasia).

**1.12.2 declaration:** `DIM_PRECASIA` selects `WorldProviderPrecasia`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:precasian_tall_forest`.
- Dimension type: `aoa3:precasia`.
- Declared type fields: `logical_height=256`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:precasian_lower_rock`, fluid `minecraft:air`, sea level `0`.

#### 1.20.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (13): `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`.
- Dimension type: `aoa3:precasia`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:precasian_stone`, fluid `minecraft:water`, sea level `62`.

#### 1.21.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (13): `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`.
- Dimension type: `aoa3:precasia`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:precasian_stone`, fluid `minecraft:water`, sea level `62`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Aprecasia) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Aprecasia) (9 dimension-tagged entries) · [1.20.1 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&dimension=aoa3%3Aprecasia) (11 dimension-tagged entries) · [1.21.1 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&dimension=aoa3%3Aprecasia) (13 dimension-tagged entries).

### Precasia backup resource

Comparison key: `aoa3:precasia_backup`.

This backup-named resource is present only in the selected 1.20.1 data. It references the Precasia dimension type and noise settings. No separate ordinary travel route is inferred from its name.

#### 1.20.1 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:multi_noise`.
- Direct biomes (13): `aoa3:precasian_caves`, `aoa3:precasian_deadlands`, `aoa3:precasian_desert`, `aoa3:precasian_forest`, `aoa3:precasian_jungle`, `aoa3:precasian_ocean`, `aoa3:precasian_plains`, `aoa3:precasian_river`, `aoa3:precasian_savannah`, `aoa3:precasian_shore`, `aoa3:precasian_tall_forest`, `aoa3:precasian_tar_pits`, `aoa3:precasian_volcano`.
- Dimension type: `aoa3:precasia`.
- Declared type fields: `min_y=-64`, `height=384`, `logical_height=319`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:precasian_stone`, fluid `minecraft:water`, sea level `62`.

**Inspect the matching roster:** [1.20.1 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&dimension=aoa3%3Aprecasia_backup) (11 dimension-tagged entries).

### Runandor

Comparison key: `aoa3:runandor`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-runandor.webp" width="160" height="160" alt="1.16.5 Runandor Realmstone source-item study">

**1.16.5 entry note:** Place a Vox Light in Mysterium, drop a Blank Realmstone and one Runic Energy above it, then use an Active Rune Stone on the light. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#runandor).

**1.12.2 declaration:** `DIM_RUNANDOR` selects `WorldProviderRunandor`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:runic_cliffs`.
- Dimension type: `aoa3:runandor`.
- Declared type fields: `logical_height=256`, `has_skylight=true`, `has_ceiling=false`, `bed_works=true`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:runic_stone`, fluid `minecraft:water`, sea level `15`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Arunandor) (9 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Arunandor) (7 dimension-tagged entries).

### Shyrelands

Comparison key: `aoa3:shyrelands`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-shyrelands.webp" width="160" height="160" alt="1.16.5 Shyrelands Realmstone source-item study">

**1.16.5 entry note:** Craft Darkly Powder, Bloodstone, Glowstone, Haunted Flower, Magic Mending Solution and a Blank Realmstone together. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#shyrelands).

**1.12.2 declaration:** `DIM_SHYRELANDS` selects `WorldProviderShyrelands`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:shyre_remnants`.
- Dimension type: `aoa3:shyrelands`.
- Declared type fields: `logical_height=256`, `fixed_time=10000`, `has_skylight=true`, `has_ceiling=false`, `bed_works=false`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:bright_rock`, fluid `minecraft:air`, sea level `0`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Ashyrelands) (11 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Ashyrelands) (13 dimension-tagged entries).

### Vox Ponds

Comparison key: `aoa3:vox_ponds`.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-vox_ponds.webp" width="160" height="160" alt="1.16.5 Vox Ponds Realmstone source-item study">

**1.16.5 entry note:** Interact with an AoA trader or banker in Creeponia using the Blank Realmstone while environmentally protected. [Full conditions and restrictions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5#vox-ponds).

**1.12.2 declaration:** `DIM_VOX_PONDS` selects `WorldProviderVoxPonds`; its integer ID comes from configuration.

#### 1.16.5 resource details

- Generator: `minecraft:noise`; biome source: `minecraft:fixed`.
- Direct biomes (1): `aoa3:vox_wastes`.
- Dimension type: `aoa3:vox_ponds`.
- Declared type fields: `logical_height=256`, `has_skylight=false`, `has_ceiling=false`, `bed_works=false`, `respawn_anchor_works=true`, `coordinate_scale=1.0`.
- Generator defaults: block `aoa3:polluted_stone`, fluid `minecraft:water`, sea level `14`.

**Inspect the matching roster:** [1.12.2 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&dimension=aoa3%3Avox_ponds) (8 dimension-tagged entries) · [1.16.5 bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&dimension=aoa3%3Avox_ponds) (11 dimension-tagged entries).

## Vanilla dimensions and the full travel loop

AoA additions to the Overworld, Nether and End are separate from this custom-dimension census. Use the [loot/modifier reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Loot-Tables-and-Global-Modifiers-1.21.1), [mining guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mining-and-Ore-Generation-1.21.1) and [Nethengeic Pit route](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Ledger-1.21.1#nethengeic-look-for-the-pits-encounter-area) for those additions.

A complete realm still needs its entry/acquisition path, generator and biomes, structures, mobs/NPCs/bosses, resources, recipes/loot, hazards, atmosphere, death/respawn and return travel to work together. Validate multiplayer, saved chunks and cross-version migration against the exact target build; do not convert a source-file count into runtime acceptance.

## Evidence and credits

[Released dimension-resource graph and legacy registration instructions](https://herbertofury.github.io/Advent-of-Ascension/dimension-resource-atlas-evidence.json) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist).

Checked 2026-10-17. Original documentation for the owner’s Enderloom project. AoA is created by Tslat and contributors. No game or Java/mod code was executed for this atlas.
