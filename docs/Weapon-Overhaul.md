![The Ascension Armory](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-upgrade-banner.svg)

**Mandatory for every weapon:** [Complete feature, concept-fidelity and QA standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard). All 31 feature groups require separate concept/design, implementation and QA status; no silent omissions or concept-mismatch passes.

# Every weapon, elevated

**Owner-approved project goal · implementation pending · no runtime performance claim.**

Every accepted AoA weapon should offer an optional premium, fully animated 3D remodel. The quality bar is the strongest TaCZ and Bedrock weapon presentations: convincing moving mechanisms, satisfying reloads, expressive inspection, weighty firing, readable sights and polished first- and third-person animation. Preserve each weapon's AoA identity instead of replacing the arsenal with generic modern guns.

[Reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Implementation checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog) · [Original item atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Items-Atlas)

## Reproduce the authoring checks

[Run the 21 scoped test suites from clean source archives](Weapon-Authoring-Reproducibility). Includes exact input hashes and the corrected Baronator fixture packaging. These are authoring checks, not native game or visual-quality acceptance.

[Search all 228 first-target weapon implementations](Weapon-Implementation-Map): actual class chains, declared methods and source hashes. Structural coverage is not finished model/gameplay coverage.

[Reusable Java presentation core](Weapon-Presentation-Core): sight timing, branch-aware cosmetic events and bounded game-time emission. Pure-core tests pass; native integration and visual acceptance remain open.

[Illustrated Divine Station upgrades for 1.20.1](Divine-Station-Weapon-Upgrades-1.20.1): all 70 shipped routes, exact ingredients, source sprites and customization-preservation caveats.

[Ammunition Desk for 1.20.1](Weapon-Ammunition-1.20.1): illustrated lookup for 172 conventional weapon IDs and 13 base ammo identities, resolved through inherited methods. Net consumption and effects remain separate contracts.

## Explore the weapon profiles

[Browse the illustrated Ascension Armory](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?revision=fae99f4): searchable concept cards beside the actual released sprites, full-size artwork, source profiles and available interactive authoring studies. The gallery explicitly distinguishes design coverage from native weapon acceptance.


