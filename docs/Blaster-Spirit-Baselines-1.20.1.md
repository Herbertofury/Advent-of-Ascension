# Spirit-powered blasters · stored baselines for all 56

**Minecraft 1.20.1 / AoA 3.7.1 · actual released constructors and class hashes · not effective combat stats.**

This fills the Spirit-weapon gap beside the [172 conventional-ammo weapons](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Ammunition-1.20.1). All 56 blaster constructors were inspected. Fifty forward the four normal arguments; six special constructors account for fixed/explicit charge times or EPIC item-property wrappers.

## Read these values correctly

- Base damage is a stored argument. Utility weapons, custom impacts, healing, repeated hits and effects can make actual behavior very different. No DPS ranking is inferred.
- Delay and charge are stored tick values, not a promise of effective input-to-shot latency or a proven firing frequency.
- Base Spirit is before the inherited modifier calculation and weapon-specific paths. This is not a universal cost-per-hit column.
- Names link to the item atlas. Full behavior and native acceptance remain per-weapon work.

### Critical exceptions: Light Spark and Soul Spark

Both store **zero base Spirit cost**, but that does **not** mean free use. Their display/start-use path returns/checks **200 Spirit**. Their entity-impact override also has a separate conditional `consumeResource(SPIRIT, 200, false)` call for a noncreative server player after the special-attack immunity gate. Preserve the distinction between stored baseline, start-use threshold and impact-time resource handling. Do not replace these with a generic zero-cost shot or an unconditional 200-cost-per-shot rule.

The static audit confirms those distinct calls; exact outcome/interruption behavior and multiplayer tests remain required.

### Inherited cost calculation in this release

For the ordinary player path, the released method calculates:

`(1 + 0.3 × Greed) × baseSpirit × max(0, 1 − 0.07 × Recharge)`

It then multiplies by **0.7** when wearing the full Ghoulish set. Non-player holders, and creative players when this is not a display calculation, take the method's zero-cost branch. The game uses float arithmetic. These method-level rules do not replace special impact paths above or establish all downstream resource behavior. The newer named-source comparison uses a Recharge helper; this page follows the pinned released method instead.

## Stored baseline table

