[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Versions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Worlds](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Systems](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Systems) · [Progress](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Progress)

# Progress · what is proven and what remains

**Updated: 2026-10-17 UTC. A private owner-local playable candidate has scoped native/production acceptance; the complete historical/latest merge remains unfinished. No fabricated completion percentage.**

## Current owner-local playable candidate · 2026-10-16

The owner's Desktop Enderloom worktree has now been inspected directly and reconciled with exact local runtime receipts. **Advent of Ascension · Current Playtest** runs on Minecraft 1.20.1 / Forge 47.4.23 / Java 17. Native client/server and ordinary signed-in production rendering/movement plus server save/restart pass. Vanilla hearts remain default. [Current evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/development/current-playtest.json) · [Full runtime checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist) · [Upstream reconciliation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Upstream-Reconciliation).

The exact JAR is `57fd3b10d979e7567dc404b25a90eb38bf8ff6c9ac58b348ba712fa6bd48bca8`, 146,794,782 bytes. The native-client JAR differs only in its manifest build timestamp; all program/resource members match. Full historical/latest parity, remaining Extraction/Anima/deity consumers, all progression, optional compatibility, multiplayer, save migration and performance acceptance remain open. The modified JAR and original AoA files are local, not a new public mod download. Earlier documentation-only observations below are retained as history and are superseded by this section where they describe missing local access.

<!-- current-documentation-status-start -->
## Current documentation at a glance

**Checked 2026-10-17 UTC.** These counts describe source-backed documentation and local documentation checks. They do not extend the separate owner-local runtime acceptance above.

