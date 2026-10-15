# Legacy creature and model atlas

**301 source-derived Java model portraits**, accompanied by **151 official geometry-resource previews** across the 1.16.5 and 1.20.1 artifacts. These counts overlap across releases and include non-living entity resources; they are not a claim of 452 distinct mobs.

Models/textures are by **Tslat and contributors**. Every entry preserves its source generation and mapping evidence. Full-size legacy PNGs are available by clicking the lightweight thumbnails.

## Java-coded 1.16.5 models

- [Legacy model gallery 1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-1)
- [Legacy model gallery 2](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-2)
- [Legacy model gallery 3](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-3)
- [Legacy model gallery 4](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-4)
- [Legacy model gallery 5](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-5)
- [Legacy model gallery 6](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-6)
- [Legacy model gallery 7](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-7)
- [Legacy model gallery 8](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Gallery-8)

The strict constructor adapter converted 335 of 343 inspected Java model classes, checking that every literal box and parent relationship was accounted for. Of those, 301 had unique texture mappings and were rendered. The Bone Creeper adapter follows its verified zero-delta constructor delegation. Other inherited, procedural, shared-texture and custom-rendered classes remain separately tracked.

## Official geometry resources

- [1.16.5 geometry gallery: 42 pairs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Geometry-Gallery-1.16.5)
- [1.20.1 geometry gallery: 109 pairs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Geometry-Gallery-1.20.1)

These pair model geometry and textures from the same official release JAR. They include creatures absent from the Java-constructor pass, such as Kror, Coratee and the Corrupted Traveller. An exact geometry-plus-texture hash permits reuse of an identical rendered showcase across releases without rerunning Blender.

## What these images establish

The images show the actual source/artifact geometry in a static reference pose. They do not prove runtime animation, exact render scaling, shader behavior, gameplay registration or a completed Enderloom port. Variant textures and intentional invisible models must not be mistaken for removed content.

The modern [interactive Model Observatory](https://herbertofury.github.io/Advent-of-Ascension/) can inspect compatible geometry resources from a local official JAR. Java-coded models are represented by the static galleries until a dedicated interactive adapter is finished.

## 1.12.2 source-mapped entity portraits

[Browse the 1.12.2 entity atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Atlas-1.12.2): 467 mapped model/texture presentations across 447 source entity IDs, including variants and non-living resources. Thirteen galleries include source-model and renderer links; remaining inherited/procedural mappings are listed explicitly. These are reference renders, not proof of a playable conversion.

## Procedural constructor supplement: Shiny Squid

![Shiny Squid constructor rest pose](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-shiny-squid-constructor.png)

**Shiny Squid · `aoa3:shiny_squid` · 1.16.5 reference.** A dedicated adapter expands the model's eight-iteration tentacle loop: one body plus eight tentacles, with the source positions and Y rotations. The 64×32 texture comes from the official 3.6.11 JAR. This adds one procedural-constructor showcase beyond the original 301 literal-model portraits.

[Model constructor](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/client/model/entity/animal/ShinySquidModel.java) · [Renderer texture selection](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/client/render/entity/animal/ShinySquidRenderer.java). Tentacles are shown at constructor rest, without swimming animation. Standard documentation lighting does not reproduce the original fullbright shader or runtime body rotations. Original model and texture by Tslat and contributors.
