# Released projectile/firing declaration census

All 228 gun/shotgun/sniper/cannon/blaster registrations in AoA 3.7.1 for Minecraft 1.20.1 are indexed against the pinned release/class hashes. This is code-navigation evidence, not 228 completed upgrades.

134 weapon classes directly reference projectile classes; 94 require inherited or non-projectile-path review. The signature-aware index finds relevant firing/factory declarations for every row, preserving inherited overloads separately. A declaration's presence never proves that a particular call executes, or establishes projectile count, runtime damage, lifespan, chance branches or impact behavior.

## Important distinction

Soul Storm declares the three-argument fireBlaster method and inherits the four-argument method. Laser Blaster declares the four-argument method and inherits the three-argument method. Resolving solely by method name loses this distinction. The regression checks keep both signatures and identify their declaring classes.

Other concrete source checks: Apoco Assault Rifle allocates RedBulletEntity; Abominator inherits a LimoniteBulletEntity factory; Discharge Shotgun inherits a MetalSlugEntity factory. These checks do not determine every subsequent effect or behavior.

## Reproduce

Python 3 and an official JDK with javap are required. Obtain the pinned AoA release separately; no JAR or upstream bytecode is redistributed in this bundle.

1. Download conventional-weapon-baselines-1.20.1.json and blaster-baselines-1.20.1.json from this repository's docs folder.
2. Run build.py --jar /path/to/AoA3-1.20.1-3.7.1-all.jar --javap /path/to/jdk/bin/javap --baseline-dir /path/to/baselines.
3. Run resolve_factories.py with the same --jar and --javap paths.
4. Run test_census.py.

Class-hash-keyed local javap caches avoid repeating the disassembly on later runs. Both the registry baselines and exact artifact/class hashes are checked. The output records class hashes and inheritance paths for later human review. The cache is local research material and is not bundled.

Before making a feature claim, trace the actual dispatch and impact/resource logic and confirm it in the target game. Names such as RedBullet, ToxicBullet or Laser do not by themselves establish gameplay effects.
