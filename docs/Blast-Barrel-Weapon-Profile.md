# Blast Barrel: heavy explosive-hit scatter

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · no accepted native upgrade.**

## Original behavior

Blast Barrel is a **three-pellet Spreadshot shotgun**. Its subclass selects the heavy-long firing sound and calls the shared explosion helper with strength input **2.0** from its weapon impact-effect hook.

That hook belongs to the shared successful-damage path. Do not interpret it as a guaranteed explosion on every visual collision or every block contact. The ordinary Limonite projectile and shared environmental/physics rules still apply. Helper strength is not a measured damage total or an independently verified blast radius.

| Released field | Value / boundary |
|---|---|
| ID | `aoa3:blast_barrel` |
| Stored damage input | 13.0; not guaranteed final damage |
| Pellet count | 3 |
| Durability | 740 |
| Delay | 62 ticks, nominally 3.1 seconds at 20 TPS |
| Recoil input | Approximately 0.4; not camera degrees |
| Knockback input | Approximately 0.4; not a measured distance |
| Ammunition / fire mode | Spreadshot / non-automatic |
| Projectile loop | Inherited `BaseShotgun` / `LimoniteBulletEntity` |
| Unique subclass behavior | Heavy-long sound selector; explosion-helper strength 2.0 in impact-effect hook |

The three pellets are not a promise of 39 direct damage plus three identical blasts. Hit success, immunity and shared damage/environmental rules must be tested in the exact build. **Blast Barrel and Blast Cannon are different weapons**; the latter's acquisition or sticky-bomb behavior must not be copied here.

## Original appearance

![Released Blast Barrel sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/blast-barrel-original-preview.png)

Preserve the broad dark-brown front, charcoal central braces, warm amber lower-front accents and short descending brown rear grip. The small source sprite leaves some geometry ambiguous; the paired shrouds in the concept are an interpretation, not evidence of two independently scheduled shots.

## Acquisition and historical identity

### First target: 1.20.1 / 3.7.1

The checked release registers Blast Barrel and includes its creative-tab reference. The exact-item scan found **no packaged recipe, loot or trade JSON reference** for it. This does not prove every possible runtime/modpack acquisition route is absent, but it is not enough to publish a survival obtaining recipe or current dungeon drop.

### Historical: 1.12.2 / 3.3.6

The historical source-derived acquisition index records Blast Barrel in `aoa3:structures/dawnlightdungeon/general`, at `/pools/0/entries/11`, with weight 2 and quality 2. These fields are not a standalone percentage chance.

That gives the redesign a real **historical Dawnlight Dungeon association** to preserve. The concept's sunburst engraving is new art inspired by that association; it is not proof of a named maker or manufacturing story. Do not silently carry the old loot route into 1.20.1.

[Historical acquisition evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-acquisition-evidence-1.12.2.json) · [Current source receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/blast-barrel-source-evidence.json)

## Concept: dark bronze, amber and weight

![Blast Barrel refined concept with readable controls, side silhouette, optional trim and proposed impact palette](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/blast-barrel-concept-v2.png)

The first draft failed visual review because it lacked a clearly readable trigger/control opening. This revision provides visible clearance and reduces the amber insets' brightness. Actual model/hand fit remains untested; a painted opening is not a 3D collision result.

The effect palette is a proposed amber treatment. It is not a screenshot of the original projectile or explosion. The broad shroud, amber windows and leather-like grip should read as a deliberate fantasy artifact in both Minecraft-fit and premium materials, without permanent expensive scene lighting.

This sheet is partial coverage: hero, side silhouette, optional trim and an impact palette. Detailed projectile/muzzle/finisher boards, full attachment variants and complete animation storyboards remain open.

## Full feature plan

- **Original firing mode:** preserve three pellets, resource rules, heavy-long sound identity and the checked impact hook. Keep presentation timing separate from the released delay.
- **Barrels and handling:** compact heavy shroud, stabilized precision conversion and a separately balanced spectacle conversion. New spread, explosive behavior or resource costs require explicit rules and visible correspondence.
- **Muzzle / projectile / impact:** capture the original first; bounded amber flash, readable traces, contact sparks and optional smoke-ring styling. Preserve hit attribution, loot and server authority; never infer block destruction from an art panel.
- **Inspection:** a restrained sequential amber-inset pulse and metal settling motion, with no bonus shot, refill or damage. Test cancellation and reduced-motion/effects settings.
- **Animation:** equip, aim, fire, optional reload, inspect and first/third-person transitions. All shrouds, controls, grip and accessories must clear each other throughout the full motion.
- **Reload:** optional for the original resource behavior. Only conversions with an explicit magazine or charge system receive those mechanics.
- **Customization:** original-fit and premium skins, gameplay-earned charm bonuses, stickers, animated/glowing emblems, custom projectile/tracer/impact/finisher selections and comfortable attachment placement.
- **Craftables / dismantling:** current survival obtaining remains unresolved. Any newly designed recipe must be labeled as new; effect transfer and parts recovery need item-conservation and full-inventory tests.
- **Death effects:** optional confirmed-kill cosmetics, preserving loot, kill credit and multiplayer state. No undocumented extra area damage.
- **Performance:** cached attachment state, no idle repeated scanning, bounded particles and LODs, and measured frame-time lows with the intended mod stack.

## Open acceptance gates

- [ ] Native direct-hit, failed-hit, entity/block contact and environmental-rule tests
- [ ] Original projectile/impact/audio captures and current acquisition verification
- [ ] Complete attachment, muzzle, projectile and finisher concepts
- [ ] Actual model proportions, hand fit, collision sweeps and animation interruption tests
- [ ] Native export, multiplayer, persistence, dismantling and performance qualification

[Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
