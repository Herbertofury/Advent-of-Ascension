# Reusable animation and cosmetic core

**Original engine-independent Java source · compiled and tested on Java 17/21 · native integration pending.**

[Download the consolidated source package](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-presentation-core-v2.zip) · [Exact test output and archive hash](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-presentation-core-v2-tests.json).

This brings four reusable presentation primitives into one package. It does not contain a Minecraft mod entry point or native hooks, and is not a file to put in the Mods folder. Earlier standalone studies remain available for provenance.

| Component | What is implemented | Boundary |
|---|---|---|
| SoulSightFrame | Reusable atlas-frame output, explicit Flame/Candle/Gem and display-pass gates, reduced-motion frame | Actual textures, bone transforms, buffers and native game clock still need an adapter |
| ImpactVisualLedger | Bounded cosmetic event identity with separate weapon/projectile branches, actor/weapon/world separation | Finite window; evicted events can be accepted again; never server damage validation |
| EmissionClock | Per-emitter game-time scheduling, duplicate-timestamp suppression, visibility rebasing and bounded stall recovery | Cosmetic requests only; production visual budgets and native particle pools remain unvalidated |
| FrameVisibilitySet | Pre-bound discrete frame visibility, duplicate-part validation, no-op repeated selections and explicit disposal | Native bone binding and pass ownership remain adapter responsibilities; discrete frames do not implement crossfade |

## Visibility is different from zero scale

The pinned [TaCZ BedrockPart render path](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/client/model/bedrock/BedrockPart.java) checks its visibility flag and then transforms/compiles nonempty parts. The inspected path has no equivalent early-out for a zero scale alone. A frame-bone effect should not assume that collapsing unused planes removes their CPU submission work.

The new helper validates a complete set of actual part identities before changing visibility. It hides all frame targets once on binding. Repeatedly selecting the same frame performs no writes; a frame change touches only the old and new targets. It hides on invalid selection/disposal and rejects use after disposal. Bindings must belong exclusively to this owner and must be rebuilt after resource reloads. Callbacks must be nonthrowing cosmetic assignments.

Tests cover 15 parts, repeated selections, changing frames, bad indices, duplicate native identities through distinct callback wrappers, null bindings, disposal and separate instances. These tests count visibility writes; they do not measure TaCZ frame time or certify native integration.

A further source detail matters for future effect exports: the presence of a standalone Step interpolator class does not mean Bedrock `lerp_mode: step` is supported. The pinned [LerpMode enum](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/api/client/animation/AnimationChannelContent.java) does not include STEP, and the inspected [scale-channel conversion](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/api/client/animation/Animations.java) falls back to linear for unknown values. Validate the actual import/playback path instead of trusting an exporter label.

## Why timing is separate from rendering

The [released Hive Blaster renderer](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hive-Blaster-Weapon-Profile) requests particles inside its render method and keeps its color counter on the renderer. The new clock is intended to avoid copying render-invocation-dependent emission into the upgraded presentation.

The scheduler test supplies the same ten seconds of game time at 20, 30, 60, 144, 240, 1000 and 2000 updates per second. Each schedule produces 400 requests using a 40-per-second test rate. Repeating a timestamp emits nothing. Paused time, two emitters, hidden/resume transitions, clock rollback, invalid values and long stalls are also exercised.

These are simulated input cadences, not achieved game FPS. The rate 40 is a math fixture, not the chosen particle density for any weapon. Long stalls and configured caps intentionally drop excess cosmetic requests rather than accumulating a backlog; that tradeoff needs visual acceptance.

## Safe integration contract

- Drive updates from the appropriate paused game/presentation clock, not wall time.
- Own state per emitter/render owner. Notify the clock when emission stops; it cannot infer invisibility from silence alone.
- Apply the event ledger once per logical branch notification, then fan out to configured effects. Do not use it once per particle, camera or shader pass.
- Keep gameplay projectiles, damage, resource costs and authority outside this package.
- Treat world generations and event identities as adapter responsibilities. The ledger is not authentication or permanent replay protection.
- Draw existing effects across supported views/passes without spawning them again.

## Verification and remaining work

The source compiled with an actual Corretto 17 JDK and ran its four test mains on that runtime and OpenJDK 21. This establishes pure-core JVM checks, not Minecraft 1.20.1/1.21.1 API compatibility.

Native hook placement, original-versus-upgraded visual comparison, real hands/aim, interruption, shader/Vulkan behavior, networking, saves, allocations and frame/tick measurements remain open. No numeric source test substitutes for those gates.

[Sight integration plan](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Flame-Native-Renderer-Plan) · [Customization](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization) · [Authoring reproducibility](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Authoring-Reproducibility)

[Earlier consolidated v1 source remains available](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-presentation-core-v1.zip).