| What you can use | Current coverage | Open it |
|---|---|---|
| Illustrated walkthroughs | 121 version-scoped routes | [Tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html) |
| Item/block reference | 10,133 release-specific resource candidates, with explicit preview limits | [Item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html) |
| Crafting reference | 6,837 recipe definitions; dynamic recipes explained separately | [Recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html) |
| Compact contextual guide index | 559 links across 518 item cards; 947 recipe cards, plus specialist links added directly to newer references |  [Find an item](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html) |
| Equipment | 411 modern weapon references; 204 armor records; 48 ordinary set source reviews | [Armor effects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1) |
| Historical firearm panels | 328 release-specific panels: 172 in 1.12.2, 78 in 1.16.5 and 78 in 1.20.1 | [Historical item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&family=verified) |
| Historical archergun panels | 9 source-checked 1.12.2 arrow-firing weapons | [Ammunition and special effects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Archergun-Ammunition-and-Special-Effects-1.12.2) |
| Historical staff panels | 57 staves, 134 base rune-cost entries, 29 custom casting gates and 800 arithmetic-model cases | [Casting and hand safety](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Runes-Casting-and-Hand-Safety-1.12.2) |
| Historical blaster panels | 56 blasters; 4,144 cost-model and 3,618 timing-model cases | [Energy and Spark exceptions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blaster-Energy-Timing-and-Spark-Exceptions-1.12.2) |
| Historical vulcane panels | 8 revenge-target weapons and 7 additional effects | [Revenge and effects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-Revenge-Targets-and-Effects-1.12.2) |
| Historical throwable panels | 7 weapons, 2 Grenade recipes and branch-specific impact guidance | [Throws and Runic Bombs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Throwable-Weapons-Impacts-and-Runic-Bombs-1.12.2) |
| Historical melee panels | 36 swords, 29 greatblades and 5 mauls, with distinct input labels | [Melee material inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sword-Materials-and-Attack-Inputs-1.12.2) |
| Historical weapon registration coverage | All 412 direct constructors in the checked 1.12.2 WeaponRegister method are matched to cards and portraits | [Exact census](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-weapon-census-1.12.2.json) |
| Illustrated historical weapon tables | 412 inline source-model portraits across 13 family guides | [Historical gun table](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2) |
| Worn armor previews | 48 ordinary set studies plus 18 special/standalone studies | [Armor Atelier](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html) · [Special helmets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Armor-and-Skill-Helmets-1.21.1) |
| Trading | 363 candidate definitions for 1.12.2, 207 for 1.16.5 and 55 for 1.21.1; Herald contexts resolve to four or five offers | [Trading Desk](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html) |
| Modern loot | 1,315 table resources and 25 global modifier definitions | [Loot reference](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1) |
| Local documentation validation | 192 checks passing; not Minecraft game tests | [Test receipt](https://herbertofury.github.io/Advent-of-Ascension/documentation-regression-suite.json) |

### Recent useful additions

- [Herald banner exchanges](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Undead-Herald-Banner-Exchanges-1.12.2): 22 conditional and four common offers, 26 illustrated banners and a realm-aware Trading Desk.
- [Historical farming](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crop-Growth-Planting-and-Harvesting-1.12.2): 16 crops, 128 growth-state previews and checked planting/harvest rules. [Seed acquisition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Finding-Seeds-and-Starting-a-Farm-1.12.2) connects exact recipes, loot references, trades and callbacks while keeping Thorny Plant Seeds unresolved.

- [Resolved historical declarations](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Registered-Blocks-and-Items-1.12.2): 34 restored entries, six crystal-block model repairs and exact-ID aliases that preserve existing links.

- [Historical 1.12.2 guns](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2): 78 exact constructor references, lazy item panels, source portraits, recoil-field behavior and the AoA hardcoreMode damage branch.

- [Historical Exp Flask](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Exp-Flask-Storage-and-Recovery-1.12.2): automatic orb capture, inventory priority, withdrawal tiers, actual empty/filled textures and float storage/capability limits.

- Historical item cards now also connect Soul Tablets, Runation, Pixon harvesting, Infusion crafting and reward boxes to their checked guides: 559 exact links across 518 cards, with an 11,652-byte inline index and no additional requests.

- [Historical realmstone challenges](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-and-Challenges-1.12.2): 23 illustrated destination stones, exact acquisition predicates, two recipes and consumption/timing warnings.

- [Historical skill availability](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Skill-Training-and-Availability-1.12.2): all 15 skill routes, clear inactive/retained limits, and a bounded direct-reference audit across 3,451 released AoA classes.

- [Companion abilities](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Minion-Abilities-and-Choosing-Companions-1.12.2): 22 minion comparisons and bestiary summaries, status effects, healing, utility interactions and movement limits.

- [Creation minions and forge](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Creation-Minions-Slabs-and-Forge-1.12.2): 22 illustrated minions,21 slab recipes, summon/sacrifice values on bestiary cards and checked spawn/ownership test targets.

- [Expedition training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Expedition-Sprinting-Bonuses-and-Falls-1.12.2): grounded sprint timing, three selectable bonuses, twenty XP tiers, fall multipliers and armor/configuration test targets.

- [Hunter requirements and training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2): 71 illustrated released defaults, bestiary level/XP sorting, and distinct attack, death-XP and ordinary-drop checks.

- [Butchery and Innervation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2): temporary pickup models, checked combat gates, Rage criticals, health tiers and displayed-level XP boundaries.

- [Pixon harvest rewards](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2): sixteen illustrated interaction rewards and their XP now open directly inside eight bestiary cards, sharing the existing on-demand loot cache.

- [Historical Runation shrines](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runation-Rune-Shrines-and-Inputs-1.12.2): exact four-post layout, fourteen illustrated tiers, input-rune recipes and destructive practice/post-removal warnings.

- [Exact recipe links](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes): all 6,837 recipe cards can be shared individually; historical enchantment names are clearer and neighboring search matches stay distinct.

- [Historical Infusion crafting and enchanting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-and-Enchanting-1.12.2): all 386 shipped recipes, 37 enchantment families, exact slot layout and visible recipe-browser requirements.











- [Worlds and travel atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions): 24 comparison identities, 22 code-era declarations and exact 21/7/10 data-definition counts, with biome references and travel links kept release-specific.
- The larger how-to coverage now uses **11,652 inline bytes** for inventory links and **8,461 bytes** for recipe links. Common wiki prefixes are stored once; links are decoded once with no extra requests. Existing associations are preserved. These are payload measurements, not measured Minecraft FPS gains.

### What still prevents a “complete AoA” claim

1. Full historical/latest content parity and the remaining Extraction/Anima/deity consumers, as scoped by the owner-local runtime receipts.
2. Authentic 1.7.10 visual coverage and the explicit 1.20.1 renderer/placeholder gaps. Historical reference images are not repaired modern runtime models.
3. Unresolved acquisition and activation routes, including modern Petal progression and the inspected Rosidian/Spaceking summon paths.
4. Target-build acceptance for the recorded source findings, including equipment transitions, storage/delivery, multiplayer, saves, compatibility and measured performance.

[Runtime checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Render limits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage) · [Source findings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes) · [Restoration roadmap](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Roadmap)
<!-- current-documentation-status-end -->

<details><summary>Earlier documentation milestones and receipts · historical counts</summary>

## Tutorial and equipment reference snapshot · 2026-10-17

The [visual tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html) now contains **55 illustrated, release-scoped guides**. **81 local documentation/source-analysis checks pass**; these are not game tests. New equipment panels are lazy, reuse the selected inventory release and do not fetch statistics separately.

- **Crafting route completed in documentation:** [Frame Bench and eight armor Infusion sets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1) links ten menu-driven frame choices, two shapeless preparation recipes and 32 exact Infusion recipes. Full-set totals preserve repeated ingredients and active tags.
- **204 armor references:** 48 four-piece sets and 12 individual pieces, with material inputs, matching-slot links, 11 any-set headpieces and six explicit unbreakable/max-damage overrides. [Armor preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Materials-and-Set-Preparation-1.21.1). [48 neutral worn-armor studies](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Worn-Armor-Gallery-1.21.1) now cover the ordinary sets; [12 custom Skill Helmet variants and six standalone-piece studies](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Armor-and-Skill-Helmets-1.21.1) complete the current armor-registration visual associations. Animation, special-effect walkthroughs and runtime acceptance remain open.
- **411 modern equipment references:** 78 direct guns, 17 shotguns, 50 cannons, 27 snipers, 33 bows, nine crossbows, 57 staves, 56 blasters, eight Vulcanes, eight throwables and 68 melee weapons. [Gun defaults](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Statistics-and-Ammunition-1.21.1), [wrapped gun families](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Shotgun-Cannon-and-Sniper-Statistics-1.21.1), [archery preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bows-and-Crossbows-1.21.1), [illustrated staff rune planner](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Rune-Costs-and-Preparation-1.21.1), [blasters and Spirit recovery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blasters-and-Spirit-1.21.1), [Vulcanes and Rage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-and-Rage-1.21.1), [throwable preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Throwable-Weapons-1.21.1), [melee property routing and repairs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Melee-Weapons-and-Property-Routing-1.21.1). The panel IDs exactly match the 411 registrations in the inspected released AoAWeapons class; this is not a census of every runtime/addon item.
- **156 historical gun references:** 78 each for 1.16.5 and 1.20.1, with constructor recoil kept distinct from the base getter. [Historical comparison](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Gun-Constructor-References).
- **Practical encounter guides:** King BamBamBam’s gold/energy loop, Nethengeic Wither’s aura branches, Tyrosaur’s armour/roar behavior, and six exact Dryad Sprite hoe matches. These preserve unresolved runtime and loot-condition limits.
- **Find and share a route:** ten normal/elite modern boss arena routes are separately labeled in the bestiary’s dimension filter. Inventory, recipe and bestiary filters have shareable links and refuse unsupported releases instead of silently substituting data.
- **Cache correctness:** explorer resource URLs carry content revisions, with release caching and stale-request guards retained. This prevents a freshly published interface from silently receiving the previous dataset under an unchanged URL.

Still open: authentic 1.7.10 asset access, remaining 1.20.1 renderer gaps, additional equipment families and subclass-specific effects, and exact-build runtime validation. Documentation coverage does not close the owner-local merge, migration, multiplayer or performance acceptance work above.

## Current verified documentation status · 2026-10-16

Counts below describe inspected rosters and documentation, not a playable merged Enderloom build. They supersede older intermediate appearance counts later on this page.

| Selected release | Inspected roster | Current appearance result |
|---|---:|---|
| 1.12.2 / 3.3.6 | 525 source-mapped classes | 513 static-body entries; three dynamic references; nine particle/empty-body cases |
| 1.16.5 / 3.6.11 | 419 living-source entries | 409 body portraits; eight particle previews; Shadow invisible; Doppelganger player-skin behavior |
| 1.20.1 / 3.7.1 | 285 living-source entries | 107 portraits/resource studies; 178 explicit renderer-gap/target-mismatch explanations |
| 1.21.1 / 3.7.16.1 | 83 living-source entries | All 83 have source-mapped static portraits; selected variants and state galleries included |

The 1.20.1 picture count includes nine released NPC atlas diagnostics and a Coratee intended-texture study. They are labeled clearly, not presented as repaired runtime rendering. Zero unclassified entries in an inspected roster does not establish a complete runtime registry.

- [1.16.5 appearance census](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Bestiary-Coverage-1.16.5)
- [1.20.1 appearance census and variants](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bestiary-Coverage-1.20.1)
- [Nine released NPC texture-atlas mismatches and proposed repairs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/NPC-Texture-Atlas-Mismatch-1.20.1)
- [Modern portraits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Bestiary-Portraits)
- [Historical realmstone progression: 22 routes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Realmstone-Progression-Walkthrough-1.16.5)
- [Practical modern skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1)

The searchable bestiary supports release, dimension and biome-selector filters, exact creature links, 787 modern artifact stat-builder records, and lazy illustrated loot. Reverse drop lookup links items back to creatures. Selected-release loading avoids fetching every roster at startup, with caching, retry and stale-result tests.

The recipe explorer covers **6,781 definitions**: 1,172 on 1.12.2; 2,296 on 1.16.5; 1,781 on 1.20.1; 1,532 on 1.21.1. Dynamic recipes are explained separately rather than flattened into invented fixed recipes. Ten modern skill data files and all 201 default ability records now match the inspected released artifact semantically.



<!-- practical-coverage-start -->
### Practical walkthrough and navigation coverage

The [visual tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html) now contains **44 version-scoped illustrated walkthroughs**. Recent routes cover rune stations, Ashfern cooking, Tea Sink brewing, Infused Press operation, all 36 shipped weapon-upgrade definitions original-trophy elite progression King BamBamBam’s gold-interception combat loop the Nethengeic Wither’s aura-sensitive damage choices Tyrosaur’s armour/roar mechanics all six Dryad Sprite hoe matches with conditional rewards and 78 released gun-stat references. Acquisition gaps, component behavior and static-analysis limits are stated beside the instructions.

- **156** historical item cards now show independently extracted 1.16.5 / 1.20.1 gun-constructor inputs and literal fire-mode getters. The recoil argument is explicitly separated from the base recoil getter; matching numbers do not imply runtime parity.
- **78** modern item cards now include lazy, version-checked gun-stat panels: damage inputs, tick intervals, durability, firing mode, modifiers and ammunition. These are registered defaults, not measured DPS; wrapped weapon categories remain separate work.
- **250** exact-release item/block cards and **387** recipe cards have contextual how-to links. Eight modern boss cards link directly to the trophy progression guide. Ten modern token/altar arena routes are now separately labelled and included in the bestiary dimension filter without changing natural-spawn fields.
- Item, recipe and bestiary result links preserve selected releases and filters; unsupported releases are not silently substituted in those three browsers. Selected-release caching and lazy pictures remain in place. Inventory, recipe, creature, drop, trade and loot JSON URLs now use dataset-specific content hashes. Changed references receive a fresh cache entry; existing in-page caches, lazy category loading and filter behavior remain intact. No extra manifest request or runtime file hashing is added. [Cache evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/explorer-data-revisions.json).
- **59 passing local documentation/source/UI checks** cover the current build, including a public-metadata snapshot helper that shares one retrieval across audits and respects API cooldowns. These are not Minecraft gameplay tests.
- The guide indexes were compacted without dropping their measured coverage; subsequent additions retain full regression checks. [Recipe-index measurement](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/recipe-guide-compaction-proof.json) · [Current test receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/documentation-regression-suite.json).

Remaining work includes authentic 1.7.10 visual coverage, the explicit 1.20.1 runtime-renderer gaps, unresolved acquisition routes and exact-build acceptance for the recorded source findings. Static previews and tutorial coverage do not mark those game implementation tasks complete. [Visual limits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage) · [Source findings and repair targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes).
<!-- practical-coverage-end -->

## Verified by this documentation pass

- [x] Existing destination repository identified and preserved.
- [x] Published Enderloom AoA requirements located at commit `67a7881`.
- [x] Upstream branches and official release metadata inspected and pinned.
- [x] Cross-version source census created, with comments excluded from registration counts.
- [x] Version, world, skill, combat, conversion and testing guides authored.
- [x] Original documentation artwork and attributed upstream visual references organized.
- [x] Current Desktop Enderloom worktree and accepted generated artifacts reconciled directly with the 2026-10-16 owner-local runtime evidence above.
- [ ] A completed owner-specific AoA build certified by this pass.

## Published visual and recipe deliverables

Initial deliverables verified on 2026-10-15, extended by the current-status section above. Counts are version-specific records, not unique cross-version content or converted gameplay.

- [x] Modern item/block atlas: 2,328 initial previews; 137 entity model/texture presentations after source-mapping supplements, including explicitly labeled unused resource studies.
- [x] Historical item/block galleries: 7,600 regular previews across 1.20.1, 1.16.5 and 1.12.2, plus seven documented 1.12.2 edge cases.
- [x] 1.12.2 entity atlas: 537 static model/texture presentations across 513 source entity IDs, with inherited-model, misc/variant and special-model supplements.
- [x] 1.16.5 literal Java model gallery: 301 portraits; historical geometry galleries add 151 version-specific presentations. These categories can overlap entity identities.
- [x] Live model viewer: local official-JAR geometry/texture viewing with orbit, zoom, variants and PNG export; CPU fallback visually tested.
- [x] Artifact-backed legacy attribute dataset: 485 source-mapped entities and 2,221 literal getter values, with a compact searchable field guide and method provenance. Runtime final attributes remain unverified.
- [x] Live recipe explorer: 6,781 extracted recipe definitions across four releases; local rendering tests pass for every card. Legacy metadata-specific dyes, saplings, wool and charcoal are correctly distinguished. Chest and Lapis Lazuli examples were verified in the deployed browser UI.
- [x] First-portal illustrated walkthrough and 522 growth-stage references across 66 version-specific plant records in four releases.
- [x] Optional premium weapon overhaul requirements and official authoring/compatibility references. Reloading remains optional independently of improved visuals.
- [x] Static Coratee texture-helper mismatch documented with artifact bytecode evidence; runtime fix/test remains outstanding.
- [ ] Obtain the blocked official 1.7.10 binary through an authorized available route or owner upload, then render that release's assets.
- [ ] Finish interactive Java-coded legacy and item/block preview adapters.
- [ ] Qualify dynamic effects, animations and rendering parity in actual target-game runs.
- [ ] Complete all feature-by-feature gameplay, progression and migration acceptance checks against the owner-specific build.

See [Render Coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage), [Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html) and [Source Findings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes) for evidence and limits.

## Existing Enderloom evidence

The [September 22 v5 checkpoint](https://github.com/Herbertofury/Enderloom/blob/67a7881377ad4680936729efdf4b64f6abc5f931/docs/northpoint/ENDERLOOM_APEX_CONVERSION_V5_CHECKPOINT.md) records packaged-JVM linkage safeguards and targeted/self-test passes for the conversion toolkit. It covers checks such as invocation/descriptor drift, access rules, constructors, method handles and nested metadata. Those are valuable infrastructure receipts; they are **not** proof that every AoA feature has been converted and played.

The published [AoA requirements](https://github.com/Herbertofury/Enderloom/blob/67a7881377ad4680936729efdf4b64f6abc5f931/docs/knowledge/Advent-of-Ascension.md) and [detailed acceptance ledger](https://github.com/Herbertofury/Enderloom/blob/67a7881377ad4680936729efdf4b64f6abc5f931/docs/knowledge/Acceptance-AOA.md) explicitly distinguish source requirements from current certification. Preserve that distinction.

## AoA completion gates

| Gate | Required result | Current evidence status |
|---|---|---|
| AOA-01 · lineage | Accepted authoritative source/content union; identity and migrations | Published requirement found; final accepted local union pending verification |
| AOA-02 · semantic port | Complete target code, registries, networking, integrations, persistence | Private 1.20.1 target artifact/native admission verified; complete semantic union open |
| AOA-03 · content & assets | Every accepted feature and its real behavior/assets | Upstream census is a starting inventory; target parity pending |
| AOA-04 · native proof | Packaged client/server, mechanics, travel, saves/migration | Owner-local native client/server and short production play pass; full gameplay/travel/migration open |
| AOA-05 · clean replay | Rebuild from originals using reusable Enderloom transformations | Toolkit checkpoint exists; complete AoA replay pending |
| AOA-06 · delivery | Installable output and normal Studio workflow | Private owner profile installed and signed-in play passes; finished public release open |

## Local evidence boundary

This retained paragraph describes the original documentation-only pass. The current owner-local candidate section above supersedes its lack of local access.

The owner supplied `C:\Users\Owner\Desktop\Enderloom` as the local project. This no-new-agent documentation pass did not inspect that folder. These statuses mean **not verified here**, not “the work does not exist.” Do not overwrite or restart the local conversion to make it match this snapshot.

Next reconcile: current Git commit/dirty changes, active session ID/target, accepted input hashes, generated source/output JAR hashes, build logs, packaged linkage results, native screenshots/test receipts, save migration and performance results. Add exact dates and links; keep historical receipts rather than replacing them with unqualified “done.”


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sources-and-Credits). Source presence is not target runtime proof.

## Searchable inventory and multi-state reconciliation

The [Items & Blocks Observatory](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html) indexes all **10,077 version-specific archive-resource candidates**: 9,928 regular source-model previews and 149 separately classified initial exceptions. This is not a runtime registry count. Each exception links to an existing supplement or preserves the exact remaining limitation. [Record-by-record ledger](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Inventory-Preview-Resolution-Ledger).

The [multi-state supplement](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Multi-State-Block-References) accounts for 135 Thorny Plant age/height states and six activity-portal axis states across three releases. Of the plant states, 93 have visible texture regions and 42 have verified fully transparent UV regions. These supplement the 522 earlier age-only references; they do not establish natural state transitions or world renderer parity.

## Historical rune workflow regression targets

Published the illustrated 1.16.5 Rune Post/Randomizer handbook with 14 mappings, released recipe/loot evidence and an exact bytecode-backed output-stack remainder finding. A standalone harness covers requested counts 1–128. Consume-before-loot and mixed-hand cases are documented as runtime regression targets. These are not applied game fixes or in-game test receipts. See [Rune production handbook](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rune-Production-and-Randomizer-1.16.5).

## Interactive rendered turntables

Added turntables for all 83 inspected modern source-roster entries with 24 fixed-framing camera views each (1,992 frames), keyboard/drag/scrub controls, opt-in rotation and a bounded four-image cache. These are selected static appearances; Shiny Squid uses a clearly labeled Java neutral-body adapter. This is a rendered rest-pose presentation, not a live geometry viewer, runtime animation test or encounter-completion proof. [Turntable guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Model-Turntables).


## Trading Desk and NPC location reference · 2026-10-16

The illustrated Trading Desk covers **252 version-scoped offer definitions**: 207 in the inspected 1.16.5 custom-trader catalog and 45 in the inspected 1.21.1 catalog. The historical picker includes 21 named Lottoman variants sharing one verified pool, so aliases do not inflate offer counts. Two hundred forty-three version-specific item illustrations support the tables/cards. All 23 historical trader-pool portraits loaded in the live guide.

The historical location pass joins 29 released/source special-spawner chains, all 258 released structure templates, 158 template pools, biome starts and dimension structure settings. It establishes **candidate acquisition evidence for 43 of 44 trader identities**: eight custom-spawner traders, 33 embedded-template identities and two crate-hook identities. Skill Master remains explicitly unresolved. Jigsaw reachability is an over-approximation and is not a live spawn/generation certification.

The 419-entry historical bestiary now includes direct offer links for all 44 traders and candidate biome/dimension evidence where established. Regression checks cover all 252 offer cards, selected-release caching, stale-request/failure handling, locked/special-stack labels and shared-pool selection. The 1.16.5 roster remains release-lazy; its current uncompressed data size is 1,032,133 bytes, not a claimed network or FPS benchmark.

- [Search the Trading Desk](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html)
- [Historical trading guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trading-and-Traders-1.16.5)
- [Modern trading guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trading-and-Traders-1.21.1)
- [Find historical traders](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Finding-Traders-1.16.5)

No new runtime acceptance is asserted by this documentation pass. The earlier owner-local runtime section retains its independent scope.


## Broader loot reference · 2026-10-16

The modern reference now indexes all **1,315 loot-table resources** found in the inspected AoA3 3.7.16.1 archive (1,314 AoA namespace plus the bundled Minecraft Wither override), and all **25 registered global modifier definitions**. The 1,340 normalized records preserve source hashes, nested references, conditions and operations, with base image coverage for 1,472 referenced item IDs. Seventeen current-version image gaps were filled, including a separately checked neutral Wither Skeleton Skull model.

The inventory explorer links 1,173 exact-ID block/item table resources and contextual searches for other modern entries. Tests cover every fact panel, source item-reference multisets, all resource hashes, lazy category/icon caches, exact links, failure recovery and unchanged 10,077-record inventory navigation. The UI loads one index first and fetches category facts only when inspected.

The player guide explains Silk Touch/Fortune branches, global Ivory conditions, four explicit world-table mappings and the spawner/split-child flag checks. Vanilla Wither custom-death-loot evidence is kept separate from table entries, avoiding the false conclusion that an unlisted Nether Star was removed. No runtime drop-rate, loader-port or balance certification is inferred.

- [Loot resource browser](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1)
- [Illustrated conditions and modifier guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Loot-Tables-and-Global-Modifiers-1.21.1)

## Skill Master acquisition walkthrough · 2026-10-17

The modern trading reference now includes **55 base offers across seven vendor groups**, adding ten checked Skill Master definitions without changing the previous 45. The illustrated acquisition guide connects the Nowhere utility lobby to six Skill Helmets and four crystal sizes, exact base token shopping totals, five shipped parkour-course records, six reward-tier tables and eight boss-table references. Tier-five course availability is explicitly unresolved in this archive.

The tutorial library now has **56 version-scoped illustrated routes**. Inventory cards retain prior how-to links and add this route: **306 links across 293 cards**, using a single precomputed inline lookup. All **82 local documentation regression checks pass**. These are documentation/source checks, not game tests or private-candidate certification.

[Skill Master and Archaic Tokens](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1) · [Trading Desk](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.21.1&vendor=vendor%3Askill_master)

## Armor effects beside the previews · 2026-10-17

All **48 ordinary set studies** now carry expandable released-tooltip descriptions, covering **100 effect lines**. The Armor Atelier searches effect wording as well as set names, with one precomputed search index and no added data requests. The new [activation guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1) separates intended tooltip text from nine checked callback routes and documents the Alacrity partial-set source mismatch without claiming a reproduced game bug.

The tutorial library contains **57 illustrated routes**, with **83 passing local documentation checks**. Full interpretation of the remaining set callbacks, equipment-transition behavior and actual target-build combat/performance tests remain open. The existing owner-local runtime receipts retain their independent scope.

## All ordinary armor sets reviewed · 2026-10-17

The [armor effects guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1) now reviews **all 48 ordinary sets**, retaining **194 released set methods**, **24 shared methods**, four selected external methods and 14 attribute modifier definitions. It distinguishes cross-class rune/Spirit/planting effects, equipment cleanup and damage-category exclusions. Rosidian and Spaceking summoning activation remains explicitly unresolved; the documentation does not substitute tooltip text for an implementation path.

Five exact gallery cards carry relevant source-review notices. Ghastly scan frequency and Biogenic’s negative air write are bounded acceptance targets, not reproduced failures or measured performance regressions. All **84 local documentation checks pass**; the tutorial library remains at **57 illustrated routes**. No game execution or private-current-candidate certification is inferred.

</details>
