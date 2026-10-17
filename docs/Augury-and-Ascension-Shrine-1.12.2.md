# Augury and the Ascension Shrine: retained features and version limits

**Primary artifact: Minecraft 1.12.2 / AoA 3.3.6.** The release retains an Ascension Shrine, ten essence items and Augury-related classes, but the inspected shrine activation is a stub. A separate **1.7.10 pinned-source reference** contains an active essence interaction. Do not merge these into one supposedly working tutorial.

[Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Historical Anima](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) · [Soul Tablets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Tablets-Effects-and-Ownership-1.12.2) · [Ancient Cavern](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2)

![Retained 1.12.2 Ascension Shrine and ten essence item previews, with inactive-handler warning](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/augury-retained-items-1.12.2.webp)

## What the released 1.12.2 shrine actually does

The selected activation method reads the world's client/server flag and returns **true**. Its released bytecode contains no invoked methods that consume an essence, grant XP, change tribute, play the intended sound or validate a required Augury level.

The pinned source includes a TODO and a large **commented-out** interaction block. That commented block is not the executed released behavior. A successful interaction return does not prove the shrine trained the skill.

The block is genuinely constructed in the released block-registration method, and the ten essence constructors retain level/XP metadata. Registration and available artwork do not establish a working training loop or a normal survival acquisition route.

[Inspect the exact historical Shrine resource card](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Atile.AscensionShrine.name).

## Ten retained essence definitions

These are **stored constructor values**, not XP currently granted by the 1.12.2 shrine. Each link opens that release's resource preview.

| Essence | Stored level field | Stored XP field |
|---|---:|---:|
| [Weak Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakEssence.name) | 1 | 4 |
| [Molten Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MoltenEssence.name) | 10 | 7 |
| [Charged Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ChargedEssence.name) | 18 | 10 |
| [Ominous Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.OminousEssence.name) | 27 | 12 |
| [Empowered Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EmpoweredEssence.name) | 36 | 15 |
| [Luminate Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LuminateEssence.name) | 45 | 20 |
| [Ancient Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AncientEssence.name) | 58 | 120 |
| [Dark Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DarkEssence.name) | 66 | 250 |
| [Ethereal Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EtherealEssence.name) | 75 | 400 |
| [Divine Essence](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DivineEssence.name) | 84 | 600 |

The direct member-reference scan checked **3,451 AoA classes** for calls to `AuguryEssence.getLvlReq`, `AuguryEssence.getXp`, `AuguryUtil.getMaxCreation` and `AuguryUtil.getMaxSoul`.

- No direct calls to the two essence getters were found in that scan.
- The two maximum-resource helpers were referenced by three client rendering methods, with two calls in each method.
- This does not rule out reflection, generic skill XP mechanisms, commands or external mods. In particular, it does not prove that no route can ever change an Augury level.

A literal-ID scan of the release's recipes, loot tables and advancements found no matches for these ten essence IDs or the Ascension Shrine ID. This is a bounded resource result, not proof of every possible code-driven acquisition route. Do not invent a crafting recipe or natural drop source to fill the gap.

## Maximum-resource helpers do not scale with Augury here

The selected `getMaxCreation(level)` and `getMaxSoul(level)` methods each return **200**, independent of their argument. Older tiered values visible inside source comments are inactive.

The selected resource-regeneration helper also uses a 200 cap and applies its resource-regeneration modifier before storing the result. These findings do not certify every resource-writing path or external modifier, but they do reject a tutorial claiming that these two released helpers grant larger Soul/Creation pools as Augury levels rise.

## Retained Augury armor and master trades

The armor class declares Augury level **100**. Its full-set buff callbacks add/remove a **0.3 Augury XP modifier**. Its `onEffectTick` requests **0.01 Soul regeneration** through the shared helper. That is a callback amount, not a measured per-second regeneration rate or proof of how often every equipment configuration calls it.

The Augury Master's selected trade-list method declares four exchanges, each with one Lunaver Coin as the input and one armor piece as the output:

- Augury Helmet
- Augury Chestplate
- Augury Leggings
- Augury Boots

[Inspect the historical Augury Master](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aaugury_master).

These are declared trade entries. They do not by themselves prove natural NPC placement, complete skill progression, every trading restriction or a finished modern port.

## Older 1.7.10 source-only restoration reference

