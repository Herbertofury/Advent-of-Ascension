# Purity Shotgun: the blue-armored upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source-backed profile and concept proposal · no accepted native upgrade.**

## What it does

Purity Shotgun fires **three Spreadshot pellets**, with one shared boosted-shot decision before the pellet loop. Its custom method calls `RandomUtil.oneInNChance(5)` once; every pellet receives multiplier input **1.5 when selected, otherwise 1.0**. This preserves Destruction Shotgun's shot-level boost structure. Do not reroll per pellet, client or visual effect.

The name does not establish healing, cleansing, holy damage or status removal. No unique explosion hook appears in this inspected class. Preserve ordinary projectile behavior unless the player explicitly equips a separately balanced conversion.

| Released field | Value / boundary |
|---|---|
| Registry ID | `aoa3:purity_shotgun` |
| Stored damage input | 14.0; not guaranteed final hit damage |
| Pellets | 3 |
| Durability | 1090 |
| Delay | 56 ticks, nominally 2.8 seconds at 20 TPS |
| Recoil input | 0.25; not camera degrees |
| Knockback input | Approximately 0.4; not measured distance |
| Ammunition | Spreadshot |
| Loop projectile | LimoniteBulletEntity; age input 4, piercing input 0 |
| Shared boost | One-in-five helper; multiplier 1.5 or 1.0 |
| Fire mode / sound | Non-automatic; heavy long shotgun sound selector |

Compared with Destruction Shotgun's constructor fields, damage input rises from 10.5 to 14, durability from 690 to 1090, and recoil input falls from approximately 0.45 to 0.25. The three-pellet count and 56-tick delay stay the same. These comparisons do not establish measured DPS, camera motion or guaranteed aggregate damage: shared damage rules, enchantments and hit handling still apply.

## Original identity and provenance

![Actual released Purity Shotgun texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/purity-shotgun-original-preview.png)

Keep the compact charcoal body, saturated blue swept plates, cyan inset bands and angular blue rear grip. These anchors distinguish the upgrade from a generic tactical shotgun. Engraved armor, crystal-like microdetail and articulated plates are new visual interpretations.

The verified **Fungal Upgrade Kit recipe** establishes upgrade lineage. It does not establish an official maker, a specific biome origin, a sacred purification story or literal fungal biology. Any such additional narrative needs its own source or must be labeled new project lore.

## Illustrated upgrade tutorial

| Input weapon | Upgrade kit | Result |
|---|---|---|
| ![Destruction Shotgun](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/destruction-shotgun-original-preview.png) | ![Fungal Upgrade Kit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-fungal-upgrade-kit-sprite.png) | ![Purity Shotgun](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/purity-shotgun-original-preview.png) |
| Destruction Shotgun | Fungal Upgrade Kit | Purity Shotgun |

1. Obtain the input weapon using the [Destruction Shotgun infusion recipe](Destruction-Shotgun-Weapon-Profile).
2. Obtain a Fungal Upgrade Kit. Its acquisition route is separate from this recipe and must be checked for your pack/version.
3. Follow the [Divine Station upgrade guide](Divine-Station-Weapon-Upgrades-1.20.1) for the shipped `aoa3:upgrade_kit` system. This is not an ordinary crafting-grid recipe.
4. Before committing a valuable customized weapon, verify preservation of enchantments, names, durability and new project attachments in that version. This profile does not promise untested data transfer.

Images above are released textures enlarged with nearest-neighbor sampling. The source recipe is `data/aoa3/recipes/upgrade_kit_purity_shotgun.json`.

## Revised concept and QA notes

![Purity Shotgun concept, not in-game](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/purity-shotgun-concept-v2.png)

The first draft invented recipe icons and used a flat sprite where a comparable 3D material option was needed. The revised sheet removes the misleading icons and compares two 3D treatments. Its small sprite-inspired illustration is generated reference art; only the extracted texture above is the actual original.

The blue flash, pellet trails, armor inspection and mushroom charm are proposals. The charm is not a recipe ingredient. Grip reach, trigger clearance, muzzle spacing, animation collision and first-person framing remain unaccepted until modeled and tested. Cyan effects do not add energy damage or an explosion to the original behavior.

## Full feature plan

- **Firing:** authoritative three-pellet shot; restrained flash and a readable, optional accent for the existing shared boost. No random gameplay decisions in rendering.
- **Projectiles and impacts:** distinguish muzzle flash, in-flight trail, impact sparks, surface dust and decals. Capture actual original flight/impact footage before final comparison acceptance.
- **Inspection:** blue plates lift slightly and reseat with clearance for hands, sight and charms. Interruptions return cleanly without firing, rerolling or consuming ammunition.
- **Attachment families:** compact optic, protected muzzle, alternate grip/handling pieces, removable armor treatment and optional decorative mushroom charm. A precision/scatter conversion must declare its changed pellet count, damage, cost and recoil rather than silently replacing original mode.
- **Craftable variants:** preserve the original upgrade route; add independently balanced precision and wider-spread variants only with visible parts and corresponding behavior. Extra emitters must have explicit gameplay rules.
- **Customization:** gameplay-earned functional charms; skins; static, animated and emissive stickers; emblems; optional projectile, tracer, impact and finisher effects. Separate cosmetic presets from server-authoritative bonuses.
- **Reload:** optional presentation according to actual ammo mode; no mandatory magazine timer added to original mode. Reload, inspect and interruption clips require separate ownership and collision checks.
- **Material choices:** Minecraft/TaCZ-fitting and higher-detail treatments with the same identity, plus reduced-effects settings. Avoid continuous idle particle or shader costs.
- **Performance:** reuse pooled effects, cap burst emissions and decals, use LODs and profile dense combat. No zero-cost claim before measurement.

## Required acceptance evidence

- [ ] Actual original projectile flight and impact captured in the pinned game build.
- [ ] Source roll frequency and shared-pellet behavior verified in-game.
- [ ] Concept-to-model silhouette, blue/cyan palette and material comparison approved.
- [ ] Hand reach, trigger guard, complete animation sweeps and attachment clearance pass.
- [ ] First-/third-person, interrupted inspect/reload and multiplayer behavior pass.
- [ ] Both visual treatments and all customization/effect families have explicit implementation status.
- [ ] Native TaCZ export, integration and representative performance measurements pass.

[Complete weapon standard](Weapon-Completeness-Standard) · [Weapon gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html) · [Machine-readable source evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/purity-shotgun-source-evidence.json)
