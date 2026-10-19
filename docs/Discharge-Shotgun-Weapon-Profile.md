# Discharge Shotgun — a close-range explosive scattercaster


**Quick status:** source behavior is documented; the newest grip/surface model is still an unaccepted authoring study. Native gameplay, hand fit and the full feature set remain open. Earlier texture and recoil checks apply only to their named source revisions.

## Owner-selected visual target

![Approved Discharge Shotgun concept target](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-owner-target-v1.png)

The owner explicitly selected this design as the target for a close, high-quality model realization. Match the silhouette, proportions, red/white/dark materials, central energy chamber, grip, raised capacitor forms and muzzle details. Preserve A as the core design and develop the depicted B/C configurations as separately documented craftable variants. Concept approval does not approve any model or runtime behavior.

Every variant needs the [full weapon feature package](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard): projectile/tracer/muzzle/impact/decal/death art and implementation, crafting, attachments, textures, animation, audio and independent concept-fidelity/native QA. Keep the exact-version original baseline below; proposed energy-looking visuals do not silently rewrite its resource or damage rules.


**Baseline: AoA 3.7.1 / Minecraft 1.20.1. Released-file analysis and upgrade concepts; native upgraded weapon not yet accepted.**

## What it actually does

Discharge Shotgun fires a four-projectile burst of `DischargeShotEntity` after one ammunition check using Discharge Capsules. It is not fully automatic. Its identity is a compact black/red body, broad front, silver dorsal fins with red accents and a rear grip. The upgrade should retain that recognizable silhouette while making its capsule, moving fins, recoil and impact feedback feel deliberate and powerful.

Its **base-damage constructor input is zero, but it is not harmless**: damage is routed through explosion behavior. The impact call chain contains an important distinction that a conversion must not flatten away.

- On an ordinary entity hit with a valid weapon and living owner, the shared bullet handler first calls the weapon's impact method, which requests an explosion with strength input **2.5**. It then calls the projectile's entity-impact method, which requests another explosion with strength input **1.8**.
- On a block impact, the projectile's block-impact method requests the **1.8** explosion.
- These are separate source-level calls. Do not add the strengths into a made-up “4.3 radius” or multiply them into a guaranteed final-damage figure. Damage immunity, other entities, event handlers and actual runtime behavior need testing.
- The helper uses the projectile entity's coordinates. The supplied hit-vector argument is not used by these overrides to position the explosion.
- Block damage is controlled by the destructive-weapon/mob-griefing rule path. A spectacular cosmetic impact must not bypass those permissions.

This existing two-stage entity-hit path is different from an accidental duplicate network callback. Preserve and test the original mode before making an explicitly declared upgraded behavior change.

## Verified baseline inputs

| Property | Released input / behavior |
|---|---|
| Item | `aoa3:discharge_shotgun` |
| Base damage input | 0; explosions supply the attack behavior |
| Pellets | 4 projectile spawn attempts per accepted burst |
| Durability input | 160 |
| Firing-delay input | 55 ticks; nominally 2.75 seconds at 20 TPS |
| Knockback constructor input | 0 |
| Stored recoil constructor input | 13, not degrees or the effective camera kick |
| Effective recoil caveat | Inspected inherited getter returns 0.35; its shot calculation uses 1 for zero base damage before multiplying by that getter |
| Ammunition | Discharge Capsule; ammunition checked before the pellet loop |
| Projectile | `DischargeShotEntity` |
| Lifespan parameter | 4, with an `age > lifespan` discard check after the superclass tick; not an exact four-tick range guarantee |
| Projectile damage-multiplier / piercing inputs | 1.0 / 0 |
| Gravity return | 0 |
| Fire sound | `ITEM_GUN_SHOTGUN_HEAVY_FIRE_LONG` |

The shared spread factor is `0.1 × pelletCount × (1 − 0.15 × Form enchantment level)`. This is a spread input, not an angle in degrees. Other firing eligibility, ammunition/enchantment and cooldown behavior still belongs to the native pipeline.

