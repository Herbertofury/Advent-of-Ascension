# Sabbath · violet and teal, withering sniper

**AoA 3.7.1 / Minecraft 1.20.1 · source-backed baseline and partial concept study. No native upgrade acceptance.**

## What the weapon actually does

Sabbath is a **Metal Slug sniper** with **SCOPE_3**. Its impact hook checks for a living target, then requests **Wither I for 280 ticks**, nominally 14 seconds at 20 TPS. The named upstream source identifies Wither; the released bytecode records the 280-tick request; the bundled EffectBuilder converts its default level 1 to amplifier 0.

This is a target debuff request, not a shooter buff, explosion, automatic execution or guarantee that every creature accepts Wither. Immunities, cancellation and other mods remain native test cases. Preserve the successful-hit/impact path rather than triggering gameplay from cosmetic animation.

| Released constructor input | Value |
|---|---:|
| Damage | 44 |
| Durability | 450 |
| Delay | 97 ticks, nominally 4.85 seconds at 20 TPS |
| Recoil modifier | Approximately 0.035 |
| Ammunition | Inherited Metal Slug |
| Scope | SCOPE_3 |
| Firing sound | Heavy sniper, long variant |

The table records source inputs. It does not establish final combat damage, screen recoil, effective range or captured sound. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/Sabbath.java) · [Exact released evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sabbath-released-evidence.json).

## Original identity

![Released Sabbath sprite, alpha-composited on neutral gray](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sabbath-original-preview.png)

Retain the broad dark body, violet sections, teal underside/rear accents, long raised sight with red end accents, short silver muzzle and slanted rear grip. These anchors distinguish Sabbath from other snipers without inventing a religious origin, a creator or a specific manufacturing dimension.

## Illustrated infusion

![Sabbath six-slot infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sabbath-infusion.webp)

Combine **Sniper Frame** with Ghoulasm, Primordial Skull, Darkly Powder, a ghoulish-ingot-tag member, a ghastly-ingot-tag member and a gunpowder-tag member. Ghoulish and Ghastly are separate requirements. The recipe diagram is order-independent, and tag icons are examples rather than an exhaustive tag expansion. [1.20.1 Infusion Table walkthrough](Infusion-Table-Crafting-1.20.1).

The ingredients can inform a proposed spectral material direction. They do not prove that a depicted skull spirit, crystal enclosure or inspection wisp is an original mechanic.

## Concept development

![Sabbath revised concept with smooth guard opening](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sabbath-concept-v2.png)

V2 removes the inward-pointing guard ornaments seen in V1 and uses a smooth open control area in both main views. The charcoal, violet, teal and red identity remains. The spectral wisp, crystal-like panels and optic shell are proposed visuals, not evidence of original projectile appearance or new gameplay. Actual hands, aim alignment, opposite-side construction and full animation still require testing.

<details><summary>Earlier V1: retained, but rejected as the hand-clearance target</summary>

![Earlier Sabbath concept with problematic inward guard points](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sabbath-concept-v1.png)

The inward-facing spikes and hooks should not pass hand-clearance QA. Retained for design history, not an accepted mesh or pose.

</details>

## Optional modules and feedback storyboard

![Sabbath module and effects concepts, revised labels and charm placement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sabbath-modules-fx-v2.png)

The standard shroud preserves original rules. **Spectral Lance** and **Wraith Orbit** are proposed gameplay conversions, not cosmetic equivalents: a beam and orbiting discs require their own server-authoritative hit rules, bounded lifetime/range, ammunition/resource policy, cadence, damage and Wither application limits. No untested damage or free-resource bonus is implied.

The board also explores an exterior skull charm, alternate optic casing, static/glowing emblem, muzzle flash, flight trail, impact ring, temporary terrain mark and confirmed-kill motes. Original flight/impact capture remains explicitly pending. The terrain mark is a temporary overlay, never a changed block; the finisher requires a confirmed death event and expires. Native materials, animation, collision and performance remain open.

V2 moves the charm outside the guard and corrects V1’s misleading cosmetic-module labels. Its full swing envelope, actual hands and aim/inspect poses still need geometry tests. A gameplay-affecting charm would need a separate declared bonus; this illustrated charm is currently a cosmetic proposal.

<details><summary>Retained V1 board: rejected labels and charm placement</summary>

![Earlier module board with labels and charm placement requiring correction](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sabbath-modules-fx-v1.png)

V1 called beam/disc conversions cosmetic and placed a charm across control-space. Those are not accepted design targets.

</details>

[Feature-by-feature status](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sabbath-feature-status.json) records concept work separately from implementation and native QA.

## Complete feature plan

- **Shape and materials:** preserve the original color/silhouette hierarchy in Minecraft-fit and premium modes; readable purple/teal channels, bounded glow, texture/UV/normal review.
- **Parts and craftables:** optional optic shell, exterior shrouds, grip finishes and earned charms. Any alternate spectral beam or projectile conversion needs an explicit separate resource, damage and cadence specification.
- **Motion:** equip, idle, movement, aim, confirmed fire, deliberate recovery, optional reload, inspect and interrupt recovery, with real first/third-person hand meshes.
- **Effects:** native original flight/impact captures first; optional muzzle, tracer, projectile, entity/armor/terrain/fluid impacts, expiring decals and confirmed-kill finishers. A skull-wisp inspect is cosmetic; no unconfirmed kill or debuff event.
- **Personalization:** skins, static/animated/glowing stickers, custom emblems and gameplay-earned charms; effect choices and reduced-motion/intensity options.
- **Progression and compatibility:** documented recipes, salvage and save/reload conservation; original fallback, server-authoritative hit/effect handling, optional TaCZ/turret integration and exact-version regression tests.
- **Performance:** cache assets/settings, bounded game-time effects, and measured startup/memory/frame-time comparisons under equivalent scenes.

## Acceptance gates

- [ ] Original native scope, shot, impact, sound and Wither acceptance cases
- [ ] Complete attachment, projectile, impact, decal and finisher concepts
- [ ] Faithful mesh, two texture treatments and clear hand/guard/sight space
- [ ] Full animation and interrupt-safe optional reload handling
- [ ] Multiplayer, immunity/cancellation, migration and compatibility tests
- [ ] Measured performance and reduced-motion/effect options

[Armory](Weapon-Overhaul) · [Complete weapon standard](Weapon-Completeness-Standard)

Original AoA identity/assets belong to Tslat and contributors. New concepts remain proposals. No native or final-art acceptance is promoted.
