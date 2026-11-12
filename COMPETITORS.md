# Comparable adventures and restoration benchmarks

## Identity and scope

This is an independent [AoA restoration atlas and Enderloom integration project](README.md). The most important baseline is **official AoA itself**, not replacing its identity with another mod. [Version Matrix](docs/Version-Matrix.md), [Content Specification](docs/Content-Specification.md) and [Testing & Performance](docs/Testing-and-Performance.md) retain authority over completeness.

| Reference and primary source | Why it belongs | Proposed comparison |
|---|---|---|
| [Official Advent of Ascension](https://github.com/Tslat/Advent-Of-Ascension) | Canonical upstream source and lineage | Compare retained content, progression and behavior against the relevant historical and modern versions independently. A source declaration is not proof of a playable feature. |
| [The Aether](https://github.com/The-Aether-Team/The-Aether) | Original adventure mod ported to modern Minecraft | Study restoration documentation, dimension entry and upgrade compatibility while preserving recognizable identity. |
| [Twilight Forest](https://github.com/TeamTwilight/twilightforest) | Established adventure/dimension source project | Study how to make exploration and progression legible; validate AoA's own realmstone, boss and reward routes rather than copying another progression graph. |
| [Better Combat](https://github.com/ZsoltMolnarrr/BetterCombat) | Combat presentation/integration reference | Optional presentation improvements must preserve AoA weapon semantics and coexist with the target pack; do not infer compatibility from attractive animation. |

## Evidence-led backlog

- [ ] For every accepted dimension, retain a complete enter → explore → encounter → reward → exit → reload scenario, with version and exact artifact identity.
- [ ] Compare the restored build with canonical AoA behavior using fixed worlds, registry census and natural progression tests, not just spawned entities.
- [ ] Evaluate guidance quality: can a new player discover the next step using the atlas without confusing removed, current and planned systems?
- [ ] Optional weapon presentation: benchmark representative scenes and multiplayer ownership, retain reversible original appearance and verify animation/event correctness.
- [ ] Reconcile future upstream changes only from permitted access. Existing access denials and full-runtime acceptance blockers are not bypassed by this research page.

**Priority:** restoration completeness and truthful version-aware documentation before adding competitor-inspired content. Other mods are design references, not evidence that the accepted all-era union is finished. Rights to upstream art/code remain separate from access to its source.

## Evidence and maintenance contract

Reviewed 2026-11-12. This is a public-source design comparison, not a hands-on benchmark, exhaustive market ranking, feature acceptance, or permission to copy code/assets. Source pages may describe newer loaders or editions than our target. Recheck exact versions, licenses and integration boundaries before implementation. Preserve approved identity and existing progress; do not replace working systems merely because a competitor exists.

During each daily review, check linked official release notes/issues and update only material changes. Record source date, observation, relevance, proposed experiment and result separately. Retain failed comparisons and the last-good evidence. Community complaints are leads, not established product defects. New speculative features remain proposals until approved. Before claiming improvement, compare the same workload and retain latency/frame-time, memory, correctness and recovery results on the actual project build.

## Review log

- 2026-11-12: initial repository-scoped comparison index; official sources reviewed at documentation level. No gameplay, performance or compatibility tests run in this pass. No implementation or native GitHub Wiki publication claimed.

## Candidate foundations, concrete reuse and shared work

| Candidate | What to build on or study | How to improve without losing AoA |
|---|---|---|
| Canonical AoA source/version lineage and existing Enderloom restoration tooling | Reuse the current version matrix, resource census, source-model references and accepted conversion pipeline. Upstream remains behavioral authority. | Drive restoration from an explicit versioned content ledger and real natural-progression receipts rather than another ad hoc port. |
| [GeckoLib](https://github.com/bernie-g/geckolib) | Candidate original weapon/creature animation event system, including sound/particle timing and concurrent poses. | Prototype one reversible premium weapon presentation; compare timing, held-item ownership, gameplay semantics and native client/server cost against the original. |
| [The Aether](https://github.com/The-Aether-Team/The-Aether) | Study modern-port and restoration structure, integration boundaries and version-specific documentation; not AoA content replacement. | Reuse permitted techniques only after loader and license review. Compare how completely a migration keeps recognizable behavior, not raw content counts. |

**Rights gates:** GeckoLib MIT license was read at blob `491454db53d5a2166d8a472d07cc8b60e6d016fb`. The Aether's official repository states LGPL-3.0 for source from Minecraft 1.7 onward and distinguishes older unlicensed code; inspect the exact files and asset terms before reuse. AoA's [official historical project page](https://tslat.github.io/Advent-Of-Ascension/) describes private-use modification limits. Default-branch `LICENSE` and `LICENSE.txt` lookups returned 404 in this pass, so **no blanket permission for public merged-mod redistribution has been established**. Retain existing rights/provenance gates.

### Shared-work proposals

- Enderloom/Minecraft-Mod-Vault: share an agreed versioned content-identity/provenance receipt, including source version, registry mapping, dependency and runtime-acceptance state. Keep private playtest artifacts private.
- JetSetCraft: reuse provider-present/provider-absent encounter test cases and inventory return safety requirements, not foreign capability assumptions.
- Hover: candidate reuse of lawful resource inspection schemas and version labels for previews; reading a model is not proof of a registered, obtainable or playable entity.

- [ ] Prove one complete dimension route using the existing restoration pipeline before adopting new infrastructure.
- [ ] Keep source-presence, renderability and full gameplay acceptance as distinct fields across tools.

### Reuse admission gates

These are **candidate foundations and experiments**, not selected dependencies or measured improvements. Before reuse: pin the exact version/commit and loader; inspect its source and dependency tree; record code, asset, trademark and redistribution terms separately; keep required notices; verify permission where terms are restrictive or unclear. Public visibility is not a license. A current default-branch license is evidence for that snapshot, not every historical release. Prefer an upstream dependency/API or a small original adapter over a fork when it preserves compatibility. Do not copy proprietary game assets or publish private fixtures.

For every admitted experiment retain baseline and candidate artifacts, representative native workloads, correctness/feature parity, cold/warm latency, p95 frame/tick time, memory, interrupted-save/recovery evidence and rollback. Promote only after the actual target improves without losing requirements. Cross-project sharing below is an interface proposal, not permission to change another project's implementation or declare integration complete.
