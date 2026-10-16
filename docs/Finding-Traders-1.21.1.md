# Finding Traders · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** The modern roaming-trader system differs from the historical 1.16.5 one. This page combines the shipped spawner resources, released-class arithmetic checks and the Precasian Lotto Hovel’s actual template entities. It does not promise a trader at a particular world coordinate or time.

[Search modern offers](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.21.1) · [Prices and restocking](Trading-and-Traders-1.21.1) · [Historical locations](Finding-Traders-1.16.5)

## The two stock roaming definitions

| Trader | Declared dimension filter | Reference |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-lottoman.png" width="80" height="80" alt="Lottoman"> **Lottoman** | Overworld, Nether and End are explicitly included. | [Bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:lottoman) |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-undead_herald.png" width="80" height="80" alt="Undead Herald"> **Undead Herald** | The source dimension guard accepts Minecraft/AoA namespaces; its stock resource excludes `aoa3:nowhere`. Retained dimension names are not a playable-realm guarantee. | [Bestiary](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3:undead_herald) |

Both stock definitions disable spawning in superflat worlds and contain no explicit biome include/exclude list. That is **not** permission to spawn inside any block: registered placement, valid spawn-block, collision, obstruction and other engine/mod checks still apply.

The explicit gamerule checked by this modern roaming implementation is **`doTraderSpawning`**, along with its passive-spawning flag. The historical 1.16.5 special spawner directly checks `doMobSpawning` instead. Global engine spawning conditions can also matter; do not treat these snippets as the only gates in a modpack.

## Timing: attempts, not appointments

| Stock setting | Value | What it means |
|---|---|---|
| Chance per eligible player | 1.0 | The per-player random gate does not itself reject a normal draw; later conditions still can |
| Attempts per player | 1 | One candidate-position attempt per eligible player on a pass |
| Interval | Uniform 12,000–36,000 ticks | Next scheduled pass; roughly 10–30 minutes at a steady 20 TPS |
| Extra delay after an accepted spawn | Uniform 8,000–12,000 ticks | Added to the shared spawner’s next time; roughly 6m40s–10m at 20 TPS |
| Initial next-spawn value | −1 | A fresh instance has no initial future-time deadline; this does not guarantee an immediate successful NPC |

Only living, non-spectator players are considered. The next interval is set before candidate spawning, so a rejected attempt still does not imply an immediate successful retry. Slow ticks, unloaded worlds, eligible players and datapack/modpack changes can alter the experience.

## Lottomans can also be in Precasian Lotto Hovels

The roaming dimension list is not the whole acquisition story. The released **Precasian Lotto Hovel** start pool contains six single-template variants, and **each of those six templates contains one canonical `aoa3:lottoman` entity**.

- Structure: `aoa3:precasian_lotto_hovel`.
- Its biome tag names `aoa3:precasian_plains` and `aoa3:precasian_savannah`, as optional entries. Both biome resources exist in the inspected archive.
- The structure set uses random-spread placement with spacing 24 and separation 12. These are placement parameters, not “a hovel every 24 blocks” or a success percentage.
- All six template-pool entries have weight one. This describes pool selection, not six guaranteed hovels or six new NPC species.
- The checked vanilla SinglePoolElement settings preserve entities and finalize them. Actual structure generation, bounding-box inclusion and mod overrides still need live testing.

[Precasia travel and archaeology walkthrough](Precasia-Realmstone-Walkthrough) · [Template, pool, biome and entity-placement evidence](https://herbertofury.github.io/Advent-of-Ascension/trader-locations-1.21.1.json)

The scan also found retained templates containing older regional Lottoman IDs. Those are not automatically working modern NPC routes; no registry-alias or activation proof is inferred from their presence.

## A coordinate-range mismatch worth knowing about

The trader code calls a helper with values named minimum 20 and maximum 64, but the checked calculation adds the **44-block width again** to each signed offset. Nonzero coordinates can therefore be roughly 44–88 blocks away on each axis, including positions beyond the named maximum. A sample axis draw of +22 becomes +66.

![Roaming trader coordinate arithmetic](https://herbertofury.github.io/Advent-of-Ascension/previews/roaming-trader-coordinate-bands.webp)

This is a static source/released-bytecode finding, not a measured spawn map. Do not use the parameter names alone to promise a 20–64-block circular search ring. [Full cross-version audit, current-candidate caveat and repair checklist](Roaming-Trader-Spawn-Geometry).

## When a trader will not restock

For the inspected modern custom trader goal, close the trade screen and move more than **24 blocks** away; another nearby living player can still block the goal. Alive, not currently trading, restock eligibility and `shouldRestock()` checks remain required. This is a necessary-condition guide, not a timer guarantee. The historical 1.16.5 goal does not contain that nearby-player check.

## Evidence

- [Stock resources, six hovel templates and vanilla placement flags](https://herbertofury.github.io/Advent-of-Ascension/trader-locations-1.21.1.json)
- [334-template canonical-ID scan](https://herbertofury.github.io/Advent-of-Ascension/trader-template-scan-1.21.1.json)
- [Exact geometry and gamerule audit](https://herbertofury.github.io/Advent-of-Ascension/roaming-trader-geometry-audit-1.21.1.json)
- [Roaming trader source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/world/spawner/RoamingTraderSpawner.java) · [Shared helper source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/world/spawner/AoACustomSpawner.java)

Model and texture artwork: **Tslat and contributors**. Diagram and extraction tools are original documentation work. No live spawn, timing, loot or current Enderloom candidate certification is claimed.
