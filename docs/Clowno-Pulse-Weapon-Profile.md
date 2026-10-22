# Clowno-Pulse: three-flag cannon with a defensive beat

**AoA 3.7.1 / Minecraft 1.20.1. Source profile and revised concept candidate; no accepted native upgrade.**

[Pulse Cannon predecessor](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Pulse-Cannon-Weapon-Profile) · [Full weapon requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard)

## Current selected concept · 22 October 2026

![Clowno-Pulse selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clowno-pulse-clean-hero-concept-v5.png)

Clean three-pole red/silver hero, with obsolete stretching panels removed. Same paired split-open, vertically aligning three-aperture sight proposal; not implemented.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Aclowno_pulse). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

Dedicated supplemental studies (partial design candidates, not implemented features):

- [Focused appearance reference ONLY; lower side transition superseded](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-ribbon-focused-view-study-v2.png).
- [Geometry-guided three-pole alignment study; full weapon transition and cloth physics remain open](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-split-flag-alignment-study-v1.png).

## What it does

Clowno-Pulse fires the inherited cannonball and applies a separate firing-time push-away operation to nearby hostile living entities around the shooter. The released tooltip says it pushes nearby enemies away when firing. Its inspected hook queries the shooter's AABB inflated by 2.5 and calls the push-away helper with input 0.75, after the parent firing effects.

These are the same selected pulse inputs observed in Pulse Cannon. The upgrade's higher registered damage and durability do not prove a larger pulse area or stronger push. Preserve the difference between declared inputs and measured gameplay.

| Released input | Value / boundary |
|---|---|
| ID | `aoa3:clowno_pulse` |
| Damage constructor input | 35.5, versus Pulse Cannon's 26 |
| Durability constructor input | 845, versus 510 |
| Firing delay | 42 ticks, nominally 2.1 seconds at 20 TPS |
| Constructor recoil input | 0.09; not camera degrees |
| Resource | Cannonball inherited from BaseCannon |
| Projectile | Inherited CannonballEntity; age input 120, piercing 0 |
| Pulse query | Shooter AABB inflated by 2.5; hostile-mob predicate |
| Push helper input | 0.75; no measured displacement claim |
| Firing sound | ITEM_SHADOW_BLASTER_FIRE |

## Original identity and crafting lineage

![Actual released Clowno-Pulse sprite, nearest-neighbor enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clowno-pulse-original-preview.png)

The source sprite retains Pulse Cannon's rectangular frame but switches to pale gray, black, red and pink accents, with **three prominent red forked dorsal shapes**. Those three shapes are essential recognition landmarks. The owner-reviewed upgrade direction identifies these as red fabric flags on black poles, not rigid crowns. The poles stay in one longitudinal row along the barrel; this design requirement does not assert that the released sprite already contains cloth simulation.

**Pulse Cannon + Clown Upgrade Kit → Clowno-Pulse**, using the released upgrade-kit recipe type. Do not replace the recipe with an invented vanilla grid. Native interaction and ingredient-acquisition screenshots remain part of the tutorial work.

## Earlier preserved art: flag and ribbon-sight concept

![Clowno-Pulse concept candidate with three inline flags and a converging ribbon sight](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clowno-pulse-inline-ribbon-concept-v4.png)

[Compare the released original with the current concept](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Aclowno_pulse).

The red top elements are fabric flags on fixed black poles. Their anchors run front-to-back along the barrel, never side-by-side across it. The animated sight variant gathers the three tethered ribbons into one open aiming shape without relocating the poles. The aiming center must remain stable and unobstructed; cloth motion must not steer authoritative shots.

**Gameplay requirement, not an implemented feature:** the flag/ribbon attachment is equipped by default on eligible flagged clown weapons and can be removed. Explicit removal must persist across switching, re-equipping and save/reload. The off state needs a usable aiming view. A converging-ribbon sight is an optional animated variant; reduced-motion behavior and multiplayer synchronization require their own tests. Original cannonball, pulse, resources and damage are unchanged by this visual requirement.

**Status:** concept panels exist. Native cloth, attachment UI/persistence, networking, sight alignment, hand fit and performance acceptance remain open. A still-image storyboard is not animation or gameplay evidence.

### Earlier concept (v2), preserved

![Clowno-Pulse concept candidate with three crowns and a shooter-centered pulse sketch](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clowno-pulse-concept-v2.png)

The sheet keeps the three red prongs, rectangular muzzle, pale structural panels and pink energy strip. It explores playful crown articulation during inspect, an optional sight and earned jester charm. The small inset is explicitly a **source-inspired sketch**; the separate extracted sprite above is the actual source evidence.

The first draft mislabeled that sketch as an original sprite and depicted the defensive effect ambiguously near the projectile. The revision corrects both: its defensive ring is around a neutral holder. The ring is a presentation proposal, not proof that the source uses a spherical query. The exact native pulse volume, behavior and visual timing still need capture.


## Complete feature package

- **Firing:** single cannonball, brief rectangular red/pink muzzle flash, crisp heavy recoil and readable recovery; pulse visual triggers around the holder at the proper firing event.
- **Inspect:** three red flags flutter from fixed inline poles; the ribbon-sight transition returns cleanly to idle. Cloth roots, clearances and cancellation behavior must remain defined.
- **Audio:** preserve released firing identity while exploring optional short stage-like accents. Repeated fire must not become an overwhelming novelty sound loop.
- **Attachments:** alternate frame shrouds, angular sights, grips and pulse-effect modules. The jester charm needs attachment clearance, bounded motion, progression and an explicit gameplay benefit if functional.
- **Craftable variants:** keep the canonical three-flag layout. Any changed flag count, different emitter or major silhouette is a separately documented alternate with resolved stats.
- **Resource/service:** reloading remains optional for the selected Cannonball presentation, with conserved ammo and no hidden magazine requirement.
- **Customization:** Minecraft-fit and concept-faithful treatments; skins, static/animated/glowing stickers, custom emblems, charms and separate projectile, trail, impact, decal and finisher channels.
- **Dismantling:** donor effects require ownership, stacking, conflict, save and multiplayer rules. Decorative flag or ribbon animation cannot silently multiply damage or push events.

## Acceptance still required

1. Record original projectile, impact, pulse, resource use and exact-version native behavior.
2. Compare source and concept proportions; fit actual hands, trigger, guard and support geometry before accepting the model.
3. Complete rig, equip, idle, movement, aim, fire, recover, inspect and optional service animation with interruption tests.
4. Check pulse AABB corners, hostile classification, allies, bosses, knockback resistance and server authority.
5. Verify materials in the actual supported renderer, clearances, effect budgets, startup/frame times, save/load and optional mods.

[Source receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clowno-pulse-source-evidence.json). The original classes and recipes were inspected from the pinned release; no in-game acceptance is implied.

Original AoA identity and assets: Tslat and contributors. New concept generated with the built-in image tool; previous drafts retained in the authoring study.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](Effective-Recoil-Routing-1.20.1).
