# Mesh normal fidelity: keep the sculpt’s shading through export

**Implemented offline diagnostics and a local source candidate. No native loader build or in-game acceptance.**

A model can pass JSON parsing, triangle counts and UV checks while losing its authored smooth shading. That matters for curved armor, beveled caps and the premium material mode. It is a separate gate from attractive Blender renders.

## What the released loader actually does

The inspected official Forge 1.20.1 **TaCZ Mesh Loader 0.1.8** source sets `FORCE_FLAT_SHADING = true`. Its constructor reads the input normals but selects geometric face normals for the baked arrays. The official 1.20.1 branch at review was commit `a3faaaf45ed956351278a5b6f86b4140f48439ea`; the official versions page still listed 0.1.8 for that target on 2026-10-19.

[Exact upstream source](https://github.com/VellEagle/TacZMeshLoader/blob/a3faaaf45ed956351278a5b6f86b4140f48439ea/src/main/java/com/example/taczmeshloader/core/PolyMesh.java#L30-L118) · [Official versions](https://modrinth.com/mod/tacz-mesh-loader/versions)

The original regression harness executes the **unmodified released bytecode**, with explicit graphics/logging stand-ins. Changing three authored corner normals while retaining the same geometry produces identical baked normal arrays. A syntactically valid normals field therefore does not prove authored shading survives.

## Soul Storm metal fixture: measured data differences

The fixture contains 136 opaque metal parts, 27,472 triangles and five neutral-pose mesh groups. It excludes the grip, flame, effects, hands and gameplay bindings. It is not a complete weapon model.

| Comparison | Result |
|---|---:|
| Original triangle corners inspected | 82,416 |
| Geometric-face control maximum error | 0.019717° |
| Authored-to-baked median normal difference | 14.954608° |
| 95th-percentile difference | 22.255623° |
| Maximum difference | 82.226989° |
| Corners differing by more than 5° | 48,716 |
| Corners differing by more than 20° | 8,758 |

The geometric-face control checks the diagnostic’s coordinate convention. The authored comparison uses the source’s Y-normal inversion. These are data differences, not a measured visual defect under a particular game shader. Both Java 17 and Java 21 reproduced the result.

## Local opt-in candidate

The proposed patch introduces `tml_normal_mode`, with the existing flat behavior as the default. Explicit `authored` mode normalizes each unique finite, nonzero normal once during model loading. Missing, zero, nonfinite and out-of-range normals use the geometric fallback. Invalid mode names/types are rejected clearly.

**This is not a released TML setting. Adding the field to stock 0.1.8 does not activate the proposal.** It requires a reviewed loader change and native qualification. The patch has not been installed or sent upstream.

Offline source-build checks:

- All **879,104 default baked float values** have the same digest for unmodified and patched source on Java 17 and Java 21.
- The authored path preserves **109,888 expanded fixture corners** within **2.981 × 10⁻⁸** maximum component error.
- Missing/zero/nonfinite/out-of-range normals, large finite normalization, invalid modes and empty GPU caches are exercised.
- Graphics stand-ins fail if a rendering/upload path is accidentally invoked. No game or GPU draw is tested.

Normal preprocessing is model-load-only. Default-array equality is not proof of zero startup or frame-time regression; equivalent-work measurements remain required.

## Rendering and compatibility gates remain open

The released fallback path negates the stored normals while the VBO upload path uses them directly. This is a separate parity question requiring actual native lighting tests, not permission to blindly reverse every normal.

Before adoption:

- [ ] Build against the exact native loader and verify old packs retain their appearance
- [ ] Compare authored/flat modes through actual VBO and fallback rendering
- [ ] Verify winding, culling, mirrored/nonuniform transforms and animated owners
- [ ] Test shader toggles, resource reloads, hands and material bindings
- [ ] Measure load time, memory, frame-time lows and compatibility under equivalent work

The Soul Storm texture-bake study has its own seam and atlas-quality checks. Passing this normal diagnostic does not approve those textures, the complete gun or any gameplay effect.

## Reproduce and contribute responsibly

[Source patch, original test harness and static geometry fixture](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tml-normal-fidelity-candidate-v1.zip) · [Detailed evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mesh-normal-fidelity-evidence.json)

The archive provides pinned-source/dependency checks, fail-closed stand-ins, a small opt-in patch and reproduction instructions. It does not redistribute upstream classes, dependency jars or a modified installed loader. VellEagle and contributors retain attribution; the patch’s GPL license is included. No third-party PR or issue was submitted.

[Soul Storm authoring study](Soul-Storm-Sculpt-Study) · [Weapon quality requirements](Weapon-Completeness-Standard) · [Weapon overhaul](Weapon-Overhaul)
