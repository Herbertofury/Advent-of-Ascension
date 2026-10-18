# Actual TaCZ hand-anchor contract study

Pinned input: TaCZ Forge 1.20.1 1.1.8-hotfix2, using the actual released JAR already recorded by this project. The evidence JSON includes its SHA-256 and exact model hashes.

## What the released files establish

- BedrockGunModel's constructor registers functional renderers at the exact names lefthand_pos and righthand_pos.
- RightHandRender and LeftHandRender delegate to RenderHelper.renderFirstPersonArm, which obtains the local player's PlayerRenderer and draws the corresponding arm. A placeholder cube in an authoring model is not itself proof of the actual displayed player arm.
- The inspected default short shotgun includes 3×12×4 authoring cubes beneath the hand-position bones. Their dimensions/pivots are reference-specific, not an automatic fit for AoA grips.
- Model roles were resolved from actual display JSON. There are 54 referenced primary models and 54 referenced LOD models in this snapshot. All 54 referenced primary models pass the structural anchor checks. LOD models are deliberately not required to contain first-person anchors.
- Two additional hk416d geometry files are not referenced by the inspected display fields. Their role remains unclassified; the missing anchors in that extra LOD file are not reported as a demonstrated mod bug.
- The published Soul Storm v15 transport has neither functional hand-position bone. It remains a geometry transport study, not a first-person-ready weapon.

## Required next implementation and QA

1. Author hand-position bones against the actual AoA grip and its coordinate conversion. Do not add both at zero merely to satisfy a structural test.
2. Test normal/slim player skins and the actual supported arm/render stack. Check sleeves, grip fit, trigger/guard space and contact throughout firing, aim, handling, reload/service and inspect.
3. Keep hands attached to the correct animation ownership hierarchy. A detachable magazine must not accidentally own the firing hand; the supporting hand must follow the intended motion.
4. Check world/third-person/GUI/shadow presentation independently. A first-person anchor does not solve third-person placement.
5. Review alternate attachments and both relevant hand configurations in the actual game. Source analysis does not establish native fit, player-model compatibility or collision freedom.

## Tools

audit_anchors.py checks names, duplicates, finite explicit pivots and parent graph integrity. Its default is a first-person model contract. LOD scope must be explicit. It never grants hand-fit acceptance.

run_study.py reads the pinned JAR and local published v15 transport. The small comment scanner preserves quoted URLs/escapes and strips only line/block comments; it is not a general replacement for Gson's full lenient parser. Six malformed structural fixtures and one valid fixture are included. Decompiled bytecode dumps are local inspection evidence, not bundled implementation code.

Run the structural fixtures with python test_anchors.py. Reproduce the source study with python run_study.py --jar /path/to/pinned-tacz.jar --model /path/to/soul_storm_transport.geo.json. Only the supplied archives are read; no game classes are executed.
