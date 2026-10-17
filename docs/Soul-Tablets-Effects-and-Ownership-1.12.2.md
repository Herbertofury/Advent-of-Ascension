# Historical Soul Tablets: effects, costs and ownership

**Minecraft 1.12.2 / AoA 3.3.6.** Compare all 17 registered tablet items, their entity effects, crafting routes and shared lifecycle. These are released-code references, not certification that a modern restoration or a particular modpack works identically.

[Train Anima and collect fragments](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) · [Historical Extraction rewards](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2) · [Armor acquisition across releases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Acquisition-Across-Versions)

![Seventeen historical Soul Tablet source-model previews ordered by Anima level](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/soul-tablet-catalog-1.12.2.webp)

## Choose the effect, then budget its Soul supply

The table's placement number is the **base** before effective Anima level and full-set adjustments. “Supply check” is the selected helper's base request, `baseTickDrain × 5`, before the full Anima set factor. It is not a measured per-second drain.

“Box expansion” is added to the tablet entity's axis-aligned bounding box for the target query. It is **not a spherical radius** or a guarantee of line-of-sight filtering.

| Tablet / illustrated recipe | Required Anima | Base placement Soul | Base supply-check Soul, approximately | Box expansion |
|---|---:|---:|---:|---:|
| [Tablet of Sight](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Asight_tablet) | 1 | 52.5 | 0.395 | 23 |
| [Tablet of Satiation](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Asatiation_tablet) | 3 | 43.5 | 0.7625 | 25 |
| [Tablet of Oxygen](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aoxygen_tablet) | 6 | 7.5 | 0.45 | 11 |
| [Tablet of Gravity](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Agravity_tablet) | 11 | 27 | 1.6085 | 14 |
| [Tablet of Cleansing](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Acleansing_tablet) | 16 | 30 | 0.8 | 7 |
| [Tablet of Agility](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aagility_tablet) | 17 | 15 | 0.84 | 15 |
| [Tablet of Awareness](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aawareness_tablet) | 23 | 7.5 | 0.455 | 20 |
| [Tablet of Breeding](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Abreeding_tablet) | 29 | 75 | 2.55 | 15 |
| [Tablet of Energy](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aenergy_tablet) | 37 | 19.5 | 1.608 | 12 |
| [Tablet of Resistance](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aresistance_tablet) | 45 | 33 | 1.535 | 16 |
| [Tablet of Proficiency](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Aproficiency_tablet) | 56 | 60 | 0.715 | 14 |
| [Tablet of Distortion](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Adistortion_tablet) | 64 | 45 | 1.465 | 10 |
| [Tablet of Pressure](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Apressure_tablet) | 71 | 37.5 | 1.51 | 10 |
| [Tablet of Sanctity](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Asanctity_tablet) | 77 | 67.5 | 1.34 | 9 |
| [Tablet of Strength](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Astrength_tablet) | 85 | 47 | 1.485 | 10 |
| [Tablet of Vitality](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Avitality_tablet) | 91 | 54 | 1.415 | 13 |
| [Tablet of Untiring](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&q=aoa3%3Auntiring_tablet) | 97 | 90 | 0.635 | 20 |

All 17 recipes reference Fragmented Anima Stone. Open an individual recipe for its other ingredients and exact shaped grid; they are not interchangeable generic tablet recipes.

## Placement: support, level, collision and payment

1. Use the tablet on the **upper face** of a block whose actual state reports a **solid upper block-face shape**.
2. On the server, meet its effective Anima requirement or use Creative.
3. The code constructs the tablet, positions it at the clicked X/Z and the support collision box's top Y, and checks entity collision.
4. It requests the adjusted Soul payment. If the resource helper accepts, it calls the spawn method.
5. Outside Creative, it then shrinks the held tablet stack by one.

