# Moon Maker · magenta sniper with pink sparklers

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## What makes the original different

Moon Maker is a Metal Slug **BaseSniper** weapon. Unlike its Mark Maker predecessor, it overrides projectile creation with **MoonMakerEntity** and selects **SCOPE_2**. The firing sound remains the medium-rifle/long report.

| Stored input | Mark Maker | Moon Maker |
|---|---:|---:|
| Damage | 36.5 | 38.5 |
| Durability | 530 | 570 |
| Delay | 70 ticks | 70 ticks |
| Stored recoil constructor input | Approximately 0.05 | Approximately 0.05 |
| Scope | SCOPE_4 | SCOPE_2 |

These are constructor inputs, not guaranteed final damage or measured recoil. At 20 TPS, the nominal input delay is 3.5 seconds.

MoonMakerEntity passes damage multiplier 1, pierce-count input 0 and launch-speed parameter 20 to the inspected BaseBullet constructor, which stores lifespan 60. Do not turn those parameters into an unmeasured effective range. The projectile subclass declares no custom entity/block impact override.

## Original appearance and upgrade lineage

![Released Moon Maker sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moon-maker-original-preview.png)

Keep the magenta/purple body, charcoal front and grip, silver/white bands, hooked forward underbody and bright green optic accent. The name alone is not evidence that the original is silver, fires moons or causes explosions. Its documented recipe lineage establishes an upgrade relationship, not an invented maker or manufacturing location.

![Mark Maker and Lunar Upgrade Kit produce Moon Maker](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-moon_maker.webp)

**Mark Maker + Lunar Upgrade Kit → Moon Maker**, using the bundled Divine Station upgrade-kit recipe. [Mark Maker profile](Mark-Maker-Weapon-Profile) · [KA-500 prerequisite](KA-500-Weapon-Profile) · [Lunar upgrades](Divine-Upgrades-Lunar) · [Station walkthrough](Divine-Station-Weapon-Upgrades-1.20.1).

## Actual extracted projectile asset versus new concept

![Original Metal Slug projectile texture, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moon-maker-projectile-preview.png)

This is the actual 16×16 released texture bound to MoonMakerRenderer, enlarged for inspection. It is not a frame captured in flight. The renderer first invokes TexturedProjectileRenderer and then loops **eight times per render invocation**, creating SPARKLER particles with RGB **255, 105, 180**, scale input **1** and age-modifier input **3**. The age modifier is not a fixed three-tick lifetime.

The render-driven spawning is an important optimization review target: do not copy particle creation into every camera/render pass in the upgrade. A game-time presentation clock and explicit budget need native density/performance comparison before replacement.

## Two integration cautions worth testing

1. **Offhand attribution:** the override receives an InteractionHand, but calls a constructor that stores MAIN_HAND. This is a source-backed regression-test target. It is not proof that offhand play is broken in every runtime context.
2. **Render-rate-dependent effects:** more renderer invocations can schedule more particles. Exact observed density and cost require native captures; the source loop is not an FPS benchmark.

## Proposed premium design

![Moon Maker concept and cosmetic proposals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moon-maker-concept-v1.png)

The concept preserves magenta and green rather than replacing the weapon with a generic moon-colored rifle. A crescent charm and orbiting inspection sparks are cosmetic proposals. The illustrated projectile is an artistic interpretation at enlarged display scale, not the original texture, physical dimensions or new ammunition rules. The crescent impact symbol is optional feedback, not a baseline terrain-breaking effect.

The forward hook, large optic and grip require further first-person proportion and clearance checks. This sheet is a partial exploration; its painted material finish is not a completed UV set or native model.

## Full feature plan

- **Shape/textures:** original anchors, restrained crescent detailing, clean UVs, game-distance readability, correct normals and both original-fit/premium material modes.
- **Aim/handling:** native SCOPE_2, aligned sight line, comfortable hand clearance and offhand regression coverage.
- **Attachments:** compact lunar shroud, steadier support fore-end and an explicitly designed fantasy split-shot conversion. Any changed trajectory, count, damage or cost needs declared server-side rules.
- **Animation:** equip, idle, aim, confirmed fire, recovery, optional reload, inspection, swapping and interruptions with first/third-person hands.
- **Feedback:** preserve baseline comparison footage; selectable muzzle, pink tracer, entity/armor/terrain/fluid impact, decal and confirmed-kill finisher channels.
- **Personalization:** earned charms, finishes, emblems and static/animated/glowing stickers with safe placement.
- **Persistence:** effect salvage, dismantling, full-inventory returns and customization transfer across KA-500 → Mark Maker → Moon Maker.
- **Performance/compatibility:** game-time emissions, bounded cosmetic retention, cached configuration and no repeated scans; native TaCZ, multiplayer, optional adapters and equivalent-work measurements.

## Acceptance gates

- [ ] Original native projectile, impact, scope, sound and resource footage
- [ ] Offhand attribution and multi-camera/render-rate regression tests
- [ ] Complete alternate-module, finisher, impact and decal concepts
- [ ] Faithful mesh, two texture modes and full animation/hand-fit qualification
- [ ] Native gameplay, networking, save migration, compatibility and performance acceptance

[Released-file evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/moon-maker-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
