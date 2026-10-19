# Head Hunter · chestnut body, cobalt optic and precision rhythm

**AoA 3.7.1 / Minecraft 1.20.1 · source-checked behavior and partial concept. No native or final-art acceptance.**

## What this weapon actually does

Head Hunter is a **Metal Slug sniper** using the inherited **SCOPE_1** overlay. Its special impact hook detects a vertical band around a living target’s eye height. A qualifying server-side impact emits feedback and can set the player’s weapon cooldown to half the firing delay. **This particular hook does not add a headshot damage multiplier.** Damage, armor, enchantments and other systems still require their own checks.

| Released input | Value |
|---|---:|
| Damage input | 41.5 |
| Durability | 380 |
| Firing delay | 92 ticks; nominally 4.6 seconds at 20 TPS |
| Recoil modifier | Approximately 0.035 |
| Ammunition | Metal Slug |
| Scope | SCOPE_1, inherited |
| Firing sound | Medium sniper, long variant |
| Qualifying-hit base cooldown example | 46 ticks from impact, subject to the conditions below |

[Named implementation](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/HeadHunter.java) · [Released-class hashes and extracted inputs](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/head-hunter-released-evidence.json).

### Exact hit conditions matter

The lower boundary is `boundingBox.minY + eyeHeight − bbHeight × 0.105f`; the upper boundary adds `bbHeight × 0.225f`. The impact’s Y coordinate must be **strictly between** those boundaries. Equality at either edge fails. This is a height-band approximation, not a skeletal head mesh, facing test or general critical-hit system. Unusual modded body proportions need explicit testing.

The target must be a living entity in a server level and the impact position must exist. The hook requests five particle packets with three damage-indicator particles each, scattered around the impact, then plays an experience-orb pickup sound at the shooter’s position at volume 1 and pitch 1.5. Original in-game appearance remains uncaptured.

Only after that feedback does it check whether the shooter still holds this **item type** in either hand. A player who does receives `int(getFiringDelay() / 2f)` cooldown ticks. It is not a persistent doubled-fire-rate buff, and it is not subtraction from whatever cooldown remained. At the baseline delay the assignment is 46 ticks; a late-arriving projectile may therefore behave differently from an immediate hit. Weapon swapping, offhand use, multiple impacts and delayed impacts belong in native regression tests.

## Original identity and acquisition

![Released Head Hunter sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/head-hunter-original-preview.png)

Preserve the long warm brown body and descending rear stock, dark central shapes, gray raised optic and small vivid blue lens. The sprite’s material is not proof of a particular wood species, maker or origin dimension.

The inspected release’s data JSON contains the item as the **Skeet advancement icon**, but no direct Head Hunter recipe or loot-table item reference was found. An advancement icon is not a reward. Acquisition through code, trades, other versions or historical content remains unresolved; this page does not invent a recipe or claim the weapon is unobtainable.

## Premium visual study

![Head Hunter concept, warm panels and blue optic](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/head-hunter-concept-v1.png)

The concept interprets the brown sections as layered warm panels with graphite framing and a cobalt optic accent. It is an artistic proposal, not established lore. The illustrated receiver-to-stock grip still needs a hand blockout, opposite-side inspection and trigger-clearance testing before becoming a model target. The blue optic treatment is cosmetic; the original scope overlay is documented separately. Do not treat this sheet as final quality acceptance.

## Full feature and customization plan

- **Two presentation modes:** Minecraft-fit texture language and premium concept-directed materials, sharing the recognizable original silhouette.
- **Modules:** optic shells, shroud profiles, stock and grip alternatives, handling modifiers, earned charms and visibly seated fasteners. Confirmed gameplay bonuses must be listed separately from visual changes.
- **Precision feedback:** a restrained blue optic pulse and short sound response only after the server confirms the qualifying hit. Avoid implying a kill, damage multiplier or permanent fire-rate bonus.
- **Conversions:** an optional fantasy pulse/beam module needs separate ammunition, cost, cooldown and damage rules. It must not silently replace Metal Slug behavior.
- **Animations:** equip, idle, aim, fire, recovery, locomotion, optional reload and inspect; interruption-safe state recovery and left/right hand clearance.
- **Effects:** baseline projectile flight/impact capture, proposed muzzle flash and tracers, material-aware impacts, expiring decals, reduced-effects mode and confirmed-kill-only finishers.
- **Crafting and salvage:** explicitly new attachment recipes, reversible variants, effect transfer, named builds, migration and resource conservation. Keep unresolved original acquisition clearly labeled.
- **Personalization:** skins, stickers, animated/glowing emblems, earned charms and selectable projectile/impact presentation with compatibility and visual-budget controls.

## Acceptance gates

- [ ] Capture original native scope, projectile, impact and qualifying-hit feedback
- [ ] Test strict band edges, modded body sizes, offhand, swaps and late projectile arrivals
- [ ] Establish version-specific original acquisition without inventing recipes
- [ ] Complete variant, attachment, inspection and effects concept sheets
- [ ] Model and texture both presentation modes; validate hands and every moving pose
- [ ] Qualify TaCZ, multiplayer, turret behavior, save migration and performance

[Weapon overhaul](Weapon-Overhaul) · [Completeness standard](Weapon-Completeness-Standard)

Original AoA identity/assets: Tslat and contributors. Proposed visuals and mechanics remain distinct from released behavior.
