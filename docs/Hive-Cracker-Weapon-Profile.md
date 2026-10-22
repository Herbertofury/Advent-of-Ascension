# Hive Cracker: the amber Lelyetian sniper upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Current selected concept · 22 October 2026

![Hive Cracker selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-cracker-dimensional-concept-v3.png)

Otherworldly amber hive-cell, hooked antenna forms and charcoal structure develop the original orange/yellow identity. Previous sheet remains a past concept. Crest size, rear silhouette and native readability need further review; no new attack behavior is claimed. Separate action study proposes visible bees moving during charge/fire and two optional sights: a bee-formed aperture or a honey aperture rapidly assembled by bees on aim. Static state panels only; no native animation is implemented. Additional Moonlit Hive craftable variant proposed with soul-blue bees and optional swarm or honey sights. Existing base remains available; recipe and native behavior are not implemented.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Ahive_cracker). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

Dedicated supplemental studies (partial design candidates, not implemented features):

- [Separate action study: visible hive bees, swarm sight and honey-built sight](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-cracker-bee-action-sights-study-v1.png).
- [Shared hive-family charm concepts; fit and animation unverified](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-family-charms-study-v1.png).
- [Shared Moonlit swarm and honey sight animation directions; individual host fit unverified](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moonlit-hive-soul-bee-sights-study-v1.png).
- [Shared soul bees inside chambers: rest, charge, release and recovery; effects are proposals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moonlit-hive-living-chambers-study-v1.png).
- [Shared soul-campfire-inspired crafting proposal, illustrated with Hiver; use matching input weapon, preserve saved data](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/moonlit-hive-crafting-study-v1.png).
- [Optional amber and additional Moonlit confirmed-defeat effects: honeycomb motes or bee-shaped particles with off option; no extra entities, damage or loot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-amber-moonlit-defeat-effects-study-v1.png).

## Released role

Hive Cracker inherits **BaseSniper** and uses Metal Slug ammunition. The inspected subclass declares its constructor, medium-rifle/long firing-sound selection and SCOPE_4 texture selection. It does not declare a unique impact hook. The name is not evidence that it launches bees, creates a swarm or deals honey damage; it is also distinct from Hive Blaster.

| Stored field | Clown Cracker | Hive Cracker |
|---|---:|---:|
| Damage input | 33.5 | 44.0 |
| Durability | 305 | 555 |
| Shot delay | 84 ticks | 84 ticks |
| Recoil input | Approximately 0.05 | Approximately 0.035 |

These are constructor inputs, not guaranteed final damage or physical measurements. At 20 TPS, 84 ticks is nominally 4.2 seconds. The checked upgrade retains its delay while increasing damage/durability and reducing its recoil input. Native sniper handling and resource behavior remain authoritative.

## Original identity

![Actual released Hive Cracker sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-cracker-original-preview.png)

Preserve the burnt-orange/brown body, warm yellow front region, raised orange top housing and short dark-gray rear/grip structures. The verified Lelyetian association comes from its upgrade kit. Amber ceramic-like materials and honeycomb decorative relief are new artistic interpretations, not a documented manufacturing process or biological mechanism.

## Upgrade recipe

At the **Divine Station**, place Clown Cracker in the left input and a Lelyetian Upgrade Kit in the middle input; the result is Hive Cracker. The exact bundled definition is `data/aoa3/recipes/upgrade_kit_hive_cracker.json`.

The recipe does not establish a particular kit drop location. Base assembly produces the declared output rather than promising arbitrary names, enchantments or third-party customization survive. Define attachment transfer explicitly and test valuable customization on a disposable copy.

[Illustrated Divine Station workflow](Divine-Station-Weapon-Upgrades-1.20.1) · [Exact recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=upgrade_kit_hive_cracker)

## Earlier preserved art: Premium concept and QA correction

![Hive Cracker hero, side profile, material details, two proposed texture treatments and inspect vignette](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/hive-cracker-concept-v2.png)

The concept keeps the orange/yellow/dark-gray palette and stepped silhouette. Its honeycomb surfaces are decorative proposals. The low-resolution inset is a generated style interpretation, not the actual source sprite shown above or a finished texture atlas.

The first generated sheet incorrectly labeled a painted inspect vignette “in-game” and attributed a particular metalworking style to Lelyetia. Those labels were corrected before publication. Earlier art remains preserved locally. The current inspect vignette is a proposal; it cannot establish animation, hand fit or native rendering quality.

The proposed grip/control geometry and protruding upper details require actual hand-rig and motion clearance checks. An attractive static render does not pass those tests.

## Full feature plan

- **Firing feel:** preserve the original deliberate sniper cadence and Metal Slug resource path. The lower stored recoil input than Clown Cracker should not become an unreviewed rate-of-fire change.
- **Sight:** retain the original SCOPE_4 behavior as an option, with alternate optics subject to camera alignment and visibility tests. [Original overlay illustration](Crystaneer-Weapon-Profile#original-silhouette-and-sight) uses the same released texture, not evidence of identical complete handling.
- **Attachments:** compact/steady handling conversions, different fore-ends and alternate sight housings. A hypothetical swarm-themed conversion would be a separately designed functional upgrade, not original behavior.
- **Materials:** Minecraft-fit and premium amber treatments share mechanics and recognizable shape. Make the yellow/orange contrast legible without excessive bloom or mandatory dynamic lights.
- **Inspection:** tilt the closed weapon to reveal surface detail, then settle into aim. Interruptions cannot change resources or leave hands stuck.
- **Animation:** equip, idle, aim, fire, recovery, optional reload and inspection in first/third person, including cancellation, swaps and handedness.
- **Resources:** original Metal Slug support, optional reload only when explicitly selected. Any magazine or charge conversion needs defined mechanics and cancellation rules.
- **Effects:** capture original shot, muzzle, flight, impact and audio first. New tracer/impact/decal/finisher choices remain separate from authoritative damage, loot and kill credit.
- **Customization:** earned functional charms, skins, stickers, animated/glowing emblems and explicit attachment stats, with clearances around hands and controls.
- **Upgrade/dismantling:** preserve or return incompatible attachments safely, including full inventories. Test persistence, multiplayer ownership and repeated upgrade actions.
- **Performance:** cached configuration, LODs, bounded effect budgets and measured frame-time lows on the intended mod stack.

## Acceptance gates

- [ ] Original native scope, projectile, impact, sound and resource captures
- [ ] Complete attachment, muzzle, projectile, impact, decal and finisher concepts
- [ ] Real hand clearance, coherent proportions and two texture modes
- [ ] Full animation/interruption and Lelyetian customization-transfer tests
- [ ] Native export, multiplayer, persistence, dismantling and performance qualification

[Released source and upgrade evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/hive-cracker-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](Effective-Recoil-Routing-1.20.1).
