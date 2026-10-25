# Reproducible weapon authoring tests

A clean extraction of seven published authoring studies now runs **21/21 Node test suites successfully**. This is a repeatable authoring check, not native Minecraft/TaCZ acceptance or approval of the models’ appearance.

## Run it yourself

1. Clone or download this repository with its `docs` files.
2. Download and extract the [QA runner](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/authoring-qa-runner-v1.zip).
3. Install Python 3.10+ and Node, then run:

```sh
python run_authoring_qa.py --docs /path/to/Advent-of-Ascension/docs --report result.json
```

The runner verifies all ten input files against pinned SHA-256 hashes, extracts into a temporary directory, supplies the exact three viewer HTML inputs and requires all 21 suites to pass. It does not silently change expected hashes or mutate the original archives. Current receipt used Node v24.19.0; other runtimes require their own run.

[Complete test output and input hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/authoring-qa-clean-extraction.json)

## What this checks

- Baronator accepted-shot alternation, duplicate and rejected event handling, recoil recovery, flash positions, finite transforms, sampled bore/feed/hand clearances and attachment assembly/viewer behavior.
- Minigun rotor timing, feed/bore geometry and simulated viewer idle/pause behavior.
- Soul Storm emitter and hand-envelope authoring checks, cosmetic recoil, bounded cosmetic particles and simulated viewer lifecycle.
- Customization data validation, inspection cancellation/timing and 10,000 flame-atlas samples.

The tests remain distinct: an animation test passing does not waive the bore or hand checks. Sampled clearances do not prove continuous collision freedom.

## A real packaging defect fixed

The original Baronator mechanism archive contained an alternation test targeting an absent historical `baronator-v2` folder and expecting 109 cuboids. The separate older prototype has 103, so substituting it would test the wrong artifact. The [revised mechanism study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-mechanism-study-qa-v2.zip) targets its own packaged 132-cuboid model and preserves the animation/event assertions. No geometry was changed to satisfy the test. The original archive remains available for provenance.

The viewer suites also depended on sibling HTML files. The runner now stages those exact published files explicitly rather than relying on an old workspace layout.

## Additional upstream-parser check

[Isolated TaCZ model parsing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/TaCZ-Isolated-Model-Parser-Check) now exercises the pinned upstream model POJOs and CubesItem deserializer against eight authoring files (seven distinct hashes). It passes on Java17 and Java21, including a clean extraction/fetch/compile run. Its Direction enum is an explicit harness stand-in; it does not launch the client, renderer or game and does not close native acceptance.

## Still required in game

Native export/load, real hand/skin/FOV combinations, attachment-switch transitions, actual translucent rendering and aim readability, shader/Vulkan compatibility, multiplayer, persistence and measured frame times. None of those gates is passed by this source-only receipt.

## Tommy donor-mount correction and v20 authoring check — 25 October 2026

The current authoring study restores the original donor drum orientation and high mounting position. The rejected side-facing/low adapter is reference-only. Short and long box alternatives use their actual donor meshes, not a stretched substitute. Original donor geometry and notices remain preserved, with credit to Khan / Khan_offline and Murasame_chaan.

Three independently reopened Blender 4.3.2 variants replay their saved geometry and owner references and bind to their exact static export contracts. Thirteen metadata/selection tests pass, including negative tests for simultaneous magazines, a wrong rest frame, reactivated retired geometry and unverified production/reload promotion. Fifty-four stored pose snapshots are explicitly reference-only, not continuous native animations.

[Exact v20 evidence and hashes](tommy-v20-authoring-evidence.json)

A source-informed discrete reload study checks 712 samples and still finds receiver boundary-contact candidates in 47 samples. These are unresolved, not waived because the original donor also has some source-surface contacts. The study does not include native controller blends, complete hand geometry, continuous collision proof or native rendering. The long box's static authored-surface check is separate from its original donor catch/ammunition/grip contacts.

The [new drum concept](weapon-concepts.html?weapon=aoa3%3Atommy) is an art candidate; the older box concept remains an alternate. Model silhouette/material fidelity, normal-sized hand fit, reload/inspect ownership and cancellation, native mesh/texture export, AoA behavior, Hari/Vulkan compatibility and performance all remain open. **No native weapon acceptance is claimed.**

Reusable safeguards: compare the donor's actual orientation and mounting before changing proportions; preserve alternates without enabling them simultaneously; bind saved scenes to their exact contract; reject release promotion while contacts or native verification remain unresolved. Never move a magazine merely to conceal an incompatible receiver.
