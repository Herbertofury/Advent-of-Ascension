[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Staff rune costs and hand safety](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Runes-Casting-and-Hand-Safety-1.12.2)

# Why a historical staff will not cast

**Minecraft 1.12.2 / AoA 3.3.6.** Before spending runes, the base staff path calls a precondition method. **29 of 57 staves customize that gate.** The remaining 28 use the base non-null result; that does not bypass rune payment or establish that every later spell action succeeds.

![Historical staff source-model portraits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/staff-inputs-and-ammo-1.12.2.webp)

## Diagnose a failed cast in order

1. Check the release, the exact staff, and the [hand-pairing and rune-payment warnings](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Runes-Casting-and-Hand-Safety-1.12.2).
2. For a staff below, satisfy its specific gate before assuming it is broken or crafting more supplies.
3. Put all required rune types in ordinary inventory slots. A precondition passing does not establish that rune payment passes.
4. A null precondition returns failure before the base method's payment, cooldown and wear. A failure **inside the later cast function** is a separate situation that can happen after those changes.
5. If the gate and supplies are correct, investigate the actual cast/projectile path and mod compatibility. This guide does not certify those later stages.

## Exact gate by staff

Open each weapon for its portrait, rune quantities and direct recipe/drop searches.

| Staff | Entry requirement | Practical check |
|---|---|---|
| [Atlantic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AtlanticStaff.name) | At least one IMob-matching target in the caster bounding box expanded by 10 on each axis. | Move close to an eligible hostile mob. The 10 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Candy Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CandyStaff.name) | At least one IMob-matching target in the caster bounding box expanded by 10 on each axis. | Move close to an eligible hostile mob. The 10 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Celestial Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CelestialStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Concussion Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ConcussionStaff.name) | At least one IMob-matching target in the caster bounding box expanded by 8 on each axis. | Move close to an eligible hostile mob. The 8 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Coral Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralStaff.name) | The selected surrounding shell positions contain exact vanilla AIR and pass the selected player mining-permission check. | This is not a universal claim/protection compatibility check. The later spell places blocks, so test it away from valuable builds. |
| [Crystal Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystalStaff.name) | At least one eligible vulnerable player in a box expanded by 20 whose health differs from max health. | The predicate excludes spectator, Creative and damage-disabled players. The check is health != max, not an explicit team/friendship check; success returns the whole eligible player list. |
| [Crystik Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystikStaff.name) | At least one IMob-matching target without the checked MAGIC_IMMUNE property, in a box expanded by 10. | A nearby mob can still fail this predicate because of its explicit magic immunity property; no promise about all other defenses. |
| [Cryston Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystonStaff.name) | At least one IMob-matching target in the caster bounding box expanded by 10 on each axis. | Move close to an eligible hostile mob. The 10 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Everfight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EverfightStaff.name) | Caster health / max health is strictly greater than 0 and strictly less than 1. | At full health the precondition returns null; the fraction is tested before rune payment. |
| [Evermight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EvermightStaff.name) | Caster health / max health is strictly greater than 0 and strictly less than 1. | At full health the precondition returns null; the fraction is tested before rune payment. |
| [Firestorm Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FirestormStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Fungal Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FungalStaff.name) | The sampled 5×5×5 offsets around caster coordinates include grass or a BlockMushroom. | The collected entries distinguish grass from mushrooms. This only establishes a workable list, not successful growth or placement. |
| [Joker Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.JokerStaff.name) | At least one IMob-matching target in the caster bounding box expanded by 10 on each axis. | Move close to an eligible hostile mob. The 10 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Lightning Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LightningStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Lightshine](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Lightshine.name) | At least one IMob-matching target in the caster bounding box expanded by 10 on each axis. | Move close to an eligible hostile mob. The 10 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Lunar Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Lyonic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LyonicStaff.name) | At least one alive IMob in a box expanded by 10 horizontally and 1 vertically. | Large vertical separation can exclude a target even if it looks nearby horizontally. |
| [Meteor Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MeteorStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Moonlight Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MoonlightStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Nature Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NatureStaff.name) | A block in the caster box expanded by 10 implements IGrowable and its canGrow(..., false) returns true. | A fully grown crop can fail the growth predicate. Each block owns its growability rule. |
| [Nightmare Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Reef Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ReefStaff.name) | The caster reports being in water. | Rain, an ocean biome label or water nearby alone is not this check. |
| [Runic Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicStaff.name) | Caster is an EntityPlayer. | The precondition itself adds no target check. This is not proof that every later cast action succeeds. |
| [Show Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShowStaff.name) | At least one IMob-matching target in the caster bounding box expanded by 30 on each axis. | Move close to an eligible hostile mob. The 30 value expands a box, not a spherical radius; this precondition does not add a line-of-sight test. |
| [Sky Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkyStaff.name) | The caster onGround flag is true. | Try from a grounded position; the check does not prove clear airspace for what the spell does next. |
| [Striker Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.StrikerStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Tangle Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TangleStaff.name) | Player caster with a non-null block ray trace using distance input 70. | Aim at a reachable block rather than empty sky. This does not check a clear overhead path for the later spell. |
| [Warlock Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WarlockStaff.name) | Caster is an EntityPlayer. | The precondition itself adds no target check. This is not proof that every later cast action succeeds. |
| [Web Staff](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WebStaff.name) | At least one active potion whose isBadEffect flag is true. | This checks the game potion flag, not every possible harmful condition. Fire, hunger or a mod custom status is not automatically included. |

## Boxes are not spherical ranges

The hostile-area gates expand the caster's existing axis-aligned bounding box. Their 8, 10, 20 or 30 inputs are not a Euclidean sphere centered on a point. Lyonic is especially different: its expansion is **10, 1, 10**. The selected hostile predicates also do not perform a line-of-sight check themselves. Do not turn these input values into universal combat ranges or claim all effects pass through walls.

## The nine block-aiming gates

Celestial, Firestorm, Lightning, Lunar, Meteor, Moonlight, Nightmare, Striker and Tangle call the same aiming helper with **70**. The helper starts at the player's eye position, constructs an endpoint from yaw/pitch and that distance, then calls the world's block ray trace with the three boolean flags **true, true, false**. A null trace produces a null gate.

This is a block trace, not a creature-target selector. It is not a proof of clear sky, chunk readiness, projectile impact or an exact maximum damage distance. Any additional spell restrictions must be documented from the cast path separately.

## Coral's shell is a bounded placement search

Coral checks selected faces around the caster's block position using offsets −2 through 2, with different loop bounds for the face passes. Candidates must be exact vanilla AIR; for a player it also calls the provider's canMineBlock check. This does not establish full compatibility with arbitrary claim or protection mods, nor does it promise the later placement succeeds.

## Restoration tests worth preserving

- For all 29 custom gates, test one accepted and one rejected situation and verify no rune/wear/cooldown change on a rejected gate.
- Compare empty sky and block hits for all nine shared aiming cases.
- Test box corners and vertical separation instead of only straight-line distances.
- Check full, partial and zero health, effect-free players, Creative/spectator players and mod-specific immunity flags separately.
- Separate entry-gate behavior from cast effects, projectile spawns, healing, protection handling and multiplayer synchronization.

[29 exact preconditions and supporting method evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/staff-precondition-evidence-1.12.2.json) · [Per-staff reviewed gate summaries](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/staff-precondition-guide-1.12.2.json).
