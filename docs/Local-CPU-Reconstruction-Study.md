# Local CPU reconstruction trial

**Decision: usable as a rough modeling reference only; reject as a finished weapon asset.**

The official MIT-licensed TripoSR source was checked out at 107cefdc244c39106fa830359024f6a2f1c78871. Public model revision 5b521936b01fbe1890f6f9baed0254ab6351c04a was downloaded with its advertised LFS content hash verified. The model weights are not redistributed in this study.

This trial runs locally on CPU with PyTorch 2.6.0+cpu and four computation threads. An explicitly documented scikit-image adapter replaces torchmcubes surface extraction. Its positive-inside analytic ellipsoid fixture checks axis ordering and outward winding against the actual TripoSR helper contract. This is not an unchanged official pipeline or an A100 performance claim.

## Results

- Discharge, 128-grid: 5,136 vertices, 10,272 triangles, one connected component, watertight, no faces at or below the chosen 1e-12 area threshold.
- Apoco, 128-grid: 6,421 vertices, 12,834 triangles, three connected components, watertight, no faces at or below that threshold.
- Apoco, 256-grid: 28,368 vertices, 56,708 triangles, ten connected components. Three faces have area at or below 1e-12, but none have exactly zero area. Higher extraction resolution reused the saved scene code rather than repeating image inference.

The GLB and PLY exports were actually produced and reopened in Blender. Five review views were rendered. An initially cropped top view was corrected by increasing its camera framing.

## What passed, and what did not

The experiment successfully produced inspectable geometry instead of only a remote-service preview. Basic finite-coordinate, connected-component and surface checks are useful technical evidence.

Visual review still finds soft/melted edges, blurred color detail, invented hidden surfaces, lost mechanical separation and incomplete negative spaces. Increased extraction resolution improves surface sampling but does not turn the reconstruction into the selected AAA concept. Ten disconnected components are not ten authored moving parts. Nothing here proves hand fit, clipping-free animation, believable resource service, native material behavior or gameplay.

Keep the original concepts and authored meshes. Use these outputs to inspect overall volume and plan deliberate retopology and component construction. Do not ship them as canonical finished weapons, increase completion counts, or reuse their baked lighting as validated PBR materials.

## Reproduction scope

The bundle contains our wrappers, the CPU adapter and fixture, dependency freeze, source/model receipts, result reports, generated input images, saved Apoco scene code and reference meshes. It excludes model weights, environments, caches and upstream source. Obtain the official source and model separately under their licenses. The scripts expect the established study layout; adjust explicit input/output paths for another workspace.

Sources: https://github.com/VAST-AI-Research/TripoSR and https://huggingface.co/stabilityai/TripoSR .

## Minimal invocation after installing the pinned dependencies

Place the pinned TripoSR checkout in source/ beside the study scripts. Download the public model with download_model.py. Then use run_cpu_v2.py --input inputs/discharge.png --out discharge-run --name discharge, or substitute inputs/apoco.png and an apoco output folder. Set HF_HOME and U2NET_HOME to writable workspace directories. extract_cached.py uses the included apoco-run-v1/scene-codes.pt for the recorded 256-grid comparison. Native game integration is deliberately absent.
