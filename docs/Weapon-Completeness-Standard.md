# Complete Weapon Standard

**Every weapon is a complete experience, not just a mesh.** This is the mandatory design, implementation and QA contract for the AoA weapon upgrade. All 31 feature groups apply to every weapon review. The first-target register contains 228 weapon IDs; historical/version-exclusive weapons remain additional scope.

## 1. The package each weapon must receive

### Identity, concept and construction
- Exact-version original appearance, function, stats, resource, projectile, effects and acquisition route.
- Canonical concept sheet, side/front/top views, material/texture direction and original-versus-upgraded comparison.
- Accurate silhouette, proportions, grip, hand room, visible supply-to-emitter story and moving-part clearances.
- Original UV/textures with purposeful pixel shading, material separation, edges, wear, seams and emissive detail. Study actual TaCZ pack files, not only promotional pictures.
- Separate concept sheets and acceptance for craftable alternate designs. An interesting alternate cannot silently replace the canonical concept.

### Complete firing and effect package
- Projectile designs and in-flight behavior; alternate projectile concepts and actual resulting values.
- Tracers and trails, including taper, lifetime, color, motion and customization.
- Muzzle flash, smoke, sparks, local light, recoil and sound synchronization.
- Entity/armor/terrain/fluid impacts and any separate area-effect behavior.
- Surface decals: marks, scorch, magical imprints, alignment, fade and bounded cleanup.
- Death/kill/finisher concepts, storyboards, sounds and selectable effects, triggered only by valid confirmed outcomes.
- Configurable projectile, tracer, muzzle, impact, decal and finisher channels. Cosmetics must not secretly change damage or resource use.
- Show original projectiles and impacts alongside new concepts. Label real game captures, extracted assets, concepts and offline renders accurately.

### Crafting and the modular armory
- Recipes, materials, ingredient images, acquisition, loot, achievements, boss rewards and progression.
- Craftable variants with clearly documented mechanical differences.
- Barrels/converters, sights/scopes, receivers, grips/stocks, suppressors/brakes and appropriate fantasy equivalents.
- Ammo/energy/feed modules and visible loading/resource-service stories.
- Dismantling and effect salvage: donor identity, transferable effects, conflicts, stacking, balance, preview and persistence.
- Original skins/mastercraft styles, earned functional charms, static/animated/glowing stickers and custom emblems.
- Visible attachments, tooltip values and authoritative behavior must describe the same resolved build. More barrels can have meaningful effects when designed, but a render is not their implementation.

### Complete animation and audio package
- Idle, equip, holster, supported movement, sprint/crouch and aim transitions.
- Firing, per-emitter recoil, charge, cooling/recovery, blocked/dry input and rapid-repeat handling.
- Tactical/empty reload where appropriate, or the correct energy/resource-service animation. Reloading remains optional where the weapon's resource design calls for it; never replace Spirit/mana with generic bullets for convenience.
- Inspect and playful mastercraft choreography, with safe cancellation and reduced-motion options.
- Hand/prop ownership through extraction, carrying, insertion and release. No floating clips, crushed hand space, clipping triggers or impossible supply paths.
- Fire/charge/handling/reload/inspect/flight/impact/finisher audio, environmental response and source/license evidence.
- First-person, third-person, world-held/dropped and GUI presentation where supported.

### Integration, documentation and quality
- Actual pinned native-stack loading and gameplay, multiplayer authority, resource accounting, save/load/migration and optional-mod compatibility.
- Effective stats, build previews, exact icons, clear tooltips and complete illustrated documentation.
- Startup and frame-time/memory budgets, LODs, bounded effects/caches, no repeated scans, and accessibility controls.
- Retained source files, concepts, previews, receipts, native footage and known defects.

## 2. Concept fidelity is a separate hard gate

A valid file, a successful parser test or a collision check does **not** mean the weapon looks right.

Before modeling, pin the chosen concept and its hash. Identify landmarks: receiver/core, barrel/emitter arrangement, stock, grip, guard, magazines/resource chambers, sights and ornament. Compare their relative size, spacing, curvature and material boundaries. Review the model at the same angle and in six useful views; fix the camera rather than accepting cropped or misleading comparisons.

Before claiming visual acceptance, record paired concept/model evidence and an explicit review of silhouette, proportions, negative space, grip, materials, texture density, color, animation and effects. Preserve any deliberate deviation as an approved alternate or document why a functional adjustment is needed. Do not pass a simplified look-alike merely because it shares the colors.

Owner feedback overrides a previous visual assessment. Failed or unreviewed art stays failed or unreviewed. Automated tools validate evidence and numeric constraints; they cannot certify beauty or concept fidelity.

## 3. Three independent phases for every feature

Each of the 31 catalogue rows records:
1. **Concept/design:** art or storyboard for visible features; a concrete specification for nonvisual systems.
2. **Implementation:** versioned source/asset and integration status.
3. **QA:** scoped evidence, defects and the tested environment.

Use `not_started`, `in_progress`, `blocked`, `ready_for_review` or `passed`. Never substitute a concept for implementation, or a unit test for native acceptance. Every phase needs evidence before `passed`.

An intentional omission requires a reason and explicit owner approval. Never default a feature to “not applicable.” An energy weapon may have resource recovery instead of a conventional magazine reload, but the entire animation/resource feature still needs a design and review.

## 4. Six independent acceptance gates

