# Amplifier: five-pellet explosive-hit shotgun

**AoA 3.7.1 / Minecraft 1.20.1. Source-backed profile and revised concept proposal. No accepted native upgraded weapon.**

## What it actually does

Amplifier uses Spreadshot ammunition and the shared non-automatic BaseShotgun firing loop, configured for **five LimoniteBulletEntity pellets**. Its own impact-effect hook calls the explosion helper with **strength input 1.0**. That number is not a measured radius or guaranteed blast damage.

The relevant call chain matters: the projectile's entity-hit path calls the weapon's damage method; BaseGun invokes the impact effect after a successful gun/heavy-gun attack. Therefore, five spawned pellets do not guarantee five successful explosions on the same target. Immunity, hit rejection, enchantments and collision order require native tests. The inspected ordinary pellet block-impact hook is empty; the entity-hit effect must not be advertised as “explodes on every block collision.” Shared destructive-weapon physics can still affect eligible blocks through separate code.

| Released input | Value and boundary |
|---|---|
| Registry ID | `aoa3:amplifier` |
| Stored damage | 9; not a guaranteed combined 45-damage hit |
| Pellet count | 5 |
| Durability | 1,100 |
| Delay | 56 ticks, nominally 2.8 seconds at 20 TPS |
| Recoil input | Approximately 0.7; not camera degrees |
| Knockback input | Approximately 0.2; not measured displacement |
| Ammo | Spreadshot |
| Loop-created projectile | LimoniteBulletEntity, age input 4, multiplier 1, piercing 0 |
| Impact-effect helper | WorldUtil.createExplosion with shooter attribution and projectile position, strength 1.0 |
| Sound | Heavy, long shotgun firing selector |

The explosion helper follows environmental rules: its player-attributed path checks destructive-weapon physics, and relevant non-player paths involve the Forge mob-griefing event. Preserve those gates. The art's cyan/gold effects are a proposed visual treatment, not a claim that the source weapon fires sound waves or laser beams.

## Actual original appearance

![Actual released Amplifier sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/amplifier-original-preview.png)

The dark forebody, bright yellow/gold segments, cyan inset details and orange/gold grip heel are the visual anchors. A premium remake should retain them. Materials and the animated indicator sequence are design proposals; no canonical manufacturer or musical-weapon lore is established by the inspected sources.

## Infusion recipe tutorial

This is an **AoA infusion recipe**, not standard shapeless crafting. Its input is a Shotgun Frame, with Enchanted Gunpowder ×1, Shyrestone ingots ×2, iron ingots ×2 and a Shyregem ×1.

| Input: Shotgun Frame | Enchanted Gunpowder ×1 | Shyrestone ingots ×2 | Shyregem ×1 |
|---|---|---|---|
| ![Shotgun Frame](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-shotgun-frame-sprite.png) | ![Enchanted Gunpowder](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-enchanted-gunpowder-sprite.png) | ![Shyrestone ingot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-shyrestone-ingot-sprite.png) | ![Shyregem](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-shyregem-sprite.png) |

**Also required: two ingredients matching `forge:ingots/iron`.** The recipe accepts tags for both ingot kinds and the gem. The pictured Shyrestone and Shyregem items are confirmed members of their packaged tags; other valid tag members may be added by a modpack. Images are actual released textures enlarged with nearest-neighbor sampling. Iron imagery and the native infusion interface walkthrough remain to be captured.

Shyrestone/Shyregem recipe ingredients support a material association, not a complete dimension-origin or official maker claim. Exact survival acquisition and infusion progression must be verified in the selected game build.

## Revised concept proposal

![Amplifier concept with corrected trigger placement and five visible pellet tips](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/amplifier-concept-v2.png)

The first concept placed the trigger too far from the grip and showed four visible pellet tips despite its five-pellet label. The revised candidate moves the controls beside the grip and shows five separated tips. Those corrections do not constitute real hand-fit or gameplay acceptance. The small pixel-style treatment is another concept interpretation, not the actual original sprite above.

## Full feature and customization plan

- **Firing:** original five-pellet preset, intentional recoil/recovery, bounded muzzle flash and clear audio timing. Separate cosmetic burst presentation from authoritative pellet spawning.
- **Impact:** distinguish successful entity-hit explosions from ordinary block feedback. Preserve environmental protection rules, source attribution and multiplayer authority. Offer lower-intensity visual settings.
- **Inspect:** optional sequential cyan-node illumination, interruptible without duplicate firing, resource changes or persistent stale effects.
- **Modules:** visible protective muzzle shroud, optic, grip/handling pieces and decorative core housing. Alternate spread or pellet-count conversions need explicit new balance and resource rules; appearance and implemented effects must agree.
- **Style modes:** Minecraft/TaCZ-fitting surface treatment and a higher-detail concept-fidelity presentation, with shared gameplay and readable silhouettes.
- **Unlocks:** craftable variants, gameplay-earned charms, skins, static/animated/emissive stickers, custom emblems and configurable projectile/tracer/impact/finisher effects.
- **Animation completeness:** equip, idle, aim, fire, recovery, inspect, all interrupts and optional reload only where the resource configuration supports it.
- **Efficiency:** pooled effects, bounded lifetime, shared materials, LOD and no repeated catalogue scans in runtime presentation. Measure startup and frame time rather than claiming zero cost.

## Acceptance work still required

Original in-game flight, entity and block impact captures; actual explosion count and immunity behavior; resource/enchantment tests; concept-to-mesh fidelity; comfortable normal/slim hands and swept attachment clearance; complete animation and effect implementation; UV/material/export validation; native TaCZ/TML integration; multiplayer, save/load, progression, compatibility and measured performance. All native gates remain untested.

[Exact-release evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/amplifier-source-evidence.json) · [Weapon baselines](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/conventional-weapon-baselines-1.20.1.json) · [Complete feature requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard)
