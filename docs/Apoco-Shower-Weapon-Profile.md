# Apoco Shower — three descending Spirit shots

**AoA 3.7.1 / Minecraft 1.20.1 source baseline. New concept exploration; no accepted native upgraded weapon.**

Apoco Shower upgrades **Spirit Shower** using an **Apoco Upgrade Kit**. It is a Spirit-powered blaster, distinct from both Apoco Rifle and Apoco Assault Rifle. A shared kit and color family do not mean the weapons share ammunition or attack rules.

## What it actually does

One call to its released firing override attempts to spawn three projectiles: Shower Shot, Weighted Shower Shot and Heavy Shower Shot. Each receives an age parameter of 60; their gravity returns are **0.05, 0.1 and 0.2**, respectively. This produces a meaningful three-path identity to preserve, rather than replacing the weapon with three identical straight bullets.

The weapon's block-impact override requests an explosion with strength input **2.5**. Its entity-impact effect requests the same input, but there is an important condition: the inherited entity-hit handler invokes that effect only if the shared energy-attack helper returns true. The base damage input is zero, and that helper forwards the attack to the target's damage method. Native zero-damage, immunity and event behavior must be tested. Do not promise that every entity contact explodes, and do not label the weapon harmless merely because its direct damage input is zero.

## Released inputs

| Property | Verified input / boundary |
|---|---|
| Item | `aoa3:apoco_shower` |
| Base direct damage | 0; explosion behavior is separate |
| Durability | 3,760 |
| Firing delay / inherited charge-time input | 10 / 10 ticks |
| Nominal time at 20 TPS | 0.5 seconds for each input; not a measured end-to-end firing cadence |
| Base resource cost | 80 Spirit; native modifiers and consumption rules remain authoritative |
| Spawn attempts per override call | One each of Shower, Weighted Shower and Heavy Shower |
| Projectile age parameter | 60 each; not a measured range or exact expiry guarantee |
| Gravity returns | 0.05 / 0.1 / 0.2; game parameters, not physical SI units |
| Explosion helper input | 2.5; not final damage or a guaranteed radius |
| Sound | ITEM_SPIRIT_SHOWER_FIRE |

The shared firing path tries resource consumption before calling this three-spawn override. Do not charge Spirit three times merely because three visual channels are modeled. Spawn attempts also are not guarantees that every entity is accepted by all runtime hooks.

## Original appearance and progression

![Actual released Apoco Shower sprite, enlarged without smoothing](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-shower-original-preview.png)

Its recognizable features are a large pale front frame, a dark olive/black body, lime accents and red upper details. The concept develops those features into a distinctive front crescent and layered shell.

The exact packaged recipe is **Spirit Shower + Apoco Upgrade Kit → Apoco Shower**. The kit is referenced by the packaged Vox Ponds loot table. This is evidence of association, not proof that the dimension or acquisition route is active in every installed release. A fungal/root-like construction or named maker is not established by that table.

[Version-aware recipe browser](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.20.1&q=aoa3%3Aapoco_shower) · [Pinned released evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-shower-released-evidence.json).

## Premium concept and functional variants

![Apoco Shower concept, front-shroud variations and qualitative effect studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/apoco-shower-concept-v1.png)

The large pale front frame encloses a proposed triad of spirit knots. The dark frame, red upper armor and lime seams retain the source palette. Fungal details are new art interpretation. The drawn arcs are qualitative; the picture does not measure original trajectories or impacts.

- **Cascade shroud:** preserve a legible three-path discharge while offering an explicitly selected spread module.
- **Focus shroud:** a visibly converging frame for an alternate trajectory/handling configuration. Any range or cost change must be declared and implemented server-side.
- **Tempest shroud:** a rotating outer frame and a distinct tumbling-energy presentation; rotation cannot silently multiply projectiles or damage.
- **Inspection:** open the front shell around a seated core, then return to the exact ready pose. Inspecting must not spawn harmful shots, spend Spirit or detach parts permanently.
- **Resource presentation:** a Spirit/recovery visual instead of a mandatory conventional magazine reload. Reloading remains optional and tied to the selected resource design.
- **Handling and comfort:** remove or reshape underside ornament that collides with hands, camera, attachments or animation sweeps. Concept art is not clearance proof.
- **Progression:** earn functional charms, effect modules and alternate shrouds through gameplay. Dismantling/salvage must preserve explicit provenance, compatibility and saved-build state.
- **Cosmetics:** Minecraft-fit and richer concept-faithful profiles; skins, custom/animated/emissive stickers and emblems; projectile, trail, impact/decal and finisher options. Visual choices cannot conceal collision or silently change gameplay.

## Original renderer and the performance work

The inspected Shower Shot renderer uses particles instead of a projectile texture. It loops three times, requesting a red Sparkler and a black Sparkler each time: **six particle requests per projectile render invocation**. The shared renderer calls that routine from rendering. If a pass renders all three shots once, that is 18 requests for that pass; it is not 18 per shot activation or a measured particles-per-second rate.

A bounded per-projectile game-time trail policy should prevent extra rendering passes from multiplying emissions, while retaining the recognizable red/black appearance and clear arcs. The [tested trail-clock component](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/Projectile-Trail-Clock.md) is reusable logic, but its integration, density tuning and native performance remain unverified. Six requests per render must not be silently reinterpreted as a proven six-per-tick budget.

Original in-game flight, entity impact and block impact footage is still required. The dramatic concept effects are not substituted for those captures. World damage must respect native permission and game-rule handling.

## Acceptance checklist

- [ ] Capture all three original trajectories and verify charge/cadence/resource behavior in the pinned game.
- [ ] Test block impact, successful/rejected zero-damage entity attacks, immunity, event cancellation and explosion behavior.
- [ ] Author concept-faithful separate parts, both material profiles and comfortable hands.
- [ ] Implement equip, idle, charge/fire/recovery, inspection and optional reload/recharge, including interruptions.
- [ ] Implement declared shrouds, charms, salvage, skins, stickers and configurable effects without changing the baseline silently.
- [ ] Check native export, authoritative gameplay, multiplayer, optional mods, migration and equivalent-work performance.

[Read-only audit and concept/review source](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/apoco-shower-source-and-concept-study-v1.zip) · [Full weapon feature standard](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Completeness-Standard).

Original AoA identity/assets: Tslat and contributors. Concept: original project exploration generated with the built-in image tool. No native upgraded weapon acceptance is claimed.
