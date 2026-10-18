# Extra Realmstones and dimension compatibility

**Owner-requested expansion · implementation and testing backlog.** The goal is a polished, optional bridge between AoA's realmstone travel and the major dimension mods, with native progression, safe arrivals and reliable return travel preserved.

[All compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Worlds and travel](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Dimensions) · [Progress and evidence](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Progress)

## Continue the existing addon

The linked project is already titled **AoA: Extra Realmstones**, by **NagusPacka**. Its listed release is **2.1 for Minecraft 1.16.5 / AoA 3.6**, dated March 21, 2024. It lists End, Twilight Forest, Atum, DivineRPG, Eternal Tales, Blue Skies, Bumblezone, Undergarden and Aerial Hell integrations, including realmstones and related portal/banner/trophy features. That historical listing does not certify modern compatibility. [Original project](https://www.curseforge.com/minecraft/mc-mods/aoa-end-realmstone) · [Exact 2.1 file](https://www.curseforge.com/minecraft/mc-mods/aoa-end-realmstone/files/5201047)

The owner reports permission from the original author to improve and update the addon. Preserve NagusPacka's attribution and record the permission's scope in project provenance. The listing remains All Rights Reserved; do not silently relabel the original code or assets as open source. A source repository was not linked in the inspected listing. Source access, release lineage and the existing implementation must be checked before claiming a completed port.

**Working direction:** continue this work as an optional Extra Realmstones addon, with a clean adapter boundary to the owner's AoA/Enderloom build. Keep its source, tests and release artifacts identifiable instead of scattering integration logic across unrelated mods.

## Dimension target roster

The roster combines the predecessor's listed integrations with the owner's request for popular dimension mods. CurseForge's [2026 dimension-mod selection](https://blog.curseforge.com/minecraft-dimension-mods/) is a discovery source, not a guarantee of a matching 1.20.1 release or an exhaustive popularity ranking. Every row below is **unqualified** until its exact release and adapter pass the tests.

| Target | Lane | Required adapter decision / tests |
|---|---|---|
| Vanilla End | Predecessor baseline | Dragon/progression policy, spawn platform and gateway/exit behavior; no destructive platform regeneration near builds |
| The Twilight Forest | Predecessor + priority | Preserve entry conditions and boss progression; distinguish access from progression unlocks |
| The Aether | Priority | Resolve its native entry/exit contract and safe floating-island arrival; check relevant installed addons separately |
| Blue Skies | Predecessor + priority | Separate Everbright and Everdawn destinations and unlocks; preserve the pinned release's entry flow |
| The Bumblezone | Predecessor + priority | Preserve native entry/return behavior and destination context; avoid return loops |
| The Undergarden | Predecessor + priority | Check native activation, destination placement, hazards and return context |
| The Midnight | Priority discovery | Pin a supported release before selecting a rift/travel adapter; do not guess a modern port |
| The Betweenlands | Priority discovery | Pin a supported release and preserve its dimension-specific survival and progression rules |
| Ad Astra | Priority discovery | Treat each planet separately; never silently bypass travel unlocks or life-support requirements |
| Dimensional Doors | Priority discovery | Dynamic pockets require destination identity and ownership checks, not one hard-coded dimension key |
| Eternal Starlight | Priority discovery | Check matching loader/version and native entry/progression contract |
| AbyssalCraft | Historical / version-gated | Preserve separate realm unlocks; no invented target-build support |
| Atum | Predecessor / version-gated | Verify the actual compatible release and native travel rules |
| DivineRPG | Predecessor | One qualified adapter record per dimension; retain progression ordering |
| Eternal Tales | Predecessor | Audit each destination and reward mapping against its exact release |
| Aerial Hell | Predecessor / version-gated | Verify destination, entry and safe-return contracts before enabling |

This is the initial audit queue, not a permanent limit. Add other popular installed dimensions after checking the actual pack manifest and supported release. Dimension-overhaul mods which modify the existing Nether or End should be tested against those same world keys rather than receiving invented extra dimensions.

## What makes this better than a collection of teleport items

- **Discoverable travel journal:** illustrated destination, source mod, unlock conditions, travel warnings, realmstone acquisition and verified return instructions.
- **Data-driven integration records:** stable dimension keys, required mod/version range, activation policy, unlock predicates, destination adapter and explicit return policy.
- **Optional dependencies:** missing mods disable only their integrations with a useful explanation. No hard load of absent classes or silent invalid registry entries.
- **Respect native progression:** default to unlocking a realmstone only after legitimate entry or an equivalent approved progression condition. A configurable shortcut mode must be labeled and server-controlled.
- **World-safe arrivals:** prefer the destination mod's supported teleport API/placement rules. Reject unsafe or unresolved destinations without carving through player builds.
- **Reliable return context:** retain source dimension and approved return point per traveler; validate them before use. Handle destroyed portals, unloaded chunks and removed dimensions without trapping the player.
- **Useful collection rewards:** optional banners and trophies should have distinct identity and documented acquisition. Additive loot hooks must not replace an entire other mod's loot table.
- **Accessible presentation:** readable destination names, color-independent icons, localization and reduced-effects options.
- **Fast operation:** cache integration discovery by resource/config generation; no full registry or pack scan on every tick or item hover. Budget chunk-search work and invalidate caches safely.

These are implementation requirements, not claims about shipped features.

## Recovery and transaction requirements

1. Validate the installed mod, target dimension, unlock state and player travel permission on the server.
2. Resolve a candidate arrival without charging the player or overwriting blocks.
3. Limit chunk loading/search; fail clearly if a safe destination cannot be established.
4. Recheck world bounds, hazards, collision clearance, ownership/protection rules and the target mod's constraints.
5. Commit travel and any resource cost exactly once. Failed, cancelled or duplicate requests must not consume resources twice or create extra portals.
6. Save the return context atomically with the operation and prove disconnect/restart behavior.
7. Test multiplayer passengers, mounts and pets only where an adapter explicitly supports them; unsupported cases must fail safely.

Do not disable claim protection or change difficulty/progression rules as a generic compatibility fix.

## Implementation checklist

- [ ] Inventory the 2.1 release's classes, metadata, recipes, loot additions, realmstones, portal behavior and optional-dependency checks.
- [ ] Obtain or identify matching upstream source; distinguish original behavior from a new design.
- [ ] Preserve credits and permission provenance, including third-party dependencies/assets.
- [ ] Audit the latest local Enderloom/AoA implementation before duplicating any portal or realmstone API.
- [ ] Build and test the core dimension adapter contract independently of optional mods.
- [ ] Port one representative route, then qualify the End and Twilight Forest baseline before expanding.
- [ ] Add the other high-priority dimensions with per-release records and reproducible round-trip tests.
- [ ] Preserve or explicitly migrate older realmstone identities and saved destination data.
- [ ] Check the predecessor's trophy fixes and ensure additive, non-destructive loot integration.
- [ ] Add recipe/guidebook integration, localization, banner/trophy previews and recovery instructions.
- [ ] Test all optional dependencies absent, one at a time and in the supported combined pack.
- [ ] Publish real runtime, save-migration and performance evidence before marking any target supported.

## Minimum test record per destination

Exact Minecraft/loader/AoA/addon/dimension-mod versions and hashes; unlock and acquisition route; first entry; repeat entry; return; death; disconnect mid-travel; removed portal; unavailable dimension; border/hazard/protected-block arrival; failed/cancelled request; inventory/resource preservation; multiplayer; resource reload; old-save migration; chunk-search budget and startup/frame-time measurements.

**No destination is release-qualified merely because its name appears in this roster or an item/model was generated.**
