# Nethengeic Wither: read the aura before choosing your weapon

[Open normal stats and illustrated loot](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3%3Anethengeic_wither) · [Boss entry and token preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) · [Trophies and elite encounters](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trophies-Gold-Crafting-and-Elite-Encounters-1.21.1)

![Nethengeic Wither aura and phase decision guide](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/nethengeic-wither-aura-guide-1.21.1.webp)

**Scope:** the normal encounter in Minecraft 1.21.1 / AoA 3.7.16.1. Selected released methods, damage tags and pinned source support the mechanics below. Tactical advice is an inference to test in actual play; elite and older encounters are not assumed equivalent.

## Prepare two ways to deal damage

The normal released builder specifies **420 maximum health, 6 base projectile damage and 1 knockback resistance**, plus flying movement. Terrain and equipment matter: keep space to see the heads and reposition, and bring sufficient supplies for an airborne fight. A static portrait is not a guarantee of actual flight or collision behavior in a restored build.

Most importantly, do not rely exclusively on an energy weapon. During the flame aura, an energy-tagged damage source can heal the boss instead of damaging it. Carry a suitable alternative and observe what your attacks actually do.

## Aura off versus aura on

| Situation | Inspected damage branch | Practical response to test |
|---|---|---|
| Aura off | Damage proceeds to the superclass implementation. | Use the opening while watching the heads, projectiles and positioning. This is not a promise that every source bypasses other immunities. |
| Aura on, melee-classified hit | A living direct attacker receives a 5-damage fire-recoil attempt, additional burning and a Nethengeic Curse effect; the boss's ordinary damage processing still follows. | Avoid blindly trading melee hits during the aura. Reposition or use a different suitable attack. |
| Aura on, energy-tagged hit that did not enter the melee branch | The boss calls `heal(amount)` and returns false from this damage handler. | Stop feeding it energy damage. Wait for the aura to end or change damage type. |
| Aura on, another damage classification | The ordinary superclass damage path follows. | An alternative can avoid this specific energy-healing branch, but it still needs normal damage and compatibility checks. |

The melee test is evaluated **before** the energy test. A modded source classified as both follows the melee branch in this handler. Do not simplify the rule to “every tagged hit always heals.”

### What counts as energy?

The inspected helper tests the `aoa3:energy` damage-type tag. Its released JSON lists `aoa3:energy_projectile` and `aoa3:energy_effect` as optional entries. Active datapacks or mods can change the tag. A glowing projectile, a magic-looking item or the weapon's display name is not sufficient evidence of its damage classification.

Fire resistance also should not be described as complete protection from this fight: physical projectile damage, curse effects and other attack paths must be considered separately.

## Watch all the heads

The main AI supports ranged attacks, strafing when the aura is inactive, and movement toward its target while the aura is active outside the Fire Bomb state. Additional head activities can run alongside the main behavior, and duplicate target selection is allowed. In multiplayer, do not assume each head must choose a different player.

A projectile hit uses the ranged-damage attribute, applies extra burning after a successful hit and can apply Nethengeic Curse. While the entity is in the Fire Bomb state, this projectile damage value is multiplied by **1.5** before the damage helper. This does not turn the base attribute into guaranteed final health loss.

A projectile block impact follows an explosion path. Avoid treating a nearby wall as universally harmless cover without testing the actual explosion settings and arena.

## Flamethrower phase

The inspected Flamethrower behavior requires an active aura and a living target. Its configured run duration is randomly selected between 160 and 240 ticks; it ends if its target is absent or dead. On stopping, it returns to the fireball state, turns the aura off if needed and sets a special-attack cooldown.

The null-projectile damage path is distinct from ordinary fireballs: it makes a flamethrower damage attempt, with separate one-in-four checks for added burning and Wither. Avoid standing still just because a visible fireball has not arrived. Exact hit cadence, particle-to-hit correspondence and safe movement windows need runtime tests.

## The half-health Fire Bomb is conditional

At the unmodified 420 maximum health, half health is **210**. Fire Bomb can become eligible at or below that threshold, but the inspected start condition also requires:

- The one-time `doneFireBomb` flag is still false.
- The aura is currently off.
- There is a living attack target.
- The surrounding behavior scheduler and cooldown permit activation.

It is therefore misleading to promise that crossing 210 immediately starts a fixed animation. Modifiers to maximum health also move the numerical threshold.

The configured phase duration is 280 ticks. Its update logic enables the aura after running time reaches 20 and repeatedly prepares and launches rings of physical fireballs at several heights. Do not count on a single horizontal line or a permanently safe layer. When the phase stops, remaining prepared projectiles are launched, the used-phase flag is set and the aura is switched off if still active.

**Practical response to test:** preserve room and healing before half health, keep watching the whole projectile pattern, and do not rush into the boss the instant the main phase animation seems to end. Existing side-head attacks and the final prepared projectiles still matter.

## Restoration findings that need targeted tests

Two details deserve explicit implementation acceptance rather than silent assumptions:

1. **Side-head target mismatch.** The left-head activation's pinned start condition checks the second-target memory, but its released fireball activation method reads the third-target memory. The right activation also reads the third target. Test two distinct targets, a missing third target and synchronized head orientation before deciding on a repair. This is a verified code mismatch, not a reproduced multiplayer failure.
2. **Phase history after reload.** The released load method marks Fire Bomb as already done whenever restored health is at or below half maximum. That reconstructs history from health rather than demonstrating that the phase actually ran. Test saving before and after phase activation, healing above half and reloading; preserve encounter state without enabling repeated bursts or silently suppressing an unplayed phase.

Neither issue is marked fixed in Enderloom by this documentation. The guide also does not certify damage-type compatibility, particle performance, flight stability or phase cleanup.

[Released method evidence, energy tag and ten independent branch cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/nethengeic-wither-combat-evidence-1.21.1.json) · [Pinned boss source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/nethengeic_wither/NethengeicWitherEntity.java) · [Damage classification helper](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/util/DamageUtil.java) · [Image provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/nethengeic-wither-art-evidence-1.21.1.json).

AoA artwork and mechanics: Tslat and contributors. Original independent diagram and explanations; no game screenshot or runtime certification is implied.
