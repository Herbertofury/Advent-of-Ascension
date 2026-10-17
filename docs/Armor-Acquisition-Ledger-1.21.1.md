# Armor acquisition ledger · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** Before planning a set, check whether its acquisition route is actually represented in this release. This ledger covers all **204 registered armor items**, grouped into **48 four-piece sets and 12 individual pieces**.

[Armor Atelier](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1) · [Effects and activation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Set-Effects-and-Activation-1.21.1) · [Materials and durability](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Materials-and-Set-Preparation-1.21.1)

## What the census establishes

- **32 pieces:** exact recipe outputs, forming eight Infusion sets.
- **20 pieces:** explicit item entries in six loot tables. A table entry alone does not prove the complete spawning/progression route.
- **6 pieces:** previously traced Skill Master trade offers.
- **1 piece:** Old Boot entries in two custom Hauling pools.
- **4 pieces:** retained Hydrangic station outputs; obtaining the modern inputs and station remains unresolved.
- **141 pieces:** no route in these selected source categories. This is an open research result, not a claim that every such item is unobtainable.

These categories cover **63 distinct items**. Separately, **92 armor items** occur in the recipe-viewer hiding tag. Hiding is a presentation flag; it is not deletion, a universal disable flag or proof of survival availability.

## Start with a documented route

1. [Build a Frame Bench and infuse eight armor sets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1). The guide includes all four frame choices, exact ingredients and full-set shopping lists.
2. [Reach the Skill Master and plan tokens](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1). Check the linked guide’s release-specific entry and reward boundaries before planning a helmet purchase.
3. For **Biogenic**, both Guardian modifier definitions are listed in the shipped NeoForge global modifier registry. They select the corresponding extra loot tables under Guardian/Elder Guardian entity predicates. Each table has one roll: ordinary Guardian has empty weight 100 and each armor piece weight 2; Elder Guardian has empty weight 100 and each piece weight 10. These are the eligible pool’s base weights, not a tested universal kill chance.
4. For **Old Boot**, both custom water Hauling pools require Hauling level 50. The default pool entry has weight 5 and luck modifier 5.0; Barathos water has weight 1 and luck modifier 2.0. These fields are not percentages and this is not an ordinary vanilla fishing recipe.
5. [Read the Petal Crafting release comparison](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Petal-Crafting-and-Hydrangic-Armor) before assuming retained Hydrangic outputs can be reached in an unmodified modern survival world.

## Full-set drops and single-piece rewards are different

![Explosive armor source model](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-explosive-1.21.1.webp)

### Explosive and Predatious: the selected reward can be a complete set

The normal King BamBamBam and Tyrosaur tables each contain a one-roll `special_loot` pool. It chooses between a weapon entry with weight **3** and an `aoa3:multi` entry with default weight **1**. The checked Multi entry loops over its child entries and creates each expanded child's loot. In these two tables, those children are the four unconditional armor pieces.