The pinned 1.7.10 source at commit `cb1ca8c65315c749a6edd5f3ca602b2aa27dac6d` has active code in its Ascension Shrine interaction. **A matching released 1.7.10 artifact was not available for verification here**, so this section is a restoration reference, not a binary-verified gameplay claim. The illustration above uses 1.12.2 assets and is not evidence of 1.7.10 visual parity.

The older source requires server-side interaction, a player who is **not sneaking**, and a non-null held item. It switches on the held item's **unlocalized name**, then applies the route's level check where one is present.

| Older source item key | Explicit minimum level | XP request |
|---|---:|---:|
| `item.EssenceWeak` | No explicit check in this case | 4 |
| `item.EssenceMolten` | 10 | 7 |
| `item.EssenceCharged` | 18 | 10 |
| `item.EssenceOminous` | 27 | 12 |
| `item.EssenceEmpowered` | 36 | 15 |
| `item.EssenceLuminate` | 45 | 20 |
| `item.EssenceAncient` | 58 | 120 |
| `item.EssenceDark` | 66 | 250 |
| `item.EssenceEthereal` | 75 | 400 |
| `item.EssenceDivine` | 84 | 600 |
| `item.GhostStone` | 50 | 40 |

This older list includes **Ghost Stone at level 50 for 40 XP**, in addition to the ten essences. On a successful branch:

1. It requests the route's Augury experience.
2. Outside Creative, it calls the inventory helper to consume one matching registered item. This is an inventory-helper operation, not a whole-held-stack payment.
3. It plays the Augury sound.
4. In dimension 0 during daytime, it requests +4 Luxon tribute.
5. It updates the multiplayer player's container view.

The source checks a display/unlocalized-name string to choose a branch but consumes a specific registered inventory item. A restoration should validate item identity and payment success before awarding effects, rather than assume that a matching name guarantees the intended item was consumed. No exploit or live item-loss behavior is claimed by this source review.

Do not copy the commented-out 1.12.2 whole-stack example into this older per-use route. Likewise, do not describe the older active code as what stock AoA 3.3.6 currently executes.

## Ancient Cavern requirements are a separate question

The historical Ancient Cavern shrine checks documented in the [cavern walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ancient-Cavern-and-Deity-Shrines-1.12.2) use the four other required skills and tribute. Augury checks visible in comments are not active requirements in the selected released handlers. Do not tell a player to solve this inactive Ascension Shrine loop before those encounters without target-build evidence.

## Restoration decisions and tests

- [ ] Choose the intended behavior explicitly: source-only 1.7.10 per-use parity, a separately designed batch interaction, or another documented target.
- [ ] Preserve stable registry and save identifiers; keep old essence metadata distinct from actual accepted input/payment.
- [ ] Resolve survival acquisition and NPC availability from target-version evidence rather than inventing recipes or drops.
- [ ] Test each essence and Ghost Stone, low/exact required level, empty hand, sneaking and Creative.
- [ ] Validate registered item identity, payment success and XP/tribute order; reject same-name substitutes safely.
- [ ] Test held stack versus another inventory stack and full inventory/container synchronization.
- [ ] Decide whether maximum Soul/Creation should remain 200 or implement a separately specified progression; check every affected writer and UI.
- [ ] Verify armor requirement, callback frequency, XP modifier cleanup and Soul regeneration on a dedicated server.
- [ ] Keep any fixes and redesigned mechanics clearly separated from historical parity and the stock release evidence.

## Evidence

Sixteen selected released methods, ten essence constructor bindings, one block-registration segment and the 3,451-class direct-reference scan support the 1.12.2 findings. Eleven older route cases were extracted separately from a pinned 1.7.10 source file. No Minecraft/server/mod was executed.

- [Released evidence and separately labelled older source reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/augury-retained-evidence-1.12.2.json)
- [Image provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/augury-retained-art-evidence-1.12.2.json)
- [Pinned 1.12.2 shrine source](https://github.com/Tslat/Advent-Of-Ascension/blob/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source/block/functional/utility/AscensionShrine.java)
- [Pinned 1.7.10 shrine source, not release-artifact verified](https://github.com/Tslat/Advent-Of-Ascension/blob/cb1ca8c65315c749a6edd5f3ca602b2aa27dac6d/source/block/functional/AscensionShrine.java)
