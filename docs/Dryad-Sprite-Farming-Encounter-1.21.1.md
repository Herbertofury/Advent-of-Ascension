# Dryad Sprites: prepare the right hoe before you harvest

[Open all six appearances and loot](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3%3Adryad_sprite) · [Farming, soils and harvesting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Farming-Soils-and-Harvesting-1.21.1) · [Skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1)

![Six Dryad Sprite variants paired with their exact hoes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/dryad-sprite-hoe-matches-1.21.1.webp)

**Scope:** Minecraft 1.21.1 / AoA 3.7.16.1. Released skill/loot JSON and selected class methods were checked against pinned source. This is a source-based encounter walkthrough, not a live spawn-rate or reward test.

## Unlock and trigger the encounter

The released Farming definition unlocks `aoa3:dryad_sprite_spawn` at **Farming level 44**. With that ability active, its server-side block-break handler tests its scaled chance and then requires:

- The broken block is a `CropBlock` at maximum age.
- The player is not in Creative's instant-build mode.
- The block above the crop is air.
- The entity spawn succeeds.

A successful spawn is assigned to the harvesting player. The handler uses the block-break event: do not assume every right-click harvest or another mod's automated harvester triggers the same route. Likewise, a plant that looks mature but uses a different block class is not automatically eligible.

The chance scales through the shared ability helper. The resource's base and per-level numbers are not a guaranteed encounter every fixed number of crops. Carry the matching tools before harvesting rather than relying on a sprite waiting while you craft them.

## Match the exact variant

| Sprite appearance | Inspected matching offering |
|---|---|
| Wood | Minecraft Wooden Hoe |
| Stone | Minecraft Stone Hoe |
| Iron | Minecraft Iron Hoe |
| Gold | Minecraft Golden Hoe |
| Diamond | Minecraft Diamond Hoe |
| Netherite | Minecraft Netherite Hoe |

Interact with the correct hoe. The held stack must both support the hoe-till action and match the variant's ingredient. A higher-tier hoe is not an automatic substitute, and another mod's tool with the same material name does not automatically pass the exact-item ingredient check.

**A wrong hoe discards the sprite.** It plays an unhappy response rather than letting you cycle through every hoe until one works. Ordinary damage is rejected unless its source has the technical-damage tag, so attacking it is not the intended reward route.

The selected success-interaction method does not shrink the hoe stack or call a durability-consumption method. Describe this as showing/interacting with the matching hoe, not a promise that a tool is sacrificed. External mod hooks can still affect behavior.

## Ownership and timing

Only an allowed owner can initiate the successful interaction. Naturally spawned ability sprites are assigned to the harvesting player. An unowned sprite can become owned on the first eligible interaction before the hoe test, so an empty-handed interaction can matter in multiplayer too.

While its success timer is still −1, the regular despawn check discards it once its age exceeds **100 entity ticks**, in addition to inherited despawn behavior. That is a source threshold, not a guarantee of five seconds of real time on every server.

A correct match starts a **44-tick success countdown**, stops navigation and movement, and leads to the happy/reward sequence. Once the countdown has begun, the ordinary unresolved-sprite expiry condition is no longer the same. Successful sprites are not accepted by the inspected `shouldBeSaved` condition; test chunk unloading or disconnection rather than assuming a pending reward survives either.

## What the success sequence can award

The inspected success path awards **10–19 vanilla XP** when the mob-loot gamerule allows that award. Its owner must be found as a player, and the player's kill callback must accept the event, for the inspected death-loot call to run. Loot conditions and other hooks still apply.

The released entity table has two player-kill-conditioned pools:

1. **1–5 Sticks**, with configured loot functions for **500 Dexterity XP** and **5,000 Farming XP**. These functions act on the generated stack; do not multiply the configured skill XP by the number of sticks. Actual skill handling/modifiers still apply.
2. A rare **Dryad's Blessing** entry with weight 1 against an empty entry of weight 1,000. Under the unchanged single-roll, ordinary-weight configuration, that is 1/1,001 for this pool once eligible, not a guaranteed encounter reward.

The Farming resource separately restricts equipping Dryad's Blessing until level **92**. Obtaining an item and being able to equip it are different milestones. The Helm of the Dryad's level-100 equip restriction does not mean it appears in these two loot pools.

## The six variants are not a uniform six-way roll

The inspected selector starts with Wood as fallback, then tests non-Wood registered variants in order and stops at the first passing predicate. The stock non-Wood definitions each use a chance based on registry size. Sequential first-success selection does not make every form equally likely. Registry additions and ordering can also affect the outcome, so this guide does not assign a fabricated fixed rarity to each portrait.

## A practical farming routine

1. Reach the ability unlock and check that your skill/ability configuration is active.
2. Prepare the six exact hoes where you can select them quickly.
3. Break mature eligible crops with clear air above them.
4. Identify the sprite's variant and interact as its owner with the matching hoe.
5. Stay through the success sequence and inspect the reward; do not attack or test random hoes.
6. Keep acquisition, rare-item luck and equip-level requirements separate when planning progression.

## Evidence and restoration checks

[Five released class selections, six offerings, skill/loot resources and interaction branches](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/dryad-sprite-encounter-evidence-1.21.1.json) · [Entity source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/npc/ambient/DryadSpriteEntity.java) · [Spawn ability](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/player/ability/farming/DryadSpriteSpawn.java) · [Variant matching and selection](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/entity/variant/DryadSpriteVariant.java) · [Illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/dryad-sprite-art-evidence-1.21.1.json).

Acceptance should cover all six forms, correct/wrong hoes, owner versus another player, right-click/automated-harvest compatibility, expiry versus success timing, owner disconnection, chunk unloading, gamerules and the actual skill-XP recipient. No restored-build gameplay pass is claimed here.

AoA portraits and mechanics: Tslat and contributors. Vanilla hoe models: Mojang/Microsoft. Original independent layout and explanations.
