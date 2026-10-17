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

## Petal Crafting acquisition and registry migration boundaries

The [illustrated three-release Petal Crafting guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Petal-Crafting-and-Hydrangic-Armor) follows the actual station interaction and separates retained resources from working acquisition. Both inspected 1.16.5 and 1.20.1 releases include the five-color shapeless Petals recipe. Their entity loot references number six and five respectively. The inspected 1.21.1 archive has no matching Petals recipe or small-petal loot references, and explicitly hides the six petal items from recipe viewers, while retaining the station interaction and Garden Castle template.

All three castle templates contain one station at local (13, 12, 13). Historical 1.16.5 includes the configured structure, template pool, Floral Islands start and Gardencia placement resources. No matching Garden Castle worldgen JSON link was found in the two newer archives by this scan. A retained template does not establish a playable modern survival route.

The historical leggings ID is `aoa3:hydrangic_legs`; the newer inspected versions use `aoa3:hydrangic_leggings`. Preserve that distinction in links and require an explicit save-migration/alias decision when porting. Do not silently rename existing saved content.

One qualifying non-creative station interaction consumes one Petals item and chooses one armor piece; duplicates are possible. The modern delivery helper tries inventory insertion and a player-targeted dropped-item fallback, so its ignored boolean is not evidence of ordinary full-inventory item loss. Acceptance still needs resource acquisition, all four outcomes, delivery, reconnect and farming-effect checks in the target build.

