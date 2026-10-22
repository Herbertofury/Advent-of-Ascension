# Soul Storm: complete weapon profile

> Latest sight direction: the default Soul Storm aiming sight is an animated Soul Flame. Soul Candle and Soul Gem are optional attachments; preserve the older gem concepts. [Sight specification](Soul-Storm-Sights).


**First documented lane: AoA3.7.1 / Minecraft1.20.1.** Original facts below come from the released JAR and explicitly linked source comparison. Our premium design and upgrade values are proposals; native upgraded gameplay has not been measured.

[Concept art](Soul-Storm-Art-Direction) · [Functional upgrade policy](Functional-Weapon-Upgrades) · [Attachment gallery](Attachment-Concept-Gallery)

## Current selected concept · 22 October 2026

![Soul Storm selected concept candidate, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-anchored-flame-focus-concept-v1.png)

Five-emitter Soul Flame sight study; the default upgrade has four emitters, with five/six as options Final art review remains open.

[Original-versus-concept comparison and preserved alternatives](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html?weapon=aoa3%3Asoul_storm). Earlier art below is preserved history or a separately labelled variant, not a replacement for this selected main. Original source behavior and all native acceptance gates remain unchanged.

## Lore and material provenance

The pinned infusion recipe uses a Blaster Frame, two Ghoulasm entries, three Ghostly Powder entries and the Ghastly ingot tag. Ghoulasm appears in the packaged Greckon world loot table; spectral creature tables reference Ghostly Powder. Preserve this haunted material identity in both visual treatments. Original maker and artist intent remain unknown, and retained world data is not proof of current dimension availability.

The soul-flame sight and plasma-disc treatment are our adaptations. They must not erase the original Spirit resource or be misrepresented as original projectile visuals. [Recipe, ingredient provenance and evidence boundaries](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Soul-Storm-Lore-and-Materials.md).

## What the original weapon is and does

Soul Storm is a Spirit-powered rapid-fire blaster. Its identity is a compact indigo/cyan weapon with a circular side motif and a striped emitter stack. It fires SoulStormEntity projectiles, rather than conventional bullets or the newer generic straight beam path. The original projectile renderer produces a cluster of cyan and blue sparkler particles; it does not draw the large plasma-disc mesh imagined for our upgrade.

The projectile's strong gravity value makes its flight drop rather than remain a straight laser. This suggests a close-range, falling-stream personality, but usable range and hit rate still need a real-game capture instead of a guessed distance. A successful entity hit passes the base damage into the energy-projectile damage helper. The inspected Soul Storm class does not add a unique impact override; its inherited legacy block-impact and impact-effect hooks are empty. The base projectile discards itself after server-side impact handling.

It uses Spirit and has durability. The one-tick firing-delay input allows a nominal20 firing opportunities per second at20TPS once use is admitted; resource availability, game state, modifiers and target damage handling affect actual results. It is not a conventional magazine weapon and does not need a cosmetic reload imposed on its original mode.

### Original strengths, limitations and quirks

- **Strength:** rapid repeat fire and a recognizable blue/cyan stream rather than a slow single precision shot.
- **Limitation:** falling flight demands trajectory awareness; it should not be described as an unchanged long-range hitscan weapon.
- **Resource pressure:** a base Spirit cost is paid per successful firing attempt, with enchantment/equipment modifiers in the cost path.
- **Quirk:** the renderer adds sparkler particles during rendering. New effects should use bounded, frame-independent emission rather than copy a render-rate-dependent spawn pattern blindly.
- **Unverified here:** actual DPS against representative targets, practical range and interactions with every installed enchantment/mod. These need their own evidence.

## How to obtain it in this version

The released infusion_soul_storm recipe produces Soul Storm from a Blaster Frame plus the following infusion ingredients:

| Ingredient | Count |
|---|---:|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-blaster_frame.png" width="48" alt="blaster frame" /> Blaster Frame, input item | 1 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-ghoulasm.png" width="48" alt="ghoulasm" /> Ghoulasm | 2 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-ghostly_powder.png" width="48" alt="ghostly powder" /> Ghostly Powder | 3 |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-icon-ghastly_ingot.png" width="48" alt="ghastly ingot" /> Ghastly ingot ingredient | 1 |

The ingot uses the forge:ingots/ghastly tag, so eligibility follows that tag rather than a hard-coded icon alone. This is an infusion recipe, not an ordinary shaped crafting-grid recipe. The matching source has Infusion Table recipe handling; native crafting verification remains open.

[Exact released acquisition data](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-profile-acquisition-evidence.json)

## Original art and projectile assets

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sprite.png" width="192" alt="Original Soul Storm item sprite" />

The source sprite has five bright horizontal emitter bands. That visual observation does not mean the original code already owns five independently firing muzzles.

The following are the eight actual sparkler image masks from the released JAR. The runtime colors them cyan/blue; these are source assets, **not a screenshot of the projectile in flight**.

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-0.png" width="64" alt="Original sparkler frame0" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-1.png" width="64" alt="Original sparkler frame1" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-2.png" width="64" alt="Original sparkler frame2" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-3.png" width="64" alt="Original sparkler frame3" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-4.png" width="64" alt="Original sparkler frame4" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-5.png" width="64" alt="Original sparkler frame5" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-6.png" width="64" alt="Original sparkler frame6" /> <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-sparkler-7.png" width="64" alt="Original sparkler frame7" />

## Original values versus the upgrade direction

