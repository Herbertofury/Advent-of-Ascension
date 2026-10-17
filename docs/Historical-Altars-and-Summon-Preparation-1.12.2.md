# Historical altars and summon preparation

**Minecraft 1.12.2 / AoA 3.3.6.** Match the altar with its input, then read the exceptions before activating it. This reference covers **23 concrete classes in the historical altar package**. It is not a claim to catalog every boss-summoning mechanism in AoA or to certify those mechanics in a modern port.

[Worlds and travel](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Four Guardians](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Four-Guardians-Altar-and-Rewards-1.12.2) · [Primordial Five](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Primordial-Five-Shrine-and-Phase-Guide-1.12.2) · [Ancient Cavern](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2)

![Historical altar blocks and declared inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/historical-altar-inputs-1.12.2.webp)

## Start with the common rule, then check the override

The shared `BossAltarBlock` handler checks the held activation item, rejects Peaceful on the server, and calls the altar's condition method. When that condition passes, it consumes **one held item outside Creative before calling the activation effect**.

This is not a universal fee for every row below. Clunkhead uses durability; Guardian and Rockrider are separate block handlers; Primordial overrides the ordinary payment flow; Army Block's condition has a side effect and returns false. Delayed effects and item-use hooks also change what a right-click actually does.

The shared handler has no general dimension gate or universal nearby-boss check. Do not treat a method that creates an entity as proof that the structure, item acquisition, multiplayer behavior or interaction precedence is fully working in a target build.

## Altar and input index

Block and item links open the exact historical inventory record. Creature links open that release's bestiary with its model and loot references.

