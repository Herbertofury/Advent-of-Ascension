# Light Blaster: crystal-focus motion blockout

This independent cosmetic prototype explores the requested green-crystal sight transformation. It does not replace the selected Light Blaster concept and is not an implemented Minecraft or TaCZ weapon.

## What is included

- Eight rigid faceted crystal pieces, with stable identities throughout the sequence.
- A neutral reference mount, not a weapon model or final hand-contact surface.
- A four-second animation: resting crest, formation, held aperture, rear aiming view, return.
- A Blender scene and reproducible render scripts.
- A small independent Java focus-state controller and regression tests.

The crystal count is a prototype choice, not a claim that eight is the final released-source count. The rendered sequence stretches timings to make the movement readable; it is not bound to the Java controller or an engine event.

## Verified scope

The geometry check examines 6,400 projected triangles across 50 focused frames. Minimum radial clearance from the sight center is approximately 0.5539 scene units. The focused camera projects the intended center to (0.5, 0.5). Each shard is a closed manifold mesh, retains unit scale, and returns to its original pose.

The independent cosmetic controller passes 30,044 sampled assertions, including finite-input validation, focus reversal, disabled return, clamping, and event-boundary comparisons at 20, 30, 60, 120, 144 and 240 updates per second. These are sampled assertions, not 30,044 distinct gameplay scenarios.

## Not verified or implemented

- Complete weapon geometry, exact source crystal count, hand rig or final materials.
- AoA/TaCZ input integration, network state, save behavior or item data migration.
- Continuous intermediate collision clearance, shard self-intersection, physical inertia or cloth.
- Native renderer appearance, first-person FOV fit, performance or accessibility settings.
- Damage, resource consumption, accuracy, magnification or other gameplay changes.

Any final attachment must preserve the normal weapon and explicit off selection. Cosmetic motion alone must not change combat statistics. The actual weapon requires testing with AoA and TaCZ together.

## Reproduce

Use Blender 4.3.2 to run `build_motion.py`, `verify_geometry.py`, and optionally `render_clean.py`. Java sources compile with Java 17; run `LightCrystalFocusStateTest` after compilation. No external weapon models or proprietary source assets are included.
