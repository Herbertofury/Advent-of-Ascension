# Minigun: industrial nostalgia amplified

**Current gameplay direction:** original behavior is the baseline, not the ceiling. Attachments may intentionally increase damage/projectile count and change firing patterns, resources and effects. See [Functional weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades). Accidental duplicate callbacks remain bugs; deliberate multishot is a feature.


**Concept exploration, not an installed remodel.** Keep the original bright orange body, graphite structure, pale steel, round side medallion, compact multi-barrel front and rear striped/ribbed detail.

![Minigun concepts with corrected single-muzzle firing instant](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minigun-concept-exploration-v2.png)

A is closest to the source's compact silhouette; B explores stronger armored mass; C explores cleaner premium surface detail. These are working art assessments, not final owner approval. The six-tube rotor is our chosen visual interpretation of the sprite's multi-barrel front.

## Concept QA correction

The first generated feedback panel depicted multiple simultaneous muzzle flashes. The corrected panel shows one active muzzle at the captured instant and leaves the other openings dark. Rotor motion is cosmetic: do not accidentally duplicate accepted shots or add an unrequested mandatory spin-up delay or force a reload into the native one-tick firing cadence.

## Attachment personalities

![Eight Minigun attachment directions and two imagined builds](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minigun-attachment-concepts-v1.png)

| Concept | Intended role | Required check |
|---|---|---|
| Rotary Shroud | Protective cluster exterior | Every bore open, no rotor contact |
| Thermal Mantle | Cosmetic thermal-fin personality | No invented mandatory overheat mechanic |
| Survey Optic | Compact sight | View alignment, carrying-handle and hand clearance |
| Gyro Grip | Comfortable support/handling personality | Full-size hands and unobstructed controls |
| Carry Harness | Strong support frame | Connected supports outside rotor and grip travel |
| Reserve Drum | Optional resource-capacity appearance | Coherent connection, native resource identity and atomic payment |
| Tracer Prism | Spectral color/effect appearance | Cosmetic status clear, bounded particles and reduced effects |
| Salvager Badge | Collectible cosmetic crest | Preserve the orange/steel identity, no hidden gameplay buff |

Industrial Sentinel and Spectral Runner demonstrate customization fantasies. Their handles, drum mounting and sight clearances need actual geometry review; generated assembled art is not proof of fit.

## Remaining model gates

- [ ] Compare original sprite, selected concept and actual mesh at gameplay scale.
- [ ] Preserve open bores and consistent rotor phase across start, stop, resume and retrigger.
- [ ] Keep carrying and support grips comfortable without shrinking hands or controls.
- [ ] Qualify coherent optional resource presentation and complete hand choreography.
- [ ] Author original audio and bounded muzzle effects; test accessibility options.
- [ ] Prove native item/resource behavior, client/server synchronization, saved data and measured performance.

[Earlier rotary authoring study](https://herbertofury.github.io/Advent-of-Ascension/minigun-motion-lab.html) · [Attachment gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Attachment-Concept-Gallery) · [Weapon backlog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog)
