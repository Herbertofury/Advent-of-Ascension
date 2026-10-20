# Crystaneer: precision, hanging jewels and conditional rewards

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## What makes this weapon distinctive

Crystaneer is a **BaseSniper** subclass using Metal Slug ammunition. Its unique inspected impact hook can request a bonus gemstone loot table after a qualifying lethal impact. Preserve that identity when upgrading the model and effects: it is not simply a purple laser rifle.

| Released field | Stored value |
|---|---:|
| Damage input | 37.5 |
| Durability | 345 |
| Shot delay | 88 ticks |
| Recoil input | Approximately 0.042 |
| Ammunition | Metal Slug |
| Automatic fire | No |
| Scope overlay | SCOPE_4 |
| Firing sound | ITEM_GUN_SNIPER_HEAVY_FIRE_LONG |

These values are constructor inputs or inspected class selections, not measured final damage, camera degrees or audio duration. At 20 TPS, 88 ticks is a nominal 4.4 seconds. Preserve the inherited sniper movement/aim handling and native resource path; a cosmetic conversion must not replace them with generic gun behavior.

## Original silhouette and sight

![Actual released Crystaneer sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/crystaneer-original-preview.png)

Keep the charcoal/gray upper body, purple longitudinal sections, raised dark scope with green accent and especially the hanging cyan, larger green and smaller red jewel shapes. Rainbow Druse, amethyst and emerald are actual infusion ingredients. Ornate crystal mounts and a specific crafting civilization are not established lore.

![Actual SCOPE_4 overlay on a neutral background](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/crystaneer-original-scope4.webp)

This is the released alpha overlay composited onto a pale neutral background so its black reticle is visible. It is not an in-game screenshot and does not demonstrate zoom, field of view or alignment with an upgraded model.

## Conditional bonus loot, illustrated

![Source-derived Crystaneer reward pool with item images and relative weights](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/crystaneer-reward-board.webp)

The inspected path has several gates:

1. The shared gun impact path must report successful damage before calling the impact effect.
2. Crystaneer's effect checks the server side, a living target and target health at or below zero.
3. It requests `aoa3:items/crystaneer` using the target position and shooter context.
4. The bundled gift table has a **20% random-chance pool gate**, one roll and the relative weights below.

| Entry | Relative weight |
|---|---:|
| Diamond | 100 |
| Emerald | 85 |
| Amethyst Shard | 120 |
| Jade | 110 |
| Blue Gemstones | 25 |
| Green Gemstones | 25 |
| Purple Gemstones | 25 |
| Red Gemstones | 25 |
| White Gemstones | 25 |
| Yellow Gemstones | 25 |

The total is 565. A weight of 100 is not a 100% chance. No reward is guaranteed, and the 20% gate is not a reward chance on every hit. Datapacks, combat hooks and modpack changes can alter the actual outcome. Runtime tests must check duplicate impacts, kill attribution and item conservation before promising one reward decision per death.

The image reuses existing source-derived 1.20.1 item illustrations. [Image provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/crystaneer-reward-board-evidence.json)

## Craft at the Infusion Table

Place a **Sniper Frame** in the separate left base slot, then use seven distinct middle slots:

- Rainbow Druse ×3, in three separate slots
- One ingredient matching `forge:gems/amethyst`
- One matching `forge:gems/emerald`
- Two ingredients matching `forge:ingots/iron`, in separate slots

Leave the other two middle slots empty. Middle-grid order is irrelevant; stacking repeated ingredients into one slot does not satisfy separate entries. Tag membership can change in a modpack. The exact definition is `data/aoa3/recipes/infusion_crystaneer.json`, with the inspected ordinary defaults for omitted level and XP fields.

[Illustrated infusion workflow](Infusion-Table-Crafting-1.20.1) · [Exact recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=infusion_crystaneer)

## Premium concept

![Crystaneer hero, silhouette, jewel material details, reward inspiration and inspect vignette](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/crystaneer-concept-v1.png)

The sheet retains the distinctive cyan/green/red jewel cluster and purple body while adding richer surfaces and mounts. The reward vignette is cosmetic inspiration; it does not promise a particular gem or a reward on every kill. Jewel glow, reward sparkle and the inspect pose are proposals. This is not a finished texture atlas, native model, rendered animation or new projectile behavior.

The hanging gems and support-hand placement need particular clearance work. Keep the long green jewel readable without making it pass through the hand, magazine path or environment during inspection, sprinting and aim transitions. The static hand pose is not a clearance certificate.

## Complete upgrade plan

- **Sight and aiming:** preserve original scope behavior as one option; offer readable alternate sights only after matching camera, hand pose and reticle alignment. Keep reduced-bloom settings.
- **Inspection:** a short tilt catches colored light on securely mounted gems. Interrupted inspection returns smoothly to gameplay; no resource use or extra loot roll.
- **Attachments:** handling-focused fore-ends, compact versus steadier barrel treatments and sight variants. Optional prism/beam or chain-effect conversions require separately defined mechanics and costs; they are not the original weapon.
- **Reward feedback:** only play a reward cue after the authoritative reward actually exists. Client effects must never create items or independently reroll the table.
- **Firing/effects:** capture the original shot, sound, flight and impacts. Then develop distinct muzzle, tracer, impact/decal and optional finisher treatments while preserving hit behavior and loot attribution.
- **Resources:** retain Metal Slug support and make reload optional. A new reload or charge mode requires explicit gameplay definitions and cancellation rules.
- **Customization:** original-fit/premium textures, skins, charms with explicit earned bonuses, stickers and animated/glowing emblems. Charms must not tangle visually with the signature fixed jewel cluster.
- **Animation:** equip, idle, aim, fire, recovery, optional reload, inspect and interruptions in first/third person, with actual hand rigs.
- **Performance:** bounded jewel effects, optional lights, cached materials/configuration and LODs. Measure frame-time lows; beautiful translucent concepts do not establish a cheap runtime material.

## Acceptance gates

- [ ] Native original projectile, scope, impact, sound and resource captures
- [ ] Reward attribution, duplicate-impact and loot-conservation tests
- [ ] Full attachment, muzzle, tracer, impact, decal and finisher concepts
- [ ] Rigged-hand/jewel clearances, two texture modes and complete animations
- [ ] Native export, multiplayer, persistence, dismantling and performance qualification

[Released-class, loot and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/crystaneer-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
