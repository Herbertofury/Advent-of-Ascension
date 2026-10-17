# Special armor and Skill Helmet model guide

[Ordinary armor set gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Worn-Armor-Gallery-1.21.1) · [Armor preparation](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Materials-and-Set-Preparation-1.21.1) · [Skill training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skill-Training-Walkthrough-1.21.1)

![Base and trim factory variants of three Skill Helmets](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/special-armour-overview-1.21.1.webp)

**Minecraft 1.21.1 / AoA 3.7.16.1:** six registered Skill Helmets have their own detailed models, with separate base and trim factories. Five other standalone helmets and Old Boot use the ordinary armor mesh. Together with the 48 full-set studies, these references now associate a worn-model study with every one of the **204 checked armor registrations**. That is 66 study images, not 66 obtainable armor sets.

The twelve Skill Helmet views are isolated factory-pose reconstructions. Runtime head-pose copying, player skin, enchanted glint and Minecraft's exact lighting/postprocessing are omitted. Source-marked fullbright cubes are preserved and shown with an unlit documentation shader; this is not an in-game shader capture. The six ordinary-piece studies use the relevant official vanilla armor mesh parts.

## How to use a Skill Helmet

1. Choose the helmet for the skill you actually intend to train; each row below links the exact item and its recipe/drop searches. Registration does not prove that every acquisition route is presently available.
2. Equip it and verify the corresponding skill's XP behavior on your exact build. The released equip callback adds **0.5** to that skill instance's XP modifier, and unequip subtracts **0.5**. It is not a promise of a flat 50% increase for every XP source or with every other bonus.
3. These six helmets carry an unbreakable component and override maximum damage to zero. They are also explicitly enchantable and declare compatibility with any armor set. Check the other worn slots and equipment requirements separately.
4. The selected stock cosmetic path uses skill level **1000**, including vanity levels, for the trim appearance. This is a model/texture variant, not an ordinary smithing-template recipe.
5. If the displayed variant seems wrong, use the viewer/wearer test matrix below before reporting it as a confirmed defect.

### Read the XP bonus carefully

The inspected skill XP path applies the server's global XP modifier, then the Nowhere multiplier of 0.5, then the skill instance's XP modifier, followed by the positive-cycle multiplier of `3 × cycle`; the result is clamped to at least zero. `adjustXp` has an `ignoreXpBuffs` branch and other conditions, so this is not an unconditional reward formula for every event. With an otherwise 1.0 skill modifier, one +0.5 equip callback makes that factor 1.5; with an existing 2.0 factor it becomes 2.5, not 3.0. Other event handlers and actual equip/unequip balance still need runtime verification.

## Six registered Skill Helmets: base and trim

### Helm of the Dextrous

Skill registration: **DEXTERITY** · [Exact item, properties and acquisition searches](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_dextrous)

| Base factory | Trim factory |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_dextrous-model-1.21.1.webp" width="330" alt="Helm of the Dextrous base isolated source-model study"><br>16 parts · 41 cubes · 0 source fullbright cubes | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_dextrous_trim-model-1.21.1.webp" width="330" alt="Helm of the Dextrous trim isolated source-model study"><br>17 parts · 42 cubes · 8 source fullbright cubes |

### Helm of the Dryad

Skill registration: **FARMING** · [Exact item, properties and acquisition searches](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_dryad)

| Base factory | Trim factory |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_dryad-model-1.21.1.webp" width="330" alt="Helm of the Dryad base isolated source-model study"><br>33 parts · 42 cubes · 0 source fullbright cubes | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_dryad_trim-model-1.21.1.webp" width="330" alt="Helm of the Dryad trim isolated source-model study"><br>41 parts · 47 cubes · 12 source fullbright cubes |

### Helm of the Ritualist

Skill registration: **IMBUING** · [Exact item, properties and acquisition searches](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_ritualist)

| Base factory | Trim factory |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_ritualist-model-1.21.1.webp" width="330" alt="Helm of the Ritualist base isolated source-model study"><br>18 parts · 31 cubes · 0 source fullbright cubes | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_ritualist_trim-model-1.21.1.webp" width="330" alt="Helm of the Ritualist trim isolated source-model study"><br>24 parts · 38 cubes · 0 source fullbright cubes |

### Helm of the Trawler

Skill registration: **HAULING** · [Exact item, properties and acquisition searches](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_trawler)

| Base factory | Trim factory |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_trawler-model-1.21.1.webp" width="330" alt="Helm of the Trawler base isolated source-model study"><br>21 parts · 42 cubes · 0 source fullbright cubes | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_trawler_trim-model-1.21.1.webp" width="330" alt="Helm of the Trawler trim isolated source-model study"><br>26 parts · 47 cubes · 10 source fullbright cubes |

### Helm of the Treasurer

Skill registration: **EXTRACTION** · [Exact item, properties and acquisition searches](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_treasurer)

