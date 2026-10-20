# Dual Sight · cyan diagonal and layered blue optic

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept. Not a playable upgraded weapon.**

## Released weapon

Dual Sight is a **Metal Slug sniper with SCOPE_4**. The inspected subclass selects its medium/long sniper sound and scope texture. It does not implement a unique impact effect, a second projectile or an alternate-fire toggle. The name and layered optic do not establish those mechanics.

| Released input | Value |
|---|---:|
| Damage input | 38.5 |
| Durability | 350 |
| Firing delay | 91 ticks, nominally 4.55 seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.042 |
| Ammunition | Metal Slug |
| Scope texture | SCOPE_4 |
| Firing sound | Medium sniper, long variant |

These are released configuration inputs, not measured damage after armor, enchantments or other modifiers. [Named source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/sniper/DualSight.java) · [Class hashes and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/dual-sight-released-evidence.json).

## Original appearance and infusion

![Original Dual Sight sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dual-sight-original-preview.png)

The recognizable features are the broad dark forward shape, gray inset, bright cyan diagonal center, layered blue optic and angular blue rear loop. Preserve those features through both Minecraft-fit and premium presentation modes. Blue Druse in the recipe supports the ingredient identity; it does not prove an undocumented creator, origin dimension or energy source.

![Dual Sight infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dual-sight-infusion.webp)

Use **Sniper Frame** as the base. The six infusion slots contain **two Blue Druse**, one Dense Rock, **two separate quartz-gem-tag ingredients**, and one iron-ingot-tag ingredient. Do not collapse duplicate ingredient slots. Tag icons show example members. The diagram is reconstructed from the recipe, not a native crafting capture. [Infusion Table guide](Infusion-Table-Crafting-1.20.1).

## Concept and visual QA

![Revised Dual Sight concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dual-sight-concept-v2.png)

The proposed graphite/blue body keeps the cyan diagonal and rear loop prominent. The first pass omitted a complete trigger guard; the revised sheet adds a closed guard in both views while retaining the grip and trigger size. [Earlier concept, retained for comparison](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/dual-sight-concept-v1.png).

This is still a partial artistic study. View consistency, stock/grip hand clearance, aim alignment, actual meshes, textures, moving parts and native presentation remain unaccepted. A painted blue lens is not a replacement implementation of SCOPE_4.

## Full feature direction

- **Materials:** faithful low-resolution/world-fit textures and premium materials; controlled edge detail, UVs, distance readability and cost limits.
- **Optic choices:** original scope presentation by default, optional alternate housings and separately designed secondary sight behavior. Never infer double shots from the name.
- **Modules:** cyan shroud variants, loop-stock styles, grip/handling parts, earned charms and suppressor-like fantasy variants with declared tradeoffs and compatible mount points.
- **Optional conversions:** a focused cyan pulse or split visual discharge may be explored as a new opt-in module. Resource use, projectile count and damage changes must be explicit and balanced.
- **Animations:** equip, idle, aim, fire, recovery, movement, optional reload and inspection; proper hand room, interruption recovery and attachment clearance.
- **Feedback:** baseline flight/impact capture; proposed muzzle, tracer, projectile, decal and material-impact variants; confirmed-kill finishers and reduced-effects controls.
- **Customization:** skins, glowing/animated stickers, personal emblems, earned charms, named builds, recipes, reversible salvage, transferable effects and migration.
- **Integration:** multiplayer authority, TaCZ/turrets, modded targets, resource conservation, startup cost and equivalent-scene frame-time/memory tests.

## Acceptance gates

- [ ] Capture original in-game SCOPE_4, projectile, sound and impact
- [ ] Verify the six-slot infusion in the exact supported build
- [ ] Complete attachment, conversion, inspect and effect concept sheets
- [ ] Model both presentation modes and validate hands, aim and every moving pose
- [ ] Implement native animation, effects, compatibility and saved-build migration
- [ ] Measure performance and reduced-effects behavior without silently removing features

[Armory](Weapon-Overhaul) · [Completeness standard](Weapon-Completeness-Standard)

Original identity/assets: Tslat and contributors. New visual/mechanical proposals are distinct from released AoA behavior.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
