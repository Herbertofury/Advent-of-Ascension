# Soul Storm: spirit-channel authoring study

[Interactive geometry and motion preview](https://herbertofury.github.io/Advent-of-Ascension/soul-storm-lab.html) · [Original source and tests](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-authoring-study.zip) · [Weapon upgrade backlog](Weapon-Upgrade-Backlog)

![Original Soul Storm geometry study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-studio.png)

**In progress, not an installable weapon or finished AAA asset.** The original purple/cyan spirit-channel model has 77 cuboids, 19 bones and seven motion records. AoA identity belongs to Tslat and contributors. Reference-pack assets and game binaries are not bundled.

## Preserve what makes Soul Storm itself

Static inspection of the released AoA 3.7.1 / Minecraft 1.20.1 classes found damage constructor input 1.5, durability 3,190, one-tick delay and energy-cost input 2.0. The firing branch creates SoulStormEntity with an age input of 60 and references ITEM_SPRAYER_FIRE. These are static observations, not a native adapter test.

The redesign uses a visible suspended spirit core, a clear channel and open resonator fins. It does not invent bullets, magazines or mandatory reloads. Cosmetic recovery never restores Spirit. The native one-tick cadence must not be blocked by a longer visual envelope.

[Released-class evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-native-contract.json)

## Motion and feedback work

- Static inspection pose, turning spirit core, fire pulse, draw, put-away, inspect and cosmetic recovery clips.
- A separate original damped cosmetic response retains its current pose on rapid retrigger instead of snapping back to the first frame. The response is bounded and never authorizes a shot, resource payment or damage.
- The preview sleeps when static or settled, pauses correctly and respects reduced-motion startup. It uses a flat-color authoring renderer; it does not represent Minecraft lighting or final effects.

## What the tests actually establish

| Check | Result | Boundary |
|---|---|---|
| Moving core, ring and emitter against exported solids | 1,135 sampled poses, zero detected penetrations | 120 Hz plus authored keys; not continuous collision proof |
| Right-arm proxy clearance | 1,123 poses each for Steve-width and Alex-width boxes | Named palm/grip contact allowed; actual hands, skin, FOV and left-hand choreography unqualified |
| Cosmetic response | Partition-consistent damped integration; pose-continuous retrigger; bounded 20 Hz sequence and impulse spam; settles at rest | Original response model, not native recoil/gameplay |
| Viewer controls | Seven records, static idle, pulse, retrigger, pause/resume and settled rendering verified in Node harness | Real browser review separate; no native game certification |
| Source archive | Clean extraction regenerates the viewer byte-for-byte and reruns scoped tests | Requires Python/Pillow and Node; not a mod installer |

[Spatial report](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-spatial-qa.json) · [Arm proxy report](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-hand-fit-qa.json) · [Reproduction receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-reproduction.json)

## Remaining acceptance gates

- [ ] Complete hand choreography, view alignment and TaCZ pose conventions across FOV/skins/handedness.
- [ ] Refine material detail and silhouette; review all views and every interrupted transition.
- [ ] Add original resource-aware sound/VFX with bounded particles and non-strobing accessibility options.
- [ ] Implement the actual AoA Spirit/projectile adapter, keeping server authority and native item identity.
- [ ] Prove multiplayer, save persistence, resource exhaustion, missing optional mods and migration behavior.
- [ ] Measure cold/warm startup, memory, frame-time lows and tick cost in the real target pack.

The arsenal queue now records three started weapon studies. None of the 228 first-lane gun/shotgun/sniper/cannon/blaster registrations has passed every final acceptance gate.
