# Ancient Bomber · a jewel-toned grenade cannon

[Weapon overhaul](Weapon-Overhaul) · [Cannon progression](Cannon-Progression-and-Recipes-1.20.1) · [Divine Station upgrades](Divine-Station-Weapon-Upgrades-1.20.1)

![Ancient Bomber premium and world-fit concept study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ancient-bomber-concept-v1.png)

**AoA 3.7.1 / Minecraft 1.20.1.** Released-source profile and partial concept study. This is not a finished TaCZ gun, native screenshot or accepted animation set.

## Original identity and acquisition

![Actual Ancient Bomber released sprite, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ancient-bomber-original-preview.png)

A low, long charcoal body with stepped upper edges gives Ancient Bomber its silhouette. Cyan beneath the front, crimson around the upper receiver, a purple rear grip and a yellow-green rear accent distinguish it from its Boom Cannon input. The concept expands those regions into carved dark panels and jewel-like accents. The large stock, crystalline surfaces, inspection glyph and stylized impact are proposed reinterpretations, not established original lore.

The reviewed recipe establishes an **Ancient Upgrade Kit** conversion of **Boom Cannon**. It does not establish a particular maker, civilization or origin dimension. Preserve the actual sprite and recipe alongside every new design.

## What it fires

AncientBomber extends BaseCannon but overrides its ammunition and projectile factory. It consumes **Grenades**, not the Cannonballs used by the shared cannon default. Its sound override uses **ITEM_BOOM_CANNON_FIRE**.

| Stored registration input | Value |
|---|---:|
| Weapon damage parameter | 23.5 |
| Durability | 855 |
| Firing delay | 28 ticks |
| Recoil | Approximately 0.175 |
| Ammo item | Grenade |
| Projectile | GrenadeEntity |
| Projectile gravity return | 0.075 |

**Do not advertise the stored 23.5 parameter as a verified 23.5-point grenade explosion.** GrenadeEntity dispatches the separate GRENADE ShrapnelExplosion definition. That definition uses radius 3, penetration 7 and base damage 5. ShrapnelExplosion then applies its own distance and ray-hit calculations; armor, events and installed compatibility code can affect the eventual combat result. These are game-code parameters, not a measured DPS result.

The firing factory supplies maximum age 120, damage multiplier 1 and piercing value 0. BaseBullet's age expiry discards the projectile; it does not establish a timed explosion fuse. Both block and entity impact dispatch the explosion on the server. Fire damage can also detonate this projectile. Preserve these distinctions when designing reloads and effects.

Player-owned terrain damage consults AoA's destructive weapon physics rule; other ownership paths consult Forge mob-griefing behavior. The default affected-entity predicate excludes the direct and indirect exploders. These source facts do not replace native friendly-fire, griefing, protection-mod and multiplayer tests.

## Original projectile presentation

![Extracted grenade texture atlas, enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ancient-bomber-projectile-texture-preview.png)

This image is the original **texture atlas**, not a flat projectile billboard or an in-flight game capture. The registered ModelledProjectileRenderer uses GrenadeModel, whose source defines four boxes and rotates the model while it is moving. It uses a 16 × 16 texture layout. The small fourth box overlaps the upper part of the first source box; retain the source evidence rather than silently repairing it and claiming the result is the original.

The inspected explosion definition selects the ordinary explosion particle for its radius, subject to the explosion's execution path. The concept's crimson ring, glowing shards and dramatic debris are new cosmetic proposals. They do not promise block destruction, a wider damage radius or extra projectiles. Original flight, hit and expiry footage remains an open requirement.

## Crafting walkthrough

![Reconstructed Ancient Bomber upgrade recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ancient-bomber-upgrade-recipe.webp)

[Open the exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&recipe=aoa3%3Aupgrade_kit_ancient_bomber)

1. Bring **Boom Cannon** and **Ancient Upgrade Kit** to the Divine Station.
2. Put Boom Cannon into the left input and the kit into the second input.
3. Check the Ancient Bomber output before taking it. This is an upgrade-kit recipe, not an Infusion Table ingredient grid.
4. Verify preservation of enchantments, custom attachments and third-party data separately. The existence of this recipe is not proof that every extension survives conversion.

The pictured diagram is reconstructed from bundled data and item icons. Datapacks and other AoA releases may change the effective recipe.

## Full upgrade direction

- **Two presentation modes:** retain the original color blocking and stepped silhouette in both Minecraft-fit and premium materials. Validate the rear grip, hand space, sight line and first-person screen occupancy before accepting geometry.
- **Inspection:** the crimson inset projects a brief angular glyph, then collapses back into the receiver. Cosmetic animation must interrupt cleanly for firing, swapping and holstering without changing ammo.
- **Firing feedback:** readable muzzle pulse, weighty recovery, a visible grenade silhouette and short-lived impact accents. Keep gameplay trajectory and impact authority separate from decorative trails.
- **Optional loading:** make a clear fantasy resource path and sufficient hand clearance. The default resource remains Grenades; no forced extra reload delay or free ammo from an animation callback.
- **Functional variants:** separately craftable arc-control, bounce or multi-projectile fantasy conversions can offer new behavior, but require explicit resource, damage, fuse/impact, ownership and server rules. None is assumed to exist in the original weapon.
- **Modular appearance:** alternate cyan and crimson channel finishes, comfortable grip panels, sight housings, earned charms, static/animated/glowing stickers and custom emblems. Preserve readable original identity under every skin.
- **Effects customization:** separate muzzle, tracer, flight, entity/armor/stone/fluid impact, bounded decal and confirmed-kill finisher options. A cosmetic blast ring must not change hit detection or terrain.
- **Salvage:** dismantle eligible modules and transfer compatible effects with full-inventory return behavior, no duplication and versioned save data.
- **Integration:** qualify TaCZ attachment and turret adapters, protection rules, ammo bridges and AoA progression. Turret ownership and destructive-physics behavior require dedicated tests.

## Quality gates still open

- [ ] Original native fire, flight, impact, expiry and terrain-rule recordings
- [ ] All-view concept match, hand/guard clearance and credible fictional loading path
- [ ] Finished UVs and textures for both visual modes
- [ ] Equip, holster, idle, aim, fire/recovery, inspection and optional loading animations
- [ ] Complete projectile, muzzle, tracer, impact, decal, finisher and attachment concept boards
- [ ] Native damage/resource tests, server authority, ownership and multiplayer recovery
- [ ] Crafting, salvage, save migration and optional-mod compatibility
- [ ] Equivalent-content startup, memory and frame-time measurements

## Evidence

[Released class hashes and structured facts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/ancient-bomber-released-evidence.json) · [Pinned weapon source](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/item/weapon/cannon/AncientBomber.java) · [Grenade behavior](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/content/entity/projectile/thrown/GrenadeEntity.java) · [Explosion implementation](https://github.com/Tslat/Advent-Of-Ascension/blob/0be2106bebb3851c5ba2cc9974e57936a867244d/source/library/object/explosion/ShrapnelExplosion.java)

Original AoA assets and identity are credited to Tslat and contributors. Generated concept art and new customization ideas are separate. No native upgraded weapon acceptance is promoted by this page.
