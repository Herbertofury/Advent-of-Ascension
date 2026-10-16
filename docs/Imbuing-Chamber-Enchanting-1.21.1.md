# Imbuing Chamber enchanting · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** Choose a specific enchantment recipe, supply its Power Stone and Aspect Foci, then insert compatible equipment. The inspected release contains **135 imbuing recipe definitions**.

**Check the recipe before inserting valuable gear.** The valid target can be imbued as the chamber updates. The right-hand slot is not merely an uncommitted output preview waiting for you to take it.

[Infusion Table preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-1.21.1) · [Skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) · [Recipe Observatory](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1)

## 1. Build the chamber

![Seven copper-tag ingredients, an Infusion Table and an energy-stone-tag ingredient make the Imbuing Chamber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/imbuing-chamber-recipe-1.21.1.webp)

At a crafting table:

| Copper-ingot tag item | Copper-ingot tag item | Copper-ingot tag item |
|---|---|---|
| Copper-ingot tag item | Infusion Table | Copper-ingot tag item |
| Copper-ingot tag item | Energy-stone tag item | Copper-ingot tag item |

Total: **7 items matching `c:ingots/copper`, 1 Infusion Table and 1 item matching `aoa3:energy_stone`**. The shipped energy-stone tag lists Ambient, Glistening, Blooming, Shining, Gleaming, Glowing, Glaring and Radiant Energy Stones. Pack tags can change accepted inputs.

### Energy Stones and Power Stones are different

- **Energy Stone:** used by the chamber's construction recipe and by the skill-training use action.
- **Power Stone:** the specific reagent named by an enchanting recipe.

Do not put an Ambient Energy Stone into an enchanting recipe requiring an Ambient Power Stone merely because their names sound alike. A higher-tier Power Stone is not an automatic substitute either: follow the recipe's exact `power_source`.

**Energy Stone precaution:** the inspected training use action spends the **entire held stack** outside Creative. Split off the amount you intend to spend, and keep the stone needed for crafting separate. See the [training guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) before using a full stack.

## 2. Prepare the required stones and foci

Pixons are a source route for these materials. In the pinned implementation, a nearby player **actively using an Attuning Bowl** can receive the Pixon variant's loot. Simply owning a bowl is not the same as using it. The harvest is probabilistic, so do not expect a stone on every tick.

For example, the released Ambient Pixon stone table contains Ambient Energy Stone and Ambient Power Stone entries. Those are separate outcomes, not a guaranteed pair. This section describes a harvesting route once you have found a Pixon; it does not claim a guaranteed spawn location or waiting time.

Use the selected-release recipes to make the required Aspect Foci. The chamber has five focus slots, but the 135 bundled recipes inspected here use **two, three or four foci**. Unused focus slots should remain empty. Extra foci do not act as a free bonus.

## 3. Read the layout correctly

![Efficiency I example with Ambient Power Stone, Speed, Precision and Control foci, and a compatible target tool](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/imbuing-slot-layout-1.21.1.webp)

The menu has **six reagent inputs plus a separate target position**:

| Position | What belongs there |
|---|---|
| Left slot, index 0 | Recipe's Power Stone |
| Five middle slots, indices 1–5 | Recipe's Aspect Foci |
| Right-hand slot, index 6 | Compatible equipment to enchant |

The five middle slots accept Aspect Focus items. The recipe matcher treats the required foci as ingredients without a positional pattern, but still checks the exact occupied ingredient count. Keep unused slots empty and do not combine repeated entries into one occupied slot.

## 4. Example: Efficiency I

The released Efficiency I recipe requires:

- **AoA Imbuing level 5**
- **Ambient Power Stone** in the left slot
- **Speed Focus, Precision Focus and Control Focus**, one per middle slot
- A compatible mining tool in the right-hand target slot

Load the reagents, verify the intended recipe and your skill level, then insert an expendable compatible tool for your first test. After the operation, inspect the enchantment, the remaining stone count and focus durability before using valuable equipment.

