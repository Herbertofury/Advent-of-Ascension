[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Rune production](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runation-Rune-Shrines-and-Inputs-1.12.2) · [Historical archerguns](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Archergun-Ammunition-and-Special-Effects-1.12.2)

# Historical staves: rune costs, casting and hand safety

**Minecraft 1.12.2 / AoA 3.3.6.** All **57 staff registrations**, **134 rune-cost entries** and their constant damage getters are checked against released classes. This is a preparation reference, not a claim that all 57 spell effects have been fully documented or tested in a game.

![Four historical staff source-model portraits with damage-getter inputs, durability and rune-type counts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/staff-inputs-and-ammo-1.12.2.webp)

## Start with the right runes

1. Find your staff in the table below and gather **every rune type** shown. Quantities are per-type base requirements, not a total shared among different runes.
2. Use [historical Runation production](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runation-Rune-Shrines-and-Inputs-1.12.2) for the release's checked rune routes. The rune links in the staff's inventory panel lead to the corresponding rune portrait and recipe/drop searches.
3. For this historical release, keep rune stacks in **ordinary inventory slots**, rather than either hand, while the hand-routing issue below remains unresolved. This avoids the specific swapped-hand path; it is not a guarantee that every other payment problem is absent.
4. Check the spell's target/environment requirements. **29 staves declare custom precondition methods**; the default method simply returns a non-null object. A rejected custom precondition can prevent the cast before rune payment.
5. Do not hold a gun or blaster in your main hand while trying to use a staff in the offhand: the base staff use path explicitly rejects that pairing.

## What a successful base cast does

On the server, the base use method checks the precondition, then requests rune payment with buffs allowed. A null precondition or failed payment returns failure. After payment it may play the casting sound, then sets a **12-tick cooldown**, records the use statistic, damages the staff by **1**, and finally calls `cast`.

That order matters when restoring the mod: rune payment and wear happen before the specific spell's cast function. A rejected projectile spawn or a later failure inside that function is not automatically refunded by this base method. Twelve ticks is nominally 0.6 seconds at 20 TPS; it is not measured wall-clock timing or proof that no spell changes its cooldown.

## Discounts and Greed

The selected shared helper bypasses rune payment for Creative players. With buffs allowed, each rune type's amount follows:

**max(1, base quantity + 2 if Greed is present − Archmage level − 1 if wearing the full Nightmare set)**

The +2 Greed change is triggered by **any positive level**, not +2 per level. The minimum is one of each required type; discounts do not make a listed rune type free. If `allowBuffs` is false, this helper copies the base map and bypasses both these discounts and its Greed adjustment.

| Base quantity | Archmage level | Full Nightmare set | Greed present | Requested per-type amount |
|---:|---:|---|---|---:|
| 2 | 0 | No | No | 2 |
| 2 | 1 | No | No | 1 |
| 2 | 1 | Yes | No | 1 |
| 2 | 1 | Yes | Yes | 2 |
| 4 | 2 | No | Yes | 4 |

The accompanying 800-case arithmetic model explores these branches; it does not establish which enchantment levels are obtainable, permitted together or provided by other mods.

## Hand-routing defect: exact scope

The released helper's collection phase records **OFF_HAND as marker −1** and **MAIN_HAND as marker −2**. Its consumption phase reads **MAIN_HAND for −1** and **OFF_HAND for −2**. Those are opposite hands.

For example, with a staff in the main hand and a sufficient required rune stack in the offhand, the collected −1 marker leads the consumption path to fetch the staff and cast its item to `RuneItem`. This is a source-backed unsafe cast path. It has not been reproduced in a running game here, so it is recorded as a restoration defect/test target rather than a claim about your current Enderloom build.

A proper fix must keep collection and consumption tied to the same physical stack, account for hand/inventory aliases once, validate all required quantities before mutation, and test insufficient inventories without partial loss. Merely swapping variable names would not prove that every aliasing issue is resolved.

## All 57 staff inputs

**36 of these damage getters return zero.** That does not mean their spells do nothing: effects, summons, healing and other behavior can live in cast/projectile/impact methods. Use the table for supplies and reference inputs, not a damage tier list.

