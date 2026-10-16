# Source findings and restoration fixes

Concrete implementation findings discovered while building the atlas. Static evidence is kept separate from reproduced gameplay defects. Do not mark a fix complete without a target build and test result.

## Coratee texture path helper · 1.20.1

**Status: corrected in the owner-local Forge 1.20.1 candidate; actual default native texture resolution passes. Focused variant/visual/lifecycle acceptance remains open.**

The complete source recipe retains the original model/animation body and corrects the texture-getter role. The accepted native client actually resolves `aoa3:textures/entity/animal/lborean/coratee_default.png` from `CorateeModel`. [Exact candidate/resource evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/development/coratee-current-evidence.json). This supersedes the earlier static-only status; it does not claim the commented-out 1.21 class was enabled.

The official AoA 3.7.1 JAR's typed `CorateeModel.getTextureResource` method invokes `buildFormattedModelPath` at bytecode offset 16. The pinned AoA source contains the same call. GeckoLib's 1.20.1 implementation formats that helper as a `geo/...geo.json` path, whereas its texture helper formats a `textures/...png` path. A texture lookup therefore appears to receive a geometry-style resource path.

- [Exact class-bytecode evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/coratee-texture-bytecode-evidence.json), read without executing mod code.
- [Pinned AoA model source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/model/entity/animal/CorateeModel.java).
- [Pinned GeckoLib 1.20.1 path helpers](https://github.com/bernie-g/geckolib/blob/7d6f32db9168a24e14b327c0ad9f8f87dfc204de/Forge/src/main/java/software/bernie/geckolib/model/DefaultedGeoModel.java).

The inspected AoA artifact declares GeckoLib 4.3 or later. The helper source above is a pinned 1.20.1 branch reference, not a claim that every allowed dependency release was tested. The newer inspected AoA 1.21 branch comments out the entire Coratee model class; that is a separate version state, not proof that the 1.20.1 defect was fixed.

### Proposed correction and acceptance tests

- [x] Verify the selected native model resolves a PNG through the exact target GeckoLib texture helper in the accepted client.
- [x] Correct the getter to the texture-path helper while retaining every original variant expression and model/animation body.
- [ ] Confirm default and overgrown variants resolve existing PNG resources from the same artifact/version.
- [ ] Test adult and baby appearance, animation, resource reload and save/load.
- [ ] Check missing-texture/error logs and compare an actual in-game screenshot with the atlas reference.
- [ ] Confirm the fix does not accidentally activate content intentionally disabled on another source branch.
- [ ] Publish a patch and test receipt; propose an upstream contribution if the issue remains relevant there.

This finding does not certify a visual failure in a running game. The atlas can render the two real textures independently because it selects documented resources directly; successful atlas images do not establish that the game's texture-selection method works.

## Documentation renderer quality gate

The two-sided thin-surface correction is already applied to the published preview images and has a separate [validation record](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/planar-render-validation.json). It changes the offline documentation renderer, not AoA game code.


## Roaming trader coordinate bounds · official 1.20.1 and 1.21.1 references

Released-bytecode checks confirm that the inspected official trader callers pass 20/64, but their coordinate helper adds the 44-block width again to each signed offset. A +22 axis draw becomes +66; this exceeds the named maximum without proving a successful in-game spawn. The helper moved between classes across the inspected versions, so source layouts are not interchangeable.

[Illustrated geometry audit and unchecked repair/acceptance steps](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Roaming-Trader-Spawn-Geometry). The published current Enderloom inventory reports a different trader-class hash; that neither proves the issue remains nor that it is fixed. Inspect the exact current candidate before patching. No gameplay patch or FPS gain is claimed by this audit.

## Ammo Void Pouch rejection can remove stored data · 1.21.1

**Status: verified released-code null-handling path; no current Enderloom runtime reproduction or applied fix claimed.** The component add helper returns null for patched ammunition or exhausted capacity. Its click caller compares identity, then passes null to the component setter instead of rejecting the deposit. The standard setter removes component data; the checked NeoForge supplier bridge forwards null unchanged. Existing stored counts are at risk, and later unguarded component access can fail.

[Player preparation guide, precautions and acceptance checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ammunition-and-Void-Pouch-1.21.1) · [Released class hashes, exact method bytes and six independent regression-model cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/ammo-pouch-rejection-evidence-1.21.1.json). Preserve the pouch and cursor on rejected input, add defensive handling for a missing component, and test the exact target build before marking a repair complete. This finding is scoped to AoA 3.7.16.1 / Minecraft 1.21.1; it is not a claim that the private 1.20.1 candidate contains the same code.

## Stasis Capsule clears stored data after an unchecked insertion · 1.21.1

**Status: released-code finding; no current Enderloom runtime reproduction or applied fix claimed.** The release method calls `addFreshEntity`, discards its boolean result, then clears the stored entity component. A rejected world insertion can therefore lose access to the cached creature. Collision and null-recreation checks already exist, but do not cover this separate step. The checked NeoForge entity-manager path can reject a canceled join event or failed UUID insertion.

[Creature transport tutorial and acceptance checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Stasis-Capsule-Creature-Transport-1.21.1) · [Exact released methods and four independent state-transition cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/stasis-capsule-release-evidence-1.21.1.json). Preserve the payload until insertion succeeds, verify serialization before capture discards the original, and test ownership/protection semantics. This evidence is scoped to AoA 3.7.16.1 / Minecraft 1.21.1, not every historical implementation.


## Thorny Plant survival scan stops at Y=0 · 1.21.1

**Status: released-code boundary finding; no live-game reproduction or current Enderloom repair claimed.** MultiBlockCrop.canSurvive stops its downward soil scan when `posY - i < 0`, even though modern worlds can extend below zero. A Thorny Plant whose supporting farmland is below Y=0 cannot reach that farmland through this scan. The checked class also fixes the growth height at three and stages per part at five.

[Practical farming guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Farming-Soils-and-Harvesting-1.21.1) · [Released class hash, exact method bytes and source evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/farming-evidence-1.21.1.json). Inspect the exact target implementation, replace the hardcoded zero boundary with the world's actual minimum build-height semantics if applicable, and test soil below, at and above Y=0 plus the real world floor. Preserve upper-part validation, bonemeal, neighbor updates and final-growth behavior. This is an unchecked repair target, not an applied game patch.


## Fishing Cage retrieval counts storage slots, not occupied catches · 1.21.1

**Status: selected released-bytecode and source finding; no live-game reproduction or private Enderloom fix claimed.** `getLoot()` always returns a three-element array. The interaction uses its length for both durability cost and the Hauling time-budget multiplier whenever the first catch slot is non-empty. One, two or three occupied slots therefore all enter the three-wear path. A fresh 15-durability cage is not returned after its fifth such retrieval.

[Illustrated cage guide and eighteen catch previews](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Cage-Walkthrough-1.21.1) · [Released methods and four independent array-length cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/fishing-cage-evidence-1.21.1.json). Decide explicitly whether wear and XP should follow occupied slots, then test zero/one/two/three catches, final durability, full inventories, owner availability and save/reload. Preserve the exact target build's behavior until a deliberate change is validated. Inventory transfer mutates item-stack references; a second delivery-related method alone does not establish duplication.

## Hauling trap location wrapper routes to the normal pool · 1.21.1

**Status: exact released-bytecode dispatch finding; no live-game reproduction or current Enderloom patch claimed.** `HaulingSpawnPool.getTrapsPoolForLocation` and `getPoolForLocation` have identical method bytes and both call `getPoolForBiome`. A separate `getTrapsPoolForBiome` exists, but this wrapper does not call it. The released FishingTrapSpawn ability calls the trap-named location wrapper. The two shipped six-entry trap definitions therefore do not prove this path uses their intended pools.

[Player-facing rod and pool guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hauling-Rods-and-Fishing-Pools-1.21.1) · [Released class hashes, exact methods, six pool definitions and four independent dispatch cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/hauling-rods-evidence-1.21.1.json). Inspect the exact target candidate, route the trap wrapper to the trap-biome lookup if applicable, and test water/lava, default and biome overrides, missing pools, skill eligibility, cancellation and registry lifecycle. This is a concrete repair target, not a claim of an applied fix or a measured performance gain.

## Mending Table unsupported material can retain an old output · 1.21.1

**Status: exact released-code update branch and independent arithmetic finding; no in-game reproduction or private Enderloom fix claimed.** Once a target is damaged and the material slot is non-empty, both supported-material identity checks can fail and jump directly to return. That path does not reset the previous output or `totalRepairCost`. The inherited update callback runs this handler and broadcasts changes; an unsupported non-empty update with a prior result is therefore a stale-preview test target. Actual slot gestures may pass through an empty update first, so this is not a claim that every swap reproduces the problem.

[Illustrated repair guide and player precautions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1) · [Released branch target, parent/output-slot paths and eight independent repair cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mending-table-evidence-1.21.1.json). Reset output and cost on all invalid paths, revalidate atomically at extraction, and test click/swap/quick-move, changed target, empty material, tiny durability values and close/reopen. Keep component-preserving copies and ordinary material costs. No game patch or performance improvement is claimed by this documentation.

## Rune station batch splitting and post-consumption loot conditions · 1.21.1

**Status: selected released-code findings with independent arithmetic/equipment-state models; no game reproduction or private Enderloom patch claimed.** RuneCreationTask repeatedly constructs `min(64, count)` rather than using the remaining count. A target of 66 therefore constructs two 64-item stacks in the inspected loop. RuneRandomizer reduces the submitted stack before generating loot; its two table conditions inspect equipment, not an input snapshot. A final input may leave neither pool eligible, while a different source in the other hand may select another pool or make both eligible.

[Illustrated modern rune guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rune-Production-and-Current-Limits-1.21.1) · [Released evidence, seven batch cases and six equipment cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/rune-production-evidence-1.21.1.json). Use remaining-count stack construction and input-snapshot pool selection where intended, then test exact quantity conservation, both hands, last item, Creative, luck, rejected spawns and scheduled-task lifecycle. Verify actual station acquisition separately; registration and archive models do not prove survival availability.
