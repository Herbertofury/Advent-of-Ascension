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

## Still required in game

Native export/load, real hand/skin/FOV combinations, attachment-switch transitions, actual translucent rendering and aim readability, shader/Vulkan compatibility, multiplayer, persistence and measured frame times. None of those gates is passed by this source-only receipt.
