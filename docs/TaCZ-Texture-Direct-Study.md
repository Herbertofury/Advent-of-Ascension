# Actual TaCZ texture study

These findings come from downloaded pack archives and direct inspection of the selected texture pixels. The included JSON records archive and selected-file SHA-256 hashes. This package contains the audit code and metadata, not copied third-party texture assets.

## What was inspected

| Pack/version | Selected UV texture | Size | UV-folder PNGs |
| --- | --- | --- | --- |
| Ars Armorer 1.0.1 | shotgun_jet_ejector_uv.png | 64×64 | 8 |
| Create Armorer 1.2.0.1-for117 | shotgun_db_stone.png | 256×256 | 13 |
| Helldivers file 9069318 hotfix | quasar.png | 256×256 | 116 |

The inventory counts may include alternate or shader maps. They are not weapon counts. Filename presence does not prove a particular shader path is supported in a target runtime.

## Useful observations to apply

- The inspected Ars sheet uses deliberate compact pixel shading and recognizable material regions. Resolution alone is not the quality target.
- The inspected Create sheet defines wood slats, seams and material boundaries. Structural detail is purposeful rather than uniform procedural noise.
- The inspected Quasar sheet uses equipment markings, yellow warnings and an OVERHEAT label alongside material shading. Labels are part of readable fictional equipment design, not a reason to copy the source image.

## AoA implementation checklist

1. Establish silhouette and physical clearance before painting around broken geometry.
2. Make an original UV layout with consistent visible texel density. Prioritize first-person grip, receiver, sight and moving parts; budget concealed faces separately.
3. Paint distinct indigo/enamel/metal/rubber or other weapon-specific regions, with purposeful seams and restrained edge wear. Use AoA's identity and the pinned concept as the palette source.
4. Keep important markings readable at gameplay size. Avoid uniformly noisy wear that obscures the shape.
5. Separate base color and any supported emissive treatment. Verify the actual renderer supports the chosen map/channel rather than relying on Blender nodes.
6. Review neutral-lit, bright-world and dark-world views; include minification, mip bleeding, UV seams and moving-part continuity.
7. Keep LOD art recognizable and compare actual native screenshots. Do not call a procedural Blender material a shipped TaCZ texture atlas.

Current Soul Storm and Discharge sculpt studies remain material/geometry prototypes. This study does not establish that either has completed its final texture work.

## Reproduce

Requires Python and Pillow. Put the three exact archives named in texture-study.json in a sibling references/ directory, then run audit_textures.py. Compare the produced hashes with the included snapshot. Source project URLs are in the JSON. Do not bundle extracted reference pixels into the AoA pack without the required asset rights.
