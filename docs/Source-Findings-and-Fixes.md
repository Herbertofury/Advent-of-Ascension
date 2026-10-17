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

## Tea Sink melon output and Creative additive selection · 1.21.1

**Status: exact released-field selection and helper branch, plus eight independent state cases; no in-game reproduction or private Enderloom fix claimed.** The melon path consumes Nature Melon Slice but assigns that same item as its output, rather than Natural Tea. The inspected class contains no NATURAL_TEA field reference. Separately, Creative supplies amount zero to the additive-consumption helper, which returns true before searching inventory. Once Cup and Tea Shreddings checks pass, this selects Fungal Tea even without Mystic Shrooms.

[Illustrated brewing guide and player precautions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Tea-Sink-Brewing-and-Ingredient-Priority-1.21.1) · [Released methods, recipes and selection cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tea-sink-evidence-1.21.1.json). If consistent with intended behavior, return Natural Tea from the melon path and separate additive presence checks from Creative consumption cost. Test both additives, neither, hands/inventory, missing prerequisites, full inventory, water depletion/refill and Cup return after drinking. Preserve unrelated station behavior and validate the exact target build before marking either fix complete.

## Infused Press tier range and signed-count overflow · 1.21.1

**Status: selected released arithmetic/codec branches and eight independent quantity cases; no live save failure or private Enderloom patch claimed.** CompressedItemData's saved-data codec permits tiers 1–18, while the compression matcher rejects a next-tier computed count only when negative. The helper uses floating-point power/rounding and signed-long multiplication. A maximum-stack-16 tier-19 calculation wraps positive in the independent model, so this sign check does not enforce the codec boundary.

[Illustrated press operating reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infused-Press-Compression-and-Piston-Control-1.21.1) · [Exact selected methods, codec call and quantity cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/infused-press-evidence-1.21.1.json). Validate the next tier against the serialized range before creating output, use checked integer arithmetic, and test accepted/rejected boundaries plus save/load and client sync for supported stack sizes. Keep existing low-tier contents/components intact. Station acquisition and piston event timing require independent target-build validation.

## Divine Station upgrades use configured outputs · 1.21.1

**Status: released base-recipe behavior, not an unconditional modpack-loss claim or applied preservation patch.** UpgradeKitRecipe's assembly method does not read input stack data; it returns the configured output's copy. All 36 inspected declarations specify only output item ID and count. Input enchantments, names, damage and stored casts are not automatically transferred by that base method. The parent menu also invokes crafting events, so integrations can alter or cancel results.

[All illustrated upgrade routes and precautions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Divine-Station-Weapon-Upgrades-1.21.1) · [Released recipe/menu evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/upgrade-kit-evidence-1.21.1.json). If preservation is desired in the restoration, define which compatible components transfer instead of copying obsolete weapon stats wholesale. Test preview accuracy, component compatibility, exact consumption, quick move and canceled/modified crafting events in the target build. Keep stock conversion behavior distinguishable from an intentional new policy.

## Rage synchronization and Battle Vulcane recipient · 1.21.1

**Status: released-class call/data-flow evidence and bounded arithmetic models; no in-game reproduction or owner-local patch claimed.** Rage damage/drain handlers write the value directly without the setter’s dirty flag, while the selected incremental resource collector gates serialization on that flag. Near-zero positive Rage can also cross below zero in the selected drain subtraction. Separately, Battle Vulcane’s released Strength-effect call passes the hit entity as target and the user as source.

[Eight-variant guide, exact evidence and runtime acceptance cases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-and-Rage-1.21.1). Reproduce post-sync damage/drain and compare server value with the client meter; confirm intended effect recipient before changing it. Prefer the existing clamping and dirty-marking path if a fix is warranted, without adding repeated scans. Preserve resource exemptions, capacity, targeting, save/client behavior and existing owner-local fixes. These observations apply to AoA 3.7.16.1, not automatically to the private 1.20.1 candidate.

## Throwable consumption before spawn success · 1.21.1

**Status: selected released base-method ordering and bounded success/rejection models; no in-game loss reproduction or private candidate patch claimed.** AoAThrowableWeapon consumes before projectile creation. Its entity-insertion rejection branch skips success callbacks but still returns a projectile reference, and the caller’s statistic/cooldown path checks non-null rather than the insertion result. No refund appears in these selected methods.

