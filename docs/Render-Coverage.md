# Render Coverage

[Visual atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Visual-Atlas)

## Current verified documentation status · 2026-10-16

Counts below describe inspected rosters and documentation, not a playable merged Enderloom build. They supersede older intermediate appearance counts later on this page.

| Selected release | Inspected roster | Current appearance result |
|---|---:|---|
| 1.12.2 / 3.3.6 | 525 source-mapped classes | 513 static-body entries; three dynamic references; nine particle/empty-body cases |
| 1.16.5 / 3.6.11 | 419 living-source entries | 409 body portraits; eight particle previews; Shadow invisible; Doppelganger player-skin behavior |
| 1.20.1 / 3.7.1 | 285 living-source entries | 107 portraits/resource studies; 178 explicit renderer-gap/target-mismatch explanations |
| 1.21.1 / 3.7.16.1 | 83 living-source entries | All 83 have source-mapped static portraits; selected variants and state galleries included |

The 1.20.1 picture count includes nine released NPC atlas diagnostics and a Coratee intended-texture study. They are labeled clearly, not presented as repaired runtime rendering. Zero unclassified entries in an inspected roster does not establish a complete runtime registry.

- [1.16.5 appearance census](Legacy-Bestiary-Coverage-1.16.5)
- [1.20.1 appearance census and variants](Bestiary-Coverage-1.20.1)
- [Nine released NPC texture-atlas mismatches and proposed repairs](NPC-Texture-Atlas-Mismatch-1.20.1)
- [Modern portraits](Modern-Bestiary-Portraits)
- [Historical realmstone progression: 22 routes](Realmstone-Progression-Walkthrough-1.16.5)
- [Practical modern skill training](Skill-Training-Walkthrough-1.21.1)

The searchable bestiary supports release, dimension and biome-selector filters, exact creature links, 787 modern artifact stat-builder records, and lazy illustrated loot. Reverse drop lookup links items back to creatures. Selected-release loading avoids fetching every roster at startup, with caching, retry and stale-result tests.

The recipe explorer covers **6,781 definitions**: 1,172 on 1.12.2; 2,296 on 1.16.5; 1,781 on 1.20.1; 1,532 on 1.21.1. Dynamic recipes are explained separately rather than flattened into invented fixed recipes. Ten modern skill data files and all 201 default ability records now match the inspected released artifact semantically.

## Verified input artifacts

Four official JAR downloads were checked against their advertised SHA-512 hashes: 1.12.2 / 3.3.6, 1.16.5 / 3.6.11, 1.20.1 / 3.7.1 and 1.21.1 / 3.7.16.1. Complete source archives for five pinned branches were downloaded for read-only inspection. No JAR code was executed.

## Initial modern image generation pass

- **118** entity-resource models produced textured rest-pose previews from the 1.21.1 JAR.
- **2328 / 2371** localized item/block entries produced nonblank previews.
- **54** entries needed custom mapping or a renderer adapter in the initial pass. Supplements below resolve several of these; this is not the current outstanding total.
- A 24-frame Smash turntable shows the model from all sides. It is a camera orbit, not a mob animation.
- Subsequent passes cover historical inventories, Java-coded legacy entities, inherited geometry, crops and dynamic reference studies. See the dated categories below and the Progress page for current evidence.

## Accuracy boundaries

This is an independent showcase renderer, not Minecraft framebuffer capture. Lighting is standardized; rest poses omit animation state. Item overrides, animated texture timing, biome tint, emissive overlays, multipart block states, custom item renderers and runtime-selected texture variants are not all reproduced. Flat items stay flat/pixel-extruded instead of being redesigned as invented volumetric objects. Automated nonblank checks and contact-sheet review do not establish pixel-exact game-render parity.

Source resource directories can contain unused, duplicate or unfinished-looking models. For example, modern Skeletron and Tyrosaur resources must not be mistaken for verified legacy appearances or complete boss implementations. Use the version matrix and implementation evidence.

## Initial-pass exceptions (superseded where supplements exist)

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

## Supplemental 1.12.2 source edge cases

[Seven supplemental inventory previews](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Asset-Edge-Cases) cover the remaining candidates from the 2,466-record localization/model join. The initial six texture-alias diagnostics were subsequently narrowed: three Skeletron statues resolved after zero-area faces were skipped before texture lookup. Filtration System, its active form and Iropole still contain positive-area faces with undefined aliases. Shyre Cloud has a source-alpha translucent reference. Diagnostic handling and its limits are explicit. These supplement the original 2,459 regular previews and do not certify a complete runtime registry or target renderer.

## 1.12.2 entity renderer mapping pass

467 model/texture presentations across 447 source entity IDs are documented in the [1.12.2 entity atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Atlas-1.12.2). This includes variants and non-living resources, not 467 distinct mobs. The importer converted 411 of 415 inspected model classes; 78 renderer entries still need inherited, procedural or nonliteral mapping work. Two invulnerability-aura-only textures were excluded from body portraits.

All 13 current contact sheets were visually reviewed. Geometry/texture-identical portraits reuse existing 1.16.5 image URLs; 205 new unique pairs add 410 full-size/thumbnail files. Lossless WebP exports preserve exact RGBA bytes for full-size images. These remain static source references; animations, render layers, world scaling and target gameplay are not certified.

