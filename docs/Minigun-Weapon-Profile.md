# Minigun: complete weapon profile

**Documented original: AoA3.7.1 / Minecraft1.20.1.** Native upgraded gameplay and final balance remain untested.

[Concept art and attachments](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Minigun-Art-Direction) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades)

## What it is and how it plays

Minigun is the orange, steel-accented rapid-fire gun with a compact multi-barrel front and prominent round side detail. Its native behavior is a continuous automatic Limonite Bullet stream with a dedicated firing sound and a wind-down sound when the player releases use. Individual base hits are small; its identity comes from rapid repetition and sustained feedback rather than a huge single strike.

It inherits ordinary BaseGun ammunition and bullet creation. LimoniteBulletEntity follows the inherited zero-gravity bullet path and calls the gun's impact-damage logic on entity hits. The inspected Minigun class specializes sound and release feedback; it does not introduce a separate unique explosive impact override.

The original one-tick delay is the firing baseline. A rotating visual barrel cluster must not quietly add a mandatory startup delay to original mode. A deliberate functional attachment may change cadence, output or handling, with that change visible in the build's description and values.

### Strengths, limitations and quirks

- Rapid, sustained automatic fire and a recognizable release wind-down.
- Low per-projectile base input makes actual target handling especially important; raw arithmetic is not a damage benchmark.
- Continuous use consumes ammunition and durability; resource policies and enchantments must remain visible.
- Cosmetic rotation should remain phase-continuous during starts, stops and rapid retriggers.
- Useful range and performance in the full pack still need explicit verification.

## Where it comes from and original upgrade routes

The released Lelyetian Tower main chest-loot table includes Minigun. Both the tower bottom and top structure NBT files reference that table. This is a chance-based loot route, not a guaranteed weapon in every chest. The table has ten base rolls and weighted entries; luck and actual loot evaluation matter, so no unconditional drop percentage is claimed here.

Two native upgrade-kit recipes also use Minigun:

| Input and kit | Result |
|---|---|
| Minigun + <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-weapon_parts.png" width="48" alt="weapon parts" /> Weapon Parts | Megagun |
| Minigun + <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-predator_upgrade_kit.png" width="48" alt="predator upgrade kit" /> Predator Upgrade Kit | Predigun |

These are original AoA upgrade recipes, distinct from our new modular attachment system. Preserve their acquisition and saved-item semantics. [Exact loot, recipe and structure-reference evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-acquisition-evidence.json).

## Original artwork and projectile

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minigun-original-sprite.png" width="192" alt="Original Minigun item sprite" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/original-limonite-projectile.png" width="96" alt="Original Limonite projectile texture" />

Actual released-file images, not generated game screenshots. The inspected registration uses a camera-facing textured projectile renderer. Our six-tube rotor is a chosen premium visual interpretation of the sprite's multi-barrel front, not a native six-shot-per-tick claim.

## Original versus upgraded

| Property | Original evidence | Upgraded direction |
|---|---|---|
| Base damage input | 0.625 | Damage parts may genuinely raise it |
| Durability input | 2,680 | Explicit build policy; no lost item data |
| Firing-delay input | 1 tick | Increased/multiple output possible through declared upgrades |
| Nominal firing opportunities at20TPS | 20/second | Actual count follows the resolved functional build |
| Recoil constructor input | 1.5, not degrees | Handling/grip/brace parts can change the experience |
| Ammo | Limonite Bullet; Greed affects native requested amount | Capacity/efficiency/conversion parts need explicit resource behavior |
| Projectile | LimoniteBulletEntity | Improved appearance and supported functional variants |
| Gravity return | 0.0 in inherited bullet path | Original-mode behavior retained; modified paths declared |
| Projectile age input | 120 | Not a measured travel distance or exact visible duration |
| Impact | Inherited gun-damage path; no Minigun-specific explosion override found | Added status, area or secondary effects require named installed components |
| Sound | ITEM_GUN_MINIGUN_AUTOMATIC_FIRE; release uses MINIGUN_WINDDOWN | Rich original sound layering and phase-consistent visual feedback |

0.625×20=12.5 is only a raw damage-input-per-second arithmetic figure. It ignores misses, target mitigation, damage admission, enchantments and other rules. Publish measured native results separately.

## Premium visual and gameplay target

![Minigun concept directions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minigun-concept-exploration-v2.png)

Keep the orange/graphite/steel silhouette, round side medallion and rear striped detail. Add comfortable support grips, open bore corridors, purposeful material detail and satisfying rotary feedback. The first generated firing vignette showed several simultaneous flashes; the baseline art was corrected to one active muzzle at the illustrated instant. A future multishot/volley upgrade may intentionally change that behavior, but its visuals and actual admitted projectiles must agree.

[Eight Minigun attachment concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Minigun-Art-Direction) include a shroud, thermal mantle, optic, support grip, carrying frame, reserve drum, tracer module and cosmetic badge. Their generated shapes are not yet qualified physical fits.

[Released baseline audit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-minigun-baseline-audit.json) · [Weapon profile requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard)

## Upgraded impact concept comparison

![Proposed upgraded projectile and impact language](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-impact-concepts-v2.png)

This is proposed upgraded VFX art, not an original-game capture. Compare it with the actual source assets and original impact values above. Discs, primary bullet hits and the separate Baronator grenade branch have distinct visual identities. Larger impact areas or terrain-changing behavior must correspond to a declared functional module and server rules; cosmetic debris is not proof that world blocks are destroyed.


## Actual TaCZ reference: spin and inspect hooks

The default pack inside [TaCZ 1.1.8-hotfix2](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero/files/9037989) contains a dedicated Minigun Lua state machine. Its selected functions were executed unchanged with the release's embedded LuaJ libraries in an explicitly mocked context on Java 17 and 21. This is deeper than reading the animation names, but still not a native game session.

- The firing-spin update checks the elapsed-shot threshold only when its animation track is holding. It either starts another spin segment or requests a stop; the stop transition selects the winddown clip. Preserve the intent of finishing a rotation segment instead of snapping the rotor angle to zero.
- The test uses a 50 ms shot interval: elapsed values 149 and 150 restart the segment; 151 requests stop. A non-holding track issues no command in the tested update. Those are exact boundary fixtures, not a claim that every configuration fires at that interval.
- Inspect entry requests spin stop and hides the crosshair. Its exit hook restores the crosshair; shooting interruption stops the inspect animation and returns idle. The fixture checks these hook commands. It does not prove the engine always invokes exit correctly in every interruption path.
- The released context's current timestamp calls `System.currentTimeMillis`. Do not subtract a paused game-time value from this wall-clock timestamp. Our cosmetic adapter needs an explicit clock boundary and pause/rebase tests.

[Executed hook results and source hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/tacz-minigun-lua-hook-check.json) · [Original reproduction harness](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/tacz-minigun-lua-hook-check-tool-v1.zip)

The original source script and embedded runtime are extracted locally from the pinned JAR, not redistributed in the harness. Native track interpolation, rendered phase continuity, sounds, gameplay and actual hand motion remain unvalidated. AoA's native fire/resource contract must stay separate from this presentation reference.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
