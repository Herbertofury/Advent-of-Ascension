# Vivo: compact gold-and-charcoal scattergun

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · no accepted native upgrade.**

## What the original does

Vivo fires **three Spreadshot pellets** through the inherited `BaseShotgun` behavior. Its inspected subclass only changes the firing-sound pitch adjustment to **1.3**. The name does not establish life steal, healing, magnetized targets or any other special hit effect.

| Released field | Value and interpretation |
|---|---|
| Registry ID | `aoa3:vivo` |
| Stored damage input | 7.0; not guaranteed final damage |
| Pellets | 3 ordinary `LimoniteBulletEntity` pellets in the inherited firing loop |
| Durability | 710 |
| Delay | 36 ticks, nominally 1.8 seconds at 20 TPS |
| Recoil input | Approximately 0.8; not camera degrees |
| Knockback input | Approximately 0.3; not a measured distance |
| Ammunition / fire mode | Spreadshot / non-automatic |
| Inspected subclass override | Firing-sound pitch adjustment returns 1.3 |

Three pellets do not guarantee 21 total damage to one target. Accuracy, immunity and the shared damage/enchantment rules still matter. Original projectile flight, impacts and audio must be captured in the game before a replacement is accepted.

## Original appearance and provenance

![Actual released Vivo sprite enlarged with nearest-neighbor sampling](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/vivo-original-preview.png)

Retain the compact dark body, broad forward muzzle, paired gold upper accents, gray bridge and descending rear grip with its gold marking. The source sprite is the identity anchor; details hidden by a small sprite remain design decisions rather than established mechanical facts.

The packaged infusion recipe associates Vivo with a **Magnet Shard and Lyon ingots**. A magnetic-industrial material language is a reasonable new design interpretation. It is not proof of a named maker, home dimension, life-draining ability or literal electromagnetic operating mechanism. More narrative provenance remains open.

## Crafting in the checked release

Use a **Shotgun Frame** in the separate base slot of an Infusion Table, then put these four entries in four middle slots:

- Magnet Shard ×1
- One `forge:ingots/lyon` ingredient in each of **two separate slots**
- One `forge:ingots/iron` ingredient

Leave the remaining five middle slots empty. Two Lyon items stacked in one slot do not replace the two required occupied slots. Pack data can change tag membership and recipe definitions.

The exact packaged recipe is `data/aoa3/recipes/infusion_vivo.json`. It omits explicit infusion-level and XP fields; the checked ordinary recipe factory defaults those to level 1 and XP 0–0. That is not a claim of an XP-farming method.

[Illustrated 1.20.1 Infusion Table walkthrough](Infusion-Table-Crafting-1.20.1) · [Recipe Observatory: Vivo](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=vivo)

## Premium visual concept

![Vivo hero, side silhouette, gold material detail and cosmetic shard charm proposal](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/vivo-concept-v1.png)

The sheet develops a blued-charcoal shell, paired warm gold caps, recessed detailing and a compact stance. The shard charm is an optional proposal. Its position must avoid the grip, trigger, attachments and camera throughout every animation.

This is **partial concept coverage**, not a finished model. The pictured controls and trigger opening still require actual player-hand fitting; the surface wear may need restraint for the Minecraft-fit treatment. The hero, side and material panels are useful art references, not proof of dimensional consistency. Original-style and premium treatments must share the same functional attachment sockets and behavior.

## Complete upgrade plan

| Area | Proposed work and acceptance requirement |
|---|---|
| Firing and recoil | Preserve the original three-pellet mode and higher-pitched identity. Build a crisp shot response and recoverable recoil; do not silently replace the 36-tick baseline with automatic fire. |
| Optional reload | Keep original resource behavior available. Physical magazine or charge-swap animations only belong to conversions that explicitly introduce those mechanics. |
| Alternate barrels | Compact scatter shroud; precision choke conversion; gold-coil fantasy conversion with declared new costs/effects. Changes to spread, damage or projectile type need explicit balance and visible correspondence. |
| Handling and sights | Comfortable grip variants, low-profile optic and stable stock/support options. Check actual finger clearance and unobstructed aim; do not solve collisions by shrinking hands or controls. |
| Projectile / tracer | Capture the original first. Optional warm-gold traces remain separate from authoritative pellet collision; avoid permanent expensive dynamic lights. |
| Muzzle / impact | Short readable flash, material-specific contact cues and bounded debris. No implied explosion or magnet pull in original mode. |
| Finishers / death effects | Optional cosmetic aftermath tied to confirmed kills, preserving loot, kill credit, networking and reduced-effects settings. |
| Inspect and animation | Equip, aim, fire, optional reload, inspect, interruption and first/third-person transitions. A restrained gold-cap shimmer is a proposal, not an extra shot or free resource. |
| Charms / skins / decals | Earned charm upgrades, original-fit and premium skins, stickers, animated/emissive emblems, tracer/impact/finisher selections. Cap effects and preserve saved customization. |
| Craftables / variants | Preserve the released infusion route. New attachments, material variants and effect transfers need clear recipes, lossless dismantling rules and duplication tests. |
| Performance / compatibility | Cached configuration, no idle repeated scanning, bounded effects, suitable LODs and exact-version TaCZ/native testing. Measure frame-time lows, not just average FPS. |

## Open quality gates

- [ ] Original flight/impact/audio capture and native three-pellet/resource tests
- [ ] Projectile, muzzle, impact, death-effect and alternate-barrel concept boards
- [ ] Consistent side/front/rear model proportions and comfortable player-hand fit
- [ ] Full animation sweeps, charm/attachment collision checks and cancellation behavior
- [ ] Native export/materials, multiplayer, persistence, dismantling and performance evidence

[Source receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/vivo-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