[Released interaction/resource evidence](https://herbertofury.github.io/Advent-of-Ascension/petal-crafting-evidence.json). No game execution or private current-candidate parity is claimed.

## Historical gun inventory accounting and spawn acceptance · 1.12.2

The released AoA 3.3.6 audit adds four target-build checks. These findings do not assert that the current private Enderloom candidate still has the same code.

- **Multi-stack exact payment:** `ItemUtil.findInventoryItem` reuses the original requested amount for each matched stack while decrementing foundCount. A matching `[2, 2]` inventory with a request of 3 removes 4 in the independent model. Introduce a remaining-request counter, stop at zero, and preserve the no-partial-loss behavior when unique stock is insufficient.
- **Physical-stack identity:** the selected main-hand stack can also be encountered through main inventory. Deduplicate references before counting; tests must compare physical inventory counts rather than only the boolean return.
- **Projectile acceptance:** the base gun caller discards spawnEntity's boolean result after its ammunition call. Define and test failure handling for payment, gun durability, use statistics and cooldown instead of assuming a constructed projectile was accepted by the world.
- **Per-impact console output:** the inspected base impact method calls System.out.println(target). Consider removing or gating this diagnostic after checking its purpose, then profile log volume and frame/tick timing. This is a performance candidate, not a measured speedup or permission to drop functional behavior.

The player-facing [firing and ammunition guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2) includes the 16-bullet recipe, hand/attack-strength gates and the distinction between 45 inherited base ammo methods and 33 overrides. [Evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gun-firing-evidence-1.12.2.json) records 40 released methods and 201 independent matching-stack models. Preserve Creative, metadata/NBT, hand selection, subclass and multiplayer behavior when implementing a fix; no gameplay patch or runtime acceptance is claimed here.


## Historical staff rune payment: opposite-hand marker consumption

Minecraft 1.12.2 / AoA 3.3.6, released ItemUtil.findAndConsumeRunes: collection records OFF_HAND as −1 and MAIN_HAND as −2, while consumption fetches MAIN_HAND for −1 and OFF_HAND for −2. With a non-rune staff in main hand and a sufficient required rune stack in offhand, this leads to an unsafe RuneItem cast of the staff. This is a static control-flow finding, not a reproduced game crash or a claim about the current private Enderloom build.

- [ ] Bind collection and consumption to the same physical stack; de-duplicate hand/inventory aliases.
- [ ] Validate the complete bill before mutation; cover insufficient runes, partial stacks, mixed types and both hands.
- [ ] Preserve Creative bypass and the distinct allowBuffs, Greed, Archmage and Nightmare branches.
- [ ] Test precondition failure before payment and cast/spawn failure after payment, wear and cooldown.

[Staff preparation and exact caveats](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Runes-Casting-and-Hand-Safety-1.12.2) · [Released method and registration evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-staff-inputs-1.12.2.json).



## Historical blaster payment and wear boundaries

Minecraft 1.12.2 / AoA 3.3.6. The selected Soul Spark and Light Spark impact paths call Energy and Soul consumers before verifying that the shooter still holds the same weapon, and discard both consumer return values. Their zero ordinary registration inputs do not establish free or harmless impacts. The ordinary blaster base path also has distinct initial-use and Creative tick preflights, remaining-count modulo timing, and accumulated durability arguments on tick/stop.

- [ ] Validate the held weapon and full resource transaction before committing a Spark effect; test denied consumption and mid-flight hand changes.
- [ ] Test both Spark exemptions/immunity and Creative paths separately from the 54 ordinary tick-path users.
- [ ] Test actual callback wear and cancelled effects without treating integer boundary models as a reproduced exploit.
- [ ] Keep first eligible countdown timing distinct from the nominal interval, particularly delays 7, 11, 13 and 14.

[Blaster guide and source-backed caveats](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blaster-Energy-Timing-and-Spark-Exceptions-1.12.2). These are static restoration targets, not a current Enderloom runtime failure claim.



## Historical throwable impact routing and type safety

Minecraft 1.12.2 / AoA 3.3.6: BaseBullet chooses weapon.doImpactDamage when a weapon reference exists, otherwise projectile.doEntityImpact, then calls the common projectile doImpactEffect. Grenade and Runic Bomb contain explosion-helper calls in both projectile hooks, so the weaponless branch must be tested for repeated effect dispatch rather than being conflated with the weapon-bound path. No double-damage runtime result is claimed.

- [ ] Test weapon-bound, weaponless, block-hit and repeated-pierce paths separately, including saved/reloaded projectile state.
- [ ] Guard the Chakram/Goo Ball item-hook EntityLivingBase casts: their successful ranged helper can also accept certain nonliving/multipart targets.
- [ ] Preserve Runic Bomb shield removal and its released high-amplifier slow input without silently flattening them into ordinary damage.
- [ ] Verify explosion destruction policy and target effects independently; strength is not a measured radius.

[Throwable source evidence and practical guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Throwable-Weapons-Impacts-and-Runic-Bombs-1.12.2). These are static restoration targets, not a reproduced current-build failure.



## Historical melee display and parameter distinctions

Minecraft 1.12.2 / AoA 3.3.6: sword material damage bonuses are not final attack damage, and speed operands are attribute modifiers rather than attacks per second. Lunar and Millennium Greatblade attack methods read their incoming baseDmg parameter while the tooltip references a same-named stored minimum field. Goofy Greatblade uses a Gaussian term, not a fixed ±5 interval; Primordial's maximum-health tiers have discontinuous boundaries.

- [ ] Compare displayed values with the selected attack-input method and the later damage pipeline, including configuration changes after construction.
- [ ] Preserve and validate sword/maul capability-backed cooldown handoff when porting.
- [ ] Test the Primordial boundaries at 100/101,300/301 and 1000/1001 before deciding whether to preserve or deliberately rebalance them.

[Greatblade input branches](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Greatblade-Inputs-and-Damage-Branches-1.12.2) · [Sword material inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sword-Materials-and-Attack-Inputs-1.12.2) · [Maul inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Maul-Inputs-Reach-and-Knockback-1.12.2). These are source-level review targets, not a runtime defect certification.


## Historical L’Borean structure-setting mismatch

Minecraft 1.12.2 / AoA 3.3.6 released ChunkGenLBorean.func_185931_b tests drownedLottoStandSpawnChance > 0, then passes aquaticCastleSpawnChance to Random.nextInt for that branch. Defaults are 550 and 1700 respectively. A non-positive castle setting with a positive stand setting can reach a non-positive random bound after the castle guard fails. This is a static exception path, not a reproduced game crash or a statement about the current Enderloom build.

- [ ] Use the stand setting as its own positively checked random bound.
- [ ] Test independent castle/stand flags at negative, zero, one and ordinary positive values, preserving the terrain and else-if conditions.
- [ ] Preserve the five Declogging Table mappings, server-side hand selection, fresh-output policy and give-or-drop-before-shrink sequence deliberately.
- [ ] Resolve survival acquisition of the waterlogged inputs before claiming a complete restoration progression loop.

[Illustrated Declogging Table and configuration guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Declogging-Waterlogged-Weapons-1.12.2) · [Released method evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/declogging-evidence-1.12.2.json). No game files or runtime configuration were changed by this documentation work.

## Banker exchange transaction and GUI safety candidates · 1.12.2

Released AoA 3.3.6 ContainerBankerTrade uses six 20:1 conversion lanes shared by five bankers. Its output onTake callback charges a fixed 20 or 1 input coins and regenerates the preview after a successful quick-move path. A bounded model with one Silver input and space for only one Copper moves one Copper, charges the Silver and overwrites the old nineteen-Copper remainder. This is a source-derived partial-transfer risk candidate, not a reproduced Forge/modpack transaction or a confirmed defect in the current owner-local build.

The same container passes end-exclusive destination ranges [12,47),[39,47),[12,38), omitting container slot 47 or 38 as documented. The server BANKER GUI branch also passes the nearby-entity lookup result directly into a constructor that dereferences it, unlike the client’s local null guard.

- [ ] First compare the current implementation with these old released methods; do not assume parity.
- [ ] Make output delivery and input debit preserve coin value under partial capacity; reject incomplete delivery or correctly preserve paid leftovers.
- [ ] Check complete player-inventory destination ranges, especially slots 38 and 47.
- [ ] Guard missing, removed, out-of-range and stale banker GUI targets on the server.
- [ ] Test ordinary pickup, right-click, shift-click, full/partly filled inventories, close/disconnect, repeated conversion and multiplayer synchronization.
- [ ] Require before/after currency-value conservation and measured performance without capability loss.

[Illustrated banker guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bankers-Coin-Exchange-and-Inventory-Safety-1.12.2) · [Released evidence and 252 bounded models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/banker-exchange-evidence-1.12.2.json). No game files were modified or executed by this documentation work.

## Lotto Totem persistence and placement audit · released 1.12.2

The AoA 3.3.6 custom Lotto Totem NBT callbacks are reversed: readEntityFromNBT writes current UUID fields into the tag; writeEntityToNBT reads keys into the fields. Released bytecode and vanilla callback-dispatch mappings were checked. A bounded callback model loses the custom owner/winner data across a fresh save/load. This is a static finding, not a reproduced runtime session or evidence that the current Enderloom build still contains the defect.

- [ ] Verify the target build; write WinningUUID/OwnerUUID on save and restore them on read. Preserve the base entity UUID used to identify the winning choice.
- [ ] Test all five linked choices through chunk unload, server restart and multiplayer ownership. Define migration for old incomplete groups without inventing owners or winners.
- [ ] Check cancelled/partial spawns: the released item shrinks before five spawn calls and ignores their return values. Confirm appropriate failure/refund behavior.
- [ ] Check overlapping externally created groups: cleanup uses a nearby entity-class box without a group UUID filter.
- [ ] Verify both interaction callbacks before describing the 12000-tick branch as an ownership expiry.

See [the illustrated walkthrough and scoped evidence](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Lotto-Totems-Placement-Rewards-and-Save-Safety-1.12.2).

## Rosidons destination safety · released 1.12.2

The special-dimension height helper accepts at least two exact-air cells above a non-air block, while Rosidons requests feet at that block’s Y+2. A simplified full-solid column with a two-cell cavity overlaps the roof for an assumed 1.8-block standing body. The caller also truncates negative fractional X/Z toward zero for scanning but keeps the original coordinates when teleporting. These are static target-build test candidates, not reproduced current Enderloom defects.

- [ ] Verify destination bounding-box clearance, neighboring columns, safe support and hazards before relocation.
- [ ] Use consistent coordinate conversion; test negative fractions and special dimension scan starts.
- [ ] Verify Ancient Cavern/Immortallis exclusions, server authority and failure consumption/refund behavior.
- [ ] Keep search work bounded; avoid unnecessary chunk generation and measure worst-case scan cost.

See [the illustrated Rosidons safety study](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rosidons-Escape-and-Destination-Safety-1.12.2) for 72 bounded column cases and 12 coordinate examples.


## Movement and void utilities · released 1.21.1 review

[Illustrated equipment and recovery guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Movement-and-Void-Recovery-Utilities-1.21.1) records the released 3.7.16.1 behavior and target-build acceptance checklist. Static candidates: Gravitator's mutable downward scan skips heights, its offhand durability call reports MAINHAND, Distorting Artifact uses fixed Y=257 without a local landing search, and Floating Stone replaces any qualifying dropped stack with one Heavy Boulder. These findings are not private Enderloom runtime defects or completed fixes. Preserve stack/component semantics, use bounded server-side checks and validate custom dimensions and multiplayer before certifying recovery.


## Nowhere boss reward insertion · released 1.21.1 review

The [multiplayer reward guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Nowhere-Boss-Rewards-and-Multiplayer-Scaling-1.21.1) checks four distribution modes and the default health scaling. In the copied partial-stack branch of split distribution, the original stack is reduced before insertion and the failed insertion branch does not reattach or drop the copied remainder. A bounded model retains 800 cases, including 680 with a detached remainder; vanilla inventory insertion was inspected separately. This is a static target-build test candidate, not an observed loss in the private Enderloom build. Preserve item/component conservation through full, partial and failed insertion, test recipient messages independently, and keep allocation event-scoped rather than adding recurring scans.
