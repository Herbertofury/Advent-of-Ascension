# Realmstone progression walkthrough: Minecraft 1.16.5

**AoA 3.6.11 · historical full-dimension progression.** This guide combines released GUI/recipe resources with explicitly pinned source conditions. It has not been live-tested in your modpack. Do not apply these acquisition methods to 1.20.1 or 1.21.1 without checking their separate release evidence.

[Search creatures in 1.16.5](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5) · [Versioned recipes](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

## Start with the Worn Book and a Blank Realmstone

Obtain the Worn Book through the Corrupted Traveller’s food exchange. In the pinned 1.16.5 source, using the Worn Book grants a Blank Realmstone if the inventory search cannot find one. The book is not consumed by that branch. Keep it safe so that after converting your blank stone you can obtain another.

![Blank Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-blank.webp)

Use the Blank Realmstone to open its challenge GUI. Most challenges consume one blank from your hands or ordinary inventory through the inventory helper. Do not assume a stone tucked inside a backpack/container is visible to that search. The Lunalus item code specifically searches the main inventory.

A destination stone is a portal key, not a complete expedition plan. Prepare the portal frame, food, equipment, an arrival marker and a return route before leaving. Store irreplaceable supplies before deliberately taking fall, explosion, lava or boss damage.

## A practical first route

1. **Start with a low-chaos acquisition:** collect six sapling species for Precasia, or prepare a controlled mining trip for Deeplands.
2. **Convert one blank at a time.** Check that the named destination stone appeared, then use the Worn Book to obtain another blank as needed.
3. **Use the destination-specific checklist below.** Some conditions inspect player height, active effects, the final damage source or a living interaction target.
4. **Return with a concrete next ingredient.** Follow the recipe explorer for Deep Crystal, the Gravitator, special altar items and other supplies; do not import a recipe from another Minecraft version.
5. **Treat the GUI graph as a route suggestion.** Some code paths require a dimension explicitly; others only require the right creature or station. The Nowhere crafting hint is stale in the inspected release.

## Crafting examples you can follow directly

![Precasia realmstone ingredients](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-precasia-recipe-1.16.5.webp)

[Open the Precasia recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=precasia_realmstone). All six named saplings are required; the illustrated arrangement is not a fixed pattern.

![Shyrelands realmstone ingredients](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-shyrelands-recipe-1.16.5.webp)

[Open the Shyrelands recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=shyrelands_realmstone). Ingredient names and images come from the selected release.

## Destination checklist

### Deeplands

![Deeplands Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-deeplands.webp)

**Where to plan:** Early route from the Overworld.

Break an ore-tagged block at Y ≤ 5 while carrying a Blank Realmstone.

- Survival player; Creative is explicitly excluded.
- The block must belong to Forge’s ore block tag.
- One Blank Realmstone is consumed when the condition succeeds.

**Watch out:** The code checks the ore tag and height, not a special ore species or a guaranteed mining location.

Source checks: [PlayerEvents.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/event/PlayerEvents.java).

### Precasia

![Precasia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-precasia.webp)

**Where to plan:** Early crafting route.

Craft a Blank Realmstone with one each of the six vanilla 1.16.5 saplings: oak, birch, spruce, jungle, acacia and dark oak.

- Seven ingredients in a crafting table.
- Shapeless: their arrangement does not matter.
- Six copies of one sapling do not substitute for the six named species.

**Watch out:** This is the 3.6.11 recipe. Do not replace it with the modern archaeology route.

[Exact released crafting definition](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=precasia_realmstone).

### Barathos

![Barathos Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-barathos.webp)

**Where to plan:** Early combat route.

Deliver the killing melee blow to a Husk with the Blank Realmstone in your main hand.

- The target must be a Husk, not an ordinary Zombie.
- The stone’s hurtEnemy callback checks that the target’s health has reached zero.
- The main-hand stack becomes the Barathos Realmstone.

**Watch out:** Weaken the Husk with another weapon, then switch for the finishing hit. Carrying the stone while killing with a sword is not the same trigger.

Source checks: [BlankRealmstone.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/misc/BlankRealmstone.java).

### Lelyetia

![Lelyetia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-lelyetia.webp)

**Where to plan:** Early fall challenge.

Complete a fall whose event distance is greater than 25 blocks, carrying a Blank Realmstone.

- The fall event must retain a positive damage multiplier.
- One Blank Realmstone is consumed.
- The code tests fall distance, not the height of a tower.

**Watch out:** Prepare protection and recovery. An effect that sets the event’s damage multiplier to zero can prevent this trigger; the condition does not guarantee survival.

Source checks: [PlayerEvents.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/event/PlayerEvents.java).

### Creeponia

![Creeponia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-creeponia.webp)

**Where to plan:** Early explosion challenge.

Take a Creeper explosion hit with primed TNT nearby and a Blank Realmstone in inventory.

- Player health must be positive at the inspected hurt callback.
- A TNT entity must intersect the Creeper’s or player’s bounding box expanded by 3 blocks.
- The damage source must be an explosion directly from a Creeper.

**Watch out:** Placed TNT blocks are not TNT entities. The inspected code does not check the TNT fuse value. Treat this as a dangerous in-game challenge, not a guarantee that the hit will be survivable.

Source checks: [PlayerEvents.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/event/PlayerEvents.java).

### Nether

![Nether Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-nether.webp)

**Where to plan:** Lava challenge.

Toss the Blank Realmstone while your player is in lava.

- The toss event checks the player’s isInLava state.
- The tossed blank item entity is removed and the Nether Realmstone is given to the player.

**Watch out:** Throwing the stone into lava while standing safely on land does not satisfy this code. Arrange fire protection and an exit before attempting it.

Source checks: [PlayerEvents.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/event/PlayerEvents.java).

### Abyss

![Abyss Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-abyss.webp)

**Where to plan:** Nether.

Summon a Wither in the Nether while carrying a Blank Realmstone.

- The world-join check identifies a Wither with 220 invulnerable spawn ticks.
- Eligible players are sought in the Wither’s bounding box expanded by 50 blocks.
- Each qualifying player’s blank stone is consumed.

**Watch out:** This is a summon trigger, not a requirement to defeat the Wither. The Wither still creates a real encounter and terrain risk in your game.

Source checks: [EntityEvents.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/event/EntityEvents.java).

### Crystevia

![Crystevia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-crystevia.webp)

**Where to plan:** Usually reached through Deeplands.

Interact with a living Case Construct while holding the Deep Crystal block item.

- Carry a Blank Realmstone as well.
- The blank is consumed and the reward is given.
- Outside Creative, one held Deep Crystal is also consumed.

**Watch out:** Do not kill the Case Construct first. A similarly named crystal ingredient is not necessarily the required block item.

Encounter reference: [Case Construct](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Acase_construct). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [CaseConstructEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/deeplands/CaseConstructEntity.java).

### Iromine

![Iromine Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-iromine.webp)

**Where to plan:** Mineralization Station; GUI suggests Barathos route.

Use a Blank Realmstone on a Mineralization Station.

- The interaction replaces the held blank with the Iromine Realmstone.
- The inspected station branch itself has no dimension check.

**Watch out:** The GUI parent indicates a progression route, not a hard-coded requirement that this particular interaction happen in Barathos.

Source checks: [MineralizationStation.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/block/functional/utility/MineralizationStation.java).

### Candyland

![Candyland Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-candyland.webp)

**Where to plan:** Precasia.

Finish eating a Heart Fruit in Precasia while carrying a Blank Realmstone.

- The source applies 7 points of self-harm first.
- You must still have positive health afterward.
- One blank stone is consumed for the reward.

**Watch out:** Heal before eating. The exact resulting damage can depend on the game’s damage handling; the source’s 7-point request is not a live measurement.

Source checks: [HeartFruit.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/food/HeartFruit.java).

### Gardencia

![Gardencia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-gardencia.webp)

**Where to plan:** Precasia.

Drop a Blank Realmstone into a fully grown carrot crop in Precasia, then defeat the Primitive Carrotop it creates.

- The dropped item’s block position must contain a max-age vanilla carrot crop.
- The blank item entity and carrot block are removed when the creature is created.
- The creature’s server-side death in Precasia drops the Gardencia Realmstone.

**Watch out:** An immature crop does not qualify. This is a spawned encounter and a ground drop, not an instant inventory exchange.

Encounter reference: [Primitive Carrotop](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Aprimitive_carrotop). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [BlankRealmstone.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/misc/BlankRealmstone.java), [PrimitiveCarrotopEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/precasia/PrimitiveCarrotopEntity.java).

### Haven

![Haven Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-haven.webp)

**Where to plan:** Lelyetia.

Kill a Flye with melee in Lelyetia while your player is at Y ≥ 120.

- The killer must be a player.
- The height test uses the player’s Y, not the Flye’s Y.
- Carry a Blank Realmstone; one is consumed.

**Watch out:** Ranged kills do not satisfy the inspected melee condition. Prepare a safe fighting platform and fall recovery.

Encounter reference: [Flye](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Aflye). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [FlyeEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/lelyetia/FlyeEntity.java).

### Celeve

![Celeve Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-celeve.webp)

**Where to plan:** Lelyetian Warrior encounter.

Kill a Lelyetian Warrior using player-attributed firework damage while carrying a Blank Realmstone.

- The damage-source message ID must be fireworks.
- The source entity must resolve directly to a PlayerEntity in this callback.
- One blank is consumed.

**Watch out:** A firework visual effect or a separate finishing blow is not sufficient. This guide has not live-tested every launcher or modded damage source.

Encounter reference: [Lelyetian Warrior](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Alelyetian_warrior). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [LelyetianWarriorEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/lelyetia/LelyetianWarriorEntity.java).

### Mysterium

![Mysterium Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-mysterium.webp)

**Where to plan:** Creepird encounter.

Kill a Creepird while your player has Poison and carries a Blank Realmstone.

- The death callback runs server-side.
- The player is resolved from the killer or applicable owner.
- Poison must be active when the death condition is checked.

**Watch out:** Bring a recovery plan for Poison. The kill alone, followed by poisoning yourself later, does not meet the condition.

Encounter reference: [Creepird](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Acreepird). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [CreepirdEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/creeponia/CreepirdEntity.java).

### Vox Ponds

![Vox Ponds Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-vox_ponds.webp)

**Where to plan:** Creeponia.

Interact with an AoA trader or banker in Creeponia using the Blank Realmstone while environmentally protected.

- The held item must still be the blank stone.
- The protection helper checks an AdventArmour helmet’s airtight contract.
- A complete Hazmat set satisfies Hazmat’s contract; the source also defines other airtight helmets.

**Watch out:** Do not assume a Hazmat helmet alone counts as the full Hazmat set. The GUI names Hazmat, while the actual helper is broader.

Source checks: [BlankRealmstone.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/misc/BlankRealmstone.java), [DamageUtil.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/util/DamageUtil.java), [HazmatArmour.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/armour/HazmatArmour.java), [FaceMask.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/armour/FaceMask.java).

### Lborean

![Lborean Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-lborean.webp)

**Where to plan:** Gardencian creature + Candied Water.

Expose an eligible Gardencian creature to Candied Water, then kill it as a player while carrying a Blank Realmstone.

- Broccohead and nine other inspected plant-creature classes store a candiedWater flag on contact.
- The flag persists in entity save data.
- The death callback requires a player killer and consumes one blank stone.

**Watch out:** Ordinary water is not Candied Water. In the inspected Broccohead path, contact also adds 50 maximum health and multiplies current health by 1.5, making this a stronger target.

Encounter reference: [Broccohead](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Abroccohead). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [BroccoheadEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/gardencia/BroccoheadEntity.java).

### Dustopia

![Dustopia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-dustopia.webp)

**Where to plan:** Abyss.

Activate the Shadow Altar with its Book of Shadows while Night Vision is active and you carry a Blank Realmstone.

- The altar’s activation condition requires the Abyss.
- The reward is issued during successful activation, alongside scheduling Shadowlord’s spawn.
- One blank is consumed.

**Watch out:** Do not wait until after activation to apply Night Vision. Prepare for Shadowlord even though the realmstone reward does not require defeating the boss.

Encounter reference: [Shadowlord](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Ashadowlord). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [ShadowAltar.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/block/functional/altar/ShadowAltar.java).

### Greckon

![Greckon Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-greckon.webp)

**Where to plan:** Elusive encounter.

Interact with Elusive while holding Nightmare Flakes and carrying a Blank Realmstone.

- The interaction is server-side.
- One blank and one held Nightmare Flakes item are consumed.
- The reward is given directly rather than requiring an Elusive kill.

**Watch out:** Approach with the correct held item. A loot drop after defeating Elusive is a different mechanism.

Encounter reference: [Elusive](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Aelusive). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [ElusiveEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/boss/ElusiveEntity.java).

### Lunalus

![Lunalus Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-lunalus.webp)

**Where to plan:** Haven.

Select a Gravitator and move airborne over the void in Haven while carrying a Blank Realmstone in the main inventory.

- The item’s selected inventory tick must run; Creative is excluded.
- The check runs every five game ticks while airborne.
- The source checks for empty blocks below before consuming a blank.

**Watch out:** The inspected loop cumulatively subtracts its index from a mutable Y position, so it is not a straightforward every-block column scan. Use a genuine open-void location and a reliable return plan; exact trigger geometry still needs live testing.

Source checks: [Gravitator.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/item/misc/Gravitator.java).

### Runandor

![Runandor Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-runandor.webp)

**Where to plan:** Mysterium.

Place a Vox Light in Mysterium, drop a Blank Realmstone and one Runic Energy above it, then use an Active Rune Stone on the light.

- The two dropped item entities must intersect the one-block cube immediately above the light.
- The blank entity is converted to the Runandor Realmstone.
- The Active Rune Stone is consumed and the Runic Energy item entity is removed.

**Watch out:** Drop one Runic Energy, not a valuable stack: the source removes its entire item entity. Keep unrelated dropped items away; the loop can revisit a successful match because it does not break immediately afterward.

Source checks: [VoxLight.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/block/functional/light/VoxLight.java).

### Shyrelands

![Shyrelands Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-shyrelands.webp)

**Where to plan:** Late crafting route.

Craft Darkly Powder, Bloodstone, Glowstone, Haunted Flower, Magic Mending Solution and a Blank Realmstone together.

- Six exact ingredients, shapeless.
- Use the complete recipe from AoA 3.6.11.
- GUI parents point toward Greckon and Dustopia as progression hints.

**Watch out:** The ingredient’s item ID matters. The recipe explorer shows the exact versioned resources and images.

[Exact released crafting definition](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.16.5&q=shyrelands_realmstone).

### Nowhere

![Nowhere Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-realmstone-nowhere.webp)

**Where to plan:** Construct of Strength encounter, associated with Crystevia.

Carry a Blank Realmstone and survive an attack from a Construct of Strength that has Strength active.

- The inspected onAttack callback requires a player target with positive health.
- The construct itself must have the Strength effect.
- One blank is consumed and the Nowhere Realmstone is given.

**Watch out:** The released GUI still describes a crafting recipe involving a Shulker Box, Golden Apple, End Crystal and Beacon. No such bundled 3.6.11 recipe was found. The released Construct of Strength class contains the blank-to-Nowhere reward path; do not spend those crafting ingredients based on the stale hint.

Encounter reference: [Construct Of Strength](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.16.5&entity=aoa3%3Aconstruct_of_strength). Inspect its release-specific attributes, spawn evidence and loot before attempting the challenge.

Source checks: [ConstructOfStrengthEntity.java](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/content/entity/mob/crystevia/ConstructOfStrengthEntity.java).

## Troubleshooting

| Symptom | Check |
|---|---|
| Nothing happens after a kill | Correct creature, final damage type, player attribution, current effect and blank stone in the searched inventory |
| Wrong stone or no recipe | Exact Minecraft/AoA release; Nowhere’s released hint is stale in this inspected version |
| The GUI shows a parent dimension | It is a navigation hint; inspect the actual acquisition conditions rather than assuming a hard gate |
| A dropped-item interaction consumes too much | Use single-item drops for Runic Energy; source code removes the whole item entity |
| A realmstone is missing from the ground | Some routes give directly to the player; Primitive Carrotop instead drops its reward on death |
| A trigger works in source but not my pack | Check source/release drift, event cancellation, inventory wrappers, altered tags and other mod overrides; no live compatibility guarantee is made here |

## Evidence and limits

[Released GUI nodes, recipe hashes, source hashes and released class references](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/realmstone-progression-evidence-1.16.5.json) · [Structured walkthrough data](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/realmstone-route-guide-1.16.5.json).

The 22 destination routes include Nowhere’s source/class-supported encounter route, which is absent from the 22-node released GUI graph (that graph includes the Overworld root instead). Descriptions are original walkthrough notes, not a claim that every branch was executed in-game. Art uses independently rendered released items with upstream AoA credits retained.
