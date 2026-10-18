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

[Alternate barrels and skins](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Alternate-Barrels-and-Skins) · [Functional upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Functional-Weapon-Upgrades) · [Weapon profile standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Profile-Standard)
