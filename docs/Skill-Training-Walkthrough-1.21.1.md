# Skill training: what earns XP, what blocks it, and what to unlock next

**Minecraft 1.21.1 · AoA 3.7.16.1.** The ten default skill JSON files were compared directly with this released JAR: all ten match the pinned source data semantically, covering **201 default ability records**. Training descriptions below follow the pinned implementation; class hashes and method bytes are retained for review. This is not a live XP-per-hour benchmark or a guarantee that another modpack has the same events, tags or configuration.

![Ten skill choices and verified default ability counts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/skill-training-overview-1.21.1.webp)

[All unlock levels and stored parameters](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Skill-Unlocks) · [Recipes and ingredients](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1) · [Creature field guide](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1)

## Before you start grinding

1. Use Survival when checking natural XP. The inspected natural-XP guard excludes Creative and Spectator.
2. Pick one visible milestone and check its actual ability data. Reaching a level does not supply the equipment or ingredients associated with the unlock.
3. Perform a small controlled activity, then inspect the skill again. Some gains are accumulated and posted later; Dexterity is a notable example.
4. Keep server settings and data packs in mind. Global XP modifiers, skill modifiers, cycle bonuses and events can alter the result.
5. Do not read a numeric “time” argument as an XP amount or a promise that the activity takes that long. The helper scales a level-dependent XP budget by a tick-based argument.

## Dexterity: movement, jumps and critical-hit events

**Practical loop:** sprint between useful destinations, jump where safe, and fight normally rather than standing still waiting for XP.

The source records horizontal distance while sprinting on the ground or swimming. Passenger movement is excluded. Individual recorded movements of one block or more are ignored by this path, so teleportation and very large per-tick displacement are not a reliable substitute for ordinary movement.

Jump events add to an XP accumulator; sprinting jumps multiply that contribution by 1.3. Critical-hit events add another contribution based on the event's damage multiplier. The accumulated result is posted on the player's **200-tick boundary**, so a single jump may not immediately update the displayed skill.

Useful early/default milestones include movement-speed modification at level 5, a fall-damage reduction record at 15 and jump boost at 25. The level-90 double-jump record consumes 20 Energy. These are ability records, not a claim that every bonus adds together linearly.

**If XP appears stuck:** wait through the accumulator boundary, stop riding a vehicle, and test ordinary ground sprinting away from coordinate-zero edge cases. The source uses zero-valued last-position sentinels; exact behavior near X=0 or Z=0 deserves a targeted test if you see an anomaly.

## Extraction: qualifying blocks and non-food smelting

**Practical loop:** mine useful materials with the right tool and collect non-food smelting results while checking the skill panel.

The block-loot path requires a block state, an origin, a full collision shape and membership in `aoa3:extraction_trainable`. The released tag references stone, cobblestone, ores, logs, sands, grass, dirt, gravel, netherrack and obsidian families, plus explicit Blackstone, Basalt and Ancient Debris entries. External tag membership can change with the pack; a tag name alone does not prove every similarly named block qualifies.

Base contribution depends on block hardness. The inspected logic doubles it if a generated item differs from the block's item, and multiplies it by 1.5 when more than two loot-list entries are generated. That last check counts **entries**, not the number of items in a single stack.

Non-food smelting has a separate path. Nugget, ingot and gem tags use different modifiers. The pinned source has the removed-item-count multiplier commented out with a NeoForge-related TODO, so do not promise that collecting a stack awards proportionally more XP than collecting one item from that event.

**Useful milestone:** level 25 has a harvest-speed boost with an Energy drain. Check the unlock table for the stored cost parameters before relying on sustained use.

## Farming: mature crops and player-caused breeding

**Practical loop:** maintain a renewable farm, harvest mature plants, replant, and breed animals as part of normal resource production.

For ordinary `CropBlock` plants, the source requires maximum age. Nether Wart must have age 3. Other blocks in the crops tag use a separate path, but stem blocks are excluded there. The player also has to pass the harvest check. Breaking immature wheat repeatedly is not the intended qualifying loop.

A player-caused baby-spawn event is another XP source. The value passed to the time-based helper is 600; that is not “600 raw XP.”

**If a modded crop does not train Farming:** inspect its block class, age properties and tag membership. A crop-looking texture is not enough to establish compatibility.

## Hauling: complete a fishing catch

**Practical loop:** fish in an appropriate area and finish actual catches rather than repeatedly casting without a result.

The inspected subscriber handles fishing-result events. Its contribution includes a Gaussian variation. AoA's specialized hauling event doubles the base contribution, and matching hauling-fish results can apply an additional modifier. The loop applies the fish modifier for each matching returned stack, so unusual modded multi-stack results need care when comparing XP.

