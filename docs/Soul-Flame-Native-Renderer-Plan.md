# Soul Flame native renderer: source-backed integration plan

**Pinned TaCZ source:** `MCModderAnchor/TACZ` at `b482eff8c94a733ac8d0910193fca3893954027c`. This is an implementation plan from actual source, not a compiled or game-tested adapter.

## A real extension path exists

The inspected [BedrockAnimatedModel](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/client/model/BedrockAnimatedModel.java) exposes `setFunctionalRenderer`. Its model-loading overrides precreate functional bone parts. This provides a candidate route for a dedicated animated Soul Flame leaf node without pretending the standard cube loader imports Blender shape keys or arbitrary glTF meshes.

Use a dedicated empty leaf bone for the flame. The solid candle socket, optional gem and protective armor should remain separate parts. Author the flame's local origin and aiming reference explicitly in the model.

## Important behavior that must not be missed

The actual [FunctionalBedrockPart implementation](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/client/model/FunctionalBedrockPart.java):

1. Pushes the pose and applies the bone's translation, rotation and scale before invoking its renderer.
2. Invokes the functional renderer even when the ordinary `visible` flag is false.
3. When the callback returns a renderer, normal cube/child drawing is replaced by that renderer's work. Returning null falls back to ordinary visible cube/child rendering.

Consequences: explicitly gate the flame on the resolved Soul Flame/Soul Candle attachment state; hiding a bone alone can leave a ghost flame. Never attach the custom renderer to a parent containing the entire weapon, or inadvertently suppress its descendants. Avoid applying the bone transform twice.

## Pass and buffer ownership

The inspected [BedrockModel](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/client/model/bedrock/BedrockModel.java) runs deferred renderers after the main model pass and then clears that list. Its ordinary path ends a batch before these callbacks. Do not assume the earlier vertex consumer is still the correct buffer for a new translucent effect.

The actual [MuzzleFlashRender](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/client/model/functional/MuzzleFlashRender.java) is a useful reference for capturing pose matrices and requesting appropriate effect buffers. It is not a ready-made persistent sight: its shot timing and shared static fields must not be copied into per-weapon charm/sight state. A sight needs its own well-defined render state, stable attachment ownership, pause behavior and display-context policy.

## Implementation choices to compare

- **Animated textured cards:** small bounded geometry and texture-frame or UV animation; test edge-on visibility, alpha sorting and overdraw.
- **Small procedural flame mesh:** fixed topology with bounded deformation; requires a custom vertex path, not a claim that native cube JSON supports shape keys.
- **Hybrid:** a stable small emissive core with a few restrained wisps; avoid spawning an unbounded particle stream every render frame.

The Blender study currently uses three original 300-vertex flame volumes and shape keys with fixed roots. Structural checks passed for those roots, but visual quality remains below the target and no native export, shader compatibility, aim alignment or performance acceptance is claimed.

## Acceptance tests

- [ ] Flame default, Candle optional and Gem optional render correctly, without residual flame after switching.
- [ ] Transform matches the actual named bone through idle, recoil, inspection and cancellation; no double transform.
- [ ] Separate instances, dual wield, other players and GUI previews cannot share stale pose/state.
- [ ] Correct first/third-person and shadow-pass policy; verify with the actual shader/Vulkan compatibility targets.
- [ ] No gameplay state, hit direction, resource consumption or health effects are driven by flame animation.
- [ ] Low-motion and low-flash settings retain a readable stable aiming reference.
- [ ] Measure overdraw, render submissions, allocations, texture memory and frame-time changes in the actual game.

[Sight design](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Sights) · [Customization](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization)

## Released artifact cross-check

The actual `tacz-1.20.1-1.1.8-hotfix2.jar` was also inspected. Its selected classes expose the same `setFunctionalRenderer`, `delegateRender` and functional-render callback descriptors. The released functional-part bytecode likewise invokes the callback before checking the ordinary visible fallback. [Released class hashes, method instructions and manifest](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-flame-renderer-release-evidence.json) document this narrow compatibility check. This does not certify a complete adapter, shader compatibility or game execution.


## Tested Java frame core: first integration component

[Original Java source and repeatable test runner](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-sight-java-core-v1.zip) · [Actual JDK 17 test receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-sight-java-core-v1-tests.json)

The renderer-independent core now resolves fifteen-frame UV timing from caller-supplied paused presentation time and explicit sight/pass inputs. It clears caller-owned output before every sample, gates Gem and shadow rendering off, requires GUI opt-in and provides a stable reduced-motion frame. Flame and Candle remain distinct resolved options with separately authored bone origins; the code does not invent attachment offsets.

A full Corretto 17 compile/run passed 24 attachment/pass/GUI combinations and 100,000 time samples, plus wraparound, reduced-motion, invalid-time cleanup, instance-output isolation and repeated-time checks. It contains no player-state map or per-frame inventory scan. Tests verify the pure core only: actual pause hooks, rendering, blend/filter behavior and all native acceptance gates above remain open. This source archive is not an installable mod.
