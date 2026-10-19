# Confirmed-shot presentation core

**Implemented and unit-tested original logic; native integration is still open.** This small Java component selects an alternating visual emitter for one trusted weapon/session context. It does not fire a weapon.

## Behavior

- A blocked/rejected attempt produces no presentation event and does not advance the sequence.
- Duplicate and late confirmations are ignored. Gaps use the authoritative shot ordinal rather than packet-arrival count.
- Wrong weapon, session or attachment-configuration events are ignored.
- An older snapshot cannot rewind replay history. Unequipping/re-equipping retains the high-water mark.
- Changing emitter count requires a new configuration revision. Snapshot binding never resets the accepted-shot ordinal within a session.
- Projectile-count metadata is preserved. Three visible emitters do not silently change a four-projectile burst into three projectiles or three ammo charges.

The object has constant-sized state and performs no frame polling, file scanning, resource consumption, damage calls or projectile spawning. This is a source-level design property, not a measured game FPS improvement.

## Proposed mappings

- Baronator: two emitter slots, upper first then lower.
- Soul Storm: four default slots; five/six-slot attachments get a new resolved configuration revision.
- Discharge: three modeled visual channels can alternate while retaining its original four-projectile burst metadata. This is a proposed presentation mapping, not a change to its original firing class.

## Native adapter requirements

1. Create the controller from the actual weapon-instance/session lifecycle. Do not accept arbitrary client packets as authoritative merely because a record is called Confirmation.
2. Call it on the owning client thread; it is intentionally not a cross-thread synchronization service.
3. Feed accepted-shot ordinals and resolved configuration snapshots from the real game path. A new session requires a new controller. Shot ordinals continue across attachment changes within that context.
4. Preserve responsive local prediction. This confirmed-event core does not reconcile predicted first-person effects; wiring it in must not introduce a network-round-trip delay or replay an effect already predicted locally.
5. Resolve emitter bone handles once on asset load/reload. Verify their count against the resolved build; use a safe original-renderer fallback on mismatches. Do not scan meshes every shot or frame.
6. Actual ammo, Spirit, damage, projectile creation, multiplayer authority and save behavior remain with the native game/weapon adapter. This utility must not become a second firing path.
7. Exercise blocked shots, rapid input, configuration swaps, reloads, reconnects, prediction correction and multiplayer in the pinned native stack before acceptance.

## Test evidence

The same Java 17-targeted class files ran successfully under Java 17 and Java 21. Each run performs 80,031 assertions, including a deterministic cycle sweep over emitter counts 1–100 and shot ordinals 1–200, plus replay, snapshot, configuration and integer-boundary cases. This is not 80,031 separate game scenarios.

A development test caught that blindly rebinding a stale snapshot could replay old effects. Binding now preserves its high-water mark and rejects old/mismatched configurations; those cases are regression tests.

Run run_checks.py with --jdk17 pointing to a JDK 17 directory and --java21 to the second Java executable. No Minecraft classes are mocked or invoked: these are tests of the original presentation-state code only. Native animations, sound, particles, prediction and gameplay are untested.


## Released AoA event-source audit

In the inspected AoA3.7.1 gun use-tick path, successful virtual `fireGun` return handling precedes the server-player recoil call. But `GunRecoilPacket` serializes **only a recoil float and firing-time integer**. It contains no weapon-instance identity, hand, configuration revision or shot ordinal. The inspected path sends it to the firing player, and its client handler calls `ClientOperations.addRecoil`.

Do not identify a weapon by recoil amplitude or by whichever item is held when that packet arrives. Rapid swaps, offhand use and observer rendering make that unsafe. A genuinely authoritative identity-bearing native event remains required, without replacing the original firing/resource path. Third-person tracking and responsive prediction need explicit integration tests.

[Released-class evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/native-shot-event-evidence.json)

## Consume this core rather than duplicating its counter

The [Soul Storm R3 presenter](Soul-Storm-Sculpt-Study#v31-recoil-transport-bounded-tracks-and-matched-glow-ownership) takes this core's resolved `emitterIndex`. Its earlier local arrival counter was rejected after an ordinal-gap test. The existing core passed its unchanged 80,031-assertion suite on Java17/21, and the combined Java-to-Lua mock-context bridge passes 29 assertions on each runtime. This remains isolated logic evidence, not a native packet or renderer test.

[Existing original core source](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/confirmed-shot-presentation-source.zip) · [R3 combined source/tests](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-recoil-transport-v31-r3.zip)