- [King BamBamBam encounter](https://github.com/Herbertofury/Advent-of-Ascension/wiki/King-BamBamBam-Combat-Field-Guide-1.21.1): Explosive Bow or the **four Explosive pieces together**.
- [Tyrosaur encounter](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Tyrosaur-Combat-Field-Guide-1.21.1): Primal Sword or the **four Predatious pieces together**.

For this isolated, unmodified outer pool, the armor bundle has a **1-in-4 selection share**. It is not four separate 1-in-4 piece rolls. Death eligibility, custom loot-table overrides, loader hooks and datapacks remain separate. Other pools in the same boss table can also award supplies.

### Utopian: acquire a Treasure Box, then roll one reward

![Treasure Box reward possibilities](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/treasure-box-rewards-1.21.1.webp)

1. Use the [Hauling equipment and pool-selection guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hauling-Rods-and-Fishing-Pools-1.21.1). The shipped default-water and Precasia-water Treasure Box entries require **Hauling level 30**.
2. The default-water entry has weight **250** and luck modifier **15.0**; Precasia water has weight **35** and luck modifier **5.0**. These are pool parameters, not catch percentages.
3. Make inventory space and use the box on the server. The checked use method invokes `aoa3:items/treasure_box`, gives the results through the inventory helper and consumes one box outside Creative.
4. Its one-roll pool contains twelve entries with total base weight **256**. Each Utopian piece has weight **5**: **5/256 for a particular piece**, or **20/256 for any Utopian piece**, conditional on this eligible unmodified pool.
5. Duplicates are possible. A Treasure Box does not award a full Utopian set; [inspect every possible reward](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.21.1#treasure-box) before planning a collection.

### Nethengeic: look for the pit's encounter area

![Nethengeic armor source model](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nethengeic-1.21.1.webp)

The shipped **Nethengeic Pit** structure gives the Nethengeic Beast a concrete structure-spawn route. The entity's name and loot-table filename alone were not the evidence for this connection.

- The structure is eligible for `#minecraft:is_nether`, starts from absolute height **31**, and uses a lava block-match surface test. Placement can still fail against terrain; this is not a fixed-coordinate locator.
- Its registered random-spread structure set uses spacing **30**, separation **8**, salt **845278832**. These settings do not promise a pit every thirty chunks.
- The start pool has two equally weighted template alternatives, both present in the released JAR.
- Its monster override applies to **structure-piece bounding boxes** and lists `aoa3:nethengeic_beast` with min/max group size **1/1** and weight **1**. A spawn-list entry does not guarantee a beast is already standing in every pit.
- The checked spawn-rule builder requests non-Peaceful spawning, excludes Nether Wart Block below the spawn, checks the valid spawn block, and adds a nearby-same-entity exclusion with extents **15, 2, 15**. Mob caps, engine rules, other mods and eligible terrain still matter.
- The Beast's separate armor pool has one roll: empty weight **50**, then each of four Nethengeic pieces weight **2**. The isolated base pool therefore has **2/58 per piece**, not a full-set bundle.

Do not confuse the **Nethengeic Beast** with the **Nethengeic Wither** boss. Their encounter routes and tables are separate.

### Why these are stronger connections, but still bounded

The checked AoA inheritance chains for King BamBamBam, Tyrosaur and Nethengeic Beast declare no local `getLootTable` or `getDefaultLootTable` override. The official vanilla reference follows the entity type's registry ID and prefixes its path with `entities/`; a mob's custom loot-table field can replace that default. AoA's `shouldDropLoot` also requires its `hasDrops` flag alongside the inherited gate.

The separate Guardian extra-table handler iterates configured table keys, resolves each table and invokes `getRandomItemsRaw` into the generated-loot list. This supports the registered Biogenic modifier route described above, while avoiding a claim that the extra table recursively reapplies every global modifier.

[Read the selected method instructions, source hashes, pool comparison and structure resources](https://herbertofury.github.io/Advent-of-Ascension/armor-loot-route-evidence-1.21.1.json). These are static source connections, not live kill, catch or world-generation tests.

## Every ordinary set

Each picture is the existing neutral worn-model study. It is not a screenshot or an availability certificate.

### Alacrity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-alacrity-1.21.1.webp" width="180" height="180" alt="Alacrity neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=alacrity)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Archaic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-archaic-1.21.1.webp" width="180" height="180" alt="Archaic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=archaic)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Baron

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-baron-1.21.1.webp" width="180" height="180" alt="Baron neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=baron)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Battleborn

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-battleborn-1.21.1.webp" width="180" height="180" alt="Battleborn neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=battleborn)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Biogenic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-biogenic-1.21.1.webp" width="180" height="180" alt="Biogenic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=biogenic)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- Loot-table entry: `data/aoa3/loot_table/entities/vanilla_elder_guardian.json`, `data/aoa3/loot_table/entities/vanilla_guardian.json`

