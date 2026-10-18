# Automation, dimension challenges and shared ammunition

**Owner-requested compatibility targets with proposed gameplay ideas.** These designs are not shipped integrations. Pin exact Minecraft, loader and dependency releases before implementation. [All compatibility targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Compatibility-Targets) · [Extra Realmstones](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extra-Realmstones-and-Dimension-Compatibility) · [Weapon overhaul](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul)

## Create: build an expedition industry

[Official Create project](https://www.curseforge.com/minecraft/mc-mods/create)

**Proposed fun loop:** return from an AoA realm with new materials, expand a visible mechanical production line, and send prepared supplies back out on the next expedition.

- **Realm-forged ammunition lines:** sequenced assembly and appropriate pressing/mixing steps for explicitly approved cartridges and components. Preserve native material costs and progression rather than making every rare resource infinitely renewable.
- **Expedition depots:** sort realm loot into labeled storage, prepare food/healing/ammo crates and route them to a portal-side base or train station.
- **Mechanical workshop upgrades:** realm-themed casing, decorative mechanisms and manufacturing recipes for premium weapon cosmetics; presentation upgrades must not silently change damage.
- **Harvesting integration:** qualify appropriate AoA crops and material-processing recipes with clear yields. Automated harvesting must not multiply skill rewards through repeated callbacks.

Acceptance: pinned Create API/recipe types, full-inventory and interruption behavior, contraption load/unload, exact item-data preservation, no infinite conversion cycles and no unsafe portal/contraption transport assumptions.

## Botania: a living realm armory

[Official Botania site](https://botaniamod.net/) · [Official Lexicon](https://botaniamod.net/lexicon.html)

**Proposed fun loop:** cultivate realm-themed gardens, build mana infrastructure and use earned realm materials in distinctive magical crafting routes.

- **Realm-themed functional flowers:** optional original flowers with useful, bounded effects around exploration preparation or ingredient handling. Each needs a defined resource cost and progression gate.
- **Runic upgrade ceremonies:** carefully designed altar recipes for appropriate AoA magical components or cosmetic weapon accents, with visible mana flow and completion feedback.
- **Botanical armory presentation:** optional petal trails, rune-ring flashes and thematic inspection effects on eligible magical weapons.
- **Supply gardens:** automate appropriate ingredients without generating free AoA progression or bypassing dimension access.

Keep **Botania Mana, AoA Spirit, other AoA resources and ammunition separate**. A conversion or alternate payment mode needs an explicit, server-controlled exchange contract. Never treat similarly named runes or mana items as interchangeable automatically.

Acceptance: catalyst returns, interrupted crafting, automation, duplicate event prevention, clear mana accounting and no cross-resource free-casting loop.

## Applied Energistics 2: one-click expedition preparation

[Official AE2 guides, including1.20.1](https://appliedenergistics.org/guides)

**Proposed fun loop:** choose an expedition loadout, see which supplies are missing, autocraft what is legitimately craftable, then collect a complete kit before entering a realm.

- **Realm expedition kits:** ammo, healing, food and permitted utility items grouped by destination and weapon loadout.
- **Ammo restock station:** keep selected compatible ammunition stocked at a physical base-side supply point using real network inventory and normal crafting costs.
- **Rare-loot organization:** preserve unique AoA stack data while displaying useful realm/family categories and identifying ingredients still needed for upgrades.
- **Workshop automation:** expose valid processing patterns for supported AoA/Create/Botania recipes without pretending every ritual is an ordinary instant craft.

A network item listing is not a new permission to consume that item remotely. Automatic field resupply, cross-dimensional access and wireless reach remain separate opt-in features with normal AE2 access/power rules.

Acceptance: transaction simulation versus commit, crafting cancellation, disconnected networks, full inventories, ownership/security, stack-component/NBT preservation and no duplicated withdrawals on retries.

## Gateways to Eternity: a challenge pearl for every accepted dimension

[Official Gateways to Eternity](https://www.curseforge.com/minecraft/mc-mods/gateways-to-eternity) · [Owner-selected More Gateways reference](https://www.curseforge.com/minecraft/mc-mods/gateways-to-eternity-more-gateways)

Gateways to Eternity supplies wave-based enemy encounters and rewards. More Gateways already advertises integrations for several other mob mods, including Alex's Mobs and Cataclysm. Study and extend the existing data-driven approach before duplicating it. **These challenge gateways are a different system from Extra Realmstones' travel portals.**

**Proposed progression:** first legitimately discover a realm, unlock its themed Gate Pearl, clear escalating local enemy waves, then earn a distinct trophy/cosmetic and a balanced supply reward. Later challenge tiers can combine already-unlocked realms.

- **One designed encounter per accepted AoA dimension**, with its characteristic creatures, mechanics, atmosphere, escalation and completion reward.
- **Supported external dimensions** receive their own encounters after their exact mob roster and dependency version are qualified.
- **A realm identity beyond a reskin:** aerial pressure, ground formations, ranged threats or hazard-aware enemy composition, based on the actual supported mobs.
- **Boss/elite finale only when appropriate:** retain native boss prerequisites, phases, defeat credit and progression. Do not spawn incompatible scripted bosses in arbitrary locations and call that support.
- **Co-op tiers:** deliberate participant scaling, readable wave previews and fair personal/team rewards.
- **Mastery rewards:** optional premium weapon skins, trophies, banners and themed presentation unlocks; avoid mandatory repeated farming to use a basic compatibility feature.

### Gateway acceptance checklist

- [ ] Pin the exact Gateways data schema/API and check existing More Gateways content to prevent duplicate IDs or encounters.
- [ ] Confirm every referenced entity, modifier, reward and loot table exists for the selected mod combination.
- [ ] Gate pearls by legitimate realm progression by default; optional shortcut rules must be explicit.
- [ ] Preserve spawn/leash/failure rules and claim protection; validate clear space and supported dimensions.
- [ ] Prevent block destruction or persistent arena debris unless a clearly separate approved mode allows it.
- [ ] Handle player death, disconnect, chunk unload, server restart and an unavailable optional dependency.
- [ ] Prevent duplicate XP, trophies, boss credit or rewards from retries, multipart entities, summoned mobs and discarded enemies.
- [ ] Bound live entities and particles; measure the actual encounter's server tick time and client frame-time lows.

No fixed number of gateways is claimed complete. Keep a per-dimension ledger with encounter content, dependencies, unlocks, reward economics and actual test evidence.

## Scorched Guns and Terramity: shared supplies, distinct weapons

[Scorched Guns / Scorched Guns2 project](https://www.curseforge.com/minecraft/mc-mods/scorched-guns) · [Terramity project](https://www.curseforge.com/minecraft/mc-mods/terramity)

The owner's requested scope for these two is **compatible ammunition where it makes sense and participation in AoA gameplay**. A full TaCZ conversion of their arsenals is not implied.

**Proposed fun loop:** carry a mixed arsenal through AoA realms without needless duplicate stacks of genuinely equivalent basic ammunition, while each mod retains its weapon identity and progression.

- Map compatible ammunition by **exact item ID and actual ammo contract**, never by display name alone.
- Use explicit shared groups or deliberate conversion recipes only where projectile/resource types and economy are compatible.
- Keep physical bullets, shells, rockets, special capsules, mana and energy distinct unless a specifically designed conversion is approved.
- Preserve each weapon's damage, recoil, effects, reload behavior, enchantments and native server consumption. One successful shot must not debit two adapters.
- Make eligible player attacks/kills participate in AoA progression and rewards through a single authoritative attribution path.
- Decide turret, summoned-entity, automated and indirect-kill credit explicitly; do not grant unlimited AoA player skill XP to arbitrary unattended automation.
- Test ammo boxes/pouches, Creative mode, no-ammo attempts, partial stacks, special ammo, full inventories, multiplayer, death and reload cancellation.

### Ammunition mapping record

For every proposed group or conversion, record source and destination IDs, exact releases, native consumption units, conversion quantities, retained special data, supported weapons, costs and progression gates. Verify conservation and detect profitable conversion cycles. A shared tag alone does not prove both weapon implementations actually consume it correctly.

## Suggested first integrated slice

1. One validated common-ammo mapping for an appropriate AoA/Scorched Guns/Terramity pair.
2. A Create manufacturing route and AE2 base-side restock pattern for that supply.
3. One dimension-themed Gate Pearl using an already-qualified AoA creature roster.
4. A completion cosmetic for one premium AoA weapon, with a clearly optional Botania-themed visual variant.
5. End-to-end checks of costs, rewards, saves, multiplayer and performance before scaling across the roster.

These ideas connect exploration, crafting and combat without replacing the systems that make the source mods distinctive.
