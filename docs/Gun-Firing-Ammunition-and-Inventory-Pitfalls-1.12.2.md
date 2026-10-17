[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Historical gun inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2) · [Crafting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Crafting-and-Recipes)

# Historical gun firing, ammunition and inventory pitfalls

**Minecraft 1.12.2 / AoA 3.3.6.** This is a released-code operating reference and a set of independent inventory arithmetic tests. It is not a live-game test or a promise that every gun uses the same ammunition.

![Historical 16-bullet recipe, firing checks and a modeled split-stack consumption warning](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/gun-ammo-and-firing-1.12.2.webp)

## Craft ordinary Limonite Bullets

Place **one Limonite Ingot directly above one Gunpowder** in the shaped recipe. It produces **16 Limonite Bullets** in this release. The ingredients use exact item IDs, not a broad ingot tag. Do not copy the modern 48-bullet yield into the historical recipe.

[Open the exact historical recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Aitems%2Fmisc%2Fammo%2Flimonite_bullet).

## When the base gun will fire

The selected base right-click method checks these gates before its server ammunition call:

1. **Correct hand:** Brace enchantment level above zero selects the offhand; otherwise the main hand is selected. A click from the other hand fails this method.
2. **Blocking:** actively using an item while blocking returns PASS rather than firing through this branch.
3. **Sneaking offhand conflict:** when sneaking with the gun in the offhand, a main-hand BaseSniper or BaseStaff causes a failure return.
4. **Attack strength:** the player must have a cooled attack strength of at least 1.
5. **Server ammunition result:** a non-null projectile from findAndConsumeAmmo is required for the successful-use branch.

This describes the inspected base method. Subclasses, other mods and engine cooldown handling can introduce additional behavior. A FAIL or PASS result alone is not a diagnosis of missing ammunition.

## Which guns inherit the ordinary ammunition method?

Of the 78 direct gun registrations inspected, **45 inherit BaseGun.findAndConsumeAmmo**. That method requests Limonite Bullets through the shared inventory helper, with an amount of **1 + Greed enchantment level**. Its Creative helper bypass does not require the ordinary stock deduction.

The other **33 declare a different ammunition method**. An override may change the projectile, payment or both. Its presence does not by itself prove a different ammo item. The table below makes the method boundary explicit instead of assigning the Limonite rule to every weapon.

