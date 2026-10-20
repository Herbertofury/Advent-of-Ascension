# Decimator · cream armor and a precise target rule

**AoA 3.7.1 / Minecraft 1.20.1 · released-source profile and partial concept study. Native and final-art acceptance remain open.**

## What it actually does

Decimator is a **Metal Slug sniper** using **SCOPE_2**. If a living target’s **maximum health is strictly below 50**, its damage hook multiplies the incoming bullet-damage multiplier by **1.15** before calling the inherited damage method.

The condition uses maximum health, not current injury, percentage health or an automatic execution threshold. Exactly 50 does not qualify. A higher-maximum-health target remains outside this rule even when nearly defeated. Actual damage depends on the rest of the game’s damage path and other mods.

| Released input | Value |
|---|---:|
| Damage | 33 |
| Durability | 180 |
| Delay | 95 ticks, nominally 4.75 seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.05 |
| Ammunition | Metal Slug |
| Scope | SCOPE_2 |
| Sound | Heavy sniper, long variant |

These are source inputs, not measured final damage, recoil displacement or effective range. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Decimator.java) · [Pinned released evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/decimator-released-evidence.json).

## Original appearance

![Released Decimator sprite on a neutral alpha-composited background](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/decimator-original-preview.png)

Keep the pale cream/yellow front and rear panels, charcoal-gray core, stepped lower front ledge, short dark muzzle and raised dark optic with a pink-red accent. Do not erase this palette by turning it into a generic black rifle.

## Craft and upgrade

![Decimator infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/decimator-infusion.webp)

Use **Sniper Frame** with Orange Spores, Zhinx Dust, two separate iron-ingot-tag ingredients and a gunpowder-tag ingredient. The center layout is order-independent; tag icons are example members. The ingredients do not by themselves establish a spore-firing mechanic or a manufacturing origin. [Infusion Table guide](Infusion-Table-Crafting-1.20.1).

![Decimator plus Clown Upgrade Kit produces Clownimator](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-clownimator.webp)

**Decimator + Clown Upgrade Kit → Clownimator.** The upgrade changes the listed damage/durability to 49.5/545, uses SCOPE_3 and broadens the conditional maximum-health threshold to below 75. Preserve these differences instead of copying the wrong scope or threshold into a shared adapter.

| Living target’s maximum health | Decimator hook | Clownimator hook |
|---|---|---|
| Below 50 | Multiplies incoming bullet factor by 1.15 | Multiplies incoming bullet factor by 1.15 |
| Exactly 50 through below 75 | No extra factor from this condition | Multiplies incoming bullet factor by 1.15 |
| Exactly 75 or above | No extra factor from this condition | No extra factor from this condition |

This table describes the source branch, not native damage measurements. [Clownimator profile](Clownimator-Weapon-Profile) · [Divine upgrade atlas](Divine-Station-Upgrade-Atlas).

## Proposed premium treatment

![Decimator cream-ceramic and gray-metal concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/decimator-concept-v1.png)

The cream ceramic, brushed framing and small optic-inspection light are proposed art choices. The silhouette and palette remain recognizable, with a single rear grip behind the trigger and a smooth open guard in both main views. Actual hand fit, opposite-side construction, aiming alignment, proportions and motion still require model/native review; this painted opening is not a clearance certificate.

## Full feature plan

- **Presentation:** Minecraft-fit and premium texture modes; purposeful ceramic/metal detail, clean UVs/normals, bounded glow and distance readability.
- **Modules:** optic housings, cream-panel finishes, shroud options and earned skins; functional conversions need explicit resource, damage and cadence rules.
- **Animation:** equip, idle, locomotion, aim, confirmed fire, recovery, optional reload, inspect and interruption behavior with actual hands.
- **Feedback:** original/new flight and impact captures, selectable muzzle/tracer/projectile/surface impacts, expiring decals and confirmed-kill finishers. Do not infer spore bullets from the recipe.
- **Customization/progression:** earned charms with declared bonuses where applicable, stickers including animated/glowing options, emblems, module recipes, salvage and upgrade/save conservation.
- **Qualification:** multiplayer authority, maximum-health boundary cases, modded attributes, original fallback, TaCZ/turret integration, measured startup/memory/frame-time and reduced-motion options.

## Acceptance gates

- [ ] Original native flight, impact, scope, sound and resource evidence
- [ ] Maximum-health boundaries and modded-attribute regression cases
- [ ] Complete module, inspection, effect and finisher concepts
- [ ] Faithful model, both texture modes and actual hand/attachment clearance
- [ ] Full native animation, migration, multiplayer and compatibility tests
- [ ] Equivalent-scene performance and accessibility checks

[Armory](Weapon-Overhaul) · [Weapon completeness standard](Weapon-Completeness-Standard)

Original identity/assets belong to Tslat and contributors. New art and implementation proposals remain separate from released mechanics.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
