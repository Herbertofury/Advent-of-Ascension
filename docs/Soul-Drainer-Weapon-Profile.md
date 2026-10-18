# Soul Drainer — life-leech blaster

**Baseline: AoA 3.7.1 / Minecraft 1.20.1. Source and released-class study; native playtesting is still pending.**

## What the original does

Soul Drainer is a rapid Spirit-consuming blaster with a life-leech effect. Its weapon-specific impact hook calls `EntityUtil.healEntity(shooter, 0.5f)`. The inspected shared legacy impact path invokes that hook after the energy-projectile attack reports success. The utility checks that the shooter is alive, above zero health and below maximum health before requesting healing. This is a fixed healing input, not evidence of a percentage-of-damage conversion, resurrection or unlimited overheal. Other mods and native healing events can affect final results.

Its cyan/teal claw-like forward silhouette, dark center, silver collar and gold rear ring are visual identity anchors. It is distinct from Soul Storm's circular blue chamber and stacked disc upgrade.

## Original inputs and effects

| Property | Inspected evidence |
|---|---|
| Item | `aoa3:soul_drainer` |
| Damage input | approximately 0.2 |
| Durability input | 3770 |
| Fire-delay input | 1 tick |
| Base Spirit-cost input | 2 |
| Projectile | `SoulDrainerShotEntity`, constructor maximum-age input 1 |
| Weapon impact hook | Requests 0.5 healing through the shared utility |
| Firing sound | `ITEM_DRAIN_GUN_FIRE` |
| Original projectile presentation | Red flickering sparklers, despite the cyan weapon art |

The original renderer adds three `FLICKERING_SPARKLER` particle requests per invocation, with scale input 1, age-modifier input 3 and red color. Those are static renderer inputs, not a measured per-second particle budget. Age modifier 3 is not proof of a three-tick lifetime. Maximum-age input 1 is not a measured range claim.

The new cyan returning-wisp visualization below is a proposed effect. Do not pass it off as original footage. Original flight, successful/failed impacts, healing, Spirit costs and effective range all need actual captured comparison tests.

## How to obtain it

The released upgrade recipe combines **Blood Drainer + Fungal Upgrade Kit → Soul Drainer** using `aoa3:upgrade_kit`. Do not invent a standard crafting-grid recipe for it. The acquisition chain for Blood Drainer and its kit should link to their version-specific entries.

## Art and attachment exploration

![Actual released item sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-drainer-original-sprite.png)

![Original Soul Drainer premium concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-drainer-concept-exploration-v1.png)

The generated ring-grip pose is an ergonomic idea, not proof of hand clearance. Its upper-right arrow directions are illustrative and must be made unambiguous in final animation: attack travels toward the target; any returning essence visualization travels back toward the shooter. Do not use the art to define collision geometry or healing authority.

- **Siphon Claw:** articulated focus prongs around a discrete pulse; keep the familiar claw silhouette.
- **Soul Thread:** optional sustained spectral-tether conversion. Explicitly define obstruction, range, resource drain and server damage/healing intervals. It is not a claim that the original is a beam.
- **Harvest Bloom:** optional expanding ring projectile with declared target eligibility, count, damage, resource and healing rules.
- **Gilded Wisp charm and Tidal Runes decal:** original customization concepts. A charm's bonus and unlock condition must be specified; the decal remains explicitly cosmetic unless a functional module is fitted.

## Critical QA for life leech

- [ ] No healing from misses, blocked/failed attacks or duplicate callbacks unless a separately declared upgrade intentionally changes those rules.
- [ ] Test invulnerable targets, full-health/dead shooters, multiplayer ownership, reflected projectiles, multipart bosses and simultaneous defeats.
- [ ] Separate accepted gameplay healing from client wisps; a particle cannot grant health.
- [ ] Preserve resource transactions, kill credit, loot and compatibility with health/attribute mods.
- [ ] Implement native model/animations, attachment interfaces and real hand clearance; this concept is not a finished weapon.
- [ ] Capture original red sparks and proposed effects side by side under matching game settings.
- [ ] Measure actual frame/tick performance and publish remaining failures honestly.

[Released evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-drainer-released-evidence.json) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades) · [Customization](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization)