## Artifact-derived spawn egg colors

The two vanilla-template Skeletron egg previews now use color arguments read from the official 1.21.1 JAR builder calls. All 82 extracted builder palettes matched the pinned source declarations. Custom-painted egg textures remain unchanged. [Validation record](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/spawn-egg-color-validation.json). No mod code was executed.

## Additional source mapping coverage

The [modern mapping supplement](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Additional-Model-Mappings-1.21.1) adds 19 presentations: 11 actively source-mapped fish variants and eight explicitly labeled unused/historical resource studies. Together with the 118 initial previews, this illustrates 137 model/texture presentations across 128 distinct modern geometry resources. The original filename-only unresolved table above is retained as the initial-pass record; these supplements supersede its mapping gaps for Gemtrap, Skipper, Stripefish, Coratee, Boneback, Bugeye, Goalby, Night Reaper, Nightfly and Sea Troll. Trickster still lacks its texture in the inspected JAR. Unused studies are not counted as active gameplay.

The [1.16.5 variant supplement](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Shared-Model-Variants-1.16.5) adds 17 source-mapped fish and Dryad Sprite appearances beyond the initial 42 geometry/texture pairs. These are variants, not 17 newly implemented mobs.

## Thin-surface rendering correction

Zero-thickness fins, wings and similar model parts now render as one two-sided surface with separate front/back UV coordinates. This removes coincident-face black artifacts without editing original assets. 127 unique model/texture pairs were rerendered and reviewed across six contact sheets, updating 175 public image files. A synthetic red/blue-sided fixture verified that opposite sides retain their own texture region. [Validation details](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/planar-render-validation.json). This is a documentation-renderer correction, not an in-game mod change.

## Extended 1.12.2 coverage

The inherited-model, miscellaneous-registration and special-model passes raise the 1.12.2 atlas to **537 presentations across 513 source entity IDs**. Three identified dynamic item/effect renderers have separate illustrated reference studies, with runtime effects still unverified; nine additional registrations use an empty base model rather than missing cuboid geometry. Variant/effect resources are included, so these figures are not a living-mob count. The [entity atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Atlas-1.12.2) separates all three categories.

## Dynamic fluid containers

[Fluid and bucket references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fluid-and-Bucket-References) supply 21 source-defined first-frame studies for the Forge dynamic bucket cases: 18 on 1.16.5 and three on 1.20.1. Core and integration-conditional registrations are distinguished. This closes their missing-documentation-picture gap while retaining runtime rendering and animation verification as open work.

## Historical entity census classification

All 525 entity classes identified by the 1.12.2 renderer census are classified with source evidence: 513 have static model/texture portraits, three have dynamic item/effect studies, and nine have [particle or invisible-body documentation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Particle-and-Invisible-Entities-1.12.2). The classification audit reports zero unmatched entries within that census. It does not certify complete runtime registries, animations or a playable conversion.

## Historical growth-state completion

The age-only blockstate pass now covers 388 historical states across 49 version-specific plant records: 134 on 1.20.1, 126 on 1.16.5 and 128 on 1.12.2. Combined with 134 modern states, the [growth guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crops-and-Growth-Stages) has 522 presentations across 66 version-specific plant records. Every defined state in this age-only subset resolved; this does not establish all multipart states or gameplay growth behavior.

## Sign block-entity models

[15 sign-form previews across 12 block identities](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Signs-and-Hanging-Signs-1.21.1) resolve the standing, wall, wall-hanging and attached/unattached ceiling-hanging forms of Baobab, Lucalus and Stranglewood. Literal vanilla layer factories, AoA wood textures and source visibility rules are used. Six wall-only IDs intentionally have no independent inventory item. Text and runtime interactions remain separate validation work.

## Modern NeoForge fluid containers

The [bucket reference gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fluid-and-Bucket-References) also covers three 1.21.1 containers using the pinned NeoForge loader/mask and exact tint constants read from AoA 3.7.16.1. This brings the gallery to 24 version-specific studies. These are first-frame documentation views, not runtime shader certification.

## Translucent and intentionally empty resource cases

[Source asset edge cases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Asset-Edge-Cases) now include three later-release Shyre Cloud studies retaining the texture’s alpha 77/255. It also distinguishes invisible helper blocks, empty-model functional blocks, unverified custom item models and unqualified localization/resource candidates from missing active content.

## Searchable inventory and multi-state reconciliation

The [Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html) indexes all **10,077 version-specific archive-resource candidates**: 9,928 regular source-model previews and 149 separately classified initial exceptions. This is not a runtime registry count. Each exception links to an existing supplement or preserves the exact remaining limitation. [Record-by-record ledger](Inventory-Preview-Resolution-Ledger).

The [multi-state supplement](Multi-State-Block-References) accounts for 135 Thorny Plant age/height states and six activity-portal axis states across three releases. Of the plant states, 93 have visible texture regions and 42 have verified fully transparent UV regions. These supplement the 522 earlier age-only references; they do not establish natural state transitions or world renderer parity.

## Independently verified 1.20.1 sign models

[15 matching-version sign references](Signs-and-Hanging-Signs-1.20.1) resolve six previously pending wall-sign reference records. Official layer factories were decoded independently, visibility conditions checked, and released AoA textures compared byte-for-byte before reuse. This does not certify text, interaction or world placement in a running game.
