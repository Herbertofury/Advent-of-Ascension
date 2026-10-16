# Roaming Trader Spawn Geometry · source and release audit

**Finding:** the inspected official 1.20.1 / AoA 3.7.1 and 1.21.1 / AoA 3.7.16.1 implementations can select horizontal coordinates beyond the caller’s named `maxRadius = 64`. This is an arithmetic finding with released-bytecode checks, not a live-game failure report or a completed patch.

![Checked roaming-trader coordinate calculation](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/roaming-trader-coordinate-bands.webp)

## What the code actually calculates

The trader caller supplies minimum 20 and maximum 64. The helper computes a width of 44, samples an offset using that width, then adds **the width again**, multiplied by the offset’s sign, before flooring the coordinate.

| Sampled axis offset | Final offset from an integer origin |
|---:|---:|
| +22 | +66 |
| −22 | −66 |
| +43.5 | +87 |
| −43.5 | −88 |
| 0 | 0 |

For ordinary nonzero draws, this creates bands roughly 44–88 blocks away on **each axis**, rather than a 20–64 radial annulus. A point at (+66, +66) is also farther away than 64 in Euclidean distance. Terrain, heightmap, collision and spawn checks can still reject it; the diagram is not a measured distribution of successful spawns.

The exact-zero path returns the center coordinate for that axis. The implementation also clamps negative width to zero. Neither behavior should be silently assumed to satisfy a minimum-distance requirement.

## Exact artifact boundaries

- **1.20.1 / 3.7.1:** the released helper lives inside `RoamingTraderSpawner`. The newer pinned 1.20 source snapshot has refactored a similar helper into `AoACustomSpawner`; that newer class layout must not be substituted for the inspected release. The release uses SmartBrainLib’s double-valued random helper.
- **1.21.1 / 3.7.16.1:** the released helper is in `AoACustomSpawner`, and uses TME’s float-valued random helper before converting to double coordinates.
- Both released calculations contain the same width-offset behavior. **RNG sequence equivalence across releases is not claimed.**

[1.20.1 released evidence](https://herbertofury.github.io/Advent-of-Ascension/roaming-trader-geometry-audit-1.20.1.json) · [1.21.1 released evidence and standalone cases](https://herbertofury.github.io/Advent-of-Ascension/roaming-trader-geometry-audit-1.21.1.json)

## Current Enderloom candidate: verify before changing it

The published owner-local artifact inventory reports a **different** `RoamingTraderSpawner.class` hash from the official 1.20.1 reference. That difference is not proof of a fix, and the cloud documentation pass has not read the current local JAR or run its spawn path. Inspect the exact current implementation before applying a patch or marking this issue present in that candidate.

[Inventory-only comparison](https://herbertofury.github.io/Advent-of-Ascension/trader-geometry-current-inventory-comparison.json) · [Current candidate inventory](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/development/current-artifact-inventory.json)

## Decide the intended geometry first

Two different designs are possible:

1. **Axis bands / square regions:** add the intended minimum distance, rather than the width, to each signed sampled axis offset. This still produces corner regions; it is not a circular annulus. Exact zero and invalid-range handling require an explicit policy.
2. **A true radial annulus:** sample an angle and a radius using the desired distribution, then validate the final integer coordinate against the chosen distance bounds. Flooring can move a point outside a continuous bound, so validate after discretization and keep retries bounded.

The accompanying 10,000 seeded standalone axis samples demonstrate the current bound violation and one nonzero axis-band alternative. They are **not a full gameplay fix, a probability estimate, a performance benchmark or a vanilla/TME RNG emulation**.

## Implementation and acceptance checklist

- [ ] Inspect the exact current Enderloom candidate’s helper and record its class/source identity.
- [ ] Decide and document radial versus axis-band semantics; preserve intended gameplay rather than guessing from parameter names alone.
- [ ] Test zero draws, negative world coordinates, fractional offsets, equal bounds, invalid bounds and coordinates near chunk boundaries.
- [ ] Enforce the chosen limits on final integer coordinates, with bounded attempts and no forced placement after all candidates fail.
- [ ] Test ordinary terrain, caves/ceilings, water, low build heights, the Nether and the End without an unbounded vertical search.
- [ ] Verify player eligibility, gamerules, superflat restrictions, datapack overrides and per-world timing remain intact.
- [ ] Check chunk access and server-tick costs with equivalent work; do not add synchronous chunk generation or claim an FPS gain without measurements.
- [ ] Run native server/client, save/reload and multiplayer checks for the affected scope, then update the runtime acceptance checklist.

No original game classes are executed by the audit scripts, and no modified JAR is published by this documentation work.
