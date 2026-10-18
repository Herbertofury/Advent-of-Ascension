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

[Dataset](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/released-weapon-behavior-map-1.20.1.json) · [Original reproducible tool and test](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-behavior-map-tool-v1.zip) · [Verification receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-behavior-map-verification.json).

AoA source and identity: Tslat and contributors. No game JAR or decoded class files are bundled with the audit tool.