### Boreic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-boreic-1.21.1.webp" width="180" height="180" alt="Boreic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=boreic)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Candy

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-candy-1.21.1.webp" width="180" height="180" alt="Candy neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=candy)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Commander

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-commander-1.21.1.webp" width="180" height="180" alt="Commander neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=commander)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Crystallis

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-crystallis-1.21.1.webp" width="180" height="180" alt="Crystallis neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=crystallis)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Elecanyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-elecanyte-1.21.1.webp" width="180" height="180" alt="Elecanyte neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=elecanyte)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Embrodium

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-embrodium-1.21.1.webp" width="180" height="180" alt="Embrodium neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=embrodium)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Exoplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-exoplate-1.21.1.webp" width="180" height="180" alt="Exoplate neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=exoplate)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Explosive

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-explosive-1.21.1.webp" width="180" height="180" alt="Explosive neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=explosive)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- Loot-table entry: `data/aoa3/loot_table/entities/king_bambambam.json`

### Fungal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-fungal-1.21.1.webp" width="180" height="180" alt="Fungal neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=fungal)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Ghastly

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghastly-1.21.1.webp" width="180" height="180" alt="Ghastly neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ghastly)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Ghoulish

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghoulish-1.21.1.webp" width="180" height="180" alt="Ghoulish neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ghoulish)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Hazmat

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hazmat-1.21.1.webp" width="180" height="180" alt="Hazmat neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hazmat)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Hydrangic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydrangic-1.21.1.webp" width="180" height="180" alt="Hydrangic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hydrangic)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Retained Petal Crafting output; modern acquisition gap](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Petal-Crafting-and-Hydrangic-Armor)

### Hydroplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydroplate-1.21.1.webp" width="180" height="180" alt="Hydroplate neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hydroplate)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Ice

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ice-1.21.1.webp" width="180" height="180" alt="Ice neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ice)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Infernal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-infernal-1.21.1.webp" width="180" height="180" alt="Infernal neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=infernal)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Knight

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-knight-1.21.1.webp" width="180" height="180" alt="Knight neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=knight)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Lunar

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lunar-1.21.1.webp" width="180" height="180" alt="Lunar neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lunar)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Lyndamyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyndamyte-1.21.1.webp" width="180" height="180" alt="Lyndamyte neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lyndamyte)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Lyonic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyonic-1.21.1.webp" width="180" height="180" alt="Lyonic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lyonic)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Mercurial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-mercurial-1.21.1.webp" width="180" height="180" alt="Mercurial neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=mercurial)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Necro

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-necro-1.21.1.webp" width="180" height="180" alt="Necro neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=necro)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Nethengeic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nethengeic-1.21.1.webp" width="180" height="180" alt="Nethengeic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=nethengeic)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- Loot-table entry: `data/aoa3/loot_table/entities/nethengeic_beast.json`

### Nightmare

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nightmare-1.21.1.webp" width="180" height="180" alt="Nightmare neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=nightmare)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Omni

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-omni-1.21.1.webp" width="180" height="180" alt="Omni neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=omni)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Phantasm

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-phantasm-1.21.1.webp" width="180" height="180" alt="Phantasm neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=phantasm)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Poison

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-poison-1.21.1.webp" width="180" height="180" alt="Poison neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=poison)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Predatious

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-predatious-1.21.1.webp" width="180" height="180" alt="Predatious neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=predatious)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- Loot-table entry: `data/aoa3/loot_table/entities/tyrosaur.json`

### Primordial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-primordial-1.21.1.webp" width="180" height="180" alt="Primordial neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=primordial)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Purity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-purity-1.21.1.webp" width="180" height="180" alt="Purity neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=purity)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Rockbone

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rockbone-1.21.1.webp" width="180" height="180" alt="Rockbone neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=rockbone)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Rosidian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rosidian-1.21.1.webp" width="180" height="180" alt="Rosidian neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=rosidian)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Runic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-runic-1.21.1.webp" width="180" height="180" alt="Runic neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=runic)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Sharpshot

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-sharpshot-1.21.1.webp" width="180" height="180" alt="Sharpshot neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=sharpshot)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Skeletal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-skeletal-1.21.1.webp" width="180" height="180" alt="Skeletal neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=skeletal)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Spaceking

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-spaceking-1.21.1.webp" width="180" height="180" alt="Spaceking neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=spaceking)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Speed

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-speed-1.21.1.webp" width="180" height="180" alt="Speed neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=speed)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Subterranean

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-subterranean-1.21.1.webp" width="180" height="180" alt="Subterranean neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=subterranean)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Utopian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-utopian-1.21.1.webp" width="180" height="180" alt="Utopian neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=utopian)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- Loot-table entry: `data/aoa3/loot_table/items/treasure_box.json`

