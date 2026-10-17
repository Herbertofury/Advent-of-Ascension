# Experiment W-801 and the reserved-item chain

**Minecraft 1.12.2 · AoA 3.3.6.** This is a spoiler-marked map of the declared hidden sequence and its item-validation behavior. The released code has been traced; the complete quest has not been played through or certified here. Several transitions need callback-order and client/server tests before a restored build can claim that the full sequence works.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-experiment_w801.webp" width="160" height="160" alt="Experiment W-801">

## Protect the item’s sequence data

Reserved items and Experiment W-801 require a nonempty stack with an NBT compound whose **alien_orb boolean is true**. Their valid-stack constructors create that flag. A display name or matching item ID alone is insufficient.

- An invalid inventory stack is set to count zero and the supplied inventory slot is replaced with EMPTY during its update callback.
- An invalid dropped stack is emptied and its item entity is removed.
- Several quest transitions replace an entire hand stack rather than shrinking one item. Do not assume stacked or custom-tagged inputs survive.
- Restoration/migration code must preserve valid flags and test slot ownership before enabling those cleanup callbacks. The wiki does not award, edit or spawn these items.

<details>
<summary><strong>Spoilers: inspect the declared sequence</strong></summary>

### 1. Alien Orb entry condition

The selected player-death callback calls the reserved-item helper. The helper checks the lowercased **registry path**, not translated display names:

| Slot | Required first letter |
|---|---|
| Main-hand item | a |
| Helmet / armor slot 3 | l |
| Chest / armor slot 2 | i |
| Legs / armor slot 1 | e |
| Boots / armor slot 0 | n |

If its other checks pass and its inventory helper does not find an existing Alien Orb, it attempts to drop a valid Alien Orb. The helper returns early when health is positive and the world is not Hardcore; this does not make Hardcore a requirement. Treat this as an in-game death-triggered route with normal inventory/world-loss risks, not a recommended test on a valuable save. No specific equipment combination is certified by the name-prefix predicate alone.

### 2. Follow the transformation branches

| Current stage | Declared interaction | Result and important caveat |
|---|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-alien_orb.webp" width="80" height="80" alt="Alien Orb"><br>Alien Orb | Interact with a Zal Child while holding the orb. | Server branch replaces the used hand with valid Fleshy Bones and calls the NPC removal helper. A Zal Citizen instead supplies a special dialogue key; it is not this conversion. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-fleshy_bones.webp" width="80" height="80" alt="Fleshy Bones"><br>Fleshy Bones | Use on a Charging Table. | The item-use branch replaces the used hand with valid Dark Bones. This branch has no local world.isRemote guard; client/server validation is required. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-dark_bones.webp" width="80" height="80" alt="Dark Bones"><br>Dark Bones | Use on a Mineralization Station. | Replaces the used hand with valid Rock Bones; also requires side/reconciliation testing. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-rock_bones.webp" width="80" height="80" alt="Rock Bones"><br>Rock Bones | Interact with an Assassin. | Server branch replaces the used hand with a valid Millennium Upgrader. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-millennium_upgrader.webp" width="80" height="80" alt="Millennium Upgrader"><br>Millennium Upgrader | The item’s hit callback sees both attacker and target in lava. | Server branch replaces the attacker’s main hand with a valid Molten Upgrader. This is not a generic lava-crafting recipe. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-molten_upgrader.webp" width="80" height="80" alt="Molten Upgrader"><br>Molten Upgrader | At moon-phase factor 1, the hit callback sees a qualifying target at health ≤ 0. | For Dark Beast, Irkling, Night Watcher, Scrubby or Skellox, it clears the attacker’s main hand and attempts to drop a valid Moonstone. Lethal-hit callback ordering is a required runtime test. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-moonstone.webp" width="80" height="80" alt="Moonstone"><br>Moonstone | Hit an Arcworm, then satisfy its height/attacker check. | The hit branch requests Levitation for 200 ticks at amplifier 10. The Arcworm handler separately requires Y > 275, a player attacking entity and Moonstone in that player’s main hand. It drops a valid Experiment W-801, clears that hand and removes the Arcworm. |

### Arcworm boundary details

The Arcworm update method calls handleArcworm after its superclass update. The handler uses the Arcworm’s attacking-entity getter, not simply the nearest player or any player holding Moonstone. It has no local server-side guard. Its spawn predicate also requires Y < 35 before delegating to its parent check, whereas the sequence’s final height gate is Y > 275. The levitation request alone does not prove the target will cross that height under actual physics, obstructions or effect handling.

### Soulbone is not an active step in this branch

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/reserved-portrait-1.12.2-soulbone.webp" width="80" height="80" alt="Soulbone"><br>Soulbone

Soulbone is registered as a reserved item with the same sequence flag, but the proposed Shyre-log conversion is commented out in the pinned source and absent from the checked released block-interaction method. Do not insert that commented idea into the playable walkthrough.

</details>

## The final blaster

Experiment W-801 is hidden from its normal Creative tab in the constructor. Its fire override creates an Arcworm projectile with the supplied maximum-age argument **120**; that argument is not a measured range or guaranteed flight duration. Use the [historical blaster guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blaster-Energy-Timing-and-Spark-Exceptions-1.12.2) for shared Energy and timing behavior. Its own validity flag must remain intact when inventory data is copied or migrated.

## Restoration and compatibility checklist

- [ ] Validate each transition on a disposable test save before advertising end-to-end completion.
- [ ] Preserve the alien_orb boolean on valid reserved items and the final weapon; test missing compound, missing key, false key and true key separately.
- [ ] Check inventory and dropped-entity cleanup, including moved slots, custom names, additional NBT and stacked inputs.
- [ ] Confirm actual lethal-hit callback order for the Molten Upgrader’s target-health check.
- [ ] Reconcile table-use and Arcworm side handling so a port cannot duplicate client/server transitions.
- [ ] Test Y = 275 versus Y > 275, player versus non-player attacker, changed attacking entity and main/offhand differences.
- [ ] Check the five qualifying full-moon target classes individually; do not substitute every night mob.
- [ ] Keep Soulbone’s commented-out source idea separate from implemented content.

## Evidence

[Twenty-one released method records and eight item registrations](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/experiment-sequence-evidence-1.12.2.json) · [Source portrait crop evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/reserved-item-art-evidence-1.12.2.json) · [Weapon acquisition atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Weapon-Acquisition-1.12.2)

Images are exact crops of existing source-asset studies, not new geometry or game screenshots. AoA models, textures and original systems are by Tslat and contributors. No Minecraft process or game save was used for this static documentation pass.