**Do not assume a universal fixed XP per fish.** Your skill level, event subtype, result list and server modifiers all matter.

## Innervation: combat outcomes, not simply damage taken

**Practical loop:** choose enemies you can defeat reliably, use the bestiary to prepare, and aim for a repeatable combat-and-recovery loop.

The source tracks recent damage associated with targets and awards XP through its entity-kill path. Base calculation limits counted damage to 1.5 times the target's maximum health. Armour, toughness, movement and entity classifications can modify the reward.

Notable modifiers in the inspected implementation:
- AoA-marked spawner-born targets: ×0.25
- Flying or water-navigation targets: ×1.1
- Movement speed above 0.3: ×1.1
- Non-hostile targets: ×0.5
- Boss-tagged targets: ×1.3

These are calculation factors, not guarantees that a particular farm is fastest or that another mod uses AoA's spawner marker. Do not repeatedly take damage expecting this modern training implementation to behave like an older version.

## Imbuing: successful chamber output and Energy Stones

**Practical loop:** choose an Imbuing Chamber recipe you currently qualify for, provide its exact inputs, and complete the chamber operation. The recipe's XP method determines the award; the skill class being a thin wrapper does not mean the system has no XP sources.

The menu checks the recipe's Imbuing level requirement. A registered recipe does not automatically become usable at level 1. The output handling awards positive recipe XP through the player skill helper.

Energy Stones are a separate source. **Using one consumes the entire held stack outside Creative in the inspected implementation.** Split off the quantity you actually intend to spend first. The item calculates level-fraction XP across the stack, potentially accounting for level changes as it goes. Do not label this as one stone per click.

The 139 default Imbuing ability records include many restrictions/unlocks; their count is not 139 separate crafting systems.

## Faunamancy: a training hook exists, but the default ability list is empty

The released item tag contains `aoa3:faunamancers_blade`. The pinned training check requires a tagged tool in the player's main hand, nonzero event damage, very low target velocity (`lengthSqr < 0.01`) and a health/damage condition.

**Important implementation caveat:** the handler receives a post-damage event but evaluates `target.getHealth() - damage <= 0`. Without validating event timing in-game, do not simplify this into a certified “only killing blows” rule. The exact predicate is recorded for testing.

This skill has an event-driven XP path despite **zero default ability records** in the inspected release. That is different from proving a complete summon/companion progression system exists.

## Alchemy, Artifice and Creation: do not invent a grind

Each has zero default ability records in the released files, and the inspected Java skill classes are thin constructor wrappers. This evidence does not support a detailed working training loop or a full unlock tree for these three systems.

An add-on may extend them. Until a specific implementation or event hook is verified, report the gap rather than telling players to perform unproven repetitive actions.

## Cycling is a progression reset

The inspected cycle method requires level 100 or higher and fewer than ten cycles. It increments the cycle, then resets that skill to **level 1 and zero XP**. Future positive-cycle XP applies a factor of `3 × cycle count`, not `3` raised to the cycle count.

Do not cycle merely to inspect the menu. Review the loss of current level eligibility and the intended long-term benefit first. Global settings, skill modifiers, the Nowhere ×0.5 factor and event hooks can still change final XP.

## Troubleshooting checklist

| Symptom | First checks |
|---|---|
| No natural XP | Survival mode, correct event, skill below underlying level 1000, configuration and event cancellation |
| Dexterity updates late | Wait for the 200-tick accumulator boundary; avoid testing as a passenger |
| A crop gives nothing | Maturity, harvest permission, crop class/tag, stem exclusions |
| A block gives nothing | Full collision shape, extraction tag, valid block-loot context |
| Smelting a large stack does not multiply XP | The inspected removed-count multiplier is commented out; test the exact release instead of assuming |
| Energy Stones all disappear | The use handler consumes the full held stack outside Creative |
| A level unlock is unusable | Required recipe, item, resource cost and ability-specific conditions still apply |
| An empty skill page looks unfinished | Separate registration, XP hooks and default abilities; do not infer all three from one indicator |

## Sources and reproduction

- [Ten released skill files compared with pinned source](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/modern-skill-artifact-comparison.json)
- [Training class hashes, method bytes and released tags](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skill-training-evidence-1.21.1.json)
- [Pinned skill implementations](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16/source/player/skill)
- [XP helper and level budget](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/util/PlayerUtil.java)
- [Imbuing Chamber menu](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/menu/ImbuingChamberMenu.java)
- [Energy Stone stack consumption](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/EnergyStone.java)

The icons are released AoA GUI artwork arranged into an original documentation overview; credit remains with Tslat and contributors. This page documents systems and known test targets, not a completed Enderloom gameplay or performance certification.
