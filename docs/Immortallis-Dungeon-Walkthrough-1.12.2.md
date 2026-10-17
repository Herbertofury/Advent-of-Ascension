# Immortallis: the nine-stage dungeon

**Historical walkthrough: Minecraft 1.12.2 / AoA 3.3.6.** The route below is checked against selected methods in the released JAR and its loot resources. It is not a promise that a modern port has restored this dungeon, and it is not a recorded playthrough.

[Worlds and travel atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Ancient Cavern and deity basics](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2) · [Version comparison](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

## Before you enter

Bring a Blank Realmstone, supplies for a dangerous hit, five Silver Coins for the Dungeon Keeper, and inventory space for a Return Crystal and boss coins. Keep progress coins safe: the dungeon uses them as keys between stages.

To obtain the Immortallis Realmstone, survive a successful melee attack from a **Construct of Strength while the construct itself has Strength**. The server callback checks that the target player is still alive, consumes one Blank Realmstone from that player's inventory, and gives or drops the Immortallis Realmstone. Giving Strength only to yourself does not satisfy that check. The construct's Strength-effect handler also increases the incoming amplifier using `(amplifier + 1) × 4`; treat this as a dangerous preparation step, not an ordinary unmodified hit. The selected callback does not itself impose a dimension check; Crystevia is the relevant creature's usual setting.

The Immortallis portal arrival is **(-5, 20, 3)**. The Dungeon Keeper's selected fixed trade exchanges **5 Silver Coins for 1 Progress Coin 0**. Enter through the first progressor with room for the Return Crystal.

## Route at a glance

![Immortallis nine-stage route, bosses and progress coins](https://herbertofury.github.io/Advent-of-Ascension/previews/immortallis-nine-stage-route-1.12.2.webp)

| Stage | Requirement | Next room / player destination | What to do there |
|---|---|---|---|
| 1 | Spend Progress Coin 0; accept Return Crystal | Gold room: (28, 20, 2) | Collect and deposit Impure Gold |
| 2 | Pluton tribute ≥100 | Klobber: (67, 21, 2) | Defeat Klobber and collect Progress Coin 1 |
| 3 | Spend Progress Coin 1 | Skeletal spirits: (81, 21, 2) | Earn Erebon tribute from Skeledon / Skelekyte |
| 4 | Erebon tribute ≥100 | Proshield: (122, 21, 2) | Defeat Proshield and collect Progress Coin 2 |
| 5 | Spend Progress Coin 2 | Pure Gold room: (141, 24, 2) | Collect and deposit Pure Gold |
| 6 | Pluton tribute =200 | Mirage: (168, 24, 7) | Defeat Mirage and collect Progress Coin 3 |
| 7 | Spend Progress Coin 3 | Evil spirits: (189, 20, 2) | Earn more Erebon tribute |
| 8 | Erebon tribute =200 | Flash: (233, 21, 3) | Defeat Flash and collect Progress Coin 4 |
| 9 | Spend Progress Coin 4 | Completion area: (0, 20, 0) | One Return Crystal is removed; all tribute resets |

The four boss-gate branches check tribute without subtracting it. The later 200-point targets build on the earlier meter. These are source-defined player destinations, not a surveyed safe route through a modified server's terrain.

## Gold rooms: collect, then deposit

**Impure Gold:** Goldum's eligible death callback gives or drops one Impure Gold when the credited player's Pluton tribute is below 100 and their inventory does not already contain that item. A player kill or a tameable's player owner can qualify. Deposit it at the Gold Accumulator, then collect another. The ordinary increment is `min(100 − current tribute, 20)`.

**Pure Gold:** Goldus similarly checks that the credited player's inventory does not already contain Pure Gold, then gives or drops one. Its selected callback has no corresponding below-100 tribute gate. The Pure Gold Accumulator contributes 20 per deposit before shared modifiers. Both accumulators consume the held gold outside Creative mode.

With resources enabled, starting at zero and without the Holy Sword modifier, five Impure Gold deposits reach 100; five Pure Gold deposits later take 100 to 200. These are arithmetic examples under those assumptions, not unconditional required kill counts. Ground drops are not the same as inventory contents; pick up your materials before moving on.

### Holy Sword changes the arithmetic

The shared tribute method doubles signed changes while its Holy Sword condition applies, then clamps tribute to 0–200. The early accumulator computes its limit before that multiplier. From zero, three modified Impure Gold deposits can produce **0 → 40 → 80 → 120**. An additional early deposit at 120 computes a negative input and can model **120 → 80**. Stop using the early accumulator once its gate is met. Two modified Pure Gold deposits from 120 reach 200.

These boundary calculations are independently checked Python examples derived from the selected released methods. The adverse extra-deposit case remains a target for in-game regression testing, not a claim of a reproduced session.

## Spirit rooms: who contributes

Skeledon and Skelekyte check the configured Immortallis dimension and award Erebon tribute below 100, using `min(4, 100 − current)`. Ghastus, Urv and Visage have selected Immortallis death callbacks contributing 4 toward the later meter. Eligible credit resolves a player or a tameable's player owner; an arbitrary environmental death is not the same thing.

Without shared multipliers, 25 eligible +4 contributions take zero to 100, and another 25 take 100 to 200. Holy Sword and resource configuration alter those assumptions. Read the meter and use the appropriate progressor rather than treating the number of enemies as a universal counter.

## Four bosses and their rewards

### Klobber

![Klobber historical source-model preview](https://herbertofury.github.io/Advent-of-Ascension/previews/legacy-1.16.5/1.16.5-model-KlobberModel-thumb.webp)

[Creature card](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aklobber)

The selected default table has separate one-roll statue and progress-coin pools: `klobber_statue` and `aoa3:progress_coin1`. These are default table contents, subject to the actual death/drop path and server modifications.

**Fight plan: crouch deliberately when the pull threatens your position.** Klobber's living-update callback selects vulnerable players inside its bounding box expanded by 11 on each axis. Non-sneaking players receive horizontal velocity toward its position: each horizontal component uses the sign of the offset multiplied by 0.019. Sneaking skips this particular pull branch; it does not make you immune to melee attacks. This is a box-shaped query, not a guaranteed spherical 11-block radius. Its base getters return 1,000 health and 20 melee damage before shared modifiers.

The selected override has no explicit server-only guard. Whether inherited update/network behavior duplicates the effect is a port-testing question, not an established multiplayer defect.

### Proshield

![Proshield historical source-model preview](https://herbertofury.github.io/Advent-of-Ascension/previews/legacy-1.16.5/1.16.5-model-ProshieldModel-thumb.webp)

[Creature card](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aproshield)

The selected default table has separate one-roll statue and progress-coin pools: `proshield_statue` and `aoa3:progress_coin2`. These are default table contents, subject to the actual death/drop path and server modifications.

**Fight plan: prefer a genuinely non-melee damage source when avoiding retaliation.** After the superclass accepts an incoming hit, Proshield checks AoA's melee classifier. If it qualifies, the immediate attacker receives a new mob-damage attempt with half the incoming `amount` argument. It is not “exactly half of the health Proshield lost”: armor, damage events and the retaliation target's mitigation are separate. Base getters return 500 health and 5 melee damage.

The helper requires a non-null true source, matching immediate/true sources, and excludes projectile, `thrown`, magic, explosion and fire damage. A weapon's appearance is not its damage classification. Those exclusions explain this reflection branch only; they do not prove that every ranged or magic weapon bypasses every inherited defense.

### Mirage

![Mirage historical source-model preview](https://herbertofury.github.io/Advent-of-Ascension/previews/legacy-1.16.5/1.16.5-model-MirageModel-thumb.webp)

[Creature card](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amirage)

The selected default table has separate one-roll statue and progress-coin pools: `mirage_statue` and `aoa3:progress_coin3`. These are default table contents, subject to the actual death/drop path and server modifications.

**Fight plan: keep the four teleport destinations in view and reacquire your aim after each move.** Mirage is a ranged boss whose selected projectile factory creates a Spiritual Shot with the `MAGIC` type. Its base projectile-damage getter is 8 and base health is 750; these are not final player health-loss values.

Each eligible server living update independently checks `nextInt(80) == 0`. Within Immortallis it then selects one of four coordinates: **(167,24,8), (168,24,-2), (177,24,8), (177,24,-2)**. The source has no guaranteed four-second cooldown. At a nominal 20 eligible updates per second, 80 trials corresponds to a four-second mean waiting time, but moves can happen much sooner or later. The random choice can also select its current corner. Outside Immortallis, a different coordinate/height branch applies; do not use the fixed-room map as a universal behavior description.

### Flash

![Flash historical source-model preview](https://herbertofury.github.io/Advent-of-Ascension/previews/legacy-1.16.5/1.16.5-model-FlashModel-thumb.webp)

[Creature card](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aflash)

The selected default table has separate one-roll statue and progress-coin pools: `flash_statue` and `aoa3:progress_coin4`. Flash also has a one-roll pool choosing **one Archaic armor piece** from four equal-weight entries, plus a separate Dungeon Tokens pool with a 5–12 count range. This does not award the entire armor set in one pool roll. These are default table contents, subject to the actual death/drop path and server modifications.

**Fight plan: expect relocation around melee exchanges; be ready to turn and reacquire.** On the server, a melee-classified incoming damage attempt can make Flash teleport **before** the superclass reports whether that hit was accepted. Separately, the inherited successful outgoing melee path calls Flash's `doMeleeEffect`, which also relocates it. “Only teleports after you damage it” therefore misses a second trigger and the ordering of the first.

Within Immortallis both paths choose among **(235,22,10), (235,22,-3), (228,22,3)**. Non-melee attacks avoid this particular incoming-melee trigger, but do not switch off its outgoing-melee relocation or certify immunity bypasses. Base getters return 1,000 health and 9 melee damage. The constructor enables slippery movement and supplies an AI movement-speed value of 3.2; neither that argument nor the separate 0.329 base movement getter should be labeled as measured blocks per second.

## Return Crystal, failure and recovery

- **No room at stage 1:** if the Return Crystal cannot be inserted, the handler resets tribute and drops a replacement Progress Coin 0 at the player. Recover that ground item; the refund is not a guaranteed inventory insertion. The successful room teleport is in the other branch.
- **Using the Return Crystal inside Immortallis:** finishing its use resets tribute, removes one of each Progress Coin 1–4 if present, consumes the crystal outside Creative, and moves the player to **(-5, 20, 3)**. That is the dungeon entrance, not an automatic trip to the Overworld.
- **Outside Immortallis:** the selected use callback reports the wrong-dimension message. Do not rely on it as a universal escape item.
- **Duplicates:** the cleanup calls request one coin of each kind, not an unlimited purge of every duplicate. Progress Coin 0 is not among those four cleanup calls.
- **Completion:** stage 9 consumes Progress Coin 4, teleports to (0, 20, 0), attempts to remove one Return Crystal and resets tribute.
- **Death / changing dimension:** the shared reset callbacks documented in the Ancient Cavern guide make saved tribute unsafe to assume. This is not a checkpointed-run guarantee.

## Building and multiplayer boundaries

The provider restricts interaction with placeable blocks, buckets, armor stands and hanging entities. Its placement/mining helpers separately have Creative and torch exceptions; those helpers must be read together with interaction restrictions. A torch exception alone is not verified permission to place it through every path. Normal respawn in this provider is disabled.

The boss progressors instantiate a boss at fixed coordinates, discard the spawn call's boolean result, then teleport the player. The selected branches do not demonstrate a private per-player instance, a multiplayer reservation, a retry-safe summon transaction, or protection from repeated activations. These are explicit acceptance-test targets before calling a restored port stable.

## Restoration and testing checklist

- Preserve all nine stage bindings and all five progress-coin identities.
- Check successful and full-inventory entry, ground-item refund recovery, and disconnect/rejoin around transitions.
- Test ordinary and Holy Sword tribute arithmetic, resource-disabled configuration, and the 100/200 gate boundaries.
- Check player, tameable-owner, environmental and multiplayer kill credit separately.
- Verify failed boss spawn, duplicate activation, two players sharing a room, and missing/modified loot resources.
- Test Return Crystal inside/outside the dimension, duplicates, death, completion and portal return-location persistence.
- Verify actual structure placement, collision, boss combat, renderers and performance in the target port. None is certified by this static documentation audit.

## Evidence and scope

[Released-method and exact-loot evidence](https://herbertofury.github.io/Advent-of-Ascension/immortallis-evidence-1.12.2.json) records 27 selected methods, nine progressor constructor bindings, four loot resources and arithmetic examples. Source interpretation is pinned to upstream commit `29dd8a8a20642ee182b851e34ef58b65f68e68bf`; selected released bytecode is retained with class hashes.

[Boss combat callback evidence](https://herbertofury.github.io/Advent-of-Ascension/immortallis-combat-evidence-1.12.2.json) supplements the route with 26 selected released methods. Tactics are source-derived guidance; successful live-fight validation remains separate.
