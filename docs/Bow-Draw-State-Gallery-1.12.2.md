[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Historical bow timing and ammo](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bow-Draw-Timing-and-Ammunition-1.12.2) · [Item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&family=historical-bow)

# Historical bow draw-state gallery

**Minecraft 1.12.2 / AoA 3.3.6.** Every one of the 33 inspected bows now has a four-state source-texture sheet: its resting layer and the three released draw overrides. That is **132 checked texture references**, not 132 different weapons.

![Alacrity Bow resting and three drawing texture states](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-alacrity_bow.webp)

These are the actual 16×16 layer0 textures enlarged with nearest-neighbor scaling over a checkerboard. They supplement the existing source-model portraits. They are **not assembled 3D draw poses, interpolated animation, or in-game screenshots**.

## Read the four columns

| Column | Released model predicate |
|---|---|
| Resting layer | Base model's layer0 texture |
| First drawing layer | pulling = 1 |
| Second drawing layer | pulling = 1 and pull threshold 0.65 |
| Third drawing layer | pulling = 1 and pull threshold 0.90 |

All 33 inspected base model JSONs declare this same sequence of three overrides. The predicate thresholds are model-selection data. They should not be confused with the separate curved arrow-velocity calculation in the firing guide.

The selected pull property uses the bow draw multiplier and elapsed use time divided by 20 while an active item is a BaseBow. The separate pulling property requires active use and the active stack to be the same stack. These two checks are not interchangeable. The released property methods are included in the evidence.

## Browse every bow

Open a name below for its sheet. The item link opens the normal source-model portrait and draw-timing panel; the draw-state image is created only when that panel is first expanded, with a full-resolution fallback link if the image fails to load.

<details><summary>Alacrity Bow · four source states</summary>

![Alacrity Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-alacrity_bow.webp)

[Open Alacrity Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AlacrityBow.name).

</details>

<details><summary>Ancient Bow · four source states</summary>

![Ancient Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-ancient_bow.webp)

[Open Ancient Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AncientBow.name).

</details>

<details><summary>Atlantic Bow · four source states</summary>

![Atlantic Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-atlantic_bow.webp)

[Open Atlantic Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.AtlanticBow.name).

</details>

<details><summary>Baron Bow · four source states</summary>

![Baron Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-baron_bow.webp)

[Open Baron Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BaronBow.name).

</details>

<details><summary>Boreic Bow · four source states</summary>

![Boreic Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-boreic_bow.webp)

[Open Boreic Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BoreicBow.name).

</details>

<details><summary>Daybreaker Bow · four source states</summary>

![Daybreaker Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-daybreaker_bow.webp)

[Open Daybreaker Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DaybreakerBow.name).

</details>

<details><summary>Deep Bow · four source states</summary>

![Deep Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-deep_bow.webp)

[Open Deep Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.DeepBow.name).

</details>

<details><summary>Explosive Bow · four source states</summary>

![Explosive Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-explosive_bow.webp)

[Open Explosive Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ExplosiveBow.name).

</details>

<details><summary>Haunted Bow · four source states</summary>

![Haunted Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-haunted_bow.webp)

[Open Haunted Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.HauntedBow.name).

</details>

<details><summary>Ice Bow · four source states</summary>

![Ice Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-ice_bow.webp)

[Open Ice Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.IceBow.name).

</details>

<details><summary>Infernal Bow · four source states</summary>

![Infernal Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-infernal_bow.webp)

[Open Infernal Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.InfernalBow.name).

</details>

<details><summary>Justice Bow · four source states</summary>

![Justice Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-justice_bow.webp)

[Open Justice Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.JusticeBow.name).

</details>

<details><summary>Lunar Bow · four source states</summary>

![Lunar Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-lunar_bow.webp)

[Open Lunar Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.LunarBow.name).

</details>

<details><summary>Mecha Bow · four source states</summary>

![Mecha Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-mecha_bow.webp)

[Open Mecha Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.MechaBow.name).

</details>

