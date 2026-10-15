![The Ascension Armory](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/weapon-upgrade-banner.svg)

# Weapon reference library

**Primary-source research checked 2026-10-15.** These are study targets for craft and implementation, not claims that their assets may be copied or that all packs work together. Download exact compatible releases from their official pages. Keep author credits and code/asset licenses separate.

[Design contract](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul) · [Build checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Upgrade-Backlog)

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
