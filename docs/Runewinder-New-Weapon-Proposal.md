# Runewinder — standard and Soulflame proposal

**Working name · entirely new AoA weapon proposal · generated concept, not in-game.** Requested October 27, 2026. This is not an existing released AoA registry entry and does not increase the audited 434-identity source roster.

![Runewinder standard and Soulflame concepts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/runewinder-standard-soulflame-concept-v1.png)

## Owner direction

Use the Guycot 40's distinctive elongated side chamber and visible circulating-loop idea as visual inspiration. Replace the historical chain-round presentation with a necklace of luminous engraved rune beads inside the weapon. The player-facing side has a clear glass/crystal panel so the user can see the necklace move. The supplied historical image is a reference, not a redistributed project asset or a fabrication drawing.

The **standard** candidate uses titanium, graphite and restrained bronze around ivory/cyan rune beads. The **Soulflame** candidate belongs visually with the purple-flame family: obsidian/dark silver, amethyst accents, violet beads and a small purple-flame aiming sight. The shared chassis is intended to support future dimension finishes. The working name, registry IDs, crafting, damage/cadence values and mana costs remain design work. Capacity and projectile selection now follow the owner-approved bead contract below.

## Fictional internal-motion contract

The necklace is a closed loop retained inside the body, not a loose belt dangling from the receiver and not a sequence of real cartridges. A visible active bead pulses at the emitter-side index. A confirmed firing event advances the loop once; rejected input, dry input, cosmetic inspect events and duplicate network events must not advance it. This is an animation/game-state proposal, not a reproduced real mechanism.

Model the bead path and glass clearance as authored game geometry. Preserve stable bead identity and interpolation around the complete loop. Test start/stop, partial recovery, equip/holster, save/load, repeated input and multiplayer correction. Glass must show meaningful internal motion from actual first-person angles without obscuring the user's hand or sightline. A mirrored left-handed mode needs its own camera/visibility review.

Capacity equals the installed necklace’s bead count. Players can customize and upgrade that count through functional necklace attachments. The ordered bead types determine successive projectiles: ice → fire → ice → fire, poison → fire, or other deliberate combinations. Forty is a historical reference and prototype configuration, not a mandatory capacity. The generated art does not prove an exact count or a continuous 3D path.

## Flame sight and dimension variants

The Soulflame sight forms a small open aiming shape from violet flame when focused. Keep its center readable, suppress excessive bloom, and provide reduced-flash/static-reticle options. It must align to the actual aim transform, not merely look centered in a side render.

Dimension skins may change materials, bead glyphs, light color, cosmetic trails and sight styling while retaining the same base rig. Do not silently change damage, resource type, cadence, targeting or projectile count through a skin. Functional dimension conversions, if requested, require separate explicit build definitions and tooltips.

## Production path and acceptance

Start from the best suitable licensed rig or a rough mesh, refine the approved silhouette and build the internals upward. Inspect actual donor files and permissions first. Do not force a conventional firearm's magazine or reload into this necklace design. Reuse a proven animation/state framework where compatible, not an unsuitable exterior solely because it already exists.

- [x] Standard and purple-flame concept candidates produced; previous source roster unchanged.
- [ ] Owner visual review and working-name decision.
- [ ] Shared source mesh, exact closed bead path and player-facing glass verified.
- [ ] Animated internals, confirmed-shot synchronization, interruptions and resource policy implemented.
- [ ] Flame-sight alignment, exposure, reduced-effects mode and left-handed visibility tested.
- [ ] Dimension finish system and separately defined functional variants reviewed.
- [ ] Native TaCZ/AoA export, gameplay, multiplayer, saves, frame-time and memory qualification.

All native and art acceptance gates remain open. No claim of actual animated playback is made by these static sheets.

[Every-weapon standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard) · [Base reuse and permission gate](Weapon-Base-Reuse-Register.md) · [Concept presentation](runewinder-concept.html)

## Reused motion foundation · 2026-10-27

