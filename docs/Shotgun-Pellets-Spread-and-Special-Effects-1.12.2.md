[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Gun inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2) · [Ammunition pitfalls](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2)

# Historical shotguns: pellets, spread and special effects

**Minecraft 1.12.2 / AoA 3.3.6.** Seventeen direct shotgun registrations are checked against their released constructors. The base behavior and eight selected subclass methods are inspected separately. These are not measured DPS, hit-rate or runtime compatibility results.

![Four historical shotgun previews with exact pellet, timing and recoil inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/shotgun-inputs-1.12.2.webp)

## Choose by behavior, not a single damage number

Open a gun below and expand **1.12.2 shotgun inputs · pellets and spread**. The item browser also offers a **Historical shotgun inputs** family filter for this release. All 17 panels are lazy and reuse the existing release data.

Damage and pellet count are separate constructor inputs. Multiplying them does not establish how much health one trigger pull removes: pellets may miss, collide or follow special impact logic, and target immunity/defenses and other modifiers still matter. **Discharge Shotgun has a zero damage input but a separate explosion path**, so a zero-input ranking would misrepresent it.

| Shotgun and portrait | Damage input | Pellets | Delay · ticks | Durability | Knockback factor | Recoil input |
|---|---:|---:|---:|---:|---:|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-abyssro.webp" alt="Abyssro source-model portrait" width="72" height="72" loading="lazy"><br> [Abyssro](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Abyssro.name) | 18.5 | 2 | 46 | 1100 | 0.3 | 18 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-amplifier.webp" alt="Amplifier source-model portrait" width="72" height="72" loading="lazy"><br> [Amplifier](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Amplifier.name) | 9 | 5 | 56 | 1100 | 0.2 | 25 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-blast_barrel.webp" alt="Blast Barrel source-model portrait" width="72" height="72" loading="lazy"><br> [Blast Barrel](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BlastBarrel.name) | 13 | 3 | 62 | 740 | 0.4 | 23 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-blue_barrel.webp" alt="Blue Barrel source-model portrait" width="72" height="72" loading="lazy"><br> [Blue Barrel](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BlueBarrel.name) | 14.5 | 3 | 54 | 1120 | 0.4 | 16 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-boulder.webp" alt="Boulder source-model portrait" width="72" height="72" loading="lazy"><br> [Boulder](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Boulder.name) | 11.5 | 4 | 58 | 1080 | 0.4 | 30 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-brown_blaster.webp" alt="Brown Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Brown Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BrownBlaster.name) | 6 | 3 | 54 | 300 | 0.4 | 16 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-demolisher.webp" alt="Demolisher source-model portrait" width="72" height="72" loading="lazy"><br> [Demolisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Demolisher.name) | 8.5 | 4 | 58 | 730 | 0.4 | 30 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-destruction_shotgun.webp" alt="Destruction Shotgun source-model portrait" width="72" height="72" loading="lazy"><br> [Destruction Shotgun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DestructionShotgun.name) | 10.5 | 3 | 56 | 690 | 0.4 | 14 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-discharge_shotgun.webp" alt="Discharge Shotgun source-model portrait" width="72" height="72" loading="lazy"><br> [Discharge Shotgun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DischargeShotgun.name) | 0 | 4 | 55 | 160 | 0 | 15 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-gimmick.webp" alt="Gimmick source-model portrait" width="72" height="72" loading="lazy"><br> [Gimmick](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Gimmick.name) | 4.5 | 10 | 68 | 800 | 0.2 | 28 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-ginger_blaster.webp" alt="Ginger Blaster source-model portrait" width="72" height="72" loading="lazy"><br> [Ginger Blaster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GingerBlaster.name) | 7 | 5 | 60 | 720 | 0.4 | 19 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-long_shot.webp" alt="Long Shot source-model portrait" width="72" height="72" loading="lazy"><br> [Long Shot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LongShot.name) | 15.5 | 2 | 54 | 730 | 0.2 | 12 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-mechyro.webp" alt="Mechyro source-model portrait" width="72" height="72" loading="lazy"><br> [Mechyro](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Mechyro.name) | 13 | 2 | 46 | 720 | 0.3 | 18 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-purity_shotgun.webp" alt="Purity Shotgun source-model portrait" width="72" height="72" loading="lazy"><br> [Purity Shotgun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityShotgun.name) | 15 | 3 | 56 | 1090 | 0.4 | 14 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-purple_punisher.webp" alt="Purple Punisher source-model portrait" width="72" height="72" loading="lazy"><br> [Purple Punisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurplePunisher.name) | 20.5 | 2 | 52 | 1120 | 0.785 | 23 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-red_rocket.webp" alt="Red Rocket source-model portrait" width="72" height="72" loading="lazy"><br> [Red Rocket](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RedRocket.name) | 11.5 | 2 | 52 | 500 | 0.785 | 23 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-vivo.webp" alt="Vivo source-model portrait" width="72" height="72" loading="lazy"><br> [Vivo](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Vivo.name) | 7 | 3 | 36 | 710 | 0.3 | 8 |

