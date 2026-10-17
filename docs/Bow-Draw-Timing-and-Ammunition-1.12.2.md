[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Historical weapon references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2) · [Crafting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes)

# Historical bows: draw timing and ammunition

**Minecraft 1.12.2 / AoA 3.3.6.** This guide covers 33 direct bow registrations, eight selected base methods, fifteen subclass/resource methods and 671 independent draw models. It is not a live accuracy, DPS or server-timing benchmark.

![Four historical bow source-model portraits and modeled full-charge ticks](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-inputs-1.12.2.webp)

## Craft ordinary Holly Arrows

Use a vertical shaped recipe: **Iron Nugget above Stick above Holly Top Petals**. The released recipe produces **4 Holly Arrows**. [Open the illustrated exact recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fammo%2Fholly_arrow).

The base ammo predicate accepts items in the **HollyArrow class family**. This is not the same as accepting every vanilla arrow. The inspected archive includes PopShot, SpectralHollyArrow and TippedHollyArrow subclasses; their presence alone does not establish identical effects, acquisition or crafting.

The base search checks offhand first, then main hand, then inventory slots. A different eligible arrow in your offhand can therefore be selected before one elsewhere in the inventory. It does not inspect arbitrary nested modded storage.

## How draw timing is calculated

The selected release path multiplies elapsed use ticks by the bow's draw-speed multiplier, using float arithmetic, then converts the result to an integer charge. Forge's onArrowLoose hook can change or cancel that charge. A negative hook result returns without firing.

For an unchanged hook, the local velocity calculation is:

1. Divide integer charge by 20.
2. Calculate `(f² + 2f) / 3`.
3. Clamp the result to at most 1.
4. Require a value of at least 0.1 for the selected firing branch.

A larger draw multiplier reaches the same modeled charge in fewer elapsed ticks. The values below simulate the released float32 operations and integer conversion for ticks 0–60. They do not include event overrides, input latency or server lag, and they are not an exact real-time promise.

| Draw multiplier | Earliest modeled eligible release · ticks | First modeled full charge · ticks |
|---:|---:|---:|
| 0.75 | 4 | 27 |
| 0.8 | 4 | 25 |
| 0.85 | 4 | 24 |
| 0.9 | 4 | 23 |
| 1 | 3 | 20 |
| 1.1 | 3 | 19 |
| 1.2 | 3 | 17 |
| 1.3 | 3 | 16 |
| 1.5 | 2 | 14 |
| 2 | 2 | 10 |
| 3 | 1 | 7 |

## Compare the 33 bow entries

Each name opens its own source-model portrait and lazy **1.12.2 bow inputs · draw timing and ammo** panel. The historical bow family filter lists these entries together. Damage is a constructor input, not final health removed.

| Bow and portrait | Damage input | Draw multiplier | Durability | Modeled full charge · ticks |
|---|---:|---:|---:|---:|
| [Alacrity Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AlacrityBow.name) | 9.5 | 1 | 600 | 20 |
| [Ancient Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AncientBow.name) | 22 | 1 | 1510 | 20 |
| [Atlantic Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AtlanticBow.name) | 24.5 | 0.9 | 1480 | 23 |
| [Baron Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronBow.name) | 12 | 1.1 | 3000 | 19 |
| [Boreic Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreicBow.name) | 14 | 1.3 | 1190 | 16 |
| [Daybreaker Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DaybreakerBow.name) | 17.5 | 1 | 1180 | 20 |
| [Deep Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DeepBow.name) | 15.5 | 0.85 | 700 | 24 |
| [Explosive Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveBow.name) | 17 | 0.8 | 900 | 25 |
| [Haunted Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HauntedBow.name) | 17 | 1 | 920 | 20 |
| [Ice Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IceBow.name) | 8.5 | 1 | 580 | 20 |
| [Infernal Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.InfernalBow.name) | 11.5 | 1 | 710 | 20 |
| [Justice Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.JusticeBow.name) | 14.5 | 1 | 920 | 20 |
| [Lunar Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarBow.name) | 17.5 | 1 | 900 | 20 |
| [Mecha Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechaBow.name) | 20.5 | 0.75 | 930 | 27 |
| [Nightmare Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareBow.name) | 13.5 | 1 | 890 | 20 |
| [Poison Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonBow.name) | 15 | 1 | 950 | 20 |
| [Predatious Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PredatiousBow.name) | 14 | 0.9 | 690 | 23 |
| [Primordial Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrimordialBow.name) | 18.5 | 1 | 1350 | 20 |
| [Rosidian Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianBow.name) | 15.5 | 1 | 900 | 20 |
| [Runic Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicBow.name) | 20.5 | 1 | 1320 | 20 |
| [Screamer Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ScreamerBow.name) | 12 | 1 | 665 | 20 |
| [Shyregem Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShyregemBow.name) | 7.5 | 3 | 1500 | 7 |
| [Skeletal Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalBow.name) | 8.5 | 1.5 | 720 | 14 |
| [Skydriver Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkydriverBow.name) | 14.5 | 1 | 850 | 20 |
| [Slingshot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Slingshot.name) | 17 | 1 | 1200 | 20 |
| [Soulfire Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SoulfireBow.name) | 23.5 | 0.75 | 1100 | 27 |
| [Spectral Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpectralBow.name) | 12 | 1.3 | 900 | 16 |
| [Speed Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpeedBow.name) | 8 | 2 | 930 | 10 |
| [Sunshine Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SunshineBow.name) | 27 | 0.8 | 1530 | 25 |
| [Toxin Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ToxinBow.name) | 14 | 0.85 | 900 | 24 |
| [Void Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoidBow.name) | 9 | 1.2 | 600 | 17 |
| [Weaken Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakenBow.name) | 12.5 | 1 | 700 | 20 |
| [Wither Bow](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherBow.name) | 13.5 | 1 | 835 | 20 |