| Weapon | Read the original behavior and proposed upgrade |
|---|---|
| Soul Storm | [Full profile](Soul-Storm-Weapon-Profile) · [Soul Flame default sight](Soul-Storm-Sights) |
| Balloon Bomber | [Carnival concept, Balloon ammunition, impact behavior and inspection storyboard](Balloon-Bomber-Weapon-Profile) |
| Baronator | [Full profile, alternating barrels and bonus grenade distinction](Baronator-Weapon-Profile) |
| Minigun | [Full profile, rotary identity and native acquisition](Minigun-Weapon-Profile) |
| Abominator | [Full profile and original-inspired concept](Abominator-Weapon-Profile) |
| Soul Drainer | [Full profile and life-leech contract](Soul-Drainer-Weapon-Profile) |
| Fungal Cannon | [Full profile, native weakening effect and original projectile comparison](Fungal-Cannon-Weapon-Profile) |
| Discharge Shotgun | [Full profile, two-stage impact and upgrade concepts](Discharge-Shotgun-Weapon-Profile) |
| Vortex Blaster | [Spirit-powered repulsion, original targeting and concepts](Vortex-Blaster-Weapon-Profile) |
| Ghast Blaster | [Dark purple cannon, shadow projectile, conditional withering and infusion lineage](Ghast-Blaster-Weapon-Profile) |
| Gravity Blaster | [Self-launch, nearby hostile control, infusion and upgrade concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gravity-Blaster-Weapon-Profile) |
| Predatorian Blaster | [Bone cannon concept, withering source contract and Ghast upgrade lineage](Predatorian-Blaster-Weapon-Profile) |
| Gimmick | [Ten-pellet scattergun, colorful silhouette and optional inspection](Gimmick-Weapon-Profile) |
| Long Shot | [Two-pellet extended-range source path, infusion and blue-petal concept](Long-Shot-Weapon-Profile) |
| Blue Barrel | [Three-pellet Seaside upgrade, cobalt material study and rear-charm proposal](Blue-Barrel-Weapon-Profile) |
| Vivo | [Compact gold-and-charcoal shotgun, Lyon infusion and three-pellet source behavior](Vivo-Weapon-Profile) |
| Ginger Blaster | [Five-pellet source, illustrated infusion and partial confection concept](Ginger-Blaster-Weapon-Profile) |
| Boulder | [Four pellets, gray/crimson identity and Rocky upgrade recipe](Boulder-Weapon-Profile) |
| Purity Shotgun | [Blue-armored upgrade, shared boost and illustrated kit recipe](Purity-Shotgun-Weapon-Profile) |
| Destruction Shotgun | [Three-pellet shared boosted-shot roll and infusion](Destruction-Shotgun-Weapon-Profile) |
| Amplifier | [Five-pellet shotgun, explosive-hit gate and infusion recipe](Amplifier-Weapon-Profile) |
| Mecha Cannon | [Orange cannonball and mechanical crafting lineage](Mecha-Cannon-Weapon-Profile) |
| Mechyro | [Mechanical two-pellet shotgun, crafting and Abyssro upgrade lineage](Mechyro-Weapon-Profile) |
| Abyssro | [Compact two-pellet shotgun and Abyss-associated upgrade lineage](Abyssro-Weapon-Profile) |
| Clowno-Pulse | [Three-crown concept, Pulse upgrade and defensive firing pulse](Clowno-Pulse-Weapon-Profile) |
| Pulse Cannon | [Rectangular cannon concept with separate shooter-centered repulsion](Pulse-Cannon-Weapon-Profile) |
| Rosid Rifle | [Botanical sniper concept, Metal Slugs and tooltip-versus-impact-hook discrepancy](Rosid-Rifle-Weapon-Profile) |
| Shoe Flinger | [Full profile, boot ammunition and equipment conservation](Shoe-Flinger-Weapon-Profile) |
| Iominator | [Full profile, green-spark projectile and Ancient Kit upgrade](Iominator-Weapon-Profile) |
| Hive Blaster | [Full profile, renderer caveats and upgrade concepts](Hive-Blaster-Weapon-Profile) |
| Apoco Assault Rifle | [Source-pinned upgrade lineage, Vox Ponds kit association and concept review](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Assault-Rifle-Weapon-Profile) |
| Apoco Rifle | [Distinct Discharge Rifle upgrade, explosive capsule behavior and refined concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Rifle-Weapon-Profile) |
| Apoco Shower | [Spirit-powered three-path discharge, conditional impacts and front-shroud concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Shower-Weapon-Profile) |
| Energy Cannon | [Blue forked cannon, illustrated infusion recipe and Lunar upgrade](Energy-Cannon-Weapon-Profile) |
| Moon Cannon | [Forked magenta identity, heavy/energy damage split and Lunar kit lineage](Moon-Cannon-Weapon-Profile) |
| Spirit Shower | [Three-path Spirit attack, Jawe loot-table evidence and Apoco upgrade](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Spirit-Shower-Weapon-Profile) |
| Carrot Cannon | [Carrot ammunition, botanical material provenance, concepts and unaccepted authoring](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Carrot-Cannon-Weapon-Profile) |

The 31 weapons listed above have published concepts and source-backed profiles; none is a fully accepted native upgraded weapon. The first-release production inventory contains 228 gun/shotgun/sniper/cannon/blaster registrations; other families and historical releases are additional scope.

## Build your own identity and play style

[Functional upgrades](Functional-Weapon-Upgrades) may deliberately multiply projectiles, increase damage and change behavior through declared parts. The original is the baseline, not the ceiling. [Alternate barrels and skins](Alternate-Barrels-and-Skins) keep each weapon distinctive. [Earned charms, effects, stickers and emblems](Weapon-Charms-and-Effect-Customization) add boss/achievement progression, functional charm bonuses, custom finishers, projectile/tracer/impact styles and static, animated or glowing decals. Preserve previous concept versions and distinguish proposals from measured native results.

## Choose your presentation

| Control | Required behavior |
|---|---|
| Global default | Original AoA or premium 3D; change without destroying existing items or saves |
| Weapon-family override | Configure guns, bows, magical weapons and other families independently |
| Individual weapon override | Every supported weapon can independently return to its original appearance |
| Missing optional integration | Original mode remains usable; explain the unavailable enhancement |
| Server gameplay policy | Damage, ammunition and reload rules remain authoritative and explicit |

