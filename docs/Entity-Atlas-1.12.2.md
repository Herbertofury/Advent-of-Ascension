# Entity atlas · 1.12.2

**495 mapped model/texture presentations across 475 source entity IDs.** The original 467 presentations are joined by a 28-portrait inherited-biped supplement. Counts include texture variants and non-living entity resources. These are additional generation-specific references, not a count of distinct mobs added to Enderloom.

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

[Twenty-eight additional inherited biped portraits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Inherited-Model-Gallery-1.12.2) use constructor geometry read from the official Minecraft client, with AoA renderer mappings and textures.

## Remaining renderer mappings

41 entries still require another mapping or model adapter. No placeholder is counted as a completed preview.

- `EntityAgilityTablet`: No single explicit model, literal texture or registry ID
- `EntityAnimaStone`: No single explicit model, literal texture or registry ID
- `aoa3:automaton`: No single explicit model, literal texture or registry ID
- `EntityAwarenessTablet`: No single explicit model, literal texture or registry ID
- `EntityBaneBig`: No single explicit model, literal texture or registry ID
- `EntityBaneClone`: No single explicit model, literal texture or registry ID
- `EntityBaronBomb`: No single explicit model, literal texture or registry ID
- `EntityBloodlust`: No single explicit model, literal texture or registry ID
- `EntityBossItem`: No single explicit model, literal texture or registry ID
- `EntityBreedingTablet`: No single explicit model, literal texture or registry ID
- `EntityCleansingTablet`: No single explicit model, literal texture or registry ID
- `aoa3:clown`: Model inherited, procedural or not converted
- `aoa3:creep_cow`: Model inherited, procedural or not converted
- `EntityDistortionTablet`: No single explicit model, literal texture or registry ID
- `EntityElusiveClone`: No single explicit model, literal texture or registry ID
- `EntityEnergyTablet`: No single explicit model, literal texture or registry ID
- `aoa3:fake_pigman`: No single explicit model, literal texture or registry ID
- `EntityFakeTnt`: No single explicit model, literal texture or registry ID
- `EntityFakeZorp`: No single explicit model, literal texture or registry ID
- `aoa3:friendly_creeper`: No single explicit model, literal texture or registry ID
- `EntityGravityTablet`: No single explicit model, literal texture or registry ID
- `EntityGyrocopter`: No single explicit model, literal texture or registry ID
- `EntityHeartStone`: No single explicit model, literal texture or registry ID
- `EntityLottoTotem`: No single explicit model, literal texture or registry ID
- `aoa3:meganeuropsis`: No single explicit model, literal texture or registry ID
- `EntityOccultBlock`: No single explicit model, literal texture or registry ID
- `EntityOxygenTablet`: No single explicit model, literal texture or registry ID
- `aoa3:phantom`: Model inherited, procedural or not converted
- `EntityPressureTablet`: No single explicit model, literal texture or registry ID
- `EntityProficiencyTablet`: No single explicit model, literal texture or registry ID
- `EntityResistanceTablet`: No single explicit model, literal texture or registry ID
- `aoa3:runicorn`: No single explicit model, literal texture or registry ID
- `EntitySanctityTablet`: No single explicit model, literal texture or registry ID
- `EntitySatiationTablet`: No single explicit model, literal texture or registry ID
- `aoa3:sea_spider`: Model inherited, procedural or not converted
- `EntitySightTablet`: No single explicit model, literal texture or registry ID
- `EntityStrengthTablet`: No single explicit model, literal texture or registry ID
- `EntityTreeSpirit`: No single explicit model, literal texture or registry ID
- `EntityTricksterClone`: No single explicit model, literal texture or registry ID
- `EntityUntiringTablet`: No single explicit model, literal texture or registry ID
- `EntityVitalityTablet`: No single explicit model, literal texture or registry ID

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
