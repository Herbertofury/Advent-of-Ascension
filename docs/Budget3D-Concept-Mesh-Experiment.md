# Budget3D concept-to-mesh experiment

**2026-11-15 status: preflight completed; generation blocked, no new mesh produced.** Budget3D is an experimental challenger, not the winning or rejected production method. Keep the current authored workflow and all comparison evidence until an actual same-input trial establishes a better result.

## What was verified

[Budget3D's official project page](https://budgetany.github.io/budget3d/) was inspected in a live browser. Its interactive object selector is a **pre-rendered 36-view comparison**, not an upload/generation service. No concept upload or new-object generation control was present. Website sample objects are not an AoA trial.

The [pinned source](https://github.com/BudgetAny/Budget3D/tree/31bc02c0a30b245fbccc74dc7f550e1945df0b84) generates **3D Gaussian splats in PLY**, not a polygonal weapon mesh. The [sample entry point](https://github.com/BudgetAny/Budget3D/blob/31bc02c0a30b245fbccc74dc7f550e1945df0b84/scripts/sample.py) calls Gaussian decoding and `save_ply`. A PLY suffix does not establish triangle topology, UVs, rigging or game export. The inspected repository tree and usage contain no mesh extraction stage. A separate, validated splat-to-mesh conversion is therefore a prerequisite to compare finished meshes; rendering splats or triangulating their centers is not proof of a faithful surface.

## Exact input and existing comparator

Use the existing **Discharge isolated trial reference**, not a new image with easier geometry:

- [Input PNG](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-cpu-input-reference.png), 2172 × 724 RGBA, inspected visually in this pass.
- SHA256: `525e9eb7e70a349e2ae6f6407a5898bdaff4484347289fd3a736a9c283c2513a`.
- The image is a complete side/oblique fictional weapon with a strongly elongated silhouette and three stacked muzzle-port assemblies. It is suitable as the same-input challenge, but its aspect ratio makes crop preservation a mandatory check. It is not a canonical replacement concept.
- [Existing TRELLIS CPU trial and authored-work decision](Concept-to-Mesh-Discharge-Study): 115,136 triangles; 7,431.85 seconds; 3,513,608 KiB peak process RSS. The old generated result has six openings rather than the intended three, four collapsed/near-zero UV faces and 144 position-welded non-manifold edges. These are recorded prior measurements, not rerun here.
- The old generated mesh remains rejected as the canonical upgrade. The separately authored model remains preserved; it is not automatically a fully accepted game weapon either.

Do not compare Budget3D's vendor sampling times on H100/RTX PRO 6000 with this prior CPU end-to-end time as a speedup claim. Include download/preparation, compilation, sampling, decoding, conversion, cleanup and export separately, and record device and precision.

## Resource and license preflight

The [pinned README](https://github.com/BudgetAny/Budget3D/blob/31bc02c0a30b245fbccc74dc7f550e1945df0b84/README.md) documents Python 3.10+ and a CUDA GPU; [requirements](https://github.com/BudgetAny/Budget3D/blob/31bc02c0a30b245fbccc74dc7f550e1945df0b84/requirements.txt) name a tested CUDA 12.8 setup. The entry point has a CPU device fallback, but this does not prove the complete encoder/decoder pipeline is supported or practical on CPU. No full CPU inference was run.

The available cloud executor had no NVIDIA device or PyTorch installation, about 2.5 GiB available RAM at inspection, and no swap. The connected-computer inventory offered no online GPU workstation. Installing the multi-model pipeline without enough verified capacity is not an experiment result. No weights, credentials, paid compute, or third-party inference uploads were used.

Licenses are separate:

- Budget3D code: MIT; Budget3D/Idol weights: Apache-2.0 according to the pinned upstream release statement. Preserve notices and pin actual downloaded model revisions and hashes before running.
- [DINOv3](https://github.com/facebookresearch/dinov3/blob/main/LICENSE.md): custom license, not Apache or MIT. Its agreement and authorized weight access must be satisfied; using a converter or another download URL does not waive them. Research attribution and redistribution obligations apply. This experiment concerns fictional game artwork, not real weapon design.
- The [actual encoder source](https://github.com/BudgetAny/Budget3D/blob/31bc02c0a30b245fbccc74dc7f550e1945df0b84/budget3d/models/encoders.py) defaults to the VAE from [FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B), whose official card identifies Apache-2.0. Do not confuse it with the separately licensed FLUX.2-dev model or download the full unrelated diffusion model. Verify exact VAE revision/notices before use.
- No blanket redistribution permission is inferred for model dependencies, upstream game assets, generated references or conversion tools.

## Bounded continuation recipe

On an authorized machine with suitable CUDA, storage and RAM, inspect the exact model files and dependencies, obtain authorized access where required, then use an isolated environment. Preserve the baseline and the original reference bytes.

Run Turbo first at budgets 1.0, 0.7 and 0.4 with the same seed 42 and synthetic image mode. A representative command, **not executed in this pass**, after prerequisites and pinned weights are ready:

```sh
python scripts/sample.py --ckpt weights/turbo/budget3d_idol_turbo.safetensors --turbo --image discharge-cpu-input-reference.png --mode synthetic --budget 1.0 --seed 42 --out results/discharge-turbo-b100.ply
```

Use separate weight directories so Idol and Turbo `config.json` files do not overwrite one another. Start without `--fast`; measure cold and warmed compiled mode separately if evaluated. Retain the emitted `_input.png` and reject clipped/cropped or distorted conditioning before spending on conversion. Pin the upstream Idol SDK and all downloaded revisions, preserve stdout/stderr, elapsed time and peak memory, and hash every result.

For each real generated PLY, verify its representation before claiming mesh statistics. Select and license-review a conversion method that consumes the actual representation; retain the raw splats and conversion settings. If no reliable conversion exists, classify Budget3D as a reference-render candidate rather than a mesh-production replacement.

## Winner criteria and open result

Compare six matched views plus native first-/third-person views. Score silhouette and intended port count first, then cavities/negative spaces, thin details, hidden-side inventions, palette/material preservation, welded topology, UV degeneracy, editable part ownership, hand clearance and animation interruption. Include artist repair time, final triangle/texture budget and native frame-time/memory. A fast ugly or unriggable surface loses; a prettier render alone cannot pass export or gameplay.

Promote only a method that improves the target result with the required behavior intact. Keep one chosen production route once evidence supports it, while preserving failed experiments and rollback material rather than deleting history. **Current comparison: not run. Winner: undecided. Native acceptance: none.**

Next blocker to resolve is an adequately provisioned authorized executor and model-access/license preflight, followed by a real splat-to-mesh extraction trial. Nothing in this page marks the arsenal, the Discharge weapon or the requested experiment complete.

## SuGaR conversion lead: unproven, not a drop-in converter

Reviewed 2026-11-15 against [SuGaR commit 7c10c4a](https://github.com/Anttwo/SuGaR/tree/7c10c4ae4a267dece512f5c7f40ed212a0a2ab44). Its [documented pipeline](https://github.com/Anttwo/SuGaR/blob/7c10c4ae4a267dece512f5c7f40ed212a0a2ab44/README.md) can extract a textured OBJ after Gaussian surface alignment and refinement. It expects a COLMAP scene plus a vanilla 3DGS checkpoint, not merely an arbitrary PLY. The nominal low-poly preset still targets 200,000 vertices: not an AoA-ready budget. Requirements include a compatible C++ compiler/CUDA 11.8 stack; the README flags Windows path incompatibilities. Keep this environment separate from Budget3D's newer dependency stack.

[Loader inspection](https://github.com/Anttwo/SuGaR/blob/7c10c4ae4a267dece512f5c7f40ed212a0a2ab44/sugar_scene/gs_model.py) confirms it loads camera/image data before reading `point_cloud/iteration_<n>/point_cloud.ply`, defaults to spherical-harmonic degree 3, and allocates CUDA tensors. Budget3D's standalone decoded Gaussian PLY is therefore insufficient by itself. PLY attribute/SH conventions, coordinate frames, scale, camera intrinsics/extrinsics and image correspondence must be checked before even claiming loader compatibility. Rendering synthetic views and constructing a calibrated scene is a possible adapter experiment, not a demonstrated solution or independent ground truth.

[SuGaR's license](https://github.com/Anttwo/SuGaR/blob/7c10c4ae4a267dece512f5c7f40ed212a0a2ab44/LICENSE.md) permits research/evaluation noncommercially and requires prior consent for other uses; it is not a permissive production dependency. Do not assume generated-asset distribution rights are settled by source availability. No SuGaR code was installed/run and no weights or datasets downloaded. Status: research candidate only; GPU availability does not alone resolve the input-adapter and licensing questions. No change to the undecided method comparison.
