[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Historical gun inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2) · [Ammunition checks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2)

# Historical snipers: stance, scopes and exact inputs

**Minecraft 1.12.2 / AoA 3.3.6.** This reference covers 27 direct sniper registrations, their exact scope getters, selected base firing methods and client scope hooks. It is static documentation, not a measured accuracy, damage or compatibility test.

![Thirteen original sniper scope textures over a documentation checkerboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/sniper-scope-atlas-1.12.2.webp)

The atlas preserves the original 385×257 source pixels for each overlay. The checkerboard replaces the transparent background only for inspection. It does not depict an actual world, live HUD scaling or a rendered sniper weapon.

## Use the intended stance

1. Hold the sniper in the **main hand**. The inspected base right-click path explicitly rejects offhand use rather than calling the ordinary gun's Brace hand selector.
2. Wait for fully cooled attack strength.
3. **Sneak while on the ground** to use the base steady-firing branch and the selected client scope flag.
4. Check the proper ammunition and its physical count before a small test shot.
5. Read your weapon's subclass and scope row below; a shared scope image does not mean identical behavior.

The base use method obtains its ammunition result before its explicit world.isRemote check. Only fireSniper is called inside that server-side branch. As with shotguns, this is an inventory-prediction/synchronization test target, not proof that the server consumes twice.

## Steady and unsteady firing are different branches

When the shooter is both sneaking and grounded, the selected base fireSniper path uses getRecoilForShot with the Control multiplier **1 − 0.15 × Control level** for the server player's recoil packet.

Otherwise it calls bullet.shoot with **20.0** and **50.0** in the velocity and inaccuracy argument positions, and sends **getRecoil() × 2** for the server-player recoil packet. That second packet calculation does not apply the same Control expression in this method.

Do not reinterpret those inputs as exact meters, degrees, hit percentages or a guaranteed recoil curve. The method then attempts to spawn the projectile; acceptance and client presentation remain separate runtime checks.

## The early-impact penalty is based on age

BaseSniper.doImpactDamage forwards to the base gun damage path with **half the supplied projectile multiplier when bullet.getAge() ≤ 1**, otherwise with the unchanged multiplier. This is an age predicate, not a fixed distance measurement or a claim that all subclasses preserve the same outcome.

The constructor damage below is still not final health removed. AoA configuration, projectile multipliers, target defenses, enchantments and subclass impact logic can change it.

## Prepare ammunition

The released Metal Slug recipe is a vertical column:

1. Iron Ingot at the top
2. Limonite Ingot in the middle
3. Gunpowder at the bottom

It produces **8 Metal Slugs**. [Open the illustrated exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fammo%2Fmetal_slug).

- **25 inspected snipers inherit the base ammo method:** Metal Slugs, amount 1 + Greed level.
- **Moon Maker:** its override still checks Metal Slugs at that amount, but constructs an EntityMoonMaker projectile.
- **Discharge Sniper:** its override checks Discharge Capsules and constructs an EntityDischargeSlug.

The shared [multi-stack accounting and spawn-acceptance warnings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2) remain relevant. Registration and an ammunition reference do not establish every weapon's Survival acquisition route.

## Compare the 27 exact-release references

Each weapon name opens its own source-model portrait and lazy **1.12.2 sniper inputs · scope and stance** panel. Use the historical sniper family filter to browse them together.

