[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Skills](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Combat skills](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2)

# Expedition: sprint training, selectable bonuses and fall protection

> Historical Minecraft 1.12.2 / AoA 3.3.6. This walkthrough follows selected released methods and independent arithmetic models. It is not live testing of your Enderloom build or modpack.

![Expedition source GUI icons, sprint rules and three selectable bonuses](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/expedition-training-and-bonuses-1.12.2.webp)

## A practical training loop

1. Prepare a safe, level route with enough food to sprint. Dangerous drops are unnecessary for the inspected training action.
2. Sprint while grounded, outside Creative mode and without riding an entity. The server checks the END phase of the player tick.
3. Stay eligible when player age reaches a multiple of 140 ticks. That boundary requests Expedition XP; merely walking is not the selected training action.
4. Open the Advent player/skills tab and click the Expedition skill icon to cycle its optional bonus.
5. Use the fall-multiplier table as a preparation aid, not permission to assume a lethal drop is safe. Other damage and armor behavior still applies.

## The timer is player age, not sprint duration

The helper checks `ticksExisted % 140 == 0` while sprinting. At healthy 20 TPS, 140 ticks corresponds to about seven seconds, but starting a sprint does not start a fresh seven-second timer. The selected code does not measure distance traveled or require uninterrupted sprinting throughout that interval.

The outer callback must also see a server-side player who is grounded, not riding and not in Creative mode. Jumping, mounted travel and airborne movement can therefore miss an otherwise eligible tick. Other mods, event order and server timing require target-build tests.

The base request uses the effective gameplay level, which caps at 100 when skills are enabled:

`getXpRequiredForNextLevel(effective level) / getXpDenominator(effective level)`

Shared XP modifiers and settings apply after this request. These values do not guarantee final XP per second.

| Effective level | XP denominator | Base request at first level of row |
|---|---:|---:|
| 1–4 | 22 | 2.500 |
| 5–9 | 35 | 2.301 |
| 10–14 | 45 | 2.882 |
| 15–19 | 65 | 3.213 |
| 20–24 | 90 | 3.737 |
| 25–34 | 150 | 3.612 |
| 35–39 | 190 | 7.395 |
| 40–44 | 230 | 9.839 |
| 45–49 | 280 | 13.016 |
| 50–54 | 360 | 16.304 |
| 55–59 | 450 | 21.007 |
| 60–64 | 540 | 28.193 |
| 65–69 | 650 | 37.721 |
| 70–74 | 750 | 52.650 |
| 75–79 | 850 | 74.817 |
| 80–84 | 950 | 107.811 |
| 85–89 | 1000 | 164.948 |
| 90–94 | 1100 | 241.501 |
| 95–98 | 1200 | 356.528 |
| 99–100 | 1300 | 481.840 |

The final column is an example at the row’s first level, not one flat XP value for the whole tier. The next-level lookup changes within each row.

## Choose a bonus

Clicking the Expedition icon sends its toggle packet. The inspected state cycles through none, Speed, food and water breathing, then back to none. The stored values 0–3 and 4–7 preserve two separate state bands; both select their bonus using remainder modulo 4. Do not flatten the whole stored field into a simple UI index when porting or saving it.

| Mode | Additional gate | Request when its random gate succeeds |
|---|---|---|
| None | No optional branch | No optional bonus; sprint XP and passive fall handling remain separate |
| Speed | Sprinting; player age divisible by 600; no existing Speed potion effect | Speed amplifier 4 for 80 ticks, ambient true, particles false |
| Food | Sprinting; player age divisible by 600 | FoodStats addStats with 5 food and saturation modifier 0.3 |
| Water breathing | In water; player age divisible by 500 | Water Breathing amplifier 0 for 400 ticks, ambient true, particles false |

All three branches inherit the outer grounded, non-riding, non-Creative server-player gate. In particular, water breathing is not an unconditional swimming timer: being in water alone is insufficient when the outer grounded check fails.

At 20 TPS, the scheduling periods are approximately 30 seconds for Speed/food and 25 seconds for water breathing. The requested potion durations are approximately four and twenty seconds respectively. Timing is based on player age and game ticks, not wall-clock promises.