| Staff and portrait | Damage getter | Durability | Base rune costs |
|---|---:|---:|---|
| [Aquatic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AquaticStaff.name) | 10 | 1220 | 2 Wind Rune; 4 Water Rune; 1 Kinetic Rune |
| [Atlantic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AtlanticStaff.name) | 0 | 1250 | 1 Distortion Rune; 2 Energy Rune; 2 Storm Rune |
| [Baron Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronStaff.name) | 12 | 1200 | 2 Wind Rune; 3 Power Rune |
| [Candy Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyStaff.name) | 0 | 950 | 3 Kinetic Rune; 2 Storm Rune |
| [Celestial Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CelestialStaff.name) | 11 | 1150 | 1 Compass Rune; 2 Lunar Rune; 2 Energy Rune |
| [Concussion Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ConcussionStaff.name) | 0 | 1150 | 4 Power Rune; 4 Storm Rune |
| [Coral Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralStaff.name) | 0 | 950 | 2 Water Rune; 8 Kinetic Rune |
| [Crystal Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystalStaff.name) | 0 | 1230 | 2 Distortion Rune; 5 Life Rune |
| [Crystik Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystikStaff.name) | 0 | 1140 | 2 Distortion Rune; 1 Life Rune; 1 Water Rune |
| [Cryston Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystonStaff.name) | 0 | 1240 | 2 Distortion Rune; 4 Energy Rune |
| [Destruction Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DestructionStaff.name) | 0 | 1170 | 2 Power Rune; 2 Energy Rune |
| [Ember Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EmberStaff.name) | 0 | 1400 | 1 Kinetic Rune; 1 Wind Rune; 1 Fire Rune |
| [Everfight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EverfightStaff.name) | 0 | 1050 | 4 Kinetic Rune; 4 Power Rune |
| [Evermight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EvermightStaff.name) | 0 | 1050 | 2 Distortion Rune; 4 Power Rune |
| [Fire Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FireStaff.name) | 5 | 850 | 2 Wind Rune; 2 Fire Rune |
| [Firefly Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FireflyStaff.name) | 11 | 1230 | 2 Wind Rune; 2 Strike Rune; 1 Fire Rune |
| [Firestorm Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FirestormStaff.name) | 16 | 990 | 1 Compass Rune; 2 Fire Rune; 2 Lunar Rune |
| [Fungal Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FungalStaff.name) | 0 | 1130 | 5 Distortion Rune; 2 Life Rune |
| [Ghoul Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GhoulStaff.name) | 0 | 400 | 2 Wind Rune; 1 Distortion Rune; 2 Life Rune |
| [Haunter's Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HauntersStaff.name) | 13 | 1225 | 4 Wind Rune; 4 Energy Rune |
| [Hive Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HiveStaff.name) | 0 | 1130 | 10 Energy Rune; 2 Life Rune |
| [Joker Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.JokerStaff.name) | 0 | 300 | 4 Wind Rune; 4 Kinetic Rune |
| [Kaiyu Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.KaiyuStaff.name) | 0 | 900 | 1 Kinetic Rune; 4 Energy Rune |
| [Lightning Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LightningStaff.name) | 0 | 1070 | 1 Compass Rune; 4 Strike Rune; 4 Storm Rune |
| [Lightshine](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Lightshine.name) | 0 | 700 | 3 Power Rune; 3 Life Rune; 2 Distortion Rune |
| [Lunar Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarStaff.name) | 16 | 1250 | 1 Compass Rune; 2 Lunar Rune |
| [Lyonic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicStaff.name) | 0 | 1100 | 1 Energy Rune; 1 Wind Rune; 2 Wither Rune; 1 Strike Rune |
| [Mecha Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechaStaff.name) | 0 | 1110 | 2 Wind Rune; 1 Distortion Rune; 1 Power Rune |
| [Meteor Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MeteorStaff.name) | 14 | 1190 | 1 Compass Rune; 2 Lunar Rune; 2 Kinetic Rune |
| [Moonlight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MoonlightStaff.name) | 0 | 1130 | 1 Compass Rune; 2 Lunar Rune; 2 Kinetic Rune |
| [Nature Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NatureStaff.name) | 0 | 1450 | 4 Life Rune; 2 Energy Rune |
| [Nightmare Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareStaff.name) | 14 | 1200 | 1 Compass Rune; 2 Lunar Rune; 2 Poison Rune |
| [Noxious Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NoxiousStaff.name) | 3.5 | 1210 | 2 Wind Rune; 2 Poison Rune; 2 Storm Rune |
| [Phantom Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PhantomStaff.name) | 12 | 1060 | 2 Wind Rune; 2 Distortion Rune |
| [Poison Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonStaff.name) | 5 | 850 | 2 Wind Rune; 2 Poison Rune |
| [Power Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PowerStaff.name) | 8 | 1010 | 2 Wind Rune; 2 Power Rune |
| [Primordial Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrimordialStaff.name) | 15 | 1230 | 2 Wind Rune; 2 Wither Rune |
| [Reef Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ReefStaff.name) | 0 | 1230 | 2 Energy Rune; 1 Water Rune |
| [Rejuvenation Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RejuvenationStaff.name) | 0 | 870 | 4 Life Rune; 2 Energy Rune |
| [Rosidian Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianStaff.name) | 10.5 | 1180 | 3 Wind Rune; 2 Water Rune; 1 Life Rune |
| [Runic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicStaff.name) | 0 | 1000 | 5 Distortion Rune |
| [Shadowlord Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShadowlordStaff.name) | 0 | 1200 | 10 Wither Rune; 2 Life Rune |
| [Show Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShowStaff.name) | 0 | 900 | 3 Compass Rune; 3 Power Rune |
| [Shyre Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShyreStaff.name) | 0 | 1380 | 3 Energy Rune; 3 Distortion Rune |
| [Sky Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkyStaff.name) | 0 | 1480 | 2 Wind Rune; 2 Kinetic Rune; 1 Energy Rune |
| [Striker Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.StrikerStaff.name) | 0 | 850 | 2 Strike Rune |
| [Sun Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SunStaff.name) | 0 | 960 | 2 Fire Rune; 1 Storm Rune; 3 Lunar Rune |
| [Surge Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SurgeStaff.name) | 0 | 1270 | 4 Power Rune; 1 Energy Rune |
| [Tangle Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TangleStaff.name) | 9 | 1140 | 2 Wind Rune; 2 Poison Rune; 1 Storm Rune |
| [Ultimatum Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UltimatumStaff.name) | 0 | 750 | 5 Life Rune; 3 Power Rune; 8 Distortion Rune |
| [Underworld Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.UnderworldStaff.name) | 5 | 1140 | 1 Compass Rune; 3 Kinetic Rune |
| [Warlock Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WarlockStaff.name) | 0 | 1050 | 3 Power Rune; 2 Kinetic Rune |
| [Water Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WaterStaff.name) | 5 | 850 | 2 Wind Rune; 2 Water Rune |
| [Web Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WebStaff.name) | 0 | 1420 | 4 Distortion Rune; 4 Energy Rune |
| [Wind Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WindStaff.name) | 5 | 850 | 3 Wind Rune |
| [Wither Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherStaff.name) | 5 | 850 | 2 Wind Rune; 2 Wither Rune |
| [Wizard's Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WizardsStaff.name) | 0 | 800 | 3 Life Rune; 3 Power Rune; 3 Distortion Rune |

## Restoration acceptance checklist

- Compare all 57 identities, durability inputs and 134 rune entries against this release before changing spell balance.
- Test plain inventory rune stacks, partial stacks, extra rune types, both hands and aliases to inventory slots.
- Test Creative, buffs disabled, Greed, Archmage and full/incomplete Nightmare sets independently.
- Verify custom precondition failures leave payment, wear and cooldown unchanged.
- Separately test a spell whose later spawn/action fails, because the base method pays first.
- Give every spell an individual effect review before claiming complete combat, utility or multiplayer coverage.
- Preserve rune-based casting in optional weapon remodels. A reload animation should not silently add a magazine requirement.

[Released constructor, rune and casting evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-staff-inputs-1.12.2.json) · [Arithmetic and hand-routing models](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/staff-cost-models-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/staff-art-evidence-1.12.2.json).
