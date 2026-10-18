# Weapon visual acceptance gate

No weapon is visually accepted while a magazine, hand, bolt, barrel, moving cover or attachment visibly cuts through an unrelated solid surface. Passing JSON/schema tests is insufficient.

## Baronator layout correction, 2026-10-18

The original magazine intersected the trigger guard. A first repair shortened the guard; that crowded the finger space and left a trigger/guard intersection. That repair is rejected. Both historical defect fixtures are retained and must fail the regression test.

The revised layout restores the full 4.8-unit guard span, moves the magazine forward by 4 model units and down by 1.6, and gives it an open structural socket below the lower barrel. The trigger connects into its mounting area and the grip cap follows the grip angle. The magazine extracts vertically; the hand opening is not sacrificed. The approved alternating upper/lower recoil is retained and is the live viewer's default firing study.

`test_reload_clearance.cjs` checks six interaction groups: magazine/hand area, trigger/guard, reserved finger envelope, magazine/lower barrel, magazine/socket, and lower barrel/socket. It uses oriented-box separating axes with a conservative broad-phase rejection, individually rotated cubes and bone transforms. Every clip is sampled at 240 Hz and at all keys. Both repaired variants must pass. The cramped-guard fixture must fail both trigger/guard and finger-space tests; the original fixture must fail both reloads.

The reserved index-finger envelope is an explicit design allowance (2.2 × 1.4 × 1.4 model units), not a substitute for fitting real Minecraft/TaCZ hands. The test also samples 110 synthetic linear recovery transitions per variant into idle, draw, holster, shoot and inspect. Engine interruption logic, spline overshoot, real hands, every other mesh pair and gameplay remain unqualified. Receiver/socket insertion contacts must be separately justified; no blanket moving-bone exemption is acceptable.

## Mandatory gates before accepting a finished asset

- Inspect every clip at authored speed and quarter speed, front/back/both sides/top/bottom and first-person camera.
- Test tactical/empty reload, draw/holster, aim, recoil, alternate fire, inspection, locomotion and attachment combinations.
- Test interruption and resumption at extraction, handoff, insertion and bolt-release phases. No teleporting magazine or fingers crossing solids.
- Define permitted contacts by named component pair and bounded insertion volume. Never suppress an entire moving bone to hide an intersection.
- Validate magazine/socket alignment, clearance along the swept path, pivots, normals, winding, zero-area/duplicate faces, UV bounds and seams, z-fighting, holes, texture bleeding and silhouette from all angles.
- Inspect real hands and all supported FOVs, left/right presentation and third-person poses in the actual pinned TaCZ build.
- Verify recoil settles cleanly, flashes follow the firing barrel, VFX/audio match confirmed shots and resource counts cannot change from animation alone.
- Reject any known visible clipping or mesh defect. Numerical tests supplement visual inspection; they do not replace it.
- Record video/screenshots, exact versions and unresolved defects. Never label an authoring preview as game-tested.

## Reference-study criteria

Study Create Armorer, Immersive Armorer, Ars Armorer and Helldivers: Escalation of Freedom for distinctive silhouettes, readable mechanisms, deliberate key poses, hand contact, staged magazine clearance, recoil recovery, synchronized flash/sound and restrained effects. These are comparison targets, not a claim that every pack is flawless or a license to copy its assets.

- https://www.curseforge.com/minecraft/customization/tacz-create-armorer-koei
- https://www.curseforge.com/minecraft/customization/tacz-immersive-armorer-koei
- https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei
- https://www.curseforge.com/minecraft/customization/tacz-helldivers-escalation-of-freedom

For each studied release, retain its official file URL, version/hash and observations about specific clips. Separate listing claims from inspected animation evidence. Author original geometry, choreography and effects unless the actual asset license and permission allow reuse.
