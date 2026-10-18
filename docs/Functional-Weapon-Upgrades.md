# Functional upgrades: the original is the baseline, not the ceiling

**Owner direction,18 October2026.** Premium TaCZ/AoA upgrades may intentionally multiply projectiles, increase damage, change firing patterns, resource capacity, handling, flight and special effects. A visually meaningful modification should have the corresponding declared gameplay meaning. This supersedes earlier baseline-only wording where it would prohibit deliberate upgrades.

## Three distinct things

1. **Original mode:** reproduce the original version's weapon and document its actual behavior.
2. **Upgraded gameplay:** installed components deliberately change the build's effective statistics and behavior.
3. **Cosmetics:** explicitly cosmetic skins, inlays or settings can change presentation without pretending to change gameplay.

Do not confuse intentional multishot with accidental duplicate callbacks. The first is a requested feature; the second remains a bug. Similarly, documented resource-efficiency upgrades are allowed; unaccounted resource duplication is not an upgrade.

## Make the appearance tell the truth

- More active emitters can mean more discs, denser sequences, bursts or volleys.
- Larger or specialized discharge modules can alter damage, projectile size, impact area or pattern when the module declares that effect.
- Sights, grips, braces and support systems can meaningfully affect aim, handling and recovery.
- Reservoirs and feed modules can change capacity, consumption policy or sustained-fire behavior.
- Recovered effect cores can add eligible special behavior to another weapon through an explicit adapter.
- Tooltips, workbench preview, rendered assembly and server-authoritative behavior must use the same resolved build definition.

Not every upgrade needs a forced drawback. Balance, progression, survival recipes and optional sandbox rules should support experimentation and fun. Compatibility and stability still require finite values, correct ownership, bounded effects and safe saved data.

## Soul Storm: modular plasma-disc stacks

The requested presentation is a top-to-bottom sequence of plasma-soul discs from independently pulsing stacked emitters. Initial concepts cover four, five and six emitters, with an extensible stack family. The original sprite has five bright horizontal bands; the native inspected firing method creates a projectile from the shooter, not a separate native muzzle for each pixel-art band.

A five/six/higher stack can genuinely fire more discs or support different patterns. Do not hold upgraded output to the unmodified weapon's ceiling. Choose and display its actual cadence, per-disc damage, resource policy and collision/impact behavior. Keep original-mode values separately available.

[Original and upgraded Soul Storm profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile) · [Attachment gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Attachment-Concept-Gallery) · [Modular armory architecture](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage)

## Implementation contract

Resolve an immutable build snapshot from item identity, installed parts and assembly revision. The same snapshot defines projectile count, scheduling, damage, costs, rendered emitters, muzzle transforms and effect budgets. Authoritative accepted attacks create the intended number of projectiles; retries or duplicate packets must not create additional ones. Preserve original item data and reversible assembly changes.

For every published build show original versus proposed versus measured values. Planned numbers are not benchmark results or proof that an adapter exists. Validate hit detection, impact ownership, resource transactions, multiplayer and frame/tick performance in the real game.
