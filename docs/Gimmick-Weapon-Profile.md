# Gimmick: colorful ten-pellet scattergun

**AoA 3.7.1 / Minecraft 1.20.1. Source profile and concept candidate; no native upgrade accepted.**

## What it actually does

Gimmick is a configured BaseShotgun subclass with **ten pellets**, Spreadshot ammunition and a long heavy-shotgun firing sound. Its inspected subclass overrides the firing sound; it does not establish a special random-effect, transformation or living-eye mechanic. The playful inspection idea below is an optional new proposal.

| Released input | Value / boundary |
|---|---|
| ID | `aoa3:gimmick` |
| Base damage input | 4.5; not a guaranteed combined ten-pellet damage total |
| Pellet count | 10 |
| Durability | 800 |
| Fire delay | 68 ticks, nominally 3.4 seconds at 20 TPS |
| Stored recoil | Approximately 1.3; not camera degrees |
| Stored knockback factor | Approximately 0.2; not measured displacement |
| Ammo | Spreadshot inherited from BaseShotgun |
| Firing mode | Non-automatic inherited return |
| Loop-created projectile | LimoniteBulletEntity; age input 4, multiplier 1, piercing 0 |
| Sound override | ITEM_GUN_SHOTGUN_HEAVY_FIRE_LONG |

The inherited spread expression is `0.1 × pelletCount × (1 − 0.15 × FORM level)`. It is not a measured angle or range. The ammo/effects factory and the actual pellet spawn loop are separate paths, so a projectile class name alone cannot establish what is spawned. Final damage, immunity, enchantment interactions and net ammo consumption need native tests.

## Original appearance and unknowns

![Actual released Gimmick sprite, nearest-neighbor enlargement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gimmick-original-preview.png)

The sprite has a broad gold/yellow front, bright green collar/support and rear cap, warm dark brown center, angled lower grip and a distinctive red-orange raised top shape. Those colors and the compact eccentric silhouette are the design anchor. Wood, enamel and a pivoting crest are interpretations rather than official manufacturing lore.

The exact-ID packaged recipe/loot scan found no direct recipe or loot entry in the inspected release. That is an acquisition gap to investigate, not proof the item is unobtainable: trades, code-side rewards and other paths still require checking. No dimension, maker or crafting recipe is invented here.

## Concept candidate

![Gimmick concept with optional expressive inspection and attachment studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gimmick-concept-v1.png)

The gold flared muzzle, green fittings, brown body and red crest remain recognizable. The sheet explores an alternate muzzle collar, green open sight and an optional inspection reveal with a decorative eye. The eye and moving crest must remain clearly identified as new cosmetic/animation ideas. They are not released behavior or established lore.

The shot panel illustrates a ten-pellet concept; artwork is not authoritative projectile-count evidence. The game implementation must count actual authoritative spawns. Comfortable hand placement, support geometry, trigger clearance and source-proportion comparison remain open before final model approval.

## Full feature direction

- **Firing and recovery:** a weighty short flash, ten small readable pellet cues and a satisfying deliberate recovery. Preserve the slow baseline cadence unless an explicit upgrade changes it.
- **Inspect:** crest lifts, a small decorative eye reacts, then the mechanism closes exactly. Keep this optional, interruption-safe and free of orphaned objects or particles.
- **Attachments:** alternate gold shrouds, green sight, ergonomic support, resource-service presentation and explicit spread/converter modules. Changed pellet count, spread, damage and resource values must agree with actual behavior.
- **Reload/service:** optional and coherent with Spreadshot use; no hidden magazine system or ammo duplication.
- **Variants and salvage:** retain the canonical silhouette; new functional variants and transferred effects require their own recipes, conflicts, progression and persistence rules.
- **Customization:** both Minecraft-fit and concept-faithful textures, earned charms, skins, stickers/emblems and separate projectile/trail/impact/decal/finisher channels.
- **All animation states:** equip, idle, movement, aim, fire, recovery, inspect and applicable service transitions with actual player hands and moving-part clearance.
- **Performance:** ten source pellets already increase per-shot work relative to a two-pellet shotgun. Budget trails and impacts per valid event; do not multiply effects by render pass, eye or client. Measure equivalent workloads.

## Acceptance work

- [ ] Find and verify the actual exact-version acquisition route.
- [ ] Capture original fire, flight, impact, resources, cadence and enchantments.
- [ ] Confirm ten authoritative spawns and proper hit/immunity behavior in-game.
- [ ] Refine silhouette, model, textures, real hand fit and all animation clearances.
- [ ] Integrate native geometry/materials, multiplayer, progression, save/load and optional mods.
- [ ] Measure frame/startup costs and effect cleanup under sustained fire.

[Source receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/gimmick-source-evidence.json) · [Complete weapon requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).

Original AoA identity and assets: Tslat and contributors. New concept generated with the built-in image tool. Final art and native acceptance remain open.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
