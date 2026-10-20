# Clown Cracker: carnival colors with deliberate sniper handling

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Original role

Clown Cracker inherits **BaseSniper**, using Metal Slug ammunition and non-automatic firing. Its inspected subclass selects the medium-rifle/long firing sound and SCOPE_4 overlay. It does not declare a unique impact effect: confetti ammunition, explosions, stun or a clown-honk sound are not established by this class.

| Stored field | Clown Cracker | Hive Cracker upgrade |
|---|---:|---:|
| Damage input | 33.5 | 44.0 |
| Durability | 305 | 555 |
| Delay | 84 ticks | 84 ticks |
| Recoil input | Approximately 0.05 | Approximately 0.035 |

These are constructor values, not guaranteed final damage or measured physical quantities. At 20 TPS the nominal delay is 4.2 seconds. Preserve inherited native sniper behavior rather than silently substituting a generic rapid-fire weapon.

## Original palette and silhouette

![Actual released Clown Cracker sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cracker-original-preview.png)

Keep its compact mustard-gold body, dark rear/grip, raised sight with blue accent, and broad pale front carrying red/green square details. The paper and Confetti Pile recipe ingredients support a carnival-themed interpretation, but do not prove that the original projectile is confetti or that it has a particular maker's history.

## Infusion: seven separate ingredient slots

At the **Infusion Table**, place a Sniper Frame in the separate left base slot. Use seven middle slots for:

- Confetti Pile ×2, one in each of two slots
- Paper ×1
- One ingredient matching `forge:gems/diamond`
- One matching `forge:ingots/iron`
- Two matching `forge:ingots/limonite`, in separate slots

Leave the other two middle slots empty. Middle-grid order is irrelevant. Stacking two repeated ingredients in one slot does not substitute for two entries; tags can be changed by a modpack. The bundled definition is `data/aoa3/recipes/infusion_clown_cracker.json`, using the inspected ordinary defaults for omitted level/XP fields.

[Illustrated Infusion Table workflow](Infusion-Table-Crafting-1.20.1) · [Exact recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=infusion_clown_cracker)

## Lelyetian upgrade

At the **Divine Station**, put Clown Cracker in the left input and a Lelyetian Upgrade Kit in the middle; the output is [Hive Cracker](Hive-Cracker-Weapon-Profile). The exact bundled definition is `data/aoa3/recipes/upgrade_kit_hive_cracker.json`.

This upgrade keeps the checked delay while increasing damage/durability and reducing recoil input. The base recipe does not inherently promise to copy arbitrary custom item data. Test names, enchantments and third-party attachments on disposable copies, and explicitly define which custom pieces survive or are returned.

[Divine Station workflow and data-transfer limits](Divine-Station-Weapon-Upgrades-1.20.1)

## Premium concept: a short playful inspection

![Clown Cracker hero, side profile, material/sight details and optional confetti inspection concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cracker-concept-v1.png)

The sheet develops the original pale/red/green front and gold/dark body into richer material detail. Its three-beat inspect concept tilts the closed weapon, briefly flutters optional cosmetic confetti, then settles back. Confetti is **not a replacement for Metal Slug ammo** and is not claimed as an original firing effect.

These are painted concept poses, not implemented animation frames. The proposed control geometry and supporting-hand position need actual rig/clearance checks; the artwork alone cannot pass those gates. Material closeups are design targets, not completed texture atlases.

## Complete upgrade plan

- **Handling:** deliberate sniper fire and readable recovery, preserving native timing and resources. Do not accidentally turn a cosmetic inspect flourish into a firing or reward event.
- **Sight:** retain the original SCOPE_4 option. [Actual shared overlay illustration](Crystaneer-Weapon-Profile#original-silhouette-and-sight); alternate optics still need native aim alignment.
- **Inspect:** optional brief confetti, bounded particle count, a reduced-effects version and immediate interruption on gameplay actions. No persistent litter, extra loot or server simulation for a cosmetic flourish.
- **Attachments:** compact/steady handling choices, fore-end/sight variants and clearly defined fantasy conversions. Functional changes require explicit resource and stat rules, with matching visible appearance.
- **Materials:** original-fit and premium treatments retain the white/gold/red/green identity; avoid excessive bloom or expensive permanent lights.
- **Resources:** original Metal Slug behavior, optional reload only when deliberately selected. Define any magazine/charge conversion and its cancellation rules.
- **Animation:** equip, idle, aim, fire, recovery, optional reload, inspect, swaps and interruptions in first and third person with actual hand rigs.
- **Effects:** record the original projectile/muzzle/impact/sound first, then add separate tracer, decal, impact and optional confirmed-kill cosmetic choices. Preserve damage, loot and kill credit.
- **Customization:** earned functional charms with explicit bonuses, skins, stickers and animated/glowing emblems. Keep ornaments outside control/hand paths.
- **Persistence/performance:** safe upgrade/dismantling with full inventories, multiplayer/save tests, cached configuration, LODs and measured frame-time lows.

## Acceptance gates

- [ ] Original native scope, projectile, impact, sound and resource captures
- [ ] Complete attachment, muzzle, tracer, impact, decal and finisher concepts
- [ ] Rigged-hand clearance, coherent proportions and two material modes
- [ ] Full animation/interruption and Lelyetian customization-transfer tests
- [ ] Native export, multiplayer, persistence, dismantling and performance qualification

[Released source and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/clown-cracker-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