| Property | Original released-file evidence | Proposed upgraded behavior |
|---|---|---|
| Base damage input | 1.5 damage points | May increase through functional components; show resolved per-disc damage |
| Durability input | 3,190 | Explicitly configured per build; no hidden loss during conversion |
| Firing-delay input | 1 tick | A real sequence/volley scheduler can support increased output from upgraded stacks |
| Base resource-cost input | 2.0 Spirit | Declared cost/capacity/efficiency policy per installed build |
| Projectile | SoulStormEntity | Visible plasma-soul disc, with explicit collision and impact behavior |
| Launch-speed parameter | 3.0 in the inherited constructor path | Configured by projectile/attachment; not an unexplained visual speed change |
| Gravity return value | Approximately0.6 | Preserve original-mode flight; flight-changing upgrades may deliberately alter it |
| Projectile age input | 60 | Explicit lifetime policy; do not call this a measured flight duration |
| Original appearance | Cyan and blue SPARKLER particles | Bright-rimmed flat discs with swirling Spirit interiors and short trails |
| Particle renderer inputs | Six iterations, cyan+blue each iteration; scale0.25; ageModifier3.0 | Bounded frame-independent effects and reduced-effects settings |
| Entity impact | Energy-projectile damage helper, then inherited impact hook | Readable disc impact; damage, area/status/secondary effects follow installed parts |
| Block impact | Inspected legacy hook is empty; projectile handling discards on impact | Cosmetic impact by default; deliberate gameplay effects require a defined module |
| Sound identity | ITEM_SPRAYER_FIRE | Original sprayer-like identity with new original layered feedback |

The particle ageModifier is **not** a fixed3-tick lifetime. The inspected particle constructor computes lifetime from a randomized expression. Renderer invocations, damage input and theoretical rates are not direct measurements of in-game performance or target damage.

## Plasma-disc stack concepts

![Four, five and six emitter plasma-disc concepts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-disc-stack-concepts-v2.png)

- **Disc Cycler:** four independently pulsing emitters, alternating top to bottom.
- **Classic Stack:** five-emitter family that echoes the original sprite's five bands.
- **Storm Stack:** six-emitter upgrade with genuinely greater output or a different supported pattern.
- **Further stacks:** extensible upgrades, with actual geometry, scheduling, resources and performance qualified for each supported configuration.

Generated concept views are illustrative; count, spacing and fit must be verified against the real mesh. The firing panels are sequence composites, not proof that all slots fire simultaneously. A volley attachment may deliberately introduce simultaneous fire as a separate declared mode.

## Five- and six-emitter authored variants

These are actual editable authoring models, still unaccepted as finished or playable weapons. The four-emitter base remains separate.

![Five-emitter authoring study, unaccepted](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-5-stack-unaccepted.png)

![Six-emitter authoring study with physical sight riser, unaccepted](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-6-stack-unaccepted.png)

The taller front supports and rear manifold match the selected count. A physical riser raises the six-stack brazier, rooted fire and reticle together after review found only 0.005 authoring units of lower-reticle clearance. The corrected bound is 0.225; native first-person aim and hand fit remain untested.

Independent recoil clips preserve each variant’s vertical offsets. Scoped checks cover 105/126 moving-emitter poses against the lower wing. Actual released parser classes accept eleven clips/462 keys on Java 17 and 21, and matching hardware bone contracts are checked. This does not implement damage/resource upgrades or certify native playback.

The exported hardware fixtures deliberately omit vortex, plasma, fire and reticle effects shown in the authoring renders. Final materials, effects, animation integration, complete collision checks and native performance remain open.

[Editable scenes, generators, clips, matching hardware files and exact evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Soul-Storm-Stack-Studies.md).

## Example numerical test fixture, not final balance

This makes the upgrade intention concrete without pretending it is already implemented. Assume five pulses per emitter per second,1.5 damage per disc,2 Spirit per disc, every scheduled disc admitted,20TPS, no target mitigation or missed shots:

| Draft stack | Discs/second | Raw damage input/second | Spirit/second |
|---|---:|---:|---:|
| Four emitters | 20 | 30 | 40 |
| Five emitters | 25 | 37.5 | 50 |
| Six emitters | 30 | 45 | 60 |

These are arithmetic design examples, **not measured DPS or approved final balance**. Damage cores, efficiency parts, firing modes and progression rules can change the numbers. The interface must show the actual resolved build values. More emitters are allowed to make the weapon stronger; original behavior is a baseline, not a ceiling.

## Impact, effects and testing plan

A disc needs a readable rim and thin body in flight, a coherent arc, and an impact that makes clear what was hit. Visual trails do not create extra damage. A larger functional disc should have a matching declared collision/impact profile rather than an oversized visual hiding a tiny hitbox. Test walls, moving targets, multiple targets, shields/boss rules, ownership and secondary effects.

Compare original and upgraded captures using the same scene, hardware and target. Record actual firing count, damage events, resource spending, impact distribution, frame-time lows and server tick cost. Use source-derived visualizations until game capture is available, labeled honestly.

[Native contract receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-native-contract.json) · [Original particle assets and renderer inputs](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-original-projectile-assets.json) · [Released projectile/impact audit](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-released-projectile-impact-audit.json)

## Upgraded impact concept comparison

![Proposed upgraded projectile and impact language](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-impact-concepts-v2.png)

This is proposed upgraded VFX art, not an original-game capture. Compare it with the actual source assets and original impact values above. Discs, primary bullet hits and the separate Baronator grenade branch have distinct visual identities. Larger impact areas or terrain-changing behavior must correspond to a declared functional module and server rules; cosmetic debris is not proof that world blocks are destroyed.


## Editable sculpt progress

[Current sculpt, four-emitter motion and retained source iterations](Soul-Storm-Sculpt-Study). Visual and native acceptance remain open; the sampled Blender animation is not gameplay footage.
