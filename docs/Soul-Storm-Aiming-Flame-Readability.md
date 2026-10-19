# Soul Storm · Aiming flame readability

[Weapon profile](Soul-Storm-Weapon-Profile) · [Sculpt study](Soul-Storm-Sculpt-Study) · [Mesh normal fidelity](Mesh-Normal-Fidelity-and-Opt-In)

## A clear center without losing the living flame

The default Soul Storm sight is a living soul flame that forms a focused crosshair. The flame-card enlargement introduced an authoring defect: during the aiming transition, its shader aperture no longer followed the sight center. The flame could cover the intended target marker even though the fully focused endpoint looked correct.

![Controlled before and after at halfway focus](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-aim-mask-v34-comparison.webp)

**This is a controlled Blender authoring comparison, not a Minecraft screenshot or native first-person acceptance.** Both sides use the same camera, marker, lighting, frame and render settings. The pink square is a deliberately contrasting QA marker behind the sight.

## Scoped correction

The v34 patch changes four shader-driver expressions. The mask center and distance metric now track the flame card's changing dimensions. A smooth opening through focus 0–0.35 clears the central aiming area earlier. The relaxed flame, fully focused sight, geometry and existing motion are preserved in the checks below.

| Check | Result | Limit |
|---|---|---|
| Evaluated mask center | 202 card samples over 101 frames; maximum error 0.0000006744 world units | Authoring coordinates only |
| Raw geometry | Exact hash equality for mesh positions, topology, UVs, shape keys and parent names | Shader changes intentionally excluded |
| Sampled evaluated motion | Exact hash equality over 101 frames for 438 mesh objects | Sampled animation, not continuous collision proof |
| Relaxed render | Pixel-identical | Controlled orthographic camera |
| Fully focused render | Pixel-identical | Controlled orthographic camera |
| Halfway transition | Marker is visibly exposed through the center | No native gameplay readability claim |

[Machine-readable evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-aim-mask-v34-evidence.json)

## Reproduce and edit

[Download the small patch bundle](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/soul-storm-aim-mask-v34-patch.zip). It requires the existing [v33-R6 editable texture-study scene](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-metal-texture-study-v33.zip); its SHA-256 is checked before applying changes. The bundle contains the build script, controlled render setup, anchor test and geometry-preservation test. It avoids duplicating the complete source scene in another archive.

Tested with Blender 4.3.2. Follow README.md in the bundle. Retain the original scene for comparison and rollback.

## Required next quality gates

- [ ] Bind the effect to the actual native aiming state and verify the native camera.
- [ ] Test changing FOV, resolution, bright and dark backgrounds, and moving targets.
- [ ] Verify hand fit, view obstruction and aim accessibility options.
- [ ] Confirm no gameplay, networking, compatibility or equivalent-work performance regression.
- [ ] Complete the wider weapon proportion, texture and concept-fidelity review.

This is a bounded authoring improvement. It does not mark Soul Storm or any other weapon as complete or playable.
