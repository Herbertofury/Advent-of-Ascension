# Clown Cannon · a sinister green carnival cannon

[Weapon overhaul](Weapon-Overhaul) · [Concept gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html) · [All 50 cannons and recipe routes](Cannon-Progression-and-Recipes-1.20.1)

![Clown Cannon concept, proposed upgraded art](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cannon-concept-v2.png)

**Status:** released-source profile and first concept exploration. No accepted upgraded mesh, animation set or native playable release. This page covers **AoA 3.7.1 for Minecraft 1.20.1**; do not silently transfer its numbers to other releases.

## Original identity first

![Actual released item sprite, nearest-neighbour enlargement](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cannon-original-preview.png)

The actual sprite has a broad flared muzzle, dark charcoal body, grey framing and bright green segmented accents. The concept keeps that palette and overall silhouette, then proposes sculpted metalwork, star engraving and glowing inlays. Those added details are design proposals, not established canonical lore. The small generated sprite inset is labeled “SPRITE-INSPIRED STUDY”; the extracted image above is the authoritative asset. The [earlier concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cannon-concept-v1.png) is retained for history but its “ORIGINAL SPRITE” inset label was misleading and failed provenance QA. Revision 2 fixes that label within the image itself.

The weapon's play identity is a deliberate cannon shot with a chance to severely slow a living target. It is not established here as a confetti blaster, area explosion or poison weapon merely because of its name or green color.

## What the released weapon does

| Stored registration input | Value |
|---|---:|
| Damage parameter | 22.5 |
| Durability parameter | 570 |
| Firing delay | 32 ticks |
| Recoil parameter | approximately 0.18 |
| Ammunition | Cannonball |
| Automatic firing | No, inherited BaseCannon behavior |

These are constructor parameters, not a measured DPS or damage-per-hit guarantee. Shared cannon logic scales its attack input with target armor/toughness and delegates damage to the heavy-attack helper. Enchantments, attributes, immunity and other mods may change the result.

### What “stun” actually means here

The English tooltip describes a 20% chance to stun. The inspected implementation is narrower:

1. Shared cannon impact damage must return success.
2. The target must be a living entity.
3. RandomUtil.oneInNChance(5) must pass. The bundled random helper compares a random float with 1/5.
4. The effect helper requests **Movement Slowness for 30 ticks**, using **builder level 100**. The bundled EffectsLib subtracts one for Minecraft's amplifier, producing **amplifier 99**.

At 20 ticks per second, 30 ticks is nominally 1.5 seconds. This is an extreme movement-slowdown request, **not evidence of a general AI, attack, animation or action lock**. Potion-helper conditions and target behavior still matter. Do not promise every successful shot stuns, or that every creature becomes completely inert.

## Original projectile and feedback

![Actual released cannonball texture, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cannon-projectile-preview.png)

ClownBallEntity uses a 120-tick maximum-age argument, zero piercing value, damage multiplier 1 and gravity 0.1. Its renderer uses the ordinary dark cannonball texture. Each renderer invocation requests three green FLICKERING_SPARKLER particles and three white SPARKLER particles at the projectile position, with no added vertical offset.

These are render-invocation counts, not particles per game tick. That distinction matters when designing stable effects at different frame rates. The new sheet's large glowing orb and sweeping trail are proposed feedback, not a screenshot of original flight or impact. Original in-game flight/impact capture remains required.

## Acquisition and progression

The inspected release contains no explicit aoa3:clown_cannon reference in bundled data JSON, including the recipe/loot scan. This does **not** establish that it is unobtainable: code-generated, loot-function or external routes may exist. Acquisition investigation remains open, and no fabricated crafting recipe is supplied. The all-cannon guide keeps this gap visible.

## Proposed upgrade kit, to be designed and tested

- **Default carnival bell:** retain the recognizable flared muzzle and green/white trail; clear, short hit confirmation for the slowdown proc.
- **Ringmaster focus:** an alternate restrained magical focusing silhouette with a thinner projectile trail. Any gameplay change needs explicit stats and server authority.
- **Spotlight crown:** cosmetic aiming trim with readable ADS visibility, avoiding a bright obstruction over the target.
- **Verdant masquerade skin:** charcoal, lime and silver baseline, with optional darker weathered or polished finishes. Preserve a Minecraft-fitting texture option and the detailed concept-fidelity option.
- **Earned charms and decals:** small hanging carnival tokens, static/emissive/animated sticker options, placement zones kept clear of fingers, moving parts and sightlines.
- **Custom feedback:** selectable tracer, impact and defeat effects with bounded particle budgets and reduced-flash settings. A visual proc cue must not falsely indicate a slowdown the server rejected.

These are an unimplemented design backlog. Do not increase damage merely by installing a cosmetic component; gameplay-bearing attachments need matching visible changes, readable tradeoffs and balance tests.

## Animation and quality gates

- [ ] Fit the hand rig comfortably; validate finger, grip and guard clearance in idle, fire, aim, inspect and optional reload states.
- [ ] Build a faithful mesh and two texture treatments; compare matched views with the concept and original sprite.
- [ ] Author equip, idle, fire/recover, aim transition, inspect and optional reload animations, including interruption handling.
- [ ] Provide projectile, muzzle, tracer, impact, decal and optional defeat-effect concepts with explicit original-versus-proposed labels.
- [ ] Preserve non-reloading gameplay where the chosen resource system calls for it; never force a magazine system onto every AoA weapon.
- [ ] Verify exact acquisition routes and gameplay progression rather than inventing a drop table.
- [ ] Capture original projectile flight/impact in game and qualify upgraded behavior in the actual target modpack.
- [ ] Test server-authoritative chance/effect behavior, immunity, multiplayer synchronization, frame-rate-independent particles and performance budgets.

## Evidence

[Structured release evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clown-cannon-released-evidence.json) includes class hashes, registry factory and bundled library identities.

[Named ClownCannon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/ClownCannon.java) · [Named projectile source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/entity/projectile/cannon/ClownBallEntity.java)

Source inspection and concept art are evidence of research progress, not native acceptance.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