The selected path **does not check whether the spawn call succeeded** before shrinking. A cancelled spawn can therefore require recovery logic in a port; this is a code-derived test target, not a reproduced item-loss incident. Creative bypasses the level restriction and stack shrink in this method, but it still reaches the resource helper; do not infer that every helper/configuration payment rule is bypassed.

### Initial cost versus ongoing supply

Initial placement requests:

`basePlacement × (1 − (effectiveAnima − 1) / 200) × armorFactor`

The armor factor is 0.5 for the full Anima set, otherwise 1. At effective Anima 1 the level multiplier is 1; at effective 100 it is 0.505. The shared skill getter caps effective level at 100.

The ongoing helper instead requests:

`baseTickDrain × 5 × armorFactor`

It does not include the initial level discount. The server update path considers supply/effects when the entity is alive and `ticksExisted % 5 == 0`. Failed supply deactivates the tablet. These conditional tick checks are not a measured real-time rate or a guarantee that every modded timing/configuration behaves the same.

## Every selected tablet effect

Potion amplifiers below are zero-based values from the call, and durations are ticks. The shared target helper uses the expanded box; player-targeting predicates do not restrict their effects to the tablet's owner or an owner-selected team in these methods.

### Tablet of Sight

Players: Night Vision, 300 ticks, amplifier 0, when absent or remaining duration is below 250.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Asight_tablet).

### Tablet of Satiation

Players needing food or with saturation at most zero: calls food addStats(1, 2.0). This is a helper input, not a direct +2 saturation claim.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Asatiation_tablet).

### Tablet of Oxygen

Living players with air below 300: sets air to 300.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aoxygen_tablet).

### Tablet of Gravity

Living players: Jump Boost, 10 ticks, amplifier 4.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agravity_tablet).

### Tablet of Cleansing

Living players with active effects: removes effects whose potion reports isBadEffect(). Other mod effects depend on their classification.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acleansing_tablet).

### Tablet of Agility

Living players: Speed, 10 ticks, amplifier 2.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aagility_tablet).

### Tablet of Awareness

Living IMob targets: Glowing, 10 ticks, amplifier 0.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aawareness_tablet).

### Tablet of Breeding

Living animals not already in love, growing age at least zero: age zero enters love with owner; age greater than 10 is reduced by 10. Babies are excluded by this predicate.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Abreeding_tablet).

### Tablet of Energy

Living players: requests +10 Energy through the resource helper.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aenergy_tablet).

### Tablet of Resistance

Living players: Resistance, 10 ticks, amplifier 1.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aresistance_tablet).

### Tablet of Proficiency

Selected doTickEffect method is empty. No XP bonus is established by this method; do not invent an effect from the name.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aproficiency_tablet).

### Tablet of Distortion

Living players: Invisibility, 10 ticks, amplifier 0.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Adistortion_tablet).

### Tablet of Pressure

Living IMob targets: Slowness, 10 ticks, amplifier 2.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Apressure_tablet).

### Tablet of Sanctity

Living IMob targets: sets fire for 1 second if not fire-immune; otherwise applies Wither for 40 ticks, amplifier 0.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Asanctity_tablet).

### Tablet of Strength

Living players: Strength, 10 ticks, amplifier 1.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Astrength_tablet).

### Tablet of Vitality

Only when world time modulo 10 is zero: living players without Regeneration receive it for 50 ticks, amplifier 1.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Avitality_tablet).

### Tablet of Untiring

Living players: Haste, 10 ticks, amplifier 0.

[Inspect this tablet model](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Auntiring_tablet).


### Proficiency: an explicit documentation gap

Its released `doTickEffect` consists only of a return instruction. The shared base can still perform its ordinary Soul-supply check while active, but this selected effect method does not grant a benefit. Do not describe it as a working XP enhancer from its name alone. Restoring an intended effect requires separate design/source evidence and tests; this guide does not invent one.

### Breeding: do not confuse adults and babies

