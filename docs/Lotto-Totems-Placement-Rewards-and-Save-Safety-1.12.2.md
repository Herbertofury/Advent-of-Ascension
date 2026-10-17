# Lotto Totems: placement, rewards and save safety · 1.12.2

**Minecraft 1.12.2 · AoA 3.3.6.** One Lotto Totem item requests five choices, with one winning index selected when placed. This guide covers the exact layout, the thirteen-entry reward table, owner checks and a released save-callback problem.

![Five-choice placement schematic and source model](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-five-choice-layout-1.12.2.webp)

## Prepare and choose

1. **Prepare a clear 3×3 area.** The clicked center pad and four diagonal pads need solid upper faces. The helper checks replaceable material above each diagonal pad. Clear space above all five as a practical precaution; the local helper does not explicitly check the center’s headroom.
2. Use the item on the **upper face** of the center block. Side faces and a non-solid upper face fail the local gate. A nearby Lotto Totem in the clicked-block box expanded by 4 blocks prevents placement; this is a box test, not a spherical radius.
3. On the server, passing the layout check shrinks the held-hand stack by one, chooses a winner index with nextInt(5), and attempts to spawn five linked totems. The spawn return values are ignored, so protection hooks or other spawn rejection can matter after the item has been consumed.
4. Choose one of the totems as its owner. The reward callback checks the owner UUID, or allows interaction when that field is null. Picking the winning UUID requests loot; choosing another does not.
5. The accepted interaction then removes nearby Lotto Totem entities in a box expanded by 2 around the selected totem. Do not expect to try all five sequentially as independent attempts.
6. **Resolve the placed group before relying on save/reload in an unverified restoration.** The released custom read/write callbacks are reversed; see the persistence warning below.

Numbers in the diagram show source iteration order, not a better winning position. The source chooses one of five indices uniformly. The 20% one-choice model assumes all five intended entities exist and the normal selection/cleanup path is used; it is not a promise under spawn cancellation, modified code or broken persistence.

## What a winning choice requests

The callback asks LootUtil for the Lotto Totem table with **custom luck 5**, then separately requests one Lotto Banner. The shipped table contains **one pool, one roll and thirteen weighted item entries**, with total weight 560. Luck 5 is not five reward rolls. All thirteen entries omit quality; the inspected vanilla serializer defaults quality to 0, so luck does not change these particular entry weights.

The percentages below are **conditional on already picking the winning totem**, using the unmodified shipped table and the inspected default weight behavior. They are not per-purchase chances or guarantees about modded loot hooks. Stack quantities are the table’s requested ranges.

| Reward | Requested amount | Weight / 560 | Share of winning table |
|---|---|---:|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-golden_upgrade_kit.webp" width="64" height="64" alt="Golden Upgrade Kit"><br>Golden Upgrade Kit | 1 | 20 | 3.5714% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-magic_repair_dust.webp" width="64" height="64" alt="Magic Repair Dust"><br>Magic Repair Dust | 1–5 | 60 | 10.7143% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-small_skill_crystal.webp" width="64" height="64" alt="Small Skill Crystal"><br>Small Skill Crystal | 1–10 | 75 | 13.3929% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-medium_skill_crystal.webp" width="64" height="64" alt="Medium Skill Crystal"><br>Medium Skill Crystal | 1–9 | 50 | 8.9286% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-large_skill_crystal.webp" width="64" height="64" alt="Large Skill Crystal"><br>Large Skill Crystal | 1–8 | 35 | 6.2500% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-giant_skill_crystal.webp" width="64" height="64" alt="Giant Skill Crystal"><br>Giant Skill Crystal | 1–7 | 20 | 3.5714% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-minecraft-diamond.webp" width="64" height="64" alt="Diamond"><br>Diamond | 5–25 | 90 | 16.0714% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-minecraft-emerald.webp" width="64" height="64" alt="Emerald"><br>Emerald | 5–25 | 60 | 10.7143% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-minecraft-nether_star.webp" width="64" height="64" alt="Nether Star"><br>Nether Star | 1 | 15 | 2.6786% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-aoa3-colour_cannon.webp" width="64" height="64" alt="Colour Cannon"><br>Colour Cannon | 1 | 1 | 0.1786% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-minecraft-ghast_tear.webp" width="64" height="64" alt="Ghast Tear"><br>Ghast Tear | 1 | 19 | 3.3929% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-minecraft-experience_bottle.webp" width="64" height="64" alt="Bottle o' Enchanting"><br>Bottle o' Enchanting | 10–32 | 100 | 17.8571% |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/lotto-reward-1.12.2-minecraft-golden_apple.webp" width="64" height="64" alt="Enchanted Golden Apple (metadata 1)"><br>Enchanted Golden Apple (metadata 1) | 1–2 | 15 | 2.6786% |

The Enchanted Golden Apple uses historical **metadata 1**. Its picture is base apple artwork; it does not fabricate the enchantment glint. The Lotto Banner is added outside this weighted table. The callback assigns the generated item entities an owner name when a drop object is returned; that is not a claim of permanent theft-proof pickup.

### Colour Cannon example

Colour Cannon has weight 1 out of 560: **1/560 of winning table rolls**, about 0.1786%. Under the stated ordinary five-choice model, that becomes **1/2800 per one-choice attempt**, about 0.0357%. These are two different denominators; quoting1/560 as the per-Totem chance would omit the winner-selection step. Changes to the table, eligibility, spawning or interaction flow invalidate that simple combined model.