A [source-only cosmetic sequence prototype](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/runewinder-cosmetic-sequence-prototype-v1.zip) reuses the existing EmitterSequence.java unchanged and adds a normalized closed-loop bead pose target. The original 60,000-selection tests and new 10,000-advance / 107,000-generated-position checks pass under the existing JDK 17.0.21. Rejected, duplicate and bonus events do not advance; sequence gaps resynchronize to the authoritative index.

This is not a rigged model, native animation, event-authority implementation or save system. Forty visual beads are a study configuration, not accepted gameplay capacity. Glass clearance, time interpolation, flame sight and actual first-person visibility remain open. No external donor asset was reused and no native gate is promoted.


## Rotating-sleeve mana reload and bead crafting · owner direction, 2026-10-27

The clear side cover rotates around the chamber in its end collars, like a bank pneumatic-tube carrier. It does not swing wide on a hinge. The player lifts out the whole closed necklace, charges its beads with mana in hand, snaps it back into the side track and rotates the cover shut flush. The target is a rapid, readable reload; actual duration is not yet measured or balanced.

Each bead is a functional projectile slot, not merely a colored texture. Preserve player-authored bead order, bead count, individual charge state and next-shot index. The necklace is one item with stable identity; extraction, hand charging and insertion must not duplicate or lose it. Empty, partly charged and mixed-element necklaces need explicit UI states. Larger capacity attachments require a reviewed visual path/necklace fit rather than overlapping or hiding extra beads.

Cyan cold/soul fire is a requested variant with a cyan flame sight. Fire, ice, purple flame, poison and biome beads are functional customization candidates. Necklaces can be arranged like jewelry, including alternating combinations. Shot order follows the bead order. Exact damage, interactions with previously applied statuses and upgrade costs remain design/balance decisions. No element combination is automatically approved to bypass cooldowns or double-spend mana.

Existing requested compatibility targets include Ars Nouveau, Iron’s Spells ’n Spellbooks/IronsArms and Botania. Their mana pools, conversion rules and availability must stay distinct. A successful hand-charge animation does not prove an adapter exists. Use transactional debit/charge semantics and test cancellation, insufficient mana, disconnect, full inventory, death and save/load before claiming compatibility. No new mandatory dependency is selected here.

Cosmetic dimension skins remain separate from these functional bead attachments. The build preview must show the actual ordered bead list, capacity and selected mana source; skins cannot silently rewrite them.


### Persistent beads and visible charge

A fired bead stays attached to the necklace and goes dark. It is not ejected, consumed or destroyed. Mana recharge relights that same bead. The ordered bead identities and element types persist through firing and recharge; only their charge states and the next-shot cursor change. Show remaining charged shots separately from total bead capacity. Empty and partial-charge behavior, cancellation and save restoration must preserve every bead without free refills.

**Reload image pending correction.** The earlier segmented-shutter sheet is rejected for its cover motion. The approved cover is one smooth transparent sleeve rotating around the chamber, not slats, a coiling blind or a hinged door. The corrected render request did not produce an image.

![Cyan Soulfire variant, alternating bead necklaces and optional cosmetics](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/runewinder-cyan-mixed-beads-study-v1.png)

The mixed-loop sheet’s ice/fire sequence was corrected to alternate continuously. The earlier reload sheet is not current evidence for the approved cover motion. These are storyboards and design illustrations, not a guarantee of exact shared geometry, identical bead counts between panels or implemented mana adapters.


## Persistent-bead state candidate

[Source and checks](https://github.com/Herbertofury/Advent-of-Ascension/raw/refs/heads/main/docs/runewinder-bead-state-prototype-v2.zip) extend the reused sequencer with ordered element slots, bead-count capacity and per-bead charge. The new offline tests retain every bead through 80,000 stress shots, verify dark/relit state, duplicate guards and immutable in-memory snapshot restoration. The charge operation is simulation-only and debits no real mana. Native adapters, transactional costs, disk saves, networking and visual integration remain unimplemented/unqualified. The prototype’s 64-bead limit is a test budget, not approved gameplay balance.
