# From beautiful sculpt to a native weapon

**Pinned study: TaCZ 1.1.8-hotfix2 / Forge 1.20.1. Actual released classes inspected; native rendering is still untested.**

The Soul Storm Blender studies are valuable editable source, but a `.blend` or glTF export is not automatically a TaCZ gun model. This page records the actual boundary and the routes worth testing before more sculpting is mistaken for finished implementation.

## What the released files show

- `GltfManager` loads `AnimationStructure` from `animations/*.gltf`. The associated raw structure contains accessors, animations, buffers, buffer views and nodes. This inspected path is for animation, not proof of arbitrary glTF mesh/material import.
- `BonesItem` stores cuboids. `BedrockModel` constructs `BedrockCubeBox` or `BedrockCubePerFace` from those records.
- An **executed test using the unmodified released POJO classes** confirms that a `poly_mesh` payload is silently discarded. A mesh-only bone parses with no cuboids. A mixed bone retains its one real cuboid and drops the polygon payload. Java 17 and 21 both passed this boundary test.
- `BedrockModelPOJO.getGeometryModelNew()` selects the first geometry entry. Do not export several entries and assume all are drawn.
- The inspected `BeforeRenderHandEvent` exposes a pose stack. Its existence alone is not a complete custom renderer API.

**A successful JSON parse can therefore conceal missing geometry.** Our export gate must check recognized geometry and actual rendered output, not just “no exception.”

[Reproducible released-parser tool v2](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tacz-released-parser-check-tool-v2.zip) · [Java 17/21 results](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tacz-released-parser-check-v2.json) · [Exact class hashes and reference counts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tacz-native-mesh-boundary-evidence.json)

## Route A: native cuboid model with authored texture detail

Use the released format deliberately: purposeful rotated/beveled-looking cuboid assemblies, per-face UVs, authored textures, sensible bone hierarchy and separately validated visual effects. Compare the in-game silhouette and material response against the concept. Do not silently replace the sculpt with crude boxes and call that equivalent.

The improved presentation audit checked actual Ars Armorer, Create Armorer and Helldivers packs: **8 + 13 + 57 display records**. None of their main models in this bounded scan declared `poly_mesh` or multiple geometry entries. That is evidence for these particular files, not a statement that every addon uses the same route or that their visual quality is fully reproduced.

[Static presentation audit v2](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tacz-presentation-audit-tool-v2.zip) reports polygon payloads and multiple geometry entries alongside UV dimensions, cuboids and exact-path LOD references. Its reader supports comments/trailing commas while preserving quoted URLs; it is not a complete Gson/JSON5 implementation.

## Route B: scoped custom geometry bridge, pending native prototype

The released `BedrockCube` is an interface with a `compile(PoseStack.Pose, VertexConsumer, …)` method. `BedrockPart` holds a public list of those objects, and `BedrockModel.getNode(name)` exposes a named part. This is a **candidate extension seam**, not proof of a supported stable mesh-import API.

A prototype could attach immutable custom geometry only to our own model parts and preserve their native bone transforms. Before adopting it, demonstrate all of the following:

1. Correct vertex format, face winding, normal transforms, UVs, alpha, light and overlay in the real renderer.
2. Valid topology for the render pipeline. Do not assume triangle data or degenerate quads work with every collector.
3. Resource-reload lifecycle and installation after model availability, before any relevant geometry cache is populated.
4. First/third-person, dropped, inventory, fixed-display, attachment and LOD behavior.
5. Shader, accelerated renderer and Hari/Vulkan compatibility with identical fallback behavior and measured frame times.
6. No mutation of another pack's shared model instance and no cross-item cosmetic state leaks.

### Accelerated rendering cache warning

The shipped Accelerated Rendering compatibility mixin calls the `BedrockCube.compile` interface while building a collected mesh and reuses its cached mesh on a later cache hit. This makes the seam interesting, but also makes **dynamic vertex/UV mutation inside a cached part unsafe to assume**. A changing flame atlas or per-frame morph must use a verified dynamic route, immutable prebuilt frame parts, or explicit cache lifecycle support. Do not rebuild meshes every frame or globally disable acceleration to hide the problem.

Static source inspection does not prove cache behavior under every runtime configuration. Verify reloads, attachment swaps, alternate emitter counts and multi-player/multi-weapon displays in game before promotion.

## Acceptance rule

The Blender source stays preserved. Visual quality, native geometry, animations, materials and performance are separate gates. A parser smoke test, a render image, a candidate Java interface or a generated concept cannot substitute for an actual accepted weapon.

[Editable Soul Storm studies](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Sculpt-Study) · [Released parser scope](https://github.com/Herbertofury/Advent-of-Ascension/wiki/TaCZ-Released-Parser-Check) · [Reusable presentation core](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Presentation-Core)
