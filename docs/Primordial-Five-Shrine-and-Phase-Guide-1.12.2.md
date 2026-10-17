# The Primordial Five: eight lamps, five phases

**Minecraft 1.12.2 / AoA 3.3.6.** Prepare the Dustopian shrine, light its eight required lamps and fight a sequential five-boss chain. This guide uses selected released methods and exact loot resources; it does not certify a live playthrough or a restored modern port.

[Worlds and travel](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions#dustopia) · [Four Guardians](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Four-Guardians-Altar-and-Rewards-1.12.2) · [Ancient Cavern](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2)

![Primordial Five phase order and historical models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/primordial-five-phase-chain-1.12.2.webp)

## Before the fight

- Find a Primordial Shrine in Dustopia and prepare a retreat route.
- Bring **Darkly Powder** to light unlit Dustopian Lamps. An initially unlit eight-lamp setup needs eight successful one-item lamp activations outside Creative.
- Bring supplies for the whole chain. Defeating the first boss is not the end.
- Avoid Peaceful: the shrine's server activation method explicitly rejects that difficulty.
- Do not relight and reactivate casually during a fight. The reviewed shrine callback does not contain a nearby-boss gate.

The inspected Dustopia generator checks a positive configured `primordialShrineSpawnChance`, makes its random trial, checks terrain and requests the structure. This is a source generation route, not a guaranteed location or independent promise that a converted world already contains it.

## 1. Light the correct eight lamps

Use **Darkly Powder on an unlit Dustopian Lamp without sneaking**. On the server, the selected lamp callback consumes one powder outside Creative and replaces the block with the lit Dustopian Lamp. It is a block interaction, not a recipe or a redstone-power test.

The shrine requires the actual **lit block type** at every position below. A different light source or an unlit lamp with a similar texture does not satisfy this equality check.

Coordinates are relative to the **shrine block**, with Minecraft world axes: **+X east, −X west, +Z south, −Z north, +Y up**. They are not relative to the direction the player faces.

| Lamp | X offset | Y offset | Z offset |
|---|---:|---:|---:|
| 1 | −3 | +1 | −5 |
| 2 | −3 | +1 | +5 |
| 3 | −1 | +1 | −4 |
| 4 | −1 | +1 | +4 |
| 5 | +1 | +3 | −3 |
| 6 | +1 | +3 | +3 |
| 7 | +1 | +5 | −1 |
| 8 | +1 | +5 | +1 |

The released structure places the shrine at local `(3,1,5)` and its eight initially unlit lamps at positions matching these offsets. Both the activation expressions and structure placement calls were checked. Do not confuse a structure-local coordinate with an absolute world height.

The inspected Dustopia world loot table lists Darkly Powder in a one-roll dimension-specific pool: empty weight 100, Dustopia Tokens 80, Darkly Powder 20 and Darkly Upgrade Kit 2. This table alone is not a guarantee that every Dustopian mob or action produces powder. Okazor also lists it among possible supplies, which is a possible return from the encounter rather than a guaranteed source for the first activation.

## 2. Activate the shrine

Once all eight required positions contain the lit block, activating the shrine on the server:

1. Chooses one of the eight positions and changes that lamp to its unlit form.
2. Creates Kajaros at the shrine's X/Z and **Y+3**.
3. Attempts to spawn it and sends the encounter message.

The shrine override does not consume an activation item from the player's hand. Its `getActivationItem` returns null, and the override bypasses the shared altar's ordinary item-payment branch. **Darkly Powder is paid to light lamps, not handed to the shrine as an additional ninth ingredient.**

The spawn return is discarded after the lamp change. A rejected spawn can therefore require recovery handling in a port; no transactional rollback is established by this method. The selected callback also has no explicit dimension gate or active-chain check. Those are restoration requirements to evaluate, not a claim that repeated activation is a stable intended farming loop.

## 3. Follow the five phases

| Order | Boss | Base health | Base damage getter | Main reviewed threat |
|---|---|---:|---:|---|
| 1 | [Kajaros](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Akajaros) | 1,750 | 23 melee | Debuffs and healing on its melee effect |
| 2 | [Miskel](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amiskel) | 1,300 | 14 projectile | Magic impacts, severe effects and healing |
| 3 | [Harkos](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aharkos) | 1,300 | 13 melee | Continuous healing attempts and random jumps |
| 4 | [Raxxan](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Araxxan) | 1,000 | 15 melee | Conditional random effects and healing |
| 5 | [Okazor](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aokazor) | 1,200 | 50 melee | Third-hit healing trigger within its reset window |

These are base getter values, not final damage received or a complete difficulty-adjusted health calculation. The first four server death callbacks create the next phase using a constructor that copies the previous boss's position and rotation. They discard the spawn result and mark the old entity dead. Do not assume a safe pause or automatic recovery from a cancelled transition.

### Kajaros: avoid feeding melee healing

The selected melee effect applies Blindness, Nausea and Slowness to a living target, each for **150 ticks at amplifier 2**, and attempts to heal Kajaros by 20. At nominal 20 TPS, 150 ticks is 7.5 seconds. Keep room to move and avoid treating close-range trades as damage only: its successful melee effect can both impair your response and recover its health.

### Miskel: avoid successful projectile impacts

The impact effect chooses between Blindness for **120 ticks at amplifier 15** and Wither for **80 ticks at amplifier 6**, then attempts to heal Miskel by 40. An effect's stored amplifier is not a promise that every effect visibly scales at every level. The ranged damage/impact path and server modifiers still matter. Reposition rather than standing still and trying to out-heal every hit.

### Harkos: keep pressure while retaining an escape route

On server living updates, while health is positive, Harkos attempts to heal **0.5**. A separate `nextInt(150) == 0` branch sets vertical motion to 0.8 and fall distance to −1. That is a random jump check, not a fixed jump timer. Its constructor enables slippery movement. Prepare for a moving, regenerating target; these source inputs are not a measured regeneration-per-second benchmark.

### Raxxan: distinguish the receiver of an effect

The server callback uses an `if / else if / else if` chain with random checks: a 1-in-100 first branch, a 1-in-100 second branch if the first failed, and a 1-in-200 healing branch only if both earlier branches failed. These are not three independent guaranteed timers.

The first branch looks for a non-Creative nearby player, but calls `addPotionEffect` on **Raxxan itself**, applying Nausea for 100 ticks at amplifier 4 and playing a sound. Do not rewrite that source behavior as “the nearby player receives nausea.” The second branch applies Invisibility to Raxxan for 25 ticks at amplifier 5; the last attempts to heal it by 100. The intended purpose of self-applied nausea is a review question, not a newly fixed bug.

### Okazor: break the hit sequence

On the server, its melee-effect callback increments `healCounter` and resets `healCountdown` to **80**. When the counter is **exactly 3**, it calls `heal(getMaxHealth())`.

Living updates decrement a positive countdown; only an update that begins with a non-positive countdown resets the counter. In the isolated countdown model, `(counter=2, countdown=80)` becomes `(2,0)` after 80 updates and `(0,0)` after 81. Actual hit/update ordering still needs live validation.

Avoid giving it three qualifying melee effects before the counter resets. The condition is equality with three, not “every third hit”: the selected method does not reset the counter immediately after the heal. Nor does the code establish a fixed four-second healing timer. Plan around avoiding contact and giving the reset window time to elapse rather than assuming a simple repeating cooldown.

## 4. Rewards and rearming

Each inspected phase table includes its own one-roll statue pool. Okazor's final rare pool has one roll with empty weight **100**, quality **−10**, plus Primordial Greatblade weight **18**, Primordial Bow **27** and Primordial Staff **27**. These are weights, not fixed percentage rates, and the rare weapon is not guaranteed. Supply and world-table pools remain separate.

Open each exact creature card above for its full illustrated table reference. A death callback starting the next phase does not mean every reward appears together or that every death condition permits the same loot path.

One lamp is turned off during a normal shrine activation. After the encounter, inspect all eight positions before rearming. If only that one lamp is off and the structure is otherwise intact, one successful Darkly Powder lamp activation restores that condition. Do not assume every damaged or partially restored shrine needs exactly one powder.

## Restoration acceptance checklist

- Check all eight positions individually, missing/wrong/unlit blocks, player orientation, sneaking and Creative lamp costs.
- Verify Peaceful rejection and define whether an explicit dimension or active-chain gate should be added.
- Test lamp mutation, rejected Kajaros spawn, simultaneous activation and repeat activation.
- Test all four phase transitions with spawn cancellation, unloaded chunks, save/reload and multiplayer.
- Check the exact recipients, durations and amplifiers of effects; retain a clear distinction between intended behavior and current callbacks.
- Test Okazor's second/third/fourth hit, 79/80/81-update boundaries and ordering within a tick.
- Test all five loot paths, modifiers, cleanup and performance on disposable saves before advertising a complete stable restoration.

## Evidence and credits

[Released methods, source hashes, lamp expressions, structure coordinates, loot tables and countdown examples](https://herbertofury.github.io/Advent-of-Ascension/primordial-five-evidence-1.12.2.json) · [Historical model inputs and image hashes](https://herbertofury.github.io/Advent-of-Ascension/primordial-five-art-evidence-1.12.2.json).

AoA systems, models and textures: Tslat and contributors. Original documentation, diagram and static analysis tools. No Java/game/mod execution or runtime fix is claimed.
