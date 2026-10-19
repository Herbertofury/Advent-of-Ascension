# Game-time projectile trail scheduling

An original, dependency-free presentation component for the AoA weapon overhaul. It is an authoring/integration candidate, not an installed mod or verified FPS improvement.

## Why this exists

The pinned AoA 3.7.1 CarrotBallRenderer performs eight iterations of two particle requests after its base rendering call: 16 requests per renderer invocation. This count was checked against released bytecode and recorded in `carrot-cannon-released-evidence.json`. It does not identify the number of native render invocations per second or prove a measured bottleneck.

`ProjectileTrailClock` moves the scheduling decision to a per-projectile game-time owner. The renderer should only draw existing effects. Repeated render passes, camera views and duplicate callbacks must not generate extra requests.

## Contract

- Create a fresh instance for each projectile lifetime and world/session. No global scan or global map is needed by this component.
- Call from an actual client game-time update on its owning thread, with a nonnegative monotonically increasing tick value. Do not call it from a render loop.
- First valid update establishes a baseline. Spawn effects are a separate native hook.
- Paused, duplicate, stale and closed-projectile updates emit zero requests.
- A forward tick produces the configured request count once. A zero budget is valid; negative and greater-than-4096 budgets are rejected. This validation ceiling is not a recommended game setting.
- Gaps do not trigger an unbounded catch-up burst. `skippedTicks` explicitly reports missed ticks. There is no hidden position interpolation, because this component has no position history.
- Removal is terminal. Resetting the world clock must create a new instance, rather than reusing an old projectile clock.

## What the tests establish

57,662 assertions on both Java 17 and Java 21 cover 1, 2, 3, 8, 30 and 100 callbacks per tick, repeated/stale updates, initial and later pauses, explicit gap accounting, terminal removal, zero budget, invalid inputs and a jump to Long.MAX_VALUE. Across 200 forward ticks, the fixture always returns 3,200 requests for a configured budget of 16, regardless of duplicate callback count.

The number 16 is a test fixture, not an approved replacement for the original visual density. At 20 client ticks per second that policy would nominally schedule 320 requests per second, which is not equivalent to 16 per render invocation. No appearance-preservation claim follows from the test.

## Native integration and quality gates still open

1. Confirm the correct loaded client-world tick hook, lifetime ownership, pause behavior and removal path in the exact target version.
2. Keep the orange/golden and flickering-yellow effect identities, offsets and cosmetic-only behavior from the source audit. Native particle settings and culling still apply.
3. Decide and document whether the trail is time-based or distance-based. A bounded sampled-position path could fill visible gaps; never invent old positions or teleport a trail through intervening terrain.
4. Visually compare equal projectile paths at low/high FPS, different FOVs, multiple render passes and pause/resume. Record the original and proposed native captures.
5. Measure equivalent-work client frame time, allocations and particle counts. Tune visible density and batch implementation before claiming a no-loss optimization.
6. Ensure renderer code no longer schedules duplicate emissions before enabling the new hook; running both paths would increase work.
7. Validate shared projectile removal, dimensions, multiplayer and modded render hooks. This clock does not change damage, ammo, projectile physics, spawning or game balance.

Run `python run_checks.py` with the documented JDK paths or pass `--jdk17` and `--java21`. Only original source and test results are bundled; no upstream game classes or dependency binaries.
