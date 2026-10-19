# Brown Blaster: the original Seaside-upgrade family

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · no accepted native upgrade.**

## Original behavior

Despite its name, Brown Blaster belongs to the **shotgun** family. The checked registration constructs `BaseShotgun` directly: three ordinary Limonite bullet entities, Spreadshot ammunition and non-automatic fire. No unique elemental, healing or explosive impact behavior is established by this registration.

| Released field | Brown Blaster | Blue Barrel upgrade |
|---|---:|---:|
| Stored damage input | 6.0 | 14.5 |
| Pellets | 3 | 3 |
| Durability | 300 | 1,120 |
| Delay | 54 ticks | 54 ticks |
| Recoil input | Approximately 0.9 | Approximately 0.4 |
| Knockback input | Approximately 0.4 | Approximately 0.4 |

These are constructor inputs, not measured final damage, camera angles or knockback distances. At 20 TPS, 54 ticks is nominally 2.7 seconds. Three pellets do not guarantee three successful hits or 18 total damage. The upgrade keeps the checked pellet count and delay while changing other fields; it is not evidence of an entirely different firing class.

## Recognizable original materials

![Released Brown Blaster sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/brown-blaster-original-preview.png)

Keep the long dark front, understated gray upper line, brown lower-front area and warm brown rear/grip. The premium concept should make a comparatively simple weapon feel well made, rather than adding glowing fantasy parts that erase its identity.

Leather is a verified infusion ingredient. Cognac leather treatment, bronze fasteners and decorative surface craftsmanship are new visual choices; they are not a confirmed historical maker or manufacturing story.

## Make the Brown Blaster

At the checked release's **Infusion Table**, put a Shotgun Frame in the separate left base slot and use four middle slots for:

- Spreadshot ×1
- One ingredient matching `forge:leather`
- One ingredient matching `forge:ingots/iron`
- One ingredient matching `forge:gunpowder`

Leave the other five middle slots empty. Tag membership can change with modpack data. The exact definition is `data/aoa3/recipes/infusion_brown_blaster.json`; omitted infusion-level and XP fields use the checked defaults, level 1 and XP 0–0.

[Illustrated 1.20.1 Infusion Table workflow](Infusion-Table-Crafting-1.20.1) · [Released recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=infusion_brown_blaster)

## Upgrade into Blue Barrel

Use the **Divine Station**, not the Infusion Table, for this next step:

1. Brown Blaster in the left input
2. Seaside Upgrade Kit in the middle input
3. Check Blue Barrel in the right output before taking it

The exact definition is `data/aoa3/recipes/upgrade_kit_blue_barrel.json`. The base recipe assembles its declared output rather than inherently copying every piece of input customization. Test named, enchanted or third-party-modified weapons on a disposable copy first.

[Illustrated Divine Station guide and data-transfer limits](Divine-Station-Weapon-Upgrades-1.20.1) · [Blue Barrel profile](Blue-Barrel-Weapon-Profile)

## Concept: restrained craftsmanship, clear family continuity

![Brown Blaster hero, side silhouette, material study and Blue Barrel family-upgrade comparison](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/brown-blaster-concept-v1.png)

The sheet uses warm brown surfaces and dark steel for the original weapon, then shows its Seaside counterpart as a separate comparison. The blue gun in that lower panel is the upgrade reference, not a blue-glowing default Brown Blaster. The material closeup is concept art, not a completed texture atlas.

The visible grip/control opening still needs actual player-hand and animation clearance checks. This sheet covers hero, silhouette, material and family continuity. Projectile, muzzle, impact, finisher, full attachments and complete animation storyboards remain open.

## Complete upgrade plan

- **Firing feel:** preserve the three-pellet baseline and deliberately stronger recoil input than Blue Barrel. Make recovery readable without silently changing the released shot delay.
- **Barrel and handling options:** a compact handling conversion, steadier precision conversion, alternate fore-end and low-profile sight. Every functional change needs an explicit stat/resource rule and matching appearance.
- **Original resource mode:** reload remains optional. A conversion may introduce a magazine or charge cycle only when its mechanics are defined; do not impose one on the original resource path by accident.
- **Materials:** original-fit and premium treatments share geometry and behavior. Use detailed brown material work and controlled metal wear without mandatory dynamic lights.
- **Projectile / muzzle / impact:** first capture the original. Optional understated trails, short muzzle feedback and surface-aware impact dust remain separate from authoritative hit rules.
- **Inspect / animations:** equip, aim, fire, optional reload, inspect and interruption in first/third person. A restrained hand-check or material-detail inspection should not change ammo or provide a gameplay bonus.
- **Customization:** earned charms and explicit bonuses, skins, stickers, animated/glowing emblems, custom projectile/tracer/impact/finisher choices. Keep ornaments clear of hands and controls.
- **Crafting / upgrade continuity:** preserve both released routes. Define which attachments and cosmetics survive Seaside conversion, return incompatible pieces safely and test full-inventory dismantling.
- **Finishers:** optional cosmetic confirmed-kill effects preserving loot, kill credit and multiplayer state; no invented baseline elemental damage.
- **Performance:** cached configuration, no repeated idle scanning, bounded effects/LODs and measured frame-time lows on the intended mod stack.

## Open acceptance gates

- [ ] Original projectile/impact/audio captures and native three-pellet/resource tests
- [ ] Full attachment, muzzle, projectile, impact and finisher concept coverage
- [ ] Consistent model proportions, actual hand fit and both material treatments
- [ ] Full animation/interruption and Seaside customization-transfer tests
- [ ] Native export, multiplayer, persistence, dismantling and performance qualification

[Source and comparison evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/brown-blaster-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
