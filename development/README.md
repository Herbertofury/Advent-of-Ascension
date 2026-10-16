# Living AoA development

Advent of Ascension is created by Tslat and contributors. This is the owner's Enderloom restoration project, with an existing local playable candidate; it is not an official Tslat release or a certified complete historical/latest union.

## Current usable candidate

In the owner's installed Enderloom, choose **Advent of Ascension · Current Playtest**. The verified target is Minecraft 1.20.1 / Forge 47.4.23 / Java 17. Native client/server acceptance and ordinary signed-in rendering, movement, server save/restart pass. Vanilla hearts are the default, with all optional modes retained. The JAR is local, not a public download here.

- [Current native/production facts and exact local receipt hashes](current-playtest.json)
- [Every member of the exact candidate](current-artifact-inventory.json)
- [Already implemented Coratee texture-helper fix and its remaining limits](coratee-current-evidence.json)
- [Runtime checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
- [Living upstream reconciliation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Upstream-Reconciliation)

The complete historical/latest union, Extraction/Anima, additional deity consumers, all natural progression and travel, optional full-pack compatibility, migration and equivalent-work performance gates remain open. Twenty-five loaded-world validation contexts are not full dimension gameplay acceptance.

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
