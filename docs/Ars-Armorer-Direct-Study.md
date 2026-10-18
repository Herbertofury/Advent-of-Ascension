# Ars Armorer: direct gallery and pack study

**Reviewed 2026-10-18. Reference study, not AoA implementation or game-test evidence.**

Koei's [official four-image gallery](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei/gallery) and [Ars Armorer v1.0.1_for117](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei/files/7358702) were inspected directly. The gallery still points to that file. Archive SHA-256: `42bf9b52c340693c3f961b1385880e9938b5d032bd3b31eec539539b88204c7a`.

[Machine-readable evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/ars-armorer-deep-study.json) records eight weapon display/animation definitions, 36 attachment definitions and script hashes. Lua was read, not executed. No in-game animation, sound-listening or performance certification is implied.

## What the gallery actually shows

- **Attachments:** color-framed glyph tiles distinguish families and tiers. Shape and icon differences accompany color. Apply that clarity to our effects, delivery patterns, efficiency modifiers and capacity upgrades, with readable text and keyboard/controller navigation.
- **gun1:** an open, elongated gold-framed magical implement uses substantial negative space and a magenta core. Its mechanism reads as a fantasy device rather than a conventional rifle with a magical texture.
- **gun2:** an asymmetrical, compact purple/gold weapon keeps a small colored core visually distinct from its frame. Major forms carry the identity before fine surface details.
- **gun3:** six floating blade-like forms surround a central magical object and the player's hands. This is a strong reference for unconventional AoA weapons. A screenshot alone does not establish homing, melee or projectile behavior.

Use those principles to improve AoA-specific silhouettes and exposed resource pathways. Keep each AoA weapon's own colors, identity and mechanics; avoid turning the entire arsenal into one recolored chassis.

## The useful customization architecture

The released index maps semantic roles onto TaCZ's existing slots:

| Semantic role in this pack | Backend slot | Definitions |
|---|---|---:|
| Effect glyphs | grip | 18 |
| Efficiency/recovery modifiers | stock | 7 |
| Delivery/spread triggers | muzzle | 8 |
| Reserve capacity | extended_mag | 3 |

This is an important architecture lesson, not permission to label every AoA effect a literal grip. Our UI and saved data should retain typed semantic roles, then translate through versioned TaCZ adapters. Physical suppressors, grips and barrels must coexist with magical modules without overwriting one another's slots.

The data and logic work together. Some attachments have only lightweight JSON properties while their meaningful behavior is selected by Lua. Therefore, importing JSON alone would lose behavior. Conversely, blindly running the donor's full shot routine could create duplicate projectiles or costs.

## Resource and action behavior observed

- The normal and drill logic explicitly reject manual reload. None of the eight inspected weapon animation files contains a conventional reload clip.
- The normal logic represents a regenerating reserve with TaCZ magazine-count APIs. It checks cost/capacity before normal firing, consumes the computed amount, and replenishes after a delay. Resource-named parameters do not establish integration with actual Ars Source or AoA Spirit.
- Effect, modifier and delivery choices influence costs. Double-fire invokes two shots in its branch. Horizontal/vertical spread variants alter delivery. These need explicit AoA adapters, successful-shot provenance and balance tests.
- The flying-blade configuration has six reserve units, distinct blade groups and delayed removal/recovery behavior. Treat inventory capacity, visible blade count and animation state as separate values requiring synchronization.
- The drill has separate logic. It should not be generalized from the ordinary gun path without reviewing its own cost and success conditions.
- Client state-machine logic also evaluates effect/cost choices. This highlights a risk for our design: compute an authoritative server result and replicate presentation data rather than maintain divergent client/server formulas.

## Animation and performance lessons

All eight display definitions specify LOD resources. That is a useful authoring pattern, not a measured frame-rate result. The ordinary weapons animate cores, barrel groups, hands, camera and separate action tracks; the flying-blade asset has distinct blade groups. Keep draw, inspect, recoil, movement and recovery independently interruptible and restore state on every exit.

Do not infer shot cadence from clip duration. A long visual recovery may overlap later native shots. For Soul Storm, its native one-tick delay must remain authoritative; a longer authored pulse must not slow firing or produce additional Spirit charges.

