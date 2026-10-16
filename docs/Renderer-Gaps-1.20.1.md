# Minecraft 1.20.1: released renderer gaps and restoration checks

**Artifact audited: AoA3-1.20.1-3.7.1-all.jar.** This page distinguishes released bytecode from the pinned 1.20 source snapshot. It is not a claim about every newer AoA release, all gameplay availability, or the current state of the user's Enderloom build.

## What was verified in the released classes

The static initializer of `AoAEntityRendering` contains **186 renderer-package assignments** using the constructor of `JankyJankTempRendererToPreventCrashesWhileInDev`.

- Those assignments reference **181 distinct entity registry fields**, because five assignments repeat the Primordial Banker target.
- **173 distinct referenced entities** are present in this wiki's inspected 1.20 living-entity roster.
- The remaining eight artifact references are the Pixon variants listed in the evidence file.
- The placeholder class declares only its constructor and a texture getter. The getter's complete bytecode is `aconst_null; areturn`; the class does not override body rendering.
- This proves a concrete released renderer gap. It does not independently prove whether each entity naturally spawns, whether other code replaces a renderer, or whether the whole mod is playable.

The audit decodes instruction boundaries, resolves the constructor through `BootstrapMethods`, records the entity registry field and resulting renderer field, and retains class hashes. No game code was executed.

[Full released-class evidence, offsets and entity references](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/placeholder-renderer-audit-1.20.1.json).

## Five field names do not match their released target

| Renderer field | Entity registry field actually supplied in 3.7.1 | Pinned source target |
|---|---|---|
| PRIMORDIAL_MERCHANT | PRIMORDIAL_BANKER | PRIMORDIAL_MERCHANT |
| PRIMORDIAL_SPELLBINDER | PRIMORDIAL_BANKER | PRIMORDIAL_SPELLBINDER |
| PRIMORDIAL_WIZARD | PRIMORDIAL_BANKER | PRIMORDIAL_WIZARD |
| PROFESSOR | PRIMORDIAL_BANKER | PROFESSOR |
| TOY_MERCHANT | PRIMORDIAL_BANKER | TOY_MERCHANT |

The source snapshot already uses the named target for these five lines. That is why reading only the branch would miss the difference in the released JAR. Do not count these as five additional distinct placeholder-target entities or claim they are fixed in the released binary merely because the source is corrected.

## Why some modern cards cannot show an authentic body preview

The searchable bestiary labels these renderer gaps. A registered mob ID, stats builder or loot resource is not evidence that a textured body renderer exists. The wiki will not silently paste a 1.16.5 portrait onto a 1.20.1 card and imply that it is the released appearance.

For historical reference, select **1.16.5** in the bestiary and search the same creature ID where available. Historical artwork is useful restoration input; its geometry, texture mapping, animations and behaviours still need an explicit port and validation.

## Enderloom restoration checklist

- [ ] Reconcile every affected entity against the exact target-build registry and renderer registration.
- [ ] Restore a valid body renderer or explicitly classify intentional invisible/particle entities.
- [ ] Correct the five released field/target mismatches in the port, checking whether the chosen source revision already contains the correction.
- [ ] Validate each historical model and texture pair rather than matching filenames alone.
- [ ] Restore animation controllers, layers, emissive effects, variants, scale and hitbox alignment separately from static portraits.
- [ ] Add a regression check that rejects a production creature renderer returning a null texture unless the entity's rendering contract intentionally permits it.
- [ ] Add a registry-to-renderer audit that flags duplicate entity targets and unassigned expected targets.
- [ ] Test spawn, rendering, combat, death, loot and reload for each restored entity on both client and server.
- [ ] Keep frame time, loading time and memory measurements alongside visual correctness. A substitute generic mob is not restoration.

These are documented implementation goals, not completed fixes or live-game acceptance results.

## Source comparison

- [Pinned 1.20 renderer declarations](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java)
- [Pinned placeholder renderer class](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/render/entity/JankyJankTempRendererToPreventCrashesWhileInDev.java)
- [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)
- [Bestiary](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bestiary)
