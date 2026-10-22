# Monster: amber fork-jaw sniper

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Current selected concept · 22 October 2026

![Monster selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/monster-dragon-mouth-concept-v2.png)

Amber/black dragon-mouth study preserves the open forked jaw silhouette with a visible barrel between the teeth and amber upper eye motif. Exact jaw proportions, native hand fit and sight alignment remain open. Earlier concept is preserved.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Amonster). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

## Original role

Monster inherits **BaseSniper**, using Metal Slug ammunition and non-automatic firing. Its subclass selects the heavy-sniper/long firing sound and **SCOPE_2** overlay. It does not declare a custom impact effect. Orange armor and an open jaw do not establish fire damage, a bite attack or two gameplay projectiles.

| Stored input | Monster | Dark Beast upgrade |
|---|---:|---:|
| Damage | 38 | 50.5 |
| Durability | 250 | 560 |
| Delay | 96 ticks | 96 ticks |
| Stored recoil constructor input | Approximately 0.05 | Approximately 0.035 |

At 20 TPS the nominal delay is 4.8 seconds. These are constructor inputs, not guaranteed final damage, physical recoil measurements or native benchmark results.

## Original identity

![Actual released Monster sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/monster-original-preview.png)

Preserve the bright orange/amber upper shell and forked jaw, charcoal lower rear and grip, squared stock and raised orange/black sight. The open negative space at the front is a defining shape. A richer lacquered or worn-metal finish is an artistic interpretation, not a confirmed account of its manufacture.

## Acquisition and version boundaries

The inspected 1.20.1 / AoA 3.7.1 bundled data references Monster as the **input** to the Dark Beast upgrade. That does not provide a current recipe or drop that grants Monster itself; the current survival acquisition route remains unresolved here. Code-side, datapack and modpack sources require separate investigation.

The independently inspected 1.12.2 / AoA 3.3.6 evidence lists Monster in **Graw's** loot table, `aoa3:entities/bosses/graw`, at `/pools/2/entries/2`, with **weight 16**. That is historical evidence and a relative weight, not a current drop claim or 16% chance. Do not infer a modern crafting recipe or weapon-maker story from it.

[Historical acquisition evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-acquisition-evidence-1.12.2.json)

## Upgrade to Dark Beast

![Monster plus Darkly Upgrade Kit produces Dark Beast; released-sprite documentation diagram](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-dark_beast.webp)

At the **Divine Station**, put Monster in the left input and a Darkly Upgrade Kit in the middle. The exact bundled `upgrade_kit_dark_beast.json` result is [Dark Beast](Dark-Beast-Weapon-Profile). The checked input cadence stays the same while damage/durability increase and recoil input decreases.

Do not assume arbitrary custom item data survives the original recipe. Define preservation or return rules for attachments, names, charms and transferable special effects, and test full-inventory cases.

[Station tutorial](Divine-Station-Weapon-Upgrades-1.20.1) · [All Darkly upgrades, pictured](Divine-Upgrades-Darkly) · [All 70 upgrade recipes](Divine-Station-Upgrade-Atlas)

## Earlier preserved art: Premium concept and open design work

![Monster hero, material modes, proposed muzzle/tracer/impact presentation and inspection storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/monster-concept-v1.png)

The sheet retains amber armor, dark lower parts and an open forked jaw. Warm muzzle/tracer colors are proposed cosmetics, not evidence of original fire damage. The painted inspection sequence is not executable animation, and the small material-mode examples are not finished texture atlases.

The jaw tips and optic are visually emphasized; actual model proportions, sight obstruction, guard clearance and supporting-hand placement still require rigged review. Do not turn visible decorative ports into accidental extra resource use or damage.

## Full feature plan

- **Identity and materials:** original-fit and premium modes with the same fork-jaw silhouette, readable orange/dark separation, clean UVs, mip-safe details and controlled highlights.
- **Handling:** preserve baseline sniper cadence. Optional steadier and more mobile configurations need explicit costs and matching visible changes.
- **Attachments:** jaw-armor, optic and fore-end alternatives; a deliberately selected fantasy dual-discharge conversion could animate alternating jaw channels, but must define its extra resource/projectile/damage rules separately from the baseline.
- **Optics:** retain SCOPE_2 as the original option. Alternate sights need measured first-person alignment and clear target visibility.
- **Animation:** equip, idle, aim, confirmed fire, recovery, optional reload, inspection, swaps and interruptions with actual first/third-person hand rigs. Any optional jaw inspection movement needs collision checks and must not trigger firing.
- **Resources:** original Metal Slug behavior, with reloading optional. A selected magazine conversion must have explicit capacity, cancellation and persistence behavior.
- **Effects:** first capture original native projectile flight, muzzle, impact and sound. Then support configurable tracer, muzzle flash, impact, decals and confirmed-kill finisher presets with reduced-effects choices.
- **Customization:** earned functional charms, skins, static/animated/glowing stickers and emblems, all kept clear of hands, moving parts and sight lines.
- **Dismantling and compatibility:** explicit special-effect transfer rules, safe inventory returns, native TaCZ export, multiplayer authority and save/load testing.
- **Performance:** cached configuration and shared resources; no repeated scans or permanent cosmetic ticking. Measure startup, memory and frame-time lows before acceptance.

## Acceptance gates

- [ ] Current acquisition route resolved without importing historical assumptions
- [ ] Original native scope, projectile, impact, sound and resource captures
- [ ] Complete attachments, charms, muzzle/tracer/impact/decal and finisher concepts
- [ ] Faithful rigged model, two finished material modes and full animation/interruption tests
- [ ] Native export, multiplayer, persistence, compatibility and performance qualification

[Released source evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/monster-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](Effective-Recoil-Routing-1.20.1).
