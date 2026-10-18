# TaCZ released-bytecode parser checks

**Executed against the actual 1.20.1 / 1.1.8-hotfix2 release in isolated Java 17 and Java 21 harnesses. Native game acceptance remains open.**

This closes a specific gap in the earlier source-compiled parser study: the model and animation classes now come directly from the released JAR, unchanged, instead of being rebuilt from a possibly different source snapshot.

## Exact inputs and boundary

- [Official CurseForge file 9037989](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero/files/9037989), uploaded 2 October 2026.
- [Matching Modrinth release AzCBJlex](https://modrinth.com/mod/timeless-and-classics-zero/version/AzCBJlex); full archive SHA-512 and 18 class SHA-256 values are pinned in the tool manifest.
- Only the selected model/animation class bytes enter the test classpath. The complete mod entrypoint and Forge/Minecraft runtime are absent.
- Explicit stand-ins remain: six-value Direction enum; the used GsonHelper numeric conversion; GunMod plus a narrow logger diagnostic sink; an unused ResourceLocation POJO type placeholder.

The production file is newer than the latest GitHub release entry returned during the refresh. Its changelog lists a backported vulnerability fix. Use the exact artifact ID/hash when reproducing; a GitHub release title alone is not a complete production-version check.

## Results

| Check | Observed result |
|---|---|
| Models | Eight historical JSON files, seven unique hashes, 1,385 stored cuboids parsed |
| Animations | Eight historical JSON files, seven unique hashes, 101 clips and 1,162 keys parsed |
| Weapon identities represented | Baronator, Minigun, Soul Storm and Iominator |
| Mirroring | Bone-inherited mirror and explicit cube `false` fixture pass |
| Face UV lookup | Six distinct face UV values exercise the released getFace convention |
| Numeric scalar | Scalar 2 expands to the tested three-component vector |
| Unsupported expression fixtures | Standalone expression yields an empty channel; a string vector component falls back to zero with diagnostics |
| Authored numeric inputs | No unsupported-expression diagnostic was produced |
| JVMs | Same Java-17-compiled harness passes on Java 17 and Java 21 |

These totals include preserved variants; they are not eight finished weapons. **The Soul Storm v13 Blender sculpt is not one of these TaCZ JSON inputs.** No new mesh/export acceptance is implied for it.

The face lookup intentionally exposes a native convention that an exporter must respect: the tested EAST/WEST and UP/DOWN lookups select the corresponding opposite named UV entries, while NORTH/SOUTH keep their names. This is a POJO lookup observation, not a world-space orientation bug or a rendered UV acceptance test.

[Full results and limitations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tacz-released-parser-check.json) · [Original reproducible harness and authoring fixtures](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tacz-released-parser-check-tool-v1.zip)

## What remains mandatory

Native resource loading, attachment registration, actual model rendering, transform/interpolation playback, hands/FOV, sound callbacks, shader passes, multiplayer state, original resource/damage behavior, migration and measured performance remain separate gates. A passing data parser cannot prove those systems work.

The harness rejects sound-effect inputs and does not pretend to execute them. It pins every input file and refuses an empty/missing fixture set. Upstream classes and third-party JARs are fetched or supplied locally, not redistributed in the tool archive.

[Earlier source-based parser checks](TaCZ-Isolated-Model-Parser-Check) · [Versioned native adapters](Versioned-Weapon-Adapters) · [Weapon authoring reproducibility](Weapon-Authoring-Reproducibility)
