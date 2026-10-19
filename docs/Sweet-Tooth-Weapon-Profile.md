# Sweet Tooth · candy-colored sniper with a hit-triggered speed boost

**AoA 3.7.1 / Minecraft 1.20.1 · partial concept and source study · native upgrade unaccepted.**

## What the original does

Sweet Tooth is a **Metal Slug BaseSniper**. Its special impact hook gives the **shooter Speed III for 80 ticks**, nominally four seconds at 20 TPS. It does not buff the target. The inspected BaseGun caller invokes the hook after its attack method returns success, so the upgrade must not award the boost just for firing, missing, or playing a cosmetic impact effect.

The bundled EffectsLib takes builder level 3 and converts it to Minecraft amplifier 2. This is Speed III, not Speed IV. The official named source agrees with the released bytecode. Native conditions, stacking, immune targets and multiplayer behavior still need tests.

| Registered input | Value |
|---|---:|
| Damage | 32.5 |
| Durability | 460 |
| Firing delay | 77 ticks, nominally 3.85 seconds at 20 TPS |
| Recoil modifier | Approximately 0.05 |
| Ammunition | Metal Slug |
| Scope | Inherited SCOPE_1 |
| Sound | Medium rifle, long report |

These are constructor inputs, not measured final damage, animation timing or recoil displacement. SweetTooth does not override projectile creation or scope selection. Original native flight, impact and scope footage remain required.

## Keep the original candy identity

![Actual released Sweet Tooth sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sweet-tooth-original-preview.png)

The original combines chocolate-brown structure, red/white peppermint accents, a bright yellow band, dark raised sight with yellow highlights and pink rear decoration. The candy ingredients support this visual theme, but do not establish a fictional manufacturer, origin story or new edible ammunition. The upgrade keeps Metal Slugs unless a separately designed gameplay conversion explicitly changes the contract.

## Illustrated infusion recipe

![Sweet Tooth infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sweet-tooth-infusion.webp)

Use **Sniper Frame** as the base input with seven ingredients: Candy Corn twice, Candy Cane, Chocolate Block, Gingerbread Cookie, Sugar and an iron-ingot tag match. The two Candy Corn entries occupy two ingredient slots. The reconstructed diagram's middle grid is order-independent. It is a recipe guide, not an in-game capture. Iron is a tag example and datapacks can change matches.

## Revised premium concept

![Sweet Tooth revision three concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sweet-tooth-concept-v3.png)

The proposed chocolate enamel, frosted ceramic, amber accents and glossy icing preserve the original color zones. The hero and side views now put the rear grip behind the trigger, with an open guard. A single peppermint muzzle collar and rear peppermint grip preserve the two main accent zones.

**This remains a partial, unaccepted art study.** The inspection inset still contains an older double-collar detail and must be reconciled before using it as a modeling reference. Native hands, actual scale, optic alignment, all moving-part clearances and matching opposite-side construction have not passed QA. The painted texture is a reference, not a finished UV map.

<details><summary>Earlier concepts retained, with their rejected details</summary>

![First Sweet Tooth exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sweet-tooth-concept-v1.png)

Revision one introduced an oversized underbody slab and extra front peppermint collar. It did not pass ergonomic review.

![Second Sweet Tooth exploration](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sweet-tooth-concept-v2.png)

Revision two opened the guard but put the pistol grip on the wrong side of the trigger. Revision three corrects that arrangement in the main and side views. Neither earlier version is discarded or presented as accepted.

</details>

## Full customization and feedback plan

- **Original-fit / premium:** retain chocolate, yellow, peppermint and pink grouping in both visual modes; author real UVs, material response and readable small-scale detail.
- **Attachments:** compact amber sight housing, peppermint sleeve, stable fore-end and optional candy-glass fantasy scatter conversion. Gameplay-changing conversions need explicit damage, projectile count, effect, resource and authority rules.
- **Animation:** equip, idle, aim, confirmed fire, recoil recovery, optional reload, inspection, switching and interruption recovery, with first/third-person hands.
- **Inspect:** restrained icing ribbon or gingerbread charm flourish; it must not block aiming or grant a speed buff.
- **Flight / impacts:** preserve original comparison footage; separate muzzle, tracer, entity/armor/terrain/fluid impact, decal and confirmed-kill finisher channels. Painted golden sparks are cosmetic proposals.
- **Progression:** earned gingerbread charms, skins, emblems and static/animated/glowing stickers; customizable tracer, impact and death effects with safe placement.
- **Effect salvage:** conserve resources, retain unknown extension data, support full-inventory returns and keep server-authoritative Speed rewards independent of client cosmetics.
- **Performance:** game-time presentation, bounded particles/decals, cached settings, no repeated scans, and measured equivalent-work native testing.

## Acceptance checklist

- [ ] Original native flight, impact, scope, sound and successful-hit speed evidence
- [ ] Consistent inspection, attachment, projectile, decal and finisher art
- [ ] Faithful mesh, two UV/material modes, hand fit and collision review
- [ ] Correct shooter-only Speed III duration, successful-hit gating and stacking
- [ ] Native networking, persistence, optional compatibility and performance acceptance

[Released evidence and recipe](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sweet-tooth-released-evidence.json) · [Official named source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/content/item/weapon/sniper/SweetTooth.java) · [Bundled effect-level audit](Sludge-Sniper-Weapon-Profile) · [Weapon overhaul](Weapon-Overhaul)

Original AoA assets and behavior are credited to Tslat and contributors. Generated art, tests and proposed integration work are separate. No native acceptance is promoted.