The selected predicate requires growing age **at least zero**, so it excludes negative-age babies. Age zero calls `setInLove(owner)`; values above 10 are reduced by 10. Values 1–10 receive neither operation in this callback. Normal animal ticking is a separate mechanism and may continue changing those ages.

## Reclaiming and losing support

The selected interaction accepts the recorded owner UUID, or any player when the UUID is null. For an allowed interaction while the entity is alive:

- On the server outside Creative, an empty hand receives a new tablet stack directly.
- With an occupied hand, it tries inventory insertion and drops the stack if insertion fails.
- The tablet entity is then removed and the action reports SUCCESS.
- Creative interaction removes it without this ordinary item-return branch.

The returned stack is newly constructed from the relevant tablet item. Original custom item components/NBT are not retained by this selected entity storage path; custom-name or other modded-item round trips need their own preservation policy.

On the server's eligible update check, air directly below triggers a tablet item drop and entity removal. If the owner object and drop exist, the code assigns the drop's owner name. This is an air-below check, not the same full support-face check used at placement; replacement with a non-air but unsuitable support is a separate test case.

## Deactivation and save/reload boundaries

### Refilling Soul does not show an automatic retry here

A failed supply check calls `deactivate()`, setting the synchronized active flag false. The update branch tests supply only while active. There is no reactivation method in the selected base class. Reclaiming and placing again uses a new entity, but do not promise automatic restart merely from recovering Soul.

### Owner UUID persistence depends on the resolved owner object

The reader restores `ownerUUID` from `OwnedBy` and attempts to resolve that UUID through the server's current player list. The writer stores `OwnedBy` only when the **owner object is non-null**, rather than checking only the UUID.

An independent model with a fresh output compound therefore distinguishes:

| Owner present in player list when reading | UUID read | Resolved owner object | Next selected write |
|---|---|---|---|
| Yes | Preserved | Present | Writes `OwnedBy` |
| No | Preserved in memory | Null | Omits `OwnedBy` |

This is a **source-derived ownership persistence test target**, not a claim that live theft or ownership loss has been reproduced. The selected supply helper also immediately fails when the owner object is null. Reconnection, chunk load order, dimension changes and repeated saves need live dedicated-server testing before relying on persistence.

The active flag initializes true through entity data registration and is not explicitly written/read by these custom NBT methods. Do not assume a saved deactivation state or an offline-owner state is restored exactly without testing.

## Restoration and compatibility checklist

- [ ] All 17 item → entity → recipe joins, exact skill requirements and stable IDs.
- [ ] Initial versus ongoing Soul payment; full/partial Anima set and configuration variants.
- [ ] Upper solid face, slabs/shapes, entity collisions, rejected spawn and refund behavior.
- [ ] Player/IMob/animal target predicates, range corners, other players and modded effect classifications.
- [ ] Proficiency's intended effect and Soul spending; do not mark it complete solely because placement succeeds.
- [ ] Breeding ages −1/0/1/10/11, love state, and owner attribution.
- [ ] Deactivation, replenished Soul, reclaim/re-place and save/reload.
- [ ] Owner online/offline at load, later reconnect, dimension changes and a second save with unresolved owner.
- [ ] Reclaim with empty hand, full inventory, Creative and custom item data; support removed versus replaced.
- [ ] Dedicated-server concurrency and profiling without repeated world-wide scans.

## Evidence and limits

The catalog joins **17 released constructor bindings, 17 recipes and 17 entity portraits**, with **89 selected released methods** covering item construction, effect predicates, effect bodies and the shared lifecycle. The owner/write example is an independent model. No game/server/mod was executed for this documentation pass.

- [Released catalog and lifecycle evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-tablet-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-tablet-art-evidence-1.12.2.json)
- [Pinned upstream base tablet entity](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/entity/misc/tablet/EntitySoulTablet.java)
- [Pinned upstream tablet item](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/item/tablet/TabletItem.java)
