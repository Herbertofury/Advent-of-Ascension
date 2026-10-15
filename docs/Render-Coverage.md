# Render Coverage

[Visual atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Visual-Atlas)

## Verified input artifacts

Four official JAR downloads were checked against their advertised SHA-512 hashes: 1.12.2 / 3.3.6, 1.16.5 / 3.6.11, 1.20.1 / 3.7.1 and 1.21.1 / 3.7.16.1. Complete source archives for five pinned branches were downloaded for read-only inspection. No JAR code was executed.

## Current image generation coverage

- **118** entity-resource models produced textured rest-pose previews from the 1.21.1 JAR.
- **2328 / 2371** localized item/block entries produced nonblank previews.
- **54** entries still require custom mapping or a renderer adapter.
- A 24-frame Smash turntable shows the model from all sides. It is a camera orbit, not a mob animation.
- Only the modern 1.21.1 release has this first complete render pass. Earlier releases have been acquired, but their Java-coded model adapters and galleries remain unfinished.

## Accuracy boundaries

This is an independent showcase renderer, not Minecraft framebuffer capture. Lighting is standardized; rest poses omit animation state. Item overrides, animated texture timing, biome tint, emissive overlays, multipart block states, custom item renderers and runtime-selected texture variants are not all reproduced. Flat items stay flat/pixel-extruded instead of being redesigned as invented volumetric objects. Automated nonblank checks and contact-sheet review do not establish pixel-exact game-render parity.

Source resource directories can contain unused, duplicate or unfinished-looking models. For example, modern Skeletron and Tyrosaur resources must not be mistaken for verified legacy appearances or complete boss implementations. Use the version matrix and implementation evidence.

## Still unresolved

| Entry | Reason |
|---|---|
| Air Gap · `aoa3:air_gap` | custom renderer or unsupported model without elements |
| Ashfern · `aoa3:ashfern_crop` | assets/aoa3/models/item/ashfern_crop.json |
|  · `aoa3:banner_extension` | custom renderer or unsupported model without elements |
| Baobab Wall Hanging Sign · `aoa3:baobab_wall_hanging_sign` | custom renderer or unsupported model without elements |
| Baobab Wall Sign · `aoa3:baobab_wall_sign` | custom renderer or unsupported model without elements |
| Bubble Berries · `aoa3:bubble_berry_crop` | assets/aoa3/models/item/bubble_berry_crop.json |
| Candied Water · `aoa3:candied_water` | custom renderer or unsupported model without elements |
| Chilli · `aoa3:chilli_crop` | assets/aoa3/models/item/chilli_crop.json |
| Eye Bulbs · `aoa3:eye_bulb_crop` | assets/aoa3/models/item/eye_bulb_crop.json |
| Floracles · `aoa3:floracles_crop` | assets/aoa3/models/item/floracles_crop.json |
| Goldicaps · `aoa3:goldicaps_crop` | assets/aoa3/models/item/goldicaps_crop.json |
| Green Manure · `aoa3:green_manure` | assets/aoa3/models/item/green_manure.json |
| Heart Fruit · `aoa3:heart_fruit_crop` | assets/aoa3/models/item/heart_fruit_crop.json |
| Killzone · `aoa3:killzone` | custom renderer or unsupported model without elements |
| Living Growth · `aoa3:living_growth` | '' |
| Lucalus Wall Hanging Sign · `aoa3:lucalus_wall_hanging_sign` | custom renderer or unsupported model without elements |
| Lucalus Wall Sign · `aoa3:lucalus_wall_sign` | custom renderer or unsupported model without elements |
| Luna Globes · `aoa3:luna_globe_crop` | assets/aoa3/models/item/luna_globe_crop.json |
| Lunacrike · `aoa3:lunacrike_crop` | assets/aoa3/models/item/lunacrike_crop.json |
| Lunalons · `aoa3:lunalon_crop` | assets/aoa3/models/item/lunalon_crop.json |
| Magic Marangs · `aoa3:magic_marang_crop` | assets/aoa3/models/item/magic_marang_crop.json |
| Mystic Shrooms · `aoa3:mystic_shroom_crop` | assets/aoa3/models/item/mystic_shroom_crop.json |
| Portal · `aoa3:nowhere_activity_portal` | assets/aoa3/models/item/nowhere_activity_portal.json |
| Rosidons · `aoa3:rosidon_crop` | assets/aoa3/models/item/rosidon_crop.json |
| Shyre Cloud · `aoa3:shyre_cloud` | blank render |
| Stranglewood Wall Hanging Sign · `aoa3:stranglewood_wall_hanging_sign` | custom renderer or unsupported model without elements |
| Stranglewood Wall Sign · `aoa3:stranglewood_wall_sign` | custom renderer or unsupported model without elements |
| Tar · `aoa3:tar` | custom renderer or unsupported model without elements |
| Tea · `aoa3:tea_crop` | assets/aoa3/models/item/tea_crop.json |
| Thorny Plant · `aoa3:thorny_plant_crop` | assets/aoa3/models/item/thorny_plant_crop.json |
| Toxic Waste · `aoa3:toxic_waste` | custom renderer or unsupported model without elements |
| Trilliads · `aoa3:trilliad_crop` | assets/aoa3/models/item/trilliad_crop.json |
| Candied Water Bucket · `aoa3:candied_water_bucket` | assets/neoforge/models/item/bucket.json |
| Compressed Item · `aoa3:compressed_item` | custom renderer or unsupported model without elements |
| Creature Essence · `aoa3:creature_essence` | empty geometry |
| Discovery · `aoa3:discovery` | assets/aoa3/models/item/discovery.json |
| Expedition · `aoa3:expedition` | assets/aoa3/models/item/expedition.json |
| Lessons · `aoa3:lessons` | assets/aoa3/models/item/lessons.json |
| Primitive · `aoa3:primitive` | assets/aoa3/models/item/primitive.json |
| Raw Herring · `aoa3:raw_herring` | assets/aoa3/models/item/raw_herring.json |
| Tar Bucket · `aoa3:tar_bucket` | assets/neoforge/models/item/bucket.json |
| The Portal · `aoa3:the_portal` | assets/aoa3/models/item/the_portal.json |
| Toxic Waste Bucket · `aoa3:toxic_waste_bucket` | assets/neoforge/models/item/bucket.json |
| Gemtrap · `gemtrap` | requires renderer-specific texture mapping |
| Skipper · `skipper` | requires renderer-specific texture mapping |
| Stripefish · `stripefish` | requires renderer-specific texture mapping |
| Coratee · `coratee` | requires renderer-specific texture mapping |
| Boneback · `boneback` | requires renderer-specific texture mapping |
| Bugeye · `bugeye` | requires renderer-specific texture mapping |
| Goalby · `goalby` | requires renderer-specific texture mapping |
| Night Reaper · `night_reaper` | requires renderer-specific texture mapping |
| Nightfly · `nightfly` | requires renderer-specific texture mapping |
| Sea Troll · `sea_troll` | requires renderer-specific texture mapping |
| Trickster · `trickster` | requires renderer-specific texture mapping |

