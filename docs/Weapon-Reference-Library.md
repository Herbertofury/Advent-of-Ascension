![The Ascension Armory](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-upgrade-banner.svg)

# Weapon reference library

**Primary-source research checked 2026-10-15.** These are study targets for craft and implementation, not claims that their assets may be copied or that all packs work together. Download exact compatible releases from their official pages. Keep author credits and code/asset licenses separate.

[Design contract](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Build checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog)

## AoA originals to preserve during an overhaul

[Buy historical weapons: 29 trader offers, input quantities and cannon upgrades](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Buying-Weapons-and-Trader-Upgrades-1.12.2)

[Acquisition atlas for all 412 historical weapons](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Weapon-Acquisition-1.12.2): exact recipes, direct loot-table references, trader candidates and clearly marked unresolved routes.

Before redesigning a weapon, compare its original appearance and release-specific resource behavior. These illustrated **1.12.2 / AoA 3.3.6** tables now place a checked source-model portrait beside every listed weapon name:

- [36 swords: material and attack inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sword-Materials-and-Attack-Inputs-1.12.2)
- [29 greatblades: inputs and variable damage branches](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Greatblade-Inputs-and-Damage-Branches-1.12.2)
- [5 mauls: reach and knockback inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Maul-Inputs-Reach-and-Knockback-1.12.2)
- [78 guns: constructor inputs and recoil](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Gun-Constructor-Inputs-and-Recoil-1.12.2)
- [17 shotguns: pellets, spread and special effects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Shotgun-Pellets-Spread-and-Special-Effects-1.12.2)
- [27 snipers: stance, scopes and inputs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sniper-Stance-Scopes-and-Inputs-1.12.2)
- [50 cannons: ammunition and armor scaling](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Cannon-Ammunition-and-Armor-Scaling-1.12.2)
- [33 bows: draw timing and ammunition](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bow-Draw-Timing-and-Ammunition-1.12.2)
- [9 archerguns: trajectories and effects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Archergun-Ammunition-and-Special-Effects-1.12.2)
- [7 throwables: payment, impacts and Runic Bombs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Throwable-Weapons-Impacts-and-Runic-Bombs-1.12.2)
- [8 vulcanes: stored revenge targets and effects](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-Revenge-Targets-and-Effects-1.12.2)
- [56 blasters: Energy, timing and Spark exceptions](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blaster-Energy-Timing-and-Spark-Exceptions-1.12.2)
- [57 staves: rune costs and hand safety](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Runes-Casting-and-Hand-Safety-1.12.2), with [29 custom casting requirements](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Staff-Casting-Requirements-and-Troubleshooting-1.12.2)

These 412 portraits preserve existing source-model atlas pixels. They cover all 412 direct weapon constructors in the checked 1.12.2 WeaponRegister method, with [exact identity and family evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-weapon-census-1.12.2.json). This does not certify every effect, runtime-injected addon item, new animated remodel or in-game renderer. Keep version differences explicit and retain optional reloading rather than imposing magazines on rune/resource weapons.

## Owner-selected quality anchors

