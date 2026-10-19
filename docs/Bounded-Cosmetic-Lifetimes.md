# Bounded cosmetic lifetimes

[Effects storyboard](Soul-Storm-Effects-Storyboard) · [Weapon quality standard](Weapon-Completeness-Standard)

## Keep the effect collection from growing forever

Soul Storm's proposed short-lived impacts and decals need explicit cleanup. The engine-independent v5 presentation candidate adds a fixed-capacity lifetime metadata pool. It has no native renderer or gameplay authority. No currently installed mod behavior is changed by this study.

The pool keeps expiry times in a minimum heap instead of scanning the world or discovering resources on every frame. Capacity is configured at construction (1–4096); each accepted lifetime is positive and at most 60 seconds. A full pool returns zero for an additional **cosmetic** request and creates no deferred backlog. Native visual quality and suitable budgets still require measurement; this is not a default-quality reduction or an FPS claim.

[Source and reproducible tests](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/aoa-presentation-core-v5.zip) · [Evidence manifest](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/aoa-presentation-core-v5-evidence.json)

## Ownership and time rules

- One owning presentation thread and paused game time.
- Advance once at the presentation update boundary, then add accepted cosmetic requests.
- Same-time updates do not create extra expiry or emissions.
- Rewinding time requires an explicit world reset; invalid time rejects before mutation.
- World reset clears resident metadata but does not recycle handle serials.
- Handles belong to one pool. They are not network identities, authentication or transferable cross-pool references.
- Native resources need a separate owner. Metadata expiry alone does not free a GPU buffer or remove a rendered decal.

The existing confirmed-shot core and impact duplicate ledger keep their own jobs. This pool neither replaces them nor processes ammo, damage, projectiles, loot or block changes. A dropped cosmetic request must never discard a gameplay event.

## Scoped tests

The nine existing v4 source/test files remain byte-for-byte unchanged. The new lifetime test performs 3,381,737 assertions per runtime, including a deterministic 100,000-step independent map oracle, capacity pressure, same-time updates, expiry boundaries, stale handles, reset/reuse, non-finite values and update-rate comparisons. Capacity 1 and 4096 are explicitly tested.

All six suites passed on Java 17 and Java 21, including a clean extraction of the published bundle. Existing sight, impact-ledger, emission-clock, frame-visibility and atlas tests still pass. These are isolated logic checks, not millions of native gameplay scenarios.

## Complexity, without inflated performance claims

| Operation | Source-level bound |
|---|---|
| Add | O(log capacity) |
| No-expiry update | Root check |
| Expire due entries | O(expired entries × log capacity), at most resident capacity |
| Handle lookup | O(1) |
| Retained metadata | Fixed arrays allocated at construction |

These bounds do not establish improved FPS, lower GPU memory or lower startup time. Native tests must measure the same content and workload, including frame-time lows and visible effect density.

## Remaining adapter gates

- [ ] Native ownership and reliable resource release on expiry, unload and disconnect
- [ ] Explicit priority policy and visual-pressure behavior without gameplay loss
- [ ] Camera/shader/material integration and first-person readability
- [ ] Duplicate/predicted/corrected event integration with the existing accepted-shot core
- [ ] Measured native performance, memory, compatibility and quality parity

The candidate intentionally has no manual early-cancellation API or priority arbiter. Those require a concrete adapter use case and tests before extending it.
