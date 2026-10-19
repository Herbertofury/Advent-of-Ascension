# Hand clearance must use the rendered player arm

**Pinned release study: TaCZ 1.20.1 / 1.1.8-hotfix2. Read-only source inspection; no native hand-fit acceptance.**

A modeled proxy can fit while the actual in-game hand still clips. The released default AK47 model contains 3×12×4 example cubes under `lefthand_pos` and `righthand_pos`, but those cube dimensions are not sufficient proof of what the player sees.

## Actual rendering route

- `BedrockGunModel` registers functional renderers for `lefthand_pos` and `righthand_pos`.
- The inspected right-hand renderer checks the first-person/render-hand conditions, applies its native transform, captures matrices and delegates rendering.
- `RenderHelper.renderFirstPersonArm` obtains the current player's `PlayerRenderer` from the entity renderer dispatcher and invokes the corresponding arm rendering path.
- In `FunctionalBedrockPart`, a non-null functional renderer uses that renderer branch instead of normal cube compilation. The normal geometry path is a fallback, not proof that an authoring cube is the final arm.

This is why shrinking a proxy, trigger or guard until a simple box test passes is inadequate. The complete model hierarchy, native transform conventions, skin/arm variant and first-person camera matter.

## Required AoA weapon QA

1. Keep the hand sockets and complete parent transforms explicit in the exported model.
2. Validate the actual wide/slim player variants and both main-hand choices in the pinned native stack. The example 3-wide cube does not prove that every player arm is 3-wide.
3. Inspect equip, idle, aim, fire/recovery, inspection and every applicable reload/charge phase at authored speed and slow motion.
4. Test interruption, attachment configurations, supported FOVs and third-person poses. A first-person pass cannot substitute for a third-person pass.
5. Measure grip, trigger/guard and forearm clearance using the evaluated poses. Do not hide an intersection by reducing hand size or suppressing the relevant geometry.
6. Keep offline proxy results labeled as proxy results until native captures match.

The inspected bytecode contains a 180-degree transform on an obfuscated axis field. The audit records that behavior without guessing the axis mapping. The native adapter must resolve and test the exact coordinate convention.

## Evidence and reproduction

[Hash-pinned evidence](tacz-native-hand-contract.json) · [Original audit script](tacz-native-hand-contract-tools.zip).

The script verifies the supplied release hash, relevant class markers and example anchor dimensions without executing game classes. Control-flow interpretation was also reviewed directly. It is not a complete renderer simulator or a native client test. The archive contains no TaCZ gamepack assets or classes.

Source artifact: [official TaCZ release](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero/files/9037989).

[Weapon completeness standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard) · [Weapon overview](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul).
