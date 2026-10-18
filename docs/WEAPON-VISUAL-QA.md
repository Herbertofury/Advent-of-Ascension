# Weapon visual acceptance gate

No weapon is visually accepted while a magazine, hand, bolt, barrel, moving cover or attachment visibly cuts through an unrelated solid surface. Passing JSON/schema tests is insufficient.

## Baronator defect and correction, 2026-10-18

The original trigger guard extended into the magazine even in the resting pose. The reload also moved the magazine rearward toward the grip. The correction shortens/repositions the guard around the trigger and extracts/reinserts the magazine vertically. Both original and alternating-barrel variants inherit this correction.

`test_reload_clearance.cjs` uses oriented-box separating axes, including individually rotated cubes and bone transforms. It tests every animation at 240 Hz plus every keyframe, against the grip, grip cap, grip ribs, trigger guard and trigger. The retained pre-fix fixture must fail; both repaired variants must pass. This is a scoped geometric regression, not whole-weapon approval. Receiver sockets and intentional assembled overlaps are not silently certified by this test. The local expanded test also evaluates 110 synthetic linear recovery transitions per variant from sampled reload phases into idle, draw, holster, shoot and inspect. These are authored pose-crossing tests, not an implementation or certification of the TaCZ runtime interruption controller.

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