## Actual original visuals

![Nearest-neighbor enlargement of the released weapon sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-sprite-preview.png)

[Unmodified sprite bytes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-original-sprite.png).

![Nearest-neighbor enlargement of the released orange projectile texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-projectile-preview.png)

The renderer registration resolves to `TexturedProjectileRenderer` using this orange projectile texture. The red crystalline trails and red impacts in the concept below are proposed upgrades. Actual original in-flight and impact screenshots remain to be captured in game.

## Premium upgrade exploration

![Three original upgrade concepts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-concept-exploration-v2.png)

- **A · Core Discharge Scattercaster:** closest to the compact original silhouette. A visible fictional capsule seat and silver fins communicate charge, discharge and recovery.
- **B · Capacitor Crown:** articulated dorsal armor and red energy accents, with a distinct fin-opening inspection and restrained reactive stages.
- **C · Modular Breacher:** a flared emission assembly supporting alternate spread modules and a visibly different front silhouette.

The generated sprite inset is a reconstruction; the separate original above is the actual source. The effect vignettes are visual proposals and do not specify damaging pellet count. Comfortable hand/trigger clearance, capsule extraction and moving-fin envelopes still require actual models and animation QA. [Earlier v1 concept retained](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-concept-exploration-v1.png); v2 corrects C's cropped grip.

### Attachment and play ideas

- **Focus Choke:** a tighter deliberate discharge pattern, with the corresponding mechanical front visible.
- **Scatter Crown:** extra discharge channels and an explicitly defined multishot/damage upgrade. Resolve projectile count, ammunition policy and hit behavior on the server.
- **Pulse Chamber:** a distinct energy-pulse branch with its own collision and impact contract; do not silently substitute it for original explosions.
- **Capsule Cradle:** an optional visible loading/recharge presentation. Reloading remains optional rather than being imposed on every AoA upgrade.
- **Reactive fins and earned charms:** fins reveal brighter red seams through progression; charms can grant declared bonuses. Cosmetic sparks during inspection cannot damage mobs or detonate capsules.
- **Skins/effects:** preserve an original-inspired black/red/silver option, then offer unlockable materials, decals, trails and impact treatments without hiding targets.

## Acquisition evidence

A scan of this release's `data/aoa3` JSON files found no direct `aoa3:discharge_shotgun` reference. This does not prove there is no code-driven, creative, external-pack or other acquisition route. Do not invent a crafting recipe or label a historical route as current without verifying it.

## Current exterior refinement

[Inspect the muzzle, grip, capacitor and layered rear-receiver studies](Discharge-Exterior-Refinement), including three actual authoring views and a compact editable Blender scene. The scoped geometry checks pass for the recorded scene, while rear-receiver design, final concept fidelity, moving hands, materials/export and native gameplay remain unaccepted. Three visible channels do not change the original four-projectile behavior.

## Earlier grip and surface refinement

![Unaccepted Discharge authoring study with contoured grip](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-surface-study-v22.png)

The latest editable study adds three shallow grip contours, matte patterned panels, a smaller branching crest and armor traces seated against the curved surface. It still needs much stronger receiver/front-assembly sculpting to match the owner concept. The thin ornament geometry is high-resolution authoring detail for later bake/LOD work.

![Grip texture and comfortable control-space study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-grip-study-v21.png)

The v21 trigger and guard exactly preserve the prior evaluated static geometry; 21 new parts have no static triangle-surface intersections with the trigger. V21 has 70,228 triangles; v22 has 74,132, both with zero degenerate triangles in the scoped check. This does not prove hand fit, swept animation clearance, native materials, performance or a completed weapon. Earlier export evidence does not transfer automatically.

[Editable Blender scenes, input checkpoint and rebuild/QA scripts](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-grip-and-surface-study-v1.zip) · [Scope and rebuild instructions](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Discharge-Grip-and-Surface-Study.md).
## Acceptance checklist

