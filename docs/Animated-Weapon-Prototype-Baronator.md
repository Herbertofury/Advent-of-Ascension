# Animated weapon prototype: Baronator

**First original authoring milestone · not an installable or game-tested upgrade.** This is the start of the requested premium animated AoA arsenal. AoA and the Baronator identity are credited to Tslat and contributors.

[Open the interactive authoring lab](https://herbertofury.github.io/Advent-of-Ascension/armory-workbench.html) · [Weapon overhaul](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Full weapon backlog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog) · [Compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Download original editable prototype](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ascension-armory-authoring-prototype.zip)

![Original Baronator authoring model with red armor, twin muzzle channels and mechanical detail](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/armory-baronator-prototype.webp)

## See the exported motion

![Animated authoring preview: equip, firing and bolt cycling, inspection with opening vents, then secondary-effect cue](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/armory-baronator-motion.webp)

This preview is rendered from the exported model and keyframes. It is not Minecraft footage, a successful TaCZ load or evidence that the native grenade mechanic is wired up.

## Actual deliverables

- Original Bedrock Entity geometry: **95 cuboids across 23 bones**, with a 128×128 palette texture.
- **12 animation records:** idle, two static mode poses, equip, holster, shoot, inspection, empty inspection, two optional reload demonstrations, vent and grenade-effect cue. Static poses are not counted as twelve distinct full-motion sequences.
- TaCZ-style display configuration and view/hand/muzzle/shell locator names, pending in-game alignment.
- Editable generators and a reproducible Blender authoring/rendering pipeline.
- Static checks covering the bone hierarchy, finite geometry, texture bounds, referenced animation bones, clip timing and manifest hashes; **2,478 sampled channel frames** checked at 60Hz.
- A version-keyed coverage ledger covering **412 legacy weapon records, 411 modern weapon records and 78 audited 1.20.1 direct guns**. These overlap across releases and are not completed weapon upgrades.

## Preserve what makes it an AoA weapon

The first target contract is the 1.20.1 / AoA3.7.1 Baronator. Its audited registration inputs are damage3, shot interval5ticks and durability2480, with a full-auto default. These inputs are not guaranteed final damage or measured fire rate.

The associated source has an additional grenade branch after a successful native shot. Turning this into an ordinary TaCZ rifle would omit part of its identity. The implementation must retain the original server-authoritative shot, cost and special-effect paths while improving presentation.

**Reloading remains independently optional.** The default is native ammo/resource behavior. The prototype's reload clips only demonstrate an animation direction; they do not transfer ammo, create a magazine requirement or establish a working gameplay conversion.

## Still open before a playable release

- Native AoA presentation bridge and actual TaCZ resource-loading test.
- Authored first-person hand interaction, sight alignment, left-handed view and FOV validation.
- Custom third-person choreography, sounds and polished muzzle/secondary effects.
- Interrupt-safe transitions during swaps, drops, death, travel and reconnects.
- Original/premium toggles on existing saved items and graceful missing-backend fallback.
- Multiplayer and equivalent-work startup, memory and frame-time benchmarks.
- Further art and animation iteration against the owner's quality bar; this first pass is not declared finished.

## Tooling and provenance

The geometry, palette and keyframes are original project work. No TaCZ default artwork or animation clips are included. Format/API study uses [the pinned official TaCZ source](https://github.com/MCModderAnchor/TACZ/tree/b482eff8c94a733ac8d0910193fca3893954027c); default-pack examples are references, not redistributed assets. The source archive includes generation and validation scripts, with current limitations clearly recorded.


## Reload collision correction and acceptance gate

The reported magazine/handle clipping was reproduced: the original trigger guard intersected the magazine at rest, and the reload moved the magazine toward the grip. The live authoring lab and downloadable source now use a shortened, repositioned guard and a vertical extraction/reinsertion path. The grip cap also follows the grip angle. Earlier embedded milestone images above predate this repair.

The new oriented-cuboid regression must detect the retained old defect. It checks the magazine against the grip, cap/ribs, trigger guard and trigger throughout all clips at 240 Hz plus every keyframe. Both Baronator variants pass this scoped check. This does not certify every mesh pair, real first-person hands or engine transitions. Known visible clipping or mesh errors block visual acceptance.

[Read the mandatory visual QA gate](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/WEAPON-VISUAL-QA.md) · [Published collision evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/reload-clearance-qa.json)
