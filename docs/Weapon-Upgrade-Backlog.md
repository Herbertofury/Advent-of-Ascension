# Ascension Armory — implementation checklist

**Current gameplay direction:** original behavior is the baseline, not the ceiling. Attachments may intentionally increase damage/projectile count and change firing patterns, resources and effects. See [Functional weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades). Accidental duplicate callbacks remain bugs; deliberate multishot is a feature.


**Status: requested design goal; no upgrade build certified.**

[Design](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [References](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

## Current authoring milestone · 2026-10-18

[Original animated Baronator prototype and editable source](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Animated-Weapon-Prototype-Baronator) now exist. The public approved-firing authoring variant has 103 cuboids, 27 bones and 15 animation records; a separate mechanism lab explores feed and hand-fit repairs. These remain unqualified authoring studies, not native gameplay acceptance. The older versioned ledger covers overlapping historical/modern records; the new first-lane production queue explicitly covers all 228 ranged registrations in AoA 3.7.1 for Minecraft 1.20.1. Neither ledger counts them as finished upgrades. Native AoA/TaCZ integration, hand animation, sound, multiplayer and performance acceptance remain open.

[Central compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Dimension mods and Extra Realmstones](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extra-Realmstones-and-Dimension-Compatibility)

## Soul Storm: original spirit-channel study

[Preview, source and scoped evidence](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Authoring-Study): 77 cuboids, 19 bones, seven motion records, sampled moving-part and right-arm-proxy checks, plus pose-continuous bounded cosmetic response. Native Spirit behavior, complete hand rig, audio/VFX and runtime acceptance remain open.

## Concept-first art direction

Every weapon starts with actual original-reference and gameplay study, then high-quality generated concepts, critique, and a consistent modeling target. Preserve recognizable AoA nostalgia while radically improving silhouette, materials, motion, sound and effects. Numerical collision checks do not certify good art. The earlier Soul Storm blockout is rejected as the visual benchmark; see [Soul Storm art direction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Art-Direction) before further modeling. [Baronator concept exploration](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Baronator-Art-Direction) now establishes its original-red, twin-barrel visual target and heavy alternating firing feel.

## Complete per-weapon descriptions and comparisons

Every weapon needs the [complete profile standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard): what it is, how it fires, projectile/impact behavior, resource use, strengths and quirks, plus original-versus-proposed-versus-measured values and art. Start with [Soul Storm’s full source-grounded profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile).

## Foundation
- [ ] Enumerate every accepted weapon by registry ID and source version; distinguish alternate variants from unique weapons.
- [ ] Record native ammo, projectile, skill, enchantment and special-effect contracts.
- [ ] Audit existing Enderloom/AoA work before creating duplicate adapters.
- [ ] Pin the primary loader/runtime and compatible TaCZ/tool versions.
- [ ] Implement reversible global, family and individual presentation toggles.
- [ ] Preserve original presentation when optional integrations are absent.
- [ ] Define an opt-in gameplay reload mode separately from cosmetic presentation.

- [ ] Study Ars Armorer, ArsArms and IronsArms; pin matching releases/source and evaluate optional magic-through-firearms adapters without changing native AoA costs or effects. See the [reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library#magic-through-firearms-references).

- [ ] Make reloading independently optional per weapon, disabled by default when absent from native AoA behavior; retain full premium visuals with native mana/energy/ammo use and no added reload delay.
- [ ] Test switching reload options without duplicated resources, lost charges or server/client disagreement.

## Vertical slice before scaling
- [ ] Choose representative magazine, per-round, magical/energy, bow and unusual weapons.
- [ ] Build original, AoA-faithful premium models and textures.
- [ ] Complete all applicable first- and third-person animations and sound/effect timing.
- [ ] Validate exported hand, sight, ground and fixed poses.
- [ ] Keep ammo and shot authority on the server; verify cancellation and reconnect behavior.
- [ ] Demonstrate original/premium toggles on existing saved items without lost properties.
- [ ] Compare startup, memory, frame time and low-percentile performance against original mode.
- [ ] Publish actual screenshots and short motion captures, not concept renders as implementation proof.

## Complete the arsenal
- [x] Maintain the [first-lane 228-weapon production queue](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/arsenal-production-queue.json), including unfinished entries and six separate acceptance gates. Historical-only weapons and other families remain additional coverage work.
- [ ] Add family-appropriate reload/recharge/rearm and inspection variety.
- [ ] Test FOV, handedness, camera-motion options and supported shader/resource-pack combinations.
- [ ] Test dedicated/integrated multiplayer, death, drops, dimension changes and item swaps mid-reload.
- [ ] Test saves across supported updates and graceful fallback after removing optional dependencies.
- [ ] Add LOD, lazy assets and bounded cache invalidation without repeated scans.
- [ ] Audit licenses and contribute broadly useful fixes to upstream projects where appropriate.
- [ ] Release only after gameplay, visual, compatibility and performance gates have recorded evidence.

## Required acceptance record per weapon

Registry ID and version; baseline mechanics; remodel author/license; animation state coverage; backend and dependency pins; toggle/fallback results; save and multiplayer evidence; comparison images/video; measured startup/memory/frame-time results; unresolved defects. A checked box requires a linked result, not just generated files.


## Modular armory and effect salvage

See [the complete researched design and acceptance checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage) and [conceptual physics references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Physics-and-Speculative-Technology).

- [ ] Implement extensive interchangeable barrels, scopes, suppressors, stocks, grips, feeds, handling and cosmetic modules.
- [ ] Recover specific weapon effects as reusable cores; keep detach, extract, dismantle and recycle operations distinct.
- [ ] Add AoA-specific dimension/resource/effect mechanics with explicit native-version evidence.
- [ ] Build server-authoritative atomic transactions with duplicate prevention, protected items and full-inventory safety.
- [ ] Show visible assembly, every effect, before/after handling and clear incompatibility explanations.
- [ ] Preserve optional reload behavior and native resources; validate TaCZ and Apotheosis adapters separately.
- [ ] Test modular combinations, animation clearance, saves, multiplayer and measured performance before marking shipped.

## Minigun rotary study — 2026-10-18

[Open the interactive Minigun motion lab](https://herbertofury.github.io/Advent-of-Ascension/minigun-motion-lab.html) · [Original editable source](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minigun-motion-study.zip) · [Scoped bore evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/minigun-bore-clearance-qa.json)

- Original orange/charcoal model, currently 302 cuboids, 20 bones and 11 animation records; eight records enabled for inspection.
- Removed six solid decorative bore caps. All six visual barrel corridors pass 438 sampled barrel/angle checks; the original cap defect is retained as a negative fixture. This is not a complete spatial acceptance test.
- Added a frame-rate-independent cosmetic rotor controller with continuous phase through start, stop and resume. Standalone tests cover timestep subdivision, invalid inputs and stationary rest.
- Hollowed the receiver and enlarged the carry-handle opening. The side-feed route, hand fit, moving cover/vent clearance and reload ownership still need work.
- Native one-tick firing must not wait for cosmetic spin-up. Native ammo, resource costs and item identity stay authoritative.
- No native runtime, gameplay, performance or final artistic acceptance is claimed. The arsenal remains in active production; a published study is not a completed weapon.

The [parked-rotor feed cutaway](https://herbertofury.github.io/Advent-of-Ascension/minigun-feed-lab.html) separately tests intake, cartridge rotation and chamber transfer against all exported solids at 120 Hz (661 poses). The tray stops behind the barrel opening. This remains a transfer blockout: carrier support, cyclic rotary timing, discharge/ejection and complete hand choreography are open. The [clean-extraction receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/minigun-study-reproduction.json) verifies both viewers reproduce from the original source archive.


## Earned and expressive customization

- [ ] [Weapon charms, effect channels, stickers and emblems](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization): gameplay-earned functional charms; finishers, defeat effects, projectiles, tracers and impacts; static/animated/glowing decals, custom emblems and saved layouts.
- [ ] [Alternate barrels and skins](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Alternate-Barrels-and-Skins): identity-specific transformations for every weapon, retained concept history and actual original flight/impact footage.
- [ ] Apply the [direct Charmsy release findings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Charmsy-Direct-Study), with original assets and explicit AoA/TaCZ adapters.
