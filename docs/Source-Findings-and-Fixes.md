# Source findings and restoration fixes

Concrete implementation findings discovered while building the atlas. Static evidence is kept separate from reproduced gameplay defects. Do not mark a fix complete without a target build and test result.

## Coratee texture path helper · 1.20.1

**Status: static mismatch confirmed; in-game reproduction and fix pending.**

The official AoA 3.7.1 JAR's typed `CorateeModel.getTextureResource` method invokes `buildFormattedModelPath` at bytecode offset 16. The pinned AoA source contains the same call. GeckoLib's 1.20.1 implementation formats that helper as a `geo/...geo.json` path, whereas its texture helper formats a `textures/...png` path. A texture lookup therefore appears to receive a geometry-style resource path.

- [Exact class-bytecode evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/coratee-texture-bytecode-evidence.json), read without executing mod code.
- [Pinned AoA model source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/model/entity/animal/CorateeModel.java).
- [Pinned GeckoLib 1.20.1 path helpers](https://github.com/bernie-g/geckolib/blob/7d6f32db9168a24e14b327c0ad9f8f87dfc204de/Forge/src/main/java/software/bernie/geckolib/model/DefaultedGeoModel.java).

The inspected AoA artifact declares GeckoLib 4.3 or later. The helper source above is a pinned 1.20.1 branch reference, not a claim that every allowed dependency release was tested. The newer inspected AoA 1.21 branch comments out the entire Coratee model class; that is a separate version state, not proof that the 1.20.1 defect was fixed.

### Proposed correction and acceptance tests

- [ ] Verify the helper behavior in the exact GeckoLib version selected for the target build.
- [ ] Replace the model-path helper with the texture-path helper, or return the explicit correct texture resource path.
- [ ] Confirm default and overgrown variants resolve existing PNG resources from the same artifact/version.
- [ ] Test adult and baby appearance, animation, resource reload and save/load.
- [ ] Check missing-texture/error logs and compare an actual in-game screenshot with the atlas reference.
- [ ] Confirm the fix does not accidentally activate content intentionally disabled on another source branch.
- [ ] Publish a patch and test receipt; propose an upstream contribution if the issue remains relevant there.

This finding does not certify a visual failure in a running game. The atlas can render the two real textures independently because it selects documented resources directly; successful atlas images do not establish that the game's texture-selection method works.

## Documentation renderer quality gate

The two-sided thin-surface correction is already applied to the published preview images and has a separate [validation record](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/planar-render-validation.json). It changes the offline documentation renderer, not AoA game code.
