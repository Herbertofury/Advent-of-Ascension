# Soul Storm: soul-flame aiming sight

**Owner correction, 18 October 2026:** Soul Storm's default aiming/crosshair motif is an animated soul flame. The prominent gem in earlier concepts remains an optional attachment, not the default. Keep every earlier concept available.

## Three swappable sights

| Sight | Role and appearance | Animation direction |
|---|---|---|
| Soul Flame | Default: a free, living cyan-blue soul flame above the sight mount | Wisps curl and breathe around a stable aiming reference; gentle response to charge and firing |
| Soul Candle | Optional: a small sculpted candle holding a spectral flame | Candle stays fixed; flame animates independently with restrained flicker |
| Soul Gem | Optional: a mounted soul crystal, preserving the older concept direction | Subtle internal soul motion and glow; optional pulse on accepted firing events |

The sight is mounted to the weapon. Any matching HUD reticle is a separately configurable presentation option. Do not replace the flame with a fixed gem while calling it the default flame variant.

## Aim must remain reliable

The animated flame is presentation around a stable aim reference. Its changing tip must not alter the authoritative firing direction or make the true center impossible to read. ADS alignment, projectile spawn, camera convergence and obstruction checks require actual in-game tests. Offer restrained-glow and reduced-animation settings; keep a precise center marker available.

Keep wisps out of the target sightline, budget alpha overdraw and avoid attaching an uncontrolled dynamic light to each flame. Test dark and bright scenes, different FOVs, moving targets, recoil, all supported barrel modules and left/right-hand modes. Sight switching updates the resolved assembly and preview without losing saved skins or decals.

These are required designs, not completed native attachments. Earlier gem-forward illustrations are preserved as optional Soul Gem studies. New default renders should show the animated-flame concept explicitly.

[Soul Storm profile](Soul-Storm-Weapon-Profile) · [Art direction](Soul-Storm-Art-Direction) · [Alternate barrels](Alternate-Barrels-and-Skins)

## Sight concept sheet

![Soul Flame default; Soul Candle and Soul Gem optional](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-sight-concepts-v1.png)

The lower strip illustrates animation key poses, not an actual animation clip. The first-person vignette is generated concept art, not in-game capture or proof of aim alignment.

[Source-backed native renderer plan](Soul-Flame-Native-Renderer-Plan) explains the actual functional-bone hook, hidden-node caveat and required runtime tests.

[Original playful inspection storyboard](Soul-Storm-Inspection-Storyboard).

[Original animated flame texture study](Soul-Flame-Flipbook-Study) includes editable source, fifteen rendered frames, UV tests and clean-extraction pixel reproduction; native integration remains pending.


[Controlled aiming-transition correction](Soul-Storm-Aiming-Flame-Readability) follows the flame mask through 101 sampled frames and preserves relaxed/full-focus renders. [Coordinated effect storyboard](Soul-Storm-Effects-Storyboard) covers the wider proposed feedback; both retain native acceptance gates.

## Editable optional-sight study

[Flame, Candle and Gem workshop](Soul-Storm-Optional-Sight-Workshop) includes the source patch, closeups, clean rebuild and preservation evidence. These authoring variants still require artistic and native acceptance.
