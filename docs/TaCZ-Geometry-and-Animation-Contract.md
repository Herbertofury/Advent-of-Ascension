# TaCZ geometry and glTF animation are separate contracts

[Released-class evidence](tacz-geometry-animation-contract.json) · [Native hand contract](TaCZ-Native-Hand-Contract.md) · [Model acceptance standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard)

## Verified boundary

In the inspected **TaCZ 1.20.1 / 1.1.8-hotfix2** release:

- `BonesItem` contains a list of `CubesItem` plus bone name, pivot, rotation, parent and mirror data.
- `CubesItem` describes dimensions, origin, pivot, rotation, inflation and UV data.
- `GltfManager` loads `animations/*.gltf` into `AnimationStructure` through `RawAnimationStructure`.
- That inspected raw animation type contains accessors, animations, buffers, buffer views and nodes. It does not contain mesh, material, image or skin fields.

Therefore, **the presence of a glTF loader is not proof of arbitrary GLB mesh/PBR rendering**. Renaming an exported triangle mesh or passing a JSON/parser check does not make it a ready stock TaCZ gun.

This is a scoped audit of released classes, not a claim that no third-party adapter or future TaCZ version can support other geometry.

## Two honest delivery paths

| Path | Required work | Acceptance evidence |
|---|---|---|
| Stock-compatible authored geometry | Produce geometry, materials and bones that the pinned native model path actually consumes; preserve weapon identity and useful detail | Native model load, real hand rendering, animations, attachment behavior and performance |
| Optional high-fidelity mesh backend | Implement or integrate a real triangle/material renderer and connect it to the same gameplay and animation contracts | A native rendered mesh, correct material channels, transforms, fallback, multiplayer behavior and measured cost |

The high-fidelity authoring GLB is a reference asset until the second path is implemented and tested. The world-fitting option should not inherit an untested renderer dependency.

## Keep authoring progress useful

Retain editable source geometry, texture channels, original-to-concept comparisons and explicit moving-part ownership. Test transforms and native hands separately. Keep server-side shots, ammunition, effects and progression authoritative; renderer choice must not duplicate or replace them.

A clean mesh diagnostic is valuable, but it is neither a gameplay integration test nor a native frame-time measurement.