- [ ] Capture original flight, entity impact and block impact in the exact release.
- [ ] Test both entity-hit explosion stages, final damage, immunity behavior and environmental rules.
- [ ] Test single ammo check versus the four-projectile burst and all relevant enchantments.
- [ ] Build the model, capsules, fins, comfortable hands and interruption-safe animations.
- [ ] Make every functional module's appearance agree with its declared projectile/resource behavior.
- [ ] Validate native export, multiplayer, saved builds, combat-mod compatibility and measured frame/tick costs.

[Released class and asset evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-released-evidence.json) · [Repeatable audit tool and concept prompts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-shotgun-audit-tool-v1.zip) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades)

Original AoA assets and identity: Tslat and contributors. Concept work: original project exploration generated with the built-in image tool.


## Confirmed-shot presentation core

An original Java core now maps accepted shot ordinals to visual emitter indices while rejecting duplicate, stale, wrong-weapon and wrong-configuration events. Discharge’s proposed three visual channels remain separate from its original four-projectile burst. This component does not consume ammunition, deal damage or spawn projectiles.

The same Java 17-targeted classes passed 80,031 assertions on each of Java 17 and Java 21, including deterministic emitter-count/ordinal sweeps. These are component checks, not native gameplay tests. Native event wiring, local prediction reconciliation, animation/bone binding and multiplayer/performance verification remain open.

[Implementation, reproducible checks and integration limits](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Confirmed-Shot-Presentation.md).



<details>
<summary>Earlier authoring revisions, rejected reconstructions and technical evidence</summary>

## Earlier v15 authoring and export baseline, still unaccepted

![Unaccepted Discharge v15 authoring render](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-authoring-v15-unaccepted.png)

Three distinct dark muzzle housings now have narrow metallic edges and actual side openings. Visual review caught older overlapping walls behind the first vent cuts; those redundant pieces were removed. Enamel chips/roughness and quieter red chamber energy improve the authoring materials. The receiver, rear shaping and grip detail still fall short of the selected concept.

The neutral-pose check reports 57,608 evaluated triangles with no flagged nonfinite, near-zero-area or negative closed-volume geometry. 297 frontal and 54 side-opening ray samples pass their defined regions. These limited checks do not certify continuous/animated clearance, hand fit, projectile paths or native gameplay. Chamber shader keys remain authoring-only. The existing capsule/four-projectile baseline is unchanged.

[Editable source, rebuild chain, QA and remaining gaps](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Discharge-Authoring-Refinement.md). New geometry/materials require fresh native exports and bakes; earlier atlas studies are not automatically current.



### v15-based texture and recoil exports

The new owner-isolated export includes base color, emission color and linear roughness maps for 142 parts. Rest-pose position/UV reconstruction errors are zero; corner-normal vector error remains below 0.000336. The chamber is frozen at the source frame and its local render error remains larger than the overall image average. Normal/bump export, animated energy and native material binding remain open.

Three independently owned muzzle-channel recoil clips now exist. A 340-frame authoring check covers 6,120 part transforms; actual released TaCZ parser classes accept all three clips and 111 keys on Java 17 and 21 with documented helper stand-ins. This does not prove native playback, bone binding, hand clearance or firing behavior.

[Source, maps, editable animation and exact QA limits](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Discharge-Material-and-Recoil-Study.md).

## Earlier modeled study: v7, still below the visual target

![Unaccepted Discharge v7 authoring prototype](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-sculpt-v7-prototype.png)

The rear assembly and grip are more deliberately shaped, with shallow contact grooves and conforming side panels. Two duplicated crown ribs were removed. The generator now normalizes closed-face orientation and limits prism/cylinder bevels by thickness, rather than repeatedly fixing individual thin parts. Twenty actual-constructor regression fixtures pass. The current evaluated source has 51,144 triangles, no degenerate triangles and no negative closed volumes. These are scoped geometry results, not complete collision or visual acceptance.