| Weapon | Base damage | Durability | Delay ticks | Charge ticks | Base Spirit |
|---|---:|---:|---:|---:|---:|
| [Apoco Shower](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aapoco_shower) | 0 | 3760 | 10 | 10 | 80 |
| [Atomizer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aatomizer) | 11 | 3150 | 8 | 8 | 15 |
| [Beamer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Abeamer) | 1 | 3240 | 1 | 1 | 3 |
| [Blast Chiller](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Ablast_chiller) | 4 | 1750 | 6 | 20 | 20 |
| [Blood Drainer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Ablood_drainer) | 0.1 | 2750 | 1 | 1 | 2.5 |
| [Bone Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Abone_blaster) | 6 | 2430 | 6 | 6 | 20 |
| [Bubble Horn](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Abubble_horn) | 11 | 3200 | 8 | 8 | 15.5 |
| [Colour Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Acolour_cannon) | 45 | 1000 | 40 | 40 | 110 |
| [Confetti Cannon](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aconfetti_cannon) | 0 | 1000 | 10 | 10 | 0 |
| [Confetti Cluster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aconfetti_cluster) | 0 | 1500 | 5 | 5 | 0 |
| [Dark Destroyer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Adark_destroyer) | 0 | 3180 | 100 | 100 | 80 |
| [Darkly Guster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Adarkly_guster) | 8 | 3790 | 5 | 5 | 7 |
| [Death Ray](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Adeath_ray) | 19 | 3840 | 12 | 12 | 17 |
| [Doom Bringer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Adoom_bringer) | 0 | 2820 | 3 | 3 | 15.5 |
| [Eradicator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aeradicator) | 1 | 2790 | 1 | 1 | 2 |
| [Experiment W-801](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aexperiment_w_801) | 37 | 5000 | 50 | 50 | 90 |
| [Flowercorne](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aflowercorne) | 2.5 | 2910 | 4 | 4 | 20 |
| [Fragment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Afragment) | 3 | 3830 | 2 | 2 | 2.5 |
| [Froster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Afroster) | 3.5 | 2800 | 3 | 3 | 7.5 |
| [Gas Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Agas_blaster) | 0 | 2860 | 1 | 1 | 0.5 |
| [Ghoul Gasser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aghoul_gasser) | 0 | 3210 | 1 | 1 | 1 |
| [Gold Bringer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Agold_bringer) | 0 | 3830 | 3 | 3 | 12.5 |
| [Gravity Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Agravity_blaster) | 4 | 600 | 1 | 1 | 120 |
| [Hell Horn](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Ahell_horn) | 12.5 | 3800 | 8 | 8 | 11.5 |
| [Illusion Revolver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aillusion_revolver) | 14 | 3200 | 10 | 10 | 20 |
| [Illusion Smg](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aillusion_smg) | 4 | 3240 | 3 | 3 | 7 |
| [Ion Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aion_blaster) | 13 | 2810 | 11 | 11 | 28.5 |
| [Iro Miner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Airo_miner) | 4 | 3060 | 4 | 4 | 7 |
| [Laser Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Alaser_blaster) | 1.2 | 2840 | 1 | 20 | 2.5 |
| [Light Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Alight_blaster) | 22.5 | 3810 | 14 | 14 | 20.5 |
| [Light Spark ⚠](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Alight_spark) | 0 | 7 | 1 | 10 | 0 |
| [Luna Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aluna_blaster) | 3 | 3200 | 2 | 2 | 4 |
| [Mecha Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Amecha_blaster) | 36 | 2770 | 30 | 30 | 80 |
| [Mind Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Amind_blaster) | 19.5 | 3180 | 14 | 14 | 27.5 |
| [Moon Destroyer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Amoon_destroyer) | 0 | 3750 | 100 | 100 | 60 |
| [Moon Shiner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Amoon_shiner) | 3.5 | 1810 | 5 | 5 | 17.5 |
| [Odious](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aodious) | 1 | 3190 | 1 | 1 | 1.5 |
| [Orb-O-Cron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aorbocron) | 18.5 | 3230 | 13 | 13 | 26.5 |
| [Paralyzer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aparalyzer) | 1.5 | 3900 | 1 | 1 | 1.5 |
| [Party Popper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aparty_popper) | 1.5 | 2810 | 1 | 1 | 3 |
| [Poison Plunger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Apoison_plunger) | 0 | 2600 | 20 | 20 | 50 |
| [Power Ray](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Apower_ray) | 12.5 | 2490 | 12 | 12 | 38.5 |
| [Proton](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aproton) | 2.5 | 3000 | 2 | 2 | 4.5 |
| [Reefer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Areefer) | 5 | 3600 | 4 | 4 | 7 |
| [Revolution](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Arevolution) | 0 | 2800 | 20 | 20 | 66 |
| [Sea-O-Cron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aseaocron) | 20.5 | 3800 | 13 | 13 | 18.5 |
| [Skullo Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Askullo_blaster) | 3.5 | 3780 | 2 | 2 | 3 |
| [Soul Drainer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Asoul_drainer) | 0.2 | 3770 | 1 | 1 | 2 |
| [Soul Spark ⚠](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Asoul_spark) | 0 | 5 | 1 | 20 | 0 |
| [Soul Storm](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Asoul_storm) | 1.5 | 3190 | 1 | 1 | 2 |
| [Spirit Shower](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aspirit_shower) | 0 | 2870 | 10 | 10 | 100 |
| [Swarm-O-Tron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Aswarmotron) | 2 | 2400 | 12 | 12 | 33 |
| [Toxic Terrorizer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Atoxic_terrorizer) | 0 | 2760 | 7 | 7 | 22 |
| [Vortex Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Avortex_blaster) | 0 | 2870 | 1 | 1 | 130 |
| [Whimsy Winder](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Awhimsy_winder) | 6 | 2830 | 5 | 5 | 13 |
| [Wither's Wrath](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&q=aoa3%3Awithers_wrath) | 7.5 | 800 | 7 | 7 | 21 |

Rounded table labels preserve readable values; the [exact dataset](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/blaster-baselines-1.20.1.json) retains the extracted floating-point values and individual class hashes.

## Upgrade requirements

1. Preserve Spirit as a first-class resource. Cosmetic presentation must not secretly add ballistic ammo or mandatory magazine reloads.
2. Display stored, modified and special-condition costs distinctly when creating the upgrade UI.
3. Resolve charge, firing, accepted impact and resource commitment as separate events; no duplicate charge on cosmetic replay.
4. Recheck all special overrides before applying generic attachments, conversion parts or TaCZ turret behavior.
5. Keep 1.21.1 component-driven values in their own adapter; do not label this historical table as the latest game's stats.

[Reproducible pinned static audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/blaster-baseline-audit-v1.zip) · [Versioned adapters](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Versioned-Weapon-Adapters) · [Full weapon profile standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard)

Original AoA: Tslat and contributors. No game classes were executed by this static audit, and no native upgrade acceptance is implied.
