# Predigun: separate bone belt, original ammunition contract

**AoA 3.7.1 / Minecraft 1.20.1 · artifact-backed source profile and partial concept art · native upgrade unaccepted.**

## The important distinction: projectile versus inventory ammunition

Predigun creates a `BoneBulletEntity`, but it does not override `BaseGun.getAmmoItem()`. The inspected inherited method returns **Limonite Bullet**. A bone-shaped projectile class and the requested bone-ammo belt appearance do not authorize changing the inventory cost to ordinary bones.

The proposed external belt can present bone-styled ammunition while preserving the original resource contract. Exact consumption, enchantment exceptions, creative-mode behavior, multiplayer authority and actual projectile rendering still require native capture. Do not infer those details solely from a class name or a painted belt.

## Original source behavior

The checked class extends `BaseGun` and inherits fully automatic firing. Its firing sound is the Minigun automatic-fire sound, with a pitch adjustment of 1.1; the release callback selects the Minigun wind-down sound.

| Stored constructor input | Value |
|---|---:|
| Base damage | 1.0 |
| Durability | 6120 |
| Delay | 1 tick |
| Recoil constructor input | 1.0 |

These are stored inputs, not final damage, measured sustained fire rate or measured recoil. The inherited `getRecoilModifier()` inspected in this artifact returns approximately **0.35**, not the constructor input above. Later calculations and client application must be reviewed before describing the actual kick.

The projectile constructor passes 120 and 0 into the checked lifespan/piercing path. These fields alone are not a promise about flight duration, collision outcomes or effective damage in a modpack.

## Upgrade and dimension evidence

The bundled upgrade recipe combines **Minigun** with a **Predator Upgrade Kit** to produce **Predigun**. It does not establish that third-party attachment data, names or effects transfer correctly; those need explicit preservation tests.

The kit is referenced by a bundled Barathos world loot table. This is an acquisition-related source association, not proof that the table or dimension is active in this release and not exclusive creator lore.

[Recipe and loot-reference index](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-origin-data-index-1.20.1.json) · [Exact artifact-backed inspection receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/predigun-source-profile-evidence-1.20.1.json).

## Selected long-body concept and preserved history

![Predigun long machine-gun concept with separate hanging bone belt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predigun-bone-belt-concept-v3.png)

Retain the longer machine-gun proportions and distinctive dorsal fins. The ivory shapes on the side are a separate linked belt with a hanging curve, not fixed ribs or armor fused to the body. Three-dot and glyph details are decorative film nods, not automatic targeting, thermal vision or a change in damage.

[Compare released reference and selected concept](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Apredigun) · [Earlier fin-blade exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predigun-fin-blade-concept-v2.png) · [First exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predigun-concept-v1.png).

## Separate belt-motion study

![External bone-belt motion study: rest, advance and settle](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predigun-bone-belt-motion-study-v1.png)

This is a static exterior-motion storyboard, not a validated feed mechanism, mesh, animation or gameplay test. The belt must remain visibly separate, avoid the hands and grip, and settle coherently after movement. A cosmetic advance must not consume resources independently of the original server-authorized shot. Do not add a forced spin-up or manual reload merely because the visual design resembles a heavy machine gun.

## Implementation and completeness gates

- [ ] Capture original firing, release sound, resource use and projectile appearance with AoA and TaCZ together.
- [ ] Validate long-body silhouette, dorsal-fin consistency, grip placement and first/third-person hand clearance.
- [ ] Separate the visual belt from the receiver mesh; review its motion through fire, inspect, aim, movement and interruption.
- [ ] Preserve original shot cadence and resource behavior; test repeated input, cancellation and multiplayer events.
- [ ] Produce identity-specific sights, muzzle options, feed alternatives, finishes, decals, charms, tracers, impacts, finishers, audio/accessibility and build-interface sheets. The current belt study is not a complete customization package.
- [ ] Qualify export, save/load, attachment transfer, compatibility and measured performance before native acceptance.

## Provenance and limits

Inspection uses the official AoA 3.7.1 / Minecraft 1.20.1 artifact with SHA-256 `f417ecb337d4a3b2aebec559a9262d8a86cc93ee7910f4eea64108bff063193a`. The receipt records hashes for Predigun, BaseGun, BoneBulletEntity, BaseBullet and the upgrade recipe. Original classfiles, decompiled source and the game JAR are not redistributed here.

[Stored baseline index](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-baselines-compact-1.20.1.json) · [Released class-routing map](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/released-weapon-behavior-map-1.20.1.json) · [Complete feature standard](Weapon-Completeness-Standard).
