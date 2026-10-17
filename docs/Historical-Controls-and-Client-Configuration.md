# Historical controls and client configuration

Use this comparison when moving between the four pinned documentation releases. It is a field-by-field reference, **not a drop-in config converter**. Saved keybindings, modpacks and runtime hooks can change what a player actually sees.

![Release-specific HUD corner and halo defaults](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/historical-hud-config-migration.webp)

## The changes most likely to trip you up

- **Bottom resource-HUD corners are declared in the checked 1.12.2 and 1.16.5 releases, but absent from the 1.20.1 and 1.21.1 enums.** Do not carry Bottom_Left or Bottom_Right into a release that does not declare them.
- **Halo enum spelling changed.** The checked 1.16.5 and 1.20.1 artifacts use Donator, Super_Donator and Wiki_Editor. The 1.21.1 artifact uses DONATOR, SUPER_DONATOR and WIKI_EDITOR.
- **Section names changed.** The two intermediate client configs use General Settings and Fun Options. The checked 1.21.1 client config uses general_settings and fun_options. Preserve the generated TOML structure for each version.
- **The 1.12.2 main config mixes presentation and gameplay.** Do not treat the whole legacy file as a harmless client-appearance preset.
- **screenShake appears in the checked 1.21.1 client definitions, not in the two intermediate ClientConfig classes.** Absence of this setting does not mean that a release never produces camera motion.

## Default controls across releases

| Action | 1.12.2 / 3.3.6 | 1.16.5 / 3.6.11 | 1.20.1 / 3.7.1 | 1.21.1 / 3.7.16.1 |
|---|---|---|---|---|
| Resource HUD | O | O | O | O |
| Skill HUD | Unbound | Unbound | Unbound | Unbound |
| Advent GUI | Delete | Delete | Delete | Delete |
| Creature statistics toggle | Unbound | Not in this four-key registration | Not in this four-key registration | Not in this four-key registration |
| Ability action | Not in this four-key registration | V | V | V |

The older client uses LWJGL2 Keyboard codes: O=24, Delete=211 and unbound=0. The later clients use GLFW codes: O=79, Delete=261, V=86 and unbound=−1. These are different encodings of key defaults, not evidence that the user must press a different letter. Do not copy numeric key codes between the systems.

The absence statements above apply only to the inspected AoA registration methods. They do not exclude controls supplied by another mod.

## Presentation defaults

The 1.12.2 column covers **13 selected presentation fields**, not every field or nested category in MainConfig. The 1.16.5 and 1.20.1 columns cover all 14 definitions in each released ClientConfig; the modern guide covers all 15. A dash means absent from this scoped set, not globally impossible behavior.

| Key | 1.12.2 | 1.16.5 | 1.20.1 | 1.21.1 |
|---|---|---|---|---|
| showVanityLevels | true | — | — | — |
| showXpParticles | true | true | true | true |
| showDailyMessages | true | — | — | — |
| showWelcomeMessage | true | true | true | true |
| showPlayerHalos | true | true | true | true |
| personalHaloPreference | Super_Donator | Donator | Donator | DONATOR |
| mainWindowTheme | Default | — | — | — |
| mainWindowPausesGame | true | — | — | — |
| thirdPartyBestiary | true | true | true | true |
| hudResourcesPosition | Top_Right | Top_Right | Top_Right | Top_Right |
| hudResourcesHorizontal | true | true | true | true |
| useToasts | true | true | true | true |
| partyDeaths | false | false | false | false |
| adventGuiTheme | — | Default | Default | Default |
| disableHudPotionOffset | — | false | false | false |
| hudSkillProgressRenderType | — | Bar | Bar | Bar |
| rotatingTrophies | — | true | true | true |
| healthRenderType | — | BAR_NUMERIC | BAR_NUMERIC | BAR_NUMERIC |
| screenShake | — | — | — | true |

mainWindowTheme in the historical selected fields and adventGuiTheme in the later client configs are different keys. Similar purpose does not make the files interchangeable. The legacy mainWindowPausesGame default is not a guarantee that a multiplayer server pauses.

## Exact choices to preserve

| Release | Resource HUD corners | Halo choices |
|---|---|---|
| 1.12.2 | Top_Right, Top_Left, Bottom_Right, Bottom_Left | Donator, Super_Donator, Wiki_Editor |
| 1.16.5 | Top_Right, Top_Left, Bottom_Right, Bottom_Left | Donator, Super_Donator, Wiki_Editor |
| 1.20.1 | Top_Right, Top_Left | Donator, Super_Donator, Wiki_Editor |
| 1.21.1 | Top_Right, Top_Left | DONATOR, SUPER_DONATOR, WIKI_EDITOR |

The intermediate and modern skill progress choices are Ring, Bar, Percent and None. Their health choices are HEARTS, BAR, NUMERIC and BAR_NUMERIC. These names are case-sensitive. Selecting a halo preference does not grant eligibility for it.

## Safe migration checklist

1. Identify the actual Minecraft and AoA release, not only the modpack name.
2. Let that release generate its own config structure. Close the game before manual edits.
3. Transfer only the individual preference you understand, using the destination key, section and enum spelling.
4. Rebind controls through the destination game’s Controls screen rather than transplanting numeric key values.
5. Test HUD visibility, scale, potion overlap and both supported orientations in the target instance.
6. Leave gameplay, dimension IDs, progression, portal and leaderboard settings alone unless you deliberately intend to change them.
7. Compare before/after performance only with a repeatable benchmark; this reference makes no FPS-improvement claim.

For complete modern explanations, use [Controls, HUD and client settings · 1.21.1](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Controls-HUD-and-Client-Settings-1.21.1).

## Why the released files matter

The available 1.20 source pin uses a newer-looking halo enum name, while the inspected 3.7.1 artifact still references AoAHaloUtil.Type.Choosable.Donator. This comparison follows the released class instructions and records their hashes. A nearby source snapshot is not treated as byte-for-byte proof of an entire release.

## Evidence

- [Older release settings, key registrations and exact enum initializer receipts](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/historical-client-settings-evidence.json)
- [Modern settings comparison](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/client-settings-evidence-1.21.1.json)
- [Diagram receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/historical-client-settings-art-evidence.json)

This page documents released defaults without changing any user configuration or executing Minecraft/mod code.
