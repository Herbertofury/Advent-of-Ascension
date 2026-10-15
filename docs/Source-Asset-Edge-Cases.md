# Source asset edge cases

## The last seven 1.12.2 inventory candidates

These supplemental previews cover the seven records excluded from the first 2,459-image historical inventory pass. Together the regular galleries and this diagnostic sheet illustrate all **2,466 unambiguous localization/model candidates in that extraction**. This is not a census of every runtime registry entry.

![Seven source edge-case inventory previews](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.12.2-source-edge-cases.webp)

Models and textures: **Tslat and contributors**, official AoA 3.3.6 artifact. These are independently rendered documentation images.

| Asset | Why the strict first pass stopped | Supplemental handling |
|---|---|---|
| Filtration System | Some faces reference undefined `#missing` texture aliases | Explicit magenta/black diagnostic texture for those faces; original visible faces retained |
| Boiling Filtration System | Undefined texture aliases | Same explicit diagnostic handling |
| Gold Skeletron Statue | Undefined texture aliases | Same explicit diagnostic handling |
| Iropole | Undefined texture aliases | Same explicit diagnostic handling |
| Ornate Skeletron Statue | Undefined texture aliases | Same explicit diagnostic handling |
| Skeletron Statue | Undefined texture aliases | Same explicit diagnostic handling |
| Shyre Cloud | The original cutout threshold discarded its translucent pixels | Preserve nonzero alpha in a nearest-depth reference preview |

The unresolved faces are largely hidden in this view. Their absence from the visible screenshot does not prove the source contains no defects. No source textures or mod files were patched, and no guessed replacement artwork was substituted.

The Shyre Cloud view preserves the source alpha but does not implement full runtime translucent surface blending. Its color and opacity can differ against other backgrounds or under the game's lighting.

## Restoration implications

- Inspect and test undefined aliases before changing them. Hidden internal faces may be deliberately irrelevant to the visible mesh; a broad material replacement could introduce a regression.
- Keep cutout and translucent rendering paths separate. A threshold suitable for plants can erase a cloud-like block.
- Check every model from several angles and against contrasting backgrounds in the target game before declaring renderer parity.
- Preserve the exact source generation. In particular, an old statue asset does not establish the behavior or appearance of a later entity implementation.

[Historical galleries](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Galleries) · [Coverage and remaining work](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage)
