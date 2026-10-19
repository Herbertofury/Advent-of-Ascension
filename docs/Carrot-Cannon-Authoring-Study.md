# Carrot Cannon authoring study

**Work in progress. This is an editable source study, not a playable TaCZ pack or accepted final artwork.** The preserved concept remains the visual target.

[Download editable source, texture, animation and checks](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/carrot-cannon-authoring-study-v1.zip) · [Versioned file hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/carrot-cannon-authoring-receipt.json)

![Unaccepted authoring render, still below the concept target](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-authoring-unaccepted-v12.png)

## What is authored

- Individually editable orange shell pieces, metal collars, faceted amber details, leaf blades and root-grip components.
- A generated painted orange surface with recorded prompt, source hash and cylindrical UV mapping across 96 shell pieces. It is a stylized color texture with painted shading, not measured physical albedo or a complete native PBR set.
- A presentation rig for whole-weapon recovery and a separately pivoted trigger. The 48-frame/60-FPS timeline is an authoring fixture informed by the original delay input, not a verified native firing schedule.
- Source-space, geometry, orientation and sampled movement checks. Original gameplay values, ammo identity and projectile behavior are not modified by these assets.

## Defects found and corrected during this pass

1. Automatic single-image reconstruction fused the metalwork, foliage and grip. It remains a rejected reference, not the delivered model.
2. Early thin bevels and coincident leaf-tip points created degenerate triangles. Later constructors narrow bevels according to part thickness and avoid collapsed tip vertices.
3. Dense curved foliage reached 629,260 evaluated triangles. The simpler v5 study reduced that to 105,916 before later detail changes. This is an authoring geometry reduction, not an in-game performance result.
4. The first trigger-parent setup shifted the trigger out of its intended location. A neutral-pose comparison against the pre-parented source catches this; a test that only returns to the already-wrong starting pose does not.
5. Measured inward winding in closed collars and plate parts prompted targeted coincident-vertex welding and outward-orientation repairs. Open bore and backed glass surfaces are treated separately.
6. The initial 92-key animation sampling exceeded its declared error tolerances. The denser candidate uses 362 keys per track and is checked against 3,601 authoring samples. Native interpolation and bone binding remain open.

## Later geometry/material refinement

The v11 leaf material replaces 288 tiny vein curves with parameter-aligned color and bump detail on 32 leaves. Evaluated geometry fell from 110,416 triangles in v10 to 49,616 in v11. Matched closeups show that the earlier tubes sometimes floated above/beyond the blades; the material treatment is subtler and keeps the leaf silhouettes. Native texture baking and performance are still untested. Backed receiver-glass faces subsequently received explicit outward-facing normals, independently of the closed-solid checks.

## How to rebuild

Use Blender 4.3.2 with `--python-exit-code 1`. Keep the included directories as siblings. Run their `build.py` scripts in this order:

1. `carrot-cannon-authoring-v5`
2. `carrot-cannon-texture-v6`
3. `carrot-cannon-detail-v7`
4. `carrot-cannon-motion-v9`
5. `carrot-cannon-orientation-v10`
6. `carrot-cannon-leaf-material-v11`
7. `carrot-cannon-open-faces-v12`

The latest editable scene is included in the last directory. Earlier intermediate scenes are not duplicated in the bundle. The orange texture and its generation prompt are included with v6. Run the final directory's geometry, orientation, motion and clip-export checks after rebuilding. Released-parser verification requires the separately pinned parser-study dependencies; these upstream binaries are not redistributed here.

## What still prevents acceptance

The body is too uniformly segmented, the grip needs substantially better root/bark detail, and foliage/material richness still falls short of the concept. Native hands, readable loading/resource-service presentation, full locomotion/inspection animations, attachment variants, projectiles, impact/finisher effects, complete native textures, crafting, multiplayer and measured performance are unfinished.

A passed parser or geometry test does not make this a gorgeous finished weapon. This study must not replace the original concept as the quality target or increase the accepted-weapon count.
