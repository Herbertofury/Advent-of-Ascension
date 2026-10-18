# Baronator: complete weapon profile

**Documented original: AoA3.7.1 / Minecraft1.20.1.** Proposed upgrades are not yet measured in-game.

[Concept art](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Baronator-Art-Direction) · [Attachment gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Attachment-Concept-Gallery) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades)

## What it is and how it plays

Baronator is a compact red automatic gun that mixes ordinary bullet fire with occasional explosive surprise. Successful primary fire can also launch a grenade through a separate server-side one-in-five chance call. Its personality therefore includes both the primary bullet stream and the extra grenade; replacing everything with a generic double-barrel rifle would lose an important native behavior.

The base gun consumes Limonite Bullet ammunition and creates LimoniteBulletEntity. Normal bullet impact uses the gun damage path, including applicable enchantment and target rules. Baronator deliberately excludes its grenade from that ordinary bullet-damage override; the grenade has its own impact/explosion behavior. It is not simply another identical bullet with a different model.

The grenade drops more than the ordinary zero-gravity bullet path and triggers an AoA shrapnel explosion on block or entity impact. Its explosion/protection/terrain interactions deserve explicit testing in a forever-world pack. Do not portray that blast as only a harmless visual effect.

### Strengths, limitations and quirks

- A straightforward automatic primary attack gains an intermittent grenade follow-up.
- The bonus is chance-based, not a guaranteed grenade from every trigger event.
- Bullets and grenades have different impact paths and flight behavior.
- Ammunition, durability, recoil modifiers and target rules affect sustained use.
- Actual target DPS, practical range and full modpack interactions remain separate verification work.

## How to obtain it in this version

The released infusion_baronator recipe uses one Gun Frame as its input and one each of Grenade, an iron-ingot ingredient, a baronyte-ingot ingredient and a varsium-ingot ingredient. The three metals are tag ingredients: forge:ingots/iron, forge:ingots/baronyte and forge:ingots/varsium. Do not assume every visually similar ingot qualifies.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-gun_frame.png" width="48" alt="gun frame" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-baronyte_ingot.png" width="48" alt="baronyte ingot" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-varsium_ingot.png" width="48" alt="varsium ingot" />

Use the version's infusion recipe system, not a guessed normal crafting-grid arrangement. [Released recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-acquisition-evidence.json).

## Original artwork and projectile assets

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-original-sprite.png" width="192" alt="Original Baronator item sprite" />

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/original-limonite-projectile.png" width="96" alt="Original Limonite projectile texture" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/original-grenade-texture.png" width="128" alt="Original grenade texture sheet, not an assembled model" />

These are actual released-file assets. The Limonite projectile is registered with a camera-facing textured renderer in the inspected source. The grenade uses a model and texture; its texture sheet alone is not an in-game grenade screenshot.

## Original versus upgraded

| Property | Original evidence | Upgraded direction |
|---|---|---|
| Base damage input | 3.0 | Functional parts may increase per-projectile damage |
| Durability input | 2,480 | Explicit build policy and safe saved-item conversion |
| Firing-delay input | 5 ticks | Declared upgraded cadence, burst or volley modes |
| Nominal primary opportunities at20TPS | 4/second | Can increase with meaningful components; measure actual output |
| Recoil constructor input | Approximately0.95, not degrees | Weighty upper/lower recovery with configurable handling |
| Primary ammo | Limonite Bullet; native amount path includes Greed | Capacity, cost and conversion adapters must state their effects |
| Primary projectile | LimoniteBulletEntity | Improved presentation or deliberate projectile conversion |
| Primary gravity return | 0.0 in inherited path | Original-mode trajectory retained; upgrades can change it deliberately |
| Extra attack | Server-side oneInNChance(5) after successful primary fire | Preserve as baseline, then explicitly compose or modify through upgrades |
| Bonus grenade gravity return | Approximately0.075 | Declared projectile profile, not guessed from its appearance |
| Grenade explosion configuration | Radius3, penetration7, baseDamage5, blocksDropChance0.1 | These are configuration inputs, not measured damage/radius against every target; functional upgrades need their own records |
| Sound | Generic fire plus separate air-cannon cue for bonus branch | New original layered feedback, retaining recognizable two-part personality |

The primary arithmetic3×4=12 damage-input units/second excludes the grenade and all real hit/target behavior. It is not measured DPS. Explosion parameters likewise do not tell the whole damage or terrain outcome without the explosion implementation, settings and scene.

## Premium firing personality

![Baronator concept directions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-concept-exploration-v1.png)

The requested visual rhythm is upper barrel, then lower, with independent heavy recoil and a miniature-broadside feeling. Installed modules may intentionally increase shot count, damage, cadence and effects. The server-resolved build and the displayed barrels must agree. An intentionally stronger dual discharge is valid; an accidental repeated callback is not.

Preserve the original compact red identity while improving material separation, comfortable hand space, sound, flash and impact readability. Test each optional scope, shroud, damper, brace and effect core through actual animations and gameplay.

[Released baseline audit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-minigun-baseline-audit.json) · [Weapon profile requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard)

## Upgraded impact concept comparison

![Proposed upgraded projectile and impact language](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-impact-concepts-v2.png)

This is proposed upgraded VFX art, not an original-game capture. Compare it with the actual source assets and original impact values above. Discs, primary bullet hits and the separate Baronator grenade branch have distinct visual identities. Larger impact areas or terrain-changing behavior must correspond to a declared functional module and server rules; cosmetic debris is not proof that world blocks are destroyed.
