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
