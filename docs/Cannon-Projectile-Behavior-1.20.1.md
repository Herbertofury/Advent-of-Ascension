# Cannon Projectile Behavior · 1.20.1

[Cannon crafting guide](Cannon-Progression-and-Recipes-1.20.1) · [Weapon overhaul](Weapon-Overhaul)

**AoA 3.7.1 / Minecraft 1.20.1: all 50 registered cannons, 41 referenced projectile classes.** This is a released-class census, not captured native flight. It exists to prevent an upgrade from accidentally flattening different weapons into one generic cannon behavior.

## Important differences to preserve

The projectile gravity method is not uniformly 0.1. Ghoul Cannon uses 0.05; several specialist projectiles use 0.015, 0.06 or 0.075. Fifteen projectile classes inherit BaseBullet’s zero-return method. A zero gravity return does not prove a motionless projectile, a hitscan attack or absence of other movement logic. Constructor velocity, drag, update methods, collision and server behavior still require separate inspection.

Five cannon weapon classes inherit their projectile factory directly from BaseCannon. The other 45 declare a factory. This census verifies those direct superclass relationships rather than assuming all missing methods resolve to the same class.

### Projectile-class distribution

Counts below count unique projectile classes, not weapons; several weapons can share a projectile.

| Resolved gravity-method return | Unique projectile classes |
|---|---:|
| 0 | 15 |
| 0.015 | 4 |
| 0.05 | 3 |
| 0.06 | 2 |
| 0.075 | 2 |
| 0.1 | 15 |

These values are game-code parameters, not metres per second squared or a measured travel arc.

## Every cannon and its projectile

Sprites are the actual released item images. Profile links lead to weapon-specific research where available. “BaseBullet inherited” means the direct projectile superclass supplies the zero-return method; it does not mean the entire projectile behavior is identical.

