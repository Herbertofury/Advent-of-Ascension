# One weapon identity, two visual treatments

Owner-approved direction, 18 October 2026. Every weapon starts with one strong, non-pixelated AAA-quality canonical concept grounded in the original AoA silhouette and identity. Matching colors alone is insufficient. Soul Storm, Discharge and the supplied Iominator sheets set the artistic ambition.

The authoring work includes the model and deliberate texture work. Generating concept art is the beginning, not a substitute for building the asset.

## Minecraft-fit

Translate the canonical design into cohesive in-game materials, purposeful texture density, readable forms and effects. Retain its distinctive construction, ornaments and silhouette. Do not reduce it to generic boxes or use arbitrary noisy pixels as a substitute for texture art.

## Concept-faithful

Aim for the concept's richest geometry, surface detail, materials, lighting and effects. Preserve design landmarks instead of loosely approximating their colors. This is a fidelity target, not a promise that offline lighting or an unsupported shader will look identical in every renderer.

## Shared behavior and implementation requirements

- Both are visual treatments of the same weapon, with the same selected attachments, progression and authoritative behavior.
- Keep attachment/emitter/sight/hand anchors, animation ownership and event timing consistent. Do not change projectile count or damage merely because a visual profile changed.
- Preserve useful combat telegraphs and aiming readability in both modes, with reduced-motion/effect controls.
- Select locally without duplicating inventory items or resetting builds. Persist the preference; handle unavailable assets with an explicit fallback.
- Reuse cached resources and bounded effects. Preload and swap safely; do not rescan packs or rebuild meshes every frame. Validate resource release and repeated toggling.
- Measure frame-time/memory/startup costs on the actual target stack. Greater visual complexity is not automatically free. Neither profile bypasses performance or compatibility QA.
- Keep separate screenshots, native footage and defect lists for each profile. A finished concept or successful parser test does not complete either mode.

## Apoco correction

The owner rejected the first Apoco Assault Rifle concept direction as unrecognizable and uninspiring. Its concept-v1 and model-v1/v2 are retained as rejected history, not the canonical target. Rebuild the concept from the original identity first; do not keep refining the rejected generic long-rifle design and call it faithful.

The two new owner-supplied images are quality references for Discharge and Iominator. They are not Apoco's original appearance. Apoco's exact released sprite and source baseline must be compared independently.
