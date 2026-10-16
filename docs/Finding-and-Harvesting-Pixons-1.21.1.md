# Finding and harvesting Pixons · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** Pixons supply Energy Stones and Power Stones for Imbuing progression. Make an Attuning Bowl, find a suitable Pixon, stand close and **hold the use action**. Carrying the bowl alone does not harvest anything.

![Eight Pixon variants paired with their Energy Stone and Power Stone item appearances; coloured dots represent source palettes, not creature models](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/pixon-stone-reference-1.21.1.webp)

[Imbuing Chamber](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Imbuing-Chamber-Enchanting-1.21.1) · [Skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1) · [Loot reference](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Loot-Tables-and-Global-Modifiers-1.21.1)

## 1. Make an Attuning Bowl

![Attuning Bowl recipe with seven amethyst-tag ingredients and one gold-tag ingredient, leaving the top-middle slot empty](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/attuning-bowl-recipe-1.21.1.webp)

| Amethyst | Empty | Amethyst |
|---|---|---|
| Amethyst | Gold ingot | Amethyst |
| Amethyst | Amethyst | Amethyst |

Use **7 items matching `c:gems/amethyst` and 1 matching `c:ingots/gold`**. The shaped recipe outputs one bowl. Pack changes to these tags can change accepted ingredients.

## 2. Search the right world

The stock custom-spawner files select these pools. A dimension appearing in this table is **configuration evidence, not proof that its complete historical gameplay is accessible in this release**. Check the [version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) before planning a trip.

| Pool | Dimension selectors in the shipped definition |
|---|---|
| T0 | Overworld |
| T1 | Nether, Barathos, Lelyetia, Creeponia |
| T1, shorter intervals | Precasia |
| T2 | Abyss, Mysterium, Candyland, Iromine, Haven, Celeve, Crystevia, Gardencia |
| T3 | Dustopia, L’Borean, Runandor, Greckon |
| T4 | Shyrelands |

The stock lists do **not** include the End or Nowhere. Flat worlds are excluded, as are biomes in `c:is_dead`. The registration path also rejects dimension namespaces other than `minecraft` and `aoa3`; support for third-party dimensions needs compatibility work beyond editing a selector.

### What the variant weights mean

| Variant | T0 | T1 / Precasia | T2 | T3 | T4 |
|---|---:|---:|---:|---:|---:|
| Ambient | 30 | 10 | 0 | 0 | 0 |
| Glistening | 25 | 40 | 30 | 10 | 0 |
| Blooming | 20 | 35 | 40 | 20 | 10 |
| Shining | 15 | 30 | 35 | 35 | 40 |
| Gleaming | 10 | 25 | 30 | 30 | 35 |
| Glowing | 5 | 20 | 25 | 25 | 30 |
| Glaring | 1 | 15 | 20 | 20 | 25 |
| Radiant | 0 | 10 | 15 | 15 | 20 |

These are **relative weights within a selected pool**, not percentages and not encounter rates. Radiant is absent from the Overworld pool. A pool containing Radiant still does not guarantee one will appear.

### Waiting and searching without false promises

- The server requires its passive-spawn flag and `doMobSpawning` to permit the spawner check.
- Ordinary configured intervals are **12,000–36,000 ticks**, or **10–30 minutes at 20 TPS**. Precasia uses **9,000–27,000 ticks**, or **7.5–22.5 minutes**.
- These are attempt intervals, not guaranteed spawn times. The first eligible check can occur earlier; there is no mandatory initial ten-minute wait implied by the interval alone.
- The code adds an extra delay per counted spawn: ordinarily **3,000–6,000 ticks**; Precasia **2,000–4,000 ticks**. Lag and loaded-world ticking affect wall-clock time.
- `chance_per_player: 1.0` does not guarantee a visible Pixon. Candidate placement, biome and survival checks still apply. The attempt count uses a biased 1–3 sample plus integer player luck.
- Look around suitable supported, unobstructed terrain rather than expecting a fixed landmark. Placement rejects fluid, blocked/suffocating space, signal sources and blocks preventing mob spawning inside.

