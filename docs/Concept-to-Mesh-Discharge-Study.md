# Discharge concept-to-mesh study

**Current decision: generated mesh rejected as the canonical upgrade.** Keep the owner-selected three-port concept and the separately authored model. A successful generation process does not establish art or native-game acceptance.

[Current editable Discharge work](Discharge-Exterior-Refinement) · [Original weapon behavior](Discharge-Shotgun-Weapon-Profile) · [Full quality standard](Weapon-Completeness-Standard)

## Local CPU follow-up · 2026-10-19

A separate local `trellis.cpp` run completed at 1024 resolution using q8 models, eight CPU threads, 12 steps, a 120,000-face target and a 2048 texture atlas. It produced an actual GLB, which was imported and rendered from six views.

![Generated Discharge mesh, rejected as the canonical weapon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-cpu-mesh-oblique.png)

The obvious concept mismatch is the **six muzzle openings in two columns**, whereas the selected design requires three. Soft/fused forms, invented hidden-side details and orange/gray surface drift also remain. A nice-looking oblique render cannot waive those defects.

### Trial input and limits

![Isolated image-to-3D trial input, not a replacement canonical concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-cpu-input-reference.png)

This isolated trial reference is a generation input. It does not replace the original concept sheet or authorize invented geometry on unseen sides. Each generated surface must still be checked against the actual design.

### Numeric evidence

| Check | Observed result | Meaning |
|---|---:|---|
| Process result | Exit 0; 7,431.85 seconds | Generation completed; about 124 minutes on this CPU setup |
| Peak process RSS | 3,513,608 KiB | Process memory observation, not a Minecraft memory/FPS result |
| Output triangles | 115,136 | Actual output, below the requested target |
| Texture atlas | 2048 × 2048 | Does not guarantee appropriate materials or texel usage |
| Strict UV preflight | 4 collapsed/near-zero-area UV faces | Fails the checked export subset |
| Position-welded boundary edges | 0 | Does not alone establish a manifold mesh |
| Position-welded non-manifold edges | 144 | Topology still fails manifold acceptance |
| Native acceptance | None | No game installation, animation binding or performance certification |

The many index-based components/boundaries include UV-seam splits. They must not be reported as thousands of detached physical pieces. Position-welded analysis is a separate diagnostic and still finds non-manifold edges.

![Six actual generated-mesh inspection views](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-cpu-mesh-six-views.jpg)

## What happens next

1. Keep the generated result as an experimental reference, without replacing the authored Discharge model.
2. Preserve three cosmetic muzzle ports and the original four-projectile gameplay distinction.
3. Author separate moving components and deliberate negative spaces; check the actual hand and full animation paths.
4. Repair/export UVs only after concept fidelity is correct. A clean UV report cannot repair the wrong silhouette or invented ports.
5. Verify original identity, attachments, materials, effects, sound and gameplay in the target runtime before accepting a release.

[Machine-readable result and rejection reasons](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-cpu-mesh-review.json)

<details>
<summary>Earlier hosted-service and visual-hull experiments, preserved as historical context</summary>

The following record describes earlier attempts. Its model version references are historical; current authored work is linked above.

# Discharge concept-to-mesh study

Status: **reference studies only; no finished weapon accepted**. The first-target arsenal still contains 228 IDs, with historical/version-exclusive weapons additional scope. A good silhouette or valid mesh is not a complete weapon.

## What was actually attempted

The owner-selected Core Discharge Scattercaster concept remains canonical. A transparent, complete-gun cutout was generated for image-to-3D trials; the original concept was preserved. The first crop was rejected for tight/clipped framing; the second was retained as a trial input, not as a new canonical design.

- [Microsoft TRELLIS.2](https://huggingface.co/spaces/microsoft/TRELLIS.2) produced eight-camera previews. Its GLB extraction failed at both 300,000/2048 and 100,000/1024 face-target/texture settings. No original generated mesh was downloaded.
- A credential-free API upload was denied by the network proxy. That route was stopped; no access-control workaround was attempted.
- The older official TRELLIS link redirected to the [community demo](https://huggingface.co/spaces/trellis-community/TRELLIS). One seeded generation/extraction request also returned empty error panels; the Download GLB control yielded no file.
- Hunyuan3D 2.1 was inspected but not used because its published output-license territorial limitations complicate broad mod distribution.

No cause is assigned to the generic service errors. An unrelated upstream bug report is not proof of our failure's cause.

## Local reference-volume reconstruction

Authorized preview silhouettes were used to construct a separate local visual hull. This is **not the TRELLIS source mesh**, nor a recovery of its topology or PBR maps. Eight calibrated camera masks constrain a voxel volume; marching cubes creates an approximate surface, with preview projections used only as reference color.

The 256-grid study has 64,611 vertices and 128,974 triangles. Local checks found no nonfinite vertices, degenerate triangles, boundary edges or nonmanifold edges. Observed-view silhouette intersection-over-union ranged from 0.962 to 0.976.

**Visual decision: reject as a shipping asset.** The front and oblique views still reveal projection tears, doubled details and missing cavities. The geometry has no authored moving-part ownership, grip/hand clearance validation, rig, gameplay integration or native performance evidence. Increasing resolution did not solve those problems.

## How this can help the actual weapon

1. Use the reference volume to compare receiver, crown, muzzle, grip and rear assembly proportions against the canonical sheet.
2. Author clean separate components with meaningful pivots and physically readable energy/feed paths. Preserve the intentional negative spaces instead of covering them with projected color.
3. Build an original UV/material pass with controlled texel density, purposeful detail and bounded emissive regions. Reprojected JPEGs are not final texture work.
4. Validate moving-part paths and actual native hand anchors before animating detailed reload/service/inspect sequences.
5. Complete all effects, modular attachments, variants, crafting and documented gameplay behavior under the [Complete Weapon Standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).
6. Compare concept, model and native footage side by side. Ask whether the silhouette is recognizable, whether the feedback is satisfying, and whether the weapon is actually enjoyable to use. Record specific failures, not an unsupported “AAA” score.

## Evidence

The research bundle contains the original reconstruction scripts, exact trial settings, preview provenance, numeric reports and rejected visual-review decisions. It does not bundle third-party program code or imply that a hosted preview is a native Minecraft render.

The canonical authored Discharge v7 remains separately preserved. Neither that model nor this reference hull has final visual or native gameplay acceptance.


</details>
