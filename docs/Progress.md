[Home](README.md) · [Versions](Version-Matrix.md) · [Worlds](Dimensions.md) · [Systems](Systems.md) · [Progress](Progress.md)

# Progress · what is proven and what remains

**Snapshot: 2026-10-15. No fabricated completion percentage.**

## Verified by this documentation pass

- [x] Existing destination repository identified and preserved.
- [x] Published Enderloom AoA requirements located at commit `67a7881`.
- [x] Upstream branches and official release metadata inspected and pinned.
- [x] Cross-version source census created, with comments excluded from registration counts.
- [x] Version, world, skill, combat, conversion and testing guides authored.
- [x] Original documentation artwork and attributed upstream visual references organized.
- [ ] Current Desktop Enderloom worktree, active AoA session and generated artifacts verified directly.
- [ ] A completed owner-specific AoA build certified by this pass.

## Published visual and recipe deliverables

Verified on 2026-10-15; counts are version-specific records, not unique cross-version content or converted gameplay.

- [x] Modern item/block atlas: 2,328 initial previews; 137 entity model/texture presentations after source-mapping supplements, including explicitly labeled unused resource studies.
- [x] Historical item/block galleries: 7,600 regular previews across 1.20.1, 1.16.5 and 1.12.2, plus seven documented 1.12.2 edge cases.
- [x] 1.12.2 entity atlas: 537 static model/texture presentations across 513 source entity IDs, with inherited-model, misc/variant and special-model supplements.
- [x] 1.16.5 literal Java model gallery: 301 portraits; historical geometry galleries add 151 version-specific presentations. These categories can overlap entity identities.
- [x] Live model viewer: local official-JAR geometry/texture viewing with orbit, zoom, variants and PNG export; CPU fallback visually tested.
- [x] Live recipe explorer: 6,781 extracted recipe definitions across four releases; local rendering tests pass for every card. Legacy metadata-specific dyes, saplings, wool and charcoal are correctly distinguished. Chest and Lapis Lazuli examples were verified in the deployed browser UI.
- [x] First-portal illustrated walkthrough and 134 growth-stage references across 17 plants.
- [x] Optional premium weapon overhaul requirements and official authoring/compatibility references. Reloading remains optional independently of improved visuals.
- [x] Static Coratee texture-helper mismatch documented with artifact bytecode evidence; runtime fix/test remains outstanding.
- [ ] Obtain the blocked official 1.7.10 binary through an authorized available route or owner upload, then render that release's assets.
- [ ] Finish interactive Java-coded legacy and item/block preview adapters.
- [ ] Qualify dynamic effects, animations and rendering parity in actual target-game runs.
- [ ] Complete all feature-by-feature gameplay, progression and migration acceptance checks against the owner-specific build.

See [Render Coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage), [Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html) and [Source Findings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes) for evidence and limits.

## Existing Enderloom evidence

The [September 22 v5 checkpoint](https://github.com/Herbertofury/Enderloom/blob/67a7881377ad4680936729efdf4b64f6abc5f931/docs/northpoint/ENDERLOOM_APEX_CONVERSION_V5_CHECKPOINT.md) records packaged-JVM linkage safeguards and targeted/self-test passes for the conversion toolkit. It covers checks such as invocation/descriptor drift, access rules, constructors, method handles and nested metadata. Those are valuable infrastructure receipts; they are **not** proof that every AoA feature has been converted and played.

The published [AoA requirements](https://github.com/Herbertofury/Enderloom/blob/67a7881377ad4680936729efdf4b64f6abc5f931/docs/knowledge/Advent-of-Ascension.md) and [detailed acceptance ledger](https://github.com/Herbertofury/Enderloom/blob/67a7881377ad4680936729efdf4b64f6abc5f931/docs/knowledge/Acceptance-AOA.md) explicitly distinguish source requirements from current certification. Preserve that distinction.

## AoA completion gates

| Gate | Required result | Current evidence status |
|---|---|---|
| AOA-01 · lineage | Accepted authoritative source/content union; identity and migrations | Published requirement found; final accepted local union pending verification |
| AOA-02 · semantic port | Complete target code, registries, networking, integrations, persistence | Current target artifact evidence pending |
| AOA-03 · content & assets | Every accepted feature and its real behavior/assets | Upstream census is a starting inventory; target parity pending |
| AOA-04 · native proof | Packaged client/server, mechanics, travel, saves/migration | Current runtime receipts pending |
| AOA-05 · clean replay | Rebuild from originals using reusable Enderloom transformations | Toolkit checkpoint exists; complete AoA replay pending |
| AOA-06 · delivery | Installable output and normal Studio workflow | Current release/install proof pending |

## Local evidence boundary

The owner supplied `C:\Users\Owner\Desktop\Enderloom` as the local project. This no-new-agent documentation pass did not inspect that folder. These statuses mean **not verified here**, not “the work does not exist.” Do not overwrite or restart the local conversion to make it match this snapshot.

Next reconcile: current Git commit/dirty changes, active session ID/target, accepted input hashes, generated source/output JAR hashes, build logs, packaged linkage results, native screenshots/test receipts, save migration and performance results. Add exact dates and links; keep historical receipts rather than replacing them with unqualified “done.”


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](Sources-and-Credits.md). Source presence is not target runtime proof.
