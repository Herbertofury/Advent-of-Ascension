# Neutral-pose parenting regression

A source-to-rig check added after a real Carrot Cannon authoring defect: the trigger's nonzero pivot was not evaluated before preserving its world transform, so it moved into the surrounding model. Owner-name tests and return-to-ready tests passed because both used the already-wrong pose.

## Required comparison

Capture the original world matrices before parenting. Evaluate the new parent transforms, preserve the child world pose, update the dependency graph, and compare against that original baseline. Also verify the part follows its owner correctly after a controlled parent movement. A test comparing frame 48 only with frame 0 cannot detect a frame-0 setup defect.

The included Blender fixture exercises 64 translated/rotated/nonuniformly scaled parent setups, including reflected X scale. Maximum neutral matrix error was 7.152557373046875e-7. The deliberately unpreserved nonorigin-parent case yields an error of 3.0 and must be detected. These are matrix tests, not proof of correct normals or native bone interpretation.

## Visual and contact checks still required

- Inspect neutral and moving poses from more than one angle. A vanished trigger, detached magazine or shifted sight fails review regardless of test count.
- Model real attachment seating. Avoid resolving intersections by leaving a part visibly floating or making it too small to use.
- Explicitly identify intentional joint contacts. A pivot's intended mating surfaces do not exempt the rest of the trigger, guard, hand space or magazine path from collision checks.
- Include source-to-export ownership, pivot and coordinate-frame tests. Check the actual game's hands, animations and interrupted states before acceptance.
- Constraints, armature bone parenting, preexisting shear and native engine matrices are not covered by this fixture. Unsupported cases must be handled or rejected explicitly.

Run with Blender 4.3.2: `blender -b --python-exit-code 1 --python check.py`.