The pack's resource logic repeatedly reads attachment identifiers. For our implementation, compile immutable module definitions when an assembly changes, cache by item assembly revision, and invalidate on actual edits/resource reloads. Read changing resource balances at the authoritative shot transaction. Benchmark the real adapter rather than assuming caching yields a particular FPS gain.

## Concrete AoA acceptance tasks

- [ ] A distinct magical module UI with effect, delivery, modifier and resource roles, including names, tradeoffs and incompatibility reasons.
- [ ] Preserve Spirit, runes, Rage, native ammunition and other actual resources through explicit adapters; no silent conversion into a regenerating TaCZ magazine.
- [ ] Test zero/partial/full resource, insufficient cost, rejected shots, multi-projectile delivery, reconnects and mid-animation item swaps.
- [ ] Support conventional weapon parts and magical modules simultaneously without slot collisions or effect recursion.
- [ ] Show a weapon's resource path and action feedback without inventing forced reloads.
- [ ] Test first/third-person hand placement, FOV, handedness, interruption blends, sounds, LOD switches and measured performance.

## Attribution and reuse boundary

The [project license page](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei/license) identifies **Creative Commons Attribution 4.0 International**. Credit Koei, retain relevant notices and license links, and identify modifications if licensed material is reused. Check the provenance of individual assets and dependencies separately. This study publishes observations and hashes; the original AoA authoring packages do not bundle Ars Armorer models, textures, sounds or scripts.

[Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Modular armory](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage) · [Weapon QA](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Mechanism-and-Animation-QA)


## Actual geometry, UV and LOD follow-up

All eight main display records were resolved against the same downloaded v1.0.1 archive. The counts below include stored attachment variants and visual planes; they are not runtime draw-call or performance counts.

| Model | Bones | Stored cuboids/planes | Rotated cuboids | Declared UV / PNG size |
|---|---:|---:|---:|---|
| auto_rifle_stream_ejector | 35 | 23 (0 planes) | 9 | [64, 64] / [128, 128] |
| mortar_source_thrower | 28 | 69 (54 planes) | 25 | [64, 64] / [128, 128] |
| pistol_source_ejector | 33 | 20 (0 planes) | 12 | [32, 32] / [64, 64] |
| shotgun_jet_ejector | 36 | 24 (0 planes) | 10 | [32, 32] / [64, 64] |
| shotgun_splash_ejector | 36 | 30 (0 planes) | 18 | [64, 64] / [128, 128] |
| sniper_distance_ejector | 35 | 32 (0 planes) | 20 | [64, 64] / [128, 128] |
| special_miner_drill | 19 | 24 (0 planes) | 10 | [32, 32] / [64, 64] |
| special_source_flying_blade | 37 | 51 (0 planes) | 7 | [64, 64] / [128, 128] |

Every counted cuboid uses per-face UV records. Several 128×128 PNGs accompany a 64×64 declared UV space: the source data distinguishes logical UV coordinates from image pixels. Do not normalize against the PNG dimensions alone without respecting the model UV declaration. The mortar includes 54 zero-extent visual planes; treating all zero extents as invalid solids would reject intentional presentation geometry. Collision QA must distinguish visual planes from physical obstruction volumes.

Seven display records declare LOD model/texture paths absent from this archive. The flying-blade LOD is present: 6 bones and 8 cuboids, compared with the main model’s 37 bones and 51 cuboids. This is an exact-file observation, not a claim that the pack crashes; external resource packs or native fallback behavior must be assessed separately. A declared LOD entry is insufficient evidence of an operating optimization.

### Apply this to the AoA upgrade

- Spend detail on silhouette, material separation, per-face UV painting and purposeful movement. A larger cuboid count alone cannot meet the art target.
- Keep decorative/translucent planes out of solid feed-path clearance checks while still checking their visual overlap, depth sorting and overdraw.
- Validate every main and LOD reference from a clean exported pack, with attachment variants and texture dimensions explicit.
- Design and visually compare actual simplified LOD assets before claiming distance-rendering savings. Preserve identity and readable effects.
- Verify first-person UV orientation, crispness, hands and all attachment variants in the native renderer; a source census cannot approve them.

[Machine-readable eight-model audit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ars-armorer-model-presentation-audit.json) · [Original audit script and synthetic test](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/model-presentation-audit-tool-v1.zip)

Reference art/models belong to Koei. This follow-up publishes factual counts and original tooling; it does not bundle the reference pack.
