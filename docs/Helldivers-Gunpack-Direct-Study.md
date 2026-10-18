# Helldivers gunpack — actual hotfix file study

**Direct file inspection, 2026-10-18.** Reference: zeta1918's [October 5 emergency hotfix, file 9069318](https://www.curseforge.com/minecraft/customization/tacz-helldivers-escalation-of-freedom/files/9069318). The file list separately flags the October 3 build as faulty; this study uses the later listed hotfix. No game execution, native compatibility or performance pass is claimed.

Archive SHA256: `43c0884bf721f8d746b1b8d5d4e8153153ca386cdac3878db3a182e044e7af93` · 61,488,777 bytes · 2,155 ZIP entries.

## Coverage and identity

The archive census resolves **57 gun-display records, 56 gun-index records and 90 Lua files**. These are stored resource counts, not proof of 57 distinct playable weapons. A test-railgun display exists without a matching test-named gun-index record in this scan. The archive also contains older/newer script variants; the filename with the highest suffix is not automatically the active implementation.

For example, the actual railgun data file selects **railgun_mk2_logic**, while Quasar and PLAS-101 select their **mk3** logic. Our research follows those declarations. Native dynamic overrides or other packs still require separate inspection.

## Useful lessons for AoA upgrades

### Attachment variants need real animation coverage

The BR-14 animation file has 54 clips, including magazine-specific reload/continuation/follow-up sequences, inspections, empty/out-of-mag states, fire-mode changes and offset variants. This is a concrete example of why one generic reload cannot stand in for every installed attachment.

For our modular armory, define the supported configuration matrix first. Test each visible magazine/hand path and interrupted continuation. A bigger attachment must have a corresponding safe animation path; hiding it for the entire reload or shrinking the grip is not an acceptable collision fix.

### Charge changes both function and presentation

The selected PLAS-101 script uses cached charge state to modify weapon properties. One stock attachment changes the charged explosion behavior and burst count. The associated animation file includes charge-start/spin/shoot and expansion/ending clips.

For Soul Storm's beam, disc-stack and branching conversions, a visual upgrade must be paired with declared behavior and resource costs. Charge, visible emitter count and actual discharge must agree. Partial-charge release, interrupted charge, swapping the attachment and returning to the weapon are required test cases. This archive demonstrates a technique; it does not prove our conversions work.

### Preserve typed state rather than assuming every ammo field means ammunition

Quasar's selected script uses a processed timestamp stored through magazine-ammo API calls to recover cooling progress on initialization. It attempts a real-system timestamp API and falls back to the current timestamp API. Its shot path does not consume ammo, and its reload callback returns false.

This is a significant integration warning: **a field named ammo can be used as persistent state by a gun's script**. A generic “refill ammo,” “transfer magazine,” or “copy all gun data” operation could corrupt such a design. Our salvage, upgrade and compatibility layers need weapon-aware state ownership, explicit schema/version handling and a conservative policy for unknown fields.

Do not copy this storage approach into every AoA weapon. Define whether cooling should advance while paused, offline or unequipped; clamp invalid/backward clock deltas and test reconnect/reload behavior. Preserve the original weapon contract where required.

### LOD is real, but savings vary substantially

All **49 declared LOD model/texture pairs** resolve inside this archive. The eight displays without a LOD declaration are a separate category, not missing references.

| Display | Main bones / cuboids | LOD bones / cuboids |
|---|---:|---:|
| BR-14 | 50 / 608 | 7 / 12 |
| PLAS-101 | 63 / 720 | 8 / 10 |
| Quasar | 50 / 748 | 29 / 718 |
| Railgun | 117 / 647 | 93 / 209 |

These are stored geometry counts, including variants and helpers. Quasar's LOD retains most cuboids, whereas some others are much smaller. A present LOD file alone does not establish a measured frame-time improvement. Compare visible silhouette, active bones, effects, shader passes and native timings under the same scene.

### Originality and readability still matter

Use the references to understand animation ownership, state handling and presentation craft. AoA weapons must retain their own sprites' identity, realm themes and original behavior. A large number of cuboids, effects or clips is not automatically better art or more fun.

## Tests to add to our acceptance matrix

- [ ] Resolve the active data/script/state-machine chain, including external references and overridden resources.
- [ ] Exercise charge interruption, partial release, overcharge, item switching and server reconciliation.
- [ ] Test every supported attachment's reload/inspection and no-mag states with actual hands.
- [ ] Verify upgrade/salvage preserves supported typed state without treating timestamps as ammo.
- [ ] Test paused/offline cooling policy and invalid clock deltas explicitly.
- [ ] Compare actual main/LOD visual parity and equivalent-work native performance.

[Complete path/count/hash audit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/helldivers-model-animation-audit.json) · [Reproducible audit tools](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/helldivers-audit-tool-v1.zip) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

## Attribution and reuse boundaries

Reference pack: **zeta1918**, with script attribution comments also naming **foxatl** in selected files. The [project listing](https://www.curseforge.com/minecraft/customization/tacz-helldivers-escalation-of-freedom) labels its license Attribution-NonCommercial-ShareAlike 4.0 International. Underlying game assets and third-party contributions require their own provenance review. This study publishes our factual observations and audit tools, not the reference ZIP, models, sounds, textures or Lua source. It is not a blanket permission to transplant Helldivers assets into AoA.
