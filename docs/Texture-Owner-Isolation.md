# Texture ownership during modular weapon baking

**A surface must keep its own material when a neighboring part moves or is removed.** A correct-looking assembled render alone cannot prove that.

## Failure caught

All-source selected-to-active projection can hit a nearby clamp, band or attachment before the intended source surface. That neighboring color then becomes permanently painted onto the owner's atlas. The error may be hidden while the parts remain assembled.

The first per-owner attempt exposed a second selection problem: a hidden merged target was still selected and could become an unintended source. Hiding an object is not a replacement for checking the selected-source set.

## Corrected contract

1. Deselect every object in the controlled bake scene before each part.
2. Make exactly one original owner and its atlas target visible/selected; assert those are the only selected objects and the target is active.
3. Keep the other source/target parts hidden for that bake. Preserve each part's UVs, corner normals, transform and owner relationship.
4. Clear the image only for the first part of each channel, then accumulate the remaining islands.
5. Inspect separated components and test removable overlays. Recheck UV padding, mip behavior and native material binding independently.

The reusable owner_selection.py implements the selection contract. The fixture executes that same function, including a deliberately hidden, previously selected decoy.

## Verified synthetic regression

A red owner sits just behind a removable blue neighbor. The old all-source bake writes RGBA [0,0,1,1] onto the red owner's center. The isolated bake writes [1,0,0,1], and the hidden decoy is deselected. These are actual Blender bake results, not a drawn illustration.

## Apoco technical study

The corrected study baked separate 1024² base-color and emission maps for 70 source-owned parts. Its reconstruction check covers 63,702 UV loops: zero UV error, zero corner-normal vector error, maximum world-position error about 1.19e−7 and zero error in one controlled owner translation.

The underlying compact Apoco blockout and material art remain unaccepted. This study does not implement an in-game visual-profile switch or establish native rendering, PBR equivalence, mip safety, hand fit, animation collision, performance or gameplay quality. Normal/bump and roughness export require separate work. These are original procedural authoring materials baked into real texture files, not a claim of a finished hand-painted texture set.

## Earlier studies

The earlier Discharge atlas studies remain historical evidence for their stated geometry/UV and assembled-image checks. They do not prove isolated color ownership. Re-bake with owner isolation before treating their textures as ready for moving/removable components.

## Discharge corrected bake

The v12 owner-isolated rebake covers 143 parts and 100,160 UV loops: zero position/UV error, maximum corner-normal vector error 0.00033557, and zero error in the tested owner translation. These are scoped reconstruction results, not complete animation or native validation. The authored v7 shape and art retain their prior acceptance limitations.

[Source, maps and synthetic regression bundle](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-texture-owner-isolation-study.zip). The package retains source-owned object relationships and reproducer paths. Old all-source textures remain historical evidence and must not be silently treated as corrected.
