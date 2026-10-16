# Boss entry and token preparation · Minecraft 1.21.1

**AoA 3.7.16.1.** This is a source-grounded preparation and entry guide, with released recipe/component evidence. It is not a claim that every encounter chain has passed an in-game test. In particular, the Warped Horn/Skeletron chain has a concrete unresolved state-setting gap described below.

![Boss tokens and preparation states](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/boss-entry-tokens-1.21.1.webp)

[Boss attributes and mechanics](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modern-Boss-Dossiers) · [Smash tactics](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Smash-Combat-Field-Guide) · [Versioned recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1)

## The essential distinction: entry item versus arena summon

The modern boss item does not simply create the boss beside you when you right-click it. For a ready token, the inspected common item flow takes a server player **into Nowhere** after its use action finishes. The actual encounter is requested at a **Boss Altar inside Nowhere**.

The common use duration is 60 ticks; Bone Horn uses 63. At a steady 20 TPS those correspond to approximately three seconds, but these are tick counts, not a measured wall-clock guarantee. If the Nowhere level is unavailable, the common finish-use method returns without teleporting.

Do not reuse a historical altar recipe or assume that a modern item with the same name behaves like its 1.16.5 counterpart.

## 1. Prepare a ready token

### Troll Idol → Smash

[Recipe and exact output components](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=troll_idol) · [Smash field guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Smash-Combat-Field-Guide)

The released crafting recipe produces a Troll Idol with **damage value 19**. This is not “19 damage dealt,” and it does not mean the item is ready to summon Smash.

The source requires an undamaged idol for boss entry. Its melee callback reduces the damage value by one when the idol itself delivers the finishing hit to an entity in the undead tag. Starting from the recipe's damage 19, that means 19 qualifying finishing hits if nothing else modifies the item or callback behavior.

A practical preparation loop is to weaken an undead target with ordinary equipment, switch to the idol for the final hit, and check the item's state afterward. Merely carrying it while killing with another weapon does not invoke its hit callback.

### Nethengeic Callstone → Nethengeic Wither

[Recipe and exact output components](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=nethengeic_callstone)

The released recipe starts at **damage value 2**. The preparation order in the inspected item code is:

1. At damage 2, hit a vanilla Wither using the Callstone. A qualifying hit changes it to damage 1.
2. At damage 1, hit a Nethengeic Beast using the Callstone. A qualifying hit changes it to damage 0.
3. The undamaged item can then use the boss-entry flow.

Unlike the Troll Idol callback, this particular method does **not** test that the target died. Do not add an invented killing-blow requirement. These are still dangerous encounters; prepare defences and a retreat before trying to land the required hit.

### Explosive Idol → King BamBamBam

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aexplosive_idol)

The source defines a special Piglin exchange rather than an ordinary fixed crafting recipe:

- The Piglin must be wearing a Golden Helmet and have an empty offhand.
- Interact while holding an **Enchanted Golden Apple or an AoA Gold Coin**. The event splits one item from your stack into the Piglin's offhand and marks the special exchange.
- Keep the Piglin alive and at full health. The delayed check runs after 120 ticks, and the loot modifier also requires full health.
- The released modifier is attached to the Piglin bartering loot table. When the marked, healthy Piglin reaches that path, the modifier returns an Explosive Idol and clears the marker.

A normal gold-ingot barter does not set this special marker. The 120-tick check is part of a multi-event sequence; this guide has not live-tested every interaction with other Piglin mods.

### Bone Horn → Tyrosaur

**Start here:** [Find the first horn, understand Cocoon odds, and collect its repair materials](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bone-Horn-Acquisition-1.21.1).

[Repair recipe and strict ingredient components](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=bone_horn) · [Wounded Tyrosaur reference](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3%3Awounded_tyrosaur)

The relevant released crafting recipe is a **repair stage**, not a fresh horn made from nothing. It requires:

- An existing Bone Horn with the recipe's strict component match, including damage value **2**
- Ivory
- Footbone Fragment
- Legbone Fragment
- Chestbone Fragment
- Skullbone Fragment

The result has damage value **1**. Because this ingredient uses strict components, an arbitrarily modified horn can fail even if its visible name looks right. The recipe explorer now displays the horn identity, damage values and exact-component requirement directly.

At damage 1, finish using the horn in **Precasia**. The source searches for a valid nearby Wounded Tyrosaur spawn location. It can fail to find one; a sound or cooldown alone does not prove a creature spawned. The spawned wounded creature targets the user.

A qualifying player kill of a Wounded Tyrosaur repairs a matching damage-1 Bone Horn in that player's searched inventory to damage **0**. That undamaged horn can then enter the regular Tyrosaur boss flow. A horn with damage greater than 1 does not start this use action.

The released Cocoon loot table contains Bone Horn entries with durability-setting functions and different biome/loot conditions. They are not unconditional drops. Keep biome, Silk Touch and selected pool conditions attached to any acquisition advice; do not convert a table entry into a guaranteed reward.

### Warped Horn → Skeletron: unresolved acquisition link

[Item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awarped_horn) · [Wounded-chain audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skeletron-wounded-chain-audit.json)

The Warped Horn is a valid Skeletron boss token in the inspected source. Its normal acquisition chain is **not certified here**:

