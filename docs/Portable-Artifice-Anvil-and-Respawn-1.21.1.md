# Portable artifice: Temporal Anvil and Anchoring Crystal

**Minecraft 1.21.1 · AoA 3.7.16.1.** These two tools have registered source implementations, but the inspected shipped data does not establish their acquisition route. This guide explains what their code does and what still needs testing; it does not invent a crafting recipe.

![Temporal Anvil and Anchoring Crystal utility-flow comparison](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/portable-artifice-overview-1.21.1.webp)

## Find the right reference

| Tool | Item reference | Source-observed purpose |
|---|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/portable-artifice-temporal_anvil.webp" width="64" height="64" alt="Temporal Anvil source-model item"> Temporal Anvil | [Exact item card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:temporal_anvil) | Opens an ordinary AnvilMenu from item use |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/portable-artifice-anchoring_crystal.webp" width="64" height="64" alt="Anchoring Crystal source-model item"> Anchoring Crystal | [Exact item card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:anchoring_crystal) | Starts a delayed, same-dimension saved-spawn teleport workflow |

Both are declared in AoAArtificeDevices, which is included in the source item-registry initialization. The scan checked 3,929 shipped data JSON resources and found no literal references to either item ID. That is a bounded resource finding, not proof that code-side rewards, trades, commands or a modpack cannot supply them.

## Temporal Anvil: what opens and what does not change

1. Use the item. On the server, its override asks the player to open a menu.
2. The menu is the ordinary Minecraft AnvilMenu, using the player inventory.
3. Taking an output calls the inherited onTake behavior first, then plays a customized anvil-use sound for that player.

This subclass does not replace the XP calculation with a free-repair rule. Do not assume its name means time reversal, unlimited free enchanting or removal of normal anvil restrictions. The inspected custom behavior is the portable menu request and output-take sound; loader and other mod changes remain separate.

The tool is configured to stack to one. This use override does not shrink or damage the held tool. Actual input consumption, XP costs, invalid combinations, closing the menu, reconnecting and interaction with other inventory mods still need a target-build test.

For a distinct material-repair workstation, compare the [Mending Table guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1). It is a different system and should not inherit assumptions from this anvil menu.

## Anchoring Crystal: check the destination before charging

The server-side start checks reject use when:

- the player is dead or dying;
- the current world is Nowhere;
- no saved respawn position is set;
- the saved respawn dimension is different from the current world.

When those gates pass, the item begins a **100-tick use**. At the nominal 20 ticks per second that corresponds to five seconds, but lag and interrupted item use can change the experience. The code uses the NONE use-animation value; particles are requested while the use progresses.

This is not an unrestricted cross-dimensional escape tool. A bed saved in the Overworld does not satisfy the server's same-dimension gate while you are in Precasia or the Nether. Confirm the world's bed/anchor rules before attempting to set a spawn point; this guide does not guarantee safe placement or a valid arrival location.

## Completion checks are separate from start checks

At completion, the implementation requires a ServerPlayer and a saved respawn dimension matching the current dimension. It asks the respawn-position helper for a transition, then passes that transition through the NeoForge respawn-position event.

It teleports only when the resulting transition's destination level is the same level passed into the completion callback. A changed or invalid spawn point, a fallback destination or another mod's event result can therefore change the outcome. Passing the start checks is not a guarantee of landing at the exact original bed coordinates.

| Example | What the inspected gates establish |
|---|---|
| No saved respawn position | Server start rejects use |
| Saved spawn in a different dimension | Server start rejects use |
| In Nowhere | Start rejects use |
| Valid start, but final transition targets another level | The completion teleport branch is not taken |
| Matching respawn dimension and same-level final transition | The completion teleport branch is eligible; arrival safety remains separate |

The method returns the same item stack and contains no item-consumption call. That does not certify every patched/modded behavior or convert this into a death/respawn transaction.

## Does it consume a Respawn Anchor charge?

The AoA call passes **true** to findRespawnPositionAndUseSpawnBlock. In the inspected unmodified Minecraft 1.21.1 helper, that argument reaches the boolean tested before the anchor-charge decrement. When it is true, that decrement branch is skipped.

This supports a scoped vanilla-helper expectation, not an unconditional guarantee for a NeoForge-patched installation or event-modified world. Anchor validity, the available standing position, forced respawn state and dimension rules are still involved. Test with an expendable charged anchor in a copied world before relying on this behavior.

The vanilla helper also contains an Overworld fallback when the saved spawn cannot be resolved. The crystal's later same-level check matters: a fallback to another level is rejected by its teleport branch, while a same-level fallback may still be used. Do not describe every missing-bed case as either a guaranteed failure or an exact-bed return.

## Why Unbreaking and Mending are rejected

Both items inherit ArtificeItem. Its enchantment-support override rejects enchantments in aoa3:artifice_tool_incompatible before delegating to the normal item check. The inspected tag contains **Unbreaking** and **Mending**.

That is not permission for every other enchantment: the ordinary item compatibility check still has to pass. Datapacks can change tag contents.

## Restoration and acceptance checklist

- Establish an actual acquisition route before advertising these as craftable survival rewards.
- Test ordinary anvil inputs, costs and output taking, including full inventory and disconnect cases.
- Test the crystal with a valid point, no point, a point in another dimension, Nowhere and an invalidated point.
- Test a respawn-event override that changes the destination level.
- Verify anchor-charge behavior against the actual loader build and active mods.
- Check particle load with repeated/multiplayer use; this analysis makes no measured FPS or zero-cost claim.

[Five AoA class selections, two vanilla helper methods and 48 isolated branch cases](https://herbertofury.github.io/Advent-of-Ascension/portable-artifice-evidence-1.21.1.json) · [Image evidence](https://herbertofury.github.io/Advent-of-Ascension/portable-artifice-art-evidence-1.21.1.json) · [Movement and void-recovery tools](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Movement-and-Void-Recovery-Utilities-1.21.1)

AoA item artwork: Tslat and contributors. The vanilla helper reference comes from the official unmodified Minecraft 1.21.1 distribution and mappings, not a certified NeoForge runtime. No Java/game code, menu transaction or teleport was executed.
