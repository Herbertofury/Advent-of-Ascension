# Blasters and Spirit: manage charge, cost and recovery

[Open the item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Staff rune preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Rune-Costs-and-Preparation-1.21.1) · [Gun ammunition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Statistics-and-Ammunition-1.21.1)

![Six released blaster models with base Spirit and charge inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/blaster-statistics-overview-1.21.1.webp)

**Scope:** 56 released blaster registrations in Minecraft 1.21.1 / AoA 3.7.16.1. Configured damage, shot interval, Spirit cost, charge-up input and durability are joined from released builders and item factories. These are not measured DPS, beam ranges or wall-clock firing timings.

## Before a fight

1. Check your weapon’s **base Spirit cost**, not a bullet or staff-rune requirement copied from another weapon family.
2. Check charge-up and interval separately. They are different fields used at different points of the firing path.
3. Read the current Spirit meter and allow a recovery margin. Do not assume you begin every encounter at the configured maximum.
4. Test the actual spell or projectile. A zero damage input can accompany a special effect rather than an empty weapon.
5. Check enchantments, armour and modified components before calculating how many shots you can afford.

## How Spirit recovers in the inspected release

The released Spirit resource JSON sets maximum 200, passive regeneration input 0.04 per tick, damage-based regeneration input 0.4 per eligible damage, and inverse-health regeneration modifier 3.5. Active data can replace these settings.

The released health scaling is `1 + (1 - currentHealth / maximumHealth) × (3.5 - 1)` with those stock settings. That factor multiplies either the passive input or the eligible-damage input.

| Health fraction | Stock factor | Passive input per tick | Input from 10 eligible damage |
|---|---:|---:|---:|
| Full | 1 | 0.04 | 4 |
| Half | 2.25 | 0.09 | 9 |
| Quarter | 2.875 | 0.115 | 11.5 |

These are arithmetic examples from the inspected configuration and method, before capacity clamping. They are not measured recovery rates and do not imply that taking damage is a safe strategy. Actual elapsed time depends on game ticks.

The damage-triggered path excludes sources in `aoa3:no_spirit_regen`. The bundled tag lists optional AoA vulcane, energy-projectile, magic-projectile, magic-effect and energy-effect types, vanilla explosion/player-explosion/fireworks, and the `neoforge:is_magic` tag. Tag membership can change with active data. Do not assume every blaster hit refills the Spirit it just spent.

## Why the base cost may differ from actual payment

The released cost path applies Spirit-consumption enchantment processing, then multiplies by `1 + modifiedAmmoCost × 0.3`. A full Ghoulish armour set applies a further 0.7 factor. Creative shot-consumption handling and non-player cases have their own branch. The table retains the base component value instead of silently guessing the player’s final cost.

## Charge-up versus repeated shots

The inspected use path checks the appropriate hand, blocking and attack-strength state, relevant off-hand restrictions and available Spirit before starting use. The server tick path has a charge-minus-two guard, checks the player cooldown and attempts payment before firing. A successful attempt applies durability handling; a configured interval greater than one adds a player cooldown. A failed firing attempt releases use.

These details are why the charge-up field is not a guaranteed stopwatch duration and why dividing damage by the interval would be an incomplete DPS claim. Subclasses and actual tick scheduling still matter.

## Released blaster defaults

