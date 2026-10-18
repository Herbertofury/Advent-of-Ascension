# Animated weapon prototype: Baronator

**First original authoring milestone · not an installable or game-tested upgrade.** This is the start of the requested premium animated AoA arsenal. AoA and the Baronator identity are credited to Tslat and contributors.

## Current inspection branches

- [Connected mechanism and hand-carry study](https://herbertofury.github.io/Advent-of-Ascension/baronator-mechanism-lab.html): 132 cuboids, 41 bones and 20 exported records, with nine enabled inspection actions. Feed/bore and selected arm/carry checks are scoped authoring evidence.
- [Modular part-fitting study](https://herbertofury.github.io/Advent-of-Ascension/baronator-attachment-lab.html): six visual combinations, from the base model to an original prism sight and dual external runic housings. No optics, suppression, crafting or stat changes are implemented. [Design, comparison image and source](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage#first-visual-assembly-study).
- The 103-cuboid firing study below is retained as an earlier milestone, including its known mechanism limitations.

All branches remain authoring prototypes. Native behavior, final art, camera/hand alignment, interruption handling and performance acceptance are still open.

## Historical firing prototype

[Open the historical firing lab](https://herbertofury.github.io/Advent-of-Ascension/armory-workbench.html) · [Weapon overhaul](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Full weapon backlog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog) · [Compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Download original editable prototype](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ascension-armory-authoring-prototype.zip)

![Original Baronator authoring model with red armor, twin muzzle channels and mechanical detail](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/armory-baronator-prototype.webp)

## See the exported motion

![Animated authoring preview: equip, firing and bolt cycling, inspection with opening vents, then secondary-effect cue](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/armory-baronator-motion.webp)

This preview is rendered from the exported model and keyframes. It is not Minecraft footage, a successful TaCZ load or evidence that the native grenade mechanic is wired up.



**Historical layout defect:** the 103-cuboid variant below has no demonstrated connected feed route. The newer mechanism study above addresses that layout with a connected path and scoped checks; it still must complete the [mechanism and animation QA contract](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Mechanism-and-Animation-QA) before full acceptance.

## Actual deliverables

- Original Bedrock Entity geometry: **103 cuboids across 27 bones in the alternating-barrel variant**, with a 128×128 palette texture.
- **15 animation records in the revised variant:** the original twelve records plus independent upper/lower firing and an alternating-barrage preview. The live lab defaults to the approved top/bottom firing study. Static poses and a combined preview are not separate finished gameplay actions.
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

The original magazine intersected the guard. A first fix shortened the guard and was rejected because it crowded the finger opening and left a trigger/guard collision. Both faulty layouts are retained as failing regression fixtures.

That earlier revised layout restores the full trigger opening, moves the magazine forward and lower into an open structural socket, attaches the trigger into its mounting area and aligns the grip cap. Extraction is vertical. The approved alternating upper/lower heavy recoil is retained in the live viewer and editable source package. Earlier embedded milestone images above predate this layout.

The geometry gate now covers six interactions: magazine/hand area, trigger/guard, reserved finger space, magazine/lower barrel, magazine/socket and lower barrel/socket. Both variants pass every sampled clip at 240 Hz plus all keys and 110 synthetic linear recovery transitions each. The reserved finger envelope is a design allowance, not a real hand-rig certification. Exact engine transitions, hands, other mesh pairs and gameplay remain open. Known visible clipping or mesh errors block visual acceptance.

[Mandatory visual QA gate](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/WEAPON-VISUAL-QA.md) · [Collision evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/reload-clearance-qa.json) · [Pinned Armorer reference study](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/reference-pack-study.json)
