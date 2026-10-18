# Geometry checks that a successful render can miss

These tools inspect authoring geometry in Blender. They do not grant native, artistic, hand-fit or continuous-collision acceptance.

- check.py compares neutral-pose evaluated triangle-coordinate multisets at 1e-7 quantization and flags exact coincident object surfaces. Review intentional overlays; it does not automatically delete anything.
- check_winding.py reports signed volumes for closed manifold meshes. Negative volume in the intended solid parts is an orientation defect. Open/nonmanifold surfaces require separate side/culling review.
- fix_closed_winding.py repairs only the identified closed negative meshes, with explicit handling for the named Discharge grip panel. It refuses shape-key meshes and mirrored transforms. It writes a separate output, keeps vertex positions unchanged, and never guesses a repair for arbitrary open surfaces.
- verify_winding_preservation.py checks that unoriented faces, per-corner UVs, material slots and transforms stayed unchanged.

## Actual defects found

Discharge v3 contained two duplicate crown-rib objects. The generator produced the same cross-rib once from each side. v4 produces each only once: 96 triangles removed, no FPS claim. The exact-surface test then reports no duplicate object surfaces.

Later closed-volume checks found nine inward-oriented closed parts in Discharge v5, plus one explicitly reviewed inward-facing open grip panel. Discharge v6 corrects these ten objects. Soul Storm v18 had 36 inward-oriented closed parts; v19 corrects those. Both corrected scenes report no remaining negative closed volumes. Preservation checks pass for all 10 and 36 changed objects respectively.

Earlier triangle-area and unit-normal-length checks could not detect these orientation issues. Earlier authoring renders were not release acceptance; some two-sided render paths can conceal wrong winding. Older transport artifacts must be re-exported from corrected sources and checked in the actual renderer before release.

## Limits

Signed volume alone is not a complete topology/culling proof. Review disconnected components, cavities, inconsistent adjacent winding, intentional inside surfaces, transparency and every open mesh. These checks are additional gates, not replacements for native first/third-person testing.

The small duplicate fixture creates two coincident cubes and one offset cube. The duplicate is detected while the offset remains distinct.
