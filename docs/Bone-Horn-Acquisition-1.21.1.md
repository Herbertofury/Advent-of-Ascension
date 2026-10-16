# Find and repair the Bone Horn · Minecraft 1.21.1

**AoA 3.7.16.1.** A practical route from a broken horn to the Tyrosaur entry token. These instructions combine shipped loot and world-generation resources with inspected item code. They have not been certified in the owner's current Enderloom build.

![Cocoon, Bone Horn, Bone Fragments Ore, Ivory and the four bone fragments](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bone-horn-acquisition-reference-1.21.1.webp)

[Boss entry and preparation](Boss-Entry-and-Token-Preparation-1.21.1) · [Exact repair recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=bone_horn) · [Precasia archaeology and entry](Precasia-Realmstone-Walkthrough)

## 1. Find a Cocoon before collecting the repair ingredients

The recipe repairs an **existing damage-2 Bone Horn**. It does not craft a new horn from fragments alone.

A useful starting search is **Precasian Desert sand**. The shipped desert biome includes the `aoa3:desert_cocoons` placed feature. Its placement sequence makes 1–3 attempts, starts from the world-generation surface heightmap, scans down for sand, then applies a vertical offset of **−6 to −1** before attempting to replace a sand-tagged block with an unwebbed Cocoon. This suggests searching below the sandy surface rather than only looking for hanging cocoons.

Those are placement attempts and offsets, not a promise of 1–3 cocoons in every chunk or a universal absolute Y coordinate. Terrain, target blocks, biome filtering and world-generation changes still matter.

## 2. Use the correct harvesting branch

The [Cocoon loot reference](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=aoa3%3Ablocks%2Fcocoon) has distinct branches:

| Harvest context | Shipped table behavior |
|---|---|
| Silk Touch | Returns the Cocoon block through the Silk Touch pool; the horn pools require **no Silk Touch** |
| Precasian Desert, no Silk Touch | One weighted selection among six entries; Bone Horn weight 1 out of total weight 17 |
| Outside Precasian Desert, no Silk Touch | A separate Bone Horn pool has a **0.01 random gate** and one roll |

For the eligible stock desert pool, **1/17 ≈ 5.88%** is the conditional horn-selection probability. That is a calculation from this particular one-roll pool, not a general claim that loot weights are percentages. The other desert entry weights are 4, 4, 3, 3 and 2; all have zero default quality, and this pool has zero bonus rolls.

The outside-desert 1% gate is separate from its ordinary multi-roll materials pool. Neither route guarantees a horn after a fixed number of attempts. Loot overrides, game rules and failed harvests can change actual outcomes.

Both horn entries apply the same `set_damage` function. Despite the JSON value `0.32333332`, this is **not an integer damage value or a drop chance**. The inspected vanilla function interprets it as remaining durability; with the released horn's maximum durability of 3, its float calculation produces **damage 2**, matching the repair ingredient.

## 3. Collect one of each fragment and Ivory

You need **Footbone Fragment, Legbone Fragment, Chestbone Fragment, Skullbone Fragment and Ivory**, alongside the existing damage-2 horn. Use the recipe viewer for the exact ingredient layout and component requirements.

- [Bone Fragments Ore](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=aoa3%3Ablocks%2Fbone_fragments_ore) and [Deepslate Bone Fragments Ore](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=aoa3%3Ablocks%2Fdeepslate_bone_fragments_ore) have one non-Silk-Touch selection among four equal-weight fragment types. **One ore does not give all four types.** Fortune uses the ore-drop count bonus on the selected type; it does not select the missing types for you. Silk Touch yields the ore block.
- Outside-desert Cocoon materials, Precasian cave archaeology and the Precasian Lotto Hovel loot table also reference these fragments. They are alternative sources, with their own conditions, rather than guaranteed complete sets. [Find fragment references](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&q=bone%20fragment).
- [Ivory's registered modifier](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&ref=modifier%3Aaoa3%3Amisc_ivory) targets Hoglins, Zoglins, Ravagers and Goats with a `0.33333334` random gate. It is not a universal creature drop. Inspect the modifier conditions before choosing a hunting route.

## 4. Repair, awaken and finish preparing the horn

1. Craft with the damage-2 horn and the five required materials. The recipe outputs **damage 1**. Its ingredient uses strict components, so extra component changes can prevent a match.
2. Use the damage-1 horn in **Precasia** to request the nearby Wounded Tyrosaur encounter. Valid spawn space is required; sound or cooldown alone does not establish a successful spawn.
3. A qualifying player kill repairs a matching damage-1 horn in the player's searched inventory to **damage 0**.
4. Follow [the Nowhere and Boss Altar steps](Boss-Entry-and-Token-Preparation-1.21.1#2-enter-nowhere-and-gather-at-the-boss-altar) for the regular Tyrosaur encounter.

Do not confuse this Tyrosaur preparation route with the separate fire/tar conversion into Skeletron. The **Warped Horn acquisition state remains an explicitly unresolved test target** in the boss guide.

## Evidence and checks

[Released acquisition resources, pool arithmetic and vanilla durability code](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bone-horn-acquisition-evidence-1.21.1.json) · [Illustration provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bone-horn-guide-art-evidence.json) · [Mining and generation guide](Mining-and-Ore-Generation-1.21.1).

Artwork belongs to Tslat and the AoA contributors. The illustrations are source-model references, including the corrected ore overlay; they are not runtime screenshots or proof of each horn damage-state appearance.