Presentation changes must not silently alter damage, ammo economy, skill requirements, projectile effects, enchantments, progression or existing item identity. A magazine-based gameplay conversion is a separate, opt-in rule set. Cosmetic reload animation alone must never imply ammunition was consumed or replenished.

## Reloading is optional

**Owner requirement:** premium 3D models and animations must work with reloads disabled. Reloading is an independent per-weapon option, not a prerequisite for the visual upgrade. Default to each original weapon's actual resource system: mana, energy, ammunition or another native cost. Do not add magazines, manual reload input, reload delays or artificial downtime to weapons that do not normally have them.

When enabled, optional reload/recharge mechanics must be clearly described and server-approved. A mana weapon may have a purely cosmetic casting or energy-flow animation without a reload action. Players can use the full premium remodel, firing, aiming and inspection quality while retaining original firing behavior. Disabling optional reloads must preserve valid resource state and cannot grant free ammo or mana.

## An arsenal, not one repeated animation

- **Magazine weapons:** tactical and empty reloads, believable magazine handling, correct remaining-round state.
- **Per-round weapons:** shell or round insertion with interrupt-safe timing.
- **Bolt, pump and heavy weapons:** distinctive mechanisms, recovery and handling weight.
- **Energy and magical weapons:** preserve native mana/energy behavior; optional recharge, vent, crystal replacement or rearming only when appropriate and explicitly enabled.
- **Bows and crossbows:** draw, tension, nocking/loading and release that preserve native mechanics.
- **Melee and unusual weapons:** appropriate ready, attack, inspect and recovery animations; do not invent a magazine where none belongs.

A weapon is complete only when its remodel, texture/materials, first-person pose, third-person pose, firing effects, sound and all applicable animation states are finished together.

## Animation and visual acceptance

Equip, holster, idle, aim, fire, recoil, inspect and relevant reload/charge states must blend without hand clipping, camera jumps or sudden pose resets. Include empty inspection and interrupted reload behavior where applicable. Test left-handed view, multiple FOVs, sprinting, swimming, riding, resource packs and supported shaders. Provide reduced camera-motion and effects options.

Maintain recognizable silhouettes, colors, lore and exaggerated fantasy mechanisms. Use strong art direction before increasing polygon counts. Every upgraded weapon needs a labeled comparison image and a short animation showcase, with the exact build and asset provenance recorded.

## Technical direction

Use a shared weapon manifest and version-specific presentation/runtime adapters. Investigate contribution to existing TaCZ tools and compatible gunpack pipelines before writing duplicate infrastructure. The verified official TaCZ baseline is Forge 1.20.1; its existence does not establish a working backend for every historical AoA or future loader version.

Keep the backend optional. A failed asset or absent TaCZ must produce a clear fallback, not corrupt or permanently replace original AoA items. Separate presentation state from server simulation. The server commits shots, ammo changes and reload completion; animation events cannot grant ammunition on their own.

Test reload cancellation through weapon swaps, drops, death, reconnects and dimension changes. Never duplicate rounds or lose special AoA properties during conversion, save/reload or multiplayer synchronization.

## Performance is a release gate

Measure startup, asset memory, CPU/GPU frame time and low-percentile performance against the same world, settings and original presentation. Load equipped/visible assets lazily, use distance-appropriate detail, bounded caches and shared immutable resources. Avoid per-frame pack scans and unnecessary animation ticks for invisible weapons. Provide a lightweight tier while keeping the premium option available.

No-loss performance and compatibility are acceptance targets requiring measurements, not promises established by these documents. Publish the hardware, scene, sample duration and before/after results with each milestone.

## Definition of complete

One traceable record per accepted weapon and source version: registry ID, original behavior, model/texture ownership, animations, backend/version support, fallback, conversion policy, screenshots, multiplayer tests and performance evidence. An unchecked or unsupported weapon remains visible in the coverage ledger.

[Reproducible Predatorian and Pulse source checks](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/predatorian-pulse-source-study.zip) verify narrow pinned bytecode markers and recipe structure; they do not certify gameplay or final art.
