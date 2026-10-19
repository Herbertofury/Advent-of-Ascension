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
| Abominator | [Original-inspired heavy weapon and alternate barrel exploration](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Abominator-Weapon-Profile) |
| Abyssro | [Compact two-pellet Spreadshot identity and Abyss-associated Mechyro upgrade lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Abyssro-Weapon-Profile) |
| Amplifier | [Five-pellet shotgun, successful-hit explosion hook and infusion recipe](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Amplifier-Weapon-Profile) |
| Apoco Assault Rifle | [Vox Ponds-associated upgrade lineage; organic styling remains interpretation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Assault-Rifle-Weapon-Profile) |
| Apoco Rifle | [Explosive Discharge Capsule identity with a refined organic shell](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Rifle-Weapon-Profile) |
| Apoco Shower | [Spirit-powered three-path discharge and pale front-shroud concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Apoco-Shower-Weapon-Profile) |
| Balloon Bomber | [Red-gold carnival cannon, Balloon ammunition and playful inspection storyboard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Balloon-Bomber-Weapon-Profile) |
| Baron SSR | [Red-brown Metal Slug sniper with historical Baroness loot evidence and restrained material/inspect concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Baron-SSR-Weapon-Profile) |
| Baronator | [Alternating upper/lower barrel presentation; preserve the grenade distinction](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Baronator-Weapon-Profile) |
| Blast Barrel | [Three-pellet explosive-hit shotgun with a historical Dawnlight Dungeon association and controlled amber concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blast-Barrel-Weapon-Profile) |
| Blue Barrel | [Three-pellet Seaside upgrade of Brown Blaster, cobalt material study and rear-mounted charm proposal](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blue-Barrel-Weapon-Profile) |
| Boulder | [Four-pellet Spreadshot identity, stepped stone-like silhouette and Demolisher upgrade](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boulder-Weapon-Profile) |
| Brown Blaster | [Three-pellet shotgun with illustrated infusion workflow and verified Seaside upgrade lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Brown-Blaster-Weapon-Profile) |
| Carrot Cannon | [Carrot ammunition, botanical shape and rootwork design](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Carrot-Cannon-Weapon-Profile) |
| Clown Cracker | [Carnival-colored Metal Slug sniper, seven-slot infusion and optional confetti inspect concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Clown-Cracker-Weapon-Profile) |
| Clownimator | [Three red crowns, corrected rear grip and maximum-health-based damage multiplier; pictured Decimator upgrade](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Clownimator-Weapon-Profile) |
| Clowno-Pulse | [Three red crowns, playful inspect concept and shooter-centered defensive pulse](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Clowno-Pulse-Weapon-Profile) |
| Crystaneer | [Jewel-cluster sniper with original scope overlay, illustrated conditional loot and inspect concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crystaneer-Weapon-Profile) |
| Dark Beast | [Fork-jawed dark Metal Slug sniper, pictured Darkly upgrade and revised material/inspection proposals](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dark-Beast-Weapon-Profile) |
| Deadlock | [Crimson stepped sniper, pictured infusion and directional target-movement rule](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Deadlock-Weapon-Profile) |
| Decimator | [Cream-gray sniper, maximum-health threshold below 50, five-slot infusion and pictured Clownimator progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Decimator-Weapon-Profile) |
| Destruction Shotgun | [Three pellets share one boosted-shot roll; infusion and Purity upgrade lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Destruction-Shotgun-Weapon-Profile) |
| Discharge Shotgun | [Owner-selected scattercaster target with original four-projectile behavior](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Discharge-Shotgun-Weapon-Profile) |
| Discharge Sniper | [Crimson capsule-powered sniper; pictured Divine upgrade, conditional explosion policy and unresolved original flight visuals](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Discharge-Sniper-Weapon-Profile) |
| Energy Cannon | [Blue split-jaw cannon, illustrated infusion recipe and mixed damage identity](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Energy-Cannon-Weapon-Profile) |
| Floro500 | [Magenta-green Metal Slug sniper with pictured Floro upgrade, finish variants and cosmetic petal inspection](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Floro500-Weapon-Profile) |
| Fungal Cannon | [Fungal silhouette and the original weakening-effect contract](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fungal-Cannon-Weapon-Profile) |
| Ghast Blaster | [Dark purple cannon, heavy shadow projectile and conditional withering effect](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ghast-Blaster-Weapon-Profile) |
| Gimmick | [Colorful ten-pellet Spreadshot weapon; expressive eye inspection is a new optional proposal](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gimmick-Weapon-Profile) |
| Ginger Blaster | [Five-pellet source behavior, illustrated infusion and partial confection-themed concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ginger-Blaster-Weapon-Profile) |
| Gravity Blaster | [Self-launch and hostile-control identity with gravity-focused upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gravity-Blaster-Weapon-Profile) |
| Hive Blaster | [Hive-inspired forms with original projectile and renderer caveats](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hive-Blaster-Weapon-Profile) |
| Hive Cracker | [Amber Lelyetian sniper upgrade with Metal Slug behavior and clearly labelled inspect concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hive-Cracker-Weapon-Profile) |
| Iominator | [Original green-spark identity; alternate feed-layout studies stay separate](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Iominator-Weapon-Profile) |
| KA-500 | [Cyan-orange Metal Slug sniper with pictured infusion recipe and Floro500 / Mark Maker upgrade routes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/KA-500-Weapon-Profile) |
| Long Shot | [Two-pellet shotgun with source-backed longer projectile lifetime and blue-petal concept details](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Long-Shot-Weapon-Profile) |
| Mark Maker | [Crimson Metal Slug sniper with pictured KA-500 and Moon Maker upgrade lineage, cosmetic inspect and impact proposals](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mark-Maker-Weapon-Profile) |
| Mecha Cannon | [Orange cannonball, mechanical shapeless crafting and proposed inspect gearing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mecha-Cannon-Weapon-Profile) |
| Mechyro | [Mechanical two-pellet shotgun, shapeless assembly and Abyssro upgrade lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mechyro-Weapon-Profile) |
| Mineral | [Compact rose/silver Metal Slug sniper, pictured Terminator + Rocky Kit upgrade and optional cosmetic lattice study](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mineral-Weapon-Profile) |
| Minigun | [Rotary weapon identity, purposeful moving parts and attachment studies](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Minigun-Weapon-Profile) |
| Monster | [Amber fork-jaw Metal Slug sniper, pictured Darkly upgrade and version-specific Graw loot evidence](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Monster-Weapon-Profile) |
| Moon Cannon | [Forked magenta cannon with mixed heavy/energy damage and Lunar kit lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Moon-Cannon-Weapon-Profile) |
| Moon Maker | [Magenta Lunar upgrade, actual Metal Slug texture and pink sparkler renderer audit with offhand regression target](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Moon-Maker-Weapon-Profile) |
| Predatorian Blaster | [Compact bone cannon concept, paired yellow nodes and Ghast Blaster upgrade lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Predatorian-Blaster-Weapon-Profile) |
| Pulse Cannon | [Rectangular magenta cannon and a separate shooter-centered hostile repulsion pulse](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Pulse-Cannon-Weapon-Profile) |
| Purity Shotgun | [Blue-armored Destruction upgrade, three pellets and a shared boosted-shot roll](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Purity-Shotgun-Weapon-Profile) |
| Purple Punisher | [Two-pellet Haunted upgrade of Red Rocket with violet material and inspection concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Purple-Punisher-Weapon-Profile) |
| Red Rocket | [Crimson two-pellet shotgun, five-slot infusion and verified Haunted upgrade lineage; no baseline rocket behavior](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Red-Rocket-Weapon-Profile) |
| Rosid Rifle | [Botanical sniper identity; friendly-Rosid tooltip differs from empty inspected impact hook](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Rosid-Rifle-Weapon-Profile) |
| Sabbath | [Violet-teal sniper, Wither I impact request, six-slot infusion and corrected smooth-guard concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sabbath-Weapon-Profile) |
| Shoe Flinger | [Boot ammunition, playful launch effects and equipment conservation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Shoe-Flinger-Weapon-Profile) |
| Sludge Sniper | [Green-olive Metal Slug sniper with seven-slot infusion and verified Slowness II / Poison I source semantics](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sludge-Sniper-Weapon-Profile) |
| Soul Drainer | [Life-leech identity with an unmistakable soul-energy presentation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Drainer-Weapon-Profile) |
| Soul Storm | [Five-emitter Soul Flame sight study; the default upgrade has four emitters, with five/six as options](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile) |
| Spirit Shower | [Three descending Spirit projectiles, source-linked loot and Apoco upgrade](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Spirit-Shower-Weapon-Profile) |
| Sweet Tooth | [Chocolate, peppermint and icing sniper; pictured infusion and shooter-only Speed III successful-hit audit; grip revisions retained](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sweet-Tooth-Weapon-Profile) |
| Terminator | [Charcoal/silver sniper, SCOPE_3, eight-slot infusion and Mineral upgrade lineage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Terminator-Weapon-Profile) |
| Vivo | [Compact three-pellet shotgun with gold accents, Lyon infusion and a higher-pitched firing identity](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vivo-Weapon-Profile) |
| Duster | [Dark-brown/teal identity, inherited scope and six-slot infusion](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Duster-Weapon-Profile) |
| Bolt Rifle | [Ochre/charcoal sniper, inherited scope and seven-slot infusion](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bolt-Rifle-Weapon-Profile) |
| Dual Sight | [Cyan/blue scope identity, six-slot infusion and revised guard concept](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dual-Sight-Weapon-Profile) |
| Head Hunter | [Brown/cobalt sniper, precise hit-band and cooldown source contract](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Head-Hunter-Weapon-Profile) |
| Viper-1 | [Warm brown-black sniper, pictured infusion and Poison II source contract](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Viper-1-Weapon-Profile) |
| Vortex Blaster | [Spirit-powered repulsion and readable vortex-focused feedback](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vortex-Blaster-Weapon-Profile) |

