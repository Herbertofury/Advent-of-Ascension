# Discharge Sniper · capsule-powered explosive upgrade

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## The original is not a generic Metal Slug sniper

Discharge Sniper extends BaseSniper but overrides its ammunition with **Discharge Capsule** and creates **DischargeSlugEntity**. It inherits SCOPE_1 and uses the plasma-gun firing sound. Do not copy a conventional sniper's resource contract or the separate Discharge Shotgun's projectile arrangement into this weapon.

| Registered input | Value |
|---|---:|
| Damage constructor input | 10 |
| Durability | 540 |
| Firing delay | 24 ticks, nominally 1.2 seconds at 20 TPS |
| Stored recoil constructor input | Approximately 0.4 |
| Projectile constructor damage multiplier | 1 |
| Pierce argument | 0 |
| Launch-speed parameter | 20 |

These parameters are not a measurement of final explosion damage, effective range or animation recoil. The chosen projectile constructor also stores MAIN_HAND through BaseBullet although the weapon override receives a hand argument. Offhand attribution is a regression-test target, not an automatically proven runtime bug.

## Explosion behavior and world protection

Both entity and block impact methods call the projectile's explosion helper with **strength parameter 1.8**. The selected WorldUtil overload uses the projectile entity's coordinates; the impact Vec3 is not forwarded by this helper. Native collision-position tests should therefore compare the visual impact and actual explosion position before changing the path.

Terrain interaction is conditional. For a player owner, the helper checks the destructive-weapon-physics rule. Other living actors use Forge's mob-griefing event; the fallback uses the destructive-weapon rule. The resulting interaction selects MOB or NONE, with the fire flag false in this call.

Preserve this policy in a presentation upgrade. A dramatic cosmetic impact must not create a second explosion, bypass protection rules or edit blocks merely because the concept artwork shows debris. Native damage, attribution, multiplayer and protected-world tests remain open.

## Original appearance

![Released Discharge Sniper sprite, alpha-composited on a neutral background](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-sniper-original-preview.png)

Keep the deep-red upper barrel/shroud, separated lower-front red prong, pale silver muzzle and braces, gray rear grip, red rear assembly and raised dark sight with orange end accents. The neutral-background preview honors the original alpha channel. Invisible RGB pixels in the source file are not extra weapon geometry.

## Crafting and progression

![Discharge Rifle and Weapon Parts upgrade to Discharge Sniper](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/divine-upgrade-discharge_sniper.webp)

**Discharge Rifle + Weapon Parts → Discharge Sniper** in the bundled Divine Station upgrade recipe. This establishes an upgrade lineage, not a new invented manufacturing origin. Keep installed resource, durability and customization migration behavior explicit when implementing the upgraded form.

[Divine Station walkthrough](Divine-Station-Weapon-Upgrades-1.20.1) · [Complete illustrated upgrade atlas](Divine-Station-Upgrade-Atlas)

## Original flight visuals are still unresolved

The registered provider is DischargeSlugRenderer, confirmed through AoAEntityRendering's provider bootstrap. Its own addParticles method is empty. Its ParticleProjectileRenderer base calls that method and the EntityRenderer superclass, and returns null for its texture.

This inspection does not establish the bright red orb shown in the new concept as original in-game footage. A native capture and broader entity/particle tracing are still needed before declaring the original invisible or its visual behavior broken. Keep the new flight design explicitly separate from the extracted-source facts.

## Proposed premium design

![Discharge Sniper corrected concept labels and conditional impact study](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-sniper-concept-v2.png)

Crimson ceramic and silver framing amplify the original palette. The separated fore-end keeps the recognizable negative space; orange highlights retain the original sight accents. The red flight/tracer treatment and large impact flare are new concepts. The destructive impact panel is explicitly game-rule dependent.

The trigger-guard opening, grip proportions, optic alignment and underside support still require native hand-proxy and model checks. This sheet is not a completed mesh, texture set, animation package or accepted native weapon.

<details><summary>Earlier concept preserved</summary>

![Earlier Discharge Sniper concept](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/discharge-sniper-concept-v1.png)

Revision one used an overly definitive long-range/energy description and did not label the destructive impact's conditional policy. Revision two fixes those labels in the artwork itself; neither is native acceptance.

</details>

## Full feature and module plan

- **Shape/materials:** faithful red/silver/orange grouping, clear fore-end slot, two selectable visual treatments, authored UVs and controlled emissive detail.
- **Sights and handling:** preserve original scope semantics; offer compact hood and support variants, with actual camera/hand clearance and offhand tests.
- **Conversions:** a focused discharge emitter, a separately designed split-emitter variant and a fictional restrained-impulse module. Any changed shot count, damage, area, terrain interaction or cost must be explicit and server-authoritative.
- **Animation:** equip, idle, aim, confirmed fire, recoil/recovery, optional resource servicing, inspection, switching and interruptions with first/third-person hands. A cosmetic mechanism must not invent a forced bullet-magazine reload.
- **Feedback:** original-versus-new flight, muzzle, tracer and entity/armor/terrain/fluid impacts; bounded decals and confirmed-kill finishers. Support a non-destructive visual presentation without silently altering gameplay rules.
- **Customization:** earned charms, skins, stickers/emblems, configurable projectile/tracer/impact/death channels, effect salvage and full-inventory-safe returns.
- **Compatibility/performance:** preserve capsule spending, explosion ownership and game rules; test multiplayer, TaCZ/turret adapters, save migration and equivalent-work frame-time/memory behavior.

## Acceptance checklist

- [ ] Original native flight, impact, explosion-position, sound and scope footage
- [ ] Complete module, inspect, decal and finisher concept coverage
- [ ] Faithful model, hand fit, two texture modes and full animations
- [ ] Capsule accounting, offhand attribution and protected-world explosion tests
- [ ] Multiplayer, persistence, compatibility and performance qualification

[Released evidence and exact recipe](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/discharge-sniper-released-evidence.json) · [Separate shotgun profile](Discharge-Shotgun-Weapon-Profile) · [Weapon overhaul](Weapon-Overhaul)

Original AoA identity, assets and behavior are credited to Tslat and contributors. Source analysis, generated concepts and new implementation proposals remain distinct. Native acceptance stays zero.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