1. Mechanism continuity and exact-version behavior.
2. Spatial/mesh correctness, hands, attachments and swept motion.
3. Animation ownership, interruption and recovery.
4. Confirmed-shot behavior, feedback and resource consistency.
5. Export and resource loading in the pinned native stack.
6. Native gameplay, networking, saves, performance and visual review.

Check keyframes, dense samples, extrema, transitions and known-bad regression fixtures. Sampled AABB clearance is only that; it is not continuous triangle collision proof. Inspect moving parts at normal and slow speed. Keep authored defaults, optional variants and all supported attachment combinations identifiable; disclose which combinations were actually exercised.

## 5. Performance without hiding losses

Maintain high-detail and LOD sources separately. Benchmark startup, frame times and lows, memory and effects costs in comparable native scenes. Do not call fewer triangles or smaller JSON an FPS result. Preserve resource/animation/visual correctness while optimizing. Exact float32 export equivalence is useful evidence, but it is not native rendering or loading acceptance.

## 6. Current owner-directed corrections

- **Soul Storm:** current grip, proportions and weak floating-looking flame are not canonical-quality accepted. Rework toward the concept. The flame must be rooted in its socket and form a clear crosshair when focusing/aiming; retain optional candle/gem choices. Improve actual texture work with reference-pack study.
- **Discharge Shotgun:** the supplied concept is the explicit visual target. Match it closely; include the depicted craftable variants and their effects. Concept approval is not model/runtime approval.
- **Iominator:** preserve and improve the current looping rear-feed design as a separate craftable alternate. The canonical version must follow the supplied concept. Do not use alternate-design approval to pass canonical fidelity.

## 7. Definition of done

A weapon is fully accepted only when every feature has passed its concept/design, implementation and QA phases (or has an owner-approved documented omission), the canonical visual review is accepted, all six native/technical gates are passed with evidence, and its guide exposes the complete package and remaining compatibility limits. Until then, report the real milestone and open work.

The machine-readable catalogue, manifest template, coverage register and validator enforce completeness bookkeeping. They never grant native or artistic acceptance by themselves.

## 8. Required aesthetic and play-experience self-review

At each meaningful iteration, answer these questions with evidence and specific defects, not a generic score or praise:

1. Would I choose to use this weapon, and what gives it a recognizable AoA identity?
2. Does it match the chosen concept's silhouette, proportions, negative space and material hierarchy from comparable viewpoints?
3. Is it beautiful at normal gameplay scale as well as in a close-up render? Is any part still toy-like, weak, floating, cluttered or awkward?
4. Do firing, recoil, impacts, sound and recovery make its intended power readable? Does feedback stay clear during rapid use?
5. Is the animation enjoyable repeatedly, with responsive input and safe interruption? Are hand clearance and the visible resource path believable within the fictional design?
6. Do attachments and craftable variants create distinct useful play choices, with visible and mechanical changes that agree?
7. Are projectile, muzzle, impact and finisher effects exciting while preserving aiming clarity, accessibility and performance?
8. What is the weakest part now, what concrete change addresses it, and what evidence would show the change worked?

Record observation type: concept inspection, authoring render, offline animation, or native playtest. A render can establish an art defect; it cannot establish that a weapon is fun to play. Native play-feel remains untested until actual interaction is observed. A failed answer stays a tracked defect and prevents complete acceptance where relevant. Do not increase praise to match effort spent.

For the full-set announcement, reconcile all 228 first-target IDs plus the separately inventoried historical/version-exclusive scope. Report exact version coverage, remaining unsupported combinations and evidence. Never announce every AoA weapon complete from the first-target count alone.

## 9. Source-to-export regressions that must be caught

- Measure the actual authoring FPS, frame hold and atlas sequence. Do not assume a default scene rate. Test the presentation sampler against the recorded timing data.
- Evaluate modifiers, curves and transforms before geometry checks. Triangle area and unit-normal length do not prove outward winding. Check intended closed-solid orientation and review open surfaces/culling separately.
- Detect exact duplicated surfaces; review intended overlays instead of blindly deleting them. Stress-test the actual thin-part constructors so new inlays and indicators do not repeat old bevel-collapse defects.
- Compare authoring and exported material appearance using matched camera, lighting, sample count and seed. Preserve procedural coordinate meaning, raw color and emission intensity. A diffuse BSDF contribution is not automatically the intended raw metallic color.
- Preserve per-part ownership through UV packing/baking. Verify positions, UVs, material mapping, corner-normal error and controlled owner motion. A merged still image cannot pass animation ownership.
- Turn critical measured limits into failing tests. Logging a large normal error while returning success is not a pass.
- Prioritize texel density where detail needs it before increasing every texture. Report local error regions, memory assumptions and native limits; background-heavy image averages can hide defects.
- Fail unsupported material/alpha/rig cases explicitly. Do not silently apply an opaque-material pipeline to transparent flame or mixed shaders.
- Keep source revisions and evidence hashes aligned. A corrected authoring scene does not repair an older exported fixture automatically.

These checks supplement concept fidelity, real hand fit, native gameplay and performance testing. They do not replace them.


## 10. One canonical concept, two selectable visual treatments

Use a strong AAA-quality concept faithful to original identity, then personally author the model and textures for both Minecraft-fit and concept-faithful presentation. Both represent the same weapon and resolved build. See [Weapon Visual Profiles](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Weapon-Visual-Profiles.md) for shared behavior, resource and QA requirements. The first Apoco concept and v1/v2 blockouts are owner-rejected history.
