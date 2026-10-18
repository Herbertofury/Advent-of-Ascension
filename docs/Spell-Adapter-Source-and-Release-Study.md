# Spell adapters: actual source and released-file study

**2026-10-18 · Static engineering study. No Minecraft runtime acceptance claimed.**

The published JARs were downloaded through the Curse Maven coordinates linked by their official file pages and inspected as archives/class files. The public source archives were separately downloaded at exact commits. No addon code was executed.

| Reference | Released file | Pinned source | Inspected released classes |
|---|---|---|---:|
| ArsArms | [1.20.1–3.0.4, file 7949131](https://www.curseforge.com/minecraft/mc-mods/arsarms/files/7949131) | [edb4f00](https://github.com/mumu17-git/ArsArms/tree/edb4f00cdbace81b9b7ab4867dfc6dc84664016b) | 9 |
| IronsArms | [1.20.1–3.0.6, file 7949129](https://www.curseforge.com/minecraft/mc-mods/ironsarms/files/7949129) | [fc5c153](https://github.com/mumu17-git/IronsArms/tree/fc5c153f4939307c80b4dffda37d8725ffb61cd5) | 8 |

[File hashes, dependency metadata and class/member evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/spell-adapter-source-and-release-study.json).

## What the code teaches us

### ArsArms

The [bullet-event implementation](https://github.com/mumu17-git/ArsArms/blob/edb4f00cdbace81b9b7ab4867dfc6dc84664016b/src/main/java/com/mumu17/arsarms/event/ArsArmsBulletEvents.java) uses TaCZ fire/impact events and Ars Nouveau ReactiveCaster. The inspected code charges a stored gun resource during firing and later casts on impact. Its impact path reads the player's current main-hand stack and tracks casting eligibility by player UUID.

For AoA, preserve the useful event separation but attach immutable source-weapon/effect provenance to each successful shot or projectile. Test two weapons fired before impact, item swaps, misses, piercing, multiple pellets, cancelled damage and duplicate callbacks. A shooter-level flag alone cannot represent the identity of every outstanding shot.

The [charging handler](https://github.com/mumu17-git/ArsArms/blob/edb4f00cdbace81b9b7ab4867dfc6dc84664016b/src/main/java/com/mumu17/arsarms/network/RequestSyncChargedManaMessage.java) and [client charging loop](https://github.com/mumu17-git/ArsArms/blob/edb4f00cdbace81b9b7ab4867dfc6dc84664016b/src/main/java/com/mumu17/arsarms/client/ChargeManaToAmmoBoxTick.java) are important transaction references. Our adapter should accept an intent to charge a particular stack, then calculate the allowed transfer on the server from current resources and capacity. Never trust a client-provided desired balance. Validate stack identity, bounds, enchantment/effect eligibility and transaction ordering.

### IronsArms

The [bullet-event implementation](https://github.com/mumu17-git/IronsArms/blob/fc5c153f4939307c80b4dffda37d8725ffb61cd5/src/main/java/com/mumu17/ironsarms/event/IronsArmsBulletEvents.java) stores spell ID/level for attachment to projectile persistent data. This is a stronger starting point for shot-specific provenance than reading only the current item at impact. Its surrounding pending/casting state is still keyed by player and must be considered when adapting the design.

The impact path handles target-specific spell data and temporarily changes player position/orientation around casting, with restoration in a finally block. Our design should prefer an explicit projectile-impact casting context when the spell API supports one. If an integration truly requires temporary state, test all restoration paths, nested callbacks, continuous casts, recasts, dimension transitions and exceptions. Do not copy temporary relocation into every spell adapter by default.

The [Arcane Anvil mixin](https://github.com/mumu17-git/IronsArms/blob/fc5c153f4939307c80b4dffda37d8725ffb61cd5/src/main/java/com/mumu17/ironsarms/mixin/ArcaneAnvilMenuMixin.java) creates a copied result stack with an inscribed spell when the ordinary result is empty. AoA's salvage/modular workbench also needs separate preview and commit phases. Test actual ingredient consumption, result extraction, shift-click, creative mode, inventory-full cases and cancellation. A correct-looking output preview does not prove a safe crafting transaction.

## Integration boundaries

Both addons target TaCZ IGun items. Native AoA items do not become compatible merely because a model uses TaCZ-style geometry. Keep an explicit AoA-native item/resource/event adapter, preserve saved item identity and use optional dependencies only where their contracts are verified.

Both inspected Gradle property files pin TaCZ 1.1.7-hotfix2. That is source build metadata, not proof of compatibility with every later TaCZ build. The released metadata is recorded separately. Both JARs declare MIT; ArsArms also includes a repository LICENSE.txt, while the inspected IronsArms source snapshot has no top-level license file. Preserve attribution and check individual reused material before incorporating code.

The ArsArms repository README still describes an ammo-box workflow, while its current released source handlers and public instructions use guns. Treat documentation drift as a reason to verify the exact release, not to combine the two workflows into player guidance.

## Our resulting QA contract

These are preventive requirements for our implementation, not claims that a runtime exploit or bug has been reproduced in either reference mod.

- [ ] Exact source weapon, assembly revision, resource receipt, shooter, world/session and successful-shot ID per effect event.
- [ ] Resource transfer uses server-calculated amounts, cannot mint value, and fails without partial mutation.
- [ ] Multi-projectile and on-hit effects define whether costs and procs are per primary shot, per projectile or per target.
- [ ] No stale current-hand lookup for effects belonging to an earlier shot.
- [ ] Pending entries expire and clear on logout/session changes; duplicate impacts cannot recast.
- [ ] Continuous spells preserve source identity and cannot refill a player's pool from an unrelated held item.
- [ ] Workbench preview never consumes inputs; commit revalidates and changes input/output atomically.
- [ ] Avoid per-frame inventory scans and repeated reflective integration lookup. Cache stable capabilities and assembly definitions; invalidate when they change.
- [ ] Test optional-mod removal, save migration, dedicated server behavior and measured costs before acceptance.

[Reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Ars Armorer file study](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ars-Armorer-Direct-Study) · [Modular armory](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage)
