# Soul Storm inspection: A Little Soul

An original playful inspection proposal using Soul Storm's **default animated Soul Flame** sight. This is our own storyboard, not a COD animation reconstruction or native game capture.

![Revised inspection storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-inspect-storyboard-v2.png)

## The moment

1. **Invitation:** hold the weapon securely and open the free palm beside the sight flame.
2. **Curiosity:** a small expressive wisp peeks out of the flame.
3. **Reveal:** it floats above the palm while the soul chamber continues its gentle motion.
4. **Play:** it loops around the chamber; fitted emitters glow in sequence without firing.
5. **Return:** it curls back into the flame.
6. **Ready:** temporary effects clear and the weapon returns to its normal ready pose.

Use the fitted emitter count rather than hardcoding four for five/six-emitter upgrades. Candle and Gem variants require their own appropriate emergence/return poses. The sight variant and attachment revision are part of the inspection's input.

## Art QA and preservation

The [first storyboard](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/soul-storm-inspect-storyboard-v1.png) is retained. It placed the supporting hand too far forward under the bridge while leaving the intended rear grip visibly empty. Revision 2 brings the hand toward the actual grip. It is still concept art: hand contact, full-size fingers, every pose transition and attachment clearance require a consistent 3D model and native camera review before acceptance.

## Safe presentation behavior

The proposed short timing sketch is 4.5 seconds, with beats at 0, 0.7, 1.4, 2.3, 3.7 and 4.5 seconds. These are editable design values, not final authored animation timing.

Attack, weapon swap or assembly change must cancel cleanly. The inspect must not consume Spirit, heal, spawn damaging shots, reset firing cooldowns or advance gameplay muzzle parity. A long frame stall should jump to the appropriate presentation state and clear stale temporary effects rather than replay every missed flourish in one frame.

## Reproducible standalone helper study

[Original helper source and tests](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/inspection-customization-design-study.zip) · [Hash and test receipt](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/inspection-customization-design-study-evidence.json)

- The customization helper checks namespaced identities, earned charm eligibility, declared effect channels, finite decal settings and immutable output snapshots. Fourteen standalone checks pass.
- The inspection helper checks equal normal-rate beat sequences at four step sizes, two stall cases and seven cancellation points, plus pause, assembly changes and single cleanup behavior.
- **Not included:** Minecraft/Forge/TaCZ adapter, actual pose blending, input interception, multiplayer, persistent unlock storage or native cleanup implementation. Passing these tests does not make the weapon playable or prove zero performance regression.

[Sight variants](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Sights) · [Mastercraft/Mythic references](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mastercraft-and-Mythic-Animation-References) · [Full weapon profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Soul-Storm-Weapon-Profile)
