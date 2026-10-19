# Ginger Blaster: confection-themed heavy scatter

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept coverage · no accepted native upgrade.**

## Original behavior

Ginger Blaster is a **five-pellet Spreadshot shotgun**. Its inspected subclass adds only a heavy-long firing sound selector beyond its constructor; the firing loop comes from `BaseShotgun`. That loop uses ordinary `LimoniteBulletEntity` pellets. The name and candy ingredients do not establish edible projectiles, healing, burning or explosive impacts.

| Released field | Value / boundary |
|---|---|
| ID | `aoa3:ginger_blaster` |
| Stored damage input | 7.0; not guaranteed final damage |
| Pellet count | 5 |
| Durability | 720 |
| Delay | 60 ticks, nominally 3 seconds at 20 TPS |
| Recoil input | Approximately 0.75; not camera degrees |
| Knockback input | Approximately 0.4; not a measured distance |
| Ammunition | Spreadshot |
| Fire mode | Non-automatic |
| Unique subclass behavior | Heavy-long shotgun firing sound selector |

Do not infer a guaranteed 35 damage total from five pellets: hit handling, immunity, enchantments and shared damage rules still apply. Any candy-projectile or status-effect conversion is new gameplay requiring its own declared rules.

## Original identity

![Actual released Ginger Blaster sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ginger-blaster-original-preview.png)

Keep the caramel-brown front and grip, dark gray structural middle, and angular ivory trim above and below. Gingerbread and Sour Gummy are verified recipe associations. Glazed ceramic armor, decorative icing, a little cookie performer and a living confection story are new interpretations, not established maker lore.

## Infusion tutorial with source textures

[Follow the illustrated 1.20.1 workstation and slot walkthrough](Infusion-Table-Crafting-1.20.1). Put the two Sour Gummies in separate ingredient slots; one stack of two does not replace them.

Use a **Shotgun Frame** as the infusion input, with:

- Sour Gummy ×2
- Spreadshot ×1
- Sugar ×1
- One ingredient matching `forge:ingots/iron`
- One ingredient matching `forge:gingerbread`

| Sour Gummy | Spreadshot | Gingerbread Cookie | Gingerbread Wing |
|---|---|---|---|
| ![Sour Gummy](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-sour-gummy-sprite.png) | ![Spreadshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-spreadshot-sprite.png) | ![Gingerbread Cookie](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-gingerbread-cookie-sprite.png) | ![Gingerbread Wing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/recipe-gingerbread-wing-sprite.png) |

The released gingerbread tag contains **Gingerbread Cookie and Gingerbread Wing as alternatives**. The recipe needs one matching ingredient, not both. A pack may add further tag members. Sugar and iron are named requirements but are not pictured here; the images above are actual AoA textures enlarged with nearest-neighbor sampling.

The source recipe is `data/aoa3/recipes/infusion_ginger_blaster.json`. This is an AoA infusion recipe, not an ordinary crafting-grid arrangement. Verify the exact version's infusion interface and progression requirements before treating this as a complete in-game walkthrough.

## Hero, material and inspect concepts

![Ginger Blaster proposed hero, material treatments and inspection](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ginger-blaster-concept-v1.png)

This sheet explores the original palette, richer confection-like materials, a cosmetic side-hatch performer and a detachable cookie-medallion idea. It is deliberately a **partial concept sheet**: projectile, impact, finisher and full attachment boards remain to be made. The Minecraft-fit panel is a visual direction, not a working texture pack or verified matching 3D model.

The side hatch needs a purposeful, non-conflicting placement on the actual model. It must clear the hand and controls, close safely when interrupted and never produce an item, free shot or gameplay advantage merely because the inspection played. Actual grip/control placement remains unaccepted.

## Full feature plan

- **Firing:** retain the five-pellet original mode; bounded muzzle flash, readable recoil and weighty recovery. Keep cosmetic cookie crumbs separate from actual collision/damage.
- **Projectiles and impacts:** capture original in-flight and impact footage first. Optional candy-colored trails, dust/spark variants and finishers must preserve authoritative hit events and original loot/kill credit.
- **Animation:** equip, aim, fire, optional reload, inspect and interruption in first and third person. The cookie performer is an optional inspection flourish, with a reduced-motion alternative.
- **Attachments:** short confection-styled optic, protective ivory muzzle trim, alternate grip and trim plates, cookie charm and independently balanced precision/scatter conversions. Every functional change needs visible correspondence and explicit cost/handling rules.
- **Variants and crafting:** preserve original infusion as the baseline; new decorative recipes and functional variants remain separate. No invented upgrade-kit route is presented as released content.
- **Customization:** gameplay-earned charm bonuses, skins, stickers, animated/emissive decals, custom emblems, separate projectile/tracer/impact/finisher channels and clear compatibility feedback.
- **Reload:** optional for original mode; only add magazine mechanics when the selected conversion explicitly supports them.
- **Performance:** bounded particles, cached attachment state, no idle gameplay polling, suitable LODs and measured dense-scene frame times. Bright icing or a charm must not imply a permanent dynamic light.

## Open acceptance evidence

- [ ] Complete original flight/impact captures and native five-pellet behavior tests.
- [ ] Complete projectile, impact, finisher and attachment concept coverage.
- [ ] Approve silhouette, controls, actual player-hand fit and both visual treatments.
- [ ] Test complete hatch, charm and attachment animation sweeps and cancellation.
- [ ] Validate native export, multiplayer, saves, resources and measured performance.

[Complete feature standard](Weapon-Completeness-Standard) · [Source evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ginger-blaster-source-evidence.json) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
