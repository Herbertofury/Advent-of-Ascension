# Weapon ammunition · Minecraft 1.20.1

**Released AoA 3.7.1: 172 conventional weapon IDs, 13 declared ammo identities.** [Open the illustrated Ammunition Desk](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html) to search weapons, filter by supplies or family and open the original item/recipe references.

This is an inheritance-aware `getAmmoItem` audit, not a net-consumption or gameplay test. It resolves the first method implementation along each weapon's actual recorded class chain. The 40 relevant methods use simple constant-return paths in this pinned release; the audit rejects unrecognized instruction shapes instead of guessing.

## What to bring

| Ammo identity | Weapon IDs using this base identity | Browse |
|---|---:|---|
| Limonite Bullet | 63 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Alimonite_bullet) |
| Metal Slug | 34 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Ametal_slug) |
| Cannonball | 31 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Acannonball) |
| Spreadshot | 16 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Aspreadshot) |
| Grenade | 12 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Agrenade) |
| Discharge Capsule | 6 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Adischarge_capsule) |
| Balloon | 2 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Aballoon) |
| Cobblestone | 2 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=minecraft%3Acobblestone) |
| Wheat Seeds | 2 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=minecraft%3Awheat_seeds) |
| Chilli | 1 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=aoa3%3Achilli) |
| Carrot | 1 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=minecraft%3Acarrot) |
| Leather Boots | 1 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=minecraft%3Aleather_boots) |
| Nether Wart | 1 | [Show weapons](https://herbertofury.github.io/Advent-of-Ascension/weapon-ammo-explorer.html?ammo=minecraft%3Anether_wart) |

## The exceptions that are easy to miss

- **Dart Gun and Gardener:** Wheat Seeds, not an inferred conventional bullet based on the gun family.
- **Jack Rocker and Jack Funger:** Cobblestone.
- **Shoe Flinger:** Leather Boots. Old Boot is the infusion ingredient, not this method's ammo identity.
- **Carrot Cannon, Chilli Chugger and Wart Gun:** Carrot, Chilli and Nether Wart respectively.
- **Discharge family variants:** the audited overrides use Discharge Capsules, including the Discharge Shotgun rather than the shared shotgun Spreadshot default.
- **Iominator:** its base ammo is Limonite Bullet, while its projectile is ToxicBulletEntity. Ammo identity and projectile/effect identity are different contracts.

## What this does not guarantee

The result does not establish a fixed one-item-per-shot cost. Creative rules, inventory selection, pouches, enchantments, exemptions, multishot and other installed mods can affect actual spending. It does not prove ammunition is obtainable in every Survival pack or that an equipped item will be preserved/recovered. The 56 blaster IDs are excluded from this item-ammo table; inspect their resource contracts separately.

For example, Shoe Flinger's equipment-creating effect needs material-conservation tests before transplantation to another weapon. Using a cheap ammo identity with a donor's item-producing effect can create an unintended item factory.

## Evidence and reproduction

The AoA item IDs are resolved from released registry assignments; Grenade resolves through the weapon registry. Five vanilla fields are paired with explicitly recorded named counterparts from the official pinned AoA source snapshot, with source hashes retained. This distinction is visible in the evidence instead of hiding obfuscated fields behind an unverified guess.

An independent reconstruction reproduced all 172 records and all 40 method findings. The illustrated browser embeds the small resolved dataset, renders 24 cards per batch and reuses existing release-specific source-model images. It does not scan a player's game or account.

- [Exact resolved records, methods, class hashes and named-source comparisons](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-ammo-resolution-1.20.1.json)
- [Original reproduction and browser-test tools](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-ammo-audit-tool-v1.zip)
- [Underlying class-chain map](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Implementation-Map)
- [Upgrade/salvage state ownership](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage)

Original mod, names and images: Tslat and AoA contributors; vanilla identities belong to Minecraft/Mojang. No native compatibility, damage or performance acceptance is implied.


## Lighter reference images

The browser now uses page-sized thumbnail atlases at the same 96×96 display size. The default first 24 cards need a 102,234-byte atlas instead of seven full source sheets totaling 1,366,010 bytes: about 92.5% fewer image-asset bytes for that view. All full-size originals remain available through item links. This is a measured file-size comparison, not a measured startup-time or Minecraft-FPS claim.

[Thumbnail provenance and size receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-ammo-thumbnail-proof.json) · [Updated audit, atlas builder and browser tests](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/weapon-ammo-audit-tool-v2.zip)
