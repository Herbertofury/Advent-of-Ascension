# Four Guardians: power the altar and plan the final color

**Minecraft 1.12.2 / AoA 3.3.6.** This historical walkthrough follows the released Guardian Altar and four guardian classes. It covers preparation, the redstone gate, combat differences, color-dependent rewards and restoration hazards. It is not certification that a modern merged build has restored the encounter.

[Worlds and travel](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions#haven) · [Ancient Cavern](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2) · [Immortallis](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Immortallis-Dungeon-Walkthrough-1.12.2)

![Four Guardian colors and their final-opponent rare rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/four-guardians-final-color-rewards-1.12.2.webp)

## Prepare before powering anything

- Reach Haven and find the Guardian Tower's altar.
- Bring a **Voliant Heart**, combat supplies and a way to power all four horizontal sides of the altar.
- Keep the activation circuit small and separate from valuable redstone builds. The altar removes connected redstone wire during activation.
- Decide which color-specific reward you want before the fight. In an intact linked encounter, the final guardian's table is the one that becomes available.
- Leave room around the altar: the four initial spawn positions are eight blocks away on both horizontal axes.

## 1. Reach Haven and locate the altar

The checked historical Haven Realmstone route is in Flye's death callback: on the server, in Lelyetia, a player must receive credit through AoA's melee-damage classification while **the player's Y is at least 80**. The callback consumes one Blank Realmstone from that player and gives or drops the Haven Realmstone. It checks the player's height, not an assumed height of the Flye. This is a conditional kill route, not a crafting recipe.

[Inspect Flye](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aflye). Use the release-specific travel atlas for the preceding world progression rather than substituting modern realmstone rules.

The Haven chunk generator includes a configuration-gated Guardian Tower branch. It sits after other structure checks in an `else if` chain, so its chance is not an independent guarantee for every chunk. The tower's third construction section places the Guardian Altar at **local offset (14,72,14)** from the structure base. This is a relative construction offset, not the altar's absolute world Y.

**Restoration finding:** the selected released tower gate samples its terrain check at `(x + 14, y − 1, x + 14)` while the actual structure placement uses `(x, y − 1, z)`. The repeated X in the terrain check warrants a targeted generation test; it does not prove every tower fails to generate or identify a guaranteed search location. Preserve existing saves while testing any correction.

## 2. Obtain a Voliant Heart

[Inspect Voliant and its illustrated drops](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Avoliant).

The selected Voliant table has a dedicated one-roll Heart pool with a 0–1 count operation and a separate Looting count operation. It can produce zero; do not treat one kill as a guaranteed Heart.

Two other inspected resources list the Heart:

- **Guardian Tower general chest table:** Heart weight 2 in the main pool, alongside other entries. The pool has 10 rolls plus its declared bonus-roll range. These are table settings, not a promise that every chest contains a Heart.
- **Haven world table:** Heart weight 30 alongside an empty entry of weight 300 and Copper Coin weight 100. This is a shared table reference, not permission to label every Haven action as a Heart drop source.

The four guardian tables also contain Hearts among their supply entries, but that is a possible return from a successful encounter, not the prerequisite source for your first summon.

## 3. Power the four horizontal neighbors

Hold the Voliant Heart and activate the altar. On the server, the handler loops through **all four horizontal directions** and checks `getRedstonePower(adjacentPosition, direction)`. If any result is zero, it returns before consuming the Heart or summoning the group.

Think of the test as four required incoming signals: north, south, east and west. Power on only one side is insufficient. A block that looks powered is not proof that it provides power toward the queried side; inspect the actual connections and directionality. This guide describes the checked gate rather than claiming a particular untested circuit schematic always works.

The next gate looks for an `EntityMob` implementing `BossEntity` in the altar-centered box extending 15 blocks along each axis. If one is found, activation returns before the payment. This is a box query with a specific class filter, not a universal spherical check for every modded boss.

Once these gates pass:

1. One Heart is removed outside Creative mode.
2. Adjacent vanilla redstone-wire networks are traversed and removed, with item-entity drop attempts.
3. Four guardians are created, spawned and linked to one another through their guardian fields.
4. Nearby players receive the encounter message.

The handler belongs to `GuardianAltar`, not the shared `BossAltarBlock` implementation. Its selected method has no explicit Peaceful-difficulty check or dimension gate. That does not certify a stable Peaceful encounter or free placement elsewhere; do not borrow another altar's checks when documenting this one.

### Initial positions relative to the altar

| Guardian | X offset | Y offset | Z offset |
|---|---:|---:|---:|
| Blue | +8 | 0 | +8 |
| Red | −8 | 0 | +8 |
| Yellow | −8 | 0 | −8 |
| Green | +8 | 0 | −8 |

The four spawn calls discard their boolean results. Payment, wire removal and guardian linking are not proven to be a single rollback-safe transaction if an event cancels one of those spawns.

## 4. Read each guardian's threat

| Guardian | Base health | Base projectile damage | Checked special behavior |
|---|---:|---:|---|
| [Blue](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ablue_guardian) | 750 | 20 | Successful impact effect can apply Blindness for 40 ticks, amplifier 2 |
| [Green](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agreen_guardian) | 750 | 20 | Entity-impact effect and block-impact callback request a strength-2 explosion |
| [Red](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ared_guardian) | 750 | 20 | Successful impact effect can apply Slowness for 40 ticks, amplifier 2 |
| [Yellow](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ayellow_guardian) | 750 | 15 | Magic-type projectile; no additional impact-effect override was found in the selected class |

Base damage is not final health lost. Forty game ticks is nominally two seconds at 20 ticks per second; server timing and effect handling remain relevant. An amplifier is the stored source input, not a claim that every effect gains an extra useful tier from it.

Keep sightlines and a retreat lane. Blue interferes with vision, Red with movement, and Green's block-impact explosion means a missed shot is not automatically harmless. Your desired final color may change which threat you leave alive longest. The selected guardian entity-impact overrides skip targets that are both `AoARangedMob` and `BossEntity`; that is a specific friendly-fire exclusion rather than protection for every entity or every damage source.

## 5. Choose the last guardian for its rare table

Each guardian's `getLootTable` returns its color's table only when all three linked guardian checks pass. A referenced guardian passes when it is **null, marked dead, or has health exactly zero**. Otherwise the getter returns null.

For a normally linked group that stays intact, this means you should leave the color matching your desired rare reward until last:

| Final color | Color-specific rare entry | Shared rare alternative |
|---|---|---|
| Blue | Frosticator, weight 22 | Guardian's Sword, weight 27 |
| Green | Germinator, weight 22 | Guardian's Sword, weight 27 |
| Red | Dragilator, weight 22 | Guardian's Sword, weight 27 |
| Yellow | Electinator, weight 22 | Guardian's Sword, weight 27 |

Each one-roll rare pool also has an **empty entry of weight 100, quality −10**. These are weights, not fixed percentage rates, and the color-specific reward is not guaranteed. A separate statue pool contains Guardian Statue; supply and Haven-table pools remain separate. Open the exact creature card to inspect the full table with item images.

**Linkage caveat:** null references satisfy the gate. The selected classes use runtime object fields to link the group; this audit does not certify that those links survive save/reload, unloading, partial spawn failure or custom spawning. Do not generalize the last-color strategy to an already broken or unlinked encounter. This is an important restoration test, not a claim that a particular live session reproduced a reload bug.

## Keep altar wiring isolated

The private `breakWire` helper removes the current wire and recursively visits horizontal wire neighbors. Its count-of-20 check occurs **after** a recursive neighbor call. A forward-first chain model matching that ordering visits 21 or 64 nodes before unwinding; the literal 20 is therefore not a reliable global deletion cap.

This is a bounded independent Python graph example, not execution of Minecraft's world mutation. Direction order and the network layout influence actual traversal. The safe preparation advice is to keep the altar's redstone circuit separate from valuable wiring and avoid testing an enormous connected network in a real save.

A port should use an explicitly bounded worklist, check the budget before visiting another node, and define the intended per-activation limit. Test item-drop failure and protected-block cancellation before advertising lossless circuit recovery. No such runtime fix is claimed here.

## Troubleshooting

- **Nothing happens and the Heart remains:** verify all four power queries and the nearby-boss gate. Creative mode does not consume a Heart, so inventory changes alone are not a reliable success indicator there.
- **Heart or wires disappear but a guardian is missing:** inspect spawn-cancellation events and logs on a copied save. The inspected code does not roll the transaction back based on spawn return values.
- **A color-specific reward does not appear:** the rare pool can choose the empty entry or Guardian's Sword. Confirm the last linked color and the server's actual loot resources.
- **Rewards differ after unloading or rejoining:** verify guardian reference persistence and null-link behavior rather than assuming the same encounter state was restored.
- **Tower search seems inconsistent:** inspect the configured chance, earlier structure branches and the X/Z terrain-check mismatch. No fixed spawn coordinate is promised.

## Restoration acceptance checklist

1. Verify the Flye key route with player Y 79/80, eligible melee classification, Lelyetia and inventory overflow.
2. Verify the four individual redstone sides, no-power and partial-power cases, Creative, Peaceful and custom boss classes.
3. Test isolated wire, straight chains in each direction, loops, branches and multiple adjacent roots. Bound work before mutation; do not assume the existing 20 check is sufficient.
4. Test all four spawn positions, cancelled spawns, repeated activation and multiplayer calls.
5. Verify all four kill orders, simultaneous deaths, null links, unload/reload and custom-spawned guardians.
6. Validate effect durations, explosion behavior, damage modifiers, recipe/loot pack changes and frame/tick-time impact in the target build.

## Evidence and credits

[Selected released methods, exact loot resources and wire examples](https://herbertofury.github.io/Advent-of-Ascension/four-guardians-evidence-1.12.2.json) · [Illustration source crops and hashes](https://herbertofury.github.io/Advent-of-Ascension/four-guardians-art-evidence-1.12.2.json).

AoA models, textures and systems: Tslat and contributors. Original documentation and static evidence tools. No Java, game or mod code was executed for this walkthrough.