| Cannon | Projectile class | Gravity return | Gravity implementation |
|---|---|---:|---|
| ![Ancient Bomber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-ancient_bomber.png) Ancient Bomber | `GrenadeEntity` | 0.075 | Direct override |
| ![Ancient Discharger](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-ancient_discharger.png) Ancient Discharger | `TriDischargeShotEntity` | 0 | BaseBullet inherited |
| ![Aqua Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/aqua-cannon-original.png) [Aqua Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Aqua-Cannon-Weapon-Profile) | `HeavyBlueCannonballEntity` | 0.1 | Direct override |
| ![Balloon Bomber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/balloon-bomber-original.png) [Balloon Bomber](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Balloon-Bomber-Weapon-Profile) | `BalloonBombEntity` | 0.1 | Direct override |
| ![Big Blast](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-big_blast.png) Big Blast | `CannonballEntity` | 0 | BaseBullet inherited |
| ![Blast Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-blast_cannon.png) Blast Cannon | `StickyCoolBombEntity` | 0 | BaseBullet inherited |
| ![Blissful Blast](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-blissful_blast.png) Blissful Blast | `SmileyCannonballEntity` | 0 | BaseBullet inherited |
| ![Bomb Launcher](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-bomb_launcher.png) Bomb Launcher | `StickyRedBombEntity` | 0 | BaseBullet inherited |
| ![Boom Boom](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-boom_boom.png) Boom Boom | `VolatileCannonballEntity` | 0.05 | Direct override |
| ![Boom Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-boom_cannon.png) Boom Cannon | `GrenadeEntity` | 0.075 | Direct override |
| ![Boulder Bomber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-boulder_bomber.png) Boulder Bomber | `CannonballEntity` | 0 | BaseBullet inherited |
| ![Bozo Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-bozo_blaster.png) Bozo Blaster | `BozoBallEntity` | 0.1 | Direct override |
| ![Bulb Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/bulb-cannon-original.png) [Bulb Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bulb-Cannon-Weapon-Profile) | `HeavyWitherBallEntity` | 0.1 | Direct override |
| ![Carrot Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/carrot-cannon-original-sprite.png) [Carrot Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Carrot-Cannon-Weapon-Profile) | `CarrotBallEntity` | 0.1 | Direct override |
| ![Clown Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-clown_cannon.png) [Clown Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Clown-Cannon-Weapon-Profile) | `ClownBallEntity` | 0.1 | Direct override |
| ![Clowno-Pulse](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/clowno-pulse-original.png) [Clowno-Pulse](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Clowno-Pulse-Weapon-Profile) | `CannonballEntity` | 0 | BaseBullet inherited |
| ![Coral Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/coral-cannon-original.png) [Coral Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Coral-Cannon-Weapon-Profile) | `HeavyBlueCannonballEntity` | 0.1 | Direct override |
| ![Discharge Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-discharge_cannon.png) Discharge Cannon | `DischargeShotEntity` | 0 | BaseBullet inherited |
| ![Energy Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/energy-cannon-original.png) [Energy Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Energy-Cannon-Weapon-Profile) | `EnergyShotEntity` | 0 | BaseBullet inherited |
| ![Erebon Stickler](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-erebon_stickler.png) Erebon Stickler | `ErebonSticklerShotEntity` | 0.015 | Direct override |
| ![Floro RPG](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-floro_rpg.png) Floro RPG | `FloroRPGEntity` | 0 | BaseBullet inherited |
| ![Flower Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-flower_cannon.png) [Flower Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Flower-Cannon-Weapon-Profile) | `FlowerBallEntity` | 0.1 | Direct override |
| ![Fungal Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/fungal-cannon-original-sprite.png) [Fungal Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fungal-Cannon-Weapon-Profile) | `FungalBallEntity` | 0.1 | Direct override |
| ![Ghast Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ghast-blaster-original.png) [Ghast Blaster](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ghast-Blaster-Weapon-Profile) | `HeavyShadowballEntity` | 0.1 | Direct override |
| ![Ghoul Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-ghoul_cannon.png) [Ghoul Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ghoul-Cannon-Weapon-Profile) | `GhoulBallEntity` | 0.05 | Direct override |
| ![Giga Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-giga_cannon.png) Giga Cannon | `GigaGreenBallEntity` | 0 | BaseBullet inherited |
| ![Golder Bomber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-golder_bomber.png) Golder Bomber | `GoldenCannonballEntity` | 0.05 | Direct override |
| ![Hive Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-blaster-original-sprite.png) [Hive Blaster](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hive-Blaster-Weapon-Profile) | `HiveBallEntity` | 0.1 | Direct override |
| ![Hive Howitzer](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-hive_howitzer.png) Hive Howitzer | `HeavyRedCannonballEntity` | 0.1 | Direct override |
| ![Iro Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-iro_cannon.png) Iro Cannon | `OrangeCannonballEntity` | 0.1 | Direct override |
| ![Jack Funger](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-jack_funger.png) Jack Funger | `FungalRockFragmentEntity` | 0.06 | Direct override |
| ![Jack Rocker](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-jack_rocker.png) Jack Rocker | `RockFragmentEntity` | 0.06 | Direct override |
| ![Luxon Stickler](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-luxon_stickler.png) Luxon Stickler | `LuxonSticklerShotEntity` | 0.015 | Direct override |
| ![Mecha Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/mecha-cannon-original.png) [Mecha Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mecha-Cannon-Weapon-Profile) | `OrangeCannonballEntity` | 0.1 | Direct override |
| ![Mini Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-mini_cannon.png) Mini Cannon | `MiniGreenBallEntity` | 0 | BaseBullet inherited |
| ![Missile Maker](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-missile_maker.png) Missile Maker | `MultiplyingGrenadeEntity` | 0.075 | Direct override |
| ![Moon Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moon-cannon-original.png) [Moon Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Moon-Cannon-Weapon-Profile) | `MoonShotEntity` | 0 | BaseBullet inherited |
| ![Pluton Stickler](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-pluton_stickler.png) Pluton Stickler | `PlutonSticklerShotEntity` | 0.015 | Direct override |
| ![Predatorian Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/predatorian-blaster-original.png) [Predatorian Blaster](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Predatorian-Blaster-Weapon-Profile) | `HeavyBoneCannonballEntity` | 0.1 | Direct override |
| ![Pulse Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pulse-cannon-original.png) [Pulse Cannon](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Pulse-Cannon-Weapon-Profile) | `CannonballEntity` | 0 | BaseBullet inherited |
| ![RPG](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-rpg.png) RPG | `RPGEntity` | 0 | BaseBullet inherited |
| ![Selyan Stickler](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-selyan_stickler.png) Selyan Stickler | `SelyanSticklerShotEntity` | 0.015 | Direct override |
| ![Shadow Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-shadow_blaster.png) Shadow Blaster | `HeavyShadowballEntity` | 0.1 | Direct override |
| ![Shyre Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-shyre_blaster.png) Shyre Blaster | `CannonballEntity` | 0 | BaseBullet inherited |
| ![Smile Blaster](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-smile_blaster.png) Smile Blaster | `SmileBlasterEntity` | 0.1 | Direct override |
| ![Super Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-super_cannon.png) Super Cannon | `SuperGreenBallEntity` | 0 | BaseBullet inherited |
| ![Ultra Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-ultra_cannon.png) Ultra Cannon | `UltraGreenBallEntity` | 0 | BaseBullet inherited |
| ![Vox Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-vox_cannon.png) Vox Cannon | `VoxCannonEntity` | 0 | BaseBullet inherited |
| ![Water-Balloon Bomber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-water_balloon_bomber.png) Water-Balloon Bomber | `WaterBalloonBombEntity` | 0.1 | Direct override |
| ![Wither Cannon](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-guide-wither_cannon.png) Wither Cannon | `HeavyWitherBallEntity` | 0.1 | Direct override |

## Upgrade regression requirements

- [ ] Match each original projectile class and inherited method before choosing an upgraded visual.
- [ ] Capture original travel, fall, impacts and lifetime in the target release; separate native footage from concept art.
- [ ] Preserve collision/hitbox and damage semantics unless a gameplay-bearing attachment explicitly changes them.
- [ ] Check velocity, drag, per-tick custom movement, lifetime, piercing, split/spawn behavior and server ownership; this gravity table alone is insufficient.
- [ ] Use time-based visual particle budgets while retaining original effect identity, rather than coupling emissions to render frequency.
- [ ] Test multiplayer, low/high frame rates, slow server ticks, unloaded chunks and relevant compatibility targets.

## Evidence and limits

[Released class census and hashes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-projectile-census-1.20.1.json) records every factory method, weapon-class hash, projectile-class hash and resolved gravity owner. [Reproducible extraction and tests](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-projectile-census-tools.zip) requires the separately obtained official AoA JAR and a Java development kit. It does not bundle the mod.

The extractor only accepts simple two-instruction float-return overrides for this summary. More complex methods must be inspected instead of taking the first constant as a result. The baseline is one pinned release; newer versions remain separate work. Native testing is not inferred.
