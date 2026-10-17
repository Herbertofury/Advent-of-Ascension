[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Skill guides](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Bestiary](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bestiary) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)

# Butchery and Innervation: combat pickups, Rage and health

> **Historical Minecraft 1.12.2 / AoA 3.3.6.** Selected released callbacks and helper methods support this guide. These are source-backed rules and independent arithmetic models, not a live combat or Enderloom compatibility test.

## The practical training loop

1. Fight eligible non-player targets with ordinary melee damage if you want chances to spawn **Bloodlust**. The selected helper checks an eligible hurt event, not only a finishing blow.
2. Defeat eligible non-player entities with player-linked kill credit for chances to spawn a **Heart Stone**. A player-owned tameable killer can also provide credit in the selected death callback.
3. Move into the temporary pickup before its entity age reaches **200 ticks**. At healthy 20 TPS that is approximately ten seconds, but actual elapsed time depends on server timing and other lifecycle behavior.
4. Bloodlust requests **Butchery XP**. A Heart Stone requests **Innervation XP** and attempts healing according to the collector’s displayed Innervation level.
5. Watch Rage when using Butchery criticals. The critical chance, damage multiplier, resource-consumption request and armor exemption are separate checks.

![Bloodlust and Heart Stone source models with collection rules](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/combat-skill-pickups-1.12.2.webp)

[Bloodlust creature card](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Abloodlust) · [Heart Stone creature card](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aheart_stone)

## Bloodlust: what qualifies?

The selected server-side hurt callback takes its outgoing-player branch only when the injured entity is not a player and the damage’s true source is a player. It calls the outgoing-damage handler, then checks melee classification and rejects absolute damage before trying Butchery criticals and a Bloodlust spawn.

The inspected melee helper requires a non-null true source, the same immediate and true source, and damage that is not projectile, thrown, magic, explosion or fire damage. A weapon’s appearance alone does not establish that it follows this path.

With skills enabled and a registered, non-blacklisted target, the Bloodlust helper has a **1 in 30 spawn attempt**. It does not require target death. This conditional attempt is not a guarantee of one pickup every thirty swings, and event cancellation/order or other mods can change whether the callback runs.

Bloodlust pickup happens on server collision with any player while the pickup is not dead. The selected collision method contains no owner/killer restriction. It requests XP, plays its collection sound and marks itself dead. Its living-update path also marks it dead at age 200 ticks. Multiplayer competition for a pickup must be tested rather than assumed owner-exclusive.

## Heart Stones: kill credit and eligibility

The selected death callback requires a non-player victim on the server and a suitable true-source killer. A player directly, or a tameable entity whose owner is a player, supplies player-linked credit. Then it checks:

- Victim maximum health is greater than 1.
- A random gate: **1 in 8** if the victim implements Minecraft’s IMob interface, otherwise **1 in 24**.
- The victim has a registered entity ID that is not in the inspected Heart Stone blacklist.

IMob is a code interface, not a visual guess that a creature looks hostile. The selected death branch does not itself contain the same skills-enabled guard used by Bloodlust spawning; XP awarding and other configuration effects occur further down their own paths.

On server collision, a Heart Stone uses the collecting player’s displayed Innervation level for both healing and the XP denominator. The healing helper only calls heal for an entity that is alive, has positive health, and is below maximum health. Full health therefore does not make the pickup’s XP request depend on a successful heal. The pickup is consumed afterward.

## How pickup XP is calculated

Both collision methods read **getLevelForDisplay**, rather than the gameplay-level getter used by the Butchery critical multiplier. Each requests:

`next-level XP lookup at displayed level ÷ skill-specific denominator`

The request then passes through the shared XP system, so configuration and skill XP modifiers can change the final award. It is not a fixed XP item value. The denominator tiers are:

| Displayed level | Bloodlust / Butchery denominator | Heart Stone / Innervation denominator |
|---|---:|---:|
| 1–4 | 4 | 4 |
| 5–14 | 7 | 7 |
| 15–29 | 11 | 11 |
| 30–44 | 20 | 25 |
| 45–59 | 35 | 40 |
| 60–74 | 45 | 60 |
| 75–89 | 60 | 80 |
| 90–94 | 80 | 100 |
| 95+ | 110 | 150 |

The final denominator remains 110 for Butchery and 150 for Innervation above level 100. The XP lookup itself changes formula beyond 100, so do not extrapolate the lower-level exponential indefinitely.

| Displayed level | Bloodlust base XP request | Heart Stone base XP request |
|---|---:|---:|
| 1 | 13.750 | 13.750 |
| 5 | 11.504 | 11.504 |
| 15 | 18.987 | 18.987 |
| 30 | 43.624 | 34.899 |
| 45 | 104.129 | 91.113 |
| 60 | 338.313 | 253.735 |
| 75 | 1059.913 | 794.935 |
| 90 | 3320.639 | 2656.511 |
| 95 | 3889.398 | 2852.225 |
| 100 | 6263.915 | 4593.538 |
| 101 | 5734.454 | 4205.266 |
| 999 | 8523.665 | 6250.688 |
| 1000 | 0.000 | 0.000 |

The selected lookup makes the base request at displayed level 101 lower than at 100. At 1000 it returns zero. These values preserve the released branch and float arithmetic; they are not smoothed into a made-up progression curve. Values above are rounded for reading, while the evidence retains the computed float values.

