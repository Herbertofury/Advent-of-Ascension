# Soul Storm · readable spectral effects

[Weapon profile](Soul-Storm-Weapon-Profile) · [Aiming readability](Soul-Storm-Aiming-Flame-Readability) · [Complete feature standard](Weapon-Completeness-Standard)

## Keep the original and the proposed upgrade separate

The inspected AoA 3.7.1 / Minecraft 1.20.1 renderer creates cyan/blue SPARKLER particles around SoulStormEntity. It does **not** render the large flat plasma disc shown in the upgrade concept. The projectile's gravity return is approximately 0.6, and the inspected inherited legacy impact-effect hooks are empty. Those source observations are not a native flight/impact capture or a measured range.

Original extracted sparkler frames, shown separately from the proposal:

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-0.png" width="80" alt="Original sparkler frame 0" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-3.png" width="80" alt="Original sparkler frame 3" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-7.png" width="80" alt="Original sparkler frame 7" />

[Released projectile/impact audit](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-released-projectile-impact-audit.json) · [Extracted asset provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-original-projectile-assets.json)

## Six coordinated effect channels

![Revised Soul Storm effect concepts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-effects-concept-v2.png)

**Proposed cosmetic art, not an in-game screenshot, implementation or native acceptance.** The training dummy is an illustrative prop. Its disappearance does not authorize hiding a living target or changing drops.

| Channel | Art direction | Required behavior boundary |
|---|---|---|
| Disc flight | Bright, thin rim and swirling translucent interior; short falling trail | Original-mode gravity remains the baseline; a deliberately altered trajectory belongs to a declared functional module |
| Muzzle bloom | Brief localized cyan slot flash and wisps | Spawn once from the accepted shot event at the active emitter, never once per render frame |
| Stone impact | Local spectral shatter against an intact surface | No default block destruction, physical cracks, new damage area or persistent debris |
| Water contact | Small ripple with restrained wisps | Cosmetic surface feedback; do not create fluid updates or infer a new underwater mechanic |
| Surface decal | Clear bright-to-faded-to-absent sequence | Bounded lifetime, bounded retained count, proper surface alignment and cleanup on world unload |
| Finisher | Optional voxel-to-soul-mote dissolve | Only after authoritative confirmed death; preserve drops, experience, loot attribution and other mods' death handling |

Reduced-glow mode must keep the projectile and aiming cues readable. It cannot simply remove every useful visual. The illustrated comparison is a direction, not a calibrated accessibility or frame-time test.

## QA changes made before accepting this concept direction

The first draft left a visible rune in its supposedly **CLEAR** stage, showed chipped stone that implied destruction, and made the muzzle flash look like a sustained beam. Revision 2 removes the residual decal, keeps the stone intact and reduces the flash. These corrections are visual concept checks only.

<details>
<summary>Preserved earlier draft, with known QA defects</summary>

![Earlier draft, not the accepted visual direction](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-effects-concept-v1.png)

Keep this draft for comparison. Do not use its persistent final rune or damaged block as the default implementation target.

</details>

## Implementation contract

1. Resolve the installed effect set when the assembly changes; do not rescan resources during firing.
2. Keep accepted-shot identity separate from cosmetic rendering. Prediction/reconciliation must not double-trigger flashes or resource costs.
3. Advance effect clocks independently of frame rate. Bound concurrent particles, decals and lights, and record how overload degrades visual detail.
4. Avoid per-particle dynamic lights and unbounded transparent layers. Preserve the crisp rim through distance/quality changes.
5. Test opaque/translucent ordering, water surfaces, chunk boundaries, paused time, reconnect and world unload.
6. Compare original and upgraded flight/impact footage in the actual target stack. Record which functional module intentionally changes behavior.
7. Measure equivalent-work frame times, low-percentile FPS, allocation and startup cost before declaring performance acceptance.

## Remaining visual work

- [ ] Entity/armor impacts, distinct from stone and water
- [ ] Alternate barrel/beam/lightning effect variants with their own explicit gameplay rules
- [ ] In-game timings, sound design and confirmed-event synchronization
- [ ] Native original-versus-upgraded captures and accessibility review
- [ ] Performance, multiplayer, shader and optional-mod qualification

This sheet advances six design channels. It does not complete the entire weapon or its full feedback package.


[Bounded cosmetic lifetime candidate](Bounded-Cosmetic-Lifetimes) adds isolated expiry/pressure tests to the existing presentation core. It does not yet own native resources or establish a performance gain.
