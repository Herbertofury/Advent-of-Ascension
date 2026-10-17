[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Staff rune costs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Runes-Casting-and-Hand-Safety-1.12.2)

# Historical blasters: energy, firing timing and Spark exceptions

**Minecraft 1.12.2 / AoA 3.3.6.** All **56 direct blaster registrations** are joined to released constructor identities. Ten base methods, eight Spark-specific methods and the shared resource consumer support the behavior notes below. Inputs are not final damage, measured DPS or a runtime compatibility certificate.

![Four historical blaster source-model portraits showing distinct energy and delay inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/blaster-inputs-and-ammo-1.12.2.webp)

## First use and troubleshooting

1. Equip the blaster in the **main hand**, which is the base weapon-hand result for these entries. The initial use check rejects a different hand.
2. Let the player's cooled attack strength reach **1**. The initial right-click path rejects a lower value.
3. Check Energy. The initial server preflight calculates the modified cost and compares the current Energy balance before starting active use. The generic Creative bypass in the later tick calculation does not automatically bypass this earlier check.
4. Hold use for the repeated firing path. A shot is attempted only on eligible countdown ticks and after the selected payment succeeds. Insufficient resources stop active use in the base tick path.
5. Read the Spark exception below before interpreting a zero base Energy or damage input.

## How the base Energy expression works

For the ordinary Survival tick path, the computed cost is:

**(1 + 0.3 × Greed level) × base Energy input × max(0, 1 − 0.07 × Recharge level)**

The full **Ghoulish** armor-set branch then multiplies this value by **0.7**. The actual implementation uses float32 arithmetic; displayed decimal examples are rounded. The tick calculation uses zero for Creative before that armor factor.

This is the blaster's calculated request, not a guarantee of the final resource deduction. Its shared `consumeResource` helper can bypass payment when resources are disabled or for Creative, applies resource-fortitude buffs, checks the resulting amount and updates the resource map. The blaster's earlier balance checks use their calculated value before that helper adjustment.

| Base Energy | Greed | Recharge | Full Ghoulish | Calculated Survival request, approximately |
|---:|---:|---:|---|---:|
| 20 | 0 | 0 | No | 20 |
| 20 | 1 | 0 | No | 26 |
| 20 | 0 | 2 | No | 17.2 |
| 20 | 1 | 2 | No | 22.36 |
| 20 | 1 | 2 | Yes | 15.652 |

The 4,144-case independent model includes edge levels to test the clamp; it does not establish that those levels or enchantment combinations are legally obtainable. The selected shared Energy consumer also schedules the next regeneration time at current global tick +50; other regeneration behavior is outside this one method.

## Countdown timing is not simply “wait one interval”

The selected tick gate is **remaining + delay ≤ 72,000** and **remaining % delay == 0**. It uses the remaining-use counter, not an elapsed counter starting at zero. In the independent model `elapsed = 72,000 − remaining`, the first eligible elapsed value is therefore:

| Delay input | First eligible elapsed count in this model |
|---:|---:|
| 1 | 1 |
| 7 | 12 |
| 11 | 16 |
| 13 | 19 |
| 14 | 26 |
| 20 | 20 |
| 100 | 100 |

Later eligible points remain spaced by the delay. These are integer-expression examples, not a measurement of actual input latency, callback ordering or wall-clock firing time. The evidence includes **3,618 timing cases across 18 distinct delays**.

## Durability is deferred in the base path

The ordinary tick path does not simply call one damage point after every shot. After a successful payment and fire call, it compares `(72,000 − count) / delay` with remaining item durability and may pass that accumulated value to `damageItem`. On stop, the base callback separately passes `(72,000 − useTicksRemaining − 1) / delay`.

Test the actual callbacks before promising exact wear per successful projectile. Countdown lifetime, stopped use, cancelled spawns and the near-break branch are separate cases. The zero-elapsed/delay-one model produces a negative release argument; that is a boundary to test, not proof of a player-triggerable repair exploit.

## Soul Spark and Light Spark are special

Both have zero ordinary damage and Energy registration inputs, but override the repeated-use and release callbacks. Their selected tick method fires on the countdown gate without calling the ordinary base Energy consumer, and their release callback is empty.

