# Carrot Cannon

**Original baseline: AoA 3.7.1 / Minecraft 1.20.1. Concept exploration; no native upgraded weapon accepted.**

## What the original actually does

Carrot Cannon is a non-fully-automatic heavy projectile weapon that uses vanilla Carrots as ammunition. It launches `CarrotBallEntity` with gravity, giving it an arcing projectile identity. Its renderer combines the carrot-shaped texture with orange/golden and flickering yellow spark effects. Preserve that playful botanical identity instead of treating it as a generic explosive launcher.

Its damage follows the shared cannon path. For a living target, that path adjusts the incoming raw multiplier by `1 + (armor × 1.5 + armorToughness × 0.5) / 100`, then calls the heavy-gun attack routine. Successful hits reach the shared knockback path and can disable a blocking player's shield. This is not a final-damage formula: native damage handling, modifiers, targets and other mods still affect the outcome.

The inspected Carrot Ball class does not add a custom impact override. No unique explosion or debuff implementation was found there. A new pulp burst, roots or terrain effect must be explicitly classified as cosmetic or as a declared functional upgrade.

## Exact-version inputs

| Property | Released input or behavior |
|---|---|
| ID | `aoa3:carrot_cannon` |
| Base damage input | 10 |
| Durability input | 520 |
| Delay field | 16 ticks; nominally 0.8 seconds at 20 TPS, not a measured firing cycle |
| Stored recoil argument | Approximately 0.4; not degrees or effective camera kick |
| Recoil caveat | Inherited BaseGun getter returns 0.35; shot calculation and client camera handling are separate |
| Ammo identity | `minecraft:carrot` |
| Projectile | `CarrotBallEntity` |
| Maximum-age input | 120; not an exact observed flight duration |
| Projectile damage-multiplier / piercing inputs | 1.0 / 0 |
| Gravity return | Approximately 0.1 |
| Full automatic | BaseCannon returns false |
| Fire sound | `ITEM_CARROT_CANNON_FIRE` |

## Original artwork

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-original-sprite.png" width="192" alt="Unmodified released Carrot Cannon sprite" />
<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-original-projectile.png" width="128" alt="Unmodified released Carrot Ball projectile texture" />

These are actual released asset bytes enlarged by the page layout. Original in-flight and impact captures still require the game. The concept below is proposed artwork, not an original-game screenshot.

## Infusion recipe and material provenance

The packaged infusion recipe takes a Cannon Frame as its input and lists six ingredient entries:

- One Small Orange Petal entry.
- One Rosid Root entry.
- One `forge:ingots/iron` entry.
- Two `forge:ingots/limonite` entries.
- One `forge:crops/carrot` entry.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-cannon_frame.png" width="48" alt="Cannon Frame" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-small_orange_petal.png" width="48" alt="Small Orange Petal" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-rosid_root.png" width="48" alt="Rosid Root" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-limonite_ingot.png" width="48" alt="Limonite Ingot" />

Use the infusion system, not an invented normal crafting-grid arrangement. The recipe's carrot tag is distinct from the gun's vanilla-Carrot ammo identity: a modded crop satisfying the recipe tag is not automatically accepted ammunition.

Rosid Root occurs in the packaged Gardencia world loot table; Small Orange Petal occurs in the Carrotop entity loot table. These are material associations, not a verified manufacturer, creator-intent statement or proof of active dimension availability in this target. Root-grown armor and leafy ornamentation are an artistic interpretation consistent with those materials and the original sprite.

[Versioned recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=aoa3%3Acarrot_cannon).

## Premium concept exploration

![Proposed Carrot Cannon redesign, attachments and effects](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-concept-v1.png)

Keep the orange/green botanical ends, central metal structure and root-like details recognizable. The first concept explores grown contours, layered metal collars, golden pollen accents and an earned charm. It is not owner-approved final art, a mechanical blueprint or an implemented weapon.

- **Focus collar:** a precision-oriented alternate front, with declared projectile/handling changes rather than a silent baseline rewrite.
- **Harvest crown:** visibly separated multishot channels. Projectile count, damage and carrot cost must agree with the server-resolved upgrade.
- **Rootwork grip and recoil housing:** comfortable hand space and readable recovery, without shrinking the trigger or allowing leaves to intersect moving parts.
- **Petalglass optic and earned charm:** optional aiming presentation and a Carrotop-inspired collectible; gameplay bonuses require explicit balance and provenance.
- **Inspection:** a restrained living-leaf/seed flourish that returns to the exact ready pose. Inspection cannot consume carrots, create damaging shots or leave cosmetic parts detached.
- **Projectile and impact:** retain a recognizable orange carrot silhouette and golden/yellow trail. Pulp, petals and soil-like flecks are cosmetic unless a separate declared upgrade changes the world.
- **Customization:** both Minecraft-fit and concept-faithful visual profiles, skins, stickers, charms, tracers, impact/decal and finisher variants remain in the full feature checklist.

## A real renderer performance concern

The released CarrotBallRenderer calls its base renderer, then loops eight times with two particle requests per iteration: **16 requests per render invocation**. One is SPARKLER with RGB 223,153,0 at Y+0.2; the other is FLICKERING_SPARKLER with the named yellow color at Y−0.2. This is a source-level count, not measured particles per second or a benchmark.

The upgraded effect should have a separate, per-projectile game-time emission policy so repeated render passes do not create duplicate trails. Preserve the orange/yellow character and evaluate perceived richness with native captures. Pooling, batching and bounded scheduling are candidates; none has yet proved a no-loss performance improvement for this weapon.

## Still required

Full concept-fidelity model and texture work; comfortable native hands; loading/inspection/firing interruption checks; projectile and impact capture; complete attachment, charm and cosmetic implementation; exact native ammo/resource behavior; crafting/progression; multiplayer/mod compatibility; measured frame/tick/memory costs. A concept image and released-file audit do not satisfy these gates.

[Released evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-released-evidence.json) · [Repeatable read-only audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/carrot-cannon-audit-v1.zip) · [Full weapon feature requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).

Original AoA identity/assets: Tslat and contributors. New concept: project exploration generated with the built-in image tool.
