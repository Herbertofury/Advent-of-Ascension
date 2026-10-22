# Complete weapon customization art program

Scope: all **434 audited raw release-union registry IDs**, including the **411 first-target IDs**. Shared artwork never merges distinct registered identities. The older 228-firearm implementation register remains a useful subset and is not replaced or reset.

The [live comparison gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html) has a selected base concept for every audited entry. This closes missing base images, not art approval, attachment coverage or native implementation. The [machine-readable register](weapon-customization-art-register.json) tracks separate artwork requirements against the existing 31-feature contract.

## Dedicated sheets for every weapon

1. Sights/scopes and aim transformations, with clear focused view and reversible transitions.
2. Barrels, muzzles and functional converters, with original mode preserved.
3. Magazines, feed/resource modules and visible resource-service handling.
4. Grips, stocks, receivers and support attachments, including hand and motion clearance.
5. Skins, finishes and mastercraft variants.
6. Static, animated and luminous stickers, decals and emblems, including off states.
7. Charms/trinkets, attachment points and motion limits.
8. Projectiles, tracers and trails, distinguishing original from proposed conversions.
9. Muzzle/charge feedback, recoil and recovery presentation.
10. Impacts and world decals across relevant entities, armor, terrain and fluids.
11. Optional death/finisher effects for confirmed outcomes only.
12. Equip, movement, idle, inspect, firing and reload/resource-service storyboards.
13. Complete builds, compatibility, crafting and UI previews.
14. Audio direction, accessibility and effect-intensity options.

A fantasy weapon can use identity-appropriate equivalents, but no category disappears automatically. Exceptions require an explicit owner-approved omission with rationale. A single crowded sheet does not satisfy all categories. Existing combined sheets are partial evidence until individual options and compatibility are reviewed.

## Honest evidence states

- `requires_reconciliation`: inspect existing work before declaring an image absent. This is not a claim that older art does not exist.
- `partial_candidate`: linked concept studies exist, but the full category is not accepted.
- Base concept, customization art, implementation and native QA are separate gates. Currently no complete customization package or native weapon is accepted by this register.
- Generated pictures are concepts, not gameplay captures or proof that a sight animates, a magazine fits or a companion fires correctly.
- Preserve previous concepts and specifically requested alternates. Keep dedicated studies separate from selectable alternate weapon designs.

## First detailed packages

Abominator now has its corrected visible magazine, plus separate magazine, sight, muzzle/converter, skin, charm/emblem, tracer, impact and finisher studies. Remaining handling, animation, audio, full-build and compatibility work is still open. The large impact illustrations do not authorize terrain destruction or establish gameplay scale.

Darkly Guster has corrected rear-swept bat wings, an explicit wing-to-sight study, playful flight-inspect choreography, proposed follower modes and per-shot propeller-gust effects. These are proposed game features, not existing source mechanics or implemented multiplayer behavior.

Bubble Horn has a new brass/cyan hero concept and a separate optional musical-bubble sight: form on focus, hold a readable center, pop on focus loss. Its previous design is retained as an alternate. The separately earned mouthpiece is a functional upgrade: actual trumpet-playing, much higher damage, more bubbles per shot and faster projectile motion, while original mode and the Spirit resource family remain distinct. Exact values and unlock route are not final.

Hiver and Hive Cracker have bee charge/action and optional bee/honey sight studies. Eradicator has a separate green-ooze spike sight study. None of these isolated studies completes the whole weapon package.

## Production gates after concept work

1. Pin the exact released source, original appearance, resource, effects and progression. Record upstream drift before implementation.
2. Review silhouettes, materials and close-up details against both the original and the selected concept. Reject generic substitutions and unrequested shape changes.
3. Build or clean the model into editable, separately articulated parts. Mesh-generator output is a starting asset, never automatic production approval. Check provenance and license before use.
4. Retopologize where needed; inspect UVs, texel density, seams, normals and texture baking. Do not assume arbitrary dense meshes or PBR materials are supported by the chosen TaCZ renderer.
5. Validate an importer/exporter proof of concept against the actual pinned pack format before investing in full production detail.
6. Rig moving components and attachments with stable pivots and clear ownership. Compare real TaCZ reference animations and hand placement, not just promotional renders.
7. Implement authoritative gameplay separately from client presentation. Test cancellation, dry/blocked actions, switching, save/reload and multiplayer state.
8. Test in **AoA plus TaCZ together**, including first/third person, hand fit, aim, inspect, attachment combinations, audio and performance. Static renders and pure component tests cannot replace this gate.

The register must be regenerated when the gallery changes. Its catalog hash deliberately ties each report to a specific evidence snapshot; no automated check grants subjective art approval.
