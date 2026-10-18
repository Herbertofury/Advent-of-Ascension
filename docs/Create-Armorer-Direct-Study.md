# Create Armorer — actual model, animation and script study

**Direct archive inspection, 2026-10-18.** Read the published [Create Armorer v1.2.0.1-for117 file](https://www.curseforge.com/minecraft/customization/tacz-create-armorer-koei/files/7598625), rather than relying on gallery screenshots or an older search cache. This archive has 13 gun-display records, 18 gun geometry files and four Lua scripts. No game execution or native compatibility pass is claimed.

Archive SHA256: `479f0ac05833ccec554efa1b22e6f71553c7ebe7f381310c28467a399c98b0ba` · 7,107,566 bytes · 521 ZIP entries.

## What the files actually contain

Counts include stored variants, hands/helpers and visual planes. They are not simultaneous visible geometry, draw calls or runtime cost.

| Display identity | Bones | Cuboids / planes | Zero-extent visual planes | Authored clips |
|---|---:|---:|---:|---:|
| cannon_40mm_salamander | 33 | 213 | 3 | 7 |
| gl_revolver_devastator | 34 | 111 | 0 | 10 |
| mg_platemag_flywheel | 177 | 561 | 256 | 9 |
| pistol_auto_stress | 39 | 83 | 1 | 13 |
| pistol_revolver_torque | 41 | 188 | 8 | 8 |
| rifle_assult_crane | 45 | 102 | 0 | 8 |
| rifle_assult_roller | 45 | 142 | 8 | 10 |
| shotgun_db_stone | 28 | 90 | 0 | 8 |
| shotgun_pump_bearing | 56 | 239 | 0 | 12 |
| smg_auto_crank | 177 | 378 | 252 | 12 |
| sniper_semi_clockwork | 42 | 232 | 0 | 8 |
| sniper_semi_m1 | 53 | 129 | 3 | 14 |
| special_melee_wrench | 22 | 13 | 0 | 14 |

## Useful techniques for our AoA weapons

### 1. Layer moving mechanisms and presentation independently

The Roller state machine separates base/bolt/main tracks, gun kick, movement and burst presentation. It has different empty/nonempty inspection and reload routing. Its inspection state hides the crosshair on entry and restores it on exit; shooting interrupts that main inspection track.

For AoA: treat inspect, recoil, movement and special flourish as independently owned tracks. Every exit route must restore temporary UI/visibility state. A cancelled inspection must not duplicate ammo transfers, leave a hidden sight, or block the next valid shot. Our current Iominator clips are only a motion foundation; they do not yet implement this complete state machine.

### 2. Frame-based visual planes are intentional geometry

The Flywheel machine gun stores 256 zero-extent planes; the Crank SMG stores 252. Many belong to numbered frame bones rather than solid weapon parts. For example, Flywheel's frame_1 uses crossed planes, and reload clips gate its scale from zero to visible and back over a short interval.

This gives a concrete reference for animated steam/smoke/energy presentation. Do not reject every zero-size dimension as a malformed solid. Conversely, do not count every stored frame as a simultaneously visible particle or claim a performance win from a file count.

For Soul Storm, compare this bone-frame approach with the planned single sampled atlas surface. A single-surface approach could reduce stored geometry and animation bookkeeping, but we need native shader/pass/visual tests before claiming it is faster or equivalent. Texture access, transparency and overdraw remain relevant.

### 3. Keep visual threshold events synchronized with gameplay

Roller's gameplay script caches acceleration and a one-time loading flag. Its visual state machine separately tracks acceleration and burst presentation. The source contains a useful boundary test: starting from zero and taking consecutive qualifying branches, the client-side condition can observe count 15 immediately after incrementing, while the gameplay loading branch is an `elseif` that observes an already-15 count on a later call.

This is a **source-level test case to reproduce**, not a confirmed player-visible bug: callback ordering, timestamp semantics and native API behavior have not been exercised here. For our upgrades, prefer one authoritative transition/event identity for the flourish and associated resource change. Test threshold crossing, interruption, resume, duplicate events and item switching rather than assuming two similar counters stay aligned.

### 4. Verify LOD assets instead of trusting declarations

Eight of the 13 displays reference LOD model/texture pairs absent from this ZIP: 16 unresolved exact asset paths. Five pairs are present. External resource packs or native fallback behavior may resolve missing paths; the audit does not establish a crash or rendering defect.

Our export checks must inspect actual main/LOD files, correct namespaces, logical UV size versus PNG dimensions and attachment variants. Do not claim a working optimization merely because a display JSON has a `lod` key.

### 5. Accept source JSON syntax deliberately

The pack contains commented JSON. Our audit now reads comments and trailing commas while preserving quoted URLs, escaped quotes and delimiter text. This is a bounded JSON-with-comments reader, not full JSON5 support. A strict-parser failure is not evidence that the native pack fails to load.

## Apply the findings, with honest gates

- [ ] Add native cancel/interrupt tests for every inspection and reload state.
- [ ] Use shot/event identity for synchronized threshold flourishes; verify client/server lifecycle.
- [ ] Compare timed-atlas and frame-bone effects visually and under equivalent native workloads.
- [ ] Resolve all authored LOD and texture paths in a clean export before packaging.
- [ ] Separate solid collision volumes from effect planes and helper geometry in QA.
- [ ] Keep hand fit, feed/reload presentation, shader compatibility and runtime performance as independent acceptance gates.

[Full factual census with exact paths and script hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/create-armorer-model-animation-audit.json) · [Our reproducible audit tool](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/create-armorer-audit-tool-v1.zip) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

## Attribution and reuse

Reference pack by **Koei**. Its [project license page](https://www.curseforge.com/minecraft/customization/tacz-create-armorer-koei/license) identifies Creative Commons Attribution 4.0 International. Retain attribution, license links/notices and modification descriptions if licensed material is reused, and check individual asset/dependency provenance. This publication contains our audit tooling and factual observations, not the downloaded pack or its models, textures, sounds or scripts.