[Eight-weapon guide and exact creation/spawn evidence](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Throwable-Weapons-1.21.1). Test constructor failure, canceled/rejected insertion, ordinary success, last-stack items, exemptions and multiplayer. If correcting the transaction, prevent both lost inventory and duplicate projectiles and place success feedback after the intended commit boundary. Test hand and dispenser paths separately; their context construction is different.

## Melee property-helper routing · 1.21.1

**Status: 68 released registration traces and selected helper-method evidence; no in-game reproduction or private candidate patch claimed.** The five Maul factories’ overload chain supplies approximately -3.46667 to the eventual extra-damage argument and zero to the attack-speed argument. Pluton Scythe’s one-argument factory request resolves an inherited Greatblade helper, not its separate two-argument Luck helper. Rock-Pick Sword and Troll-Basher Axe also forward positive tool-tier speed into their selected melee helper; preserve those released inputs until intended behavior is established.

[Complete melee inputs, eight repair-tag references and targeted acceptance cases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Melee-Weapons-and-Property-Routing-1.21.1). Verify equipped attributes, attack cadence, reach, knockback, special effects, repairs and multiplayer in the exact build before changing helper signatures or routing. The guide distinguishes tier damage input, its stored minus-one bonus and later helper arguments instead of presenting intended-looking values as measured combat results.

## Skill Helmet cosmetic ownership and selection · 1.21.1

**Status: released method and factory traces; no multiplayer defect reproduced or private candidate patch claimed.** All twelve base/trim routes for the six registered Skill Helmets resolve to their intended selected layer factories. Both model and texture selection read the local `ClientPlayerDataManager` skill instance. Model trim additionally requires the rendered entity to be a Player; texture trim does not have the equivalent entity gate in the inspected method.

- [ ] Establish whether cosmetic ownership is intended to follow the wearer or viewer, then test local/remote players with opposite skill levels.
- [ ] Test supported non-player wearers while the viewer is at level 1000; verify that geometry and texture select the same variant.
- [ ] Test 999 → 1000, resource reload, reconnect and changes of viewed entity; preserve cached model reuse.
- [ ] Verify equip/unequip and reconnect do not accumulate the Skill Helmet's +0.5 XP modifier. Keep XP sources that ignore buffs separate.
- [ ] If selection changes are warranted, share one bounded variant decision between model and texture paths and use existing synchronized skill/equipment state; avoid repeated registry or inventory scans during rendering.

The stock level setter clamps 0–1000, so the `>=1000` versus `==1000` comparison alone does not establish a stock reachable mismatch. [Illustrated models, XP interpretation and acceptance matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Armor-and-Skill-Helmets-1.21.1) · [Exact released selection evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skill-helmet-selection-evidence-1.21.1.json).

## Frame Bench selector bounds and dynamic recipes · 1.21.1

**Status: released menu/slot methods and 32 exact armor Infusion definitions inspected; no in-game crash or private candidate patch claimed.** Ten frame choices are menu-driven. The display-only FrameBenchRecipe returns a null serializer, so a JSON-only recipe census misses frame production. One output-take callback consumes one Scrap Metal. The inspected clickMenuButton assigns a changed selection and refreshes output without an explicit range guard before the later selection-array access.

- [ ] Validate selection bounds and preserve the ten current options; do not assume the client screen is the only possible caller.
- [ ] Verify normal take, repeated take, shift-click, empty input, full inventory, close/disconnect and reopen without duplication or input loss.
- [ ] Keep client buttons, menu selection, display recipes and any future data-driven extensions aligned without repeated registry scans.

[Illustrated preparation and eight full-set shopping lists](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1) · [Exact released evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/frame-bench-and-armor-infusion-evidence-1.21.1.json). Other armor acquisition paths remain separate work; absence from the 32 Infusion outputs is not proof of unavailability.

## Skill Master acquisition and the missing tier-five course record

