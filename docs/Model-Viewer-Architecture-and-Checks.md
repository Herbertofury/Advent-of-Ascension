# Model viewer architecture and checks

The interactive block, plant-state and workstation references now embed the same original software rendering core. A fix to its projection, texture handling or cache behavior can be applied consistently to all three views.

![Pinned source data, one shared renderer and three interactive views](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/shared-viewer-renderer-architecture.webp)

[Block models](https://herbertofury.github.io/Advent-of-Ascension/block-models.html?v=1.21.1) · [Plant states](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1) · [Workstations](https://herbertofury.github.io/Advent-of-Ascension/workstation-3d.html?v=1.21.1)

## What is shared

- View-depth and screen-projection calculations
- UV-to-screen texture transforms
- Textured triangle drawing with approximate face ordering
- Canvas pixel-density and dimension limits
- Source-image decoding and a bounded, least-recently-used promise cache
- Constant geometry preparation: face centers and pixel-space UVs

Each page retains its own source-data validation, selection controls, release boundaries and fallback text. The workstation page also retains its separate optional WebGL path. The shared core governs the software canvas path, not every renderer on the website.

## One source, no additional startup request

The canonical [original renderer source](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/viewer-renderer-core.js) is embedded byte-for-byte in each page when the documentation is assembled. It is not loaded as an additional external script at startup.

A synchronization tool and a hash check ensure the three embedded copies match the canonical source. This keeps a single maintenance point without adding a script fetch to the existing page load.

[Synchronization helper](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sync_viewer_renderer_core.py). In a checkout, run `python docs/sync_viewer_renderer_core.py`; for another folder, pass `--docs-root /path/to/docs`. The folder must contain the core and all three viewer HTML files. An isolated-folder test checks that repeated synchronization leaves the same bytes.

[Core and consumer hash receipts](https://herbertofury.github.io/Advent-of-Ascension/viewer-renderer-core-evidence.json)

## Work avoided during drawing

The source meshes are immutable within a loaded reference. Face centers and pixel-space UVs are prepared once for that model, rather than recomputed on every camera draw. Changing the view still projects and orders faces, because their screen positions and depth depend on the camera.

A deterministic check draws a prepared model 100 times and verifies that its prepared geometry is reused and its source images are not decoded again.

These are implementation checks. No browser frame-rate improvement, peak-memory figure or in-game FPS gain is claimed without a corresponding measurement.

## Cache and failure behavior

The software image cache contains at most **128 promise entries**. A cache hit refreshes its recency. An evicted, older request that subsequently fails cannot remove a newer promise for the same texture key.

The current model and in-flight operations can retain image references independently of this map, so 128 is not an absolute browser-memory limit. The block viewer separately bounds its chunk-promise cache to three entries.

Canvas drawing saves and restores its graphics state even if a draw operation throws. Each page catches a drawing failure, displays its labeled static reference, disables unusable camera controls and offers an actual reload action. It does not enter a repeated source-fetch loop.

Plant fallbacks show a multi-state sheet and say so. A sheet is not mislabeled as an exact rendering of the selected age/height state.

## Regression checks

| Check | What was compared |
|---|---|
| Shared source consistency | Three byte-identical embedded cores and no added external-script request |
| Prepared geometry reuse | Same cached geometry across 100 draws; no repeated image decode |
| Bounded LRU behavior | 128-entry capacity, recency refresh and eviction |
| Stale-failure protection | An older failed promise leaves a newer cached promise intact |
| Drawing failure recovery | All three page controllers show a fallback and a real reload path |
| Command-trace equivalence | 1,212 source-model cases at four camera views: **4,848 identical canvas-command traces** against the previous original renderer |

The 1,212 cases are 1,026 block references, 179 plant states and seven workstation cases. They overlap as documentation representations and are not 1,212 unique gameplay blocks.

Command-trace comparison uses an instrumented canvas interface. It checks the drawing commands and transforms; it is not pixel-perfect cross-browser certification, a GPU test, a Minecraft rendering test or proof of runtime mod compatibility.

## Keep these boundaries

- Software face ordering remains approximate, especially for intersecting or translucent surfaces.
- Static source models do not establish registration, obtainability or a complete restored dimension.
- Plant age/height states remain independent resources, not a growth simulation or an assembled tall plant.
- Explicit tint and fully transparent-state warnings remain visible.
- Unsupported releases and unknown selections must not silently receive a different model.
- Benchmark the actual target browser before making speed claims; benchmark the game separately before making game-performance claims.

Original renderer and explanatory diagram: documentation work for this atlas. Original AoA model and texture credits remain with Tslat and contributors. [Source and attribution boundaries](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sources-and-Credits).
