# Sludge Sniper · slowing, poisoning Metal Slug weapon

**AoA 3.7.1 / Minecraft 1.20.1 · source profile and partial concept study · native upgrade unaccepted.**

## What the original does

Sludge Sniper is a **Metal Slug BaseSniper** with a special living-target impact hook. The released class applies two 100-tick effect builders: **Slowness II** and **Poison I**. The bundled EffectsLib 1.7 starts its level at 1 and subtracts one when creating the Minecraft amplifier, so `.level(2)` means level II, not III. The official named source corroborates both effect names.

At 20 TPS the configured duration is five seconds. Immunities, other effects, damage rules and runtime conditions can affect the outcome; this source inspection is not a successful native hit test. The hook gates on LivingEntity. It does not establish poisonous terrain, pools, explosions or a new liquid-ammunition system.

| Registered input | Value |
|---|---:|
| Damage | 37 |
| Durability | 350 |
| Firing delay | 87 ticks, nominally 4.35 seconds at 20 TPS |
| Recoil modifier | Approximately 0.05 |
| Ammunition | Metal Slug |
| Scope | SCOPE_2 |
| Sound | Metallic sniper, long report |

Constructor inputs are not guaranteed final damage or measured animation recoil. The subclass has no custom projectile-creation override; original flight and impact recordings remain required.

## Preserve the original identity

![Actual released Sludge Sniper sprite](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sludge-sniper-original-preview.png)

Keep the broad horizontal body, dark forest-green and olive mottling, charcoal grip, gray structure and paired lime accents. Its toxic and botanical recipe ingredients support that visual direction. They do not prove a particular creator, manufacturing location or origin dimension. No unsupported Vox Ponds origin claim is added here.

## Crafting walkthrough

![Seven-slot Sludge Sniper infusion recipe](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sludge-sniper-infusion.webp)

Use **Sniper Frame** as the base input and supply seven ingredients: Toxic Lump twice, Sticky Slime, Lily Pad, an iron-ingot tag match, a gunpowder tag match and a jade-gem tag match. The two Toxic Lump ingredients occupy two slots; do not collapse them into one ingredient slot. The diagram's middle grid is order-independent and is a reconstructed guide, not an in-game capture.

The exact bundled recipe is preserved in the evidence file. Tag icons show examples; installed datapacks can change which items match. The Lily Pad is given an illustrative green display tint. Gunpowder uses the previously documented vanilla icon atlas rather than a newly captured 1.20.1 item render.

## Premium concept and its limits

![Sludge Sniper proposed premium design and cosmetic studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/sludge-sniper-concept-v1.png)

Mossy dark ceramic panels, pitted metal, botanical relief and sealed green channels reinterpret the original color regions. The painted description of a swamp/industrial design is **new art direction, not canonical lore**. Preserve the original sprite alongside this proposal.

The muzzle vapor, green tracer and mist at the stone test block are cosmetic proposals. They do not turn Metal Slugs into a new resource or give block hits the living-target debuffs. The small side-view caption “silhouette match” is an artistic goal, not a geometric validation result. The oversized optic housing, sight line, grip clearance and separation of the trigger/guard still need explicit model QA.

This board is partial concept coverage. It is not a UV texture, rig, native gunpack or proof that the full feature set is finished.

## Complete customization and animation plan

- **Materials:** original-fit and premium modes; readable green/olive grouping, restrained wetness, weathering and clean normals/UVs.
- **Handling:** a usable SCOPE_2 sight line, generous hand space, legible readiness and recoil recovery.
- **Modules:** compact optic shroud, stabilized fore-end, swamp-reed cosmetic muzzle sleeve and a separately specified fantasy spreading-shot conversion. Gameplay-changing modules must declare projectile count, damage, effects, resource cost and authority rules.
- **Animation:** equip, idle, aim, confirmed fire, recoil recovery, optional reload, inspection, swaps and interruption recovery in first and third person. A sealed-channel inspect can reveal a brief green pulse without obscuring the sight or implying an unimplemented reload resource.
- **Effects:** original-versus-upgrade flight/impact recordings; selectable muzzle, tracer, armor/entity/stone/fluid impacts, bounded decals and confirmed-kill cosmetic finishers. No persistent toxic pools are assumed.
- **Customization:** earned charms, skins, emblems, static/animated/glowing stickers, configurable tracers and death effects.
- **Salvage:** dismantle and transfer eligible effects with resource conservation, full-inventory returns, permissions and save migration.
- **Compatibility/performance:** server-side effects remain authoritative; cache presentation settings, avoid rescanning and bound emissions/decals. Test multiplayer, immune targets, simultaneous effects, TaCZ attachments/turrets and relevant magic/progression adapters.

## Acceptance checklist

- [ ] Original native projectile, hit, scope, sound and effect-duration evidence
- [ ] All module, impact, decal, finisher and animation concept boards
- [ ] Faithful model, two finished texture modes and collision/hand-fit checks
- [ ] Native effect levels, duration, immunities, stacking and resource accounting
- [ ] Networking, persistence, compatibility and equivalent-work performance

## Sources and audit

[Released evidence and exact recipe](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/sludge-sniper-released-evidence.json) · [Official named source, pinned 1.20 branch revision](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/content/item/weapon/sniper/SludgeSniper.java) · [Weapon overhaul](Weapon-Overhaul)

The release JAR, three relevant weapon classes and bundled EffectsLib class are hash-recorded. The named source file's last change is the official “Update to 3.7.1” commit. Source facts and original assets are credited to the AoA authors; generated art and integration proposals are separate.
