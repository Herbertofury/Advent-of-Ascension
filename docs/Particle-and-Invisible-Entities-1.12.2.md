# Particle and invisible-body entities · 1.12.2

The nine registrations using ModelNothing are not nine missing creature meshes. Eight Pixons deliberately render particles; Shadow has no body cuboids in its selected renderer. This page explains their source-defined presentation without inventing replacement bodies.

## Eight Pixons · source particle appearances

![Eight Pixon colors and five particle atlas cells](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-pixon-particle-studies.webp)

[AoAPixonRenderer](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/render/entities/AoAPixonRenderer.java) overrides rendering to spawn a Flickering Fluffy particle at the entity position plus 0.65 on Y. It passes a color, scale argument 150, lifespan modifier 3 and texture-index offset 5. The [factory](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/particles/FlickeringFluffyTrailParticle.java) divides the scale argument by 100, then applies randomized particle size and brightness. The picture shows source tint at full intensity for legibility; it is a texture-cell study, not a frozen game frame or a volumetric model.

The particle uses 8-pixel cells in row 4 of the official AoA particle sheet. The displayed progression uses columns 7 through 3, following its age-dependent index expression before expiry. The initial pre-update/default index, expired-particle frame and exact frame durations are not simulated. Actual particles vary in size, lifetime, motion and brightness and face the camera.

| Entity | Source color |
|---|---|
| Ambient Pixon | White |
| Blooming Pixon | Purple |
| Glaring Pixon | Brown |
| Gleaming Pixon | Cyan |
| Glistening Pixon | Green |
| Glowing Pixon | Red |
| Radiant Pixon | Black |
| Shining Pixon | Orange |

Colors are explicit in [renderer registrations](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/render/entities/EntityRenders.java) and [Enums.RGBIntegers](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/library/Enums.java). The [particle registry](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/common/registration/ParticleRegister.java) identifies the texture atlas. [Machine-readable evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/pixon-reference-evidence.json) records the atlas hash, cell coordinates and tint values.

<!-- pixon-card-links-start -->
### Open a Pixon’s illustrated card

The [released renderer audit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pixon-visual-evidence-1.12.2.json) now verifies all eight color assignments through the actual registration factories. Each card includes a clearly labelled particle-cell reference and its checked harvest/conversion route.

| Pixon | Card and source-cell preview |
|---|---|
| [Ambient Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aambient_pixon) | [![Source-cell reference for Ambient Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-ambient_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aambient_pixon) |
| [Blooming Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ablooming_pixon) | [![Source-cell reference for Blooming Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-blooming_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ablooming_pixon) |
| [Glaring Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglaring_pixon) | [![Source-cell reference for Glaring Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-glaring_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglaring_pixon) |
| [Gleaming Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agleaming_pixon) | [![Source-cell reference for Gleaming Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-gleaming_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agleaming_pixon) |
| [Glistening Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglistening_pixon) | [![Source-cell reference for Glistening Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-glistening_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglistening_pixon) |
| [Glowing Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglowing_pixon) | [![Source-cell reference for Glowing Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-glowing_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aglowing_pixon) |
| [Radiant Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aradiant_pixon) | [![Source-cell reference for Radiant Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-radiant_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aradiant_pixon) |
| [Shining Pixon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashining_pixon) | [![Source-cell reference for Shining Pixon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-particle-shining_pixon.webp)](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashining_pixon) |

[Pixon harvesting, bowl recipes, rewards and stone conversion](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2). The individual grids show all eight cells in atlas row 4 for inspection, rather than a simulated animation. They add useful references without changing the count of recovered body meshes.
<!-- pixon-card-links-end -->

## Shadow · no body model, then a different creature

[ShadowRenderer](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/client/render/entities/mobs/overworld/ShadowRenderer.java) uses ModelNothing and returns no texture. Its superclass render path may still contribute standard effects such as a ground shadow or name rendering; absence of body cuboids alone does not mean absolutely no visible pixels in every game state.

[EntityShadow](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/mobs/overworld/EntityShadow.java) creates an EntityShade on the server when its death behavior runs. The image below is **Shade, the resulting creature**, not an invented Shadow body:

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ShadeModel.png" width="256" alt="Shade, the distinct creature created by Shadow's death behavior">

The 1.12.2 atlas reuses this preview only after exact geometry/texture matching. Its 1.16.5 image filename does not relabel the source evidence. See the [historical atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Entity-Atlas-1.12.2) and portrait provenance for the 1.12.2 mapping.

## Coverage audit

All **525 entity classes identified by this renderer-mapping census** are now classified: 513 have 537 static model/texture presentations, three use documented dynamic item/effect renderers, and nine use empty base geometry with the behavior described here. There are zero unclassified entries within that census. This is not proof that every possible runtime registry entry or animation has been recovered.

[Coverage audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/entity-reference-coverage-1.12.2.json) · [Dynamic entity references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dynamic-Entity-References-1.12.2)

AoA artwork, source and designs by Tslat and contributors. These independent documentation studies do not establish target-game behavior or renderer parity.