**Do not build a farm around a claimed exact 40–128-block ring.** Those arguments appear at the Pixon call site, but the shared released position helper uses axis offsets that can exceed the named maximum. The [spawn-geometry audit](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Roaming-Trader-Spawn-Geometry) explains that helper's problem. This is a static code finding, not a measured Pixon spawn map.

## 3. Harvest, rather than attack

1. Approach the Pixon's particle effect. This entity is not a conventional modeled animal: the inspected implementation is not pickable and cannot change dimensions.
2. Keep its supporting block intact and leave room around it. Avoid enclosing or suffocating it.
3. Equip the Attuning Bowl and **actively hold use** while standing close.
4. Watch your inventory for stones. Move closer if nothing arrives; a missed random roll is also normal.
5. Stop when you have the materials you need. Pixons have a finite life, so a single one is not a permanent infinite farm.

The source range is `2 + magnitude × 0.05` blocks. Normal initial magnitudes put it just above two blocks to roughly 3.25 blocks; getting close is more reliable advice than standing at the boundary. The per-eligible-tick harvest chance is `min(25, magnitude) / 250`. This does **not** mean one item every tick.

A successful harvest increases the Pixon's age by 500 ticks and, while above the floor, reduces magnitude by 0.5, clamped to at least 1. Ordinary ticking also ages it. Smaller magnitude reduces both harvest chance and the lifespan threshold. Age, variant and magnitude are saved, so reloading is not a reset-to-infinite-harvest method. Do not infer an exact real-time lifespan from this guide.

## 4. Keep the right stone

Each variant's base loot table makes one roll: **Energy Stone weight 6; Power Stone weight 1**. That is a conditional **6/7 versus 1/7 per base-table roll**, not a probability per game tick and not a guaranteed pair. Loot modifiers can change final results.

| Pixon | Energy Stone: declared Imbuing XP | Power Stone: declared Imbuing XP |
|---|---:|---:|
| Ambient | 10 | 20 |
| Glistening | 20 | 40 |
| Blooming | 30 | 60 |
| Shining | 40 | 80 |
| Gleaming | 45 | 90 |
| Glowing | 55 | 110 |
| Glaring | 65 | 130 |
| Radiant | 75 | 150 |

These are the table functions' requested skill awards, not a guarantee after all player or pack modifiers. They are AoA Imbuing skill values, not the green vanilla XP level.

- **Energy Stones:** reserve one for the Imbuing Chamber construction recipe if needed. The inspected training use action spends the **entire held stack outside Creative**. Split a training stack before using it.
- **Power Stones:** keep the exact tier required by your enchantment recipe. Higher tiers are not automatic substitutes.
- This guide does not invent an Energy-to-Power crafting conversion. Harvesting tables are the verified route described here.

## Troubleshooting

| Symptom | Check |
|---|---|
| No stones while holding a bowl | Hold the use action, stay close and allow for random failed rolls. |
| No Pixon during a short search | Check world/biome restrictions and spawning settings; intervals are attempts, not guarantees. |
| Cannot find Radiant in the Overworld | T0 has no Radiant entry. Choose a supported accessible world with a pool that includes it. |
| Particle vanished while harvesting | Finite age and harvest-driven aging are expected; protect the supporting space too. |
| Stone does not fit the chamber | Energy and Power Stones serve different roles; match the recipe's exact Power Stone. |
| Modded dimension never gets Pixons | The source namespace gate needs an integration change; a dimension list edit alone is insufficient. |

## Evidence and scope

[Machine-readable harvesting evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pixon-harvesting-evidence-1.21.1.json) records the six released spawner definitions, eight loot tables, bowl recipe, selected class checks and pinned source interpretation. [Illustration provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/pixon-art-evidence-1.21.1.json) identifies the item previews and source palettes.

Primary implementation: [PixonEntity](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/misc/PixonEntity.java). Data and source are scoped to the recorded release and pin; this page does not certify live encounters, private Enderloom behavior or complete historical dimension restoration. Images show actual item references and labelled palette dots, not a fabricated 3D Pixon creature.