The gallery currently contains **65 published concept/source profiles out of 228 first-target firearm registrations**. No upgraded weapon has passed full native acceptance. Other families and historical releases remain additional scope.

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

## Baron SSR: original identity and historical acquisition

[Baron SSR weapon profile](Baron-SSR-Weapon-Profile) preserves the red-brown/dark silhouette, Metal Slug sniper behavior and version-specific Baroness loot evidence. Its new material, inspection and VFX sheet remains a partial concept study with native acceptance open.

## Dark Beast: compact dark sniper upgrade

[Dark Beast weapon profile](Dark-Beast-Weapon-Profile) documents its Monster + Darkly kit lineage, heavy Metal Slug sniper behavior and revised compact concept. The overlong first concept is retained as a rejected canonical direction.

## Every bundled upgrade, pictured

[Divine Station illustrated upgrade atlas](Divine-Station-Upgrade-Atlas) covers all 70 bundled upgrade-kit recipes, organized by 19 kit families, with exact base item, kit and output sprites. First frames are used for animated textures; diagrams are not native screenshots.

## Monster: amber fork-jaw sniper

[Monster weapon profile](Monster-Weapon-Profile) retains the orange/charcoal forked silhouette and documents the pictured Darkly upgrade. Historical Graw loot evidence is kept separate from the unresolved current acquisition route.

