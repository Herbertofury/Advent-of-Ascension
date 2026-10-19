# Particle emission and frame time

**Research and headless prototype. Not enabled in Minecraft; no FPS improvement or visual equivalence is claimed.**

## The actual source issue

[Aqua Cannon](Aqua-Cannon-Weapon-Profile) uses Heavy Blue Cannonball rendering. Its inspected AoA 3.7.1 renderer requests eight SPARKLER particles per render invocation. Particle demand therefore depends on rendering frequency and potentially render passes, rather than only game time. Eight requests multiplied by sixty invocations is an illustrative 480 requests/second for one projectile, before particle-engine filtering.

This observation comes from the released class, not just the weapon’s description. [Evidence and renderer hash](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/aqua-cannon-released-evidence.json).

## Prototype: separate requests from drawing

[Download original Java source, tests and integration notes](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/particle-emission-clock-prototype.zip) · [Checked runtimes and source hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/particle-emission-clock-qa.json).

The small clock accepts elapsed **game time** and returns a bounded request count. It keeps only fractional state, resets when inactive, rejects invalid inputs, and deliberately discards excessive hitch debt according to configured limits. It does not call graphics APIs, allocate particles or change damage/healing.

Headless tests cover steady totals at 10, 20, 30, 60, 90, 144 and 240 calls/second, pause/inactive transitions, reset, zero-rate behavior, bounded hitches and invalid inputs. Both checked Java 17 and 21 runtimes passed. The 5,961 assertions per runtime include repeated bounds assertions; they are not 5,961 separate gameplay scenarios.

## Important tradeoffs

A frame-coupled original has different emission rates at different frame rates. A fixed time-based rate cannot be claimed to preserve every such appearance simultaneously. Choose and capture a reference appearance first. The example test rate is not a production recommendation.

The catch-up/burst limits prevent unbounded deferred particle floods after stalls. They intentionally discard excess emission, so they are not a lossless rule under arbitrarily long hitches. Expose and tune that policy rather than silently reducing effect quality.

## Native acceptance work

- [ ] Integrate once per elapsed interval; prevent double feeding from tick and render callbacks
- [ ] Verify pause, world changes, entity removal, visibility and multiple render passes
- [ ] Compare native trail appearance against the selected original reference capture
- [ ] Profile many projectiles with frame-time, particle-count, allocation and memory measurements
- [ ] Test graphics settings, renderers, multiplayer observers and reduced-effects controls
- [ ] Confirm gameplay damage, healing, sounds and impact authority are unchanged

[Weapon completeness standard](Weapon-Completeness-Standard) · [Weapon overhaul](Weapon-Overhaul)
