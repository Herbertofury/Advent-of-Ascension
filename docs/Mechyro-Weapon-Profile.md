# Mechyro: mechanical two-pellet shotgun

**AoA 3.7.1 / Minecraft 1.20.1. Source-grounded profile and concept candidate. No accepted native upgraded weapon.**

## What the original does

Mechyro is a non-automatic Spreadshot shotgun. Its released subclass only forwards constructor values into BaseShotgun; it does not add a unique gear-driven attack, energy core mechanic or special impact effect. The inherited firing loop spawns two LimoniteBulletEntity pellets. The separate projectile-factory method returns MetalSlugEntity for the shared firing path, so examining that factory alone would misidentify the loop-created pellets.

| Released field | Value and boundary |
|---|---|
| Registry ID | `aoa3:mechyro` |
| Stored damage input | 13; not guaranteed combined damage |
| Pellets | 2 |
| Ammunition | Spreadshot |
| Durability | 720 |
| Delay | 46 ticks, nominally 2.3 seconds at 20 TPS |
| Recoil input | Approximately 0.3; not measured camera degrees |
| Knockback input | Approximately 0.3; not measured displacement |
| Loop-created projectile | LimoniteBulletEntity, age input 4, multiplier 1, piercing 0 |
| Spread | `0.1 × pelletCount × (1 − 0.15 × FORM level)`; not a measured angle |

Ammo consumption, enchantments, collision/immunity behavior and final damage still require native tests. Two pellets must not be advertised as a guaranteed 26-damage hit.

## Actual appearance and identity

![Actual released Mechyro sprite, nearest-neighbor enlargement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mechyro-original-preview.png)

Preserve the low dark upper barrel, ochre/orange mechanical body, dark brown lower form and orange rear extension. Bronze enamel, exposed gears and a luminous core are proposed material/presentation interpretations. The original pixels do not establish those materials or a canonical manufacturer.

## Crafting and acquisition tutorial

1. The packaged Iro Crate block loot table lists Incomplete Mechyro among six incomplete mechanical weapons in a one-roll pool. Its non-Silk-Touch condition applies to that pool; a separate Silk Touch pool returns the crate itself. This is packaged-data evidence, not a verified current-world spawn route or drop-rate benchmark.
2. Combine **Incomplete Mechyro + Power Core + Mecha Gear** in the released shapeless crafting recipe. Each listed ingredient appears once. This is a standard shapeless recipe, not an infusion recipe.
3. The released upgrade-kit recipe combines **Mechyro + Abyssal Upgrade Kit → Abyssro**. See the [Abyssro profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Abyssro-Weapon-Profile) for the upgraded weapon's separate baseline and Abyss-associated kit evidence.

Do not infer an official maker or complete dimension-progression story from an Iro Crate filename alone. Exact biome/spawn access and ingredient acquisition still need version-specific world testing.

### Actual recipe-item images

These are the released item textures enlarged with nearest-neighbor sampling. They are not generated ingredient illustrations or 3D game captures.

| Incomplete Mechyro ×1 | Power Core ×1 | Mecha Gear ×1 | Result: Mechyro ×1 |
|---|---|---|---|
| ![Incomplete Mechyro](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-incomplete-mechyro-sprite.png) | ![Power Core](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-power-core-sprite.png) | ![Mecha Gear](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-mecha-gear-sprite.png) | ![Mechyro](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mechyro-original.png) |

Shapeless: no particular slot arrangement is required. The upgrade uses the actual Abyssal Upgrade Kit pictured below; the recipe type is AoA's upgrade-kit system, so it is not presented as another standard shapeless crafting recipe.

![Abyssal Upgrade Kit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-abyssal-upgrade-kit-sprite.png)

[Exact sprite provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mechyro-recipe-sprite-evidence.json)

## Source-inspired concept

![Mechyro concept candidate, revised grip and two-pellet wording](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mechyro-concept-v2.png)

The first draft obscured the graspable grip and used ambiguous “two shots” text. The second separates the grip from the decorative power module and says “two pellets per shot.” It remains a candidate: comfortable moving-hand clearance, support-hand position, proportions, source fidelity and texture implementation have not passed final review. The illustrated ingredients and effects are concepts, not extracted item renders or game captures.

Offer two visual treatments of the same coherent weapon: a restrained Minecraft/TaCZ-compatible material treatment and a highly detailed concept-fidelity treatment. Neither changes gameplay merely by changing texture resolution.

## Full presentation and customization requirements

- **Firing:** clear two-pellet feedback, readable recoil/recovery, bounded muzzle flash and optional tracer treatment. Preserve the original behavior preset until separately balanced upgrades are enabled.
- **Impacts and decals:** surface-aware sparks/dust, bounded lifetime and pooled particles. The pictured orange effects are proposals; do not replace source projectile captures with them.
- **Inspection:** optional decorative gear rotation and power-light response with interruptible transitions. No free firing, hidden reload or gameplay effect from inspection.
- **Attachments:** removable optic, visible core housing, muzzle treatments, handling/stock options, charm anchor and decal zones. Visible changes must match implemented behavior when they claim gameplay effects.
- **Alternate barrels:** proposed precision two-pellet module; separately balanced wider-scatter conversion; fictional gear-driven energy presentation. Document ammo/resource changes, pellet count, damage, spread and costs for each, rather than silently inheriting original values.
- **Customization:** skins, static/animated/emissive stickers, custom emblems, unlockable gameplay charms, optional projectile/tracer/impact and finisher effects. Keep readability, network authority and particle budgets explicit.
- **Animation set:** equip, idle, aim, fire, recovery, inspect and interrupts. Reload is optional and must only exist when the configured resource model supports it; avoid fabricating a magazine mechanic for the original Spreadshot preset.
- **Craftable variants:** separate recipes and item identities for major conversions; preserve original items and previous art.

## QA gates still open

Actual original projectile flight/impact captures; source-versus-upgrade comparison; original-compatible damage/resource tests; normal and slim player hands throughout every animation; trigger/guard and module clearance; attachment combinations; texture/UV/PBR export; native TaCZ/TML integration; multiplayer authority; LODs, startup and frame-time measurements. All native gates remain untested.

## Evidence

[Machine-readable source evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/mechyro-source-evidence.json) · [Versioned weapon baselines](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/conventional-weapon-baselines-1.20.1.json) · [Weapon concept gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