Each optional branch draws an integer from 0 through 109 and succeeds when it is less than the effective level. At ordinary effective levels 1–100 that gives level/110 successful outcomes: about 0.91% at level 1, 45.45% at 50 and 90.91% at 100, conditional on the relevant state/timing checks. A bonus is not guaranteed at every boundary.

The Speed branch rejects an already active Speed effect, regardless of whether that effect would be weaker. The food call uses vanilla FoodStats and its caps; do not describe it as five guaranteed extra saturation points. The water branch does not contain the same existing-effect rejection; potion combining remains part of Minecraft’s own effect handling.

## Passive fall multiplier

The Expedition fall helper returns immediately if the event is already cancelled. Otherwise it multiplies the current event damage multiplier according to effective level:

| Effective level | Multiplier applied | Reduction of this multiplier input |
|---|---:|---:|
| 1–9 | 1.00 | 0% |
| 10–19 | 0.95 | 5% |
| 20–29 | 0.90 | 10% |
| 30–39 | 0.85 | 15% |
| 40–49 | 0.80 | 20% |
| 50–59 | 0.70 | 30% |
| 60–69 | 0.60 | 40% |
| 70–79 | 0.50 | 50% |
| 80–89 | 0.40 | 60% |
| 90–100 | 0.30 | 70% |

This is a multiplier applied to an existing fall-event value. Rounding, fall distance, other handlers, armor and subsequent damage processing can change actual health loss. “70%” in this table is not a universal guarantee of 70% less final damage from every fall.

The player-fall callback runs player-data fall handling before the Expedition helper. This ordering matters when combining the skill with armor or another cancellation path.

## Expedition armor interactions

The selected armor class declares level 100 and adds a 0.3 Expedition XP modifier in its full-set callback. Its full-set landing callback multiplies the event multiplier by 0.5. If both selected multipliers apply at level 100, their input factors combine to approximately 0.15, before remaining damage processing; this is not a live damage result.

Its effect callback requests Speed amplifier 1 and Water Breathing amplifier 0 with duration -1, and refreshes Night Vision to 300 ticks when absent or below 250 ticks. The unusual -1 duration must be validated against actual effect-update behavior; it is not sufficient evidence for a promise of permanent effects.

The full-set unequip callback removes an active Night Vision effect when its remaining duration is at most 300 ticks. The inspected method does not check the effect’s original provider, so interaction with another mod’s short Night Vision is a specific regression-test target.

Any active Speed supplied by armor or another source can also block the selectable Speed branch’s “no existing Speed” condition. Inspect actual effect state rather than assuming these bonuses stack.

## Disabled skills and porting checks

The released shared getLevel helper returns 100 when skills are disabled, while addXp exits when skills are disabled. The selected Expedition running/fall paths do not add a separate skills-enabled guard before their bonus or multiplier logic. Consequently, disabling XP and disabling all skill-derived effects must be tested as separate behaviors; do not promise that one setting turns off both.

The toggle packet handler directly calls incrementExpeditionBoost in the inspected method. No server-task scheduling call is present there. A port should follow the target loader’s safe packet-thread rules and test rapid toggles, disconnects and saves rather than copying a historical threading assumption.

- Test tick boundaries 139/140/141, 499/500/501 and 599/600/601 with eligibility changing on the boundary.
- Compare grounded sprinting, walking, jumping, mounted travel, Creative and in-water-but-not-grounded states.
- Compare no Speed, weaker Speed, stronger Speed and armor-provided Speed.
- Test ordinary and disabled-skills settings, effective/displayed level differences and XP modifiers.
- Check all eight stored toggle values and their two four-state cycles without erasing unrelated state.
- Compare cancelled falls, multiple multiplier handlers, full-set equip/unequip and other Night Vision providers.

## Evidence and limits

[Released callback evidence and 100-level arithmetic models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/expedition-training-evidence-1.12.2.json) · [Source GUI crop provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/expedition-training-art-evidence-1.12.2.json)

18 selected released methods, 100 level-model rows and eight toggle-state transitions support this walkthrough. Five GUI crops use pinned source coordinates. No Java or Minecraft code was executed.

[Pinned official source context](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source). AoA artwork and designs: Tslat and contributors. Original documentation diagram.

[Hunter training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2) · [Combat pickups](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
