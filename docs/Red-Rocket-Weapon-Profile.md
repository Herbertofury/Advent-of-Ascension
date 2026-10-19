# Red Rocket: crimson shotgun, not a rocket launcher

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## What the released weapon actually does

The checked registration constructs **BaseShotgun directly**, with two ordinary Limonite bullet entities and Spreadshot ammunition. Its name does not establish rocket projectiles, explosive damage, homing or a launcher mechanism. It is non-automatic in the inspected base class.

| Stored constructor field | Red Rocket | Purple Punisher upgrade |
|---|---:|---:|
| Damage input | 11.5 | 20.5 |
| Pellets | 2 | 2 |
| Durability | 500 | 1,120 |
| Delay | 52 ticks | 52 ticks |
| Recoil input | Approximately 0.4 | Approximately 0.2 |
| Knockback input | Approximately 0.785 | Approximately 0.785 |

These are source values, not measured final damage, camera degrees or physical distances. At 20 TPS, the nominal delay is 2.6 seconds. Two pellets do not guarantee two hits or 23 total damage. The checked upgrade increases stored damage/durability and reduces the recoil input while retaining pellet count, delay and knockback input.

## Original identity

![Released Red Rocket sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/red-rocket-original-preview.png)

Preserve the long dark upper body, muted gray longitudinal strip, crimson lower fore-end, angled dark-red rear/grip and small red front sight. The actual recipe supplies a Baronyte/Blazium material association. Crimson enamel, ornamental finishing and a particular maker's history are artistic proposals, not established lore.

## Crafting: five separate middle slots

At the **Infusion Table**, place a Shotgun Frame in the separate left base slot, then fill five middle ingredient slots:

- Two separate ingredients matching `forge:ingots/baronyte`, one in each slot
- One matching `forge:ingots/blazium`
- One matching `forge:ingots/iron`
- One matching `forge:gunpowder`

Leave the other four middle slots empty. One stack of two Baronyte ingots in a single slot does not represent the recipe's two ingredient entries. Order within the middle grid is irrelevant; modpack tag contents may vary. The bundled definition is `data/aoa3/recipes/infusion_red_rocket.json`. Omitted level/XP fields use the inspected ordinary defaults, level 1 and XP 0–0.

[Illustrated Infusion Table guide](Infusion-Table-Crafting-1.20.1) · [Exact recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=infusion_red_rocket)

## Haunted upgrade into Purple Punisher

Use the **Divine Station**: Red Rocket in the left input, Haunted Upgrade Kit in the middle, Purple Punisher in the output. The exact definition is `data/aoa3/recipes/upgrade_kit_purple_punisher.json`.

This proves an upgrade route, not a particular drop location or invented ghost-damage mechanic. The base recipe returns its declared result; arbitrary input names, enchantments and third-party custom data are not automatically promised to survive. Preserve valuable originals and test customization transfer on disposable copies.

[Divine Station workflow and transfer limits](Divine-Station-Weapon-Upgrades-1.20.1)

## Premium concept and visible QA limits

![Red Rocket hero, side view, surface detail and proposed muzzle, two-pellet streak and impact treatments](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/red-rocket-concept-v1.png)

The new sheet retains the red/charcoal identity and adds richer crimson surfaces, dark steel and a gray upper treatment. Two visible barrels are a new design interpretation, not proof that the original sprite or firing code has two independently operated barrels. The two-pellet baseline is one shot event; do not accidentally charge ammunition twice or turn it into a two-shot burst.

The muzzle flash, two red streaks and impact dust are **proposed cosmetics**. The image is not an original-game screenshot, finished texture atlas, hand-clearance test or exported model. Its control opening and pronounced angled rear still need rigged-hand and interruption checks. The sheet does not yet cover every attachment, finisher or animation.

## Full feature plan

- **Feel:** a readable, forceful two-pellet event and recovery animation preserving native timing and resource behavior. Keep flash brief enough to see the target.
- **Barrel options:** a compact handling conversion, steadier long-profile conversion and explicitly optional fantasy projectile conversion. Any functional conversion needs its own costs, stats and authority rules; rockets are not the baseline.
- **Appearance:** original-fit and premium texture modes share behavior and recognizable geometry. Controlled roughness, edge wear and red material variation should read in Minecraft lighting without mandatory dynamic lights.
- **Resource modes:** preserve Spreadshot use. Reload is optional; any magazine/charge conversion needs explicit gameplay and animation definitions rather than being imposed by the renderer.
- **Animation:** equip, idle, aim, fire, recovery, optional reload, inspect, interruption, swap, first- and third-person hand fit. An inspection may show the craftsmanship without changing ammo or granting hidden bonuses.
- **Customization:** earned functional charms with explicit bonuses, modular handling/sights, skins, stickers, animated/glowing emblems, selectable tracers, impact decals and cosmetic confirmed-kill effects. Ornaments must clear hands and controls.
- **Original comparisons:** record actual projectile flight, entity/block impacts and sound before implementing new effects. Preserve loot and kill attribution for finishers.
- **Upgrade and dismantling:** explicitly define which pieces survive Haunted conversion; safely return incompatible attachments, including with a full inventory.
- **Performance:** cache configuration, bound particles/decals and light counts, use LODs, and measure frame-time lows with the real mod stack.

## Acceptance gates

- [ ] Native original two-pellet, resource, impact and audio capture
- [ ] Full attachment, inspect, projectile, decal and finisher concepts
- [ ] Rigged hand clearance, coherent proportions and two material modes
- [ ] Full animation/interruption and Haunted customization-transfer tests
- [ ] Native export, multiplayer, save, dismantling and performance qualification

[Exact released-class and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/red-rocket-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