| Gun and portrait | Released ammunition-method owner |
|---|---|
| [Abominator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Abominator.name) | BaseGun · Limonite helper path |
| [Apoco Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ApocoAssaultRifle.name) | ApocoAssaultRifle · override, inspect separately |
| [Apoco Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ApocoRifle.name) | ApocoRifle · override, inspect separately |
| [Aqua Magnum](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AquaMagnum.name) | BaseGun · Limonite helper path |
| [Artifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Artifact.name) | BaseGun · Limonite helper path |
| [Baronator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Baronator.name) | Baronator · override, inspect separately |
| [Bayonette Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BayonetteRifle.name) | BaseGun · Limonite helper path |
| [Big Top](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BigTop.name) | BaseGun · Limonite helper path |
| [Blood Iron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BloodIron.name) | BloodIron · override, inspect separately |
| [Chain Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ChainWrecker.name) | BaseGun · Limonite helper path |
| [Chilli Chugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ChilliChugger.name) | ChilliChugger · override, inspect separately |
| [Clownershot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Clownershot.name) | Clownershot · override, inspect separately |
| [Construct](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Construct.name) | BaseGun · Limonite helper path |
| [Coral Clogger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoralClogger.name) | CoralClogger · override, inspect separately |
| [Core Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CoreRifle.name) | BaseGun · Limonite helper path |
| [Crystal Carver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.CrystalCarver.name) | BaseGun · Limonite helper path |
| [Cyclone](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Cyclone.name) | Cyclone · override, inspect separately |
| [Darkener](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Darkener.name) | BaseGun · Limonite helper path |
| [Dart Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DartGun.name) | DartGun · override, inspect separately |
| [Destruction Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DestructionRifle.name) | BaseGun · Limonite helper path |
| [Discharge Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DischargeRifle.name) | DischargeRifle · override, inspect separately |
| [Draco](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Draco.name) | BaseGun · Limonite helper path |
| [Dragilator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Dragilator.name) | Dragilator · override, inspect separately |
| [Dustometer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Dustometer.name) | Dustometer · override, inspect separately |
| [Echo Gull](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EchoGull.name) | BaseGun · Limonite helper path |
| [Electinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Electinator.name) | Electinator · override, inspect separately |
| [Flame Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FlameWrecker.name) | FlameWrecker · override, inspect separately |
| [Flaming Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FlamingFury.name) | FlamingFury · override, inspect separately |
| [Floro Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FloroRifle.name) | BaseGun · Limonite helper path |
| [Flower's Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FlowersFury.name) | BaseGun · Limonite helper path |
| [Frosticator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Frosticator.name) | Frosticator · override, inspect separately |
| [Gardener](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Gardener.name) | Gardener · override, inspect separately |
| [Gauge Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GaugeRifle.name) | GaugeRifle · override, inspect separately |
| [Germinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Germinator.name) | Germinator · override, inspect separately |
| [Golden Fury](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.GoldenFury.name) | GoldenFury · override, inspect separately |
| [Happy Haunter](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HappyHaunter.name) | BaseGun · Limonite helper path |
| [Haunter Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HaunterRifle.name) | BaseGun · Limonite helper path |
| [Heat Wave](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HeatWave.name) | HeatWave · override, inspect separately |
| [Hiver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Hiver.name) | BaseGun · Limonite helper path |
| [Hot Shot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HotShot.name) | HotShot · override, inspect separately |
| [Hunter's Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HuntersRifle.name) | BaseGun · Limonite helper path |
| [Iominator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Iominator.name) | Iominator · override, inspect separately |
| [Ion Revolver](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IonRevolver.name) | BaseGun · Limonite helper path |
| [Iro Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IroRifle.name) | BaseGun · Limonite helper path |
| [Krilinator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Krilinator.name) | BaseGun · Limonite helper path |
| [Light Iron](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LightIron.name) | LightIron · override, inspect separately |
| [Lunar Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarAssaultRifle.name) | BaseGun · Limonite helper path |
| [Mechanical Assault Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechanicalAssaultRifle.name) | BaseGun · Limonite helper path |
| [Megagun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Megagun.name) | BaseGun · Limonite helper path |
| [Miasma](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Miasma.name) | BaseGun · Limonite helper path |
| [Minigun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Minigun.name) | BaseGun · Limonite helper path |
| [Mint Magnum](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MintMagnum.name) | BaseGun · Limonite helper path |
| [MK](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MK.name) | BaseGun · Limonite helper path |
| [MK-Fung](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MKFung.name) | MKFung · override, inspect separately |
| [Nethenette Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethenetteRifle.name) | NethenetteRifle · override, inspect separately |
| [Nethengeic Slugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NethengeicSlugger.name) | NethengeicSlugger · override, inspect separately |
| [Overshot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Overshot.name) | Overshot · override, inspect separately |
| [Precasian Slugger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrecasianSlugger.name) | PrecasianSlugger · override, inspect separately |
| [Predator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Predator.name) | BaseGun · Limonite helper path |
| [Predigun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Predigun.name) | Predigun · override, inspect separately |
| [Pulsator](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Pulsator.name) | BaseGun · Limonite helper path |
| [Purity Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PurityRifle.name) | BaseGun · Limonite helper path |
| [Rocker Rifle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RockerRifle.name) | BaseGun · Limonite helper path |
| [Roulette](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Roulette.name) | BaseGun · Limonite helper path |
| [Shoe Flinger](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShoeFlinger.name) | ShoeFlinger · override, inspect separately |
| [Skullette](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Skullette.name) | BaseGun · Limonite helper path |
| [Skullifact](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Skullifact.name) | BaseGun · Limonite helper path |
| [Spectacle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Spectacle.name) | BaseGun · Limonite helper path |
| [Spine Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpineGun.name) | BaseGun · Limonite helper path |
| [Squad Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SquadGun.name) | BaseGun · Limonite helper path |
| [Stampede](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Stampede.name) | BaseGun · Limonite helper path |
| [Stormer](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Stormer.name) | BaseGun · Limonite helper path |
| [Sublimus](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Sublimus.name) | Sublimus · override, inspect separately |
| [Tiger Tommy](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.TigerTommy.name) | BaseGun · Limonite helper path |
| [Tommy](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Tommy.name) | BaseGun · Limonite helper path |
| [Vile Vanquisher](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VileVanquisher.name) | BaseGun · Limonite helper path |
| [Wart Gun](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WartGun.name) | WartGun · override, inspect separately |
| [Wrecker](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Wrecker.name) | BaseGun · Limonite helper path |

## Recoil and successful-use ordering

The selected base shot path applies the Control multiplier **1 − 0.15 × Control level** to getRecoilForShot. The offhand packet receives an additional **×2.5**. These are inspected arithmetic operations, not degrees, guaranteed camera movement or a recommendation to inject out-of-range enchantment levels.

The ammunition method runs before the projectile spawn attempt. When it returns a projectile, the base method calls spawnEntity, then records item use, applies the firing-delay cooldown, damages the gun by 1 and handles sound/recoil. The spawn method's boolean result is discarded by this caller.

Therefore a rejected spawn is a **target-build regression case**: the inspected caller does not establish a rollback of already-consumed ammunition or subsequent durability/cooldown changes. Do not batch expensive shots while diagnosing a spawn failure.

## Split-stack accounting: a real source-level warning

For a requested amount greater than one, the released shared helper collects matching stack references and totals foundCount. It checks that the collected count reaches the request. During consumption, however, it repeatedly computes the minimum of the current stack count, the **original requested amount**, and foundCount. It decreases foundCount, but does not decrease a separate remaining-request amount or stop when that request has been paid.

An independent model of that exact loop gives:

| Starting matching stacks | Requested amount | Modeled removal | Correct exact-payment target |
|---|---:|---:|---:|
| 2 and 2, separate main-inventory stacks | 3 | 4 | 3 |
| 1 and 5, separate main-inventory stacks | 3 | 4 | 3 |
| 3 and 5, separate main-inventory stacks | 3 | 3 | 3 |

The third case stops collecting after the first sufficient stack, so it does not demonstrate the error. This is why a simple test with one large stack can miss the boundary problem.

The helper also examines the main-hand stack before iterating main inventory. In the modeled multi-item path, a matching selected stack can be added a second time as the same object. A single selected matching item with a request of 2 can satisfy the counted total through duplication while only one physical item is removed. This is a bookkeeping test case, not a claim that every weapon setup exposes the same behavior.

The included **201 models** cover matching main-inventory objects, requests above one, non-Creative mode and consumption enabled. They are independent Python models of the inspected algorithm, not executed Minecraft sessions. The amount-one path, offhand/armor search and custom mod inventories need their own runtime tests.

### Practical caution

When testing a gun with a multi-item cost, start with a small known amount, compare the physical inventory before and after each attempt, and avoid relying on several small matching stacks. Keep valuable reserves out of the tested inventory while diagnosing a discrepancy. A pack may already patch this helper, so verify the actual target build before reporting the behavior as reproduced there.

## Matching is stricter than the display name

The inspected equality helper compares item identity, damageability, metadata for non-damageable items, and tag presence/content. A renamed or otherwise tagged stack is not automatically equivalent to the untagged template used by the base ammo call. This path does not scan arbitrary nested backpacks.

## Restoration and performance test checklist

- Deduplicate physical stack references before counting them. Test the selected main-hand stack appearing again in main inventory.
- Check sufficient unique stock before consuming, then maintain a remaining amount and stop at zero. Test exact payment, split stacks and insufficient stock without partial loss.
- Separate item consumption from projectile acceptance; define and test failure handling rather than assuming the spawn attempt succeeded.
- Preserve Creative behavior, item metadata/tags, hand selection, cooldowns and custom gun overrides when changing the shared helper.
- The inspected base impact method contains a System.out.println(target) call. Treat uncontrolled per-impact console output as a profiling candidate; removing or gating it is not a measured FPS improvement by this documentation pass.
- Recheck Control/Brace behavior, server/client agreement, save/reload and modded inventories. Do not claim no regression from arithmetic unit models alone.

[Released method evidence, 78 method-owner resolutions, recipe and 201 inventory models](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gun-firing-evidence-1.12.2.json) · [Source icon provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/gun-firing-art-evidence-1.12.2.json).
