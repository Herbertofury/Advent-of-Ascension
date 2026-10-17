[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [1.12.2 bow states](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bow-Draw-State-Gallery-1.12.2) · [Modern archery guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bows-and-Crossbows-1.21.1)

# Bow and crossbow draw-state comparisons

**Inspected releases:** Minecraft 1.16.5 / AoA 3.6.11, Minecraft 1.20.1 / AoA 3.7.1, and Minecraft 1.21.1 / AoA 3.7.16.1.

This gallery covers **42 item identities in each release: 33 bows and 9 crossbows**. That is 126 release-specific records and **558 source-state references**. Every selected item has its own base/override model hashes and texture hashes; newer textures are not silently substituted into an older card.

![Coral Crossbow resting, drawing, charged and firework source states](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-coral_crossbow-4009a2dafb9e.webp)

These are actual 16×16 layer0 textures enlarged without smoothing. They supplement the ordinary model portraits. They do not certify assembled 3D poses, animation, HUD/game rendering or equal weapon behavior.

## Which states are shown?

| Family | Columns / states |
|---|---|
| Bow · four states | Resting; pulling; pulling with pull threshold 0.65; pulling with pull threshold 0.90 |
| Crossbow · six states | Resting; pulling; pulling with pull threshold 0.58; pulling with pull threshold 1.0; charged; charged with firework |

The inspected resources use namespaced minecraft:pulling, minecraft:pull, minecraft:charged and minecraft:firework predicates. These are model-selection definitions. A firework image is not by itself proof that a modpack permits that ammunition or that a shot was tested.

The draw override models and their parents remain recorded as shipped. Their transform and resource-pack behavior needs separate target-client checks.

## What changed between releases?

**28 identities have matching RGBA texture sequences and predicates across all three inspected releases. Fourteen have two different source-pixel sequences.** The sheet labels identify exactly which versions share each one.

Ten of those fourteen use one sequence in 1.16.5 and another in both newer releases. Four share their 1.16.5/1.20.1 sequence but differ in 1.21.1. This is a comparison of the inspected artifacts, not a claim about the exact patch that introduced a change.

| Item | Pixel-matching release groups |
|---|---|
| Alacrity Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Ancient Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Explosive Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Ice Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Infernal Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Lunar Bow | 1.16.5, 1.20.1 ; 1.21.1 |
| Poison Bow | 1.16.5, 1.20.1 ; 1.21.1 |
| Predatious Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Runic Bow | 1.16.5, 1.20.1 ; 1.21.1 |
| Shyregem Bow | 1.16.5, 1.20.1 ; 1.21.1 |
| Skeletal Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Speed Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Weaken Bow | 1.16.5 ; 1.20.1, 1.21.1 |
| Wither Bow | 1.16.5 ; 1.20.1, 1.21.1 |

## Browse every identity and version

Expand an item to compare its source sheets. A shared sheet is reused only after checking the RGBA pixels and predicate sequence for that exact item ID. Each release-specific item link still uses its own inventory data and source references.

<details><summary>Alacrity Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Alacrity Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-alacrity_bow-2592049589fa.webp)

**Minecraft 1.20.1, 1.21.1**

![Alacrity Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-alacrity_bow-8466523ef1f4.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aalacrity_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aalacrity_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aalacrity_bow)

</details>

<details><summary>Ancient Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Ancient Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-ancient_bow-cd8c3d782989.webp)

**Minecraft 1.20.1, 1.21.1**

![Ancient Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-ancient_bow-add2fe3588a4.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aancient_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aancient_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aancient_bow)

</details>

<details><summary>Atlantic Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Atlantic Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-atlantic_bow-c4b305386f0c.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aatlantic_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aatlantic_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aatlantic_bow)

</details>

<details><summary>Baron Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Baron Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-baron_bow-0e9927cfa857.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Abaron_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Abaron_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abaron_bow)

</details>

<details><summary>Boreic Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Boreic Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-boreic_bow-7b895f7c9a71.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aboreic_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aboreic_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aboreic_bow)

</details>

<details><summary>Coral Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Coral Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-coral_crossbow-4009a2dafb9e.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Acoral_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Acoral_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Acoral_crossbow)

</details>

<details><summary>Daybreaker Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Daybreaker Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-daybreaker_bow-6620e027186b.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Adaybreaker_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Adaybreaker_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adaybreaker_bow)