| Sniper and portrait | Damage input | Delay · ticks | Durability | Recoil input | Scope symbol |
|---|---:|---:|---:|---:|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-baron_ssr.webp" alt="Baron SSR source-model portrait" width="72" height="72" loading="lazy"><br> [Baron SSR](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronSSR.name) | 35 | 88 | 240 | 20 | REDLIGHT |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-bayonette_sr.webp" alt="Bayonette SR source-model portrait" width="72" height="72" loading="lazy"><br> [Bayonette SR](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BayonetteSR.name) | 33 | 86 | 300 | 18 | BASIC |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-bolt_rifle.webp" alt="Bolt Rifle source-model portrait" width="72" height="72" loading="lazy"><br> [Bolt Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoltRifle.name) | 30 | 100 | 100 | 26 | BASIC |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-camo_rifle.webp" alt="Camo Rifle source-model portrait" width="72" height="72" loading="lazy"><br> [Camo Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CamoRifle.name) | 31.5 | 84 | 150 | 19 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-clown_cracker.webp" alt="Clown Cracker source-model portrait" width="72" height="72" loading="lazy"><br> [Clown Cracker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ClownCracker.name) | 33.5 | 84 | 305 | 17 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-clownimator.webp" alt="Clownimator source-model portrait" width="72" height="72" loading="lazy"><br> [Clownimator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Clownimator.name) | 49.5 | 95 | 545 | 18 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-crystaneer.webp" alt="Crystaneer source-model portrait" width="72" height="72" loading="lazy"><br> [Crystaneer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Crystaneer.name) | 37.5 | 88 | 345 | 21 | CRYSTAL |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-dark_beast.webp" alt="Dark Beast source-model portrait" width="72" height="72" loading="lazy"><br> [Dark Beast](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DarkBeast.name) | 50.5 | 96 | 560 | 25 | MONSTER |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-deadlock.webp" alt="Deadlock source-model portrait" width="72" height="72" loading="lazy"><br> [Deadlock](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Deadlock.name) | 25.5 | 90 | 120 | 25 | DIAMOND |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-decimator.webp" alt="Decimator source-model portrait" width="72" height="72" loading="lazy"><br> [Decimator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Decimator.name) | 33 | 95 | 180 | 18 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-discharge_sniper.webp" alt="Discharge Sniper source-model portrait" width="72" height="72" loading="lazy"><br> [Discharge Sniper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DischargeSniper.name) | 10 | 24 | 540 | 11 | DISCHARGE |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-dual_sight.webp" alt="Dual Sight source-model portrait" width="72" height="72" loading="lazy"><br> [Dual Sight](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DualSight.name) | 38.5 | 91 | 350 | 30 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-duster.webp" alt="Duster source-model portrait" width="72" height="72" loading="lazy"><br> [Duster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Duster.name) | 21 | 60 | 170 | 18 | BASIC |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-floro500.webp" alt="Floro500 source-model portrait" width="72" height="72" loading="lazy"><br> [Floro500](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Floro500.name) | 37 | 70 | 550 | 13 | FLORO |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-head_hunter.webp" alt="Head Hunter source-model portrait" width="72" height="72" loading="lazy"><br> [Head Hunter](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HeadHunter.name) | 41.5 | 92 | 380 | 23 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-hive_cracker.webp" alt="Hive Cracker source-model portrait" width="72" height="72" loading="lazy"><br> [Hive Cracker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HiveCracker.name) | 44 | 84 | 555 | 17 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-ka500.webp" alt="Ka500 source-model portrait" width="72" height="72" loading="lazy"><br> [Ka500](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Ka500.name) | 30 | 70 | 360 | 13 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-mark_maker.webp" alt="Mark Maker source-model portrait" width="72" height="72" loading="lazy"><br> [Mark Maker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MarkMaker.name) | 36.5 | 70 | 530 | 13 | MARKER |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-mineral.webp" alt="Mineral source-model portrait" width="72" height="72" loading="lazy"><br> [Mineral](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Mineral.name) | 58.5 | 112 | 560 | 22 | BOULDER |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-monster.webp" alt="Monster source-model portrait" width="72" height="72" loading="lazy"><br> [Monster](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Monster.name) | 38 | 96 | 250 | 25 | MONSTER |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-moon_maker.webp" alt="Moon Maker source-model portrait" width="72" height="72" loading="lazy"><br> [Moon Maker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MoonMaker.name) | 38.5 | 70 | 570 | 13 | MOON |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-rosid_rifle.webp" alt="Rosid Rifle source-model portrait" width="72" height="72" loading="lazy"><br> [Rosid Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidRifle.name) | 45.5 | 102 | 405 | 19 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-sabbath.webp" alt="Sabbath source-model portrait" width="72" height="72" loading="lazy"><br> [Sabbath](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Sabbath.name) | 44 | 97 | 450 | 22 | SCRATCHES |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-sludge_sniper.webp" alt="Sludge Sniper source-model portrait" width="72" height="72" loading="lazy"><br> [Sludge Sniper](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SludgeSniper.name) | 37 | 87 | 350 | 18 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-sweet_tooth.webp" alt="Sweet Tooth source-model portrait" width="72" height="72" loading="lazy"><br> [Sweet Tooth](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SweetTooth.name) | 32.5 | 77 | 460 | 17 | CANDY |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-terminator.webp" alt="Terminator source-model portrait" width="72" height="72" loading="lazy"><br> [Terminator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Terminator.name) | 53 | 112 | 470 | 22 | DOTTED |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-viper1.webp" alt="Viper-1 source-model portrait" width="72" height="72" loading="lazy"><br> [Viper-1](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Viper1.name) | 30 | 89 | 185 | 17 | SCRATCHES |

## Scope activation and presentation

The inspected END-phase client tick handler sets isSniping when the player is sneaking, grounded and holding a BaseSniper in the main hand. It selects that weapon's getScreen result. Each of the 27 resolved getters returns one of the 13 scope symbols shown above.

The selected FOV hook sets the event's new-FOV value to **0.2** while isSniping is true. This is the event value, not a standalone camera angle in degrees or a measured zoom ratio. The scope overlay and crosshair-cancellation hooks separately require first-person view; do not assume that the FOV method contains that same first-person guard.

The overlay renderer uses a post-HELMET event, rejects canceled events, and chooses one of the matching released scope textures. Resource packs, other HUD/FOV mods and actual aspect ratios can affect the final presentation. The source atlas is not a compatibility certificate.

## Target-build checks

- Main hand versus offhand, grounded crouch versus airborne crouch, and leaving the crouched state.
- First-person versus third-person FOV and crosshair behavior, including other FOV/HUD mods.
- The early age boundary at 0, 1 and 2 without substituting a guessed distance.
- Metal Slugs versus Discharge Capsules, Creative mode, Greed and split-stack payment.
- Stable and unstable recoil with Control, preserving the actual branch distinction.
- Missing or rejected projectile spawns, client inventory correction and subclass impact effects.

[Released constructor windows, six base methods, 32 scope/ammo/client method records and 13 texture hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-sniper-inputs-1.12.2.json) · [Scope-atlas provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sniper-scope-art-evidence-1.12.2.json).
