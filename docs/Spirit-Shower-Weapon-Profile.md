# Spirit Shower — the three-path Spirit blaster

**AoA 3.7.1 / Minecraft 1.20.1. Source-backed baseline and proposed art; native upgraded weapon acceptance is still open.**

Spirit Shower fires three explosive projectiles with different gravity settings. Its localized tooltip calls them “3 explosive beams,” but the inspected implementation creates three separate projectile entities. A premium presentation must preserve that distinction rather than silently replacing the attack with a continuous laser.

## What the released weapon does

A firing override attempts to spawn one Shower Shot, one Weighted Shower Shot and one Heavy Shower Shot. Each receives an age parameter of 60. Their gravity returns are 0.05, 0.1 and 0.2. These are game inputs, not SI units or measured flight ranges. Original native flight footage remains required.

Both the block-impact override and the successful entity-impact effect request the explosion helper with strength input 2.5. That is not a final damage value or a guaranteed blast radius. The registered direct-damage input is zero; entity-impact effects remain conditional on the inherited energy-attack helper accepting the hit. Zero-damage handling, immunity and cancelled events need in-game verification.

| Released input | Value |
|---|---|
| Registry identity | `aoa3:spirit_shower` |
| Family | Spirit-powered blaster |
| Base direct damage | 0; explosive effects are separate |
| Durability | 2,870 |
| Firing-delay input | 10 ticks |
| Base Spirit cost | 100, before native modifiers |
| Spawn attempts per firing override | 3 |
| Projectile age parameter | 60 each |
| Gravity returns | 0.05 / 0.1 / 0.2 |
| Explosion helper strength input | 2.5 |
| Firing sound | ITEM_SPIRIT_SHOWER_FIRE |

The shared firing path consumes resources before entering the three-spawn override. Three visual channels must not accidentally charge the player three times. Animation callbacks cannot create extra authoritative shots or refund Spirit.

## Original identity and acquisition evidence

![Actual released Spirit Shower sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/spirit-shower-original.png)

The source sprite uses a compact dark chassis, pale branching structure and red accents. These are the visual anchors for the concept. Bone-like materials and captive Spirit cores are proposed art interpretation, not established maker or material lore.

The packaged Jawe loot table contains Spirit Shower with weight 4 in a one-roll pool whose entries total 162. The unmodified single-pool calculation is **4/162, or approximately 2.47%**. This is a data-table result, not proof that Jawe spawns or that the item is obtainable through that route in every installed release. Check the actual version's acquisition and world availability before presenting a walkthrough as verified.

The packaged upgrade recipe is **Spirit Shower + Apoco Upgrade Kit → Apoco Shower**. The inspected Apoco version retains the three projectile classes, gravity settings and explosion-strength inputs; its registered durability becomes 3,760 and base Spirit cost becomes 80. This makes preservation of the original three-path attack especially important when presenting the upgrade.

[Apoco Shower profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Shower-Weapon-Profile) · [Pinned evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/spirit-shower-released-evidence.json).

## Proposed premium design

![Spirit Shower concept with three-path discharge, inspection and optional shroud](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/spirit-shower-concept-v1.png)

The proposal develops the pale frame around three crimson Spirit reservoirs, with a dark emission assembly and a readable rear grip. Its concept inspection opens the upper shell around seated cores. The three descending effect trails illustrate different paths qualitatively; they are not captured original projectiles or measured trajectories.

- **Baseline:** retain the source attack, resource identity, progression and recognizable palette.
- **Alternate shrouds:** a more open frame or a focused emission housing. Cosmetic shrouds cannot silently alter damage or trajectory. Functional variants need explicit server-owned parameters and saved-build identity.
- **Spirit presentation:** seated cores brighten during charge and discharge. Recharge/reload is optional; no conventional magazine or forced manual reload is required.
- **Inspection:** hinge or slide owned parts through a defined path, then restore the exact ready pose. No loose parts, free attacks or resource changes.
- **Customization:** earned functional charms; modular barrels/shrouds, sights and handling parts; skins, stickers, animated/emissive decals and emblems; configurable projectile/tracer, impact and finisher presentation. All applicable groups remain subject to the shared completeness standard.
- **Art profiles:** preserve both Minecraft-fit texturing and a richer concept-faithful option. Detailed materials alone do not justify losing the source silhouette.

### Art and geometry review still required

This is a design study, not an accepted modeling blueprint. The pale spikes below the body and projecting rear details need hand, camera and animation-sweep clearance checks. The support hand needs a comfortable defined contact area. Three visible reservoirs are a proposed visual metaphor, not evidence of three independent magazines or a source mechanism. Establish side/top/rear construction and all moving-part ownership before production export.

## Effects and performance

The shared Shower Shot renderer uses red and black Sparkler particles. Its loop requests six particles per projectile render invocation. Extra render passes therefore matter; six is not a proven per-tick rate. Preserve the recognizable palette while moving any new trail system onto bounded game-time emission with measured density and native performance tests. Never use additional rendering passes to multiply gameplay effects.

Capture the original flight, block hit and entity hit first, then show them beside new concepts and native upgraded footage. Distinguish projectile motion, trail, impact particles, decals and death effects. A finisher must not trigger on a rejected hit or a target that survives.

## Release gates

- [ ] Verify native acquisition and Jawe/world availability for the exact target release.
- [ ] Capture original three paths, resource cost, cadence, impacts and immunity/cancellation cases.
- [ ] Produce faithful separate-part model, UVs and both material profiles.
- [ ] Validate hands, trigger/guard, attachment fit and swept animation clearance.
- [ ] Implement equip/holster, idle, aim, charge/fire/recovery, inspection and applicable optional recharge states.
- [ ] Implement declared attachment effects, salvage, charms and cosmetic customization.
- [ ] Confirm native TaCZ/presentation integration, multiplayer authority and original-mode fallback.
- [ ] Measure startup, frame time, low-percentile performance and memory with bounded effects.

[Full weapon completeness standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard) · [Reproducible source-audit bundle](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/spirit-shower-source-study-v1.zip).