## Where the item is sold

The inspected historical trader catalog contains 22 candidate offers. The ordinary Lottoman asks 14 Silver Coins; twenty-one realm variants ask 28 of their own token type. All offer one Lotto Totem. Availability and generated offer selection remain subject to the [historical trader rules](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trading-and-Traders-1.12.2). Realm tokens are not interchangeable with the four banker coin tiers.

| Trader | Cost for one Totem | Open candidate offer |
|---|---|---|
| Abyssal Lottoman | 28 Abyss Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:abyssal_lottoman&q=lotto_totem) |
| Baron Lottoman | 28 Baron Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:baron_lottoman&q=lotto_totem) |
| Boreic Lottoman | 28 Borean Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:boreic_lottoman&q=lotto_totem) |
| Candied Lottoman | 28 Candyland Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:candied_lottoman&q=lotto_totem) |
| Celevian Lottoman | 28 Celeve Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:celevian_lottoman&q=lotto_totem) |
| Creeponia Lottoman | 28 Creeponia Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:creeponia_lottoman&q=lotto_totem) |
| Crystal Lottoman | 28 Crystevia Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:crystal_lottoman&q=lotto_totem) |
| Dustopian Lottoman | 28 Dustopia Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:dustopian_lottoman&q=lotto_totem) |
| Floro Lottoman | 28 Gardencia Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:floro_lottoman&q=lotto_totem) |
| Golden Lottoman | 28 Iromine Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:golden_lottoman&q=lotto_totem) |
| Haunted Lottoman | 28 Greckon Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:haunted_lottoman&q=lotto_totem) |
| Lelyetian Lottoman | 28 Lelyetia Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:lelyetian_lottoman&q=lotto_totem) |
| Lottoman | 14 Silver Coin | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:lottoman&q=lotto_totem) |
| Lunar Lottoman | 28 Lunar Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:lunar_lottoman&q=lotto_totem) |
| Mystic Lottoman | 28 Mysterium Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:mystic_lottoman&q=lotto_totem) |
| Precasian Lottoman | 28 Precasian Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:precasian_lottoman&q=lotto_totem) |
| Rocky Lottoman | 28 Deeplands Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:rocky_lottoman&q=lotto_totem) |
| Runic Lottoman | 28 Runandor Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:runic_lottoman&q=lotto_totem) |
| Shyrelands Lottoman | 28 Shyrelands Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:shyrelands_lottoman&q=lotto_totem) |
| Toxic Lottoman | 28 Vox Ponds Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:toxic_lottoman&q=lotto_totem) |
| Twinkling Lottoman | 28 Haven Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:twinkling_lottoman&q=lotto_totem) |
| Withering Lottoman | 28 Nether Tokens | [Browse](https://herbertofury.github.io/Advent-of-Ascension/trade-explorer.html?v=1.12.2&vendor=aoa3:withering_lottoman&q=lotto_totem) |

## Save/reload warning: reversed custom callbacks

The released **readEntityFromNBT** implementation calls the tag’s UUID setters using the current winner/owner fields. The released **writeEntityToNBT** implementation instead reads those keys from the supplied tag into the entity fields. Those directions are reversed. The artifact’s SRG callback methods and vanilla callback-dispatch references were checked, rather than relying on names in a source comment.

In the scoped model, saving a live group to a fresh tag adds neither custom key. Reading into a fresh entity leaves winnerUUID and ownerUUID null, even when a supplied tag already contains those values. The interaction code permits a null owner but requires a non-null matching winner UUID for winning loot. This combination is a **persistence risk in the inspected released implementation**, not a reproduced game session or proof the current Enderloom build still has it.

A restoration should write WinningUUID/OwnerUUID when saving, read them when loading, preserve the base entity UUID that identifies the winning choice, and define safe migration for already-incomplete old groups. Test all five entities together, ownership, winning identity, chunk unload/reload, server restart and multiplayer. Do not silently claim save compatibility from the existence of NBT methods.

## Other boundaries to test

- The item is consumed before the five spawn attempts, and their boolean return values are not checked. Verify failure/refund behavior and protected areas.
- The final successful server placement path returns PASS from the item method. Verify actual hand/use-result handling in the target game rather than assuming SUCCESS is returned.
- processInitialInteract has a 12000-tick condition, but applyPlayerInteraction still independently checks the owner. Do not advertise a ten-minute public ownership expiry without verifying the actual interaction dispatch.
- Nearby cleanup selects the entity class, not a matching group UUID. Normal spacing checks reduce overlap, but restoration tests should cover externally spawned or overlapping groups.
- The advancement request sits inside the generated-loot loop; the extra banner request follows it. Empty or replaced loot tables can therefore exercise a different branch.

## Evidence and next steps

- [Released placement, reward, persistence and probability evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/lotto-totem-evidence-1.12.2.json).
- [Layout and reward portrait provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/lotto-art-evidence-1.12.2.json).
- [Historical weapon acquisition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Weapon-Acquisition-1.12.2), [banker conversion ratios](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bankers-Coin-Exchange-and-Inventory-Safety-1.12.2), and [reward boxes/Skill Crystals](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.12.2).
- Original AoA art and systems by Tslat and contributors; vanilla references by Mojang. Independent source-derived documentation. No game files were executed or changed.
