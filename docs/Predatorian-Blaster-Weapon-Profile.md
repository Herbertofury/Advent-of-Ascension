# Predatorian Blaster: bone cannon and withering lineage

**AoA 3.7.1 / Minecraft 1.20.1. Released-source study and concept candidate; no native upgrade accepted.**

[Ghast Blaster predecessor](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ghast-Blaster-Weapon-Profile) · [Full weapon standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard)

## What it does

Predatorian Blaster is the Predator Upgrade Kit evolution of Ghast Blaster. Its inspected class creates a **Heavy Bone Cannonball**, rather than Ghast Blaster’s heavy shadow projectile. The conditional living-target impact hook retains the withering effect. Preserve that resource, projectile and upgrade identity when building the new presentation.

| Released input | Value / boundary |
|---|---|
| Registry ID | `aoa3:predatorian_blaster` |
| Damage constructor input | 23.5; not guaranteed final damage |
| Durability constructor input | 845 |
| Fire delay | 28 ticks, nominally 1.4 seconds at 20 TPS |
| Constructor recoil | 0.175; not camera degrees |
| Ammunition | Cannonball inherited from BaseCannon |
| Projectile | HeavyBoneCannonballEntity |
| Projectile constructor inputs | Age 120, damage multiplier 1, piercing 0 |
| Gravity return | 0.1 |
| Wither-related inputs | Duration 100, EffectBuilder level argument 2; argument recorded without assuming amplifier semantics |
| Firing sound | ITEM_LIGHT_CANNON_FIRE |

BaseCannon dispatches the weapon impact hook after an accepted heavy hit. The weapon additionally restricts its effect to living targets. Exact final damage, duration display, immunity, enchantment and mod interactions require native tests.

## Original appearance and provenance

![Actual released sprite, nearest-neighbor enlargement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predatorian-blaster-original-preview.png)

The source sprite is compact: a charcoal front barrel, irregular pale olive/gray outer bands, two yellow-lime central accents and a dark angled rear grip. These landmarks are the design anchor. Bone-like armor and predatory talons in the new concept are visual interpretations, not evidence of an official maker or crafting material. No dimension-of-origin claim is established by this study.

### Released upgrade recipe

**Ghast Blaster + Predator Upgrade Kit → Predatorian Blaster**, using the released `aoa3:upgrade_kit` recipe type. This is not a vanilla crafting-grid recipe. Ingredient acquisition and the exact upgrade interaction should be shown with native captures before the tutorial is marked complete.

## New concept candidate

![Original-inspired Predatorian Blaster concept, not an in-game render](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predatorian-blaster-concept-v1.png)

The sheet explores a black recessed cannon under pale olive/bone armor, paired yellow energy nodes, bounded dark projectile wisps and a brief rune impact. The lower-middle shape needs explicit grip/guard and hand-fit refinement before modeling approval. The original is more compact than the enlarged concept: compare normalized silhouette and proportions before committing geometry. The sheet is a candidate, not a finished or owner-approved asset.

The proposed ground-fracture effect is visual language only. It must not silently introduce block destruction, area damage or stronger Wither. Any gameplay modifier needs a named attachment, visible values, resource cost and server-authoritative implementation.

## Full feature direction

- **Firing:** one readable bone cannonball, a short controlled muzzle pulse, heavy return-to-ready recoil, subtle armor response and a short fading trail. The baseline does not acquire multiple projectiles just because ornament is added.
- **Attachments:** dorsal talon shroud, alternate bone sight, compact versus supported grip, resource-service housing and carefully budgeted impact/trail options. Every functional change needs actual stats and conflict rules.
- **Inspect:** paired nodes brighten in sequence, outer plates flex subtly, then return to their exact neutral pose. Cancellation must restore pose, ownership and effect state.
- **Resource service:** reloading remains optional. If enabled, the presentation must visibly make sense for Cannonball consumption and may not duplicate ammunition or create a magazine requirement silently.
- **Variants:** keep the canonical compact silhouette; alternate ornate or reinforced builds are separately craftable designs with their own concept and QA.
- **Customization:** both Minecraft-fit and concept-faithful texture treatments; earned charms, skins, stickers and emblems; separate muzzle, projectile, trail, impact, decal and finisher selections.
- **Dismantling:** retain donor identity and transfer limits for eligible effects. Withering modules need stacking, immunity, ownership and multiplayer tests.
- **Performance:** bounded particle lifetimes, pooled effects where measured useful, no repeated asset scans, sensible LOD and no unsupported promise of zero cost.

## Evidence and remaining acceptance

[Source-input receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predatorian-blaster-source-evidence.json). The release JAR hash and inspected class-output hashes are recorded. Game files are not redistributed here.

- [ ] Exact-version original flight, impact, resource and Wither captures.
- [ ] Concept revision with explicit grip, comfortable hands and source-proportion comparison.
- [ ] Editable model, deliberate textures, rig, moving parts and all required animations.
- [ ] Native material/render backend, real player arms and swept clearance.
- [ ] Projectile, effect, sound and attachment implementation with multiplayer authority.
- [ ] Crafting, upgrades, loot, save migration, optional mods and measured frame/startup budgets.

Original AoA identity and assets: Tslat and contributors. New concept generated with the built-in image tool and reviewed as a proposal. No accepted native weapon is implied.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
