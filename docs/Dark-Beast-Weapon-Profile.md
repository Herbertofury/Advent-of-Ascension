# Dark Beast: compact dark armor and heavy sniper cadence

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Original role

Dark Beast inherits **BaseSniper**, using Metal Slug ammunition and non-automatic firing. Its subclass selects the heavy-sniper/long firing sound and **SCOPE_3** overlay. It declares no unique impact effect. Its name and dark palette do not establish blindness, shadow damage, life steal or an explosive attack.

| Constructor input | Monster | Dark Beast |
|---|---:|---:|
| Damage | 38 | 50.5 |
| Durability | 250 | 560 |
| Delay | 96 ticks | 96 ticks |
| Stored recoil constructor input | Approximately 0.05 | Approximately 0.035 |

These are stored values, not guaranteed final damage or measured recoil. The nominal delay is 4.8 seconds at 20 TPS. The checked upgrade keeps that input cadence while increasing damage/durability and lowering recoil input.

## Original silhouette and material identity

![Actual released Dark Beast inventory sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dark-beast-original-preview.png)

Retain the dense charcoal/black body, substantial angular lower grip, distinctive open forked front, squared rear and raised sight with its small red accent. The sprite is dark; readability should come from controlled surface separation and restrained rim highlights rather than turning the entire weapon into a glowing red object. Obsidian-like surface treatments in the concept are artistic proposals, not confirmed construction lore.

## Divine Station upgrade

![Released Monster and Darkly Upgrade Kit sprites produce Dark Beast; documentation diagram, not a game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dark-beast-upgrade-board.webp)

Put **Monster** in the left input and a **Darkly Upgrade Kit** in the middle; the output is **Dark Beast**. This is the exact bundled `data/aoa3/recipes/upgrade_kit_dark_beast.json` recipe.

The recipe establishes an upgrade relationship. It does not prove that arbitrary third-party attachment data, custom names or enchantments will be copied. Test the original behavior on disposable items, then define explicit preservation/return rules for our customization system.

[Illustrated Divine Station workflow](Divine-Station-Weapon-Upgrades-1.20.1) · [Exact recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=upgrade_kit_dark_beast)

## Revised concept and retained history

![Revised compact Dark Beast hero, material modes, effect proposals and inspection poses](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dark-beast-concept-v3.png)

The third revision restores the original open forked jaw while keeping a compact front. The second revision had closed too much of that defining negative space. It keeps the dark layered body and red optic accent; two visible arms do not imply two gameplay projectiles. Muzzle, tracer and stone-chip panels are proposed cosmetics; the original Metal Slug behavior is not replaced by a magic beam merely because the art uses a red highlight.

[Preserved first exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dark-beast-concept-v1.png): its exaggerated front proportions were not chosen as the canonical target. [Second exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dark-beast-concept-v2.png) shortened the front but lost the original open jaw, which the third revision restores. Retaining it is not acceptance. The revision still needs real model, rigged-hand and silhouette comparison at gameplay distance.

The two material examples are design directions, not finished atlases. Inspection poses are painted storyboards, not executed animation. A textured surface alone does not prove normal-map quality, UV coverage or mip stability.

## Full feature plan

- **Materials and shape:** original-fit and premium modes, consistent silhouette, controlled specular contrast, clean UV seams and no missing micro-surfaces. Keep both modes readable in dark dimensions.
- **Handling and optics:** preserve heavy sniper cadence and SCOPE_3; optional compact/steady configurations need explicit handling tradeoffs and native aim alignment.
- **Barrel concepts:** short armored shroud, quieter cosmetic treatment and focused fantasy conversion. Any functional changes require separate visible design, ammunition/resource rules and balance tests.
- **Animation:** equip, idle, aim, fire, recovery, optional reload, inspection and modification in first/third person. Include interruption, item swaps and hand clearance throughout motion.
- **Resources:** baseline Metal Slug behavior; optional reload only for a deliberately selected conversion. Inspection cannot consume ammo, add projectiles or change cooldown.
- **Effects:** capture original flight/impact/muzzle/sound, then compare optional tracers, muzzle flashes, decals, impact presets and confirmed-kill finishers. Keep gameplay and cosmetic events separate.
- **Customization:** skins, earned functional charms, static/animated/glowing stickers and emblems; prevent ornaments clipping into hands or obscuring the optic.
- **Dismantling and upgrades:** explicitly preserve or return transferable special effects and attachments; test full inventories, save/reload and interrupted operations.
- **Integration and performance:** native TaCZ export, multiplayer authority, compatibility adapters, cached configurations, texture budgets, reduced-effects mode and measured frame-time lows.

## Acceptance gates

- [ ] Original native scope, projectile, impact, sound and resource captures
- [ ] Complete identity-specific attachments, decals, effects and finisher concepts
- [ ] Faithful model proportions, rigged-hand clearance and two finished material modes
- [ ] Full animation/interruption and Darkly upgrade customization-transfer tests
- [ ] Native gameplay, export, multiplayer, persistence and performance qualification

[Released source and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/dark-beast-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
