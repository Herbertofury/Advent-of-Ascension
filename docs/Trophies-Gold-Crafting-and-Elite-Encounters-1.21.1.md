# Trophies, gold crafting and elite encounters · Minecraft 1.21.1

**Version:** released AoA 3.7.16.1. A trophy's stored entity data and **original** flag matter more than its visible name. This guide connects eight released boss-loot pools, the nine-trophy gold recipe and the elite-token substitution map without treating decorative copies as progression items.

[Boss entry and token preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) · [Gold trophy recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.21.1&q=gold_trophy) · [Loot and modifiers](https://herbertofury.github.io/Advent-of-Ascension/loot-reference.html?v=1.21.1&q=trophy)

## 1. Keep original trophies separate from decorations

The inspected boss-loot pools explicitly write trophy data with `is_original: true` and the defeated boss's entity ID. A plain pedestal item, a renamed item or a similarly colored decoration does not establish that data.

**Do not use a spawn egg on a collected original that you want for progression.** The placed-trophy interaction replaces its stored entity with the egg's type, and the block entity sets the original flag to **false**. Survival also consumes the egg. This is a direct source/released-method finding, not an action performed on your world.

The flag is stored data; appearance alone is not a reliable originality test. Creative mode or a copied display name is not itself a substitute for checking the actual trophy record.

## 2. Craft one Gold Trophy from nine originals

![Nine original normal trophies of one valid entity ID produce a Gold Trophy; no gold-ingot ingredient](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/gold-trophy-recipe-1.21.1.webp)

Use a **3×3 crafting grid** with all nine ingredient slots occupied:

1. Every input must be a normal **Trophy** item, not Gold Trophy or Ornate Trophy.
2. Every input must carry trophy data marked original.
3. Each record must contain the **same non-empty entity ID**.
4. The first record's entity type must resolve in the active registry.
5. Inspect the result before taking it, especially if the originals contain different variant/entity data.

This custom recipe requires **no Gold Ingots**. Nine items stacked in a single slot are not nine occupied ingredient entries.

The matcher compares entity IDs, rather than demanding that every extra entity-data field is identical. Assembly carries the **first matching trophy's data record** into the Gold Trophy. It does not merge the different variants or other details from all nine inputs. If you care about a particular stored appearance, do not mix variant records casually.

The clone helper creates a fresh destination item, copies the trophy-data component and derives its item name. It is not a general promise that every unrelated custom item component is preserved.

## 3. Follow the four loot-documented routes

![Four regular bosses, original trophies, Gold Trophy tokens, elite bosses and Ornate Trophy results](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/trophy-elite-routes-1.21.1.webp)

| Normal boss table | Basic trophy data | Elite boss table | Elite reward type |
|---|---|---|---|
| Smash | Original, `aoa3:smash` | Elite Smash | Ornate Trophy, original `aoa3:elite_smash` |
| King BamBamBam | Original, `aoa3:king_bambambam` | Elite King BamBamBam | Ornate Trophy, original `aoa3:elite_king_bambambam` |
| Nethengeic Wither | Original, `aoa3:nethengeic_wither` | Elite Nethengeic Wither | Ornate Trophy, original `aoa3:elite_nethengeic_wither` |
| Tyrosaur | Original, `aoa3:tyrosaur` | Elite Tyrosaur | Ornate Trophy, original `aoa3:elite_tyrosaur` |

Each inspected table has a named trophy pool with one base roll and one entry, with no local pool condition. This is evidence of the shipped loot definition, **not a guarantee that every modded death event will deliver an item**. Active table selection, drop rules and loot modifiers still matter.

The pictures show separate source-model boss portraits and pedestal references. They do not simulate the miniature entity inside a placed trophy or certify its in-game animation.

## 4. Use the original Gold Trophy through the boss-entry flow

The Gold Trophy token method rejects missing trophy data and non-original records. Its inspected substitution map contains:

- Smash → Elite Smash
- King BamBamBam → Elite King BamBamBam
- Nethengeic Wither → Elite Nethengeic Wither
- Skeletron → Elite Skeletron
- Tyrosaur → Elite Tyrosaur

**Skeletron is a code-map entry, not a trophy acquisition route established by these eight loot tables.** Keep that gap explicit instead of assuming an ordinary Skeletron trophy drops in this release.

Follow the [Nowhere/Boss Altar entry instructions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) for the actual encounter flow and its dimension/difficulty checks. Holding a Gold Trophy is not permission to assume right-clicking any block will summon the boss. The token helper's map alone also does not certify every fallback entity as a valid encounter.

Prepare for the elite enemy independently; it is not merely a renamed normal boss. The spawning helper also applies configured multiplayer-health scaling when applicable, so a group fight need not have the same health budget as a solo encounter.

## Troubleshooting

| Symptom | Check |
|---|---|
| Nine trophies do not craft | Nine occupied slots, normal Trophy item type, original flags and matching entity IDs. |
| All names look identical but the recipe fails | Names are not the matcher; inspect stored IDs and originality. |
| Spawn-egg decorations fail the recipe | The egg-decoration path marks them non-original. |
| Ornate trophies fail in the gold recipe | The input check specifically requires the normal Trophy item. |
| The output has an unexpected variant | The first matching trophy's record is carried forward; records are not merged. |
| An original Gold Trophy is rejected at an altar | Check the complete boss-entry flow, not just the item's color or name. |
| You cannot find a Skeletron trophy route | Its elite substitution exists, but this audit did not establish acquisition. |

## Evidence and acceptance

[Eight trophy loot pools, released method hashes and eight ingredient-model cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/trophy-progression-evidence-1.21.1.json) · [Pedestal and portrait provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/trophy-art-evidence-1.21.1.json).

The independent cases cover nine valid originals, eight slots, one decoration, mixed IDs, an Ornate substitute, missing ID, unresolved first type and differing extra data with the same ID. These are documentation checks, not live crafting or combat tests. Validate actual loot delivery, item placement/breaking, save/load, variant display, Gold Trophy consumption and elite encounter behavior in the exact target build.

AoA artwork and systems are by Tslat and contributors. The diagrams and route descriptions are original source-backed documentation.
