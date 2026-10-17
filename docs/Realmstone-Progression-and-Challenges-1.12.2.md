[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [First portal and Precasia](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2) · [Dimensions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions)

# Historical realmstone progression: all 23 destination stones

> Minecraft 1.12.2 / AoA 3.3.6. This guide distinguishes shipped challenge hints from selected released trigger checks. Static acquisition evidence does not certify a safe journey, a completed modern port or every modpack interaction.

![Twenty-three historical realmstone source-model icons](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-destination-catalog-1.12.2.webp)

## Prepare before attempting a challenge

Start with the [historical first-portal walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/First-Portal-and-Precasia-1.12.2): Traveller food exchange, Worn Book, Blank Realmstone, exact frame and the sapling-based Precasia recipe are already illustrated there.

Carry a Blank Realmstone for the routes that use the inventory helper. Keep inventory space and a return plan. Challenges involving lava, a Creeper, a Wither, a large fall or hostile mobs can kill your character; prepare gear, health, escape space and a test-world copy before experimenting.

The helper used by many routes searches the inspected player inventory paths and normally consumes one matching blank. Creative behavior differs: its selected findInventoryItem implementation returns true for a Creative player before requiring a match. Direct held-item replacement, dropped-item conversion and Gravitator main-inventory scanning are separate paths and should not be assumed to share that behavior.

## Illustrated destination index

Each name links to the exact historical inventory reference. The notes describe the selected trigger, not a guaranteed spawn location for every prerequisite.

| Stone | Destination item | Checked acquisition action | Important distinction |
|---|---|---|---|
| ![Abyss Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-abyss_realmstone.webp) | [Abyss Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AbyssRealmstone.name) | Be near a Wither joining the world in dimension -1, with a Blank Realmstone. | The callback checks players in the Wither bounding box expanded by 50; it does not identify only the player who built the Wither. |
| ![Ancient Cavern Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-ancient_cavern_realmstone.webp) | [Ancient Cavern Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AncientCavernRealmstone.name) | Complete the checked five-different-Construct task within its retained 600-tick window. | Use the Ancient Cavern guide for eligible classes, timing boundaries and capability persistence. |
| ![Barathos Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-barathos_realmstone.webp) | [Barathos Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BarathosRealmstone.name) | Use the Blank Realmstone as the item hit that leaves a Husk at health ≤0. | The server item-hit callback replaces the player’s main-hand item with the result; it is not any Husk kill while merely carrying a blank. |
| ![Borean Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-borean_realmstone.webp) | [Borean Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreanRealmstone.name) | Let one of the ten checked Gardencia classes touch Candied Water, then kill it with player true-source credit while carrying a blank. | The retained flag is set by contact, not a timed soak. The historical item ID uses borean_realmstone. |
| ![Candyland Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-candyland_realmstone.webp) | [Candyland Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandylandRealmstone.name) | Eat a Heart Fruit in Precasia with a blank and remain above zero health after its self-harm request. | The method requests 7 self-harm damage before checking the reward. Prepare health and recovery. |
| ![Celeve Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-celeve_realmstone.webp) | [Celeve Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CeleveRealmstone.name) | Get player true-source kill credit on a Clown while holding the Lelyetian Greatblade in the main hand and carrying a blank. | The selected callback checks the held item at death; it does not itself require a melee-damage classification. |
| ![Creeponia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-creeponia_realmstone.webp) | [Creeponia Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CreeponiaRealmstone.name) | Take an eligible Creeper explosion hurt event with primed TNT near the player or Creeper and a blank available. | The TNT query expands either bounding box by 3. Positive health is checked in the hurt callback, not a certified post-damage survival result. |
| ![Crystevia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-crystevia_realmstone.webp) | [Crystevia Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrysteviaRealmstone.name) | Interact with a Case Construct while holding the Deep Crystal block item and carrying a blank. | The selected method consumes the blank through the helper; it does not shrink the held Deep Crystal. |
| ![Deeplands Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-deeplands_realmstone.webp) | [Deeplands Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DeeplandsRealmstone.name) | Harvest an accepted ore block at Y≤5 with a blank available. | The helper accepts BlockOre or BlockRedstoneOre classes; a modded ore tag or name alone is insufficient. |
| ![Dustopia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-dustopia_realmstone.webp) | [Dustopia Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DustopiaRealmstone.name) | Trigger the Shadow Altar activation while Night Vision is active and a blank is available. | The reward check accompanies a scheduled ritual; it is not proof of a successful boss spawn or kill. |
| ![Gardencia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-gardencia_realmstone.webp) | [Gardencia Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GardenciaRealmstone.name) | Drop a blank into a fully grown carrot crop in Precasia, then defeat the spawned Primitive Carrotop there. | The item-update path removes the dropped blank and crop after the spawn call; the creature’s death drops the realmstone without requiring another blank. |
| ![Greckon Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-greckon_realmstone.webp) | [Greckon Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GreckonRealmstone.name) | Use Nightmare Flakes on Elusive with a blank available. | The inspected method consumes the blank through the helper and shrinks one Flakes item; it lacks its own explicit side guard. |
| ![Haven Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-haven_realmstone.webp) | [Haven Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HavenRealmstone.name) | Kill a Flye with eligible melee damage and player true-source credit while the player is at Y≥80, carrying a blank. | The height check uses the player’s position; do not substitute the Flye’s Y coordinate. |
| ![Immortallis Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-immortallis_realmstone.webp) | [Immortallis Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ImmortallisRealmstone.name) | Receive a successful hit from a Strength-buffed Construct of Strength, remain above zero health and have a blank available. | Follow the dedicated Immortallis walkthrough for dungeon preparation and recovery. |
| ![Iromine Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-iromine_realmstone.webp) | [Iromine Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IromineRealmstone.name) | Use a held Blank Realmstone on a Mineralization Station. | The selected server handler switches on the held item’s translation-key suffix and replaces the held stack with Iromine’s stone. |
| ![Lelyetia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-lelyetia_realmstone.webp) | [Lelyetia Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LelyetiaRealmstone.name) | Trigger a player fall event with distance >25 and damage multiplier >0 while a blank is available. | The reward check runs before later player-data/Expedition fall handling. It does not certify surviving the final damage. |
| ![Lunalus Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-lunalus_realmstone.webp) | [Lunalus Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunalusRealmstone.name) | Hold the selected Gravitator while airborne in Haven, outside Creative, with a blank in main inventory at a five-tick world-time boundary. | Its downward air-test loop mutates the sampled position cumulatively; see the implementation warning below. |
| ![Mysterium Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-mysterium_realmstone.webp) | [Mysterium Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MysteriumRealmstone.name) | Cause a successful poison-classified damage event on a Creepird with its attackingPlayer reference set to a player carrying a blank. | Poison classification checks magic damage, no true source, not thorns, active Poison and exactly 1.0 damage. |
| ![Nether Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-nether_realmstone.webp) | [Nether Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NetherRealmstone.name) | Toss a Blank Realmstone when the dropped item entity is detected in lava by the toss callback. | This is an immediate event-time check, not a general later lava-immersion conversion. See the timing warning below. |
| ![Precasia Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-precasia_realmstone.webp) | [Precasia Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrecasiaRealmstone.name) | Shapeless: Blank Realmstone plus one each of all six vanilla sapling metadata variants 0–5. | Use the illustrated first-portal guide; this is not the modern archaeology route. |
| ![Runandor Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-runandor_realmstone.webp) | [Runandor Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunandorRealmstone.name) | Place a dropped blank and Runic Energy above a Vox Light in Mysterium, then use an Active Rune Stone. | Use exactly the required dropped entities and keep spare stacks away. The loop and whole-stack consumption warning below matters. |
| ![Shyrelands Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-shyrelands_realmstone.webp) | [Shyrelands Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShyrelandsRealmstone.name) | Shapeless: blank, Darkly Powder, Bloodstone, Glowstone block, Haunted Flower and Magic Mending Solution. | The recipe uses minecraft:glowstone, not Glowstone Dust; these exact items are not automatically replaceable by modded equivalents. |
| ![Vox Ponds Realmstone](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/realmstone-1.12.2-vox_ponds_realmstone.webp) | [Vox Ponds Realmstone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoxPondsRealmstone.name) | Interact with an AoATrader in Creeponia using a blank while environmentally protected. | The helper accepts a full Hazmat set or Face Mask, with an additional IC2 compatibility route if active. |

## The two shipped crafting recipes

Only two realmstone-output recipes were found in the inspected shipped recipe resources: Precasia and Shyrelands. Other stones in this guide use code-side challenges, not invented crafting grids.

- [Precasia Realmstone · exact illustrated recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Frealmstone%2Fprecasia_realmstone)
- [Shyrelands Realmstone · exact illustrated recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Frealmstone%2Fshyrelands_realmstone)

## Useful progression connections

These are prerequisite connections visible in the inspected actions, not an assertion that every possible route follows one mandatory order:

- **Precasia → Candyland / Gardencia:** Heart Fruit consumption or the mature-carrot ritual.
- **Deeplands → Crystevia → Ancient Cavern / Immortallis:** Case Construct interaction, then the distinct Construct challenges.
- **Lelyetia → Haven → Lunalus:** high-altitude Flye melee kill, then the Gravitator challenge.
- **Creeponia → Vox Ponds / Mysterium:** protected trader interaction or the Creepird poison route.
- **Mysterium + Vox Light / Runic Energy / Active Rune Stone → Runandor.**

Where a trigger does not itself enforce a dimension, the normal location of its prerequisite can still constrain survival acquisition. Read creature spawn evidence and station acquisition separately.

## Gardencia and Borean: two different transformations

For Gardencia, the dropped Blank Realmstone checks its own block position in Precasia for a fully grown vanilla carrot crop. It attempts to spawn a Primitive Carrotop, kills the item entity and removes that crop. It does not check the spawn boolean before removing those inputs in the selected method. Test cancelled/failed spawns with expendable inputs.

The Primitive Carrotop death callback drops Gardencia’s stone when it dies server-side in Precasia. That callback does not require player kill credit or a second blank. Moving the creature to another dimension changes this selected condition.

For Borean, the ten checked classes are Archvine, Broccohead, Carrotop, Corny, Daysee, Flowerface, Pod Plant, Squasher, Sunny and Vine Wizard. Their Candied Water contact path sets a retained flag and applies its first-contact health behavior. There is no required soak-duration counter in those selected contact methods.

Their death callback then requires the retained flag, server side, player true-source credit and a blank through the inventory helper. This is not every arbitrary Gardencia-looking mob. Their NBT reader tests presence of the AoACandiedWater key; persistence and attribute reapplication remain runtime checks.

## Runandor: isolate the two dropped inputs

The Vox Light looks for item entities inside the one-block footprint above it, from Y+1 to Y+2. The player must hold an Active Rune Stone and be in Mysterium. The scan needs more than one item entity, then remembers a blank entity and a Runic Energy entity.

When both references have been found, it shrinks the held Active Rune Stone by one, replaces the blank entity’s item with a Runandor Realmstone and kills the Runic Energy entity. Killing that entity can consume its entire dropped stack, not just one energy item.

The conversion block is inside the item-list loop with no break after success. Additional entities after both references are found can repeat the consumption/conversion calls. Creative does not add an exemption in that selected block. For a controlled attempt, use only one blank entity and one single-item Runic Energy entity in the query box, keep spare items outside it, and test rollback/cancellation separately.

## Lunalus: the air probe is not a simple vertical scan

The Gravitator path requires a selected item, an airborne non-Creative player in Haven, world time divisible by five and a blank in main inventory. Its loop starts at the holder’s block position, then repeatedly subtracts the growing loop index from the already-mutated Y value.

For an integer starting Y of 100, the first sampled heights are **100, 99, 97, 94, 90, 85…**, rather than 100, 99, 98, 97… . The all-air path can continue far below the starting column’s ordinary bottom. The method returns at the first sampled non-air block.

This is a code-derived implementation warning. Do not promise that it checks every block directly beneath the player, or encourage an unsafe void jump based on a simplified hint. The supplied arithmetic models preserve the actual cumulative update; target-build behavior near world bounds must be tested.

## Timing and attribution pitfalls

- **Nether:** the toss callback checks the dropped entity’s lava state at that event. It does not register a general conversion when a previously tossed blank later falls into lava, and the selected branch does not itself remove the tossed entity after awarding the result.
- **Creeponia / Lelyetia:** reward checks occur in hurt/fall handling. A positive-health or positive-multiplier check at that point is not a guarantee the character survives later damage.
- **Abyss:** Wither world-entry, Nether dimension -1 and nearby player inventories are the selected trigger. It does not inspect a summoner identity.
- **Celeve:** the player’s main-hand Greatblade is checked at Clown death. The selected callback does not require the damage itself to be classified as melee.
- **Mysterium:** an active Poison effect alone is not sufficient. The damage helper additionally requires magic damage, no true source, not thorns and exactly 1.0 damage; the Creepird’s attackingPlayer reference must resolve.
- **Greckon:** the Nightmare Flakes interaction lacks an explicit server-only guard of its own. Test client/server consumption and inventory delivery before treating it as duplication-safe.
- **Vox Ponds:** full Hazmat armor is not the only inspected protection route; Face Mask and the conditional IC2 helper also qualify.

## Dedicated dungeon and ritual guides

[Ancient Cavern and deity shrines](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2) covers the five-class timing task and subsequent progression. [Immortallis](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Immortallis-Dungeon-Walkthrough-1.12.2) covers the dungeon stages and recovery. [Historical altars](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Altars-and-Summon-Preparation-1.12.2) explains ritual inputs and delayed-spawn limitations, including Shadow Altar context.

## Evidence and restoration checks

[Released route methods, registration windows and recipes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/realmstone-route-evidence-1.12.2.json) · [Readable route catalog](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/realmstone-route-catalog-1.12.2.json) · [Icon provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/realmstone-route-art-evidence-1.12.2.json)

75 selected methods, 23 exact Realmstone registration windows, two complete recipe resources and 24 localized hints are retained. Hints are compared with actual predicates rather than treated as sufficient evidence. Java and Minecraft code were not executed.

Test full inventory delivery, Creative versus survival, both hands, single-item versus stacked drops, cancelled events/spawns, multiplayer attribution, capability/NBT persistence, and server-configured dimension IDs. A successful challenge should preserve unrelated inventory and save data.

AoA assets and systems: Tslat and contributors. [Pinned source context](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
