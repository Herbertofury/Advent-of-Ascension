# Apoco Rifle — sustained explosive discharge

**AoA 3.7.1 / Minecraft 1.20.1 baseline. Source-verified identity and new concept exploration; no accepted native upgrade.**

Apoco Rifle is a distinct weapon from [Apoco Assault Rifle](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Assault-Rifle-Weapon-Profile). Its released upgrade recipe starts with **Discharge Rifle**, and it uses **Discharge Capsules**. Preserve those distinctions when building attachments, effects and progression.

## What it does

The released Apoco Rifle inherits automatic fire and creates a `DischargeShotEntity`. Its direct-hit path uses the shared gun damage handling, followed by the projectile's explosion helper with a strength input of **1.8**. A block hit also requests that projectile explosion.

Unlike Discharge Shotgun, this class does not add a separate weapon-specific 2.5-strength explosion. Sharing a projectile class does not make their full attack behavior identical. Final damage depends on the native damage/explosion paths, enchantments, immunity and events; neither 2.5 nor 1.8 is a guaranteed total-damage figure.

| Released property | Verified value or boundary |
|---|---|
| ID | `aoa3:apoco_rifle` |
| Damage constructor input | 2.5 |
| Durability constructor input | 5,960 |
| Firing delay | 6 ticks; nominally 0.3 seconds at 20 TPS |
| Firing mode | Inherited automatic fire |
| Ammunition | Discharge Capsule |
| Projectile | DischargeShotEntity |
| Projectile age parameter | 120; not a measured range or exact expiry guarantee |
| Damage multiplier / piercing inputs | 1 / 0 |
| Gravity | Inherited zero-gravity return |
| Stored recoil input | 1 |
| Effective recoil caveat | Inherited modifier getter returns 0.35; the constructor input is not camera degrees |
| Firing sound | ITEM_GUN_PLASMA_GUN_FIRE |

## Original identity and provenance

![Actual released Apoco Rifle sprite, nearest-neighbor enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-rifle-original-preview.png)

The original sprite has a red upper mass, pale upper markings, dark olive/black lower structure and bright lime accents. Those colors and its compact silhouette should remain recognizable.

The packaged upgrade recipe specifies **Discharge Rifle + Apoco Upgrade Kit → Apoco Rifle**. The kit appears in the packaged `worlds/vox_ponds.json` loot table. That supports a source association with Vox Ponds; it does not establish current obtainability, an active dimension, a named maker or official mushroom/root construction lore. The fungal and root-like materials in the following concepts are explicitly new art interpretation.

[Exact upgrade recipe record](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-rifle-released-evidence.json) · [Version-aware recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=aoa3%3Aapoco_rifle).

## Refined premium concept

![Refined Apoco Rifle concept with coherent left-facing emitter and rear grip](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-rifle-concept-v2.png)

The refined concept retains the red, ivory, olive and lime identity, while making the emitter, rear grip and layered shell easier to read. It remains a drawing: hand clearance, hidden geometry, moving shell envelopes and native presentation are unverified. The inset is an emitter detail, not proof of a complete inspection animation.

[Earlier concept and effects exploration retained](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-rifle-concept-v1.png). Its ambiguous front/rear and grip layout was rejected as a modeling target. Text about ancient power in that exploration is invented concept flavor, not original lore.

## Attachment, progression and feedback direction

- **Pulse emitter:** preserve the recognizable capsule-discharge identity, with short energetic pulses and bounded cosmetic sparks.
- **Focus emitter:** a visibly narrower alternate assembly with explicitly declared handling/projectile changes. Its illustrated extended reach is a proposal, not an existing ability.
- **Chain emitter:** a separate beam/linked-energy branch requiring its own server-side target, cost and damage rules. It cannot silently replace baseline explosive shots.
- **Inspection shell:** a seated outer petal opens to reveal the fictional energy core, then returns exactly to its ready pose. Inspection must never create damaging projectiles or consume ammunition.
- **Handling and sights:** comfortable grip options, recoil/handling modules and readable sight choices. Avoid a decorative spine or leaf crossing the aim line or hand envelope.
- **Earned charms and effect modules:** explicit progression rewards with declared bonuses, compatible saved builds and dismantling rules. Cosmetic and functional contributions remain separately testable.
- **Presentation profiles:** both Minecraft-fit materials and a richer concept-faithful option. Preserve original gameplay unless the player explicitly selects a functional upgrade.
- **Skins and stickers:** static, animated and emissive decals; custom emblems; readable tracer/projectile, impact and finisher choices. Cosmetics cannot conceal collision, change damage silently or overwhelm combat readability.
- **Reloading:** optional presentation appropriate to the selected resource model. Preserve capsule consumption and do not impose conventional magazines by default.

## Original projectile versus proposed effects

[Actual packaged Discharge Shot texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-rifle-projectile-texture.png) is retained as source evidence. The red plasma flight and dramatic debris burst in concept v1 are proposals. A texture file is not an in-game capture; original projectile flight, impact, lighting and timing still need exact-version recordings.

World damage must respect the existing permission/game-rule path. Decorative debris must not destroy blocks, and repeated render passes must not multiply trail emissions.

## Actual generated mesh review

[Six rendered views and the complete first reconstruction review](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Apoco-Rifle-Generated-Mesh-Review.md) show the exported 56,328-triangle reference. Its broad silhouette is closer to the concept, but it loses fine rootwork and lime details, remains a fused mesh and has 50 non-manifold edges after exact-position welding. It is not an accepted weapon. Concept-projected colors were also tested and rejected because they visibly misalign.

![Actual generated Apoco Rifle reference, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-rifle-trellis-rear.png)

[Subsequent geometry and UV repair](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Apoco-Rifle-Mesh-Repair.md) removes the detected non-manifold edges and collapsed UVs while preserving the generated reference silhouette. Final concept fidelity, part ownership and native acceptance remain open.

## Completion gates

- [ ] Native baseline capture: firing cadence, direct hit, explosion, ammo, flight and block/entity impacts.
- [ ] Concept-faithful editable model, textures, comfortable hands and both presentation profiles.
- [ ] Equip, idle, fire, recovery, inspection and optional reload/recharge with interruption-safe transitions.
- [ ] Functional attachment, dismantling, charm, skin, sticker and effect systems with saved-build compatibility.
- [ ] Original-versus-upgraded projectile, muzzle, trail, impact, decal and finisher comparisons.
- [ ] Native TaCZ/AoA event binding, multiplayer, optional-mod compatibility and equivalent-work performance evidence.

[Read-only audit, concept prompts and review notes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/apoco-rifle-source-and-concept-study-v1.zip) · [Full weapon requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).

Original AoA identity and assets: Tslat and contributors. New concepts: original project explorations generated with the built-in image tool. No native upgraded weapon acceptance is implied.

## Higher-resolution trial and exported-mesh QA

[Read the completed 1024 trial and repair review](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Apoco-Rifle-High-Resolution-Review.md). Six actual offline views exposed a wrong muzzle direction and missing lime details. The generated mesh had 225 non-manifold edges; the first cap attempt was rejected after Blender import exposed three duplicated isolated triangles. The corrected reference removes only those three tiny disconnected faces. It retains 119,994 triangles through Blender import and reexport, with zero exact-position boundary/non-manifold edges and no preflight duplicate/degenerate/collapsed-UV issues. Diagnostic issues now fail the QA gate and command exit status. Art, moving-part, hand, material and native acceptance remain open. Higher resolution alone did not solve concept fidelity.