| Project | What the AoA team should study | Official reference |
|---|---|---|
| Timeless and Classics Zero | Complete handling/animation pipeline, gunpack structure, third-person presentation and LOD | [TaCZ](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero) · [source](https://github.com/MCModderAnchor/TACZ) |
| Create Armorer — Koei | Coherent mechanical art direction and survival integration; adapt the principle to each AoA realm | [Create Armorer](https://www.curseforge.com/minecraft/customization/tacz-create-armorer-koei) |
| Helldivers: Escalation of freedom | Distinct science-fiction weapon families and energy/arc handling; check current dependency and hotfix notes | [Helldivers gunpack](https://www.curseforge.com/minecraft/customization/tacz-helldivers-escalation-of-freedom) |

The official TaCZ page lists Forge 1.20.1 1.1.8-hotfix2 at this research snapshot. Select a compatible gunpack release rather than assuming every pack supports the newest runtime. The Helldivers listing explicitly flags one October 3 file as faulty and provides a later emergency hotfix; follow its current file notes.

## Additional high-value showcases

| Reference | Specific design lesson | Scope |
|---|---|---|
| [Immersive Armorer — Koei](https://www.curseforge.com/minecraft/customization/tacz-immersive-armorer-koei) | Industrial material language and mechanical identity | TaCZ gunpack |
| [Ars Armorer — Koei](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei) | Magical weapon styling as an alternative to generic military reskins | TaCZ gunpack |
| [EMX-Arms](https://www.curseforge.com/minecraft/customization/tacz-emx-arms-gunpack) | Additional gunpack art/handling comparison; inspect actual assets and footage before adopting techniques | TaCZ gunpack |
| [Vic's Point Blank](https://www.curseforge.com/minecraft/mc-mods/vics-point-blank) | Model polish, reload/inspect/draw presentation and custom content workflow | Separate Java weapon runtime |
| [Point Blank official extension template](https://www.curseforge.com/minecraft/customization/point-blank-official-extension-template-pack) | How another ecosystem structures authoring and extensibility | Template/reference |
| [Superb Warfare](https://www.curseforge.com/minecraft/mc-mods/superb-warfare) | Heavy weapon weight, effects and combat presentation | Separate Java mod |
| [Aplok Guns](https://www.curseforge.com/minecraft-bedrock/addons/aplok-guns) | Readable Minecraft-compatible styling, modular attachments and reload variety | Bedrock reference, not a Java dependency |
| [ActualGuns 3D](https://pixelpoly.co/store) | Premium Bedrock weapon presentation and animation showcase | Bedrock reference; [creator showcase](https://www.youtube.com/watch?v=JXV463e3ksw) |

These are qualitative study selections, not a measured ranking or a claim that every animation has been watched. Inspect gameplay capture and source/tooling before selecting a technique.

## Magic-through-firearms references

These three owner-selected references complement one another: a visual gunpack and two spell-integration addons. They are references to evaluate, not mandatory AoA dependencies or proof of existing AoA compatibility.

- **[Ars Armorer — Koei](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei):** retain as the magical art-direction reference. Study how a fantasy identity carries into weapon forms, materials and handling.
- **[ArsArms](https://www.curseforge.com/minecraft/mc-mods/arsarms)** · [official source](https://github.com/mumu17-git/ArsArms): integrates Ars Nouveau spells with TaCZ guns. The CurseForge description uses Reactive enchantment and stored mana. It lists Forge 1.20.1, version 3.0.4 and MIT licensing at this snapshot. Study event integration, mana accounting and how spell firing coexists with ordinary weapon modes.
- **[IronsArms](https://www.curseforge.com/minecraft/mc-mods/ironsarms)** · [official source](https://github.com/mumu17-git/IronsArms): integrates Iron's Spells 'n Spellbooks with TaCZ, including Arcane Anvil spell imbuing and stored mana. The listing identifies Forge 1.20.1, version 3.0.6 and MIT licensing. Study spell selection, persistent weapon state and server-authoritative resource consumption.

**Version warning:** ArsArms' current CurseForge description and repository README describe different workflows (gun/Self glyph versus ammo box/Touch glyph). Pin a release and inspect its matching code before documenting player instructions. Do not combine those workflows into an invented recipe.

**AoA application, proposed:** preserve AoA's own resource costs, projectile identities, status effects, skills and cooldowns behind an optional weapon-effect adapter. Test that one shot cannot double-cast, charge resources twice, bypass progression or lose state during reload cancellation. Compare addon hooks before adding another mixin or per-tick inventory scan. New external spell systems should be explicit optional integrations, not a silent rewrite of original AoA weapons.

## Authoring and integration toolkit

- [TaCZ gunpack documentation](https://tacwiki.mcma.club/) and [first gun guide](https://tacwiki.mcma.club/gunpack/first_gun/): separate gameplay data from display assets and presentation configuration.
- [Positioning](https://tacwiki.mcma.club/gunpack/gun_positioning/): account for aimed, idle, ground, fixed and third-person views.
- [Animation standards](https://tacwiki.mcma.club/gunpack/animation/): follow supported groups and animation names; validate export conventions rather than assuming arbitrary clips work.
- [Hand positioning](https://tacwiki.mcma.club/gunpack/hand_pos/) and [LOD](https://tacwiki.mcma.club/gunpack/lod/): use the established authoring pipeline before inventing a replacement.
- [Exception API Extension](https://www.curseforge.com/minecraft/mc-mods/exception-api-extension): evaluate extended Lua/animation state-machine features only for a concrete requirement. An extension listing a loader/version is not proof that the entire AoA/TaCZ stack supports it.
- [Bedrock animation overview](https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationsoverview?view=minecraft-bedrock-stable): useful cross-platform animation/controller concepts; not a drop-in Java renderer.

## Rights and contribution rules

TaCZ code and visual assets have different licenses (GPL-3.0 code; CC BY-NC-ND 4.0 assets on its project page). Point Blank lists All Rights Reserved. Superb Warfare separates GPL code from reserved assets. Aplok lists CC BY-NC-ND 4.0. Check the exact file and license before reuse, modification or redistribution; gunpack permissions do not automatically grant rights to the franchise they depict.

Prefer original AoA-faithful models and animations, properly licensed dependencies, and upstream contributions for reusable tooling fixes. Record provenance per asset. Do not bundle third-party models, sounds, textures or extracted game assets merely because they are linked here.

## Ars Armorer: direct follow-up study

The owner-selected [four-image gallery](https://www.curseforge.com/minecraft/customization/tacz-ars-armorer-koei/gallery) has now been inspected directly, alongside all eight weapon display/animation definitions and 36 attachment definitions in the pinned pack. Read the [detailed findings and AoA application checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Ars-Armorer-Direct-Study): semantic effect/delivery/modifier/capacity slots, rechargeable reserve handling, unconventional magical silhouettes, distinct blade groups and LOD authoring. Static inspection does not certify runtime behavior.

The [ArsArms and IronsArms source-and-release study](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Spell-Adapter-Source-and-Release-Study) now compares pinned GitHub source with the actual published JARs (17 released classes total), including impact events, stored-resource charging and workbench integration. It records preventive AoA QA requirements and keeps runtime validation open.


## Mastercraft and Mythic animation collections

[Main cross-game playlist](https://www.youtube.com/playlist?list=PL9faHbneiK_GdGNsksKaYo8Vm2rIcqpDJ) · [Organized reference index](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mastercraft-Playlist-Index): 63 visible playlist entries, 62 unique videos, grouped by study purpose. Link metadata is verified; visual sequence review is tracked separately.

Owner-selected major design references: the full BO6 and BO7 Mastercraft collections and the supplied COD Mobile Mythic showcase, plus other playful COD weapons. Study distinctive inspections, transformation reveals, reactive materials, reload presentation, tracers and defeat effects.

- [BO6 Mastercraft inspections](https://www.youtube.com/watch?v=qJkyqb7ycjo)
- [BO7 Mastercraft weapons: matching-title showcase](https://www.youtube.com/watch?v=9UCxE7kgzvE)
- [COD Mobile Mythic inspections, reloads and kill effects](https://www.youtube.com/watch?v=pdK11eIggOI)
- [Verified official examples, AoA storyboard proposals and review ledger](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mastercraft-and-Mythic-Animation-References)

Video pages are verified; detailed frame review remains pending because playback buffered. Do not equate a dated showcase title with a permanently complete catalogue or copy protected game assets.
