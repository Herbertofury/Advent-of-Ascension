# Modular Armory & Effect Salvage

**Current gameplay direction:** original behavior is the baseline, not the ceiling. Attachments may intentionally increase damage/projectile count and change firing patterns, resources and effects. See [Functional weapon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades). Accidental duplicate callbacks remain bugs; deliberate multishot is a feature.


> **Requested design target, not a shipped feature.** Updated 18 October 2026. Forge 1.20.1 is the first implementation target. All gameplay examples below are proposals; native AoA, TaCZ and compatibility tests are still required.

[Weapon mechanism & QA](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Mechanism-and-Animation-QA) · [Compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Baronator authoring prototype](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Animated-Weapon-Prototype-Baronator)

## The fantasy

Find a weapon you love. Keep its identity, rebuild its handling and appearance, recover a remarkable effect from another discovery, and create a personal hybrid that genuinely behaves differently. Let the bench show the result before spending anything. Exploration should keep producing useful parts and experiments instead of merely stronger numbers.

This must be an extensive, enjoyable system: barrels, scopes, suppressors, handling, stocks, grips, resource systems, special effects and cosmetic customization. AoA's strange weapons and dimensions should make it more imaginative than a conventional attachment menu.

## Concept-first attachment playground

[Explore the 24 initial attachment concepts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Attachment-Concept-Gallery): Soul Storm modules, Baronator upgrades and cross-weapon effect/cosmetic collectibles, including imagined assembled loadouts. These establish art targets, not working modules or qualified fits.

## First visual assembly study