</details>

<details><summary>Deep Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Deep Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-deep_bow-12359bc6c841.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Adeep_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Adeep_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Adeep_bow)

</details>

<details><summary>Explosive Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Explosive Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-explosive_bow-75a618ee7f06.webp)

**Minecraft 1.20.1, 1.21.1**

![Explosive Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-explosive_bow-01e4f5f4b4de.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aexplosive_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aexplosive_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aexplosive_bow)

</details>

<details><summary>Haunted Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Haunted Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-haunted_bow-5d432415bd39.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ahaunted_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ahaunted_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ahaunted_bow)

</details>

<details><summary>Ice Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Ice Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-ice_bow-021188dd1aa1.webp)

**Minecraft 1.20.1, 1.21.1**

![Ice Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-ice_bow-5658fd9e8b54.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aice_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aice_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aice_bow)

</details>

<details><summary>Infernal Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Infernal Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-infernal_bow-b74e8d7bdfc8.webp)

**Minecraft 1.20.1, 1.21.1**

![Infernal Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-infernal_bow-61e4847a88df.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ainfernal_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ainfernal_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ainfernal_bow)

</details>

<details><summary>Justice Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Justice Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-justice_bow-784f35b1fd59.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ajustice_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ajustice_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ajustice_bow)

</details>

<details><summary>Lunar Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5, 1.20.1**

![Lunar Bow source states for 1.16.5, 1.20.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-lunar_bow-2060b95bdf14.webp)

**Minecraft 1.21.1**

![Lunar Bow source states for 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-lunar_bow-0c976f38e23c.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alunar_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alunar_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_bow)

</details>

<details><summary>Lunar Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Lunar Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-lunar_crossbow-ebeb0f7c91e8.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Alunar_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Alunar_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Alunar_crossbow)

</details>

<details><summary>Mecha Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Mecha Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-mecha_bow-0a103f04f807.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Amecha_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Amecha_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_bow)

</details>

<details><summary>Mecha Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Mecha Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-mecha_crossbow-c6e104be9117.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Amecha_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Amecha_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Amecha_crossbow)

</details>

<details><summary>Nightmare Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Nightmare Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-nightmare_bow-484e6f508187.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Anightmare_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Anightmare_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Anightmare_bow)

</details>

<details><summary>Poison Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5, 1.20.1**

![Poison Bow source states for 1.16.5, 1.20.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-poison_bow-ffeee45393c9.webp)

**Minecraft 1.21.1**

![Poison Bow source states for 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-poison_bow-3b66a0001701.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apoison_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apoison_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apoison_bow)

</details>

<details><summary>Predatious Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Predatious Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-predatious_bow-1d857e4ff73d.webp)

**Minecraft 1.20.1, 1.21.1**

![Predatious Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-predatious_bow-05cbddb52ae5.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apredatious_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apredatious_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apredatious_bow)

</details>

<details><summary>Primordial Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Primordial Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-primordial_bow-8d4e020496db.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aprimordial_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aprimordial_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aprimordial_bow)

</details>

<details><summary>Pyro Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Pyro Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-pyro_crossbow-90f3808c9af1.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Apyro_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Apyro_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apyro_crossbow)

</details>

<details><summary>Rosidian Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Rosidian Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-rosidian_bow-469d26924e8e.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arosidian_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arosidian_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_bow)

</details>

<details><summary>Rosidian Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Rosidian Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-rosidian_crossbow-c5c1f643b368.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arosidian_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arosidian_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arosidian_crossbow)

</details>

<details><summary>Runic Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5, 1.20.1**

![Runic Bow source states for 1.16.5, 1.20.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-runic_bow-144e1813b077.webp)

**Minecraft 1.21.1**

![Runic Bow source states for 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-runic_bow-e048c8b594c6.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Arunic_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Arunic_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Arunic_bow)

</details>

<details><summary>Screamer Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Screamer Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-screamer_bow-3c34f0495553.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ascreamer_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ascreamer_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ascreamer_bow)

</details>

<details><summary>Shyregem Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5, 1.20.1**

![Shyregem Bow source states for 1.16.5, 1.20.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-shyregem_bow-feb7e8e60fd6.webp)

**Minecraft 1.21.1**

