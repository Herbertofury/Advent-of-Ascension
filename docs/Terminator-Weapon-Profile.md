# Terminator · charcoal and silver, deliberately heavy

**AoA 3.7.1 / Minecraft 1.20.1 · released-source profile and partial concept study. Native upgrade acceptance remains open.**

## Current selected concept · 22 October 2026

![Terminator selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/terminator-scifi-concept-v2.png)

New charcoal/silver sniper candidate retains the low shroud and raised red-accent sight. Small red status lens and NO FATE / T-800 engraving are decorative film nods. Exact stock proportions, hand fit and native performance remain open.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Aterminator). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

Dedicated supplemental studies (partial design candidates, not implemented features):

- [Optional movie-nod trinkets, finishes and engravings; corrected single rear charm keeps forward contact area uncluttered; native fit unverified](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/terminator-cinematic-cosmetics-study-v2.png).

## What it does

Terminator is a slow **Metal Slug sniper** with an explicit **SCOPE_3** texture override. Its weapon class declares sound, pitch adjustment and scope, but no special impact or projectile-creation override. Do not invent explosive rounds, armor piercing or automatic target execution from its name.

| Released input | Value |
|---|---:|
| Damage | 53 |
| Durability | 470 |
| Firing delay | 112 ticks, nominally 5.6 seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.035 |
| Ammunition | Inherited Metal Slug |
| Scope | SCOPE_3 |
| Sound | Metallic sniper, long variant |
| Pitch-adjust input | 0.1 |

Constructor inputs are not measured final damage, screen displacement or effective range. The sound adjustment is an input to the sound path, not a claim that the heard sound is 10% lower. Obtain actual native scope, sound, projectile and impact footage before replacing their presentation.

## Recognizable original design

![Released Terminator, alpha-composited before nearest-neighbor enlargement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/terminator-original-preview.png)

Preserve its compact charcoal/silver silhouette, short squared front, two dark front recesses, raised sight with red accents and broad stepped rear. This weapon should remain distinct from a generic long-barreled military sniper.

## Craft it, then upgrade it

![Terminator infusion ingredients](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/terminator-infusion.webp)

The released infusion uses **Sniper Frame** plus eight ingredient slots: Darkly Powder twice, Unstable Gunpowder, Power Core, an obsidian-tag member, an iron-ingot-tag member twice, and a bloodstone-gem-tag member. Repeated ingredients occupy separate recipe entries; the diagram is not a shaped crafting-grid pattern. Tag sprites are example members.

![Terminator plus Rocky Upgrade Kit produces Mineral](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-mineral.webp)

**Terminator + Rocky Upgrade Kit → Mineral.** Mineral raises the listed damage/durability to 58.5/560 and inherits SCOPE_1 instead of Terminator’s SCOPE_3. Do not silently preserve the wrong scope in an upgraded item. The recipe establishes lineage; it does not establish a particular creator or dimension of manufacture.

[1.20.1 Infusion Table walkthrough](Infusion-Table-Crafting-1.20.1). [Current Divine upgrade atlas](Divine-Station-Upgrade-Atlas) · [Mineral profile](Mineral-Weapon-Profile).

## Earlier preserved art: Proposed premium art

![Terminator concept with matching side view, proposed optic shell and material studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/terminator-concept-v1.png)

The obsidian-like surface, brushed-silver panels and red optic accents are proposed material choices informed by its palette and recipe. They are not new canonical lore. Keep surface detail readable at Minecraft scale, with an original-fit treatment and an optional premium treatment.

The compact block silhouette is retained, but the broad rear/grip needs actual hand-fit and camera testing. The painted guard opening does not prove ergonomic clearance. The optional sight shell must preserve sight visibility; a dramatic inspection light must not imply a new damage mechanic. This image remains concept art, not a finished texture atlas or native asset.

## Full feature plan

- **Modules and variants:** distinct optic shells, restrained shroud treatments, lower support and earned skins. Gameplay conversions need explicit ammunition, damage and cadence contracts.
- **Motion:** equip, idle, walk/run, aim, confirmed firing, heavy recovery, optional reload, inspect, swaps and cancellation; first/third-person and left-hand poses.
- **Effects:** original/new flight and impact comparison; selectable muzzle, tracer, projectile, armor/terrain/fluid impact, bounded decal and confirmed-kill finisher designs.
- **Customization:** charms with explicit eligible bonuses, static/animated/glowing stickers, emblems, texture modes and reduced-motion/effect settings.
- **Progression:** complete module recipes and dismantling returns; conserve eligible customization through the Rocky upgrade without copying incompatible state or duplicating resources.
- **Integration:** original fallback, TaCZ presentation and turret qualification, multiplayer authority, save/reload, exact-version regression and equivalent-scene performance checks.

## Acceptance gates

- [ ] Native original behavior, scope, sound, flight and impact captures
- [ ] Complete module, projectile, impact and finisher concept coverage
- [ ] Faithful mesh and both texture modes with hands/clearance checks
- [ ] Full animation and interrupt-safe optional reload handling
- [ ] Gameplay, migration, multiplayer and compatibility tests
- [ ] Startup, memory and frame-time measurements

[Exact released evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/terminator-released-evidence.json) · [Weapon quality standard](Weapon-Completeness-Standard) · [Armory](Weapon-Overhaul)

AoA original identity and assets: Tslat and contributors. Proposed upgrade art and implementation remain separate from the released original. No native acceptance is promoted.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](Effective-Recoil-Routing-1.20.1).
