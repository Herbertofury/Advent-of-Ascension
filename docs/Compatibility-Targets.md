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
| **Ars Nouveau** | Explicit owner compatibility target; spells, resources and magical progression | Requested; full integration unqualified; ArsArms remains a bridge to evaluate | Correct spell/resource accounting, ownership, progression and optional dependency handling |
| **Iron's Spells 'n Spellbooks + IronsArms** | Owner-selected magic-through-firearms research / optional integration candidate | Study target, not an approved mandatory dependency or working AoA bridge | Matching release, spell storage, resource accounting and persistence demonstrated |
| **Butchery** | Explicit owner target; AoA creature processing and rewards | Requested; mob mappings and loot/skill interactions unqualified | No lost progression drops or duplicated carcass/reward paths |
| **Alex's Mobs** | Explicit owner target; creature behavior, combat and progression | Requested; exact release and Citadel pairing unqualified | Native AI, tame/owner state, drops and AoA rewards remain correct |
| **Farmer's Delight** | Explicit owner target; AoA ingredients, crops and cooking | Requested; recipe/tag and workstation integration unqualified | Correct ingredients, yields, containers and effects without recipe loops |
| **Kaleidoscope Cookery** | Explicit owner target; complementary food and cooking integrations | Requested; exact release APIs/data and recipe mappings unqualified | Compatible recipes and food effects without duplication or silent overrides |
| **Create** | Explicit owner target; mechanical production and expedition logistics | Requested; recipes and automation unqualified | Preserve costs, stack data and progression; no duplication loops |
| **Botania** | Explicit owner target; magical crafting and optional presentation | Requested; mana/resource contracts unqualified | Keep Mana and AoA resources distinct; no free-casting loops |
| **Applied Energistics 2** | Explicit owner target; storage, crafting and supply preparation | Requested; transaction and pattern integration unqualified | No duplicated withdrawals, lost data or unauthorized remote resupply |
| **Gateways to Eternity** | Explicit owner target; one themed challenge per accepted dimension | Requested; encounter ledger and runtime qualification open | Correct waves, progression gates, rewards, cleanup and performance |
| **Scorched Guns** | Explicit owner target; appropriate shared ammo and AoA participation | Requested; ammo/kill-attribution mappings unqualified | Preserve native weapon behavior and debit resources exactly once |
| **Terramity** | Explicit owner target; appropriate shared ammo and AoA participation | Requested; ammo/kill-attribution mappings unqualified | Preserve native weapon behavior and debit resources exactly once |
| **Malum** | Explicit owner target; spirit/magic progression and combat | Requested; resource and reward contracts unqualified | Keep each mod's spirits/resources distinct and avoid duplicated harvest rewards |
| **Born in Chaos** | Explicit owner target; creature combat, rewards and themed challenges | Requested; roster/behavior qualification open | Preserve special mob mechanics, attribution and progression rewards |
| **TaCZ Turrets** | Explicit owner target; mount every supported AoA TaCZ weapon | Requested; native weapon hosting and turret qualification open | Correct costs, special effects, aiming/ownership, automation policy and safe fallback |
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

## Creatures, harvesting and cooking

### Butchery

