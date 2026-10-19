# Mark Maker · crimson precision upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Original role and checked behavior

Mark Maker is a **BaseSniper** weapon using Metal Slug ammunition and non-automatic firing. Its subclass selects **SCOPE_4** and the medium-rifle/long firing report. It declares no custom impact override. Its name does not establish enemy marking, debuffs or area damage.

| Stored constructor input | KA-500 | Mark Maker |
|---|---:|---:|
| Damage | 30 | 36.5 |
| Durability | 360 | 530 |
| Delay | 70 ticks | 70 ticks |
| Recoil modifier | Approximately 0.06 | Approximately 0.05 |

These are stored inputs, not guaranteed final damage or real-world physical values. At 20 TPS the nominal input delay is 3.5 seconds. Mark Maker retains the checked cadence and scope selection of its KA-500 predecessor.

## Original appearance and provenance

![Actual released Mark Maker sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mark-maker-original-preview.png)

Preserve the broad charcoal front, crimson central shell and downward forward panel, grey bands, dark grip, red rear and raised dark-red optic with a small cyan detail. Its recipe lineage is established; a specific manufacturing culture or dimension is not established by the inspected class and recipe files. Do not turn a dramatic presentation backdrop into invented canonical lore.

## Craft the upgrade, then follow its lineage

![KA-500 and Weapon Parts produce Mark Maker](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-mark_maker.webp)

At the Divine Station, combine **KA-500 + Weapon Parts → Mark Maker**. [KA-500's illustrated infusion recipe](KA-500-Weapon-Profile) shows the prerequisite weapon. [All Weapon Parts upgrades](Divine-Upgrades-Weapon-Parts).

![Mark Maker and Lunar Upgrade Kit produce Moon Maker](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-moon_maker.webp)

A further bundled recipe combines **Mark Maker + Lunar Upgrade Kit → Moon Maker**. This is a separate output item requiring its own behavior profile; the upgrade name alone does not prove celestial damage or preserve every attachment.

[Divine Station walkthrough](Divine-Station-Weapon-Upgrades-1.20.1) · [Lunar upgrade atlas](Divine-Upgrades-Lunar)

Custom names, enchantments, charms, effect modules and third-party item data require explicit preservation and return tests on both upgrade routes. The existence of a recipe does not certify a safe migration for arbitrary custom data.

## Premium concept and proposed effects

![Mark Maker concept, external appearance and cosmetic storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mark-maker-concept-v1.png)

The concept develops the crimson, charcoal and silver palette into layered enamel panels with a distinct angular fore-end. Its optic-glint inspection and seal charm are optional cosmetic ideas. The proposed red tracer and ring impact are presentation only; they do not establish an original explosion, enemy marking effect or new damage area.

The illustration is not a model, finished UV set or native capture. The broad optic, pointed lower fore-end and charm must be checked against hand poses, sight alignment and every animation before approval. Original-fit and premium material modes both remain implementation work.

## Full feature plan

- **Model/materials:** original silhouette and color anchors, clean UVs, controlled roughness, game-distance readability and two material modes.
- **Optics:** keep SCOPE_4 and a clear native aiming center; optional red-lined housings cannot obscure the target.
- **Attachments:** compact muzzle shroud, stability-oriented fore-end and a separately specified fantasy pulse conversion. Any changed damage, projectile count, cadence or resource cost must be explicit and server-authoritative.
- **Animations:** equip, idle, aim, successful firing, recovery, optional reload, inspection, swapping and interrupted transitions with first/third-person hands.
- **Feedback:** original projectile/impact/audio captures first; selectable muzzle, tracer, impact, decal and confirmed-kill finisher effects with reduced-effects settings.
- **Personalization:** earned functional charms, finishes, emblems and static/animated/glowing stickers, with collision-safe placement.
- **Persistence:** dismantling and special-effect transfer, full-inventory returns, save/reconnect and migration through KA-500 → Mark Maker → Moon Maker.
- **Compatibility/performance:** cached configuration, bounded particles, no repeated scans; actual TaCZ export, multiplayer, optional adapters and equivalent-work frame-time measurements.

## Acceptance gates

- [ ] Native original scope, projectile, impact, sound and ammo captures
- [ ] Complete attachment, finisher, decal and alternate-mode concepts
- [ ] Faithful model, textures, two material modes and hand-fit review
- [ ] Full animation/interruption and upgrade-data preservation tests
- [ ] Native gameplay, multiplayer, compatibility and performance qualification

[Source and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mark-maker-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Concept collection](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
