# TaCZ model parsing — isolated upstream-code check

**A narrower export check, not a native game or renderer pass.** Eight authoring JSON files (seven distinct byte hashes, including historical variants) were parsed using nine unmodified model-POJO source files from the [official TaCZ repository at commit b482eff8c94a733ac8d0910193fca3893954027c](https://github.com/MCModderAnchor/TACZ/tree/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/client/resource/pojo/model).

## What ran

- The actual `CubesItem.Deserializer` was registered with Gson, matching the model-specific adapter used by the pinned client asset manager.
- Parsed the authored Baronator variants, Minigun variants, Soul Storm cuboid study and Iominator v3: eight files, 1,385 stored cuboids, not eight finished weapons.
- Verified per-face UV objects were populated, numeric triples remained usable and the selected models' parent order was coherent.
- Exercised the upstream mirror-inheritance behavior: an inherited true value applies when a cube does not specify mirror, while explicit false remains false.
- Compiled with a real JDK17 compiler and ran the same classes on Java17 and Java21. A fresh extraction downloaded the pinned dependencies, compiled and passed again.

The harness adds structural assertions; this does not mean the upstream parser itself validates every malformed graph, dimension or animation. These current solid models also do not exercise the intentional zero-extent effect planes found in reference packs.

## Explicit isolation boundary

The only Minecraft-facing type needed by these classes is represented here by an explicitly labeled six-value **Direction stand-in**. It is not the real Minecraft class. Forge, the actual client asset manager, GPU/rendering classes, texture loading, animation deserializers, display/state-machine bindings and the game are not launched or tested.

A successful result therefore establishes that these JSONs can populate the pinned upstream model objects under this bounded setup. It does **not** establish native loading, appearance, animation parity, hands, shader compatibility, gameplay or frame-time performance.

The source's face accessor also remaps some direction names. Exporters should follow the actual renderer's conventions and visually verify UV orientation rather than assuming a generic preview has identical face mapping.

## Reproduce

[Download our harness and original model fixtures](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tacz-model-parser-check-tool-v1.zip). With a full JDK17+ and Python, run `python run_check.py`. It fetches the nine pinned upstream Java sources plus Gson2.10, Guava31.1-jre and jsr3053.0.2 from their original public sources, verifies SHA256 values, compiles and runs the check. It does not install a mod or launch Minecraft.

Gson/Guava versions were resolved from the official Minecraft1.20.1 library manifest. The dependency/source files are not redistributed inside the harness archive; respect their respective licenses. Our fixture JSONs and original test code are included.

[Detailed receipts, source URLs, dependency hashes and input hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tacz-model-parser-isolated-check.json) · [Other clean-extraction authoring checks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Authoring-Reproducibility)


## Numeric animation follow-up

The isolated study now also uses the pinned upstream AnimationKeyframes serializer against eight authoring animation files (seven distinct hashes). The inspected files contain 101 clips and 1,162 parsed keyframes across historical variants; these totals are not unique finished animations for 101 weapons. They pass on Java17 and Java21 without unsupported-expression diagnostics.

This second harness has explicit stand-ins for numeric GsonHelper conversion, diagnostic logging and an unused ResourceLocation type. It rejects sound-effect records instead of claiming to validate them. Actual interpolation, animation/state-machine blending, audio, hands and gameplay remain outside scope.

A useful source-level boundary is now tested: the pinned serializer does not evaluate Molang-style strings. A standalone expression yields an empty channel; a string inside a vector becomes zero with a diagnostic. Our authored numeric assets must not silently rely on such strings for procedural motion. Dynamic Soul Flame frame selection therefore still needs the explicit native adapter described in its plan; a generic exported expression is not proof that it will animate.

[Animation parsing receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tacz-animation-parser-isolated-check.json) · [Numeric animation harness and original fixtures](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tacz-animation-parser-check-tool-v1.zip)


## Newer check against released bytecode

[Actual TaCZ 1.1.8-hotfix2 parser study](https://github.com/Herbertofury/Advent-of-Ascension/wiki/TaCZ-Released-Parser-Check) uses 18 unchanged class files from the official released JAR. The earlier source-compiled studies remain valid historical evidence. Both approaches retain explicit stand-ins and do not certify a native game.
