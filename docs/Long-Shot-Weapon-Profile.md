# Long Shot: extended-range scatter

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · no accepted native upgrade.**

## What makes this shotgun different

Long Shot fires **two Limonite bullet entities using Spreadshot ammunition**. Its released tooltip says it has longer range than other shotguns, and its overridden firing loop provides concrete implementation evidence: it passes **6** to the bullet lifespan constructor input, while the inspected ordinary `BaseShotgun` loop passes **4**. `BaseBullet` assigns that integer to its `lifespan` field.

This is a longer-lived projectile path, not proof of a particular measured range in blocks or a guaranteed 50% increase in hit distance. Collision, motion, tick handling and other effects still matter. Preserve the subclass's firing path instead of replacing it with a generic shotgun loop just because both use the same pellet entity.

| Released field | Value / interpretation |
|---|---|
| ID | `aoa3:long_shot` |
| Stored damage input | 15.5; not guaranteed final damage |
| Pellets | 2 |
| Durability | 730 |
| Delay | 54 ticks, nominally 2.7 seconds at 20 TPS |
| Recoil input | Approximately 0.3; not camera degrees |
| Knockback input | Approximately 0.2; not a measured distance |
| Ammunition / mode | Spreadshot / non-automatic |
| Distinct firing implementation | Bullet lifespan input 6; per-axis `randomValueBetween(-0.5, 0.5)` offsets multiplied by spread factor |

The ordinary shotgun loop uses a different random-helper call. Preserve and test the Long Shot implementation; this observation alone is not a declaration that either spread pattern is a bug. Two pellets also do not guarantee 31 damage to a target under shared hit/immunity rules.

## Original appearance and recipe associations

![Actual released Long Shot sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/long-shot-original-preview.png)

Keep the elongated silver-gray upper barrel, raised pale forward sight, dark central structure, small cobalt lower fore-end and blue rear/grip. It remains a shotgun, not a sniper merely because its name mentions distance.

Power Core and Small Blue Petal are verified infusion ingredients. A petal-shaped decorative medallion and restrained blue light are new art interpretations. The recipe does not establish a living flower mechanism, a specific maker or an invented home dimension.

## Released infusion route

Put a **Shotgun Frame** in the separate Infusion Table base slot. Use six middle slots for:

- Power Core ×1
- Small Blue Petal ×1
- Three iron-ingot-tag ingredients, **one in each of three separate slots**
- One ingredient matching `forge:gunpowder`

Leave the remaining three ingredient slots empty. A single stack of three iron does not replace the three ingredient entries. Loaded modpack tags and recipe overrides can change accepted items.

Exact definition: `data/aoa3/recipes/infusion_long_shot.json`. Its omitted level/XP fields use the checked ordinary factory defaults, level 1 and XP 0–0; do not advertise it as an XP-training recipe.

[Illustrated 1.20.1 infusion workflow](Infusion-Table-Crafting-1.20.1) · [Released recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=long_shot)

## Concept and proposed effect language

![Long Shot premium hero, side silhouette, optional optic and fore-end details, and proposed blue effect palette](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/long-shot-concept-v1.png)

The art explores polished gray metal, cobalt trim and a restrained petal motif, with optional low-profile sight and fore-end treatments. The effect panel is **proposed cosmetic artwork**, not original projectile footage or proof of water/ice damage. A brighter trail must not change server hit rules. Actual hand fit, consistent model proportions and a Minecraft-fit texture treatment remain open.

This sheet covers hero, silhouette, some external details and an effect palette. It does not complete the full attachment, muzzle, impact, finisher or animation storyboard requirements.

## Complete upgrade plan

| Feature | Design direction and acceptance condition |
|---|---|
| Range identity | Retain the longer-lived two-pellet source mode; measure range and hit behavior in the exact game build before publishing distances. |
| Barrel variants | Precision-focused shroud, compact handling conversion and separately balanced fantasy petal-trail conversion. A physical appearance change must match declared spread, lifetime and handling effects. |
| Handling / optics | Low-profile optic, adjustable fore-end and rear support options; no obstructed sight line or cramped finger opening. |
| Firing feedback | Clear paired-shot feedback, readable recoil/recovery and bounded muzzle flash. Keep released delay separate from animation duration. |
| Projectiles / impacts | Capture original in-flight and contact visuals first; optional blue traces and petal-like dust are cosmetic until a functional conversion is explicitly specified. |
| Inspect / animations | Equip, aim, fire, optional reload, inspect and interruption in first/third person. Proposed medallion-light inspection must not consume or grant ammunition. |
| Reload | Optional for the original resource behavior; only use a physical magazine/charge cycle for a conversion that defines one. |
| Charms / skins / decals | Earned bonuses, original-fit and premium materials, stickers, animated/glowing emblems, independently selected tracer/impact/finisher effects. Place charms outside the grip and controls. |
| Finishers | Optional cosmetic confirmed-kill effects preserving loot, credit and multiplayer state; no hidden area damage. |
| Crafting / effect transfer | Retain the released infusion route; explicit new recipes, reversible cosmetic changes and item-conserving dismantling. |
| Performance | Cached attachment configuration, no repeated idle scans, bounded effects/LODs and measured dense-scene frame-time lows. |

## Open acceptance work

- [ ] Native range, spread, resource and two-pellet comparison against the released subclass
- [ ] Original projectile, impact and audio captures
- [ ] Complete attachment/muzzle/impact/finisher concepts and both material treatments
- [ ] Real hand fit, full animation/attachment collision sweeps and interruption tests
- [ ] Native export, multiplayer, persistence, dismantling and performance evidence

[Source receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/long-shot-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
