# Baron SSR: red-brown armor and a deliberate metallic report

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Original role and values

Baron SSR inherits **BaseSniper**, with Metal Slug ammunition and non-automatic firing. Its inspected subclass selects `ITEM_GUN_SNIPER_METALLIC_FIRE_LONG` and the **SCOPE_1** overlay. It does not declare its own impact effect. The baseline does not establish an explosive, elemental or rapid-fire attack.

| Constructor-stored input | Value |
|---|---:|
| Damage | 35 |
| Durability | 240 |
| Delay | 88 ticks |
| Stored recoil constructor input | Approximately 0.05 |

At 20 TPS the nominal delay is 4.4 seconds. These are stored inputs, not measured final damage, physical recoil or native performance. The inherited sniper stance, timing and resource behavior remain part of the implementation contract.

## Preserve the original visual identity

![Actual released Baron SSR inventory texture, enlarged with nearest-neighbor sampling](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baron-ssr-original-preview.png)

The original has a long dark front, red-brown body and rear stock, a substantial gray center, an angular dark grip and a raised dark sight with small warm accents. Preserve those anchors before adding detail. The richer surface finish is a new artistic interpretation; it does not establish an official manufacturer or construction story.

## Acquisition: keep versions separate

The inspected **1.20.1 / AoA 3.7.1** archive has no `baron_ssr` reference in its bundled data JSON files. That is a bounded search result, not proof that the item is unobtainable through all code, datapacks or modpacks. A current survival acquisition route remains unresolved; do not invent an Infusion Table recipe.

The separately inspected **1.12.2 / AoA 3.3.6** acquisition evidence places Baron SSR in `aoa3:entities/bosses/baroness`, at `/pools/2/entries/3`, with **weight 16**. A weight is not a 16% drop chance. This is historical Baroness loot evidence, not proof of the same drop in the current target or a canonical story about who forged it.

[Historical acquisition evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-acquisition-evidence-1.12.2.json) · [Version-aware loot explorer](https://herbertofury.github.io/Advent-of-Ascension/loot-explorer.html)

## Concept sheet

![Baron SSR red-brown hero, material variants, cosmetic effect proposals and inspection storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baron-ssr-concept-v1.png)

The hero develops red-brown panels, charcoal metal and warm optic details. Optional ivory/green finishes, a support bipod, warm tracer presentation and the inspection poses are **proposals**. A glowing optic does not make the original projectile an energy beam. No pictured pose is an implemented animation or hand-clearance test.

The front support and grip/guard geometry need a careful rigged-hand review. The material variants should share recognizable proportions; texturing must remain readable at actual gameplay distance rather than depending on tiny scratches or excessive bloom.

## Full customization and feedback plan

- **Materials:** original-fit and premium texture modes, preserving the red-brown/dark identity; test roughness, emissive exposure and mip readability.
- **Handling:** optional steady support versus mobile handling configurations, with explicit costs and no accidental timing change from presentation.
- **Optics:** retain SCOPE_1 as the original option; upgraded sights need actual first-person aim alignment and obstruction checks.
- **Barrel variants:** restrained long-form, compact silhouette and fantasy-focused conversion concepts. Any functional conversion needs its own damage/resource/visual contract; a cosmetic mesh swap must not silently alter gameplay.
- **Resources:** preserve Metal Slug behavior. Reloading stays optional; a selected magazine conversion must define capacity, cancellation, resource ownership and save behavior.
- **Animations:** equip, idle, aim, confirmed fire, recovery, optional reload, inspection, attachment swaps and interruption, in first and third person. Cosmetic effects cannot consume ammo or grant damage.
- **Effects:** capture original projectile flight, muzzle, impact and sound in-game before comparison. Provide configurable muzzle glint, tracer, impact, decals and optional confirmed-kill finishers, with reduced-effects choices.
- **Personalization:** earned charms with explicit bonuses, skins, static/animated/glowing stickers and emblems. Keep ornaments outside hands, sight lines and moving parts.
- **Dismantling:** preserve or return attachments and transferable special effects under explicit rules, including full inventories and interrupted operations.
- **Compatibility/performance:** test native TaCZ export, multiplayer authority, persistence, optional integrations and measured frame-time lows. Cache configuration; avoid repeated scans and permanent cosmetic polling.

## Acceptance gates

- [ ] Current acquisition route resolved without importing historical assumptions
- [ ] Original native scope, projectile, sound, impact and resource captures
- [ ] Complete attachments, charms, effects and finisher concept set
- [ ] Rigged-hand fit, coherent proportions, full animation/interruption and two material modes
- [ ] Native export, gameplay, multiplayer, persistence and performance qualification

[Released source evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/baron-ssr-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
