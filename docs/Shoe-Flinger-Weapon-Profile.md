# Shoe Flinger — original behavior and premium concept

**Pinned baseline: Minecraft 1.20.1 / AoA 3.7.1. Released-file research and concept exploration; no completed native upgrade.**

## What it is and does

Shoe Flinger is a deliberately absurd automatic gun that uses **Leather Boots as ammunition** and sends a tumbling boot projectile toward its target. Its graphite/silver body, green accents and small cyan muzzle detail distinguish it from a generic military weapon. Preserve the joke and the recognizable color/silhouette identity while improving the prop, animation and feedback.

On a successful shared gun-damage path, its custom living-target hook applies a scaled knockback request. If the target's feet slot is empty, it equips a **new default Leather Boots stack**. The hook does not copy the fired stack's dye, enchantments, name, damage or other metadata. It does not replace existing footwear in that inspected branch.

It also requests the La Chancla advancement for a server-player shooter when the target's health equals zero and the target cannot change dimensions. That exact predicate must not be generalized to every modded boss. Test custom bosses separately.

## Released inputs and important boundaries

| Property | Released evidence |
|---|---|
| Registry ID | `aoa3:shoe_flinger` |
| Base damage input | 6.0 |
| Durability input | 1,600 |
| Firing-delay input | 6 ticks |
| Stored recoil argument | 1.0; not a camera-angle measurement |
| Automatic | Inherited BaseGun behavior |
| Ammo identity | Leather Boots; named source comparison agrees with the released field/method shape |
| Projectile | ShoeShotEntity |
| Projectile lifespan argument | 120 |
| Projectile damage multiplier | 1.0, not launch speed |
| Projectile pierce argument | 0 |
| Gravity return | Approximately 0.13 |
| Knockback helper argument | 1.35 with three axis multipliers of 1; not a guaranteed displacement |
| Firing sound | Air-cannon sound, pitch base 0.85 plus randomized variation |

Final damage, actual firing cadence, resource exemptions/modifiers, armor interaction and knockback depend on shared helpers and runtime state. A valuable dyed, named or enchanted boot should not be assumed to come back unchanged. Any new “protect favorite equipment” option must be explicit and tested rather than claimed as original behavior.

## Acquisition

The shipped infusion recipe is **Gun Frame + Old Boot → Shoe Flinger**. This is an AoA infusion recipe, not a shaped crafting-grid layout. **Old Boot is the crafting ingredient; Leather Boots are the ammo.** Do not confuse those two items.

The archive also contains an acquisition advancement referencing Shoe Flinger. Recipe/advancement presence alone does not prove every required item is obtainable in the actual Survival pack.

## Original sprite and projectile

![Exact released weapon sprite, nearest-neighbor enlarged](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shoe-flinger-sprite-preview.png)

![Exact released shoe projectile texture](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shoe-flinger-projectile-preview.png)

The renderer uses this boot texture on a four-vertex, camera-facing spinning quad with a 0.5 scale operation. Its spin uses entity age plus partial tick, rather than incrementing a phase once per render call. The shown asset is **not an in-game flight or impact capture**. The upgraded boot can be a readable animated 3D prop, but collision, trajectory and gameplay effects need their own implementation and tests.

## Premium concept directions

![Shoe Flinger concept directions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shoe-flinger-concept-exploration-v2.png)

- **Sole Survivor:** a faithful original-mode presentation with a clear boot cradle, satisfying air-cannon shove, tumbling leather boot and playful but readable impact feedback.
- **Heelstorm:** proposed multi-boot assembly. Extra visible boots must match a real declared volley, resource budget and hit/target policy. A picture of several boots is not implemented multishot.
- **Bootlegger:** proposed returning spectral boot conversion. Define whether it returns an item, energy or only a visual. It must not both refund a boot and create free boots on targets without an intentional resource rule.

Inspection ideas include checking the loose lace, briefly presenting the worn sole, a cradle-latch check and a small embarrassed puff from a misbehaving fantasy core. Keep player movement/aim readability and cancellation safe. Charms, skins and custom trails remain optional progression features.

### Concept QA

[Version 1 remains available](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shoe-flinger-concept-exploration-v1.png). Its guard/grip ordering conflicted with the right-facing flared nozzle. Version 2 adds a rear leather-wrapped control grip behind the guard; the forward green assembly reads as a fantasy core/canister. This is still a concept interpretation, not a validated hand rig or feed mechanism. Prop proportions, actual reach, cradle-to-discharge presentation and moving-part clearances must be resolved in the model.

## Effect salvage and compatibility guardrails

The equipment-creating hook makes this weapon a particularly important material-conservation test. Transplanting it onto a cheap-ammo weapon could create an unintended boot factory. A recovery core must preserve its declared material cost or deliberately replace the item-producing outcome with an explicitly cosmetic effect.

Do not claim equipped boots are guaranteed loot: death drops, equipment rules and other mods need tests. Do not copy donor-specific advancement eligibility onto unrelated weapons by accident. Preserve the original mode's unusual behavior separately from optional safety/quality-of-life changes.

## Acceptance still open

- [ ] Native original flight, impact, ammo selection and equipment/advancement tests.
- [ ] Empty versus occupied feet slots; living versus nonliving targets; boss predicates.
- [ ] Named/dyed/enchanted/damaged ammo, creative/resource modifiers and item conservation.
- [ ] Editable geometry, meaningful loading presentation, comfortable hands and all animation clearances.
- [ ] Repeated shots, cancelled actions, duplicate packets, multiplayer ownership and saves.
- [ ] Bounded effects, reduced motion and equivalent-work performance.

[Released evidence](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/shoe-flinger-released-evidence.json) · [Audit tool and exact concept prompts](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/shoe-flinger-audit-tool-v1.zip) · [Pinned named-source comparison](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/content/item/weapon/gun/ShoeFlinger.java) · [Modular armory and effect salvage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage)

Original mod/art: Tslat and AoA contributors. New concept art is a proposed interpretation, not extracted native geometry.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
