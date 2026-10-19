# Soul Storm optional sight workshop

[Weapon profile](Soul-Storm-Weapon-Profile) · [Sight design](Soul-Storm-Sights) · [Aiming-flame correction](Soul-Storm-Aiming-Flame-Readability)

![Default Soul Flame, optional Soul Candle and Soul Gem authoring closeups](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sight-variants-v35.webp)

## Three selectable designs

Soul Flame stays the default. Soul Candle adds a wax body, wick, drips and small soul-colored inlays, with an anchored cyan flame. Soul Gem uses a faceted crystal and luminous inner heart; a separate projected cue appears as focus increases. Both optional sights use the existing mount and retain the central aiming aperture.

These are editable Blender prototypes. The material finish and concept fidelity still need artistic acceptance. They are not installed TaCZ attachments, and the rendered closeups use different framing rather than matching apparent size.

## Rebuild and select

Download the [12 KB source patch](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-sight-variants-v35-patch.zip) and the existing [v33-R6 source scene](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-metal-texture-study-v33.zip). The included README gives exact build and verification commands. Blender 4.3.2 was used. The source scene hash is checked before modification; the input remains unchanged.

Scene property `sight_variant` selects `0` Flame, `1` Candle or `2` Gem. The helper validates selection and tags the dependency graph so scripted changes update immediately. Direct unsupported property values fall back to Flame. This authoring property is not yet a native game configuration option.

## Checks that actually ran

- Clean ZIP extraction, rebuild and three checks passed with Python errors configured to fail Blender's process.
- 404 flame/candle anchor samples over 101 frames per mode: maximum world-center error 0.00000067435.
- 101 gem focus-alpha samples; viewport/render visibility agreement and invalid-mode fallback.
- 14 new closed, positive-volume decorative solids. Flat flame cards and projection planes are intentionally excluded.
- All 438 original meshes preserve geometry, UVs, shape keys, ownership and 101 sampled evaluated geometry/visibility frames in default mode.
- Controlled frame-25 default/reference images were pixel-identical. A colored center marker remained visible for both optional sights at halfway and full focus.

[Machine-readable evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/soul-storm-sight-variants-v35-evidence.json)

## Quality issues caught during development

A stale dependency update could leave the wrong sight visible after a scripted selection. The helper now forces the required update. Gem mode originally retained stray flame filaments; it now hides them and uses its own focus cue. The manifest writer also caught an argument-name collision during a clean rebuild; this is fixed in the published source patch. The scene had saved before that error, which is why a saved scene alone was insufficient proof of a clean build.

The installed Blender build lacks OpenImageDenoise. The attempted denoised pass was rejected; these final closeups use 256 samples without denoising. Earlier studies remain available separately.

## Still required before release

- Artistic/concept-fidelity review of the complete weapon, sight proportions and material finish.
- Actual TaCZ material/alpha/export binding, first-person camera and hand clearance across FOVs and transitions.
- Configuration persistence, multiplayer presentation, optional-mod compatibility and equivalent-work performance measurements.
- Continuous collision review: manifold checks do not prove that mounted decorative solids never intersect.

No ammo, damage, projectile or installed-game behavior changed. Native acceptance remains zero.
