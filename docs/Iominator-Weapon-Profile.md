# Iominator — original weapon and premium concept

**Baseline: Minecraft 1.20.1 / AoA 3.7.1. Concept exploration and released-file research; not a completed native TaCZ weapon.**

## What it is and does

Iominator is the emerald, cyan, yellow and dark-blue evolution of Abominator. The released recipe combines **Abominator + Ancient Upgrade Kit → Iominator** at the Divine Station. Its shared gun behavior is automatic and uses **Limonite Bullets**; it constructs the `ToxicBulletEntity` projectile rather than the ordinary inherited bullet class.

That class name is not proof of poison damage. In this pinned release, ToxicBulletEntity declares constructors but no custom hit-effect method. The inspected inherited entity/block impact hooks and BaseGun's special-effect hook are empty. Damage follows shared gun attack handling, including enchantment and attack-path modifiers. **A poison status effect, lingering acid pool or chaining beam is not established by these inspected paths.** External event handlers and the actual pack remain a separate test obligation.

## Released values and behavior

| Property | Verified released input / path |
|---|---|
| Registry ID | `aoa3:iominator` |
| Family | Gun / BaseGun |
| Base damage input | 2.875 |
| Durability input | 6000 |
| Firing delay input | 3 ticks |
| Stored recoil argument | Approximately 0.95; not a camera-angle measurement |
| Ammo | Limonite Bullet, inherited |
| Automatic | Yes, inherited BaseGun method |
| Projectile | ToxicBulletEntity |
| Projectile lifespan argument | 120 |
| Projectile damage multiplier argument | 1.0, not a launch-speed value |
| Projectile pierce argument | 0 |
| Firing sound | `ITEM_GUN_GENERIC_FIRE_1` |

These are registration and method inputs, not guaranteed effective DPS, measured range or final target damage. At ideal 20 TPS the delay input corresponds to 0.15 seconds, but actual firing cadence requires runtime verification. Lifetime expiry, collision and entity update ordering also prevent equating the lifespan argument to a measured flight duration.

## Original appearance, flight and impact

![Exact released Iominator sprite, nearest-neighbor enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-sprite-preview.png)

The recognizable anchors are the green body, cyan horizontal stripe, repeated yellow accents, dark downward section and large blue-green rear loop silhouette. Preserve these anchors even when the geometry becomes more sculpted and luxurious.

![Released Limonite bullet texture used by ToxicBulletRenderer](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/limonite-bullet-texture-preview-1.20.1.png)

The actual renderer registration maps ToxicBulletEntity to **ToxicBulletRenderer with the Limonite bullet texture**. Its render method requests **eight green FLICKERING_SPARKLER particles per render invocation**, with scale 1 and age modifier 3. The latter is not a verified three-second lifetime.

This is a texture/bytecode reference, **not original in-game flight or impact footage**. The visual effect's source call frequency is coupled to rendering; it must not become a promise of fixed per-second emission or an FPS benchmark. The upgraded effect should use a paused game-time clock and bounded cosmetic budget, with native visual comparison before accepting the change. [Presentation core](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Presentation-Core).

## Premium directions and visual effects

![Iominator concepts with corrected grip placement and three visual directions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-concept-exploration-v2.png)

- **Verdant Legacy:** faithful ballistic mode, green spark accents and a restrained readable tracer. Preserve the original damage/resource contract; the depicted impact flourish is proposed presentation, not recovered original footage.
- **Ancient Lattice:** optional ion-focusing conversion with a visible muzzle change and a coherent, narrow energy presentation. Any new beam behavior needs explicit collision, resource, damage and networking implementation.
- **Prism Bloom:** optional branching energy conversion. Visible branches must correspond to real declared projectile/target behavior, costs and limits. Cosmetic branches must be labeled as cosmetic rather than implying extra hits.

The upgraded model should offer animated inspection, reactive but readable emissives, customizable sights, skins, charms and decals. Reloading remains optional and must fit the resource mode. The concept sheet does not establish a magazine/feed design or validate mechanical operation.

### Concept QA and retained history

[Version 1 is retained](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-concept-exploration-v1.png). It placed the apparent main grip too far forward of the trigger. Version 2 moves the grip behind the trigger and restores a visibly open guard without shrinking it. This corrects the obvious illustration issue; hand-rig reach, rear-loop wrist clearance, reload/inspection motion and mesh collision still require authored 3D tests. A polished picture is not a passed mechanism gate.

## Editable geometry and motion study

![Actual exported cuboid geometry in a Blender authoring preview](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-authoring-v3-iominator-studio.png)

[Download editable source versions 1–3](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/iominator-authoring-v1-v3.zip). The current study has 10 bones, 236 cuboids, an original 128×96 texture atlas and idle, firing, draw and inspection clips. It preserves the rear loop and broad color identity but **does not yet meet the concept's sculpting/material quality**. It is an editable blockout and motion foundation, not a finished gun or installable pack.

![Inspection motion authoring preview](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-inspect-authoring-v3.webp)

![Firing recoil authoring preview](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-shoot-authoring-v3.webp)

These use the authored keyframes in Blender, without render-only bevel geometry. The firing replay includes a pause for readability; it is not a recording of native cadence. The palette atlas is mapped in the preview, but lighting/materials and interpolation are not native renderer validation.

[Bounded structural/spatial QA](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-authoring-v3-qa.json) passes parent references, finite positive cubes, UV bounds, animation keys/neutral endpoints and trigger separation from two guard bars using oriented-box tests. All-hand collision, wrist clearance, reload/feed design, LOD, native export and visual acceptance remain open.

## Acquisition and customization preservation

[All illustrated Divine Station routes for 1.20.1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Divine-Station-Weapon-Upgrades-1.20.1) show this exact route. The base recipe copies its configured output stack, so preservation of an Abominator's name, enchantments, charms and attachments must be intentionally implemented and tested. Do not silently transfer incompatible parts or overwrite unknown extension data.

## Acceptance still open

- [ ] Capture original flight, hit effects and actual firing cadence in the pinned release.
- [ ] Author the editable model, UVs, textures, LOD and complete animation set.
- [ ] Validate comfortable hands, trigger reach, rear-loop clearance and attachment envelopes.
- [ ] Verify vanilla-compatible resource mode and any optional reload/conversion behavior.
- [ ] Compare fixed-time effects at multiple render rates and shader passes without losing intended presentation.
- [ ] Test multiplayer, saves, upgrade-data transfer and equivalent-work performance.

[Released evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/iominator-released-evidence.json) · [Audit tool and exact concept prompts](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/iominator-audit-tool-v1.zip) · [Abominator profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Abominator-Weapon-Profile)

Original source art and mod: Tslat and AoA contributors. Generated concept art is our proposed interpretation, not an extracted game model.