[Open the interactive part-fitting lab](https://herbertofury.github.io/Advent-of-Ascension/baronator-attachment-lab.html) · [Editable original source](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/baronator-attachment-study.zip) · [Scoped clearance receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/baronator-attachment-clearance-qa.json)

![Original authoring renders: base Baronator, prism sight layout, and prism with dual external runic housings](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/baronator-attachment-comparison.webp)

This is a **visual blockout**, not functional optics, sound suppression, crafting or effect transfer. Six assemblies combine the base or prism sight with standard, upper or dual external runic-damper housings. The housings are fictional exterior game art, not real device internals. Moving modules follow their barrel; visual muzzle locators move to the selected tips. Native aiming/FOV, gameplay attributes, final materials and all runtime behavior remain open.

The first sight mount intersected the roof sled. The regression caught it before publication; the revised rear-anchored mount clears its travel without shrinking the sled or hand space. The rejected mount remains a negative fixture. The scoped test checks 1,092 poses per assembly (6,552 total), plus static module bore corridors, with no reported intersections in its covered pairs. These samples are not continuous-collision or native-game certification.

The live viewer's six selections, repeated switching, part counts, pause/scrub and hand-exchange inspection were checked in cloud Chrome. Compact module definitions reduce the self-contained viewer from 334,644 to 75,653 bytes; reconstructed assemblies match the full exports exactly and repeat selections reuse cached models. This is a payload improvement, not a measured Minecraft FPS claim.


## What the Fallout research establishes

| Reference | What the author documents | Lesson for AoA |
|---|---|---|
| [Any Mod Any Weapon](https://www.nexusmods.com/fallout4/mods/4515) | Cross-weapon attachments, inherited base behavior, and warnings about broken/ugly combinations or negative attributes | Keep the experimentation; require coherent adapters, sane values and visible assembly checks |
| [Legendary Effect Overhaul](https://www.nexusmods.com/fallout4/mods/66900) | Detaching a particular effect as a loose mod; separately scrapping items for crafting currency; additional effect slots | Separate recovering a specific effect from recycling an unwanted item. Explain every active effect |
| [Legendary Modifier Framework](https://www.nexusmods.com/fallout4/mods/62513) | Effect swapping through attachment points and modular equipment changes | Use a small extensible interface. Its posted permissions prohibit conversion to another game; this is conceptual research only |
| [Equipment and Crafting Overhaul Redux](https://www.nexusmods.com/fallout4/mods/67679) | Configurable workbench/equipment features, separated from LEO; some tuning tools are not balanced progression | Separate the core framework, optional adapters, survival recipes and sandbox tuning |

These are primary author-page reviews, not an audit of their executable plugins or an assertion that their features are vanilla Fallout 4. No Fallout assets or code are being copied. Recheck exact versions and permissions before any reuse. The [2015 Xbox presentation](https://news.xbox.com/en-us/2015/06/18/games-return-to-the-wasteland-in-style-with-fallout-4/) establishes the broad base-weapon/customization design inspiration; the community systems above supply additional, distinct ideas.

## How Fallout's record structure informs the design

Static inspection of [xEdit's Fallout 4 record definitions](https://github.com/TES5Edit/TES5Edit/blob/9fb016884bec138ea6c7b872cec831537d464c3e/Core/wbDefinitionsFO4.pas), pinned at `9fb016884bec138ea6c7b872cec831537d464c3e`, shows that an Object Modification record separates its attach point, parent-slot keywords, properties, target/filter keywords, included modifications and loose-mod reference. This is tool-source evidence about the data format, not execution of Fallout 4 or proof that every combination behaves correctly.

For AoA, the useful architectural inference is to keep the installed module definition distinct from the inventory object representing a recovered part. Compatibility, appearance, effect behavior and crafting acquisition should also be separate data concerns. This makes reversible extraction and adapters feasible without turning every possible combination into a new hard-coded weapon item. Preserve explicit precedence and provenance; a collection of IDs alone does not establish a safe effect composition.

## Full customization scope

| Area | Player choices | Required visible or gameplay feedback |
|---|---|---|
| Barrel / emitter | Length/style families, split emitters, alternate firing layouts | Changed silhouette, correct muzzle positions, supported projectile pattern and handling trade-offs |
| Sights / scopes | Iron sights, magnification, reticles, themed lenses | Accurate aim alignment, readable zoom/FOV options, no blocked sight picture |
| Muzzle | Suppressors, flash control, themed discharge shapers | Sound and flash changes with clear limits; suppressors do not mean absolute silence or automatically conceal magical effects |
| Stock / shoulder support | Compact, stable, heavy, folding visual families | Handling/recovery identity, hand fit and collision-safe animation |
| Grip / fore-end | Grip styles, support grips, weight distribution | Aim acquisition, sway and movement-handling changes; preserved finger room |
| Feed / magazine / conduit | Appropriate magazine families or resource-channeling parts | Correct native resource, capacity, reload/recharge rules and believable transfer route |
| Action / firing mode | Supported semi, burst, automatic, alternating or charge behavior | Clear control explanation and server-confirmed cadence; never an unsupported silent conversion |
| Cooling / charge | Recovery, heat expression and magical charge modules | Clear readiness state and intentional trade-offs, not unlimited free output |
| Special-effect cores | Recovered native effects and authored new effects | Trigger, chance, eligible targets, resource cost, cooldown and stacking shown |
| Cosmetics | Material palettes, skins, decals, engraving, name, emissive accents | Preview at actual scale; cosmetics cannot secretly change combat statistics |
| Sound / particles | Weapon-appropriate curated variants | Distinct identity, bounded particles, shake/flash reduction and distance behavior |
| Utility | Supported illumination or information modules | Optional controls, performance budget and explicit compatibility |

Handling needs more than one opaque score. Show aim time, sway, recoil recovery, movement while aiming, ready/holster time, reload or recharge time, and the practical consequence of weight. Display only attributes that the active implementation actually supports.

## The bench experience

1. Choose a weapon and rotate/zoom its live preview. Inspect its native identity, resource and effects.
2. Select a visible part or a searchable slot list. Filter by owned, craftable, unlockable, compatible or adapter-required.
3. Preview a candidate with before/after statistics, animation sample, sound sample and an explanation of conflicts.
4. Compare a saved blueprint against the current build. Show what is missing and where its recipe or discovery comes from.
5. Show the exact cost and outputs before committing. Commit once on the server, with an inventory revision check.
6. Try the result in a contained practice setting. Reset the preview without spending resources; actual gameplay never awards damage or ammunition from the preview.

Support keyboard/controller navigation, readable text scaling, reduced motion, color-independent conflict labels, search by effect, and favorite/protected items. Show all effects, not only the first legendary-looking line. Offer named loadout blueprints without duplicating items.

## Four different salvage operations

- **Detach:** keep a reusable physical part; replace the slot with its valid base/default part where appropriate.
- **Extract effect:** recover the specific selected effect as a provenance-bearing core. Show whether the donor survives and any explicit cost; default design should favor experimentation rather than hidden destruction.
- **Dismantle:** intentionally consume a chosen weapon for an exact list of recoverable parts/effects/materials, excluding mutually incompatible double rewards.
- **Recycle:** turn unwanted parts or cores into crafting material, with a clear irreversible-output preview.

Never silently destroy a favorite, consume a donor before checking output capacity, or award both the original effect and a duplicate recovered core. A full inventory should stop the operation safely. Dropping valuable outputs into the world is not the default fallback.

## AoA-specific playstyle proposals

These names are design concepts, not claims about current AoA items or mechanics.

- **Dimensional attunement:** dimension-themed cores unlock new visual and behavioral families through exploration; verify the selected AoA version's actual dimensions and progression.
- **Runic hush:** a magical discharge-dampening alternative for appropriate energy weapons. Distinguish acoustic, flash and supernatural detection channels.
- **Spirit conduit:** preserve a weapon's real resource provider while changing its recharge/handling personality. Resource conversion requires an explicit adapter and recipe, not free ammunition.
- **Echo chamber:** a bounded delayed secondary effect with distinct feedback; secondary effects cannot recursively trigger themselves or duplicate native bonus shots.
- **Prismatic emitter:** an authored alternative pattern with a total per-shot effect budget and its own muzzle layout. Do not multiply every on-hit reward by an arbitrary pellet count.
- **Boss-memory core:** a discoverable themed behavior that encourages revisiting content while preserving boss immunities and ownership rules.
- **Baronator alternating assembly:** retain the approved upper-then-lower firing personality; evaluate compatible scopes, handling modules and effect cores around that signature. A native bonus projectile is not another barrel-parity event.
- **Living or supernatural finish:** optional material/animation personality without misrepresenting a cosmetic as a functional upgrade.

Example experiments: a quiet runic exploration build; a heavy alternating Baronator with recovery-focused handling; a resource-efficient precision emitter; or a deliberately extravagant sandbox hybrid. These are test concepts, not advertised working builds.

## Freedom without broken combinations

Provide survival progression and an optional server-configurable sandbox mode. Survival uses discovered parts, reusable cores, meaningful unlocks and explicit costs. Sandbox can relax balance and unlock restrictions. Neither mode relaxes item safety, bounded effect execution, invalid numbers, missing resources, or known visual clipping.

Separate physical compatibility from effect compatibility. A scope needs a mount, sight alignment and hand clearance; an effect needs an eligible event and resource policy. Where a visually strange combination can be made coherent, author an adapter. Otherwise explain the incompatibility and preserve the player's item. Never make an invisible attachment continue granting a hidden effect by accident.

## Implementation contract

- Keep base item identity, schema version, assembly revision and namespaced component IDs.
- Represent sockets and capabilities as data; store transforms and attachment envelopes in model-space game units.
- Keep native AoA effects, enchantments, Apotheosis affixes, projectile conversion and cosmetics as separate layers with explicit precedence.
- Resolve compositions at equip/change/reload time and cache them. No per-frame registry scans or runtime geometry QA.
- Dispatch gameplay from authoritative events with provenance, duplicate suppression and bounded secondary-event budgets.
- Revalidate player access, recipe, inventory revision, resources, capacity and server rules at commit. Use atomic input/output mutation and idempotent requests.
- Preserve unknown component IDs as inert data if a supporting mod disappears. Explain the missing adapter; do not erase the weapon.
- Version migrations must preserve the original item and effects. Test round trips and interrupted operations.
- Optional TaCZ, Apotheosis, magic-provider and turret adapters must declare supported versions. A native AoA model replacement alone does not make a TaCZ turret weapon.

## Pinned TaCZ integration feasibility

Static inspection of TaCZ commit `b482eff8c94a733ac8d0910193fca3893954027c` confirms a useful foundation, with important gaps:

- [`AttachmentType`](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/api/item/attachment/AttachmentType.java) names scope, muzzle, stock, grip, laser and extended-magazine slots. Independent barrel, receiver, resource-conduit and effect-core slots are **not** present in this enum. Our broader system therefore needs its own assembly layer and adapter, rather than a promise that a stock gunpack JSON can already do everything.
- [`AttachmentPropertyManager`](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/resource/modifier/AttachmentPropertyManager.java) registers aim, recoil, silence, weight, movement and other game modifiers. It provides property-change event/caching integration points; this is a candidate bridge to validate, not an implemented AoA bridge.
- [`AttachmentCacheProperty`](https://github.com/MCModderAnchor/TACZ/blob/b482eff8c94a733ac8d0910193fca3893954027c/src/main/java/com/tacz/guns/resource/modifier/AttachmentCacheProperty.java) aggregates attachment properties into cached values and clears temporary modifier lists. Reuse compatible mechanisms and profile the actual call sites instead of adding another repeated scan.

The proposed architecture is an AoA assembly/effect contract above version-specific rendering and gameplay adapters. Preserve the native item and resource contract; expose supported TaCZ slots through that adapter and resolve authored composite models for additional parts. Do not patch the enum blindly or assume third-party packs accept new slots. Verify licenses, APIs, load order and save behavior before implementation.

[Static-source receipt](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/modular-armory-tacz-source-evidence.json) lists file hashes and review limits; publication of that receipt accompanies the repository documentation update.

## Native AoA effects: first extraction feasibility pass

Pinned 1.20 source review shows why an effect core needs a real adapter rather than copying a weapon name or rerunning its firing method. These are source observations, not transferred effects already working in-game.

| Donor example | Observed behavior in the inspected source | Extraction requirement |
|---|---|---|
| Baronator | Successful primary fire can add a server-side chance-based grenade | Preserve its secondary-event contract; never call the donor's full firing method and accidentally consume/fire twice |
| Frosticator | Living-target slowdown plus a blue projectile type | Separate status behavior from projectile appearance; define slowdown stacking |
| Miasma | Living-target slowdown in this source version | Do not infer poison from its name |
| Electinator | Nearby Enemy lookup and scaled secondary damage | Specify whose damage basis applies; bound dispatch and prevent proc recursion |
| Golden Fury | Firing particles plus an owned harmful area-effect cloud on impact | Separate cosmetic cues from persistent entities; preserve owner and cleanup behavior |
| Blood Iron | Metal Slug ammunition and a corresponding projectile class | Treat as a resource/projectile conversion, not a universal on-hit effect |
| Gardener / Dart Gun | Seed-tag resource lookup and SeedDart projectile; Dart Gun also changes firing feedback | Preserve resource tags and cost conditions; do not replace these with a generic ammo-consumption path |
| Sublimus | Environment-dependent resource-consumption branch | Distinguish possessing ammo from consuming it; reconcile the released helper signature |
| Lunar Assault Rifle | Damage getter samples a random value | Preserve native evaluation timing; do not cache one random roll as a permanent assembled statistic |
| Clownershot / Overshot | A successful base shot requests another ammo-consuming projectile | Preserve that second resource requirement and partial-ammo behavior; it is not the same contract as Baronator's bonus grenade |

**Version boundary caught during review:** the inspected source snapshot contains NeoForge imports, while the released 1.20.1 target uses Forge references. Twelve selected released classes were therefore inspected read-only as well. The seed-resource and random-damage call sites are present, but helper signatures can differ. These are architectural/behavior references, not source files to paste into a Forge adapter unchanged. Inherited behavior, mappings and full runtime equivalence remain separate gates.

Source: [AoA gun classes at the inspected revision](https://github.com/Tslat/Advent-Of-Ascension/tree/85d6beba07e3a09032834dcf79b5a01f411092c3/source/content/item/weapon/gun). Method-name discovery across this directory is only a starting index: inherited behavior, projectile classes, registry configuration and the actual released JAR still need reconciliation. A compatible socket is not proof that a donor effect is transferable.

### Broader source inventory and extraction pitfalls

The source discovery pass covers 78 gun classes; 55 have candidate behavior hooks in the deliberately limited method-name scan. All 55 candidate classes now have a manual source note and adapter warning in the [effect-source audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/aoa-effect-extraction-source-audit.json). This does not complete projectile/helper/inherited behavior or other weapon families.

- **Material conservation:** Shoe Flinger consumes boots and can equip boots onto a target. Transferring the item-producing behavior to a cheap-ammo weapon without an explicit resource rule would create an unintended item factory. Recovery cores must specify material-producing costs and donor-specific advancement eligibility separately.
- **Unfinished source is not a working effect:** Flowers Fury's candidate summon body is commented out as a TODO in this snapshot. It cannot be marketed as a functioning extracted summon without restoration and testing.
- **Changing state is not a cached statistic:** food-dependent recoil, crouch replacement, randomized cadence/damage and environment-dependent consumption need the correct native evaluation timing. Preview ranges and conditions without spending gameplay RNG.
- **Scheduled and persistent effects:** Echo Gull delegates to a scheduled task; poison/flame/cloud effects create entities or queries. Their ownership, cancellation, unloading and server cost must be audited beyond the weapon method.
- **Composition order matters:** some donors replace an incoming damage/recoil value while others multiply or add after base damage. Define that order explicitly rather than letting attachment load order decide the result.

## Acceptance and implementation backlog

- [ ] Pin AoA/TaCZ/loader versions and inventory actual native effects/resources.
- [ ] Define typed part sockets, effect composition, schema migrations and adapter interfaces.
- [ ] Implement one end-to-end assembly: swap a scope and handling part with coherent geometry and statistics.
- [ ] Add one extractable effect with exact-output preview, provenance and atomic transfer.
- [ ] Test stale requests, duplicate packets, full inventory, two users, disconnects and save/reload.
- [ ] Validate empty/tactical reload or resource recharge with all supported attachment envelopes.
- [ ] Prove no native effect is lost, applied twice or recursively amplified.
- [ ] Add accessible live assembly preview, comparison, blueprints and protected-item controls.
- [ ] Add survival unlocks and separate sandbox rules, then playtest discovery and experimentation.
- [ ] Profile cold/warm startup, equip/change cost, allocations, frame times and server ticks.
- [ ] Expand across the registry with pairwise and worst-case combination tests; disclose untested combinations.
- [ ] Publish actual runtime receipts before marking any gameplay feature complete.
