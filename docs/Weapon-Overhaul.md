![The Ascension Armory](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-upgrade-banner.svg)

# Every weapon, elevated

**Owner-approved project goal · implementation pending · no runtime performance claim.**

Every accepted AoA weapon should offer an optional premium, fully animated 3D remodel. The quality bar is the strongest TaCZ and Bedrock weapon presentations: convincing moving mechanisms, satisfying reloads, expressive inspection, weighty firing, readable sights and polished first- and third-person animation. Preserve each weapon's AoA identity instead of replacing the arsenal with generic modern guns.

[Reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Implementation checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog) · [Original item atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Items-Atlas)

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