## Make Spreadshot

The released shaped recipe produces **5 Spreadshot**:

| Empty | Limonite Bullet | Empty |
|---|---|---|
| Limonite Bullet | Gunpowder | Limonite Bullet |
| Empty | Limonite Ingot | Empty |

[Open the illustrated exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fammo%2Fspreadshot).

Sixteen of these seventeen classes inherit the base shotgun ammunition method: it requests **1 + Greed level Spreadshot** through the shared inventory helper. Discharge Shotgun overrides this with **Discharge Capsules**. The projectile object returned by the ammo method is used as a non-null success check; the actual pellet loop constructs its own projectiles. Do not infer that the returned Metal Slug is the pellet spawned by every base shotgun.

The [historical inventory-consumption warning](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2) also matters for these helper calls. Test exact payment across split stacks before trusting a multi-item cost in a target build.

## Firing and spread

The selected BaseShotgun right-click method requires the hand selected by getGunHand and a fully cooled attack strength. Unlike the inspected BaseGun implementation, it calls its ammunition method **before its world.isRemote check**; only the fireShotgun call is inside that explicit server-side branch.

This is a client/server inventory synchronization test target. It does not prove that the authoritative inventory is charged twice, nor that client prediction necessarily produces a persistent loss.

For the base server firing call:

- Form contribution is **0.15 × Form enchantment level**.
- The supplied spread factor is **0.1 × pelletCount × (1 − Form contribution)**.
- Each pellet receives separate `(randomFloat − 0.5) × spreadFactor` offsets for x, y and z.
- The loop attempts the declared number of pellets. A spawn attempt is not a guarantee that every projectile is accepted.

These offsets are constructor inputs, not a measured angle in degrees or an exact range in blocks. Do not clamp or reinterpret them while claiming unchanged behavior without target-build testing.

The successful-ammo branch handles sound, durability, cooldown and recoil, then returns **PASS**; missing ammo returns **FAIL** in this method. A PASS result is therefore not itself evidence that the shotgun failed to shoot.

## Special cases worth knowing

| Weapon | Checked subclass behavior | What not to assume |
|---|---|---|
| Amplifier | Its impact-effect hook calls the explosion helper with strength argument 1.0 after the base successful-damage gate. | This is not a guaranteed blast radius, terrain destruction rule or total damage value. |
| Blast Barrel | Same selected hook pattern, with strength argument 2.0. | Compare actual helper settings and target behavior before treating it as a simple damage multiplier. |
| Destruction Shotgun | One `nextInt(5) == 0` draw occurs before its pellet loop; that volley uses multiplier 1.5 when charged, otherwise 1.0. | This is one 1-in-5 draw for the volley, not an independent draw for every pellet or a guaranteed every-fifth-shot cycle. |
| Purity Shotgun | The same selected charged-volley branch as Destruction. | The shared branch does not establish identical overall item balance, acquisition or all effects. |
| Long Shot | Its selected Limonite Bullet constructor call passes 6 in the argument position where the base loop passes 4. | No exact distance or lifetime guarantee is derived from that difference alone here. |
| Discharge Shotgun | Builds Discharge Shot projectiles, consumes Discharge Capsules, and its impact method calls the explosion helper with 2.5. | The zero ordinary damage input does not make the explosion harmless; acquisition remains a separate question. |

The base impact method applies its knockback helper only when damage succeeds, the factor is positive and the target is living, then calls the effect hook. It does not apply a universal unconditional knockback distance to every pellet or target.

## Small-test checklist

1. Select the exact release and item; inspect its ammunition and special-case row.
2. Bring a small known supply and test in a safe open area away from valuable builds.
3. Compare physical ammo counts and durability, especially with Greed or split stacks.
4. Check the correct hand, attack-strength readiness and cooldown before assuming missing ammo.
5. Test Form, Control and Brace separately, then together; preserve their actual arithmetic when porting.
6. For an overhaul, test client prediction, server acceptance, rejected pellet spawns, projectile collision, impact effects and resource payment. Static references do not certify those systems.

[Released registration windows, base methods, eight subclass methods and Spreadshot recipe](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-shotgun-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/shotgun-art-evidence-1.12.2.json).
