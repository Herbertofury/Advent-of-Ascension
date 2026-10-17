# Ancient Cavern and deity shrines · 1.12.2

**Minecraft 1.12.2 / AoA 3.3.6.** Follow the historical route from a Blank Realmstone to Crystevia, complete the timed Construct task, then earn tribute inside Ancient Cavern and use its four deity shrines. This is a released-source walkthrough and restoration reference, not certification that these systems already work in a newer Enderloom candidate.

[First 1.12.2 portal](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Worlds and version differences](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions#ancient-cavern) · [Legacy creature reference](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2)

![Four deity routes, tribute sources, shrines and bosses](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ancient-cavern-shrine-routes-1.12.2.webp)

## Before you leave

- Prepare the corresponding skill level before choosing a shrine: Hunter, Runation, Foraging or Infusion **70**, with the skill system enabled.
- Carry the Blank Realmstones needed for the route. Their checked constructor sets maximum stack size **one**; progress belongs to the selected stack’s capability.
- Bring your combat supplies and a return plan. Do not plan this as a freely buildable survival dimension.
- **Do not farm 200 tribute elsewhere and assume it survives entry.** The checked server dimension-change callback resets all tribute. You earn it again from the cavern’s dedicated creatures.

## 1. Reach Deeplands and obtain the Crystevia key

1. Use the [historical first-portal guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) to obtain your Blank Realmstone and prepare the frame.
2. The checked 1.12.2 harvest-event path awards a **Deeplands Realmstone** for an eligible ore block at **Y ≤ 5**, consuming one Blank Realmstone. This is a conditional event branch, not a crafting recipe or an arbitrary stone-mining reward.
3. In Deeplands, obtain a **Deep Crystal block**. The checked biome decorator places Deep Crystal at **Y 19** with randomly selected X/Z offsets; this is a source placement rule, not a guaranteed search coordinate or time.
4. Find a **Case Construct**. Interact while holding the Deep Crystal block item and carrying a Blank Realmstone. The server callback consumes one Blank Realmstone and gives a Crystevia Realmstone through the item-delivery helper.
5. The checked callback does not explicitly consume the held Deep Crystal. Avoid treating it as a repeated crafting ingredient without checking the target build.

[![Case Construct source-model study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CaseConstructModel-thumb.webp)](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CaseConstructModel.png)

[Inspect Case Construct and its source fields](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acase_construct). Keep inventory room and collect any dropped overflow safely.

## 2. Complete the five-Construct task in Crystevia

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ancient-cavern-realmstone-1.12.2.webp" width="190" height="190" alt="Ancient Cavern Realmstone 1.12.2 source-item study">

Carry a Blank Realmstone and personally get credited for killing **five distinct Construct classes** in Crystevia within a rolling **600-game-tick window**. At the nominal 20 ticks per second that is 30 seconds; server lag can change the wall-clock duration.

The caller checks the Crystevia dimension type, a class name containing `Construct`, a player as the damage’s true source, and a Blank Realmstone in inventory. The tracked key is the victim’s Java class, not its display name. Repeated kills of one type refresh that type’s timestamp but do not count as additional distinct types. Pet-owner credit used by tribute creatures below is a different callback; do not assume it satisfies this task.

The seven checked Crystevian Construct references are:

| Construct | Source-model preview |
|---|---|
| [Construct of Flight](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_flight) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfFlightModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfFlightModel-thumb.webp" width="120" height="120" alt="Construct of Flight 1.12.2 source-model study"></a> |
| [Construct of Mind](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_mind) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfMindModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfMindModel-thumb.webp" width="120" height="120" alt="Construct of Mind 1.12.2 source-model study"></a> |
| [Construct of Range](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_range) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfRangeModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfRangeModel-thumb.webp" width="120" height="120" alt="Construct of Range 1.12.2 source-model study"></a> |
| [Construct of Resistance](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_resistance) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfResistanceModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfResistanceModel-thumb.webp" width="120" height="120" alt="Construct of Resistance 1.12.2 source-model study"></a> |
| [Construct of Speed](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_speed) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfSpeedModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfSpeedModel-thumb.webp" width="120" height="120" alt="Construct of Speed 1.12.2 source-model study"></a> |
| [Construct of Strength](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_strength) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfStrengthModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfStrengthModel-thumb.webp" width="120" height="120" alt="Construct of Strength 1.12.2 source-model study"></a> |
| [Construct of Terror](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_terror) | <a href="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfTerrorModel.png"><img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfTerrorModel-thumb.webp" width="120" height="120" alt="Construct of Terror 1.12.2 source-model study"></a> |

**Boundary detail:** entries older than `currentWorldTime − 600` are removed. A timestamp exactly 600 ticks old survives that comparison. Once at least five distinct entries remain, the method consumes the Blank Realmstone and gives the Ancient Cavern Realmstone. These boundary cases are checked with independent arithmetic tests, not a live timed run.

## 3. Enter the cavern and understand its restrictions

Use the era-appropriate frame and the Ancient Cavern Realmstone. The inspected teleporter returns **(0, 18, 0)** for entry into the cavern; shrine return branches use a separate central destination **(0, 17, 0)**. These are source coordinates, not confirmation of safe terrain in a converted world.

The provider restricts building/mining and rejects several held-item interaction categories. A torch exception in a placement/mining helper must be considered together with the interaction checks; this walkthrough does not promise unrestricted torch placement. Its source also disables ordinary local respawning. Prepare before entering and validate return travel on copied saves when porting the system.

## 4. Earn tribute inside the cavern

The generated-room source binds **Bloodsucker and Flowerface spawners in Room 3**, and **Angelica and Rock Critter spawners in Room 5**. The corresponding released generation methods actually read those spawner-state fields. This is a source construction connection, not a measured spawn frequency.

Each selected creature’s death callback checks the Ancient Cavern dimension and awards **+8 tribute** to its deity when credited to a player, or to the player owner of a tameable damage source. Other kill-credit paths are not silently assumed.

| Deity | Tribute creature | Shrine boss | Required skill |
|---|---|---|---|
| Erebon | [Bloodsucker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Abloodsucker) | [Penumbra](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Apenumbra) | Hunter 70 |
| Luxon | [Angelica](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aangelica) | [Horon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahoron) | Runation 70 |
| Pluton | [Rock Critter](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Arock_critter) | [Goldorth](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agoldorth) | Foraging 70 |
| Selyan | [Flowerface](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aflowerface) | [Coniferon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconiferon) | Infusion 70 |

With no other changes or multipliers, **25 eligible +8 kills** fill a meter from 0 to its 200 cap. Each deity has its own meter. Player death and dimension changes have reset callbacks, so do not treat tribute as permanently banked progression.

### Holy Sword changes both gains and costs

The shared `addTribute` helper doubles the **signed amount** when the Holy Sword is held, then clamps the meter to **0–200**. It does not restrict that multiplier to positive gains.

- A +8 gain becomes **+16**; 13 such gains reach the cap from zero.
- A shrine’s −20 input becomes **−40**; a full meter becomes **160**, rather than 180.
- Negative changes cannot push the stored meter below zero.

This is a checked source behavior, not a newly applied fix or a claim about every modern release.

## 5. Activate the correct shrine

Activate without sneaking, on the server, in the Ancient Cavern dimension and with the AoA player capability available. For the entering-room branch, the shrine requires the associated skill at least **70** and tribute at least **200**, then passes **−20** to the shared tribute helper before spawning the boss and teleporting the player.

**The 200 gate is not a 200-point fee.** With no Holy Sword multiplier, the stored meter goes from 200 to 180. Creative mode bypasses these skill/tribute gates. The inspected getters also return level 100 when skills are disabled and tribute 200 when resources are disabled, so global configuration can alter the effective gate.

Augury 70 appears only in commented source beside these checks; the released shrine method references Hunter, Runation, Foraging and Infusion, with **no Augury skill check**.

| Deity / boss | Entering-room player destination | Boss spawn position |
|---|---|---|
| Erebon / Penumbra | `-70, 18, 80` | `-51, 18, 92` |
| Luxon / Horon | `80, 18, -70` | `80, 18, -70` |
| Pluton / Goldorth | `80, 18, 80` | `80, 18, 80` |
| Selyan / Coniferon | `-60, 18, -65` | `-60, 18, -65` |

These destinations depend on the shrine’s coordinate-zone branch. When that entry condition is false, the method keeps its central return destination instead of charging/spawning again. They are not commands to teleport into ungenerated rooms.

## 6. Inspect the rewards before choosing a boss

![Signature rare-pool rewards and separate statue rewards](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ancient-cavern-signature-rewards-1.12.2.webp)

Each of these four released boss tables has a one-roll **rares** pool with the same base structure: empty weight **100** and quality **−10**, the deity’s Stickler weight **28**, Scythe weight **19**, and Banner weight **5**. Luck can affect the empty entry’s effective weight; these numbers are not fixed percentage drop rates.

A separate one-roll **statue** pool contains that boss’s statue. Supply and shared rare-table pools remain separate. The illustration shows signature rewards, not everything awarded together or every possible supply item. Open the boss’s exact creature record above and expand its loot section for the complete version-specific table reference and item pictures.

## 7. Fight each shrine boss on its own terms

These are release-specific tactics inferred from the checked callbacks. They do not certify a successful live fight or a modern port. Health and damage below are base getter inputs before configuration, attributes, mitigation and other modifiers.

### Coniferon: change weapon class and manage the pull

Coniferon's special immunity delegates to AoA's **gun-damage classifier**: the source must have damage type `gun` and be marked as a projectile. Choose an alternative damage class instead of repeatedly spending gun ammunition into that immunity. This does not claim that every non-gun attack automatically succeeds.

Its current attack target receives horizontal pull while not sneaking, using the sign of each horizontal offset ×0.029. Sneaking skips that pull branch, but not melee damage, poison or other effects. Unlike Klobber's area query, this selected override operates on the current target and contains no explicit distance test of its own. Do not invent a pull radius from the model size.

A random `nextInt(300) == 0` branch can apply Poison for 60 ticks at amplifier 0 and request a 70-tick vine screen overlay for a server player. A successful melee effect applies Slowness for 140 ticks at amplifier 2, then uses Coniferon's own motion and the target's knockback resistance for added velocity. At a nominal 20 ticks per second these potion durations correspond to 3 and 7 seconds; the random trigger is not a fixed 15-second cooldown. Prepare for impaired movement and do not rely on crouching as universal protection.

Base references: **4,000 health, 25 melee damage**, movement getter 0.2875 and knockback-resistance getter 0.3. These movement values are not measured blocks per second.

### Horon: protect your resource budget

Horon's special immunity uses AoA's **ranged-damage helper**, which is narrower than “anything fired from a distance.” That helper checks projectile sources excluding the `gun` damage type, or `thrown`, and excludes the helper's magic classification. Guns and magical attacks are therefore different classifications for this check; validate your chosen weapon in the target build rather than assuming its visual style defines its damage type.

When Horon's successful melee effect hits a player, it asks the resource helper to consume **60 Energy, 20 Creation and 20 Soul**, with forced payment. The shared helper applies fortitude adjustments, clamps remaining resources at zero, and can bypass payment when resources are disabled or for the relevant Creative case. These are requested costs, not an unconditional measured drain of those exact amounts. Keep enough reserve for your escape and attack plan instead of planning only around health.

On eligible server living updates, an independent 1-in-60 check requests an explosion of strength 2. The selected explosion overload uses `doStrongerMobGriefing` for its destructive flag and passes a non-fiery flag; this is not a guarantee about every block or explosion-event modification. A separate 1-in-400 check with an attack target applies Weakness for 120 ticks at amplifier 3. Avoid describing either random check as a fixed timer.

Base references: **3,000 health, 24 melee damage**, movement getter 0.2875 and knockback-resistance getter 0.3. Space your engagements and monitor resource bars after contact.

### Goldorth: leave room for a heavy melee pursuer

The selected class is comparatively straightforward: **3,000 base health, 17 base melee damage**, movement getter 0.329 and knockback-resistance getter 1. Its constructor enables the slippery-movement flag and supplies an AI movement-speed value of 1.6. Neither number is a measured run speed, and the resistance getter is not proof of immunity to every modded displacement mechanic.

A practical source-derived plan is to keep a retreat lane and avoid depending on ordinary knockback to hold it away. The selected class does not define the Coniferon/Horon special-immunity overrides. That bounded observation is not a claim that inherited code, difficulty or other mods cannot alter combat behavior.

### Penumbra: avoid feeding the summon loop

Penumbra creates magic-type Penumbra Shots and has base getters of **3,000 health and 18 projectile damage**. The ranged superclass applies its own damage path and invokes the impact-effect callback only when that damage path reports success. Penumbra's override also returns early for the eight creature classes listed below. A projectile simply touching a wall is not the same checked summon trigger: the inherited block-impact callback is empty in this reviewed path.

On an eligible impact effect, Penumbra chooses one of eight alternatives and attempts to spawn it at the projectile's coordinates:

- Occulent
- Alarmo
- Shifter
- Devourer
- Basilisk
- Apparition
- Stalker
- Hellspot


| Summoned creature | Historical source-model preview |
|---|---|
| [Occulent](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aocculent) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-OcculentModel-thumb.webp" width="120" height="120" alt="Occulent historical source-model study"> |
| [Alarmo](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aalarmo) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-AlarmoModel-thumb.webp" width="120" height="120" alt="Alarmo historical source-model study"> |
| [Shifter](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashifter) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ShifterModel-thumb.webp" width="120" height="120" alt="Shifter historical source-model study"> |
| [Devourer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Adevourer) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-DevourerModel-thumb.webp" width="120" height="120" alt="Devourer historical source-model study"> |
| [Basilisk](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Abasilisk) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-BasiliskModel-thumb.webp" width="120" height="120" alt="Basilisk historical source-model study"> |
| [Apparition](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aapparition) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ApparitionModel-thumb.webp" width="120" height="120" alt="Apparition historical source-model study"> |
| [Stalker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astalker) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-StalkerModel-thumb.webp" width="120" height="120" alt="Stalker historical source-model study"> |
| [Hellspot](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahellspot) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/23120805126274f701fbc573-thumb.webp" width="120" height="120" alt="Hellspot historical source-model study"> |

The spawn call's return is ignored. This is one random spawn attempt per eligible effect, not a guarantee that eight mobs appear together, that every projectile creates a mob, or that a cancelled spawn succeeded. Keep moving to reduce successful hits and leave space to manage summoned enemies; do not mistake the roster for a guaranteed simultaneous wave. Those eight classes are also excluded from Penumbra's selected entity-impact processing, so they are not ordinary recipients of the same summon-producing hit path.

### Combat acceptance tests for the restored mod

- Test gun, arrow, thrown, magic, fire and explosion damage classifications independently; preserve native immunity distinctions without breaking other weapon mods.
- Verify crouching versus pull, target changes, knockback resistance and client/server velocity synchronization.
- Check potion amplifier/duration values, screen-overlay timing and cleanup after death, return travel or disconnect.
- Verify Horon's forced resource payments with low/zero resources, fortitude adjustments, disabled resources and Creative mode.
- Check explosion game-rule behavior on disposable test worlds, with protection/event-cancellation mods enabled.
- Confirm Penumbra's successful-hit gate, block impacts, eight exclusions, spawn cancellation, multiplayer ownership and accumulated summon performance.
- Profile the actual target build before optimizing per-tick queries. These static findings establish review targets, not measured FPS or tick-time improvements.

[Released combat methods and helper evidence](https://herbertofury.github.io/Advent-of-Ascension/ancient-cavern-combat-evidence-1.12.2.json).

## Restoration acceptance checklist

1. Preserve the 1.12.2 dimension/configuration identity and save mappings; do not assume this historical provider exists in the modern dimension JSON list.
2. Test the full prerequisite route, the one-stack Blank Realmstone capability, distinct-class tracking, exact 600/601-tick boundaries and player/pet kill-credit differences.
3. Test tribute reset on entry, exit, death and reconnect, and earning tribute from all four in-cavern spawner creatures.
4. Compare skill 69/70, tribute 199/200, Creative and disabled-system settings. Test Holy Sword gains and negative shrine deltas explicitly.
5. The shrine discards the boolean result of `spawnEntity`, then proceeds with teleporting. Test a cancelled/rejected spawn and decide how a port should handle tribute and movement atomically; this is not a report of a reproduced in-game failure.
6. Test room-side returns, blocked destinations, respawn behavior, building restrictions, repeated activation, multiplayer and save/reload before claiming a finished restoration.
7. Keep source-derived event handling; profile the target build before adding repeated global entity scans or background work.

## Evidence and credits

[Released methods, room-spawner bindings, four loot tables and boundary examples](https://herbertofury.github.io/Advent-of-Ascension/ancient-cavern-evidence-1.12.2.json) · [Artwork inputs and hashes](https://herbertofury.github.io/Advent-of-Ascension/ancient-cavern-art-evidence-1.12.2.json).

AoA systems, models and textures: Tslat and contributors. Original source-reading tools, diagrams and documentation. No Java/game/mod code was executed for this guide.