## Floro500: magenta-green botanical sniper

[Floro500 weapon profile](Floro500-Weapon-Profile) documents the KA-500 + Floro kit upgrade, original Metal Slug behavior, source-color identity and proposed finish/inspection art. Historical kit-drop associations remain version-scoped.


### KA-500: cyan-orange sniper and two upgrade routes

[Source profile, pictured infusion and concept](KA-500-Weapon-Profile) covers the Metal Slug baseline, SCOPE_4, Floro500 and Mark Maker recipes, and a compact cosmetic direction. Native gameplay and full-feature acceptance remain open.


### Mark Maker: crimson upgrade lineage

[Source profile, concept and illustrated recipes](Mark-Maker-Weapon-Profile) follows KA-500 → Mark Maker → Moon Maker. The crimson cosmetic impact is a proposal; no enemy-marking or explosion behavior is inferred from the name. Native acceptance remains open.


### Moon Maker: actual projectile and render-loop evidence

[Moon Maker source profile and concept](Moon-Maker-Weapon-Profile) preserves its magenta/green identity, shows the extracted Metal Slug texture and documents its pink-sparkler renderer. Offhand attribution and render-rate emission are explicit native regression targets. No native acceptance is promoted.


### Sludge Sniper: preserving actual debuff levels

[Source profile, seven-slot infusion and concept](Sludge-Sniper-Weapon-Profile) preserves the green/olive identity and audits Slowness II plus Poison I against the released class, named source and bundled EffectsLib level conversion. Decorative vapor and impact mist remain presentation proposals. Native acceptance remains open.


### Sweet Tooth: candy identity and shooter-only speed reward

[Source profile, infusion recipe and revised concepts](Sweet-Tooth-Weapon-Profile) documents Speed III on a successful hit, preserves earlier rejected grip layouts and separates the cosmetic inspection flourish from server-authoritative rewards. Native acceptance remains open.


### Discharge Sniper: capsule and explosion contract

[Source profile, Divine recipe and concept](Discharge-Sniper-Weapon-Profile) distinguishes Discharge Capsules from Metal Slugs, documents conditional terrain interaction, and flags the empty particle-renderer hook and offhand constructor for native tests. New glowing-flight art remains a proposal.


### Mineral: preserve the rose-colored Rocky upgrade

[Source profile, illustrated Divine recipe and concept](Mineral-Weapon-Profile) retains the compact rose/silver/red silhouette and Metal Slug baseline. Optional lattice and red-dust effects are visual proposals, not inferred mining or loot mechanics.

### Camo Rifle: source study while artwork is pending

[Camouflage contract and pictured infusion](Camo-Rifle-Mechanics-Study) documents the server-only selected-slot, shift-held invisibility refresh. This source-only page is not counted as an illustrated upgrade concept and does not certify native behavior.
