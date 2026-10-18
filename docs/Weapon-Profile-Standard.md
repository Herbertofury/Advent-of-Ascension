# Complete weapon profile standard

Every weapon needs a readable explanation, not just a stat table or attractive render.

## Explain the weapon

- What it is and its distinctive fantasy, silhouette and original identity.
- How the player uses it: press/hold, charge, cadence, alternate modes and recovery.
- What it fires: projectile class/appearance, count, trajectory, spread, speed and lifetime where verified.
- What happens on impact: damage type/value, direct versus splash, status effects, terrain interaction, ownership and special conditions.
- Its ammunition or magical resource, costs, capacity/durability and applicable modifiers.
- Strengths, weaknesses and quirks, distinguishing gameplay observations from code-based expectations.
- Acquisition, version availability, enchantment/attachment interactions and relevant dependencies when verified.

## Compare old and new

Show the original item art and actual projectile/impact assets or clearly labeled source-derived reconstruction. Never label generated concept art as an original game screenshot. Place the proposed premium design beside it, with its gameplay intention and meaningful attachment variants.

Keep separate columns for original released-file values, proposed upgraded values and measured native results. Explain units, version/build hashes, formulas and uncertainty. A base damage constructor input is not measured damage against every target; a theoretical rate is not benchmarked DPS.

## Acceptance evidence

Pin source and released artifacts. Describe exactly what was inspected. Link concept art, original authoring files, scoped geometry/animation tests and actual runtime evidence when available. No numeric QA pass can substitute for visual quality, and no concept image certifies a completed mod.


## Trace effective behavior, not only constructor numbers

For each profile, distinguish (1) a registration/constructor input, (2) the value or action reached through inherited and overridden methods, and (3) measured behavior in the actual game. Record the call chain and its conditions before presenting a value as gameplay truth.

The released Discharge Shotgun is a useful regression case:

- Its zero base-damage input does not mean zero damage: the impact path requests explosions.
- With the normal weapon/living-owner conditions, the entity-hit handler calls the weapon impact method and then the projectile impact method. Their separate strength inputs must not be summed into a fictitious radius or guaranteed damage result. Block-hit behavior differs.
- A stored recoil input of 13 is not an effective camera angle. The inspected inherited recoil getter returns 0.35 and its shot calculation has a zero-base-damage branch.
- A lifespan input of 4 is not sufficient to claim an exact four-tick travel time: inspect the comparison, increment order and superclass tick before stating a bound. Actual distance additionally needs movement and collision verification.
- A resource or LOD name in a display file does not prove the referenced asset exists or is selected at runtime. Resolve it from the actual pack and record fallback/override uncertainty.

Add these distinctions to automated source checks where possible, preserve the original call ordering in compatibility mode, and require native regression tests before changing gameplay. [Discharge Shotgun evidence and profile](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Discharge-Shotgun-Weapon-Profile).
