# KA-500 · compact cyan-orange sniper

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## What the original does

The KA-500 inherits BaseSniper: a non-automatic Metal Slug weapon. Its subclass chooses the medium-rifle/long firing report and **SCOPE_4** overlay. It declares no special impact override. The orange petal in its recipe does not establish plant projectiles, explosive hits or a canonical manufacturer.

| Stored constructor input | Value |
|---|---:|
| Damage | 30 |
| Durability | 360 |
| Delay | 70 ticks |
| Stored recoil constructor input | Approximately 0.06 |

These are stored inputs, not guaranteed final damage or physical measurements. At 20 TPS, the nominal delay is 3.5 seconds; lag and runtime conditions can alter observed timing.

## Preserve the original identity

![Released KA-500 sprite, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ka500-original-preview.png)

The long dark front, compact blue/cyan center, orange forward accent, dark grip and rear, and raised dark optic with warm accent are the visual anchors. The new concept makes the surfaces more expressive while retaining that palette and layout. A specific origin dimension or manufacturing story has not been established by the inspected subclass and recipes; do not invent one from the colors.

## Infusion crafting, with every slot shown

![KA-500 infusion documentation diagram](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ka500-infusion.webp)

Put a **Sniper Frame** in the base slot. In the middle ingredient grid, occupy six slots with:

- Small Orange Petal
- An item in `forge:gems/quartz`
- An item in `forge:ingots/skeletal`
- An item in `forge:ingots/iron`
- Another item in `forge:ingots/iron`
- An item in `forge:gunpowder`

The middle arrangement is order-independent. The two iron entries require two occupied ingredient slots; one stack of two is not a substitute. The image is a reconstructed documentation layout. Tag icons are examples, not an exhaustive membership list. Its gunpowder illustration is reused from the documented 1.21.1 vanilla icon atlas; the recipe itself is read from the pinned 1.20.1 release. Datapacks may change accepted tags.

[Infusion Table tutorial](Infusion-Table-Crafting-1.20.1)

## Two documented upgrade routes

![Floro500 upgrade](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-floro500.webp)

**KA-500 + Floro Upgrade Kit → Floro500.** The checked Floro500 constructor raises damage to 37 and durability to 550, retains the 70-tick delay and uses approximately 0.042 recoil. It uses SCOPE_2 rather than KA-500's SCOPE_4. [Floro500 profile](Floro500-Weapon-Profile).

![Mark Maker upgrade](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-mark_maker.webp)

**KA-500 + Weapon Parts → Mark Maker.** This is a distinct output identity. Do not treat it as a skin or assume it preserves the same firing behavior without its own profile. [Weapon Parts recipes](Divine-Upgrades-Weapon-Parts).

[Divine Station guide](Divine-Station-Weapon-Upgrades-1.20.1) · [All 70 illustrated upgrade recipes](Divine-Station-Upgrade-Atlas)

## Premium concept and proposed feedback

![KA-500 concept study, not in-game](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ka500-concept-v1.png)

This sheet explores a compact cyan-painted shell, orange forward panel, dark muzzle shroud, tactile grip, petal charm and optic-glint inspection. Its blue muzzle/tracer/impact effects are cosmetic proposals, not captures of the original Metal Slug. The charm's petal motif acknowledges an actual recipe ingredient without claiming magical powers or invented lore.

The first concept still needs a dedicated silhouette comparison: its enlarged optic and decorated grip must remain readable and comfortable in first-person views. Painted surfaces do not constitute finished texture maps or either required in-game material mode.

## Complete feature plan

- **Model and textures:** original-fit and premium material modes; clean UVs, mip-readable paint, restrained wear, correct normals and silhouette fidelity.
- **Optics and handling:** keep the baseline SCOPE_4 option; aligned native camera, clear aiming center, ergonomic hand space and accessory clearances.
- **Barrel variants:** short close-fitting shroud, precision-weighted fore-end, and separately specified fantasy scatter conversion. Any changed projectile count, damage or cadence needs explicit server rules and resource accounting.
- **Animation:** equip, idle, aim, successful shot, recovery, optional reload/recharge, inspection and interruption. Cosmetic optic glints never fire gameplay events.
- **Customization:** detachable earned charms; skins, emblems, static/animated/glowing stickers; optional muzzle, tracer, impact, decal and confirmed-kill finisher sets.
- **Modification:** safe part swapping, dismantling, special-effect transfer, full-inventory returns and upgrade handling for both Floro500 and Mark Maker routes.
- **Feedback and QA:** capture original native projectile flight/impact and sound first. Verify recoil readability, no clipping, moving hand clearances and reduced-effects settings.
- **Compatibility and speed:** no repeated scans; cached configs, bounded effects, native TaCZ export, multiplayer authority, persistence and equivalent-work frame-time checks.

## Acceptance gates

- [ ] Native baseline projectile, impact, scope, sound and resource captures
- [ ] Full feature-set concept sheets, attachment variants and finishers
- [ ] Faithful mesh, two material modes and first/third-person hand-fit review
- [ ] Full animation, interruption and both upgrade-path data-preservation tests
- [ ] Native gameplay, multiplayer, compatibility and performance qualification

[Source evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/ka500-source-evidence.json) · [Complete weapon standard](Weapon-Completeness-Standard) · [Concept gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
