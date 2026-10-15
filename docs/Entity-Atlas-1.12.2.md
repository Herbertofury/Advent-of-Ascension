# Entity atlas · 1.12.2

**533 mapped model/texture presentations across 509 source entity IDs.** The original 467 presentations are joined by 31 inherited-model portraits and 35 miscellaneous/variant presentations. Counts include texture variants and non-living entity resources. These are additional generation-specific references, not a count of distinct mobs added to Enderloom.

The literal importer converted 411 of 415 inspected model classes after adding explicit ModelBox support. Renderer registrations establish source IDs and shared/variant texture mappings. Missing inherited models and unresolved renderers remain open.

- [Gallery 1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-1)
- [Gallery 2](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-2)
- [Gallery 3](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-3)
- [Gallery 4](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-4)
- [Gallery 5](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-5)
- [Gallery 6](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-6)
- [Gallery 7](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-7)
- [Gallery 8](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-8)
- [Gallery 9](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-9)
- [Gallery 10](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-10)
- [Gallery 11](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-11)
- [Gallery 12](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-12)
- [Gallery 13](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Gallery-1.12.2-13)

[Machine-readable portrait provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/entity-portraits-1.12.2.json) records each entity ID, model, texture, evidence path and image URL.

## Inherited-model supplement

[Thirty-one additional inherited biped/zombie portraits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Inherited-Model-Gallery-1.12.2) use constructor geometry read from the official Minecraft client, with AoA renderer mappings and textures.

## Miscellaneous and renderer variants

[Thirty-five additional miscellaneous and variant presentations](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Misc-Entity-Gallery-1.12.2) resolve misc/eggless registrations, Automaton colors and the default Runicorn model.

## Remaining renderer mappings

7 entries still require another mapping or model adapter. No placeholder is counted as a completed preview.

- `aoa3:boss_item`: No single explicit model, literal texture or registry ID
- `aoa3:creep_cow`: Model inherited, procedural or not converted
- `aoa3:fake_tnt`: No single explicit model, literal texture or registry ID
- `aoa3:friendly_creeper`: No single explicit model, literal texture or registry ID
- `aoa3:lotto_totem`: No single explicit model, literal texture or registry ID
- `aoa3:occult_block`: No single explicit model, literal texture or registry ID
- `aoa3:sea_spider`: Model inherited, procedural or not converted

## Empty base models

These nine registrations use [ModelNothing](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/model/entities/misc/ModelNothing.java), whose constructor and render methods contain no geometry. They are not failed cuboid renders. Custom effects or other renderer behavior need separate treatment; this does not prove the whole entity is invisible in game.

- `aoa3:ambient_pixon`
- `aoa3:blooming_pixon`
- `aoa3:glaring_pixon`
- `aoa3:gleaming_pixon`
- `aoa3:glistening_pixon`
- `aoa3:glowing_pixon`
- `aoa3:radiant_pixon`
- `aoa3:shadow`
- `aoa3:shining_pixon`