- Wounded Tyrosaur has a conditional fire/tar conversion path into Skeletron.
- Skeletron's custom Warped Horn drop requires its synchronized `WOUNDED` flag to be true.
- The inspected conversion callback transfers orientation but does not set that flag. Skeletron initializes it false and can restore it from NBT.
- The released-class audit found no direct field reference outside SkeletronEntity, including references through its inheritance chain.
- A recursive scan of all **334 shipped structure NBT files** found no embedded Skeletron or Wounded Tyrosaur entity and no compound key containing `wounded`. Every template parsed successfully. This narrows the shipped-template route only; it does not cover external datapacks, commands or runtime state. [Template scan evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/wounded-structure-nbt-audit-1.21.1.json).

This is a concrete restoration/test target, not proof that no data pack, NBT path or other mod could ever supply the item. Do not send a player through an allegedly guaranteed tar-conversion reward loop until that state transition is verified or repaired.

## 2. Enter Nowhere and gather at the Boss Altar

Once the appropriate token is ready, finish its use action outside Nowhere. The common flow checks the player's Nowhere advancement state and preserves a return-location record when moving them into the dimension.

At the altar:

1. Set an appropriate difficulty. **Peaceful is explicitly rejected.**
2. Hold a valid token in the state expected by its `getEntityType` method. Damaged Troll Idols and Callstones are rejected; an undamaged Bone Horn is required for the normal Tyrosaur token.
3. Gather participating players close to the altar. The source selects living players inside a specific nearby box, not everyone on the server.
4. Stay in that area while the teleport warning/countdown runs. Eligibility is checked again before the transfer.
5. If the altar reports “in use” or no free arena, resolve that state rather than repeatedly clicking or assuming the token is broken.

The inspected arena code schedules the transfer after **100 ticks**, then schedules the boss spawn another **140 ticks** after that stage. At steady 20 TPS that is roughly five seconds followed by seven seconds, subject to server timing and the remaining-player checks. A short wait after transfer is intentional in this source flow.

## 3. Expect multiplayer scaling

The token interface applies a configured maximum-health boost for additional players. The pinned server default is **25% per extra player**, using a total-multiplier operation, and then sets the boss to its resulting maximum health.

That configuration can change. The actual player count is taken from players inside the arena near the scheduled spawn, so a static health value in the bestiary is not automatically the final multiplayer health total.

## 4. Original gold trophies and elite encounters

An original Gold Trophy with valid trophy data is also a boss token. The inspected map substitutes elite versions for Smash, King BamBamBam, Nethengeic Wither, Skeletron and Tyrosaur.

A trophy without data or without the original-trophy flag is rejected by that token method. Do not assume a decorative copy, a similarly colored block or a different trophy type unlocks the elite fight. The elite version needs its own preparation; it is not merely a renamed normal boss.

## 5. Retreat and recover deliberately

The arena transfer grants a Return Crystal. In the inspected code, its use is restricted to Nowhere and it has a 20-tick use duration. It returns players to a designated Nowhere hub/lobby route according to region and progression state; it is not a universal teleport-home item.

Outside Creative, the finish-use path consumes one crystal. **Using it while already in the lobby can consume it without moving you**, because the movement branch only runs outside that region. Use the appropriate portal/exit flow for leaving the dimension instead of assuming every crystal use exits Nowhere.

Stored-item restoration and arena cleanup are separate code paths. Their existence is not a promise that every modded inventory, disconnect or death scenario has been tested. Verify valuable-save recovery behavior before treating a new conversion build as safe for an irreplaceable world.

## Troubleshooting by symptom

| Symptom | Check |
|---|---|
| Crafted token does nothing | Troll Idol damage 19 and Callstone damage 2 are preparation states, not ready tokens |
| Bone Horn repair recipe fails | Existing damage-2 horn, every fragment, Ivory and strict item components |
| Bone Horn sounds but no full boss appears | Damage 1 invokes the Precasia wounded-creature path; damage 0 is the normal boss token |
| Right-click does not spawn a boss nearby | Modern item use is a Nowhere entry flow; request the fight at the Boss Altar |
| Altar rejects the item | Token state, correct original trophy data, Peaceful difficulty, or wrong dimension |
| Teammate stays behind | They left the selected region, changed level or failed the alive/position check before transfer |
| Arena is empty for a few seconds | Scheduled transfer/spawn stages; verify players remain present |
| Warped Horn never appears after conversion | WOUNDED flag transition is an unresolved inspected-source gap; do not claim the chain is complete |
| Return Crystal disappears without leaving the hub | The source consumes the crystal before checking the non-lobby movement branch |

## Evidence and Enderloom acceptance tasks

[Released recipe/component resources and source/class records](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/boss-entry-evidence-1.21.1.json) · [Pinned entry-item classes](https://github.com/Tslat/Advent-Of-Ascension/tree/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/misc/summoning) · [Boss Altar](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/block/functional/utility/BossAltar.java) · [Arena sequencing](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/world/nowhere/NowhereBossArena.java).

- [ ] Test all five token preparation/entry paths against the exact target build.
- [ ] Preserve recipe damage components and strict ingredient matching through conversion.
- [ ] Test party eligibility, delayed spawn, full arenas, disconnects and return-state recovery.
- [ ] Verify original-trophy elite substitutions and configured multiplayer scaling.
- [ ] Resolve and test the Wounded Tyrosaur → wounded Skeletron → Warped Horn state chain without globally marking every Skeletron wounded.
- [ ] Confirm loot, saved state, repeatability and performance without deleting phases or simplifying AI.

This page adds usable preparation instructions and clearly marked gaps. It does not certify a completed owner-specific Enderloom build.
