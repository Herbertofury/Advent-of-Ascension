# Discharge exterior refinement: muzzle, grip and capacitors

[Automatic 3D trial review: why the six-port generated mesh was rejected](Concept-to-Mesh-Discharge-Study). The separately authored model below remains the working source.

**Editable Blender authoring study. Not a finished TaCZ pack, native game capture or accepted weapon.**

The owner's [canonical concept A](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-owner-target-v1.png) remains the visual target. The [source weapon profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Discharge-Shotgun-Weapon-Profile) defines the gameplay baseline. Three visible muzzle channels in this artwork do not change the original four-projectile firing behavior.

## V32: layered rear-receiver study

![Current v32 oblique authoring view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-rear-v32-oblique.png)

![Current v32 side authoring view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-rear-v32-r3-side.png)

The plain rear surface now has paired swept silver braces, layered upper plates, dark insets and restrained red accents. These are decorative exterior parts; they do not establish a new mechanism. The overall receiver, grip and top construction still need substantially more refinement toward concept A. **This is not final art acceptance.**

<details><summary>Compare the preceding v31 scene from the same review camera</summary>

![Controlled v31 comparison view](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-rear-v31-comparison.png)

</details>

The scoped test preserves 164 existing mesh definitions/transforms/material-slot names and checks fourteen new closed solids for positive volume and nondegenerate evaluated triangles. It does not cover every intersection, hands, curves, driver state or native animation. The earlier trigger and guard were not resized to conceal clearance problems. All native, hand-fit, material-export and performance gates remain open.

[Small reproducible v32 patch](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/discharge-rear-contour-v32-r3-patch.zip) · [Scoped geometry results](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-rear-v32-r3-geometry.json). Apply to the exact v31 scene linked below. The patch generates a separate scene and rejects an unexpected source hash. The corrected r3 patch explicitly parents every new part to Discharge_Root; 21 root-transform samples check 10,752 vertex positions (maximum error approximately 7.18e-7 scene units). This prevents detached cosmetic parts during whole-weapon transforms; native animation and hand-fit remain untested.

## Previous v31 authoring views

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


## Recoil ownership and collision review, v4

The current exterior now has a separate **unaccepted recoil authoring study**. A deeper surface-sweep check caught problems that the earlier transform and parser tests could not detect: v2 had 101 sampled new intersections, including a moving throat entering the receiver and muzzle liners crossing horizontal trim.

The correction assigns the two associated horizontal trim pieces to each moving channel and recesses the receiver nose to make space for the stroke. It does not shrink the player's hands, trigger or guard. The resulting six-piece channel ownership keeps the housing, liner, light outline, throat and trim together. Three cosmetic channels do not change the original four-projectile gameplay burst.

![Sampled recoil poses, authoring scene only](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-recoil-v4-contact-sheet.jpg)

| Scoped check | Recorded outcome | Still not established |
|---|---|---|
| Owner transforms | 340 frames, 6,120 part samples; no owner-follow error or inactive-channel drift | Native interpolation and bone binding |
| Surface sweep | 110,556 pair samples at quarter-frame intervals; zero baseline or newly detected triangle intersections against other visible parts | Full solid containment, every possible pose, hands, attachments or minimum clearance tolerance |
| Static area | 172 visible objects, 71,756 triangles; no degenerate triangle under the test threshold | Complete topology, UV, material or LOD acceptance |
| Released TaCZ parser | Three position clips, 111 keys parse using released classes on both tested Java runtimes | Actual game integration, glow playback, sounds or gameplay |

Same-owner part pairs are excluded from the surface sweep. The checks deliberately expose their limits; a passing row is not a native release approval. Material-glow keys are not included in the exported position clips. Full-body/camera recoil, reload/inspect states, networking and performance remain separate work.

[Download editable recoil study and reproducible Blender checks](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/discharge-recoil-authoring-v4.zip) · [Scoped results](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-recoil-v4-evidence.json). Earlier exterior and concept studies remain preserved above.

### R3 visual regression correction

A later rendered combined scene exposed oversized cosmetic fasteners in r2. Parenting had captured a stale world matrix immediately after scale assignment. R3 updates the dependency graph first and adds six explicit dimension checks. All 512 added vertices match the pre-parenting v1 positions with zero observed drift, and the corrected side scene was rendered again. Use the r3 patch above; r2 is superseded. This is why positive-volume and transform-following tests alone do not constitute visual QA.

## Combined motion review

[The v33 combined exterior/recoil study](Discharge-Material-and-Recoil-Study) uses the corrected root-owned rear parts with the three-channel cosmetic animation, clean rebuild checks and sampled moving-surface comparisons. It remains below native and final-art acceptance.

## V34: curved capacitor canopies

![Current curved-sheet capacitor study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-capacitor-canopy-v34.png)

Two small curved armor sheets replace the visible thin cross-ribs, giving the paired capacitor structures a more coherent folded-shell silhouette. The original ribs are retained hidden. This is an incremental shape study; the complete weapon still needs substantially stronger concept fidelity and final texture work.

The two added closed solids have 348 evaluated triangles each. The inherited recoil sweep reports 119,880 moving-versus-other surface comparisons without baseline/new intersections in this scene. Those checks do not establish hands, containment, continuous collision or native rendering.

[Reproducible v34 canopy patch](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/discharge-capacitor-canopy-v34-patch.zip) · [Scoped evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-capacitor-canopy-v34-evidence.json). Apply to the generated v33 scene with its manifest. Native and final-art acceptance remain open.

## V36: grip follow-through

[The current grip and surface study](Discharge-Grip-and-Surface-Study) places the finger contours below the retained guard return, adds finer patterned inlays and includes a reproducible source archive. Its static seating and preservation checks are separate from the v35 texture/export evidence. Native hand fit, swept clearances and full concept fidelity remain open.