| Block | Input / preparation | Declared result or path |
|---|---|---|
| [Army Block](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.ArmyBlock.name) | No fixed item key; Elder/wave route | Skele-Elder preparation; see the wave exception below |
| [Baroness Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.BaronessAltar.name) | [Warlock Gem](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WarlockGem.name) | [Baroness](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Abaroness) |
| [Candy Block](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.CandyBlock.name) | [Treat Bag](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TreatBag.name) | [Cotton Candor](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acotton_candor) |
| [Clunkhead Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.ClunkheadAltar.name) | [Mega Rune Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MegaRuneStone.name); one durability damage | [Clunkhead](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aclunkhead) |
| [Craexxeus Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.CraexxeusAltar.name) | [Ancient Ring](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AncientRing.name) | [Craexxeus](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acraexxeus) |
| [C.R.E.E.P Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.CreepAltar.name) | [Explosive Gems](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveGems.name) | Delayed [Creep](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acreep) ritual |
| [Dracyon Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.DracyonAltar.name) | [Call of the Drake](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CallOfTheDrake.name) | [Dracyon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Adracyon) |
| [Graw Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.GrawAltar.name) | [Guardian's Eye](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GuardiansEye.name) | [Graw](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agraw) |
| [Guardian Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.GuardianAltar.name) | Voliant Heart + four powered sides | [Four linked Guardians](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Four-Guardians-Altar-and-Rewards-1.12.2) |
| [Hive Spawner](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.HiveSpawner.name) | [Hive Egg](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HiveEgg.name) | [Hive King](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahive_king) |
| [Hydro Table](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.HydroTable.name) | [Pure Water Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PureWaterStone.name) | [Hydrolisk](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahydrolisk) |
| [Illusion Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.IllusionAltar.name) | [Staring Eye](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.StaringEye.name) | [Elusive](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelusive), [EntityElusiveClone](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aelusive_clone) |
| [Kror Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.KrorAltar.name) | [Boulder Dash](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoulderDash.name) | Charging Table + delayed [Kror](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Akror) |
| [Mechbot Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.MechbotAltar.name) | [Gold Spring](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoldSpring.name) | [Mechbot](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amechbot) |
| [Power Station](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.PowerStation.name) | [Giant Crystal](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GiantCrystal.name) | [Crystocore](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acrystocore) |
| [Primordial Shrine](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.PrimordialShrine.name) | Eight lit Dustopian Lamps | [Kajaros → five phases](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Primordial-Five-Shrine-and-Phase-Guide-1.12.2) |
| [Rockrider Shrine](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.RockriderShrine.name) | Floating Stone + requested 200 Energy | Heavy Boulder conversion; not an immediate boss spawn |
| [Shadow Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.ShadowAltar.name) | [Book of Shadows](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BookOfShadows.name) | Lamp sequence → [Shadowlord](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashadowlord) |
| [Silverfoot Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.SilverfootAltar.name) | [Silvro Coin](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SilvroCoin.name) | [Silverfoot](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Asilverfoot) |
| [Toy Box](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.ToyBox.name) | [Toy Gyrocopter](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ToyGyrocopter.name) | [Gyro](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agyro) |
| [Vinocorne Shrine](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.VinocorneShrine.name) | [Petals](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Petals.name) | Living Growth → [Vinocorne](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Avinocorne) |
| [Visualent Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.VisualentAltar.name) | [Observing Eye](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ObservingEye.name) | [Visualent](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Avisualent) |
| [Voxxulon Altar](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.VoxxulonAltar.name) | [Vile Stone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VileStone.name) | [Voxxulon](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Avoxxulon) |

These are declared released-handler references, not a list of universally obtainable crafting recipes. Use [historical recipe search](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2) for an input's listed recipes; a missing recipe does not prove the item has no drop, trade or other acquisition route.

## Exceptions worth knowing before spending an input

### Clunkhead: durability, not stack consumption

Clunkhead Altar overrides the payment branch with `damageItem(1, player)` outside Creative. The Mega Rune Stone registration supplies maximum damage 5. That does not establish an unconditional number of activations after enchantments, damage handling and other mods are considered. Do not describe the ordinary altar's one-item shrink as this altar's cost.

### Hive King: check the nearby entity box

Hive Spawner additionally requires that its altar-centered bounding box, expanded by 20, contain no Hive King. This is a specific entity-class query, not a blanket check for every boss or a spherical distance guarantee.

### Illusion Altar: boss and clone occupy different positions

The selected effect creates Elusive and an Elusive Clone. The clone's horizontal position is based on the altar and the player's look vector; the real entity receives additional random horizontal offsets and its own height lookup. Do not expect both entities to appear on the altar itself or treat the clone as an independently registered loot-equivalent boss.

### Kror: prepare a Charging Table and remain nearby

Kror Altar requires a **Charging Table directly above it**. Holding the Charging Table item returns false from the altar override, allowing the separate placement interaction to be considered rather than starting the ritual with that item.

With Boulder Dash, the shared payment happens before the delayed task starts. The task then checks:

- The player is still in the captured original world.
- Player distance from the Charging Table is no greater than 10 under the selected distance method.
- Difficulty is not Peaceful.
- The expected Charging Table still occupies its position.

It requests **20 Energy per successful charge step**, advancing an internal amount toward 200. Ten successful steps are followed by a separate callback that attempts the spawn. Resource helpers may modify actual payment or bypass it under configuration/Creative rules; the requested total is not an unconditional measured drain.

The first task is scheduled after one second, and successful charging reschedules after one second. These are scheduler delays, not a promise that the encounter begins at an exact wall-clock deadline. Failure to pay stops that path without a reschedule in the selected branch. Moving away, changing worlds, removing the table or failing the later space search does not show a refund of the already consumed Boulder Dash or earlier Energy payments.

The spawn-position search retries while collision remains, with a failure branch once its counter exceeds 64. Clear space before starting and test cancellation/recovery in a copied save when restoring the system.

### C.R.E.E.P.: delayed explosions are part of the ritual

The effect schedules a Creep task after one second. Each run selects a corner nine blocks from the adjusted ritual center on both horizontal axes and requests a strength-1.5 explosion governed by `doStrongerMobGriefing`. After four runs, it attempts to spawn C.R.E.E.P. at the final corner; intermediate runs reschedule after two seconds.

Do not assume immediate spawning, a harmless waiting period or a fixed real-time completion guarantee. These are selected scheduler and explosion inputs, not a measured live ritual.

### Shadowlord: lamps, a delayed spawn and a realmstone side route

Shadow Altar schedules its task after one second. The task scans the 5×2×5 area around the altar, switching a lit `LampBlock` off and rescheduling after two seconds when it finds one. After it exhausts that stage, it schedules the spawn phase; later it revisits four corner lamp positions and changes matching lamps to their on/fixed form.

The activation effect also checks Night Vision and a Blank Realmstone. When both qualify, it consumes a Blank Realmstone through the inventory helper and gives or drops a **Dustopia Realmstone**. This is an activation-side route, not a requirement to defeat Shadowlord first. It remains separate from the Book of Shadows payment in the shared altar handler.

The task stores the player and altar coordinates but reads `player.world` while it runs. World changes, logout, repeated activation and lamp ownership/protection need explicit testing before calling this sequence stable. Stay in the ritual's world rather than assuming every delayed task has Kror's captured-world guard.

### Vinocorne: let Living Growth complete

Vinocorne Shrine requires the block above it to be replaceable. It places Living Growth there and schedules a 40-tick update. Growth begins at stage 0, advances through stage 5, then the stage-5 update attempts to spawn Vinocorne and removes the growth block. That is six scheduled update opportunities from the initial placement, nominally 240 game ticks if every interval proceeds as requested.

The growth depends on the shrine beneath it; removing the shrine also removes matching growth above it. Do not treat an ordinary input payment as proof that a removed, replaced or interrupted growth block still yields the boss. Scheduled game ticks are distinct from the separate executor delays used by C.R.E.E.P., Kror and Shadowlord.

### Army Block: the condition is a starter, not a successful fee gate

Army Block's condition can create a wave-0 Skele-Elder when its nearby class-filtered query finds neither a Skele-Elder nor a Skeletron. It then **returns false**. Consequently, that path does not reach the shared handler's item shrink or ordinary activation effect; do not invent an arbitrary-held-item consumption bug from its null activation key.

The selected Skele-Elder death callback advances the wave when it has a nonnegative wave, an Army Block position, has squared distance **less than 2500** from that position (the selected 50-block threshold), and the block is still an Army Block. The broader wave roster and save/reload behavior require their own encounter walkthrough; this catalog only establishes the entry connection.

### Rockrider: convert first, then use the dropped-boss-item path

Rockrider Shrine does not directly instantiate Rockrider. It checks Floating Stone, requests **200 Energy**, shrinks one Floating Stone on successful payment and gives or drops a Heavy Boulder. The selected block callback has no separate Creative exemption around that Floating Stone shrink, even though the resource helper can behave differently under Creative/configuration.

Heavy Boulder defines Rockrider spawning in Haven, subject to its collision-space check. The shared dropped-boss-item route is triggered by the item-toss event outside Peaceful, which replaces the tossed item entity with an owner-associated boss item. Its constructor supplies a lifespan of 200 ticks, and the selected update checks the timer before calling the item-specific spawn path. That is a source timer, not a live wall-clock guarantee.

**Drop one boulder at a time.** The conversion helper carries the tossed ItemStack into the special entity, and the successful item-specific spawn branch removes that entity. Do not assume dropping a whole stack means one separate encounter per item or that a rejected entity-spawn return restores the stack. A failed `canSpawnHere` check has a separate fallback setting the item lifespan to 6000; output, pickup and persistence still need runtime validation.

### Treat Bag and Toy Gyrocopter have item-use paths too

The Candy Block handler declares Treat Bag as its key, but Treat Bag also defines an edible use-finish route with a 120-tick maximum use duration. That route requires Candyland and non-Peaceful conditions, creates Cotton Candor above the user, and shrinks one bag in its own server branch. Its `onItemUseFirst` returns success, so actual item-versus-block interaction precedence must be checked rather than claiming the declared Candy Block handler alone proves a working right-click route.

Toy Box's effect creates Gyro. The Toy Gyrocopter item's separate right-click path creates a Gyrocopter entity outside Peaceful and shrinks the held item outside Creative. Keep those entry paths distinct instead of merging their entity names or assuming the same spawn position.

### Guardian and Primordial shrines have dedicated puzzles

Use the [Four Guardians guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Four-Guardians-Altar-and-Rewards-1.12.2) for four-sided redstone, Voliant Heart, wire removal and final-color rewards. Use the [Primordial Five guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Primordial-Five-Shrine-and-Phase-Guide-1.12.2) for eight lit lamps and the phase chain. Use the [Crystal Extension comparison](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crystal-Extension-and-Giant-Crystals) before preparing Giant Crystal for the Power Station, especially on older releases with different consumption loops.

## Restoration priorities

1. Preserve exact input identity, dispatch path and cost type. A one-item fee, one durability damage, Energy conversion and a lamp puzzle are different mechanics.
2. Test input acquisition separately from a block's handler. A registered block and input are not proof of a complete survival route.
3. Make failed spawns and interrupted rituals recoverable under a defined policy. Several selected paths consume inputs or change blocks before ignoring an entity-spawn return.
4. Respect thread confinement. The reviewed delayed tasks call `ModUtil.scheduleAsyncTask`, whose selected implementation schedules through a single-thread scheduled executor. Their run methods directly touch worlds, entities and players. Audit this boundary and use the target version's correct server scheduling/lifecycle mechanisms; no reproduced race or applied runtime fix is claimed here.
5. Test world change, logout, unloaded chunks, shutdown, repeated activation, multiplayer and protected blocks/items. One task's guard does not automatically protect the others.
6. Retain event-driven activation and bounded checks. Do not add a permanent global scan merely to imitate a localized interaction; profile the actual target build before claiming faster gameplay.

## Evidence and credits

[Released altar handlers, item-registration bindings and delayed/item paths](https://herbertofury.github.io/Advent-of-Ascension/historical-altar-evidence-1.12.2.json) records 102 selected methods. [Artwork atlas crops and hashes](https://herbertofury.github.io/Advent-of-Ascension/historical-altar-art-evidence-1.12.2.json).

AoA source systems, models and textures: Tslat and contributors. Original documentation and static evidence tooling. No Java/game/mod execution or runtime certification is claimed.
