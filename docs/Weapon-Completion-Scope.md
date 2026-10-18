# What “every weapon finished” means

**Fully accepted native upgrades: 0.** Concepts, editable studies, parser passes and source inventories are milestones, not finished playable weapons.

## Inspected scope so far

- The first-target 1.20.1 registry study covers 228 guns, shotguns, snipers, cannons and blasters.
- The historical 1.12.2 census covers 412 registrations across a broader range of weapon families. Of these, 228 belong to those same five families.
- 225 raw IDs match between those inputs. Three likely renamed pairs have matching class basenames and families: experiment_w801 → experiment_w_801, ka500 → ka_500, and viper1 → viper_1.
- A raw union therefore has 415 IDs, but that is not 415 proven distinct weapons. Keep versioned behavior reviews separate, and verify migration rather than silently treating a likely rename as a new weapon or equivalent save record.
- Historical melee, bows and other families are absent from the five-family first-target input because of scope. Missing rows are not evidence that those weapons were removed.

## Scope still to reconcile

Earlier versions, later additions, renamed identities, other first-target weapon families and version-exclusive behavior remain to be inventoried. Never announce all AoA weapons done from the first-target 228 count alone.

## Completion gate for each final identity

Preserve versioned original behavior and lore; approve its canonical concept; personally author both visual treatments; implement every agreed feature, attachment and variant; test animations, hands, materials, effects, resource accounting and persistence; pass actual native gameplay, networking, compatibility and performance QA; publish the complete guide with evidence. Remaining defects prevent full acceptance.

[Full weapon standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard) · [Versioned scope data](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-scope-reconciliation.json) · [Reproduction script](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-scope-reconciliation-tools.zip)
