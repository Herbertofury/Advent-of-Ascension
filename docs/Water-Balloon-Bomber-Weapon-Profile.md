# Water Balloon Bomber · a seaside carnival upgrade

[Weapon overhaul](Weapon-Overhaul) · [Illustrated armory](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html) · [Cannon progression](Cannon-Progression-and-Recipes-1.20.1)

![Premium and world-fit Water Balloon Bomber design proposals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/water-balloon-bomber-concept-v1.png)

**AoA 3.7.1 / Minecraft 1.20.1. Source profile and partial concept study, not a finished playable upgrade.** The two finishes, inspection, splash and accessories pictured above are proposed art.

## Original identity and verified lineage

![Actual released item sprite, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/water-balloon-bomber-original-preview.png)

The released sprite has a broad teal body, vivid lime bands and two raised cyan shapes. The premium concept develops these into watery domes and a polished carnival-like shell; the world-fit treatment preserves the same recognizable palette and broad silhouette. The shell ornament, liquid interior, grip treatment and jellyfish charm are new design proposals.

Its bundled upgrade is **Balloon Bomber + Seaside Upgrade Kit**. This establishes an upgrade lineage, not a canonical inventor, origin dimension or creation story. Do not invent ocean lore solely from the colors or kit name.

## Released behavior

| Stored registration input | Value |
|---|---:|
| Damage parameter | 20.5 |
| Durability | 855 |
| Firing delay | 24 ticks |
| Recoil | approximately 0.20 |
| Ammunition | Balloon |
| Firing sound | BALL_CANNON_FIRE |

The weapon overrides the normal Cannonball ammunition choice and creates WaterBalloonBombEntity. Its constructor requests a maximum age of 120, piercing value zero and damage multiplier 1. Gravity returns 0.1. These are source parameters, not a measured trajectory, guaranteed damage result or DPS figure.

### It does more than a cosmetic splash

Both block and entity impact call the projectile's explode method. That method first requests an explosion with strength input **1.5** through WorldUtil. The helper chooses terrain interaction according to the owner and destructive-weapon/mob-griefing rules; the number alone does not establish a fixed radius or terrain outcome.

The subsequent water-placement path requires server side, destructive weapon physics enabled, an empty projectile-position block, a non-ultrawarm dimension and a successful placement permission check. It then searches downward through replaceable blocks and places a water block above the support it finds, subject to its Y-bound checks. This is a real world-change pathway. A prettier splash must not silently bypass those gates, create extra water, or confuse a cosmetic puddle with a placed fluid block.

## Original projectile versus proposed feedback

![Actual released balloon projectile texture, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/water-balloon-bomber-projectile-preview.png)

The renderer uses the shared **balloon_bomb.png** texture and requests **eight cyan SPARKLER particles per render invocation** at the projectile position. The texture image is extracted evidence, not an in-game flight screenshot. Eight per render is not eight per simulation tick.

The concept proposes a translucent water-balloon form, a short readable droplet trail and a splash with an immediate clear center. Those effects are not the original implementation. Use bounded game-time emission, distance tiers and reduced-effects options; never make trail count scale without limit with FPS. Original flight, impact and fluid-placement footage still needs capture in the target build.

## Make the upgrade at the Divine Station

![Balloon Bomber plus Seaside kit produces Water Balloon Bomber](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-water_balloon_bomber.webp)

[Open the exact interactive recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Aupgrade_kit_water_balloon_bomber)

1. Obtain the original [Balloon Bomber](Balloon-Bomber-Weapon-Profile).
2. Use it with one Seaside Upgrade Kit in the Divine Station upgrade workflow.
3. Confirm the output is Water Balloon Bomber in the effective installed recipe set. This is not a crafting-grid or Infusion Table recipe.
4. Before changing a valued item, validate preservation of names, enchantments and custom extension data in the actual build. An illustrated recipe does not certify every property-transfer path.

## Fun customization direction