## Reproduction and provenance

The public gallery contains rendered showcases and original viewer code, not a downloadable collection of original AoA textures, models or JARs. Open an official local JAR in the interactive viewer to inspect the source geometry without uploading it.

Advent of Ascension models/textures by **Tslat and contributors**. These are independently rendered documentation showcases from **AoA 3.7.16.1 / Minecraft 1.21.1**, not Enderloom runtime screenshots. [Official mod](https://modrinth.com/mod/adventofascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki).

## Historical inventory pass

The historical galleries add **7,600 version-specific inventory preview records** across 161 named sheets:

| Minecraft / AoA | Rendered records | Candidate records | Mapping scope |
|---|---:|---:|---|
| 1.20.1 / 3.7.1 | 2,503 | 2,544 | Artifact localization and item models |
| 1.16.5 / 3.6.11 | 2,638 | 2,696 | Artifact localization and item models |
| 1.12.2 / 3.3.6 | 2,459 | 2,466 | Unique normalized localization/model joins; registry identity not independently certified |

These are records across releases, not unique content counts. Missing custom renderers, intentional invisible blocks, non-inventory block states and unresolved model mappings remain tracked. The 1.12.2 candidate set is not an assertion that every runtime registry entry was recovered.

[Historical gallery index](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Galleries). All 32 historical wiki pages were compared against their generated Markdown after publication.

## Legacy models and growth-stage supplements

- **301 Java-model portraits** from pinned 1.16.5 source constructors paired with official 3.6.11 textures, with full-size PNGs and lightweight thumbnails. All 602 image files were verified against their Git blob hashes after upload.
- **151 official geometry/texture pairs**: 42 from the 1.16.5 artifact and 109 from 1.20.1, displayed across seven named sheets. All were visually reviewed; 126 reused a previously rendered byte-identical geometry/texture pair.
- **134 growth-stage images across 17 plants**, taken from the age variants in the 1.21.1 artifact. These are separate block-state views, not additional item counts.

[Legacy model atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Atlas) · [Growth stages](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crops-and-Growth-Stages).

Exact constructor accounting and static-image review do not establish animation, custom renderer scaling, gameplay registration or target runtime compatibility. Outstanding variant mappings, procedural/inherited models and older 1.7.10 binary acquisition remain open.
