# Nowhere boss rewards and multiplayer scaling · 1.21.1

**Minecraft 1.21.1 · AoA 3.7.16.1.** Before a group boss fight, make inventory room and check the server’s reward policy. More players do not necessarily mean one copy of every reward per player.

![Illustrated quantity quota and copied-stack inventory limitation](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/boss-loot-quota-and-capacity-1.21.1.webp)

## Where these rules apply

The inspected event registration routes living-drop events in **Nowhere** to this handler. The handler cancels drops for a non-AoABoss or an already-canceled event; otherwise it delegates to the configured boss distribution scheme. This page does not apply that policy to every mob in every dimension.

The server-config key is **general_settings.bossDropsScheme**. The released default is **SPLIT_BETWEEN_PLAYERS**. Other server hooks and modpack changes can alter the final result.

## The four reward modes

| Config value | Inspected selection behavior | What not to assume |
|---|---|---|
| ON_GROUND | This distributor leaves the event drops alone | It does not promise private ownership or protection from other pickup behavior |
| LAST_PLAYER_TO_HIT | Walks combat entries backward for a Player; if entries are empty, tries the damage-source player/owner helper | It is not a full custom damage-ranking calculation |
| MOST_DAMAGING_PLAYER | Uses the entity’s getKillCredit result, with a damage-source player/owner fallback if credit is null | The mode itself does not sum a permanent all-fight damage ledger |
| SPLIT_BETWEEN_PLAYERS | Collects distinct eligible player attackers/owners, then apportions item counts | Equal quantity is not equal rarity, value or one of every drop |

A mode’s name is not a substitute for its implementation. Combat history, attribution and other hooks matter.

## How split mode works

1. Collect attackers from the entity’s combat history. When that history is empty, the helper can use the last damage source.
2. Resolve players or applicable owners and deduplicate them into a set. Merely standing nearby is not the eligibility rule used by this distributor.
3. If no eligible player is found, the handler cancels the drop event. If exactly one is found, it uses the direct inventory-giving helper.
4. For multiple players, gather nonempty drop stacks, shuffle their order and clear the original event collection.
5. Count **item units** across stacks. Compute **max(1, floor(total units / eligible players))** as the per-player quota.
6. Randomly select a remaining stack and an amount that fits the player’s remaining quota. Try to insert it into that player’s inventory.
7. Remove a player from the allocation set when the quota is reached or an insertion fails. Remaining retained stacks are returned as ground ItemEntities near the boss.

The set iteration is not a documented fair turn order. The code does not balance item rarity or monetary value. With ten item units and three players who all have sufficient capacity, the quota is three per player and one unit remains for the ground. With fewer units than players, some players can receive none.

The 84 quota examples in the evidence are bounded arithmetic checks, not simulations of every random draw or external inventory implementation.

## Inventory-space precaution

**Make room before the boss dies.** The inspected partial-stack path has a concrete item-accounting risk:

- It copies a chosen part of a stack and immediately subtracts that amount from the retained original stack.
- It then tries to add the copy to the player’s inventory.
- If insertion returns false, that branch removes the player from allocation and continues without reattaching or dropping the copy’s remainder.

For example, selecting three units from a ten-unit stack leaves seven in the original. If the inventory accepts one and the copied remainder contains two, only eight units remain accounted for by this branch. The two-unit remainder is not returned to the retained drop list there.

The vanilla 1.21.1 Inventory.add comparison was inspected: an undamaged stack can be partly inserted, then return false when the retry makes no further progress. This is why “false” must not be treated as “the stack was untouched.” Creative behavior, damaged items and modified inventory hooks need separate tests.

The supplied model checks 800 bounded copied-stack cases, including 680 cases with a nonzero detached remainder. **This is a static source-branch finding, not proof of an observed loss in the user’s private Enderloom build.** Whole-stack and single-recipient paths retain different object references and must be tested separately rather than lumped together.

## Multiplayer boss health

The server key **general_settings.multiplayerBossHealthBonus** defaults to **25**, interpreted as a percentage per extra player by the inspected BossTokenItem helper. Its configured range is 0–1000.

The helper does nothing if the boss is null, playerCount is below two, or the configured bonus is zero. Otherwise it applies a permanent MAX_HEALTH modifier with operation ADD_MULTIPLIED_TOTAL and amount:

**bonus / 100 × max(1, playerCount − 1)**

It then sets current health to the resulting maximum.

| Player count passed to the helper | Default added multiplier | Simple isolated factor |
|---:|---:|---:|
| 1 | 0 | 1.00× |
| 2 | 0.25 | 1.25× |
| 3 | 0.50 | 1.50× |
| 4 | 0.75 | 1.75× |
| 5 | 1.00 | 2.00× |

The last column is an isolated explanation, not a final-health guarantee with other attribute modifiers. The playerCount supplied at spawning and the eventual loot-eligible attacker set are separate inputs; do not assume their sizes always match. There are 32 bounded health-helper cases in the evidence.

## Group-fight checklist

- Agree on the server’s loot scheme before spending entry materials.
- Leave free slots and useful partial-stack capacity before entering.
- Make sure intended recipients actually participate; proximity alone is not this code’s eligibility check.
- Check retained ground drops after distribution instead of assuming everything went directly to inventories.
- Use the selected boss’s [bestiary and drop references](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1) for what it can drop. This distributor changes allocation, not the underlying loot table into a guaranteed reward list.
- Follow [boss entry and token preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) for access requirements.

## Restoration acceptance checklist

- [ ] Preserve total item count and components through successful, partial and failed inventory insertion.
- [ ] Reattach or safely drop every uninserted copied remainder before leaving the branch.
- [ ] Test no eligible player, one player, several players, offline/dead recipients and owner-attributed damage.
- [ ] Verify remainder handling when total units are smaller than the player count or not evenly divisible.
- [ ] Verify reward messages per recipient instead of trusting a shared accumulator.
- [ ] Test all four modes under the target modpack’s inventory and loot hooks.
- [ ] Compute distribution once per reward event; do not add recurring world or full-inventory scans to every tick.

These are proposed correctness/performance checks, not already-implemented fixes or multiplayer certification.

## Evidence

- [Released distributor methods, two config windows, vanilla inventory comparison and bounded models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/boss-reward-distribution-evidence-1.21.1.json)
- [Illustration receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/boss-reward-art-evidence-1.21.1.json)
- [Pinned original distribution implementation](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/library/constant/BossDropsScheme.java)

Static archive inspection and original documentation models only. No game, mod or server code was executed.
