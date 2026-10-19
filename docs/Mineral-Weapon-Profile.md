# Mineral · rose-armored Rocky upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## What the original does

Mineral is a **Metal Slug BaseSniper**. Its released class declares the constructor, a metallic sniper/long firing sound and a pitch-adjust input of 0.1. It does not declare a special impact, ammunition, projectile-creation or scope override; SCOPE_1 is inherited.

The name and rocky styling do not establish mining, bonus ores, gem ammunition, explosions or armor-piercing behavior. Those would require separate source evidence or an explicitly designed new conversion.

| Registered input | Value |
|---|---:|
| Damage | 58.5 |
| Durability | 560 |
| Firing delay | 112 ticks, nominally 5.6 seconds at 20 TPS |
| Recoil modifier | Approximately 0.035 |
| Ammunition | Metal Slug |
| Scope | Inherited SCOPE_1 |
| Sound pitch-adjust input | 0.1 |

These values are constructor/sound inputs, not measured final damage, recoil displacement, effective range or a recording of the heard sound. Preserve the slow, deliberate firing contract when designing cosmetic motion.

## Original identity and lineage

![Released Mineral sprite, correctly alpha-composited on neutral gray](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mineral-original-preview.png)

Keep the compact, broad silhouette, dusty rose/burgundy armor, charcoal/silver central body, short squared front opening, stepped rear assembly and raised rose sight with red side accents. Do not replace this distinctive palette with a generic gray rock gun just because it is named Mineral.

![Terminator and Rocky Upgrade Kit produce Mineral](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-mineral.webp)

**Terminator + Rocky Upgrade Kit → Mineral** through the bundled Divine Station recipe. This establishes its upgrade relationship, not a particular quarry, creator or dimension of manufacture. [Illustrated upgrade atlas](Divine-Station-Upgrade-Atlas) · [Divine Station walkthrough](Divine-Station-Weapon-Upgrades-1.20.1).

## Proposed premium design

![Mineral concept with original palette, compact side view and optional lattice study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mineral-concept-v1.png)

The concept interprets the rose panels as a mineral-like ceramic with silver framing, red optic accents and restrained grain. That material story is proposed art direction. The lattice shroud is an optional cosmetic study; it does not establish gem projectiles, mining powers or extra damage. The red-dust inspection vignette is also presentation only.

The rear grip sits behind the trigger and the guard is visibly open, but actual character hands, sight alignment, opposite-side construction and attachment/motion clearances still need testing. A painted opening is not a measured hand-fit result. This sheet is neither a UV texture nor a completed native model.

## Complete feature and customization plan

- **Shape/materials:** preserve the squat rose/silver/red identity in original-fit and premium modes; author clean normals, UVs, surface grain and readable small-scale detail.
- **Modules:** compact red sight casing, optional stone-lattice outer shroud and stabilized lower support. A fictional shard-scatter or resonance-beam conversion would require its own declared shot count, resource, damage, timing and server rules; it is not baseline Mineral behavior.
- **Animation:** equip, idle, movement, aim, confirmed fire, deliberate recovery, optional reload, inspection, swaps and interruption recovery with first/third-person hands.
- **Effects:** obtain original flight/impact footage before finalizing selectable projectile, tracer, muzzle, entity/armor/terrain/fluid impact, bounded decal and confirmed-kill finisher treatments.
- **Customization:** earned mineral-themed charms, skins, emblems and static/animated/glowing stickers; configurable impact and death effects without hidden gameplay changes.
- **Progression/salvage:** document every craftable module and conserve eligible customization through Terminator → Mineral, dismantling, salvage and full-inventory returns.
- **Compatibility/performance:** preserve ammunition, slow cadence, attribution and persistence; use cached settings and bounded game-time effects; test multiplayer, TaCZ/turret integrations and equivalent-work performance.

## Acceptance checklist

- [ ] Original native flight, impact, scope, sound and resource evidence
- [ ] Complete alternate-module, inspect, decal and finisher concepts
- [ ] Faithful mesh, two texture modes and actual hand/attachment fit
- [ ] Full animation, native behavior and progression migration
- [ ] Multiplayer, optional compatibility and performance qualification

[Released evidence and exact recipe](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mineral-released-evidence.json) · [Sprite reference QA](Sprite-Transparency-and-Visual-References) · [Weapon overhaul](Weapon-Overhaul)

Original AoA identity and assets are credited to Tslat and contributors. Generated concepts and integration proposals remain separate. No native acceptance is promoted.