| Base factory | Trim factory |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_treasurer-model-1.21.1.webp" width="330" alt="Helm of the Treasurer base isolated source-model study"><br>17 parts · 43 cubes · 0 source fullbright cubes | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_treasurer_trim-model-1.21.1.webp" width="330" alt="Helm of the Treasurer trim isolated source-model study"><br>23 parts · 49 cubes · 6 source fullbright cubes |

### Helm of the Warrior

Skill registration: **INNERVATION** · [Exact item, properties and acquisition searches](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:helm_of_the_warrior)

| Base factory | Trim factory |
|---|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_warrior-model-1.21.1.webp" width="330" alt="Helm of the Warrior base isolated source-model study"><br>14 parts · 41 cubes · 0 source fullbright cubes | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/helm_of_the_warrior_trim-model-1.21.1.webp" width="330" alt="Helm of the Warrior trim isolated source-model study"><br>19 parts · 44 cubes · 5 source fullbright cubes |

## Six standalone ordinary-mesh pieces

These pictures isolate the actual armor layer without a player skin underneath. Old Boot is a boots-slot item, so its worn study displays the paired leg/foot geometry used by that slot. The five headpieces declare universal set compatibility; Old Boot does not.

| Piece | Worn-model study | Base properties |
|---|---|---|
| [Achelos Helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:achelos_helmet) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/achelos_helmet-worn-1.21.1.webp" width="220" alt="Achelos Helmet isolated ordinary-armor mesh study"> | Armor 5 · toughness 7.0 · vanilla-formula durability reference 660 |
| [Oceanus Helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:oceanus_helmet) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/oceanus_helmet-worn-1.21.1.webp" width="220" alt="Oceanus Helmet isolated ordinary-armor mesh study"> | Armor 5 · toughness 7.0 · vanilla-formula durability reference 660 |
| [Sealord Helmet](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:sealord_helmet) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/sealord_helmet-worn-1.21.1.webp" width="220" alt="Sealord Helmet isolated ordinary-armor mesh study"> | Armor 5 · toughness 7.0 · vanilla-formula durability reference 660 |
| [Face Mask](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:face_mask) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/face_mask-worn-1.21.1.webp" width="220" alt="Face Mask isolated ordinary-armor mesh study"> | Armor 5 · toughness 5.0 · vanilla-formula durability reference 396 |
| [Chroma Goggles](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:chroma_goggles) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/chroma_goggles-worn-1.21.1.webp" width="220" alt="Chroma Goggles isolated ordinary-armor mesh study"> | Armor 2 · toughness 1.0 · vanilla-formula durability reference 297 |
| [Old Boot](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3:old_boot) | <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/old_boot-worn-1.21.1.webp" width="220" alt="Old Boot isolated ordinary-armor mesh study"> | Armor 2 · toughness 0 · vanilla-formula durability reference 390 |

## Viewer and wearer: a bounded rendering review

The inspected `getGenericArmorModel` and `getArmorTexture` both read `ClientPlayerDataManager.get().getSkill(...)`. The model path additionally checks that the rendered entity is a Player; the texture path has no equivalent entity-type gate in the selected method. This is a concrete reason to test which person's progress is supposed to control the cosmetic, **not a reproduced multiplayer bug**.

| Check | Why it matters |
|---|---|
| Local wearer at 999, then 1000 | Establish the intended base-to-trim transition |
| Remote wearer and local viewer at opposite skill levels | Check whether appearance follows the intended owner |
| Armor stand or another supported non-player wearer while the viewer is at 1000 | Check whether selected geometry and texture agree |
| Resource reload, reconnect and switching viewed entities | Check cached models and presentation state |

The model uses `hasLevel(1000)` while the texture uses `getLevel(true) == 1000`. The stock setter clamps levels to 0–1000, so **that comparison difference alone is not evidence of a normally reachable mismatch**. Do not “fix” it by removing the model's entity guard or substituting arbitrary player data without establishing the intended behavior.

## Evidence and remaining work

[Layer factories and geometry hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skill-helmet-model-evidence-1.21.1.json) · [Registration-to-model routes and selection methods](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skill-helmet-selection-evidence-1.21.1.json) · [Twelve render hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/skill-helmet-render-evidence-1.21.1.json) · [Six ordinary-piece studies](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/standalone-armour-render-evidence-1.21.1.json)

Each of the twelve selected models was followed from the registered helmet's skill through the cached model pair, its model factory and exact layer-definition callback. Four other dormant skill-model families are not presented here as currently registered/obtainable helmets. No Java/game code was executed. Acquisition completeness, exact equip-event balance, remote-player cosmetic ownership and real client/server rendering acceptance remain open.

AoA models, textures and systems: Tslat and contributors. Vanilla armor geometry: Mojang/Microsoft. Original extraction, neutral rendering and documentation layout.
