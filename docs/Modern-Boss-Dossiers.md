# Modern Boss Dossiers

[Bosses and combat](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bosses-and-Combat) · [Visual atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Visual-Atlas)

## Source scope

These dossiers describe the pinned 1.21 source snapshot, with images separately rendered from the official 1.21.1 / 3.7.16.1 archive. Neither a class nor a resource proves that an encounter is obtainable or complete in the target Enderloom build. Base attributes below precede difficulty, player-count, effects and other runtime changes. Health numbers are raw health points, not hearts.

## Attribute ledger

| Entity class | Max health | Move speed | Melee | Ranged/projectile | Armour / toughness |
|---|---:|---:|---:|---:|---|
| [EliteKingBamBamBamEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/king_bambambam/EliteKingBamBamBamEntity.java) | 1510 | 0.2875f | — | 25 | 15, 30 |
| [KingBamBamBamEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/king_bambambam/KingBamBamBamEntity.java) | 740 | 0.2875f | — | 12 | 10, 30 |
| [EliteNethengeicWitherEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/nethengeic_wither/EliteNethengeicWitherEntity.java) | 950 | 0.33 | — | 30 | — |
| [NethengeicWitherEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/nethengeic_wither/NethengeicWitherEntity.java) | 420 | 0.31 | — | 6 | — |
| [EliteSkeletronEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/skeletron/EliteSkeletronEntity.java) | 600 | 0.315 | 30 | — | 15, 25 |
| [SkeletronEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/skeletron/SkeletronEntity.java) | 275 | 0.31 | 15 | — | 10, 10 |
| [EliteSmashEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/smash/EliteSmashEntity.java) | 600 | 0.315 | 30 | — | 15, 25 |
| [SmashEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/smash/SmashEntity.java) | 275 | 0.31 | 15 | — | 10, 10 |
| [EliteTyrosaurEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/tyrosaur/EliteTyrosaurEntity.java) | 1290 | 0.33f | 26 | — | 10, 15 |
| [TyrosaurEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/tyrosaur/TyrosaurEntity.java) | 635 | 0.2875f | 15 | — | 10, 15 |
| [WoundedTyrosaurEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/tyrosaur/WoundedTyrosaurEntity.java) | 635 | 0.2 | 15 | — | 10, 10 |

A dash means this specific builder call was not found in the inspected method; it does not mean zero damage or zero defence. Wounded Tyrosaur is a special related mob, not simply another full-health boss.

## Smash — stateful melee pressure

![Smash model showcase](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-smash.png)

The inspected class defines axe-swing, axe-slam and charge attack states. The normal Smash checks for health below 25% and enters an enraged state once. It applies persistent attack-damage, armour and toughness modifiers using total-multiplier operations, triggers its enrage animation/sound, and inserts a 100-tick attack cooldown memory. The raw modifier amounts are 0.95, 1.1 and 1.25 respectively; these are attribute-operation amounts, not direct replacement attribute values. Shield-disabling behavior is conditional on the attack state.

**Restoration tests:** synchronize the enraged flag; preserve one-time activation and modifier identity; save/reload mid-enrage without multiplying modifiers again; align hit windows, animation and ground-slam effects; test charge pathing and unreachable targets. The elite variant requires its own behavior and scaling tests.

## Nethengeic Wither — airborne attack selection

[Normal encounter field guide: aura damage choices, projectile phases and reload/targeting checks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Nethengeic-Wither-Combat-Field-Guide-1.21.1).

![Nethengeic Wither model showcase](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-nethengeic_wither.png)

The inspected normal/elite classes distinguish fireball, flamethrower and fire-bomb states, with aerial movement and target-selection behavior. A visual floating pose is not evidence that hover, strafing, projectile collision, fire damage or sound synchronization works.

**Restoration tests:** verify each state transition and projectile family; compare flight stability in enclosed and open terrain; preserve client/server targeting, damage and projectile lifetime; test fire-related protections rather than replacing difficult behavior with generic ranged attacks.

## King BamBamBam — summons and ranged phases

[Normal encounter field guide: intercept gold, control minions and read exhaustion](https://github.com/Herbertofury/Advent-of-Ascension/wiki/King-BamBamBam-Combat-Field-Guide-1.21.1).

![King BamBamBam model showcase](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-king_bambambam.png)

Normal source states include three summon states and fireballs. The elite source adds a fourth summon state. The base attribute declarations differ substantially between normal and elite versions; copied registry entries alone will not preserve the encounter.

**Restoration tests:** reconcile summon types and counts from each state implementation, spawn permissions, ownership/cleanup, attack cooldowns and multiplayer pressure. Confirm all summons and projectiles render and remain damageable.

## Tyrosaur and wounded conversion

![Tyrosaur resource showcase](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-tyrosaur.png)

The normal/elite Tyrosaur logic includes melee behavior, roar and earthquake behavior. Its multipart geometry and hitboxes require separate acceptance; an attractive mesh is not a collision test.

The **wounded** class declares a maximum health attribute of 635, but `finalizeSpawn` sets its current health to a random 6–8% of maximum. Listing it simply as a 635-health spawn would therefore be misleading. It uses multipart tail damage modifiers and a distinct slower movement attribute. A qualifying player kill can repair a Bone Horn whose damage value is exactly one.

The inspected damage path also watches fire damage while specified body/eye positions are in tar. If the mob is dying under those conditions, it schedules a Skeletron conversion and transfers orientation. This is a conditional source path; it is not proof that the complete encounter chain is reachable in the released game.

**Restoration tests:** initial current health versus max health; multipart hit distribution; death-time scheduling once only; no duplicate conversion after reload; tar/fluid-tag compatibility; kill credit and exact horn-state condition.

## Skeletron — state persistence and historical identity

![Modern Skeletron resource showcase](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-skeletron.png)

The modern class has a synchronized wounded flag, persists it under the `Wounded` save key, selects wounded idle/walk animations, and drops a Warped Horn when the wounded state is set. Its inspected music method returns null. Do not silently assume the historical boss music or historical model is present merely because the registry name is unchanged.

The 1.16.5 source also declares `aoa3:skeletron`, but uses a visibly different three-headed skeletal model, a different base class and explicit Skeletron music packet handling. A complete historical union must record that collision and preserve the accepted old encounter alongside modern behavior through an explicit, tested identity/migration design. The choice of how to expose both designs remains a project decision.

## Evidence and next work

- [Pinned modern boss source](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss)
- [Legacy Skeletron source](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/boss/SkeletronEntity.java)
- Exact summon items, arena admission, loot tables, achievements, despawn/reset rules, sounds and full normal/elite phase timings still require per-encounter data reconciliation and runtime proof.
- Keep source-observed behavior distinct from completed Enderloom output. Do not mark a boss done because its class, item or preview image exists.

Advent of Ascension is created by **Tslat and contributors**. These are original source-based explanations and credited visual showcases.

## Practical entry and token states

[Boss entry and token preparation for 1.21.1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) covers released damage components, strict Bone Horn repair ingredients, Nowhere altar sequencing, original gold trophies and return behavior. It also flags the inspected WOUNDED-state gap in the Warped Horn acquisition chain. Do not treat the conversion callback alone as proof that the required drop flag is set.
