# Compatibility Targets

**The central AoA / Enderloom compatibility backlog.** Checked 2026-10-18. A target on this page is a goal, not a claim that an integration is implemented or tested. Advent of Ascension is created by Tslat and contributors.

[Runtime acceptance checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist) · [Current progress](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Progress) · [Premium weapon overhaul](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Weapon upgrade backlog](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog) · [Reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

## Target matrix

| Integration | Why it belongs here | Current evidence / status | Release gate |
|---|---|---|---|
| **L_Ender's Cataclysm** | Explicit owner target; boss combat, equipment and progression must coexist with AoA | Target recorded; pairwise and combined runtime qualification open | Native boss mechanics, damage ownership, rewards and progression remain correct |
| **Apotheosis** | Explicit owner target; affixes, sockets, enchanting and combat progression | Target recorded; pairwise and combined runtime qualification open | No duplicated procs, corrupted equipment or unintended damage multiplication |
| **Timeless and Classics Zero (TaCZ)** | Explicit owner target; optional premium animated AoA weapon presentation | Original authoring prototype started; native adapter and runtime qualification open | Original AoA costs/effects and item identity survive; premium presentation and optional reloads work correctly |
| **Curios** | Already named in the owner's published runtime acceptance checklist | Target recorded; slot, modifier and lifecycle qualification open | Equip/unequip, death, reconnect and removal remain safe |
| **Ars Nouveau + ArsArms** | Owner-selected magic-through-firearms research / optional integration candidate | Study target, not an approved mandatory dependency or working AoA bridge | Matching release, exact mana contract and server-authoritative spell behavior demonstrated |
| **Iron's Spells 'n Spellbooks + IronsArms** | Owner-selected magic-through-firearms research / optional integration candidate | Study target, not an approved mandatory dependency or working AoA bridge | Matching release, spell storage, resource accounting and persistence demonstrated |
| **Other Noxviola-pack mods** | Existing pack-level acceptance requirement | Exact pack manifest and release matrix still required | Every detected integration gets a named row and an evidence record before support is claimed |

The first implementation lane is the actual **Minecraft 1.20.1 / Forge target build**. Record exact dependency versions and hashes before testing. A modern upstream branch, a historical AoA source reference or a successful launch with another loader does not certify this build. Later versions require their own matrix.

## Dimension mods and Extra Realmstones

The owner also requests broad compatibility with popular dimension mods and continuation of NagusPacka's AoA: Extra Realmstones addon. See the dedicated [dimension roster and Extra Realmstones implementation plan](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extra-Realmstones-and-Dimension-Compatibility) for the predecessor integrations, priority targets, version gates, safe-travel contract and tests. These are requested targets; no new destination has been runtime-qualified.

## L_Ender's Cataclysm

[Official project](https://www.curseforge.com/minecraft/mc-mods/lendercataclysm) · [Developer source](https://github.com/lender544/new1.20.1)

- [ ] Pin the matching Cataclysm release, loader and required libraries; reproduce both mods independently first.
- [ ] Test AoA melee, guns, blasters, staves, summons and damage-over-time against representative Cataclysm bosses and multipart targets.
- [ ] Preserve boss immunity windows, damage caps, phase transitions, shields, projectile restrictions and scripted encounters. Compatibility must not silently bypass intended mechanics.
- [ ] Verify hit attribution, aggro, ownership and kill credit, including pets, delayed projectiles and multiplayer.
- [ ] Verify AoA skill/progression rewards once per legitimate event; no duplicate rewards from multipart hits or chained effects.
- [ ] Check Cataclysm weapons and effects against AoA bosses and mobs in the opposite direction.
- [ ] Test loot, structures, dimension travel and existing-world behavior; do not overwrite another mod's data or force cross-mod loot additions without a documented policy.
- [ ] Check custom renderers, particles, boss bars and visual effects with the supported graphics stack.

## Apotheosis

[Official source](https://github.com/Shadows-of-Fire/Apotheosis)

- [ ] Pin the correct version and its actual module/data layout; do not mix old module assumptions with another release.
- [ ] Explicitly map eligible AoA weapon and armor categories to affix/socket/enchantment behavior. Unsupported categories must remain explicit.
- [ ] Trace damage and proc ordering for AoA projectiles, multishot, explosive splash, rapid-fire weapons, summons and magic.
- [ ] Ensure an affix or on-hit effect fires only as intended; prevent recursive damage chains and double application by AoA and TaCZ adapters.
- [ ] Test reforging, salvaging, socket insertion/removal, enchanting and repair without losing AoA components, charges, durability, custom data or identity.
- [ ] Verify generated equipment and rarity/loot rules without duplicate modifiers or trivialized progression.
- [ ] Test with relevant Apotheosis features disabled as well as enabled, where supported by that pinned release.
- [ ] Round-trip enhanced equipment through death, storage, trading, reconnects, world reloads and migration.

## TaCZ: premium presentation without losing AoA behavior

[Official source](https://github.com/MCModderAnchor/TACZ) · [Weapon design](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Detailed work list](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog) · [Quality references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library)

- [ ] Preserve native AoA item IDs, saved properties, projectile behavior, costs, cooldowns and special effects. A generic TaCZ ballistic replacement is not equivalent.
- [ ] Implement optional global, family and per-weapon presentation settings with a safe original-model fallback.
- [ ] Author distinct original models, textures, moving mechanisms and equip, fire, aim, inspect, recovery and appropriate reload/charge animations.
- [ ] Keep **manual reloading independently optional**. Native inventory ammo, mana, Spirit or other costs remain the default where appropriate. Cosmetic clips never replenish resources.
- [ ] Keep shooting, resource payment and special-effect admission server-authoritative; animation callbacks cannot grant free shots or duplicate proc effects.
- [ ] Test the real weapon contract. For example, the source-observed 1.20.1 Baronator has an extra grenade branch after a successful native shot; a plain rifle data file would omit that behavior.
- [ ] Validate first- and third-person hands, sight alignment, left-handed play, FOV, swimming, riding and interrupted transitions.
- [ ] Verify missing TaCZ, invalid assets and failed resource reloads leave original AoA items usable.
- [ ] Measure startup, resource-reload time, memory and frame-time distributions with the same scene and workload. No FPS or zero-regression claim before measurements.

The current original geometry/keyframe prototype is an authoring milestone, not proof of a playable TaCZ/AoA integration. Its runtime bridge, sounds, hands, multiplayer and performance gates remain open.

## Curios

- [ ] Declare optional access only when the pinned API is present; dedicated servers must not load client classes.
- [ ] Verify slot eligibility and prevent duplicate attribute/ability application across slots and ordinary equipment.
- [ ] Remove effects exactly once on unequip, death, logout and dimension change as required by the native contract.
- [ ] Preserve stack data and provide safe missing-mod/save behavior rather than silently deleting equipment.

## Magic adapters and reference packs

ArsArms and IronsArms are **optional investigation lanes**. Their existence does not establish a working AoA resource adapter. Keep the originating mod's mana/Spirit costs distinct, and record which pool pays for each action. Test interruption, failed casts, Creative mode, full inventories and reconnects for duplication or loss.

The Create Armorer, Ars Armorer and Helldivers TaCZ packs remain [visual/animation reference projects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library). A reference pack is not automatically an AoA runtime dependency, nor permission to redistribute its models, textures, animations or sounds. Keep code and art licensing separate.

## Shared acceptance matrix

For each named integration, record:

1. Minecraft, loader, AoA build/hash, dependency versions/hashes and relevant configuration.
2. Baseline AoA alone, the other mod alone, the pair, and the combined supported pack.
3. Client and dedicated server results, including missing optional dependency startup.
4. Reproducible natural gameplay cases and expected resource, damage, reward and saved-state outcomes.
5. Death, disconnect, dimension travel, reload and migration cases; corrupted saves are not an acceptable fallback.
6. Cold/warm startup, memory, CPU/GPU frame times and low-percentile results with hardware and workload documented.
7. Linked test logs, screenshots or captures, exact defects and remaining gaps.

**Status vocabulary:** requested → inspected → implemented → pairwise tested → combined-pack tested → release-qualified. Only advance a row when its evidence supports that stage. Source inspection and generated assets cannot substitute for runtime proof.