Their impact path first checks special exemptions and blaster immunity. For a non-Creative server-player shooter it then:

1. Requires at least **200 Energy** and **50 Soul** according to the direct balance checks.
2. Calls the shared resource consumer for each amount with `force = false`.
3. Searches the active hand, then the other hand, for the same weapon; it can return false if neither matches.
4. Damages the found weapon by **1**.
5. Calls the target's dead/removal method when the surrounding path reaches it.

The two resource-consumer boolean results are ignored in the inspected code. Resource calls also precede the same-weapon hand check. Those orderings are restoration test targets: do not claim a transaction-safe payment or a harmless/free Spark from the zero table inputs. This is not a promise that every mob is affected; exemption and immunity checks remain in front of the effect, and other game systems can change the outcome.

## All 56 source-backed entries

Each name opens its source-model portrait and lazy historical blaster panel, with recipe and drop searches kept in the same release. **Sixteen damage inputs are zero**; special projectiles and effects need individual review. Four Energy inputs are zero: Confetti Cannon, Confetti Cluster, Light Spark and Soul Spark.

| Blaster and portrait | Damage input | Delay · ticks | Durability | Base Energy input |
|---|---:|---:|---:|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-apoco_shower.webp" alt="Apoco Shower source-model portrait" width="72" height="72" loading="lazy"><br> [Apoco Shower](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ApocoShower.name) | 0 | 10 | 3760 | 80 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-atomizer.webp" alt="Atomizer source-model portrait" width="72" height="72" loading="lazy"><br> [Atomizer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Atomizer.name) | 11 | 8 | 3150 | 15 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-beamer.webp" alt="Beamer source-model portrait" width="72" height="72" loading="lazy"><br> [Beamer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Beamer.name) | 1 | 1 | 3240 | 3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-blast_chiller.webp" alt="Blast Chiller source-model portrait" width="72" height="72" loading="lazy"><br> [Blast Chiller](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BlastChiller.name) | 4 | 6 | 1750 | 20 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-blood_drainer.webp" alt="Blood Drainer source-model portrait" width="72" height="72" loading="lazy"><br> [Blood Drainer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BloodDrainer.name) | 0.1 | 1 | 2750 | 2.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-bone_blaster.webp" alt="Bone Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Bone Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoneBlaster.name) | 6 | 6 | 2430 | 20 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-bubble_horn.webp" alt="Bubble Horn source-model portrait" width="72" height="72" loading="lazy"><br> [Bubble Horn](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BubbleHorn.name) | 11 | 8 | 3200 | 15.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-colour_cannon.webp" alt="Colour Cannon source-model portrait" width="72" height="72" loading="lazy"><br> [Colour Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ColourCannon.name) | 45 | 40 | 1000 | 110 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-confetti_cannon.webp" alt="Confetti Cannon source-model portrait" width="72" height="72" loading="lazy"><br> [Confetti Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ConfettiCannon.name) | 0 | 10 | 1000 | 0 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-confetti_cluster.webp" alt="Confetti Cluster source-model portrait" width="72" height="72" loading="lazy"><br> [Confetti Cluster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ConfettiCluster.name) | 0 | 5 | 1500 | 0 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-dark_destroyer.webp" alt="Dark Destroyer source-model portrait" width="72" height="72" loading="lazy"><br> [Dark Destroyer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DarkDestroyer.name) | 0 | 100 | 3180 | 80 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-darkly_guster.webp" alt="Darkly Guster source-model portrait" width="72" height="72" loading="lazy"><br> [Darkly Guster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DarklyGuster.name) | 8 | 5 | 3790 | 7 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-death_ray.webp" alt="Death Ray source-model portrait" width="72" height="72" loading="lazy"><br> [Death Ray](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DeathRay.name) | 19 | 12 | 3840 | 17 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-doom_bringer.webp" alt="Doom Bringer source-model portrait" width="72" height="72" loading="lazy"><br> [Doom Bringer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DoomBringer.name) | 0 | 3 | 2820 | 15.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-eradicator.webp" alt="Eradicator source-model portrait" width="72" height="72" loading="lazy"><br> [Eradicator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Eradicator.name) | 1 | 1 | 2790 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-experiment_w801.webp" alt="Experiment W-801 source-model portrait" width="72" height="72" loading="lazy"><br> [Experiment W-801](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExperimentW801.name) | 37 | 50 | 5000 | 90 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-flowercorne.webp" alt="Flowercorne source-model portrait" width="72" height="72" loading="lazy"><br> [Flowercorne](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Flowercorne.name) | 2.5 | 4 | 2910 | 20 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-fragment.webp" alt="Fragment source-model portrait" width="72" height="72" loading="lazy"><br> [Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Fragment.name) | 3 | 2 | 3830 | 2.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-froster.webp" alt="Froster source-model portrait" width="72" height="72" loading="lazy"><br> [Froster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Froster.name) | 3.5 | 3 | 2800 | 7.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-gas_blaster.webp" alt="Gas Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Gas Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GasBlaster.name) | 0 | 1 | 2860 | 0.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-ghoul_gasser.webp" alt="Ghoul Gasser source-model portrait" width="72" height="72" loading="lazy"><br> [Ghoul Gasser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhoulGasser.name) | 0 | 1 | 3210 | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-gold_bringer.webp" alt="Gold Bringer source-model portrait" width="72" height="72" loading="lazy"><br> [Gold Bringer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoldBringer.name) | 0 | 3 | 3830 | 12.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-gravity_blaster.webp" alt="Gravity Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Gravity Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GravityBlaster.name) | 4 | 1 | 600 | 120 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-hell_horn.webp" alt="Hell Horn source-model portrait" width="72" height="72" loading="lazy"><br> [Hell Horn](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HellHorn.name) | 12.5 | 8 | 3800 | 11.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-illusion_revolver.webp" alt="Illusion Revolver source-model portrait" width="72" height="72" loading="lazy"><br> [Illusion Revolver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IllusionRevolver.name) | 14 | 10 | 3200 | 20 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-illusion_smg.webp" alt="Illusion SMG source-model portrait" width="72" height="72" loading="lazy"><br> [Illusion SMG](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IllusionSMG.name) | 4 | 3 | 3240 | 7 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-ion_blaster.webp" alt="Ion Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Ion Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IonBlaster.name) | 13 | 11 | 2810 | 28.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-iro_miner.webp" alt="Iro Miner source-model portrait" width="72" height="72" loading="lazy"><br> [Iro Miner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IroMiner.name) | 4 | 4 | 3060 | 7 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-laser_blaster.webp" alt="Laser Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Laser Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LaserBlaster.name) | 1.2 | 1 | 2840 | 2.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-light_blaster.webp" alt="Light Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Light Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LightBlaster.name) | 22.5 | 14 | 3810 | 20.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-light_spark.webp" alt="Light Spark source-model portrait" width="72" height="72" loading="lazy"><br> [Light Spark](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LightSpark.name) | 0 | 1 | 7 | 0 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-luna_blaster.webp" alt="Luna Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Luna Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunaBlaster.name) | 3 | 2 | 3200 | 4 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-mecha_blaster.webp" alt="Mecha Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Mecha Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechaBlaster.name) | 36 | 30 | 2770 | 80 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-mind_blaster.webp" alt="Mind Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Mind Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MindBlaster.name) | 19.5 | 14 | 3180 | 27.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-moon_destroyer.webp" alt="Moon Destroyer source-model portrait" width="72" height="72" loading="lazy"><br> [Moon Destroyer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MoonDestroyer.name) | 0 | 100 | 3750 | 60 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-moon_shiner.webp" alt="Moon Shiner source-model portrait" width="72" height="72" loading="lazy"><br> [Moon Shiner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MoonShiner.name) | 3.5 | 5 | 1810 | 17.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-odious.webp" alt="Odious source-model portrait" width="72" height="72" loading="lazy"><br> [Odious](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Odious.name) | 1 | 1 | 3190 | 1.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-orbocron.webp" alt="Orb-O-Cron source-model portrait" width="72" height="72" loading="lazy"><br> [Orb-O-Cron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Orbocron.name) | 18.5 | 13 | 3230 | 26.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-paralyzer.webp" alt="Paralyzer source-model portrait" width="72" height="72" loading="lazy"><br> [Paralyzer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Paralyzer.name) | 1.5 | 1 | 3900 | 1.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-party_popper.webp" alt="Party Popper source-model portrait" width="72" height="72" loading="lazy"><br> [Party Popper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PartyPopper.name) | 1.5 | 1 | 2810 | 3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-poison_plunger.webp" alt="Poison Plunger source-model portrait" width="72" height="72" loading="lazy"><br> [Poison Plunger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonPlunger.name) | 0 | 20 | 2600 | 50 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-power_ray.webp" alt="Power Ray source-model portrait" width="72" height="72" loading="lazy"><br> [Power Ray](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PowerRay.name) | 12.5 | 12 | 2490 | 38.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-proton.webp" alt="Proton source-model portrait" width="72" height="72" loading="lazy"><br> [Proton](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Proton.name) | 2.5 | 2 | 3000 | 4.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-reefer.webp" alt="Reefer source-model portrait" width="72" height="72" loading="lazy"><br> [Reefer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Reefer.name) | 5 | 4 | 3600 | 7 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-revolution.webp" alt="Revolution source-model portrait" width="72" height="72" loading="lazy"><br> [Revolution](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Revolution.name) | 0 | 20 | 2800 | 66 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-seaocron.webp" alt="Sea-O-Cron source-model portrait" width="72" height="72" loading="lazy"><br> [Sea-O-Cron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Seaocron.name) | 20.5 | 13 | 3800 | 18.5 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-skullo_blaster.webp" alt="Skullo Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Skullo Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkulloBlaster.name) | 3.5 | 2 | 3780 | 3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-soul_drainer.webp" alt="Soul Drainer source-model portrait" width="72" height="72" loading="lazy"><br> [Soul Drainer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SoulDrainer.name) | 0.2 | 1 | 3770 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-soul_spark.webp" alt="Soul Spark source-model portrait" width="72" height="72" loading="lazy"><br> [Soul Spark](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SoulSpark.name) | 0 | 1 | 5 | 0 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-soul_storm.webp" alt="Soul Storm source-model portrait" width="72" height="72" loading="lazy"><br> [Soul Storm](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SoulStorm.name) | 1.5 | 1 | 3190 | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-spirit_shower.webp" alt="Spirit Shower source-model portrait" width="72" height="72" loading="lazy"><br> [Spirit Shower](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpiritShower.name) | 0 | 10 | 2870 | 100 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-swarmotron.webp" alt="Swarm-O-Tron source-model portrait" width="72" height="72" loading="lazy"><br> [Swarm-O-Tron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Swarmotron.name) | 2 | 12 | 2400 | 33 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-toxic_terrorizer.webp" alt="Toxic Terrorizer source-model portrait" width="72" height="72" loading="lazy"><br> [Toxic Terrorizer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ToxicTerrorizer.name) | 0 | 7 | 2760 | 22 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-vortex_blaster.webp" alt="Vortex Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Vortex Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VortexBlaster.name) | 0 | 1 | 2870 | 130 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-whimsy_winder.webp" alt="Whimsy Winder source-model portrait" width="72" height="72" loading="lazy"><br> [Whimsy Winder](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WhimsyWinder.name) | 6 | 5 | 2830 | 13 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-withers_wrath.webp" alt="Wither's Wrath source-model portrait" width="72" height="72" loading="lazy"><br> [Wither's Wrath](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WithersWrath.name) | 7.5 | 7 | 800 | 21 |

## Restoration and optional remodel checklist

- Compare all 56 identity/input records; keep the two Spark callbacks separate from the 54 base-tick users.
- Test initial right-click preflight versus subsequent ticks, including Creative and low Energy.
- Compare Greed, Recharge, Ghoulish and resource-fortitude handling independently.
- Test first-shot timing for delays 7, 11, 13 and 14 as well as divisors of 72,000.
- Count successful effects, rejected spawns, resource changes and wear separately during long holds and release.
- For Sparks, test weapon switching, immunity, failed resource consumption and both hands without using valuable targets.
- Keep Energy/Soul semantics when adding an optional TaCZ-quality presentation; reloading remains optional.

[Released inputs and selected methods](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-blaster-inputs-1.12.2.json) · [Float32 cost and countdown models](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/blaster-cost-timing-models-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/blaster-art-evidence-1.12.2.json).
