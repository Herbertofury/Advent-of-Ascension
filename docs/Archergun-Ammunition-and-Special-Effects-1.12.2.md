[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Historical gun firing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2) · [Historical bows](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bow-Draw-Timing-and-Ammunition-1.12.2)

# Historical archerguns: arrows, trajectories and special effects

**Minecraft 1.12.2 / AoA 3.3.6.** All nine direct archergun registrations are matched to released constructors and exact item identities. The selected base, subclass and projectile methods are also recorded. These are static release references, not final damage, measured DPS or a running-game certification.

![Four historical archergun source-model portraits and their constructor inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/archergun-inputs-and-ammo-1.12.2.webp)

## First use: prepare arrows, not a draw animation

1. Select the **1.12.2 release** in the inventory and recipe explorers. Later crossbows are a separate release family; similarly named weapons are not a reason to substitute their behavior.
2. Craft Holly Arrows: place **Iron Nugget, Stick, Holly Top Petals vertically, in that order**, for **four Holly Arrows**. [Open the illustrated exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fammo%2Fholly_arrow).
3. Eight of the nine entries request **1 + Greed level** Holly Arrows through the shared inventory helper. This is an exact item-stack matching route, not the bow's wider HollyArrow-class search. Do not assume Pop Shots or tipped variants are accepted.
4. **Spectral Archergun** creates its projectile without an inventory-item payment call in its override. That does not remove the inherited firing gates, cooldown or durability handling.
5. Follow the [gun firing requirements and split-stack warning](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Firing-Ammunition-and-Inventory-Pitfalls-1.12.2). These weapons inherit BaseGun's firing path; the 1.12.2 bow charge/release formula does not apply to them.

## All nine entries

Open a weapon name to see its source-model portrait, exact recipe/drop searches and lazy **1.12.2 archergun inputs · arrows and special effects** panel.

| Weapon and portrait | Damage input | Delay · ticks | Durability | Recoil input | Selected ammo method |
|---|---:|---:|---:|---:|---|
| [Coral Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralArchergun.name) | 13 | 12 | 600 | 3 | Holly Arrow |
| [Lunar Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarArchergun.name) | 10.5 | 12 | 1530 | 3 | Holly Arrow |
| [Mecha Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechaArchergun.name) | 11.5 | 16 | 1300 | 3 | Holly Arrow |
| [Pyro Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PyroArchergun.name) | 7.5 | 12 | 950 | 3 | Holly Arrow |
| [Rosidian Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianArchergun.name) | 9 | 12 | 1280 | 3 | Holly Arrow |
| [Skeletal Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalArchergun.name) | 8.5 | 12 | 1100 | 3 | Holly Arrow |
| [Spectral Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpectralArchergun.name) | 6.5 | 8 | 1600 | 3 | No item consumed by selected method |
| [Trolls Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TrollsArchergun.name) | 9.5 | 16 | 800 | 3 | Holly Arrow |
| [Viral Archergun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ViralArchergun.name) | 9 | 12 | 1250 | 3 | Holly Arrow |

## Trajectory: Lunar is a real exception

- The ordinary base ammo method creates **EntityHollyArrowShot** with constructor inputs `maxAge = 120` and `piercingValue = 0`, then adds **0.25** to its vertical motion. Spectral uses the same projectile and vertical adjustment.
- The ordinary projectile's gravity getter returns the float value approximately **0.05**.
- **Lunar Archergun** creates **EntityLunarHollyArrowShot** instead. Its gravity getter returns **0**, and the inspected Lunar ammo method does not add the base method's 0.25 vertical adjustment.

These facts describe the selected code paths. They do not establish an exact travel distance, constant speed through every collision, or a measured six-second useful range. Projectile updates, collision handling, server ticks and other mods still matter.

## Effects: when the hit hook actually runs

| Weapon | Checked behavior | Important ordering or limit |
|---|---|---|
| Coral | Requests Slowness, 40 ticks, amplifier 2, on a living target | Happens **before** delegating to the base damage method; it is not gated by the base damage helper's success result |
| Pyro | Calls the target's fire method with 5 seconds when the target is living | Runs from the successful base damage-effect hook; fire immunity and other defenses still apply |
| Rosidian | Rolls `nextInt(8) == 0`, then requests healing of 1 health point for the shooter | A 1-in-8 roll per eligible effect-hook call, not guaranteed every eighth shot and not 1 full heart |
| Viral | Requests Poison, 40 ticks, amplifier 2, with ambient and particle flags true | Runs from the successful base damage-effect hook on a living target; potion acceptance is separate |
| Mecha, Skeletal, Troll's | No declared special impact or ammo override among the checked behavior methods | Do not invent an extra ability from their names |
| Lunar | Uses the zero-gravity projectile described above | Not a bow draw-speed upgrade |
| Spectral | Skips the inventory-item payment in its ammo method | Does not create a survival arrow-farming promise |

Amplifier 2 corresponds to level III in ordinary potion naming; 40 ticks is nominally two seconds at 20 TPS. Neither guarantees that a target accepts or retains the effect for that wall-clock duration.

## Damage multiplier caveat for restoration

The selected **BaseArchergun.doImpactDamage** passes the float-converted damage getter directly to `dealRangedDamage`. It does **not multiply that damage by the incoming bulletDmgMultiplier**. It forwards the multiplier to the effect hook only after the helper reports success. A nonliving-target fallback also uses the damage getter.

Do not copy the ordinary BaseGun multiplier formula onto archerguns or promise that a modifier changes final damage without tracing its route. The inherited getter can still apply AoA's hardcore setting; the constructor table is not the final health change. Target defenses and external hooks remain relevant.

## Block impacts and arrow recovery

After the ordinary projectile delegates to BaseBullet's impact method, it attempts to create an in-ground Holly Arrow only when all three checks hold: **server side, projectile marked dead, block hit**. It copies the motion fields and attempts a world spawn.

- A Creative player shooter **or the Spectral Archergun** changes that new arrow's pickup status to **CREATIVE_ONLY**.
- Therefore Spectral's ammo-free shots are not evidence of free recoverable Survival ammunition.
- The selected method does not verify that the world accepted the replacement arrow. Other cases leave pickup behavior to the created arrow's defaults and subsequent processing; a guaranteed refund is not established here.
- Entity hits do not take this block-recovery branch.

## Practical test and porting checklist

- Start with a small known Holly Arrow balance, then compare Greed and split-stack inventories.
- Compare Lunar and ordinary trajectories on a safe test range without assuming an exact range from maxAge.
- Test Coral against damage-rejecting targets separately from Pyro, Viral and Rosidian because the effect ordering differs.
- Check Spectral with zero ammo, then verify cooldown, durability and Creative-only block-arrow pickup separately.
- Record normal/hardcore damage and any projectile multiplier independently.
- Preserve these resource and effect semantics in optional TaCZ-quality remodels; reload animations remain optional.

[Released registration, identity, base and projectile evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-archergun-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/archergun-art-evidence-1.12.2.json).
