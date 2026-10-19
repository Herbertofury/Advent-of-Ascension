# Floro500: magenta-green botanical sniper

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Original role

Floro500 inherits **BaseSniper**, using Metal Slug ammunition and non-automatic firing. Its subclass selects the medium-rifle/long firing sound and **SCOPE_2** overlay. It declares no unique impact effect. Flowers and green panels do not establish healing, poison, growing plants or petal ammunition.

| Stored input | KA-500 | Floro500 |
|---|---:|---:|
| Damage | 30 | 37 |
| Durability | 360 | 550 |
| Delay | 70 ticks | 70 ticks |
| Recoil | Approximately 0.06 | Approximately 0.042 |

These are constructor inputs, not guaranteed final damage or physical recoil measurements. At 20 TPS the nominal delay is 3.5 seconds. The upgrade keeps that checked input cadence.

## Original identity and grounded context

![Actual released Floro500 sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/floro500-original-preview.png)

Preserve the low broad dark front, charcoal receiver/grip, magenta/purple and green body, raised pink-green sight area, warm optic accent, pink-green rear and small cyan detail. The concept develops those colors into botanical inlays; it does not invent a canonical maker or construction story.

The separately inspected **1.12.2 / AoA 3.3.6** drop index associates the Floro Upgrade Kit with Archvine, Broccohead, Carrotop, Corny, Daysee, Flowerface, Pod Plant, Squasher, Sunny, Vine Wizard and Vinocorne. That is historical kit-collection context, not proof of the same sources in 1.20.1, a drop percentage or where this particular weapon was manufactured.

[Historical drop-index evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/drop-index-1.12.2.json)

## Divine Station upgrade

![KA-500 plus Floro Upgrade Kit produces Floro500; released-texture documentation diagram](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-floro500.webp)

Put **KA-500** in the left input and a **Floro Upgrade Kit** in the middle; collect **Floro500**. The exact bundled definition is `data/aoa3/recipes/upgrade_kit_floro500.json`.

Custom names, enchantments, charms and third-party attachments need explicit preservation/return rules; the recipe alone does not prove arbitrary item data survives. Test on disposable copies before relying on a migration.

[Station tutorial](Divine-Station-Weapon-Upgrades-1.20.1) · [All Floro upgrades, pictured](Divine-Upgrades-Floro) · [All 70 upgrade recipes](Divine-Station-Upgrade-Atlas)

## Concept, finishes and cosmetic inspection

![Floro500 hero, side silhouette, proposed finish variants and inspection/effect storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/floro500-concept-v2.png)

The default concept keeps the magenta-green identity. Ivory/gold and blue/violet panels are optional finish ideas, not evidence of implemented material modes. The required original-fit and premium rendering modes still need actual texture assets and native comparison.

The short petal flourish is an optional inspection cosmetic. It must not consume ammo, spawn gameplay projectiles, add damage or become persistent world litter. The effect strip is a proposal, not footage of the original Metal Slug flight/impact. Painted hand poses do not prove clearance or animation correctness.

The raised petals and leaf inlays need particular attention around the sight line, charging/reload motions and supporting hand. Decorative surfaces should remain legible at game distance without excessive bloom or noisy microdetail.

## Full feature plan

- **Shape/materials:** retain original color anchors and broad dark front; build original-fit and premium modes with clean UVs, mip readability and deliberate roughness. Curved leaves need [normal-fidelity checks](Mesh-Normal-Fidelity-and-Opt-In), not parser success alone.
- **Optics:** preserve SCOPE_2; optional petal-framed sights must leave the aiming center clear and align with the actual first-person camera.
- **Barrel options:** close-fitting floral shroud, a steadier root-shaped fore-end and a separately defined fantasy bloom-burst conversion. Any functional conversion requires explicit resource, projectile and damage rules.
- **Animation:** equip, idle, aim, confirmed fire, recovery, optional reload, inspection, modification and interruption with real first/third-person hands.
- **Resources:** baseline Metal Slug behavior; reloading optional. Magazine conversions need explicit capacity, cancellation, ownership and save semantics.
- **Feedback:** first capture original muzzle, projectile, impact and sound. Then support optional tracer, muzzle flash, impact, decals and confirmed-kill finishers with reduced-effects choices.
- **Customization:** earned functional charms, skins, static/animated/glowing stickers and emblems. Do not let leaves or ornaments intersect controls, hands or the optic.
- **Persistence:** safe dismantling and special-effect transfer, full-inventory returns, upgrade migration, reconnect and save/load tests.
- **Performance/compatibility:** cached configuration, bounded cosmetic emissions and no repeated scans. Validate native TaCZ export, multiplayer authority, optional adapters and measured frame-time lows.

## Acceptance gates

- [ ] Original native scope, projectile, impact, sound and resource captures
- [ ] Complete attachments, charms, finish and muzzle/tracer/impact/decal/finisher concepts
- [ ] Faithful model, clear sight/hand paths and two finished material modes
- [ ] Full animation/interruption and Floro upgrade customization-transfer tests
- [ ] Native gameplay, export, multiplayer, persistence and performance qualification

[Released source and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/floro500-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
