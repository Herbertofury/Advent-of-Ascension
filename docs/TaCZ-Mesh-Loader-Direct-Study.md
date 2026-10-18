# TacZ Mesh Loader · existing community route for the AoA sculpt upgrade

**Priority: evaluate and improve the existing loader before building a second renderer.** TML was already in the Minecraft Mods research collection; this study advances it from a source-listed candidate to an actual source/artifact review. It is still not native acceptance for our weapons.

## Pinned inputs

- [Official project](https://modrinth.com/mod/tacz-mesh-loader), project ID `SnuAzTh0`.
- [Inspected Forge 1.20.1 release: 0.1.8](https://modrinth.com/mod/tacz-mesh-loader/version/PGQI9VTN), published 30 September 2026. Archive: **204,663 bytes**.
- [Source repository](https://github.com/VellEagle/TacZMeshLoader), 1.20.1 branch pinned to `a3faaaf45ed956351278a5b6f86b4140f48439ea`. Thirty-six source/resource/build/license files were downloaded for inspection. Bundled dependency binaries were not needed.
- The GitHub releases endpoint was empty at review time. The branch pin and published artifact are separate authorities; no exact reproducible-build equivalence is claimed.
- Actual TaCZ comparison: **1.1.8-hotfix2 / Forge 1.20.1**.

The published project also lists 1.20.1 Fabric and 1.21.1 NeoForge/Fabric variants. Those are separate artifacts with different TaCZ-port dependencies; this study does not certify them.

## What the files actually establish

1. The gun-model registration key is **`mesh`**. The inspected source and released bytecode both register that value. A source example/log says `meshy`; do not copy that stale spelling into the display JSON.
2. The loader reads indexed `poly_mesh` positions, normals, UVs and polygon corners, including normalized-UV handling. Guns use the opt-in model type; attachment/ammo/block paths have their own integration hooks.
3. Main and LOD gun model loading have dedicated hooks. The corresponding nine base-TaCZ target method declarations across five classes still exist in the inspected hotfix2 artifact. This is a static compatibility prerequisite, not proof that every Mixin injects or renders correctly.
4. The source contains a VertexConsumer fallback, VBO caching and a separate optional Accelerated Rendering integration. It also tracks shader changes and invalidates relevant caches.
5. The official guidance keeps actual hand models as **cuboids**. Do not convert the hand rig merely because the weapon body becomes a mesh.

This is a substantially more complete integration starting point than our small [immutable quad dispatch experiment](https://github.com/Herbertofury/Advent-of-Ascension/wiki/TaCZ-Native-Mesh-Route). Keep that original experiment as a diagnostic/guardrail reference, rather than starting a competing renderer without evidence of a gap.

## Source-derived authoring gates

### Triangles/quads only for our export

The inspected loader converts a source triangle into four submitted vertices by repeating its last corner, and otherwise uses the supplied polygon length. Its VBO path begins a QUADS buffer. Therefore an arbitrary five-or-more-corner polygon must **not** be assumed to be safely triangulated. Our preflight rejects n-gons and asks the authoring pipeline to triangulate them explicitly. This is a source-derived risk, not a claimed reproduced in-game failure.

The repeated corner generated internally for a triangle is an intentional rendering representation. It must not be confused with an accidentally degenerate source triangle or a broken authored quad.

### Pivot, axes and normals

The reviewed source subtracts each bone's absolute pivot, divides model positions by 16, flips model Y and flips UV V. Its flat-shading switch is enabled in the reviewed source. A Blender export must check actual coordinate conventions and normals against these transforms; simply renaming a file is not an exporter. Smooth-looking concept surfaces must be compared in game before accepting the resulting shading.

### Cache and performance

The reviewed VBO cache is bounded to eight packed-light entries per mesh, with eviction notifications and closure of discarded buffers. Bounded per-mesh caches still need an aggregate budget across many bones, weapons and light changes. Test lighting transitions, shader toggles, inventory displays, dropped weapons and reloads. Do not equate a VBO path or an AR integration with a measured FPS gain or Hari/Vulkan compatibility.

## Original preflight tool

[Download the original offline preflight and tests](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tml-authoring-preflight-v1.zip). It checks the inspected indexed triangle/quad schema, unique bones, finite/representable values, positive texture dimensions, index bounds, selected degeneracy/winding cases and authoring budgets. It warns about hand-like mesh bones and nonplanar quads. Ten synthetic regression tests pass.

This tool reads data only. It does not execute TML, install a mod, run a game or certify all collisions, materials or UV seams. Its stricter authoring budgets are ours, not universal claims about every valid upstream asset.

## Integration and contribution checklist

- [ ] Make one deliberately small AoA body-mesh fixture using the official Meshy/Blockbench route or a separately validated exporter; retain native cuboid hands.
- [ ] Check `model_type: mesh`, exact resource paths, pivots and UV orientation using the pinned 0.1.8 release.
- [ ] Native-test TaCZ hotfix2 with TML alone, then AR, shaders/Oculus, ModernFix and Hari/Vulkan individually before combined-pack testing.
- [ ] Exercise first/third-person, dropped/fixed/inventory, LOD, attachments, animated parts and interrupted inspections.
- [ ] Verify reload cleanup and cache eviction under changing packed light; measure memory, startup, frame-time tails and upload spikes.
- [ ] Prepare useful upstream fixes/tests for input validation, n-gon handling and documentation spelling if the maintainer wants them. Nothing has been submitted upstream by this study.
- [ ] Resolve the license metadata discrepancy before bundling third-party source: Modrinth reports GPL-3.0-or-later, the released JAR declares GPL-3.0-only, and the source build-property template says All Rights Reserved while LICENSE.txt contains GPLv3. Record the facts rather than silently choosing one label.

[Evidence manifest, source/artifact hashes and exact target declarations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tml-direct-study-evidence.json).

**Remaining boundary:** no native TML run, accepted Soul Storm export, hand-rig validation or measured performance result has been produced here. Credit VellEagle and the TaCZ community; this study packages only original audit tooling and findings.