The opaque texture study preserves 143 separately owned parts and 100,160 UV corners. Rest positions and UVs match exactly in the reconstruction check; maximum corner-normal vector error is approximately 0.000336. A strict preflight now rejects collapsed triangles and inward closed solids before baking. Matched-camera color comparisons are recorded, including local core-region errors rather than hiding them in a background-heavy average.

The model still falls short of the concept’s sculpted surfaces and texture detail. Native hands, materials, complete animation/effects, crafting, gameplay and performance remain open. The baked maps are an export study, not finished texture art.

[Corrected editable authoring sources](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/aoa-authoring-corrections-v19-v7.zip) · [Atlas/part reconstruction source and scoped tests](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-atlas-part-study-v11.zip) · [Texture-study explanation](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Discharge-Atlas-Part-Study.md) · [Surface QA lessons](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Weapon-Surface-QA.md)

## Modeled progress: v3 remains below the visual target

![Discharge v3 unaccepted authoring study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-sculpt-v3-prototype.png)

Actual editable geometry now includes a stepped forward shield, thinner crown shells, an integrated notched lower plate, a rear capacitor crest and fitted grip details. Earlier solid box-like fins and handle-like lower loops failed visual review and were replaced.

The model is still too simple compared with the chosen concept, particularly the rear structure, crown contour, shaped surfaces and texture work. It has no native firing/animation/play-feel acceptance. The original four-projectile/capsule behavior above remains the baseline; the three visible front channels are not a change to damaging projectile count.

Static world-space QA caught 108 degenerate triangles on four thin beveled inlays. Narrowing only those bevels leaves zero degenerate triangles across 32,004 evaluated triangles. This does not certify collisions, hand fit or runtime behavior.

[Editable Blender source, rebuild script, before/final QA and defect review](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-sculpt-v3-source.zip) · [Texture reference-file study](TaCZ-Texture-Direct-Study)

## Concept-to-mesh research and rejection record

[Direct trial report](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Concept-to-Mesh-Discharge-Study.md) · [Reproducible reference-volume study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-concept-mesh-study.zip)

TRELLIS.2 produced preview images but its GLB export failed. The older community demo also returned empty error outputs. A separate local silhouette reconstruction improved the reference-volume silhouette, but front/oblique texture tearing, missing concavities and absent component rigging keep it rejected as a finished asset. It is not the original generated mesh. The authored v7 source and canonical concept are preserved separately. No native or artistic acceptance is claimed.


## Owner-isolated texture correction

The v12 rebake fixes a modular-texture hazard: all-source projection can permanently paint a neighboring removable part onto the wrong surface. The corrected selector isolates each source owner and excludes hidden selected geometry. An actual red-owner/blue-neighbor fixture catches the old error.

The Discharge reconstruction covers 143 parts and 100,160 UV loops, with zero position/UV error and maximum corner-normal vector error 0.00033557. Previous assembled v11 checks remain valid only for their stated scope; they do not prove isolated color ownership. Native material binding, mip safety, animation and final texture art remain unaccepted.

[Explanation and evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Texture-Owner-Isolation.md) · [Corrected source/maps and regression bundle](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-texture-owner-isolation-study.zip)


## Local CPU reconstruction result

A separate local TripoSR trial successfully exported and reopened a 10,272-triangle Discharge reference mesh. It remains rejected as a finished weapon: blurred colors, soft edges, invented hidden geometry and absent moving-part ownership still fail the visual and gameplay requirements. The editable authored source and selected concept remain authoritative.

[Full trial, provenance and rejection reasons](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Local-CPU-Reconstruction-Study.md) · [Reproducible wrappers and reference meshes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/local-cpu-weapon-reconstruction-study.zip)

![Unaccepted CPU reconstruction, reference only](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-cpu-reference-unaccepted.png)



</details>
