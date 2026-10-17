# Throwable weapons: prepare stacks and understand impact behavior

[Open the item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Ashfern and Hardened Parapiranha preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ashfern-Cooking-and-Food-Preparation-1.21.1) · [Other ranged weapons](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Statistics-and-Ammunition-1.21.1)

![All eight released throwable source models with impact and interval inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/throwable-overview-1.21.1.webp)

**Scope:** eight released thrown-weapon registrations in Minecraft 1.21.1 / AoA 3.7.16.1. Every selected registration explicitly configures maximum stack 64. Impact damage and throw interval are released component inputs; they do not fully describe special projectile effects or explosions.

## Prepare before throwing

1. Open a weapon below and follow its exact-version recipe and drop links. Do not assume the eight items share an acquisition route.
2. Expand **Throwable defaults · impact, interval and stack size**. Stack size describes carried items, not weapon durability.
3. Bring enough items for the intended encounter. The selected base player path calls item consumption before constructing and spawning the projectile; resource-exempt behavior must be checked separately.
4. Test Grenade and Runic Bomb away from valuable terrain and builds. Their impact-damage field is zero, but both have separate explosion definitions.
5. Check special projectile behavior before relying on recovery, returning throws or dispenser parity. A familiar weapon name is not proof of those mechanics.

## Registered defaults

| Weapon | Impact-damage input | Throw interval (ticks) | Maximum stack |
|---|---:|---:|---:|
| [Grenade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agrenade) | 0 | 9 | 64 |
| [Slice Star](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aslice_star) | 4.5 | 4 | 64 |
| [Chakram](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Achakram) | 4 | 5 | 64 |
| [Goo Ball](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agoo_ball) | 3.5 | 7 | 64 |
| [Vulkram](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avulkram) | 3 | 5 | 64 |
| [Hellfire](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahellfire) | 3.5 | 6 | 64 |
| [Runic Bomb](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arunic_bomb) | 0 | 10 | 64 |
| [Hardened Parapiranha](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahardened_parapiranha) | 10 | 20 | 64 |

Grenade and Runic Bomb retain the released builder’s zero impact-damage default. The other six explicitly set impact damage. The interval is a configured tick input, not a real-time throw-rate benchmark.

## Explosion inputs are separate

| Definition | Radius input | Block-damage input | Entity-damage input | Block-drop-chance input |
|---|---:|---:|---:|---:|
| Grenade | 3 | 7 | 5 | 0.1 |
| Runic Bomb | 3 | 7 | 3 | 0.05 |

These are released explosion-builder values, not guarantees of actual affected blocks, damage or item drops. Block-damage input 7 does not mean “exactly seven blocks break.” Geometry, explosion implementation, resistance, game rules, hooks and integrations can affect the result. Both inspected projectile classes call their explosion path on block and entity impact.

## Hand use and dispensers are different paths

The hand-use path creates a firing context from a copy of the stack and supplies the configured impact damage. The dispenser-facing `asProjectile` method builds a context through a different path. This guide does not assume that every context field, velocity or damage result is identical between hand and dispenser use.

The base hand-use path also checks blocking/use state and attack-strength readiness. A non-null projectile result leads to item-use statistics and a configured cooldown when the interval exceeds one. Subclass behavior still requires separate inspection.

## Maintainer regression target: consumption before successful spawn

The released base `findAndConsumeAmmo` calls consumption before `createProjectileEntity`. The selected `throwProjectile` path then attempts entity insertion. If `addFreshEntity` returns false, its success-only callbacks are skipped, but the method still returns the projectile reference. No refund appears in these selected base methods, and the caller treats a non-null result as sufficient for its statistic/cooldown branch.

This is a bounded transaction-order finding, not an in-game item-loss reproduction or a claim that ordinary throws fail. Other hooks can change behavior. Test construction failure, rejected entity insertion, successful insertion, Creative/resource-exempt use and multiplayer cancellation. A restoration fix should avoid both lost items and duplicated projectiles, preserve legitimate consumption, and commit success feedback only after the intended success boundary.

## Acceptance checklist

- One ordinary hand throw: original stack, projectile presence, statistic and cooldown.
- Last item in a stack and resource-exempt cases.
- Rejected/canceled creation and spawn, with a precise inventory before/after record.
- Hand versus dispenser contexts and projectile motion/damage.
- Grenade and Runic Bomb terrain interaction in a disposable test area.
- Special effects, pickup/return behavior, immunity and client/server agreement for every variant.

[Released registration, base methods and explosion segments](https://herbertofury.github.io/Advent-of-Ascension/throwable-evidence-1.21.1.json) · [Eight-model illustration provenance](https://herbertofury.github.io/Advent-of-Ascension/throwable-art-evidence-1.21.1.json).

Archive: `AoA3-1.21.1-3.7.16.1.jar`. Class hashes and instruction records are preserved. No Java game classes were executed and no private Enderloom fix is claimed. AoA assets and mechanics are credited to Tslat and contributors.
