[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Shared firing and inventory warnings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2)

# Historical throwable weapons: payment, impacts and Runic Bombs

**Minecraft 1.12.2 / AoA 3.3.6.** Seven direct throwable registrations, their constructors, self-ammunition methods, 67 behavior-method records and two Grenade recipes are checked. These are static references, not measured damage, explosion radius or runtime certification.

![Four historical throwable source-model portraits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/thrown-inputs-and-effects-1.12.2.webp)

## Prepare and throw

- These items inherit the historical BaseGun use path. Read its hand, attack-strength and payment checks rather than treating a throw as a completely separate input system.
- Each selected item method asks the shared inventory helper for **1 + Greed level copies of itself**, then creates its projectile. Preserve the [split-stack accounting warning](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2).
- The base constructor sets max damage to **0** and stack size to **64**. The selected enchantability method returns false. Greed handling in code does not prove ordinary enchanting can put Greed on these items; modified stacks or other mods are separate cases.
- Do not assume a Chakram or Vulkram returns to inventory just because of its name. Stack consumption is checked; a returning-item mechanic is not established by this review.
- Grenade and Runic Bomb have zero ordinary damage inputs. Their explosion paths make “zero means harmless” an incorrect interpretation.

## Craft Grenades

Both released recipes are shapeless:

| Ingredients | Output | Illustrated recipe |
|---|---:|---|
| Gunpowder + Scrap Metal + Iron Ingot | 3 Grenades | [Ordinary recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fweapons%2Fmisc%2Fgrenade) |
| Unstable Gunpowder + Scrap Metal + Iron Ingot | 10 Grenades | [Unstable recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fweapons%2Fmisc%2Fgrenade_unstable) |

These are the two matching direct-output recipe definitions found in the checked archive for this seven-item set. Missing direct recipe matches for the other items do not establish that they are unobtainable; inspect their same-release drop and acquisition references.

## All seven entries

| Item and portrait | Ordinary damage input | Delay input · ticks | Selected effect or behavior |
|---|---:|---:|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-grenade.webp" alt="Grenade source-model portrait" width="72" height="72" loading="lazy"><br> [Grenade](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Grenade.name) | 0 | 10 | Explosion helper uses default strength field 1.5; gravity getter approximately 0.075. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-slice_star.webp" alt="Slice Star source-model portrait" width="72" height="72" loading="lazy"><br> [Slice Star](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SliceStar.name) | 4.5 | 7 | Ordinary ranged damage; projectile gravity getter approximately 0.05. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-chakram.webp" alt="Chakram source-model portrait" width="72" height="72" loading="lazy"><br> [Chakram](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Chakram.name) | 4 | 7 | Weapon-bound successful ranged-damage path requests Poison for 60 ticks, amplifier 1 (level II). |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-goo_ball.webp" alt="Goo Ball source-model portrait" width="72" height="72" loading="lazy"><br> [Goo Ball](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GooBall.name) | 3.5 | 7 | Weapon-bound successful ranged-damage path requests Slowness for 60 ticks, amplifier 1 (level II), and plays its impact sound. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-vulkram.webp" alt="Vulkram source-model portrait" width="72" height="72" loading="lazy"><br> [Vulkram](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Vulkram.name) | 3 | 7 | Weapon-bound successful ranged-damage path requests healing of 1 health point through the living/injured-recipient helper. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-hellfire.webp" alt="Hellfire source-model portrait" width="72" height="72" loading="lazy"><br> [Hellfire](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Hellfire.name) | 3.5 | 7 | Common impact effect searches nearby EntityMob targets, attempts secondary projectiles and requests 10 seconds of fire. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-runic_bomb.webp" alt="Runic Bomb source-model portrait" width="72" height="72" loading="lazy"><br> [Runic Bomb](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicBomb.name) | 0 | 10 | Explosion strength field 1.5; nearby hostile-mob slow request and Runic Golem shield handling described below. |

## Read the impact branch before combining effects

The selected BaseBullet collision handler runs on the server. For a new entity target, it chooses **one** of two damage routes:

1. If a weapon reference exists, call the weapon's `doImpactDamage`.
2. Otherwise, call the projectile's `doEntityImpact`.

It then calls the projectile's common `doImpactEffect`. These are not interchangeable methods. For example, the weapon-bound Vulkram item path requests healing, while its weaponless projectile method only makes a direct thrown-damage call. Do not promise the same extra effects under every projectile state.

For Grenade and Runic Bomb, both the weaponless entity-impact method and the common impact method contain an explosion-helper call. Consequently, the selected weaponless branch can reach two helper invocations. This is a branch-specific restoration test target, not a claim of double final damage in a running game. The ordinary weapon-bound path is different. How a projectile becomes weaponless, persistence, spawn cancellation and mod hooks need separate runtime checks.

## Runic Bomb: slow and shield handling

The common Runic Bomb impact method calls the explosion helper, then queries **EntityMob** instances in its bounding box expanded by **3**. It requests Slowness with **30 ticks and amplifier 100**, using ambient true and particles false. The unusually high amplifier is the released input; do not silently replace it with amplifier 1.

For each matching nearby **Runic Golem** whose shield flag is active, that common path calls `deactivateShield`. The weaponless entity-impact method has its own nearby slow loop and a direct-target Runic Golem shield check before the common handler follows. Preserve that distinction during restoration.

The expanded box is not a spherical radius, and the code request does not guarantee potion acceptance, successful explosion damage or compatibility with every protection mod.

## Hellfire: targets and the advancement hook

The common Hellfire impact method searches EntityMob targets in a box expanded by **7**, attempts one secondary Hellfire projectile for each, and calls fire with **10 seconds** on each target. It counts matching targets while doing this. With at least **20** counted targets and a server-player shooter, it calls the `overworld/heckfire` advancement helper for criterion `20_target_hellfire`.

This is a target-count condition, not proof of 20 kills, 20 successful projectile spawns or a fixed damage total. Treat the secondary projectile's eventual effects separately.

## Terrain and collision safety

The player-fired explosion helper consults **destructiveWeaponPhysics** before passing its destruction flag to the world explosion call; its fiery flag is false in this selected path. Other exploder/entity branches can use **doStrongerMobGriefing**. A strength field of 1.5 is not a promise of a 1.5-block radius or a universally harmless explosion.

BaseBullet's block-collision path can also destroy certain low-hardness blocks under destructiveWeaponPhysics before deciding whether to continue to the common impact method. Test away from valuable builds. A disabled terrain-destruction flag does not by itself mean entities cannot be hurt.

## Restoration checks

- Check exact self-item payment, empty/partial stacks and the shared inventory-helper edge cases.
- Keep weapon-bound, weaponless, block-impact and repeated-pierce paths separate in tests.
- Chakram and Goo Ball cast a successful ranged-damage target to EntityLivingBase in their item hooks. The shared helper has accepted nonliving/multipart routes, so validate the target type before the potion cast; do not call this an in-game crash reproduction.
- Test Runic Golem shields, the high-amplifier slow request, and both explosion branches.
- Test Hellfire's counted targets separately from successful spawns, fire acceptance and advancement completion.
- Preserve stack-based throwing in optional remodels rather than silently adding magazines or mandatory reloads.

[Exact released evidence and recipe definitions](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-thrown-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/thrown-art-evidence-1.12.2.json).
