# Maul inputs and effect routing — Minecraft 1.20.1

**Pinned scope:** AoA 3.7.1 for Minecraft 1.20.1. Five registered mauls. This is source/bytecode review, not a native gameplay acceptance or a replacement for the separate historical 1.12.2 page. AoA remains credited to Tslat and contributors.

## Constructor inputs

| Registered ID | Attack-damage addition | Base knockback addition | Durability |
|---|---:|---:|---:|
| aoa3:coralstone_maul | 26.5 | 8.5 | 1600 |
| aoa3:crystal_maul | 23.5 | 7.2 | 1400 |
| aoa3:electron_maul | 25 | 2.5 | 1500 |
| aoa3:horizon_maul | 23 | 7 | 1300 |
| aoa3:vulcammer_maul | 28 | 8.2 | 1750 |

Damage and knockback here are attribute additions, not guaranteed final damage or travel distance. All five use AttackSpeed.THIRD, including the symbol read in the Coralstone registry factory. In the inspected AttackSpeed implementation, THIRD is based on the literal 0.33 rather than the exact fraction 1/3. Combining its modifier with an otherwise unmodified vanilla player attack-speed base of 4 gives approximately 0.528 attacks/second; buffs, attributes and actual cooldown behavior are separate.

## Shared input and ownership contract

- Main-hand defaults add attack damage, attack speed, knockback and +0.5 entity reach. The reach addition is not block reach and is not a measured total interaction distance.
- Left-click captures the player attack-strength scale into the NORTH volatile-capability slot and reapplies knockback scaled by that value. It returns false, leaving normal attack processing in place.
- On the hurt-enemy path, the captured cooldown is passed to the specialized effect, the original durability helper runs, and the full base knockback modifier is restored. A cosmetic renderer must not duplicate these calls.
- The class reports BLOCK as its use animation, but that enum alone does not implement a shield-like right-click block action. No such active-use implementation is declared by these inspected maul classes.
- Shield-disable eligibility returns true. This is not evidence that every target shield is disabled regardless of the surrounding combat rules.
- Nonzero-hardness mining on the server requests 1 durability for the exact STONE sound type and 2 otherwise. Creative block-attack eligibility is false. Enchantability is 8; looting and knockback are explicitly allowed in addition to the superclass rule.

## Per-weapon effects

### Coralstone Maul

Uses BaseMaul directly in the inspected registry. No specialized effect override is introduced by its factory. Preserve its constructor inputs and the shared input/attribute contract.

### Crystal Maul

Its living-target effect requests Slowness for 40 ticks with amplifier 1 (Slowness II). This override does not test the captured attack cooldown before requesting the effect. Do not incorrectly add a full-charge-only gate. Effect immunities and actual application still require native testing.

### Horizon Maul

Levitation is requested for 35 ticks with amplifier 0 only for a living target, an exact captured cooldown of 1.0, and a target that passes the special-attack immunity check. Near-full charge is not the same branch as exact full charge.

### Electron Maul

Electron uses a separate unkeyed volatile capability for a spirit-derived knockback multiplier; do not confuse it with the NORTH attack-cooldown slot. Every 10 world ticks, its selected-item branch can refresh the multiplier to 1 + currentSpirit / maxSpirit. Its main-hand attribute query uses base knockback times that stored multiplier, with zero falling back to one.

The special effect tests the stored multiplier against >0.75, not the attackCooldown argument and not “more than 75% spirit.” It requests lightning with both boolean flags false. The inspected lightning helper sets visual-only for non-destructive lightning and disables fire for the false fire flag; do not invent extra lightning damage from the visual.

For a server-player attacker, the effect requests consumption of the current spirit amount. There are direct server-level/server-player casts in the lightning branch before the later guarded spirit-consumption branch. Non-player, stale-capability, hand-switch and client/server routing must be tested rather than assumed safe. Do not alter gameplay while adding cosmetic motion.

### Vulcammer Maul

Its explosion branch requires captured attackCooldown >0.85, not >=0.85. The requested explosion is at the midpoint between attacker and target, with power input 2. The destructive-weapon-physics rule selects BLOCK versus NONE interaction and the helper boolean. When world damage is disabled, the additional loop sets hostile living entities within the target bounding box inflated by 2 on fire for 3 seconds. This region is not a spherical radius guarantee, and the helper power is not a fixed measured damage radius.

## Native acceptance still required

- Test all five with AoA and TaCZ loaded together, preserving existing combat-input ownership.
- Check low, boundary and full attack charge, repeated strikes, miss/recovery, both hands and switching to/from TaCZ.
- Verify effect immunity, spirit refresh/consumption, shield behavior, attribute cleanup, durability, server authority and multiplayer synchronization.
- For Vulcammer, test both destructive-physics settings in an isolated backed-up world; preserve protection behavior.
- Keep visuals, animation and sound tied to actual accepted original events without duplicate damage, resource consumption or explosions.

## Evidence

- [BaseMaul pinned source](https://raw.githubusercontent.com/Tslat/Advent-Of-Ascension/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/maul/BaseMaul.java)
- [CrystalMaul pinned source](https://raw.githubusercontent.com/Tslat/Advent-Of-Ascension/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/maul/CrystalMaul.java)
- [ElectronMaul pinned source](https://raw.githubusercontent.com/Tslat/Advent-Of-Ascension/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/maul/ElectronMaul.java)
- [HorizonMaul pinned source](https://raw.githubusercontent.com/Tslat/Advent-Of-Ascension/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/maul/HorizonMaul.java)
- [VulcammerMaul pinned source](https://raw.githubusercontent.com/Tslat/Advent-Of-Ascension/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/maul/VulcammerMaul.java)
- Constructor/effect control flow was cross-checked against the locally inspected AoA 3.7.1 release bytecode. Source pin and release identity are distinct records; native behavior is not inferred from either.
- Historical behavior belongs in the existing [1.12.2 maul page](Maul-Inputs-Reach-and-Knockback-1.12.2), not silently merged into this lane.