[Owner-selected project](https://www.curseforge.com/minecraft/mc-mods/butchery). This is the separate jmods **Butchery mod**, not merely AoA's historical Butchery skill. Its project page offers a mob-addition datapack route and notes a Farmer's Delight food option; inspect those existing extension points before writing a duplicate integration.

- [ ] Pin the target release and inspect its supported mob/tag/datapack mechanism.
- [ ] Define appropriate processing outputs for each supported AoA creature; exclude unsuitable entities rather than assigning generic meat to everything.
- [ ] Keep ordinary loot, carcass conversion, trophy/progression items and AoA skill rewards consistent; explicitly prevent duplicate drops or lost quest/boss rewards.
- [ ] Test all processing stages, tool costs, full inventories and interruption/reload behavior.
- [ ] Test the combined Butchery + Alex's Mobs + Farmer's Delight configuration and any existing addon before claiming our adapter is necessary or complete.

### Alex's Mobs

[Owner-selected project](https://www.curseforge.com/minecraft/mc-mods/alexs-mobs). The project declares Citadel as required; pin the matching dependency rather than treating it as interchangeable with another animation library.

- [ ] Qualify AoA projectile, melee, status and summon interactions with representative aquatic, flying, multipart and unusual creatures present in the selected release.
- [ ] Preserve taming, owner attribution, mounts, alliances and special creature behavior.
- [ ] Define AoA skill/kill/drop eligibility deliberately and award each event once; do not broadly tag all new mobs as equivalent progression targets.
- [ ] Verify spawn rules and dimension/biome tags without replacing another mod's natural spawn configuration.
- [ ] Audit existing Butchery integration and avoid duplicate corpse or loot processing.

### Farmer's Delight

[Owner-selected project](https://www.curseforge.com/minecraft/mc-mods/farmers-delight).

- [ ] Map appropriate AoA crops, fish, meats and ingredients into exact supported tags and workstation recipes.
- [ ] Add deliberate cutting-board, cooking-pot and skillet routes where the pinned API/data permits, with clear yields and tool costs.
- [ ] Preserve food effects, nutrition, saturation, containers/remainders and custom stack data.
- [ ] Check cooking/cutting and other cross-mod conversions for duplication loops and progression shortcuts.
- [ ] Validate crop/soil interactions and AoA skill XP without double rewards from automation or repeated callbacks.
- [ ] Show the actual cross-mod recipes and ingredient images in the wiki and supported in-game recipe browser.

### Kaleidoscope Cookery

[Owner-selected project](https://modrinth.com/mod/kaleidoscope-cookery). The listing includes1.20.1 and1.21–1.21.1 across multiple platforms; the adapter still needs an exact loader/release pin.

- [ ] Inspect the selected release's ingredient, recipe, workstation and food-effect contracts before defining mappings.
- [ ] Add appropriate AoA ingredients and dishes with distinct presentation and documented acquisition.
- [ ] Preserve containers, quantities, effects and stack data through preparation and consumption.
- [ ] Qualify coexistence with Farmer's Delight and Butchery; avoid silent recipe replacement, overlapping conversion exploits or double nutrition/XP effects.
- [ ] Test optional-mod absence and resource reload, and publish exact illustrated recipes once implemented.

All four remain targets until their pairwise and combined-pack tests pass. Shared food tags are not blanket proof of complete compatibility.

## Automation, gateways and shared ammunition

See [Create, Botania, AE2, dimension-themed Gateways and shared-ammo designs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Automation-Gateways-and-Shared-Ammunition) for concrete proposed gameplay loops and the implementation/QA checklist. Scorched Guns and Terramity are scoped to appropriate ammo interoperability and AoA participation; their full weapon conversion is not assumed.

## Magic, hostile creatures and mounted weapons

### Malum

[Owner-selected target](https://www.curseforge.com/minecraft/mc-mods/malum).

- [ ] Pin the selected release and inspect its spirit-harvest, ritual, equipment and damage contracts.
- [ ] Design deliberate AoA mob/realm integrations and optional thematic crafting paths; do not treat Malum spirits and AoA Spirit/Soul Power as the same resource.
- [ ] Preserve harvest eligibility, ownership, tool requirements, ritual costs and progression.
- [ ] Test overlapping kill, damage and harvest events with AoA skills and other magic mods to avoid duplicated rewards.
- [ ] Qualify client effects, persistent item data, multiplayer and optional-mod absence.

### Ars Nouveau

[Owner-selected target](https://www.curseforge.com/minecraft/mc-mods/ars-nouveau). This is now a full requested compatibility target. ArsArms is an existing optional bridge to inspect, not a substitute for qualifying the broader integration.

- [ ] Qualify spells and summons against AoA creatures/bosses without bypassing native encounter rules.
- [ ] Preserve spell ownership, mana costs, cooldowns and damage/kill attribution; distinguish native AoA resource pools.
- [ ] Investigate optional realm-themed recipes, magical utilities and weapon effects with explicit progression and resource contracts.
- [ ] Test repeated/chain effects, summons, automated casting and skill rewards for duplicate or unintended credit.
- [ ] Reuse or contribute to appropriate existing integration points before adding parallel incompatible systems.

### Born in Chaos

[Owner-selected target](https://www.curseforge.com/minecraft/mc-mods/born-in-chaos).

- [ ] Pin the supported creature roster and test AoA melee, projectiles, magic, summons and status effects against special behaviors.
- [ ] Preserve native spawn, transformation, death/revival and drop rules where present in the selected release.
- [ ] Define eligible AoA skill/kill rewards once per legitimate encounter, including indirect and multipart cases.
- [ ] Check existing More Gateways support before adding overlapping encounter definitions; optional AoA crossover challenges must remain separately identifiable.
- [ ] Test difficulty scaling, combined mob density, visuals, multiplayer and frame/tick-time budgets.

### TaCZ Turrets: every supported upgraded AoA gun

[Owner-selected gallery](https://www.curseforge.com/minecraft/mc-mods/tacz-turrets/gallery) · [Project and source links](https://www.curseforge.com/minecraft/mc-mods/tacz-turrets)

**Goal:** every supported TaCZ-format AoA weapon should have a qualified mounted-turret mode, keeping its distinctive native behavior. A client-only model replacement is insufficient for this requirement; the implementation needs a real weapon-host adapter.

- [ ] Pin matching TaCZ, turret and AoA releases and inspect the turret's actual gun/ammo API before choosing a carrier or adapter design.
- [ ] Preserve original item data and reversible handheld/mounted use. Never duplicate the original stack when inserting or removing a gun.
- [ ] Supply ammunition or the appropriate magical resource from a real, server-authoritative account. No free firing for player-only resource implementations.
- [ ] Preserve unusual AoA projectiles and effects, including Baronator's alternating visual barrels and independent native bonus grenade behavior.
- [ ] Implement safe target filtering, owner/team/pet protection, line of sight, obstruction handling and accurate muzzle placement in every mount orientation.
- [ ] Define player skill XP and progression credit for automated kills explicitly; do not silently impersonate an active player.
- [ ] Respect claim protection, explosion/block-damage policies and gateway encounter rules.
- [ ] Test ammo exhaustion, reload options, resource interruption, gun swaps, removal, chunk unload/reload, server restart and multiplayer synchronization.
- [ ] Verify first/third-person versus mounted animations separately, including recoil, spinning barrels, flash/particle budgets and missing assets.
- [ ] Keep unsupported host/resource combinations visibly marked until implemented, rather than claiming universal support from a gun ID alone.

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
