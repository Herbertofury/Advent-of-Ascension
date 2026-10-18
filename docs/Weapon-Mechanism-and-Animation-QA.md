# Weapon mechanism, animation and visual QA

**A weapon must make sense before it is polished.** This is the acceptance contract for the original AoA premium weapon presentations. It applies to physical, magical and science-fiction designs. A visually clear, consistent fictional mechanism is required; this document is not a real-world weapon construction specification.

[Weapon overhaul](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Baronator prototype](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Animated-Weapon-Prototype-Baronator) · [Implementation backlog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog)

## Why this gate exists

The Baronator exposed three separate defects: magazine/guard intersection, a cramped repair that caused trigger/guard intersection, and a relocated magazine without a demonstrated feed path. Passing a scoped collision test did not establish a credible mechanism. None of those layouts qualifies as a finished weapon. The approved alternating upper/lower firing feel is retained while the internal layout is redesigned.

The current published model is an authoring study. Its feed path, real hand interaction, engine transitions and runtime behavior remain unqualified. Do not call a model complete because it renders, has many keyframes, or passes JSON validation.

## Research used, and what it actually supports

### Real production art, rather than mislabeled fan art

[Atomhawk's Helldivers 2 project](https://atomhawk.com/project/helldivers-2/) identifies its work for Arrowhead across concept and 3D art. Its [weapon-design portfolio](https://atomhawk.artstation.com/projects/8b98dQ) is a direct production-art reference. Study component hierarchy and presentation; do not imply that every unrelated Helldivers fan model is a shipped asset, or that artwork proves its internal mechanism.

### Weapon identity comes from coordinated motion and effects

[Infinity Ward's animation director interview](https://blog.activision.com/cn/zh/call-of-duty/2019-07/Modern-Warfare-Initial-Intel-Detailing-Advancements-in-Animation-and-Authenticity) describes weapon-specific heft, separate empty/tactical reloads, visible magazine changes, restrained active idle and coordinated sound/impact effects. Our application: give each AoA family its own motion vocabulary and maintain state continuity instead of reusing one generic reload and amplifying camera shake.

[David Helsby's Bungie GDC session](https://www.gdcvault.com/play/1022297/The-Art-of-First-Person) frames arms, weapon and camera as the persistent first-person experience, with physical responsiveness under gameplay constraints. The public session description was reviewed; this is not a claim to have watched the full talk.

### Grounded science fiction still needs consistent rules

[Royal Armouries' game-development service](https://royalarmouries.org/entertainment-and-ip/working-with/video-games-development) explicitly combines curatorial knowledge with photographic, video and sound reference for game teams. Its [Aliens pulse-rifle history](https://royalarmouries.org/objects-and-stories/stories/m-41a-aliens-pulse-rifle) discusses a believable fictional prop built around recognizable forms and deliberately used surfaces. Its [Blade Runner blaster history](https://royalarmouries.org/objects-and-stories/stories/blade-runner-blaster) distinguishes fictional interpretation from the underlying prop. Our application: define what each visible component does; intentional fantasy must remain internally consistent. A film prop is visual reference, not engineering validation.

### Synchronize contacts and events explicitly

[Epic's animation-notify documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine) documents timed sound/particle events, socket attachment, duration-based states and synchronization markers. Apply the design principle in the TaCZ/AoA adapter: use named events and contact windows, while keeping ammo/damage authoritative on the native server. Unreal APIs are not a drop-in Minecraft implementation.

[Epic's Two Bone IK example](https://dev.epicgames.com/documentation/en-us/unreal-engine/two-bone-ik?application_version=4.27) demonstrates a three-joint solver and hand targets for weapon handling. Use explicit grip/magazine/control targets and elbow constraints; validate real hands rather than considering an empty box a hand-fit certificate.

### Inspect actual TaCZ releases

Four official release archives were downloaded and selected source files were inspected as data, without executing or redistributing their assets:

- [Create Armorer 1.2.0.1 for 1.1.7](https://www.curseforge.com/minecraft/customization/tacz-create-armorer-koei/files/7598625): Crane reload separates extraction, carried motion, alignment and seating. Matching hand/magazine deltas and curved keys are visible in the animation data.
- [Immersive Armorer 1.2.1 for 1.1.7](https://www.curseforge.com/minecraft/customization/tacz-immersive-armorer-koei/files/7598069): dual-barrel cannon separates upper/lower firing, magazine actions and motion layers. Its ammo-threshold selection is not the requested Baronator alternation policy.

- [Helldivers gunpack, file 9044777](https://www.curseforge.com/minecraft/customization/tacz-helldivers-escalation-of-freedom/files/9044777): AC7 places the supporting hand and magazine/bullet assembly beneath one carry-space bone. Empty and tactical reloads differ, with timed sound cues, separate LOD data and first/third-person firing sounds. Apply the shared-rig principle with original poses; do not copy its weapon balance or keyframes.
- [Ars Armorer 1.0.1 for 1.1.7](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei/files/7358702): the inspected source-ejector pistol has no conventional reload clips; firing moves its core and barrel groups. Its resource-named script uses TaCZ ammo-count APIs. This does not establish a shared Ars Source or AoA Spirit backend.

[Exact archive hashes and selected-member observations](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/reference-pack-study.json). Do not copy keyframes, art, sounds or scripts merely because the archive is readable. These are selected-file findings, not complete visual, gameplay or compatibility certification of those packs.

### TaCZ-specific hand and state-machine checks

[TaCZ hand-position guidance](https://tacwiki.mcma.club/zh/gunpack/gun/04_hand_pos.html) gives distinct Steve and Alex arm-preview conventions and explains that the renderer replaces preview geometry in the hand-position groups with player arms. Therefore a generic finger-clearance box cannot certify actual TaCZ hand placement. Author both arm profiles around the documented locators and verify the pinned renderer's transforms.

[TaCZ animation/state-machine guidance](https://tacwiki.mcma.club/zh/gunpack/gun/display/02_animation.html) distinguishes clips, optional custom state machines and third-person animation configuration. The [state-machine reference](https://tacwiki.mcma.club/zh/gunpack/gun/animation/state_machine_script) describes track allocation and entry/update/transition/exit behavior. A custom alternating weapon requires explicit lifecycle cleanup and correct layer initialization; a list of animation names alone does not provide that behavior. Match documentation against the exact source/version being targeted.

## Inspect the mechanism study

[Open the separate cutaway lab](https://herbertofury.github.io/Advent-of-Ascension/baronator-mechanism-lab.html) to trace intake, transfer, chamber seating and carrier return. Toggle the ghost shell and arm-fit proxies, pause and scrub the timeline. The original heavy alternating recoil is retained. The slow inspection cycle is not native firing cadence. Unreviewed reload/action sequences remain outside this study.

[Download the original editable study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-mechanism-study.zip). It is not an installable gunpack. Regeneration and scoped geometry tests do not certify a completed or game-tested weapon.

## Gate 1: function before silhouette approval

For every weapon, write a one-page mechanism brief before detailing:

1. What is consumed according to that exact AoA version: cartridge, pellet, rune, mana, Spirit or another resource?
2. Where is it stored or supplied, and where does it enter the weapon?
3. What visible route connects that supply to each firing channel?
4. Where does the charge/projectile sit immediately before firing?
5. Which parts move, which stay fixed, and what provides the apparent support and return motion?
6. What leaves the weapon: projectile, casing, vented energy, exhaust or nothing? Do not eject casings from an explicitly caseless design.
7. What changes after a shot, a rejected shot, an empty state and a reload?
8. What explains secondary effects without duplicating native costs or inventing extra damage?

Reject decorative magazines with no connection, a feed path through solid armor or the user's hand, disconnected triggers, blocked muzzle openings, and chamber locations that cannot align with their barrel. A fictional power cell can replace a mechanical feed only when that is deliberately specified and visibly coherent with the original weapon identity.

## Gate 2: spatial proof

- Build an untextured cutaway first. Label supply, transfer route, upper/lower chambers, moving assemblies, controls and support points.
- Trace the complete route from source to each destination. Check the exported geometry, not a diagram disconnected from the asset.
- Reserve swept volumes for cartridges/cells, moving parts, magazine removal and actual hand shapes. Check rotation as well as translation.
- Pairwise exceptions must be named and bounded: a cartridge inside its intended socket is different from a cartridge passing through a grip. No blanket collision exemption for an entire bone.
- Verify all angles, attached accessories, camera FOVs and handedness. Camera occlusion cannot excuse a defective mesh.
- Sample the exact interpolation and any blend curves. Sparse keyframe endpoints can miss intersections between keys; spline overshoot is a separate risk.

## Gate 3: hand and reload continuity

The support hand must actually reach and retain contact with the object it operates. Show release, withdrawal, handoff/retention, alignment, seating and return where applicable. Do not teleport a magazine, make fingers pass through a guard, or let the gun float while both hands leave it.

Track magazine ownership explicitly: attached to weapon, held, stowed or discarded. Exactly one owner at a time. During a handoff, preserve the world pose. Do not make two copies overlap or vanish to conceal a bad transition.

Empty and tactical sequences must reflect their declared chamber state. Interrupt at each meaningful phase, swap weapons, resume, aim, move and fire when allowed. Resume from actual state, not an animation timer that quietly restores missing ammo. Optional reload animation must not impose a new reload requirement on native AoA resource weapons.

## Gate 4: firing and feedback coherence

- A confirmed upper shot drives the upper recoil, muzzle cue and corresponding effects. The next confirmed primary shot uses the lower channel. Rejected inputs, duplicate packets, inspection and the native bonus grenade do not advance the sequence.
- Separate visual barrel motion, weapon motion, hand response and camera/gameplay recoil. Do not accidentally apply recoil twice.
- Use recoil recovery and supporting-hand response to sell mass. A giant muzzle flash cannot compensate for an unsupported or disconnected mechanism.
- Sounds, impact effects and particles must match the actual event and material. No extra projectile or hit from a cosmetic animation.
- Respect reduced-flash/reduced-motion settings and bounded effect budgets. Profile equivalent work before claiming performance parity.

## Gate 5: mesh and export integrity

Check positive dimensions, hierarchy, pivots, winding/normals, degenerate or duplicated faces, accidental open seams, internal faces exposed by motion, z-fighting, texture bleeding, UV bounds, attachment alignment and LOD silhouette. A barrel must actually have a readable bore; painting a dark rectangle behind a solid front face does not create one.

Export, re-import and compare. The authoring render must use the exported asset. Renderer-specific shading, culling, transforms and visibility require tests in the pinned TaCZ version. Decorative and structural overlap must be distinguished from unwanted clipping.

## Gate 6: native behavior and runtime acceptance

Preserve item identity, ammo/resource costs, fire timing, durability, enchantments, native effects and save behavior. Animation events may request cosmetics; they must not become an alternate authoritative ammo ledger. Validate duplicate/out-of-order acknowledgements, low FPS, resource reload, death, travel, reconnect and multiplayer observers. For turrets, also validate the actual host type, target filtering and resource policy.

Expensive geometry sweeps belong in authoring/build QA, not in every game tick. Runtime presentation should use prepared asset data, bounded effects and explicit native events; measure the resulting frame-time and startup behavior rather than assuming these offline tests imply performance parity.

## Evidence required to close a weapon

- Versioned mechanism brief and cutaway matching the exported model.
- Fail-before/pass-after fixtures for every corrected defect.
- Side/front/back/top/bottom, first-person and third-person review captures.
- Full animation and interruption matrix, including real hands.
- Native behavior tests and representative performance measurements.
- Explicit unresolved-issue list. Any missing mandatory proof leaves acceptance open.

**Current Baronator status:** alternating firing presentation authored; scoped clearance tests exist; mechanical feed, hand-rig and actual runtime acceptance remain open. This research raises the gate rather than retroactively declaring the prototype finished.
