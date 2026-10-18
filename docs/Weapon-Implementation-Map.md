# Behind the arsenal: released implementation map

[Open the searchable 228-weapon implementation explorer](https://herbertofury.github.io/Advent-of-Ascension/weapon-implementation-map.html).

**Minecraft 1.20.1 / AoA 3.7.1 · structural source evidence · no native-upgrade acceptance.**

The explorer connects each of the 228 first-target gun/shotgun/sniper/cannon/blaster IDs to its actual constructor class and in-package inheritance chain. It includes 227 unique weapon classes, their SHA-256 hashes, declared method signatures and directly constructed projectile classes. Detailed profiles link through where they already exist.

## How to use it

1. Search an item ID, class name or directly constructed projectile class.
2. Choose a family to narrow the list. The page shows 30 cards initially and expands on request.
3. Expand a card's class chain. It is populated once, on demand, instead of building every method list up front.
4. Look at the weapon's declared overrides and its ancestors before deciding what controls firing, recoil or impact behavior.
5. Open its full profile where available, then verify the exact method body and native behavior before implementing a conversion.

Literal registration constants are deliberately not automatically labeled as damage, degrees, radius or effective cooldown. The [profile standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard) explains why those interpretations require more evidence.

## What was checked

- The exact release archive SHA-512 and original registry class hash match the pinned input.
- All 228 selected IDs have one unambiguous constructor class; inheritance chains were inspected through their in-package parents.
- The map records 132 classes that directly construct projectile objects and 110 distinct projectile class names. This is not an exhaustive list of every runtime spawn path.
- Two full builds of the map produced byte-identical output.
- A simulated-DOM test passes pagination, exact profile links, lazy one-time class expansion, reset and family filtering. Data is inserted as text, not raw HTML.

The inherited `getRecoilModifier` declaration appears in BaseGun; `getRecoilForShot` declarations appear in BaseGun, Darkener, RockerRifle and Wrecker. That helps prioritize method-body review; declarations alone do not prove complete effective recoil behavior.

## Limits

A base class's projectile constructor does not prove every descendant uses that path. Method names do not establish effect semantics or call ordering. This structural inventory does not finish 228 profiles, models or runtime tests, and it covers neither all historical versions nor the additional weapon families. Fully accepted native upgraded weapons remain zero.

[Dataset](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/released-weapon-behavior-map-1.20.1.json) · [Original reproducible tool and test](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-behavior-map-tool-v2.zip) · [Verification receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-behavior-map-verification.json).

AoA source and identity: Tslat and contributors. No game JAR or decoded class files are bundled with the audit tool.


## Literal-decoding correction

The initial map copied only explicit constant fields from the earlier registry audit, which omitted implicit JVM float constants. The corrected decoder restores those values from their opcodes and includes instruction offsets. For example, Discharge Shotgun now shows `[0.0, 4, 160, 55, 0.0, 13.0]` and Hiver includes its final `1.0`. The class hashes and method maps were unaffected. Four decoder regression tests pass; the corrected 228-ID map has no unresolved literal offsets and reproduces byte-identically across two full builds.

These remain pushed literals in instruction order, not an evaluated argument stack or effective gameplay statistics. The decoder follows the [Java 17 JVM instruction specification](https://docs.oracle.com/javase/specs/jvms/se17/html/jvms-6.html).


## Typed stored baselines for all 228 first-target weapons

Each card now has a collapsed **Stored baseline values** section. The new 45 KB compact dataset combines 172 conventional weapons with 56 Spirit blasters. All selected constructor paths were inspected before naming the fields; the literal instruction list remains separately available for provenance.

- Conventional fields: base damage argument, durability, delay and recoil modifier; shotguns also expose pellet count and knockback factor.
- Blaster fields: base damage, durability, delay, charge and base Spirit. [Read the modifiers and exceptional impact costs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blaster-Spirit-Baselines-1.20.1).
- Lunar Assault Rifle's damage getter samples between 0.5x and 1.5x its constructor value. Darkener, RockerRifle and Wrecker have per-shot recoil overrides. The cards flag these boundaries.
- Zero base damage does not establish harmlessness, and no displayed combination is treated as proven DPS.

The extra dataset loads once per visit. A failure of this optional request leaves the structural map usable and shows a warning. Existing filtering, pagination and slow-load typed-search behavior remain checked. Simulated-DOM tests cover zero values, integer 120 formatting, the Spark exception and Lunar variation.

[Exact 172-weapon data](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/conventional-weapon-baselines-1.20.1.json) · [Pinned source-identity audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/conventional-baseline-audit-v1.zip). These data do not promote any weapon to native-upgrade acceptance.
