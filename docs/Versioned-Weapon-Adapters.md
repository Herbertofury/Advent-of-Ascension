# Versioned weapon adapters · reuse native capabilities

**Research and integration plan, not an installed compatibility layer.** Keep 1.20.1 as the first target while designing a separate 1.21.1 adapter. Newer AoA already provides useful per-stack weapon configuration; do not build a second competing stats system when the native component can own that value.

## Execution-time upstream refresh

Checked 18 October 2026: official AoA default branch `1.21` at `7919b5fe48599e6105c5740937ce36c36ef21d16`; all 46 files under its changelog directory were retrieved and hashed. The official Modrinth production release is **3.7.16.1 for Minecraft 1.21.1**, published 6 January 2026. The latest TaCZ GitHub release returned by its latest endpoint is **1.1.8-hotfix**, published 25 May 2026. The official production listing is newer: **TaCZ 1.1.8-hotfix2 for Forge 1.20.1**, published 2 October 2026 ([file 9037989](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero/files/9037989)). Its changelog includes a backported vulnerability fix. GitHub latest-release metadata alone is insufficient for a production pin. These are separate upstreams, not a statement that both work together on 1.21.1.

[Official AoA repository](https://github.com/Tslat/Advent-Of-Ascension) · [AoA release](https://modrinth.com/mod/adventofascension/version/vIo8vp51) · [TaCZ hotfix](https://github.com/MCModderAnchor/TACZ/releases/tag/1.1.8-hotfix) · [Refresh receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-upstream-refresh-20261018.json)

## Two distinct native contracts

| Concern | Pinned 1.20.1 / 3.7.1 | Current 1.21.1 / 3.7.16.1 |
|---|---|---|
| Conventional weapon parameters | Constructor fields, getter inheritance and subclass overrides | `GunStats` component read from the actual stack, with a default-stack fallback |
| Ammo selection | `getAmmoItem` is a base identity; custom overrides can use tags/exemptions | Optional item-holder set in the weapon component; current ammo predicate reads the stack |
| Item consumption | Old helper/override paths require their own tests | Current AoAGun uses TME InventoryUtil, then Ammo Void Pouch fallback |
| Blaster resources | Spirit and subclass behavior remain distinct from item ammo | `BlasterStats` carries Spirit/charge/timing fields; raytrace distance applies where the weapon actually uses it |
| Sniper sight | Version-specific native path | Native sniper-scope component supports its own name/zoom serialization |
| Persistence | Older item/NBT contracts | Native persistent and network-synchronized component registrations |

Do not transfer the 1.20.1 ammo helper's suspected split-stack behavior to the newer release by assumption. Its lookup implementation has changed. Likewise, a new component name is not proof that every old effect, projectile or acquisition route has semantic parity.

## Native configuration worth integrating

The following keys were found in the pinned current source and independently observed in the matching released class disassembly. The audit does not execute the codecs or validate a live item.

| Component ID | Useful serialized fields | Proposed attachment use |
|---|---|---|
| `aoa3:gun_stats` | damage, ticks_between_shots, recoil_modifier, unholster_time_modifier, ammo, full_auto | Receivers, handling, fire controls and ammo compatibility |
| `aoa3:blaster_stats` | damage, ticks_between_shots, spirit_cost, charge_up_ticks, beam_distance | Spirit conduits, charge units and supported beam barrels |
| `aoa3:shotgun_stats` | pellets, pellet_spread, knockback_modifier | Pellet-count, spread and recoil/knockback-oriented upgrades |
| `aoa3:sniper_scope` | scope, zoomStrength | Scope visuals and magnification |
| `aoa3:item_use_sound` | sound, pitch | Compatible cosmetic firing-sound selection |

Read the implementation boundaries before making an editor:

- **GunStats:** ammo is a registry-backed optional holder set, not a single free-text item ID. The basic codec uses numeric fields without the gameplay editor's own explicit safe ranges. Validate proposed modifications on the server and present effective values clearly. [Source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/datacomponent/GunStats.java)
- **SniperScope:** serialization resolves a scope name under AoA's scope-texture directory. Do not advertise arbitrary texture namespaces as already supported by that codec. [Source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/datacomponent/SniperScope.java)
- **Ammo Void Pouch:** its stored contents map item identities to counts. Adding a stack with a nonempty component patch is rejected in the inspected component implementation. Keep customized ammo out of lossy item-only storage; do not bypass that guard. [Source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/library/object/container/AmmoVoidPouchComponent.java)
- **Default components:** AoAGun falls back through its default stack when a component is absent. New adapter-created items need validated defaults; do not strip the default component and assume the fallback repairs it. [Source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/item/weapon/gun/AoAGun.java)

[Released hashes and key sets](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-component-audit-1.21.1.json) · [Original bounded audit tool](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-component-audit-tool-v1.zip)

## Adapter implementation order

1. Snapshot the actual equipped stack and its versioned native contract. Cache derived presentation by stack revision, resource generation and adapter version; no repeated directory scans.
2. Compose a proposed assembly without mutating inventory. Preserve unknown components and original identity; show exact resource and behavior changes before committing.
3. On 1.21.1, write supported changes through the native components and preserve component defaults/stream rules. On 1.20.1, use an explicitly separate adapter; do not pretend newer components exist there.
4. Route native projectile/effect behavior through its existing hooks. A cosmetic TaCZ display cannot silently replace Spirit, ammo pouches, enchantments or damage authority.
5. Resolve material payment and salvage under server authority with stale-revision rejection and rollback. The published pure planner is not an atomic game transaction.
6. Measure equip/modify/inspect, dense projectile combat and cold/warm startup against equivalent work before expanding to the full arsenal.

## Required regression cases

- Item/component save-load round trips and client synchronization.
- Missing or unknown components, custom item tags, invalid numeric values and altered defaults.
- Mixed ammo, customized ammo, empty/filled pouch fallback, insufficient cost and creative rules.
- Semi-auto held trigger versus a fresh press; no unintended continued charging.
- Scoped weapon custom texture/zoom and interrupted ADS.
- Source effects, attribute hooks and per-stack overrides preserved with attachment changes.
- Old-to-new migration is explicit and reversible; no automatic title-based semantic merge.

The newer AoA hotfix specifically lists scope customization, semi-auto and Ammo Void Pouch fixes. The TaCZ hotfix also lists a held-trigger charging fix and an ammo-box consumption fix. Include these as regression targets rather than assuming a compatibility layer inherits the fixes automatically. [AoA changelog](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/changelogs/3.7.16.1.md) · [TaCZ changelog](https://github.com/MCModderAnchor/TACZ/releases/tag/1.1.8-hotfix)

Original upstream source remains with its authors. This page publishes factual schema observations and original integration planning, not a redistribution of their source or game JARs.

[Actual released TaCZ model/animation parser checks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/TaCZ-Released-Parser-Check) now exercise the hotfix2 class bytes with explicit isolated-harness boundaries.
