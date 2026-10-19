# Blue Barrel: the Seaside upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · no accepted native upgrade.**

## Original behavior

Blue Barrel is registered directly as **`BaseShotgun`**, with three ordinary Spreadshot pellets. There is no unique Blue Barrel subclass in the checked registration. Its color and Seaside recipe association do not establish water damage, slowing, freezing or a special impact effect.

| Released field | Value / limit |
|---|---|
| Registry ID | `aoa3:blue_barrel` |
| Stored damage input | 14.5; not guaranteed final damage |
| Pellet count | 3 |
| Durability | 1,120 |
| Delay | 54 ticks, nominally 2.7 seconds at 20 TPS |
| Recoil input | Approximately 0.4; not camera degrees |
| Knockback input | Approximately 0.4; not a measured distance |
| Ammunition / mode | Spreadshot / non-automatic |
| Projectile class inherited from the base loop | `LimoniteBulletEntity` |

Do not multiply three pellets into a guaranteed 43.5 damage total: hit registration, immunity and shared damage rules still apply. Original in-flight and contact visuals need actual game captures before visual replacements are accepted.

## The original identity

![Released Blue Barrel sprite, enlarged with nearest-neighbor sampling](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/blue-barrel-original-preview.png)

Keep the long charcoal front, small blue forward accent, angular gray body and prominent deep-blue rear/grip. Its silhouette should remain visibly related to the released sprite rather than becoming a generic futuristic pistol.

The verified lineage is **Brown Blaster → Seaside Upgrade Kit → Blue Barrel**. Coastal engraving, blue enamel, sea glass and a sweeping light inspection are new visual interpretations of that association. The inspected data does not establish a named maker, manufacturing location or an aquatic operating mechanism.

## Released upgrade route

The exact `data/aoa3/recipes/upgrade_kit_blue_barrel.json` definition has:

| Field | Required item |
|---|---|
| Input | Brown Blaster |
| Upgrade kit | Seaside Upgrade Kit |
| Result | Blue Barrel |
| Serializer | `aoa3:upgrade_kit` |

This is an upgrade-kit recipe, **not** an ordinary shaped grid or the Infusion Table recipe used by Vivo and Ginger Blaster. Use the **Divine Station**: Brown Blaster in the left input, Seaside Upgrade Kit in the middle, then inspect the right-hand output. [Illustrated 1.20.1 Divine Station guide](Divine-Station-Weapon-Upgrades-1.20.1) explains slot indexing, source availability and data-transfer limitations. Arbitrary attachment, custom-name or enchantment preservation must be checked in that path before upgrading a valuable customized item.

[Inspect the released recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=upgrade_kit_blue_barrel)

## Concept: deep-blue enamel and controlled coastal detail

![Blue Barrel premium hero, Minecraft-fit material direction, rear-mounted sea-glass charm and inspection-light proposal](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/blue-barrel-concept-v2.png)

The sheet keeps a long dark barrel and cobalt rear section, adding restrained metal tide-line detailing. A dedicated Minecraft-fit material treatment should share geometry, attachment sockets and behavior with the premium treatment.

The first draft placed its optional charm beside the trigger. That failed visual placement review. This revision relocates it to the far rear cap; a real model still needs full hand, charm-swing and attachment collision tests. A better picture is not a collision certificate.

The inspect ribbon is proposed cosmetic light following the engraved lines, with no extra damage, resource refill, fluid placement or gameplay pulse. Offer a reduced-effects version. This is a partial hero/material/inspect sheet; projectile, impact, finisher and complete attachment boards remain open.

## Full feature plan

- **Firing:** preserve the original three-pellet mode; deliberate weight, readable recoil and quick visual recovery without secretly changing the released delay.
- **Alternative barrels:** restrained precision-choke conversion, broad scatter conversion and a separately balanced fantasy tide-pulse conversion. New projectile or damage behavior requires explicit costs, rules and matching visuals.
- **Handling and attachments:** low-profile sight options, grip/support changes, muzzle treatments and rear-cap accessories. Confirm finger room and unobstructed aiming. Any suppressor-like module needs declared sound and balance behavior rather than an automatic realism claim.
- **Optional reload:** retain original resource behavior. Physical reloads apply only to conversions that explicitly support a magazine or charge system.
- **Projectiles, tracers and impacts:** capture the original first; keep cosmetic blue traces separate from collision. Material-aware dust/sparks and optional mist should be bounded, readable and client-configurable.
- **Finishers:** optional earned cosmetic kill effects must preserve loot, kill credit and multiplayer state. Do not turn an aesthetic tide flourish into an undocumented area attack.
- **Inspect and animation:** equip, aim, fire, optional reload, inspect and cancellation in first and third person. Effects must stop cleanly on interruption, death, swap and disconnect.
- **Customization:** gameplay-earned charms with explicit bonuses, skins, stickers, animated/glowing decals, custom emblems and independently chosen projectile/tracer/impact/finisher effects.
- **Crafting and dismantling:** keep the source upgrade route; add declared recipes for new parts, reversible material choices and safe special-effect transfers. Test full inventories and item conservation.
- **Performance:** cache attachment state, avoid repeated idle scanning, use bounded particles/LOD and measure frame-time lows with the exact mod stack.

## Quality gates still open

- [ ] Original projectile/impact/audio captures and native three-pellet tests
- [ ] Full concept coverage for attachments, projectile, impact and finisher options
- [ ] Consistent multi-view model, actual hand fit and rear-charm sweep clearance
- [ ] Complete animation/interruption, resource and dismantling tests
- [ ] Native export, multiplayer, save/update and performance qualification

[Source evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/blue-barrel-source-evidence.json) · [Full feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)