![Shyregem Bow source states for 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-shyregem_bow-9d95877b3b02.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Ashyregem_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Ashyregem_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Ashyregem_bow)

</details>

<details><summary>Skeletal Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Skeletal Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-skeletal_bow-d4c72f270ddf.webp)

**Minecraft 1.20.1, 1.21.1**

![Skeletal Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-skeletal_bow-151aa3787622.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askeletal_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askeletal_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_bow)

</details>

<details><summary>Skeletal Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Skeletal Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-skeletal_crossbow-07d52f96c406.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askeletal_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askeletal_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askeletal_crossbow)

</details>

<details><summary>Skydriver Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Skydriver Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-skydriver_bow-316680d1b6f3.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Askydriver_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Askydriver_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Askydriver_bow)

</details>

<details><summary>Slingshot · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Slingshot source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-slingshot-f398c450193a.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aslingshot) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aslingshot) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aslingshot)

</details>

<details><summary>Soulfire Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Soulfire Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-soulfire_bow-f04659439a78.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asoulfire_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asoulfire_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asoulfire_bow)

</details>

<details><summary>Spectral Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Spectral Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-spectral_bow-b6c8b77571ce.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspectral_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspectral_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspectral_bow)

</details>

<details><summary>Spectral Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Spectral Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-spectral_crossbow-33ad20c44f24.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspectral_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspectral_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspectral_crossbow)

</details>

<details><summary>Speed Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Speed Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-speed_bow-0bf7b5c51f35.webp)

**Minecraft 1.20.1, 1.21.1**

![Speed Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-speed_bow-e7d9dd5ed4ac.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aspeed_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aspeed_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aspeed_bow)

</details>

<details><summary>Sunshine Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Sunshine Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-sunshine_bow-8ae63cc9aa83.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Asunshine_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Asunshine_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Asunshine_bow)

</details>

<details><summary>Toxin Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Toxin Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-toxin_bow-78bc43caae1e.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Atoxin_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Atoxin_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atoxin_bow)

</details>

<details><summary>Troll's Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Troll's Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-trolls_crossbow-f2971c854146.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Atrolls_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Atrolls_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Atrolls_crossbow)

</details>

<details><summary>Viral Crossbow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Viral Crossbow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-viral_crossbow-d283733b2965.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aviral_crossbow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aviral_crossbow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aviral_crossbow)

</details>

<details><summary>Void Bow · 1 checked source sheet</summary>

**Minecraft 1.16.5, 1.20.1, 1.21.1**

![Void Bow source states for 1.16.5, 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-void_bow-337ac7f824e9.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Avoid_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Avoid_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avoid_bow)

</details>

<details><summary>Weaken Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Weaken Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-weaken_bow-e8dd608afcb4.webp)

**Minecraft 1.20.1, 1.21.1**

![Weaken Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-weaken_bow-4b785aee2972.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Aweaken_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Aweaken_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aweaken_bow)

</details>

<details><summary>Wither Bow · 2 checked source sheets</summary>

**Minecraft 1.16.5**

![Wither Bow source states for 1.16.5](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-wither_bow-bed25ae31ed0.webp)

**Minecraft 1.20.1, 1.21.1**

![Wither Bow source states for 1.20.1, 1.21.1](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/ranged-draw-states-wither_bow-33ca1db1a9ce.webp)

[1.16.5 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.16.5&id=aoa3%3Awither_bow) · [1.20.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.20.1&id=aoa3%3Awither_bow) · [1.21.1 item reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awither_bow)

</details>


## Fast, version-safe browsing

The item browser creates a state image only when its **Bow / crossbow source draw-state textures** panel is first expanded. Images are lazy, have a reserved aspect ratio, and keep a full-resolution link if loading fails. The selected inventory release is reused; there is no extra state-data request on each card.

The 126 records use **56 pixel-distinct sheets**, avoiding 70 duplicate image files without mixing different version artwork. Shared pixels do not prove shared model transforms, item components, timing, ammo, damage or gameplay.

For the earlier historical release, the separate [33-bow 1.12.2 gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bow-Draw-State-Gallery-1.12.2) contains 132 additional state references and preserves its different model-parent structure.

[Every released model/texture hash, pixel signature and sharing group](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/ranged-draw-state-evidence.json). Source artwork belongs to Tslat and contributors; checkerboards and labels are documentation aids.
