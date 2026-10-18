# Living AoA development

Advent of Ascension is created by Tslat and contributors. This is the owner's Enderloom restoration project, with an existing local playable candidate; it is not an official Tslat release or a certified complete historical/latest union.

## Current usable candidate

In the owner's installed Enderloom, choose **Advent of Ascension · Current Playtest**. The verified target is Minecraft 1.20.1 / Forge 47.4.23 / Java 17. Native client/server acceptance and ordinary signed-in rendering, movement, server save/restart pass. Vanilla hearts are the default, with all optional modes retained. The JAR is local, not a public download here.

- [Current native/production facts and exact local receipt hashes](current-playtest.json)
- [Every member of the exact candidate](current-artifact-inventory.json)
- [Already implemented Coratee texture-helper fix and its remaining limits](coratee-current-evidence.json)
- [Runtime checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
- [Living upstream reconciliation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Upstream-Reconciliation)

The complete historical/latest union, later Anima/Soul Power/tablet/armour consumers, additional deity chains, all natural progression and travel, optional full-pack compatibility, migration and equivalent-work performance gates remain open. Twenty-five loaded-world validation contexts are not full dimension gameplay acceptance.

## Current Pixon spawning acceptance

[Complete current spawn-policy/native/production continuation](PIXON-SPAWNING-2026-10-17.md). All six policies, 986 weighted tickets, controlled real-terrain spawning and both native backends pass. Current Playtest is updated in place, preserving every existing world/config file and launch choice. Full modern Pixon reconciliation and the whole merge remain open.

## Current merge implementation

[2026-10-17 Extraction/Anima source, compile and native-test progress](merge-progress-2026-10-17.json). Complete native client/server, independent every-member readback and ordinary signed-in production/server save/restart have passed. The original `tooling/verify_anima_extraction_native.py` verifies the scoped retained local proof, rejects incomplete proof variants and optionally compares every native client/server JAR member. It does not certify the full union. The accepted update is promoted as Current Playtest; the previous verified profile and worlds remain available.

## Keep the original moving forward

`upstream-lock.json` is a dated observation, not a permanent newest-version constant. The retained modern archive matches all **14,236 official Git blob objects**, including all **46 changelogs**, at `7919b5fe48599e6105c5740937ce36c36ef21d16`. The current official production observation is AoA3 1.21.1-3.7.16.1. Freshness is separate from reconciliation: the newest source is not fully merged into the private playable target.

`tooling/upstream_guard.py` compares the live official default branch, HEAD, complete changelog tree, all GitHub releases and tags to that observation. CI checks drift on relevant changes and daily. A changed upstream fails visibly; it does not overwrite accepted content or pretend to port itself. Enderloom's existing `scripts/aoa-upstream-milestone-freshness.cjs` separately resolves the complete official provider release list. Its whole-project native acceptance runner now checks that fresh receipt against the lock before intake/build. This does not claim every Studio entry point already enforces this gate.

## Use the whole wiki as a checklist

`wiki-checklist.json` is generated from every Markdown page in a pinned wiki Git revision. It retains each checkbox's page, heading, source state, stable identity and source hash. A source checkmark never becomes gameplay certification. Removed/changed tasks and wiki drift are reported rather than silently lost. The wiki is the human checklist; this file is its derived intake, not a second semantic project model.

```console
python -m unittest discover -s development/tooling -p "test_*.py" -v
python development/tooling/upstream_guard.py --lock development/upstream-lock.json
python development/tooling/wiki_checklist.py --wiki path/to/wiki-checkout --check development/wiki-checklist.json
python development/tooling/verify_local_artifact.py --artifact path/to/aoa3-3.7.1.jar --inventory development/current-artifact-inventory.json
```

The last command verifies the supplied file and every ZIP member; it does not run Minecraft or certify missing gameplay. Rebuilt files need their own evidence, including any changed build timestamp.

## Long-lived worlds

Keep canonical IDs and proven aliases stable. Keep existing chunks and player/entity/block-entity extension data. Test travel, inventories, saves and forward migrations; apply new generation to new chunks. Any existing-chunk migration needs a separate explicit decision, snapshot and rollback. These are acceptance requirements, not a promise that all future Minecraft/mod combinations can load any save unchanged.

## Publication scope

Original maintenance tools and factual source/runtime metadata are published here. Original AoA sources, assets and the modified JAR remain local under the [upstream terms](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/LICENSE.md). No written redistribution waiver or completed public mod release is claimed. The existing player atlas and credits remain intact.

## Renderer compatibility continuation

The current playtest retains the complete Extraction/Anima foundation and all 24,103 preceding members. [Renderer compatibility acceptance](RENDERER-COMPATIBILITY-2026-10-17.md) records 24 actual OpenGL and 24 native Hari Vulkan overlay draws, clean standalone production checks, failed fixtures and limits. The 2,000 FPS objective and the full merge remain open.


[Augury and all original tablet component progress](AUGURY-TABLETS-2026-10-17.md). Native server acceptance passes; the full client and acquisition gates remain open. The current playable release is unchanged.


The [Augury/tablet continuation](AUGURY-TABLETS-2026-10-17.md) now passes complete
native client/server, normal signed-in production and selected native Hari62
renderer checks. Current Playtest is updated in place; the complete historical
union, acquisition and 2,000 FPS target remain open.

[Saved Skill Master upgrade and preserved custom trades](SAVED-MASTER-UPGRADE-2026-10-18.md). The exact current cumulative candidate passes complete native, ordinary production, required Vulkan and in-place promotion. Full historical/latest merge completion remains open.

[Whole historical block batch and mature registry identity resolution](WHOLE-HISTORICAL-BLOCK-BATCH-2026-10-18.md). The full union remains unfinished.


[Whole Snapshot source recovery and four-dimension program cohort](SNAPSHOT-WHOLE-PROGRAMS-2026-10-18.md). Complete source recovery, the 78-block native client/server batch and all four serial/parallel terrain programs are verified within their stated scopes. Current v93 stays playable; the full merge and world/entity/progression gates remain open.


The [missing entity dependency continuation](SNAPSHOT-WHOLE-PROGRAMS-2026-10-18.md)
now passes the whole native server with 128 Fade drop seeds, 700 Hunter reward
cases and both projectile lifecycle/impact cases. Every source owner and all
24 restored media files are independently read back. Corrected client effects,
full gameplay and live dimension/progression gates remain open; Current Playtest
remains v93. The first failed client fixture is retained.


The [quiet complete entity-dependency client/server continuation](SNAPSHOT-WHOLE-PROGRAMS-2026-10-18.md) now passes 2,800 actual-original XP boundary comparisons, all 56 particles and complete native draws, with QA master volume verified at zero. Full gameplay and missing-world gates remain open; playable v93 is unchanged.
