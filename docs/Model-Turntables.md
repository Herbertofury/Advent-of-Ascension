# Model Turntables

[Open the interactive rendered-turntable viewer](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html)

![Three source-model turntable previews](https://herbertofury.github.io/Advent-of-Ascension/previews/boss-turntable-cover.webp)

## Inspect a model from every side

- Drag horizontally, use the arrow buttons or scrub the angle slider. Each model has **24 rendered camera angles**, spaced 15 degrees apart.
- Use preview zoom for details and Reset to return to the first view.
- Rotation is opt-in. The viewer starts paused, stops when its tab becomes hidden, and supports keyboard arrow keys.
- Model links preserve the selected entry, and each viewer links back to that creature’s version-specific evidence.

## Included entries

This first collection has **11 source model entries / 264 rendered frames** from Minecraft 1.21.1 / AoA 3.7.16.1. These are not 11 necessarily distinct designs: some resources share appearances. All 11 IDs are present in the inspected modern source roster.

| Model entry | Open the views |
|---|---|
| Smash | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:smash) |
| Elite Smash | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:elite_smash) |
| Nethengeic Wither | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:nethengeic_wither) |
| Elite Nethengeic Wither | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:elite_nethengeic_wither) |
| King Bambambam | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:king_bambambam) |
| Elite King Bambambam | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:elite_king_bambambam) |
| Tyrosaur | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:tyrosaur) |
| Elite Tyrosaur | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:elite_tyrosaur) |
| Wounded Tyrosaur | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:wounded_tyrosaur) |
| Skeletron | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:skeletron) |
| Elite Skeletron | [24-angle preview](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html?entity=aoa3:elite_skeletron) |

## What the motion means

The camera orbits a **static source-model rest pose**. No walk cycle, attack, skinning state machine or live game shader is being simulated. The view has fixed framing across the orbit, so it does not repeatedly zoom in and out as the model turns. Source model/texture hashes and all frame hashes are retained.

This is an interactive presentation of rendered views, not downloadable live geometry or a free-pitch 3D editor. Documentation lighting differs from in-game lighting. A rendered model does not establish survival availability, boss encounter completeness or a finished Enderloom implementation.

## Loading and accessibility

The index loads once. The selected model loads one image sheet, with the other sheets deferred until selected. Revisiting a loaded model reuses the cached image. Failed image loads are evicted so Retry can fetch again. A selection sequence check prevents a late image from replacing the newest selection.

Controls remain disabled while their image is loading. Descriptive canvas labels include the model, release and current frame. The full rendered sheet and hashed evidence remain available as separate links.

## Evidence

[Model, texture and 264 frame hashes](https://herbertofury.github.io/Advent-of-Ascension/boss-turntable-index.json). The generator performs no mod or game-code execution; it reads the released geometry and textures and renders them independently.

[Bestiary](Bestiary) · [Modern boss dossiers](Modern-Boss-Dossiers) · [Boss entry and token preparation](Boss-Entry-and-Token-Preparation-1.21.1).

Models and textures credited to **Tslat and contributors**. [Upstream source](https://github.com/Tslat/Advent-Of-Ascension).