Minecraft 1.21.1 / AoA 3.7.16.1 static audit adds ten released Skill Master offer definitions to the previous 45-offer modern catalog: four Skill Crystals and six Skill Helmets. The utility-lobby template contains the canonical NPC; this is a distinct route from roaming traders. [Illustrated acquisition guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1) · [Released methods and resource hashes](https://herbertofury.github.io/Advent-of-Ascension/skill-master-acquisition-evidence-1.21.1.json).

Six tier reward tables and six parkour activity choices ship, but the inspected registry resources contain only five parkour-course records: tiers 1, 2, 3, 4 and 6. The checked course lookup returns failure when no matching course exists. A tier-five reward table therefore does not establish a playable tier-five route. This is a static completeness finding, not an observed game failure or a change to the private current candidate.

Acceptance work: verify target-build entry and safe return, utility-lobby generation/NPC presence, all ten offers, completion versus death/exit reward gates, explicit tier-five handling, full-inventory delivery, discounts/restocking and reconnect persistence. Retain real item IDs and saves. Do not silently treat missing content as completed or grant reward tables without their intended course.

## Armor tooltip versus callback scope · 1.21.1

The checked 3.7.16.1 archive supplies 100 tooltip lines across all 48 ordinary armor sets. The [illustrated activation guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1) separates those descriptions from nine callback-level interpretations and preserves 194 released set methods plus 13 shared equipment/damage methods.

Alacrity’s partial-set `handleIncomingDamage` method checks absence of `FULL_SET` and installs an armor-stage reduction using `equippedPieces.size × 0.2`, without a fall-source guard in that method. Its tooltip says fall resistance; the full-set invulnerability callback does check `IS_FALL`. This is a static scope mismatch, not a reproduced combat failure or a fix applied to the private current candidate.

Acceptance: test one, two, three and four pieces with fall and non-fall damage; include compatible helmets and equipment requirements. Decide intended behavior before changing either code or tooltip. Preserve item/save identities and event-driven equipment tracking. Measure actual damage and performance rather than treating tooltip percentages as final damage reductions. [Released route audit](https://herbertofury.github.io/Advent-of-Ascension/armour-effect-route-audit-1.21.1.json).

## Full armor-route review: external effects and unresolved activation

All 48 ordinary sets now have a release-scoped source review, with 194 set methods, 24 shared equipment/damage methods, four selected external methods and 14 attribute modifier definitions retained. A one-pass scan of 2,014 class files found direct material-field routes outside armor classes for Ghoulish (blaster Spirit cost), Hydrangic (crop placement) and Nightmare (rune payment). This bounded scan does not prove absence of tag-driven, item-ID, reflected or external-mod paths.

- **Ghastly scan frequency:** released branch offset 6 jumps to offset 31 on a nonzero `tickCount % 5`; offset 32 calls `isCrouching`, and a true result still reaches the entity search. The method does not enforce a universal five-tick throttle. Profile crouching behavior, then make an explicit interval gate only if that matches intended responsiveness and effect refresh. No measured FPS loss or fix is claimed.
- **Biogenic underwater behavior:** the full-set/in-water branch calls `setAirSupply(-10)` while its tooltip promises underwater breathing. Retain this as an acceptance target; no drowning outcome is inferred without the exact engine and hooks.
- **Rosidian and Spaceking:** their classes declare constructor/tooltip methods with no local summon callbacks. No external direct material-field activation was found in this scan. Their summoning promises remain unresolved rather than being marked implemented.
- **Nightmare:** the rune-payment adjustment requires buffs enabled and the full set; Distortion Rune is removed, while the armor subtraction clamps other rune costs to at least one before later ammo-cost changes.
- **Purity:** existing-effect cleanup on equip and future-effect rejection have different full-set gates. **Hydrangic:** the 16 passed to `hurtArmor` is damage input, not a guaranteed durability decrement per piece.
- **Damage categories:** the ranged helper excludes magic, energy and gun-tagged projectile damage. Do not promise that a ranged-armor effect applies to all guns.

[Full illustrated reviews](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1) · [External material-reference scan](https://herbertofury.github.io/Advent-of-Ascension/external-armour-routes-1.21.1.json) · [Exact route audit](https://herbertofury.github.io/Advent-of-Ascension/armour-effect-route-audit-1.21.1.json). All findings are static documentation evidence; private-current-candidate behavior and runtime performance remain separately tested concerns.