### Void

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-void-1.21.1.webp" width="180" height="180" alt="Void neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=void)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Weaken

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-weaken-1.21.1.webp" width="180" height="180" alt="Weaken neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=weaken)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **4/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Wither

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-wither-1.21.1.webp" width="180" height="180" alt="Wither neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=wither)

Selected-route coverage: **4/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- [Infusion recipe walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1)

### Zargonite

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-zargonite-1.21.1.webp" width="180" height="180" alt="Zargonite neutral worn-model study">

[View all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=zargonite)

Selected-route coverage: **0/4 pieces**. Recipe-viewer hiding tag: **0/4 pieces**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

## Individual helmets and Old Boot

[See all special-piece model studies](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Armor-and-Skill-Helmets-1.21.1).

### Achelos Helmet

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:achelos_helmet)

Recipe-viewer hiding tag: **not listed**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Oceanus Helmet

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:oceanus_helmet)

Recipe-viewer hiding tag: **listed**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Sealord Helmet

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:sealord_helmet)

Recipe-viewer hiding tag: **listed**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Face Mask

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:face_mask)

Recipe-viewer hiding tag: **listed**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Chroma Goggles

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:chroma_goggles)

Recipe-viewer hiding tag: **listed**.

- No selected direct acquisition route found. Generic code, indirect tags and external packs remain outside this census.

### Helm of the Dextrous

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_dextrous)

Recipe-viewer hiding tag: **not listed**.

- [Skill Master: 64 Archaic Tokens per helmet](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1)

### Helm of the Dryad

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_dryad)

Recipe-viewer hiding tag: **not listed**.

- [Skill Master: 64 Archaic Tokens per helmet](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1)

### Helm of the Ritualist

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_ritualist)

Recipe-viewer hiding tag: **not listed**.

- [Skill Master: 64 Archaic Tokens per helmet](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1)

### Helm of the Trawler

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_trawler)

Recipe-viewer hiding tag: **not listed**.

- [Skill Master: 64 Archaic Tokens per helmet](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1)

### Helm of the Treasurer

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_treasurer)

Recipe-viewer hiding tag: **not listed**.

- [Skill Master: 64 Archaic Tokens per helmet](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1)

### Helm of the Warrior

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_warrior)

Recipe-viewer hiding tag: **not listed**.

- [Skill Master: 64 Archaic Tokens per helmet](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Master-and-Archaic-Tokens-1.21.1)

### Old Boot

[Exact item record](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:old_boot)

Recipe-viewer hiding tag: **not listed**.

- Custom Hauling pool: `data/aoa3/aoa3/hauling_spawn_pool/barathos_water.json`, `data/aoa3/aoa3/hauling_spawn_pool/water_default.json`

## Evidence and remaining checks

[Machine-readable 204-item ledger and 44 hash-pinned resources](https://herbertofury.github.io/Advent-of-Ascension/armour-acquisition-evidence-1.21.1.json). The extractor parses each selected JSON once and matches exact registered item IDs; it does not search name substrings or infer a recipe from an advancement icon.

Remaining work: validate the documented encounter routes in the exact target build; inspect generic or indirect item suppliers; distinguish legacy-only progression from modern pathways; validate a copied save on the exact target build when runtime testing is separately authorized. Keep retained resources, static routes and live acceptance as separate statuses.

AoA systems and artwork: Tslat and contributors. Neutral mesh reference: Mojang/Microsoft. Original documentation tooling and presentation. No Java/game code was executed.
