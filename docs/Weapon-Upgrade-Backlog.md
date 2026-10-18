# Ascension Armory — implementation checklist

**Status: requested design goal; no upgrade build certified.**

[Design](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [References](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

## Current authoring milestone · 2026-10-18

[Original animated Baronator prototype and editable source](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Animated-Weapon-Prototype-Baronator) now exist: 23 bones, 95 cuboids and 12 animation records, with static export checks. The versioned ledger covers 412 legacy records, 411 modern records and 78 audited 1.20.1 guns; these are overlapping version records, not finished upgrades. Native AoA/TaCZ integration, hand animation, sound, multiplayer and performance acceptance remain open.

[Central compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Dimension mods and Extra Realmstones](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extra-Realmstones-and-Dimension-Compatibility)

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
- [ ] Maintain a visible per-weapon coverage ledger including unfinished entries.
- [ ] Add family-appropriate reload/recharge/rearm and inspection variety.
- [ ] Test FOV, handedness, camera-motion options and supported shader/resource-pack combinations.
- [ ] Test dedicated/integrated multiplayer, death, drops, dimension changes and item swaps mid-reload.
- [ ] Test saves across supported updates and graceful fallback after removing optional dependencies.
- [ ] Add LOD, lazy assets and bounded cache invalidation without repeated scans.
- [ ] Audit licenses and contribute broadly useful fixes to upstream projects where appropriate.
- [ ] Release only after gameplay, visual, compatibility and performance gates have recorded evidence.

## Required acceptance record per weapon

Registry ID and version; baseline mechanics; remodel author/license; animation state coverage; backend and dependency pins; toggle/fallback results; save and multiplayer evidence; comparison images/video; measured startup/memory/frame-time results; unresolved defects. A checked box requires a linked result, not just generated files.
