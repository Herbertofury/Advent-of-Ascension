# Ghoul Cannon · violet shell, heavy shot

[Weapon overhaul](Weapon-Overhaul) · [Concept gallery](https://herbertofury.github.io/Advent-of-Ascension/weapon-concepts.html) · [Cannon progression and recipes](Cannon-Progression-and-Recipes-1.20.1)

![Detailed and world-fit Ghoul Cannon concept proposals](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ghoul-cannon-concept-v1.png)

**AoA 3.7.1 / Minecraft 1.20.1.** Released-source profile and first concept study. Neither finish is an implemented texture mode yet. Native upgraded weapon acceptance remains open.

## Preserve the original silhouette and materials

![Actual released Ghoul Cannon sprite, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ghoul-cannon-original-preview.png)

The source sprite is dark violet and black with grey end hardware, a broad hollow-sided front body, dark horizontal recesses and a descending rear grip. The concept develops that recognizable shape into a sculpted violet shell with restrained spectral accents. It deliberately avoids replacing the weapon with a generic modern rifle or an unrelated skull-face design.

The pictured incisions, vapor, surface weathering and glowing cavity treatment are proposed art. The actual recipe uses Ghoulasm and Ghoulish ingots, supporting a material-themed direction, but this study does not establish a canonical maker, origin dimension or detailed creation story. A name or color is not proof of lore.

## Released behavior

| Registration input | Value |
|---|---:|
| Damage | 25.5 |
| Durability | 590 |
| Firing delay | 34 ticks |
| Stored recoil constructor input | approximately 0.15 |
| Ammo | Cannonball |
| Automatic fire | No, inherited BaseCannon behavior |

GhoulCannon supplies the BALL_CANNON firing sound and creates GhoulBallEntity. It does not declare a dedicated impact/status-effect override. Do not advertise life stealing, fear, soul capture, poison or an explosion as existing behavior without additional evidence.

Shared cannon logic still applies: target armor/toughness influences the attack input; successful heavy attacks can apply shared knockback and shield behavior. The stored damage parameter is not a guaranteed final damage result or measured DPS.

## Projectile and impact comparison

![Released cannonball texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ghoul-cannon-projectile-preview.png)

The projectile constructor uses maximum age 120, piercing value zero and damage multiplier 1. Its gravity override returns 0.05. The renderer uses the ordinary cannonball texture and requests **three SPARKLER particles per render invocation**, colored **RGB (193, 64, 215)** at the projectile position.

That is not three particles per simulation tick. Upgraded trails need time-based emission and capped catch-up, with measured native costs. The glowing orb on the concept sheet is an artistic proposal; original in-flight and impact gameplay footage is still required. No original explosion or special defeat effect is established here.

## Craft it in the Infusion Table

![Pictured six-slot Ghoul Cannon infusion](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ghoul-cannon-infusion.webp)

[Open the exact interactive recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Ainfusion_ghoul_cannon)

1. Put a **Cannon Frame** in the separate base slot.
2. Fill six ingredient slots: **Ghoulasm twice**, **Ghoulish-ingot tag twice**, **Gunpowder tag once**, and **Iron-ingot tag once**.
3. Keep three ingredient slots empty. Ingredient order is flexible, but repeated ingredients require separate occupied slots; one stack does not replace two slots.
4. Check Imbuing and recipe availability. The bundled recipe omits infusion_level, so the inspected factory defaults to level 1. Datapacks and other releases may change this.

The displayed tag items are examples. Ghoulish ingot's bundled tag explicitly contains aoa3:ghoulish_ingot; the selected gunpowder and iron items must satisfy the effective tags in your installed pack. The diagram is reconstructed documentation, not a captured native crafting screen.

## Proposed attachment and customization direction

- **Original-form shell:** preserve the hollow-sided violet body and dark recesses as the default identity.
- **Spectral focus barrel:** an alternate magical focusing treatment; any beam behavior would be a new, explicitly balanced mechanic, not an original feature.
- **Lantern shroud:** optional visible containment styling and a quieter trail preset. Keep the target readable while aiming.
- **Grips and handling:** visibly different fitted grip options with explicit handling tradeoffs; first-person hand fit and animation clearance are required.
- **Two visual finishes:** detailed concept-fidelity materials and Minecraft-fitting textures on the same recognizable design. The sheet explores both; neither is a finished exported skin.
- **Earned charms, stickers and emblems:** gameplay-unlocked cosmetics and separately documented perk-bearing charms, with clear attachment zones and no obstruction of moving parts or sightlines.
- **Feedback choices:** customizable projectile/tracer/impact/decal and optional defeat effects. Never imply a cosmetic vapor effect changes hitboxes, damage or status effects.

## Full production gates

- [ ] Build and compare the actual mesh against the released sprite and concept, including both side views and first-person framing.
- [ ] Validate a comfortable full-hand grip, trigger interaction and all moving clearances; the concept alone does not pass ergonomic QA.
- [ ] Author equip, idle, aim, fire/recover, inspection and appropriate optional reload/recharge animations, including interruption cases.
- [ ] Produce muzzle, projectile, tracer, impact, decal and defeat-effect boards with original-versus-proposed labels.
- [ ] Build optional craftable variants and balanced attachment stats, plus reversible skins, charms and sticker placement.
- [ ] Preserve resource-system behavior; reloading remains optional where appropriate rather than mandatory across every AoA weapon.
- [ ] Capture original flight and impact in the target release and verify the recipe in native gameplay.
- [ ] Qualify export, hands, animation, multiplayer authority, compatibility and performance before marking a playable upgrade ready.

## Evidence

[Structured class and recipe evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ghoul-cannon-released-evidence.json) · [Pinned GhoulCannon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/GhoulCannon.java) · [Pinned projectile source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/entity/projectile/cannon/GhoulBallEntity.java)

Source research, concept quality, exported assets and native acceptance remain separate checks.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
