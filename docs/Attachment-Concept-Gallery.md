# Attachment playground

**Current gameplay direction:** original behavior is the baseline, not the ceiling. Attachments may intentionally increase damage/projectile count and change firing patterns, resources and effects. See [Functional weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades). Accidental duplicate callbacks remain bugs; deliberate multishot is a feature.


**32 initial concept directions, not implemented modules or an exhaustive catalogue.** Build a collection worth experimenting with: recognizable AoA weapons, memorable parts, expressive effects and coherent assembled silhouettes. Concept art comes before modeling; every combination still needs real fit, gameplay and performance qualification.

[Modular armory and effect salvage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage) · [Soul Storm art direction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Art-Direction) · [Baronator art direction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Baronator-Art-Direction)

## Soul Storm: magical modularity

![Soul Storm attachment concepts and two imagined loadouts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-attachment-concepts-v1.png)

| Concept | Intended role | Design gate |
|---|---|---|
| Prism Crown | Spectral discharge-shaping emitter | Keep the base identity and an explicit projectile/effect budget; declared intentional damage/projectile multipliers |
| Echo Halo | Supported arcane emitter ring | Real support and collision-free articulation; no floating disconnected shell |
| Wisp Lens | Compact magical optic | Clear sight picture, aligned view and room around crest/hand |
| Runic Damper | Fictional sound/flash-softening muzzle appearance | Define what is quieter; no absolute silence or invisible magical attack claim |
| Anchor Grip | Comfortable support grip | Full-size hand fit, accessible stance and interruption checks |
| Spirit Vessel | Stored-resource visual module | Paid native resource and capacity transaction; never free regeneration from animation |
| Frost Memory | Cold-themed effect core | Pin actual donor behavior and stacking rules; do not infer unimplemented freeze mechanics |
| Storm Relay | Chain-themed effect core | Bounded targets/events, ownership and no recursive proc loops |

Quiet Explorer and Prism Tempest illustrate build personalities. The generated assembled silhouettes are ideas, not guaranteed fits. In particular, orientation and module mounting must be reconciled against one consistent base mesh before implementation. The base Soul Storm must remain recognizable when modules are removed.

## Baronator: weight and mechanical personality

![Baronator attachment concepts and imagined loadouts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-attachment-concepts-v1.png)

| Concept | Intended role | Design gate |
|---|---|---|
| Siege Shroud | Bold twin-barrel exterior armor | Preserve both muzzle openings and independent recoil travel |
| Twin Runic Dampers | Paired fictional sound/flash module housings | Check each moving barrel separately; no real device internals or absolute-silence promise |
| Admiral Sight | Raised optic | Align actual aim and check animation/hand/receiver clearance |
| Bulwark Brace | Rear support and handling personality | Do not turn a nostalgic compact weapon into an unwieldy generic rifle; folding motion needs clearance |
| Anchor Foregrip | Full-size off-hand support | Comfortable grip and coherent connected mount |
| Reserve Pod | Optional resource-capacity module | Keep native ammo identity and atomic payment; no hidden free capacity |
| Broadside Memory | Boss-effect collectible | Separate the proposed core from native bonus-grenade behavior; no duplicated shot/event |
| Baron Crest | Armor crest and cosmetic inlay | Cosmetic status remains visible; no hidden gameplay modifier |

Fortress and Quiet Crimson communicate different play styles. The concept's brace/hand opening and receiver proportions must be reconciled in actual geometry. Neither a pretty drawing nor a generic mount certifies that recoil, reload or a full hand fits.

## Cross-weapon salvage, collectibles and cosmetics

![Effect cores, cosmetic modules and an imagined modification bench](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/effect-salvage-concepts-v1.png)

| Concept | Intended role | Design gate |
|---|---|---|
| Seed Heart | Botanical resource/effect identity | Explicit seed-tag/resource adapter; preserve legitimate acquisition and payment |
| Golden Cloud | Owned area-effect concept | Owner attribution, lifetime, cleanup and bounded persistent entities |
| Echo Coil | Delayed-effect memory | One bounded secondary event, no self-recursion or duplicate rewards |
| Lunar Lens | Moon-glass optic/cosmetic | State clearly whether it changes visuals only or has a separately tested gameplay adapter |
| Shyre Prism | Bright realm-inspired lens | Preserve readable aim, modest bloom and the base weapon's identity |
| Crystal Chorus | Crystalline emitter trim | Check muzzle and animation envelope; separate cosmetic trim from projectile conversion |
| Living Wrap | Flexible botanical grip covering | Maintain hand space and avoid excessive physics cost; cosmetic by default |
| Realm Inlays | Color panels and small charms | Preview palette/identity changes; bounded secondary motion and safe missing-asset fallback |

The bench is concept art, not an existing user interface. Extraction, salvage currency, compatible socket selection and final installation must be separate, reversible and server-authoritative operations.

## Minigun: industrial modularity

![Minigun attachment exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minigun-attachment-concepts-v1.png)

Rotary Shroud, Thermal Mantle, Survey Optic, Gyro Grip, Carry Harness, Reserve Drum, Tracer Prism and Salvager Badge extend the collection with eight orange/graphite/steel concepts. [Minigun art direction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Minigun-Art-Direction) records roles and fit gates. Cosmetic thermal/rotor presentation must not add unrequested overheating, spin-up delay, forced reload or extra native shots.

## Expanding the collection

Next concept families include additional optics/reticles, stocks and handling variants, family-appropriate feeds or magical conduits, charge/recovery personalities, living finishes, dimension-themed skins and deliberately unusual supported hybrids. Each new part should create a distinct look or play decision rather than be a duplicate icon with a bigger number.

## Shared quality gate

1. Compare original weapon, selected concept and actual assembled model at gameplay scale.
2. Keep physical sockets, cosmetic overlays and gameplay effects separate.
3. Check every moving part, hand, sight and muzzle across supported combinations and interrupted actions.
4. Map native resource payment and donor-effect semantics before promising functionality.
5. Cache assembly resolution at changes; no per-frame registry scans or geometry QA.
6. Test native client/server behavior, save migration, optional dependency absence and measured startup/frame/tick cost.

Pinned TaCZ source exposes scope, muzzle, stock, grip, laser and extended-magazine slot types. Our broader barrel, conduit and effect-core system requires an explicit assembly layer and version-specific adapter; these concepts do not claim stock gunpack JSON already implements all of it.