- **Default aquatic shell:** recognizable lime bands, teal body and paired cyan domes in both detailed and world-fit material modes.
- **Bubble sight:** a restrained circular visual cue that stays readable while aiming; no targeting advantage is inferred from a cosmetic attachment.
- **Jellyfish and shell charms:** earned accessories with bounded secondary motion. Any perk-bearing variant needs explicit gameplay rules and a documented acquisition path.
- **Alternate magical discharge styles:** a focused stream, a wide splash and a bouncing bubble are possible separately crafted gameplay variants, with declared resource costs and server-authoritative behavior. None is a released feature demonstrated by this sheet.
- **Handling and shell parts:** fitted grips and visible trim variants; improvements must remain legible without losing the original silhouette. Check hands and the guard with actual first-person poses.
- **Personal effects:** configurable droplets, tracer styles, impact decals and an optional bubble-dissolve defeat effect. Decals and defeat visuals must not destroy world blocks or replace the actual reward/death logic.
- **Stickers and emblems:** static, glowing and animated placements on declared shell zones, with reduced-animation settings and no obstruction of sights or state indicators.
- **Optional reload/recharge presentation:** preserve the original Balloon resource contract by default. A loading animation cannot grant ammunition or introduce mandatory downtime merely because the model looks more elaborate.

## Source quirks that must reach QA

The inspected downward search uses a literal **Y=0** bound rather than the dimension's minimum build height. Treat below-zero worlds and custom-height dimensions as explicit regression cases, not as proven supported behavior. Also test claim protection at the final fluid destination: the shown permission check occurs at the projectile position before the lower target is resolved. These are source observations and test requirements, not claims that a fix has been implemented or a protection bypass reproduced.

Test both hands, player and non-player owners, empty/solid impacts, entities, ultrawarm worlds, destructive physics on/off, claimed areas, negative heights, save/reload and multiplayer. The rendered concept is not evidence for any of those cases.

## Newer source is a different behavior contract

A separate comparison against the refreshed official **1.21 branch**, pinned to **7919b5fe48599e6105c5740937ce36c36ef21d16**, finds a different implementation. WaterBalloonBombEntity now uses a server-side explosion builder and shot context. The water-balloon explosion definition supplies radius 2, entity-damage input 4, block-damage input 3 and block-drop-chance input 0.1, with a cannon-dependent damage function. These are different API parameters; do not equate them directly with the older strength input of 1.5 or advertise a measured buff.

After the newer explosion, its callback checks server side, non-ultrawarm dimension and destructive weapon physics. If the explosion-position block is air, it places water **there**, then schedules a callback after **20 ticks** that sets the same position to air. The older downward placement search and this newer temporary-water behavior are not interchangeable.

**Preservation and safety requirements:**

- Keep the selected release's behavior explicit. Importing a newer renderer must not silently change persistent water into temporary water, change impact location or alter damage/economy.
- Test a player or another mod replacing that temporary water before cleanup. The inspected scheduled callback does not itself check whether the block is still the water it placed. This is a source-level overwrite risk to investigate, not a reproduced loss report.
- Any new cleanup implementation should verify its own effect/state ownership before removing anything, and handle overlapping effects, chunk/dimension unloading and save/reload. A cosmetic effect must never delete a later player block.
- Audit protection hooks at the actual destination in both versions. Validate fluid spreading and its cleanup policy rather than assuming one removed source block restores the entire world.

[Version-comparison evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/water-balloon-version-comparison.json) · [Newer projectile source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/projectile/cannon/WaterBalloonBombEntity.java) · [Newer explosion definitions](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/common/registration/AoAExplosions.java)

This comparison is source analysis only. Neither version has been natively exercised by this study, and no automatic semantic merge is approved by these facts.

## Full production gates

- [ ] Match mesh silhouette and both material modes to the original and approved concept from both sides and first-person views.
- [ ] Validate full-hand clearance, guard interaction, charm motion and all attachment/animation collisions.
- [ ] Author equip, holster, idle, aim, fire/recover, inspection and any optional loading states with interrupt-safe transitions.
- [ ] Expand separate muzzle, flight, impact, decal and defeat-effect boards with original-versus-proposed labels.
- [ ] Build and balance craftable variants, handling parts, charms, stickers and skins; preserve reversible item data.
- [ ] Capture native original projectile and water-placement behavior, including the height and protection cases above.
- [ ] Qualify native export, multiplayer authority, optional integrations and equivalent-work performance.

## Evidence

[Structured registration, class and recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/water-balloon-bomber-released-evidence.json) · [Pinned weapon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/WaterBalloonBomber.java) · [Pinned projectile source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/entity/projectile/cannon/WaterBalloonBombEntity.java) · [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/client/render/entity/projectile/cannonshots/WaterBalloonBombRenderer.java)

Original AoA identity belongs to Tslat and contributors. Concept art is an authored upgrade exploration. No upgraded native weapon acceptance is promoted here.
