# Discharge exterior refinement: muzzle, grip and capacitors

**Editable Blender authoring study. Not a finished TaCZ pack, native game capture or accepted weapon.**

The owner's [canonical concept A](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-owner-target-v1.png) remains the visual target. The [source weapon profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Discharge-Shotgun-Weapon-Profile) defines the gameplay baseline. Three visible muzzle channels in this artwork do not change the original four-projectile firing behavior.

## Current authoring views

![Discharge current exterior study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-exterior-v31-oblique.png)

![Discharge side comparison view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-exterior-v31-side.png)

![Discharge top view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-exterior-v31-top.png)

These views expose the actual modeled surfaces, including the unfinished rear housing and simplified top construction. They are inspection renders, not evidence of gameplay quality.

## Changes made

- Rebuilt the three stacked muzzle housings with more deliberate aperture proportions and recessed red borders.
- Restored six shallow decorative side recesses using the official Manifold3D geometry library after two Blender Boolean trials failed topology checks. The failed trials remain rejected.
- Gave outer muzzle surfaces the existing light armor finish while keeping recesses and inner channels dark.
- Added stronger finger scallops and a gentle palm swell without shrinking the trigger or guard to hide clearance problems.
- Adjusted both capacitor assemblies together, including their paired shell, light, border and bridging parts, to reduce excessive height and improve their forward lean.

## What the checks establish

| Check | Result | Boundary |
|---|---|---|
| Three new recessed housing meshes | 1,348 triangles each; zero nonmanifold edges and zero near-zero triangles in the tested meshes | Does not certify the entire weapon's topology |
| Recess volume | About 97.03% retained per housing | Cosmetic shape-conservation check only |
| Full visible evaluated scene | 172 objects, 71,756 triangles, no degenerate triangles under the recorded world-area threshold | Not a complete intersection, normal, UV or LOD audit |
| Packaged scene reopened | Same visible object/triangle count and area-test result | Blender authoring portability only |
| External image dependencies | None required by the packaged scene | Procedural materials still need a native-compatible bake/export |
| Native game / hands / animation | Not tested | No acceptance or performance claim |

The decorative recesses are shallow modeled features; they do not establish functional ventilation or a real mechanism. Sampled aperture checks from earlier stages are not complete projectile collision proof. The concept and authoring scene deliberately remain below the release gate.

## Remaining visual work

1. Replace the broad plain rear receiver surfaces with the layered, contoured construction visible in concept A.
2. Refine the grip ornament, silhouette and actual player-hand fit across aim, fire, inspect and interruption poses.
3. Improve the capacitor plate shapes and seating. The current top view still exposes simplified construction.
4. Produce deliberate, exportable textures for both the Minecraft-fitting and concept-fidelity modes.
5. Implement and test the complete animations, effects, attachment combinations, native TaCZ/TML integration, multiplayer and measured performance.

## Editable study and reproducible scoped check

[Download the compact authoring-study archive](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/discharge-exterior-authoring-study-v31.zip). It contains the editable Blender scene, the scoped geometry-check script, recorded results and limits. Open with Blender 4.3.2 or a separately validated compatible version. This archive is not installable as a Minecraft mod.

[Machine-readable review](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-exterior-v31-evidence.json) · [Original concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-owner-target-v1.png) · [Weapon completeness requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard)