<details><summary>Nightmare Bow · four source states</summary>

![Nightmare Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-nightmare_bow.webp)

[Open Nightmare Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.NightmareBow.name).

</details>

<details><summary>Poison Bow · four source states</summary>

![Poison Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-poison_bow.webp)

[Open Poison Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonBow.name).

</details>

<details><summary>Predatious Bow · four source states</summary>

![Predatious Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-predatious_bow.webp)

[Open Predatious Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PredatiousBow.name).

</details>

<details><summary>Primordial Bow · four source states</summary>

![Primordial Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-primordial_bow.webp)

[Open Primordial Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PrimordialBow.name).

</details>

<details><summary>Rosidian Bow · four source states</summary>

![Rosidian Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-rosidian_bow.webp)

[Open Rosidian Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RosidianBow.name).

</details>

<details><summary>Runic Bow · four source states</summary>

![Runic Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-runic_bow.webp)

[Open Runic Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.RunicBow.name).

</details>

<details><summary>Screamer Bow · four source states</summary>

![Screamer Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-screamer_bow.webp)

[Open Screamer Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ScreamerBow.name).

</details>

<details><summary>Shyregem Bow · four source states</summary>

![Shyregem Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-shyregem_bow.webp)

[Open Shyregem Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ShyregemBow.name).

</details>

<details><summary>Skeletal Bow · four source states</summary>

![Skeletal Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-skeletal_bow.webp)

[Open Skeletal Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkeletalBow.name).

</details>

<details><summary>Skydriver Bow · four source states</summary>

![Skydriver Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-skydriver_bow.webp)

[Open Skydriver Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SkydriverBow.name).

</details>

<details><summary>Slingshot · four source states</summary>

![Slingshot resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-slingshot.webp)

[Open Slingshot item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Slingshot.name).

</details>

<details><summary>Soulfire Bow · four source states</summary>

![Soulfire Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-soulfire_bow.webp)

[Open Soulfire Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SoulfireBow.name).

</details>

<details><summary>Spectral Bow · four source states</summary>

![Spectral Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-spectral_bow.webp)

[Open Spectral Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpectralBow.name).

</details>

<details><summary>Speed Bow · four source states</summary>

![Speed Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-speed_bow.webp)

[Open Speed Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SpeedBow.name).

</details>

<details><summary>Sunshine Bow · four source states</summary>

![Sunshine Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-sunshine_bow.webp)

[Open Sunshine Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.SunshineBow.name).

</details>

<details><summary>Toxin Bow · four source states</summary>

![Toxin Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-toxin_bow.webp)

[Open Toxin Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ToxinBow.name).

</details>

<details><summary>Void Bow · four source states</summary>

![Void Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-void_bow.webp)

[Open Void Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.VoidBow.name).

</details>

<details><summary>Weaken Bow · four source states</summary>

![Weaken Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-weaken_bow.webp)

[Open Weaken Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WeakenBow.name).

</details>

<details><summary>Wither Bow · four source states</summary>

![Wither Bow resting and three draw override textures](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/bow-draw-states-1.12.2-wither_bow.webp)

[Open Wither Bow item and timing reference](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherBow.name).

</details>


## Parent models and restoration limits

The 33 base JSONs inherit item/bow. The 99 inspected override JSONs name aoa3:item/weapons/bows/speed_bow as their parent while supplying their own layer0 texture. Those parent references are retained in the evidence; this documentation does not silently rewrite them or claim that a flat sheet validates the entire inherited transform/override pipeline.

For a renderer port or optional weapon remodel, verify base and draw transforms, handedness, active-stack selection, resource-pack overrides and state transitions in the target client. Preserve the original textures and predicates until a deliberate replacement has been tested. A missing transition in a new renderer is not fixed merely by displaying the four textures in a wiki.

[132 texture/model references, 33 output hashes and two released property methods](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/bow-draw-state-evidence-1.12.2.json) · [Draw timing and ammunition walkthrough](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bow-Draw-Timing-and-Ammunition-1.12.2).
