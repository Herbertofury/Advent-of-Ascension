# Soul Storm: nostalgia amplified

**Current gameplay direction:** original behavior is the baseline, not the ceiling. Attachments may intentionally increase damage/projectile count and change firing patterns, resources and effects. See [Functional weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades). Accidental duplicate callbacks remain bugs; deliberate multishot is a feature.


**Concept art first.** Preserve the AoA weapon's recognizable identity, then earn the upgrade through outstanding silhouette, materials, animation, sound and effects. These images are design references, not in-game screenshots or completed models.

## Original identity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sprite.png" alt="Original AoA Soul Storm item sprite, enlarged without changing its pixels" width="256" />

Original AoA sprite and identity: Tslat and contributors. The key visual anchors are its compact silhouette, indigo/cobalt/purple body, bright cyan accents, circular rear motif and striped/finned forward emitter. The source sprite is a low-resolution identity reference; added material detail and mechanical articulation are new art direction.

## Exploration

![Soul Storm A/B/C concept exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-concept-exploration-v1.png)

**B is the current working direction**, selected for the readable circular spirit chamber, connected energy channel and strong emitter silhouette. This is a design choice, not a claim of final owner approval for every detail.

## Developed direction and feedback

![Soul Storm B development concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-design-b-development-v2.png)

The first generated development sheet had an inconsistent top view and straight-looking projectile train. The next pass corrected the top-view direction and added a gravity-curved stream. Generated multiviews remain illustrative: final orthographic truth must come from the actual mesh, with consistent silhouette, grip, crest and emitter geometry in every view.

### Visual hierarchy

- **Primary:** an integrated circular armored spirit chamber, compact confident grip and recognizable four-plate emitter.
- **Secondary:** layered indigo shell, dark recessed structure, protected energy channel, narrow metal trim and a purposeful crest.
- **Detail:** restrained cyan inlays, material roughness variation and small spectral accents. Detail must support the silhouette rather than bury it.
- **Motion:** subtle idle vortex, deliberate ring/emitter articulation, pose-continuous rapid-fire response and readable recovery.
- **Effects:** discrete Spirit projectiles with short wispy trails, not a continuous laser. Avoid opaque smoke, excessive bloom and full-screen flashing. Provide reduced-effects and camera-motion options.
- **Audio:** preserve the recognizable sprayer-like identity while developing layered original feedback. No imported commercial-game audio is assumed.

## Plasma soul discs and functional stack upgrades

The owner requests alternating top-to-bottom plasma-disc emitters and expandable four/five/six/higher stacks. These may genuinely increase output and damage. [Full weapon profile and original/new comparison](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile) separates native values from proposed upgraded builds. Original sprite inspection shows five bright horizontal emitter bands.

## Gameplay fidelity is part of the art brief

Released AoA3.7.1 / Minecraft1.20.1 inspection records one-tick firing delay, energy-cost input2.0, SoulStormEntity with age input60, and ITEM_SPRAYER_FIRE. The projectile class returns approximately0.6 for the method corresponding to gravity in the matching source. These observations constrain the adapter; they are not native runtime certification.

Keep original-mode Spirit payment, projectile behavior and firing admission; upgraded builds may deliberately change them through explicit components. Do not add conventional bullets, a cartridge magazine, forced reload, an animation-imposed firing delay, or a straight laser substitution. VFX should follow the build’s actual projectile trajectory. A flight-changing upgrade may intentionally change that trajectory, with its behavior and values documented.

[Native contract evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-native-contract.json)

## What the old model taught us

![Earlier technical blockout, not the visual target](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-studio.png)

The earlier square cage, floating cube, slab-like emitter and thin crest failed the requested visual quality. Its collision and animation tests remain useful technical scaffolding, but passing those checks does not make the art good. Rebuild the silhouette and materials toward the concept, rather than polishing the rejected blockout into a release.

## Model and acceptance gates

- [ ] Establish consistent three-dimensional structure from the hero and side design, then render real front/top/side views from the mesh.
- [ ] Compare original sprite, concept and actual model at inventory, first-person and third-person sizes.
- [ ] Preserve an uncluttered nostalgic silhouette at thumbnail size; inspect grayscale/value separation too.
- [ ] Fit full-size hands with comfortable clearance and plausible support, without shrinking hands, grip or controls to hide intersections.
- [ ] Validate moving shell/ring/emitter geometry through interrupted and repeated actions.
- [ ] Author original materials, sound and bounded VFX; measure cost instead of promising zero overhead.
- [ ] Match the native behavior and complete real-game first/third-person, multiplayer, save and performance tests.

[Earlier technical study and scoped QA](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Authoring-Study) · [Arsenal backlog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog)