This level requirement is the **AoA Imbuing skill level**, not the green vanilla experience-bar level. Recipe matching and skill eligibility are separate checks. A displayed combination of items does not establish that you meet the server-side requirement.

## Useful recipe examples

| Enchantment | AoA Imbuing level | Power Stone | Aspect Foci |
|---|---:|---|---|
| Efficiency I | 5 | Ambient | Speed, Precision, Control |
| Protection I | 8 | Ambient | Durability, Life |
| Sharpness I | 9 | Ambient | Damage, Precision |
| Unbreaking I | 30 | Blooming | Durability, Resource |
| Unbreaking II | 41 | Shining | Durability, Resource |
| Unbreaking III | 59 | Gleaming | Durability, Resource |

These are six checked examples from the 135 definitions. Higher enchantment tiers can require a different Power Stone and skill level even when their focus combination stays the same. Search the [recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=imbuing) for the exact tier.

## 5. Know what can be enchanted

The checked recipe logic rejects:

- An ordinary **Book**
- An item the target enchantment cannot apply to
- An item already holding that enchantment at the recipe's level or higher
- An item with an incompatible existing enchantment

A lower level of the same enchantment can be upgraded when the target otherwise qualifies. This is not a promise to force incompatible combinations onto any item or to ignore other mods' enchanting rules.

The assembly method **copies the target item and applies the requested enchantment**. That differs from the generic Infusion Table's recipe-defined output. The checked imbuing code therefore starts from the equipment's existing stack data rather than constructing a different base item. Test custom component-heavy equipment before relying on this as full compatibility certification.

## 6. Understand costs and when they apply

The imbuing result-slot `set` path performs its award/consumption work when the menu's imbuing flag is set. Its `onTake` path does not perform that same operation again. Treat insertion of a valid target into a prepared chamber as potentially committing the operation; removing the item afterward is not an undo action.

For the normal checked recipe path:

- One Power Stone is consumed, subject to standard crafting-remainder handling if a changed item supplies one.
- Each used focus gains one damage point and is returned until it reaches its maximum damage, when it breaks.
- The Durability Focus is constructed with **20 durability**.
- The other **11 focus types are constructed with 10 durability** each.
- Successful recipe handling can award **AoA Imbuing XP**, with recipe-specific/default calculation. Do not treat this as a fixed vanilla-XP reward.

These are stock class/resource findings. Creative behavior, custom remainders, altered durability components, event cancellation and automation still need separate runtime checks.

## Troubleshooting

| Problem | Check first |
|---|---|
| Chamber recipe does not craft | Seven copper-tag entries, Infusion Table at center, Energy Stone at bottom center |
| Enchanting setup does nothing | Power Stone rather than Energy Stone; exact recipe tier |
| Gear cannot enter the right slot | A matching recipe, target applicability, conflicts and existing enchantment level |
| You have enough vanilla XP but cannot use the recipe | Check AoA Imbuing skill level |
| Extra focus seems to prevent the recipe | Remove unused foci; exact ingredient count matters |
| A focus disappears | Check whether its durability reached the limit |
| Stone count changed before taking gear out | Valid insertion/update can commit imbuing immediately |
| Energy Stone stack vanished after use | Training use spends the whole held stack outside Creative |
| Recipe explorer has no fixed output item picture | Imbuing defines an enchantment applied to your target, not a universal output item |

## Evidence and limits

[Imbuing workstation evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/imbuing-workstation-evidence-1.21.1.json) records the 135 released recipe definitions, chamber recipe, energy-stone tag, Ambient Pixon table, selected method bodies and exact focus-durability constructor shapes. Source interpretation is pinned to [7919b5fe48599e6105c5740937ce36c36ef21d16](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16).

The diagrams use release-matched model references, representative tag ingredients and a representative compatible tool without simulated enchantment glint. They are not in-game screenshots. This guide does not certify live imbuing, every survival acquisition route, automation or the private Enderloom build. AoA artwork and systems are by Tslat and contributors; vanilla references are by Mojang/Microsoft.