## Ammo, durability and enchantments in the base release path

The selected release method treats Creative mode or Infinity above zero as infiniteAmmo. If its ammo result is empty while that flag is true, it constructs a fallback Holly Arrow stack. This describes the release callback; inherited use-start behavior and other mods remain separate checks.

The base makeArrow method creates the arrow, applies launch and enchantment settings, damages the bow by one, and consumes one ammo item when consumeAmmo is true for a player. This occurs before the caller's world spawn attempt. The caller does not establish a rollback if the world rejects the projectile.

At full local velocity, it marks the arrow critical. Its Power adjustment adds **1.5 × Power level + 1** to the created arrow's damage field when Power is positive. That field adjustment is not measured final impact damage. Punch, Flame, pickup restrictions and subclass paths remain separate behavior; do not import a different Minecraft version's formula without checking.

## Important bow-specific exceptions

| Bow | Checked behavior | Practical implication / remaining check |
|---|---|---|
| Spectral Bow | Its ammo getter constructs a Holly Arrow stack and makeArrow passes consumeAmmo=false to the base method. | It does not use the ordinary inventory deduction in that path, but the base durability operation remains. |
| Slingshot | Accepts Pop Shot or vanilla Flint and constructs EntityPopShot through its own makeArrow method. | Use the correct ammo; its separate damage field and projectile path should not be silently treated as the ordinary bow implementation. |
| Daybreaker Bow | When rotationPitch is strictly below −70, it attempts eight offset copy arrows in addition to returning the central arrow. | The condition is an upward pitch check. Spawn attempts are not nine guaranteed hits, and copied arrows have DISALLOWED pickup status. |
| Nightmare Bow | Attempts two sideways copy arrows and returns the central arrow. | Copied arrows have CREATIVE_ONLY pickup status; do not assume every projectile can replenish Survival ammo. |
| Soulfire Bow | Calls the Soul resource helper with requested amount 50; a successful result marks the arrow glowing. A glowing entity-impact hook can heal a living, non-dead shooter by 8 and then clears the glow. | Resource buffs, disabled resources and Creative exemptions can change actual payment. Block impact clears the glow instead of granting that entity-impact heal. |

The Daybreaker and Nightmare copy methods run after the base makeArrow call has handled consumption. Test the **last specialized arrow in a stack** and its copied metadata explicitly; do not assume that a depleted input stack still supplies all the original arrow information.

Soulfire's resource helper returns true without ordinary deduction when resources are disabled, and has a Creative exemption for this non-Rage resource. Otherwise it applies resource-fortitude modifiers, checks stock and subtracts the adjusted cost. “Requested 50” is therefore more accurate than promising an unconditional deduction of exactly 50 in every configuration.

## Safe small-test checklist

- Confirm this exact release and the intended ammo class before crafting a large supply.
- Check the offhand for an eligible arrow that could take priority.
- Treat the timing table as a baseline with an unchanged Forge hook; compare actual behavior in the target pack.
- Test ordinary and last-item ammo stacks, Infinity, Creative, specialized arrows and subclass bows separately.
- Check rejected spawns, durability and copied-arrow pickup behavior together.
- For a remodel, preserve drawing, resource payment and special arrow behavior. A visual upgrade should not quietly substitute modern formulas or a mandatory reload system.

[Released methods, 33 constructors, arrow class relationships, recipe and 671 draw models](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-bow-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bow-art-evidence-1.12.2.json).
