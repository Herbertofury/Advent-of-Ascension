# Purple Punisher: the Haunted Red Rocket upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## Original behavior and family continuity

Purple Punisher is constructed directly as **BaseShotgun**. It fires two ordinary Limonite bullet entities using Spreadshot ammunition and the inspected non-automatic base behavior. Its purple palette and Haunted upgrade route do not establish ghost damage, soul-energy projectiles, life steal or an explosion hook.

| Stored field | Red Rocket | Purple Punisher |
|---|---:|---:|
| Damage input | 11.5 | 20.5 |
| Pellet count | 2 | 2 |
| Durability | 500 | 1,120 |
| Shot delay | 52 ticks | 52 ticks |
| Recoil input | Approximately 0.4 | Approximately 0.2 |
| Knockback input | Approximately 0.785 | Approximately 0.785 |

These are released constructor inputs, not guaranteed final damage or measured physical quantities. At 20 TPS the nominal delay is 2.6 seconds. Two pellets do not guarantee 41 total damage. The upgrade retains the checked shot delay and pellet count while altering damage, durability and recoil input.

## Recognizable original

![Actual released Purple Punisher sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/purple-punisher-original-preview.png)

Keep the dark horizontal upper body, gray longitudinal band, saturated purple underside, raised purple top accents and broad violet rear/grip. The Haunted kit is a verified recipe association. Obsidian-like metal, violet enamel, etched ornament and a haunted architectural backdrop are creative interpretations, not a documented maker, material recipe or location of manufacture.

## Make the upgrade

First obtain the [Red Rocket](Red-Rocket-Weapon-Profile) using its verified five-slot infusion recipe. Then use the **Divine Station**:

1. Put Red Rocket in the left input.
2. Put a Haunted Upgrade Kit in the middle input.
3. Confirm Purple Punisher in the right output before taking it.

The bundled definition is `data/aoa3/recipes/upgrade_kit_purple_punisher.json`. The recipe does not establish where every kit is acquired. Its base assembly returns the declared output rather than promising arbitrary input customization will be copied. Test names, enchantments and third-party attachments on disposable copies before converting valuable equipment.

[Illustrated Divine Station guide and customization-transfer limits](Divine-Station-Weapon-Upgrades-1.20.1) · [Exact recipe explorer](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=upgrade_kit_purple_punisher)

## Concept: vivid materials and an inspect moment

![Purple Punisher hero, side profile, material treatments and proposed inspection storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/purple-punisher-concept-v1.png)

This sheet develops violet surfaces and dark metal while retaining family continuity. Its small low-resolution inset is a **new generated style interpretation**, not the actual original sprite above or a completed in-game texture. Likewise, the three inspection panels are proposed poses, not rendered animation frames from an implemented rig.

The two visible muzzles are a visual interpretation. Native behavior still produces two pellets from one accepted shot; the model must not invent two independent ammo charges or a two-shot burst. The broad rear/grip and control opening need real hand-fit and clearance review. A static image cannot prove the hands remain clear throughout motion.

## Full feature plan

- **Feel:** clearly readable two-pellet feedback with the original timing, and a less forceful camera/recovery treatment than Red Rocket's checked recoil input. Preserve actual native authority.
- **Inspection:** rotate the closed prop to reveal its purple finishing, then settle cleanly into aim. Cancellation must restore hands and pose without changing resources or granting hidden bonuses.
- **Barrels and handling:** precision, compact and alternate fore-end/sight options. An optional spectral visual treatment is distinct from a functional ghost-damage conversion; each functional upgrade needs explicit costs and rules.
- **Resources:** retain original Spreadshot behavior. Reload remains optional, with any magazine or charge-cycle conversion explicitly defined.
- **Materials:** Minecraft-fit and premium modes share behavior and silhouette. Avoid permanent expensive lights and excessive bloom that erase surface detail.
- **Effects:** obtain original projectile/muzzle/entity/block-impact footage first. Then provide separate tracer, projectile appearance, impact dust/decal, muzzle and confirmed-kill cosmetic choices without changing collision, loot or kill credit.
- **Animation:** equip, idle, aim, fire, recovery, optional reload, inspect and interruptions, in first and third person. Test gloves, skins and handedness against the actual model.
- **Customization:** earned functional charms, stickers, animated/glowing emblems, skins and clear attachment stats. Keep decorations out of hand/control paths.
- **Persistence and dismantling:** explicitly preserve or return incompatible pieces during the Haunted conversion. Test full inventories, save/reload, multiplayer and unequip during animations.
- **Performance:** cache configuration, use bounded effects and LODs, and measure frame-time lows on the real target stack.

## Acceptance gates

- [ ] Actual original projectile, impact, sound and resource captures
- [ ] Full attachment, muzzle, tracer, decal and finisher concept coverage
- [ ] Model proportions, rigged hand clearance and two material modes
- [ ] Full animation/interruption and customization-transfer tests
- [ ] Native export, multiplayer, persistence, dismantling and performance qualification

[Released-class and recipe evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/purple-punisher-source-evidence.json) · [Complete feature standard](Weapon-Completeness-Standard) · [Armory gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html)

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