| Weapon | Damage input | Interval (ticks) | Base Spirit | Charge-up input (ticks) | Durability |
|---|---:|---:|---:|---:|---:|
| [Apoco Shower](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aapoco_shower) | 0 | 10 | 80 | 10 | 3760 |
| [Atomizer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aatomizer) | 11 | 8 | 15 | 8 | 3150 |
| [Beamer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abeamer) | 1 | 1 | 3 | 1 | 3240 |
| [Blast Chiller](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablast_chiller) | 4 | 6 | 20 | 20 | 1750 |
| [Blood Drainer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ablood_drainer) | 0.1 | 1 | 2.5 | 1 | 2750 |
| [Bone Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abone_blaster) | 6 | 6 | 20 | 6 | 2430 |
| [Bubble Horn](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abubble_horn) | 11 | 8 | 15.5 | 8 | 3200 |
| [Colour Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acolour_cannon) | 45 | 40 | 110 | 40 | 1000 |
| [Confetti Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aconfetti_cannon) | 0 | 10 | 0 | 10 | 1000 |
| [Confetti Cluster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aconfetti_cluster) | 0 | 5 | 0 | 5 | 1500 |
| [Dark Destroyer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adark_destroyer) | 0 | 100 | 80 | 100 | 3180 |
| [Darkly Guster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adarkly_guster) | 8 | 5 | 7 | 5 | 3790 |
| [Death Ray](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adeath_ray) | 19 | 12 | 17 | 12 | 3840 |
| [Doom Bringer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adoom_bringer) | 0 | 3 | 15.5 | 3 | 2820 |
| [Eradicator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aeradicator) | 1 | 1 | 2 | 1 | 2790 |
| [Experiment W-801](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aexperiment_w_801) | 37 | 50 | 90 | 50 | 5000 |
| [Flowercorne](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aflowercorne) | 2.5 | 4 | 20 | 4 | 2910 |
| [Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afragment) | 3 | 2 | 2.5 | 2 | 3830 |
| [Froster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afroster) | 3.5 | 3 | 7.5 | 3 | 2800 |
| [Gas Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agas_blaster) | 0 | 1 | 0.5 | 1 | 2860 |
| [Ghoul Gasser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aghoul_gasser) | 0 | 1 | 1 | 1 | 3210 |
| [Gold Bringer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agold_bringer) | 0 | 3 | 12.5 | 3 | 3830 |
| [Gravity Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Agravity_blaster) | 4 | 1 | 120 | 1 | 600 |
| [Hell Horn](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahell_horn) | 12.5 | 8 | 11.5 | 8 | 3800 |
| [Illusion Revolver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aillusion_revolver) | 14 | 10 | 20 | 10 | 3200 |
| [Illusion Smg](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aillusion_smg) | 4 | 3 | 7 | 3 | 3240 |
| [Ion Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aion_blaster) | 13 | 11 | 28.5 | 11 | 2810 |
| [Iro Miner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Airo_miner) | 4 | 4 | 7 | 4 | 3060 |
| [Laser Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alaser_blaster) | 1.2 | 1 | 2.5 | 20 | 2840 |
| [Light Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alight_blaster) | 22.5 | 14 | 20.5 | 14 | 3810 |
| [Light Spark](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alight_spark) | 0 | 1 | 200 | 10 | 7 |
| [Luna Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aluna_blaster) | 3 | 2 | 4 | 2 | 3200 |
| [Mecha Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_blaster) | 36 | 30 | 80 | 30 | 2770 |
| [Mind Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amind_blaster) | 19.5 | 14 | 27.5 | 14 | 3180 |
| [Moon Destroyer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amoon_destroyer) | 0 | 100 | 60 | 100 | 3750 |
| [Moon Shiner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amoon_shiner) | 3.5 | 5 | 17.5 | 5 | 1810 |
| [Odious](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aodious) | 1 | 1 | 1.5 | 1 | 3190 |
| [Orb-O-Cron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aorbocron) | 18.5 | 13 | 26.5 | 13 | 3230 |
| [Paralyzer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aparalyzer) | 1.5 | 1 | 1.5 | 1 | 3900 |
| [Party Popper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aparty_popper) | 1.5 | 1 | 3 | 1 | 2810 |
| [Poison Plunger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apoison_plunger) | 0 | 20 | 50 | 20 | 2600 |
| [Power Ray](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apower_ray) | 12.5 | 12 | 38.5 | 12 | 2490 |
| [Proton](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aproton) | 2.5 | 2 | 4.5 | 2 | 3000 |
| [Reefer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Areefer) | 5 | 4 | 7 | 4 | 3600 |
| [Revolution](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arevolution) | 0 | 20 | 66 | 20 | 2800 |
| [Sea-O-Cron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aseaocron) | 20.5 | 13 | 18.5 | 13 | 3800 |
| [Skullo Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askullo_blaster) | 3.5 | 2 | 3 | 2 | 3780 |
| [Soul Drainer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asoul_drainer) | 0.2 | 1 | 2 | 1 | 3770 |
| [Soul Spark](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asoul_spark) | 0 | 1 | 0 | 20 | 5 |
| [Soul Storm](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asoul_storm) | 1.5 | 1 | 2 | 1 | 3190 |
| [Spirit Shower](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspirit_shower) | 0 | 10 | 100 | 10 | 2870 |
| [Swarm-O-Tron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aswarmotron) | 2 | 12 | 33 | 12 | 2400 |
| [Toxic Terrorizer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atoxic_terrorizer) | 0 | 7 | 22 | 7 | 2760 |
| [Vortex Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avortex_blaster) | 0 | 1 | 130 | 1 | 2870 |
| [Whimsy Winder](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awhimsy_winder) | 6 | 5 | 13 | 5 | 2830 |
| [Wither's Wrath](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awithers_wrath) | 7.5 | 7 | 21 | 7 | 800 |

## Explicit beam-distance overrides

Only these four registrations explicitly supplied a beam-distance input in the selected builder chains. No range is invented for the remaining weapons. Collision, subclass behavior and actual effective range still need matching-game checks.

- Blast Chiller: 30
- Laser Blaster: 40
- Light Spark: 3
- Soul Spark: 2

## Evidence and testing still needed

[Released registration, behavior-method and Spirit-resource evidence](https://herbertofury.github.io/Advent-of-Ascension/blaster-statistics-evidence-1.21.1.json) retains class/resource hashes, instruction bytes and the exact resource JSON. Archive: `AoA3-1.21.1-3.7.16.1.jar`.

Test insufficient Spirit, exhaustion during held use, recovery from eligible versus excluded damage, modified armour/enchantments, off-hand restrictions, durability breakage, special subclasses and client/server synchronization. Documentation arithmetic and source checks do not replace those game tests. AoA mechanics and assets are credited to Tslat and contributors.
