# Vortex Blaster · force, not a conventional bullet

**Released baseline: Minecraft 1.20.1 / AoA 3.7.1. Upgrade status: concept exploration; no native upgraded weapon accepted.**

The Vortex Blaster is a Spirit-powered crowd-control weapon. Its released firing override gathers nearby living entities through an axis-aligned box query and applies scaled knockback. Its tooltip says “Creates a large pushing force.” The redesign should make that shove readable and satisfying while retaining the old silver/black flared-muzzle silhouette.

![Original source sprite, enlarged without smoothing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/vortex-blaster-original-sprite.png)

## Original contract

| Field | Pinned released value / meaning |
|---|---|
| Registry ID | `aoa3:vortex_blaster` |
| Stored base damage | 0.0; this override does not directly call a damage method |
| Durability | 2,870 |
| Stored firing delay | 1 tick; actual use, resource and server timing still govern firing |
| Base charge field | 1 tick through the constructor chain |
| Base Spirit cost | 130.0 before inherited modifiers/exemptions |
| Item ammunition | Not a conventional bullet-magazine contract |
| Knockback call | Strength 7.0, X/Y/Z ratios 1, 1, 1 |
| Sound | `ITEM_GRAVITY_BLASTER_FIRE` |
| Original flight projectile | None spawned in this firing override |

Zero stored damage does not mean harmless: displacement can lead to falls, hazards or other game interactions. Strength 7 is an input to a helper, not seven blocks of guaranteed travel.

### Targeting and compatibility caveats

The released method computes direction from yaw/pitch, then inflates the shooter's box with each signed direction component × 7 + 1. Do not describe this as a clean cone, sphere or seven-block ray. Negative components, all headings/pitches, target sizes, self-selection and occlusion need native tests. This method does not show an explicit ray/line-of-sight filter or shooter exclusion.

The knockback helper respects its Forge knockback event/cancellation, attacker attack-knockback and target resistance attributes, and a player eligibility check. It normalizes target-minus-attacker position, incorporates half the attacker's motion, scales by adjusted strength, and can add a small same-height grounded lift before setting motion. Preserve these interactions instead of replacing them with a universal fixed shove.

The legacy BaseBlaster call returns no ShotInfo from this override path, so the generic ShotInfo firing-effects branch is skipped while the firing sound path remains. New pressure rings shown below are **proposed presentation**, not evidence of an original rendered projectile.

### Acquisition

No matching string was found in shipped `data/**/*.json`, including recipes/loot data. This bounded scan does not establish that the weapon is unobtainable: Java-coded trades/drops and progression still require review. Do not invent a crafting recipe to fill the gap.

## Upgrade concept and attachment directions

![Vortex Blaster concept v2, not gameplay](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/vortex-blaster-concept-v2.png)

The revised concept keeps the broad bell muzzle, silver/charcoal bands, compact body and rear grip. The v1 trigger was too far from the grip; v2 moves it beside the grip with a smaller open guard. This is visual concept correction, not measured hand-rig clearance.

- **Repulsion pulse:** recessed concentric rings compress inward then release a readable expanding air ripple. Bind visuals to accepted gameplay events; no extra damage.
- **Focused impulse collar:** narrower visual aperture and a precise targeting proposal. Any actual targeting change requires its own rule/upgrade, cost and UI description.
- **Wide field ring:** larger ring assembly, broader distortion and slower settling. A wider real query would be a gameplay upgrade with tested caps, not an accidental result of a cosmetic mesh.
- **Stabilizer grip:** restrained recoil animation and handling option, without bypassing the source knockback hooks.
- **Inspect:** collar segments unlock briefly, a miniature pressure ripple forms inside the bell, then all rings settle before the weapon becomes usable. Avoid blocking the muzzle or passing through hands.
- **Optional recharge presentation:** Spirit remains the default resource. Do not add mandatory magazine reloading to an energy weapon solely because the TaCZ presentation supports it.

[Earlier v1 concept remains available](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/vortex-blaster-concept-v1.png).

## Acceptance gates

- [ ] Capture original use and displaced targets in the pinned game; label original flight projectile as not applicable rather than fabricating one.
- [ ] Verify all cardinal headings, diagonal angles, up/down aiming, obstruction, self-selection and resistant/immune targets.
- [ ] Preserve Spirit spending, durability, cooldown/use rules and Forge event behavior.
- [ ] Validate grip/trigger reach, glove and support-hand clearance, aim occlusion and attachment envelopes on an actual rig.
- [ ] Test interrupt/swap/death/reconnect for ring/inspect state and effect deduplication.
- [ ] Measure real server query cost and client distortion/particle cost; cap cosmetic work independently of gameplay.
- [ ] Validate the native model, sound, renderer, multiplayer and save contracts before upgrading status.

## Evidence

[Class hashes, values and limits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/vortex-blaster-source-evidence.json) · [Reproduction tool and exact concept prompts](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/vortex-blaster-study-tool-v1.zip) · [Official source comparison](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/content/item/weapon/blaster/VortexBlaster.java)

The source comparison is newer than the pinned release; released bytecode was independently inspected. Original mod and sprite credit: Tslat and AoA contributors. Generated concepts are design proposals, not borrowed COD assets or in-game captures.
