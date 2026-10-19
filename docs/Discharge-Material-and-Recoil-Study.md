# Discharge: material maps and cosmetic recoil

**Unaccepted export/animation studies. No playable gunpack or native performance claim.**


## V33: corrected exterior and recoil together

![Combined exterior at the top-channel recoil sample](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-combined-v33-003.png)

This combines the corrected v32-r3 rear contours with the existing three-channel recoil fixture. The decorative parts follow the weapon root, their intended scale is retained, and the original four-projectile gameplay burst remains a separate contract.

<details><summary>Middle and lower channel samples</summary>

![Middle-channel sample](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-combined-v33-168.png)

![Lower-channel sample](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-combined-v33-333.png)

</details>

- 340 integer-frame checks cover 6,120 owned-part transforms, with zero observed owner-follow or inactive-motion error.
- 119,880 quarter-frame moving-versus-other triangle-surface comparisons report no baseline or new intersections in this scene. Same-owner pieces, containment, actual hands, attachments and continuous/native interpolation remain outside this result.
- Three position clips contain 111 keys total; exported JSON is byte-identical to the data accepted by the isolated released TaCZ parser on Java 17/21. Bone binding, material glow, gameplay and actual playback remain untested.
- A clean extraction rebuilt the combined scene, reproduced all four scoped check reports apart from scene-file hashes, and produced byte-identical animation JSON.

[Small v33 build/check patch](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/discharge-combined-authoring-v33-patch.zip) · [Detailed evidence and limits](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-combined-v33-evidence.json). Build from the exact v31 input archive listed in the patch README. The patch includes the corrected root-ownership stage, avoiding another full-scene backup.

**Still unaccepted:** final concept fidelity, exportable textures, player hands, full animation/effect set, native TaCZ/TML binding, multiplayer, optional integrations and measured performance. These authoring checks do not close those gates.

# Discharge v15 material export study

This export is tied to the published v15 source, not the later receiver study. It is unaccepted for native use.

The corrected per-owner bake produces 1024×1024 base-color, emission-color and linear roughness maps. 142 separately owned parts preserve 113,160 UV corners: position and UV errors are zero; maximum corner-normal vector error is 0.00033557; the controlled owner-translation check is zero. The roughness PNG has equal RGB channels and is treated as non-color data. Its alpha is not a reliable geometry coverage mask.

The authoring chamber animation is frozen at the source frame in this atlas. Linked bump/normal effects still depend on authoring nodes; they are not exported normal maps. Native material/shader support and animated energy remain separate work. Do not present this as a completed PBR or animated texture pipeline.

The 64-sample matched render has whole-image mean absolute RGB error 0.001382, weapon crop 0.003750 and chamber crop 0.016141 on a 0–1 scale. The much larger local chamber error exposes blur that a background-heavy whole-image average would hide. Render noise is included; these numbers are not acceptance thresholds.

No sampled base-texel source-owner overlap was found. Simple 16×16 box footprints mix owners in 598 occupied blocks. This is conditional mip risk, not measured native bleeding; dilation, same-owner islands and bilinear/trilinear/anisotropic sampling still need investigation.

Rebuild with Blender 4.3.2: run bake.py, check_parts.py, then render_comparison.py. The sibling discharge-finish-study-v15 source comes from the earlier published authoring ZIP. The published atlas-mip ownership checker can reproduce mip-ownership.json. Neither native rendering, hand poses, collision, complete animation nor performance is certified.


# Discharge three-channel cosmetic recoil study

Unaccepted authoring/transport fixture based on the published v 15 exterior model, not a playable gunpack.

18 authored pieces are assigned to three independently owned channel groups, top to bottom. Each has a short recoil/recovery curve and its own glow material. The fixture uses shot starts at frames 1,166,331 at 60 fps, reflecting the baseline's nominal 55 ticks/20 TPS interval for illustration. It does not schedule game firing. Each accepted original burst still has four projectiles; channel count is not pellet count.

`check.py` evaluates 340 integer frames and 6,120 part transforms: maximum owner-follow/inactive-motion error 0, all three glow materials return to neutral outside their active window. This is not continuous collision, interpolation, hand or play-feel acceptance.

`export_clips.py` emits three position-only clips with 37 keys each,0.15 seconds long. Blender-X maps to model+Z at 4 model units per authoring unit. Maximum linear sample error over 361 points/clip is 0.003077 model units. Glow/shader keys are not exported in these clips.

The actual released TaCZ 1.1.8-hotfix 2 animation-parser bytecode accepted all 3 clips/111 keys onJava 17 andJava 21. The harness validates 18 hash-pinned released classes and five pinned library JARs; documented narrow Minecraft/logging helpers are stand-ins. This does not test a real game, native animation playback, model bones, resource binding, audio, multiplayer or performance.

To reproduce authoring checks, run Blender 4.3.2 with `--python-exit-code 1 --python build.py`, then check.py and export_clips.py. `check_released_parser.py` expects the separately documented released-tacz-parser-study cache and local Java 17/21 tools; it does not download them. Do not put these sources in a Mods folder.

A future native adapter must resolve matching bones once per asset generation, select only the confirmed channel, reconcile local prediction without adding network latency, preserve original resources/cadence and restore interrupted poses. The generic confirmed-shot component is published separately.


[Source, maps, editable scenes and tests](discharge-material-recoil-study-v1.zip) · [Required v15 authoring source](discharge-authoring-refinement-v15.zip) · [Released parser harness](tacz-released-parser-check-tool-v2.zip) · [Confirmed-shot presentation component](Confirmed-Shot-Presentation.md)