## Butchery criticals and Rage

![Critical-roll thresholds and Innervation health/healing formulas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/combat-skill-rage-health-1.12.2.webp)

The critical helper first requires both resources and skills to be enabled. It chooses an integer from **51 through 100** and succeeds when that integer is no greater than the current Rage value.

| Integer Rage | Successful outcomes out of 50 | Conditional critical-roll chance |
|---|---:|---:|
| 0 | 0 | 0% |
| 50 | 0 | 0% |
| 51 | 1 | 2% |
| 75 | 25 | 50% |
| 99 | 49 | 98% |
| 100 | 50 | 100% |
| 180 | 50 | 100% |

Fractional Rage is compared against the same integer roll; the table intentionally shows integer examples. This chance describes the selected critical helper after its gates, not every possible attack or final damage event.

| Gameplay Butchery level | Critical multiplier input |
|---|---:|
| 1–14 | 1.1× |
| 15–29 | 1.2× |
| 30–49 | 1.3× |
| 50–69 | 1.4× |
| 70–89 | 1.5× |
| 90–100 | 1.6× |

At Rage **180 or greater**, a successful critical multiplies that result by another approximately 1.3. For example, the top ordinary level multiplier and high-Rage factor combine to approximately 2.08 before other damage systems. This is not a final DPS or health-loss guarantee.

After applying the event amount multiplier, a recognized full Butchery set gets a separate random boolean that can skip the consumption call. Otherwise the helper requests **200 Rage with force enabled**. The resource-consumption method applies fortitude modifiers first and clamps the remaining value to zero; force means insufficient current Rage does not reject this request. Do not describe every critical as an unconditional exact 200-point drain after all modifiers.

Consuming Rage also sets its regeneration-delay marker to global tick +100. The selected regeneration method has additional timing checks, including a recovery branch for a marker too far ahead, and only calls the Rage regenerator while the stored value is below 200.

| Stored Butchery level | Rage regeneration request per eligible regen call |
|---|---:|
| 1–19 | 0.05 |
| 20–39 | 0.10 |
| 40–59 | 0.15 |
| 60–79 | 0.20 |
| 80–94 | 0.25 |
| 95–100 | 0.30 |

The player tick handler excludes null players, spectators and client worlds, and only invokes resource regeneration when resources are enabled. These request values are not an unconditional per-second recovery promise.

## Innervation health and healing

The inspected maximum-health helper returns **floor(min(level, 100) / 5)**. Its attribute modifier uses addition operation 0. That means one extra health point per five levels, capped at +20 health at level 100. In standard heart units, +20 health is +10 hearts; other health modifiers can change the final total.

The selected level-change callback removes and reapplies this modifier when the tier changes. Login/reload, configuration changes and interactions with other health mods remain acceptance tests rather than proof from the arithmetic alone.

| Displayed Innervation level | Heart Stone heal request | Standard heart equivalent |
|---|---:|---:|
| 1–7 | 0 health | 0 |
| 8–14 | 1 health | ½ heart |
| 15–36 | 2 health | 1 heart |
| 37–69 | 3 health | 1½ hearts |
| 70+ | 4 health | 2 hearts |

The armor classes declare level 100 and a 0.3 XP modifier for their own skill when their full-set callback is active. A modifier declaration is not an independent live test of every equipment/health/resource interaction.

## Troubleshooting and restoration targets

- A Bloodlust attempt is tied to the eligible melee hurt path; switching to projectiles or a different damage classification can stop that route.
- Heart Stone chances require suitable kill credit, a victim with more than one maximum health, a registry ID and blacklist eligibility.
- A pickup can expire while you fight. Neither inspected collision method checks an owner identity before awarding the collecting player.
- Heart Stones can award XP even when no healing is possible. Check healing eligibility and XP configuration separately.
- Do not read 100% on the conditional Rage gate as a promise that all attacks are Butchery criticals.
- Test damage-callback ordering, cancelled events, fake-player automation, tameable kill credit and modded damage types explicitly.
- Test two players touching the same pickup, chunk unload/reload, disconnect and the exact 199/200-tick boundary.
- Check displayed levels 100/101/999/1000, skill-disabled state and XP modifiers without silently substituting capped levels.
- Compare healthy/injured/dead healing paths and maximum-health modifier replacement across level changes and other health mods.
- The Bloodlust position constructor calls the superclass directly rather than delegating to its one-argument constructor; size/silent/fire-invulnerability initialization differences are a code-derived runtime test target, not a reproduced live failure here.

## Sources and limits

[Released callback and arithmetic evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/combat-skill-evidence-1.12.2.json) · [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/combat-skill-art-evidence-1.12.2.json)

35 selected released methods, 100 level-model rows, 201 integer Rage cases, four displayed-level boundary examples and two source-model portraits support this guide. No Java or Minecraft game code was executed. This is a scoped behavior reference, not complete modpack combat acceptance.

[Pinned official source](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source) provides readable context; selected released bytes determine the inspected behavior. AoA assets and designs: Tslat and contributors. Original documentation and diagrams.

[Historical Anima pickups](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) · [Skill Crystal targeting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.12.2) · [Skills and progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression)
