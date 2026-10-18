> **Conceptual design reference, not a real-world construction guide or a claim of in-game implementation.**

# Weapon physics & speculative technology research

Reviewed 2026-10-18. Refresh program status before calling a technology current or fielded. Keep real-world discussion at explanatory level: no fabrication, performance optimization, targeting instructions or build specifications.

## Physical rules translated into animation
- Momentum does not vanish because propulsion is electromagnetic. Show a consistent recoil/recovery story for projectile weapons; label fantastical recoil cancellation as fiction.
- A heavy component should read as heavy through acceleration, settling, hand support and sound. Camera kick is an aesthetic signal, not a physics simulation.
- Resource and energy accounting must be legible: storage, conversion, emission and waste heat. A glow alone does not explain unlimited output.
- Different mechanisms need different visual language: a light beam is not a slow solid tracer; radio energy need not resemble lightning; plasma is not simply a laser with a different color.
- For stylized beams, arcs and visible charge effects, explicitly call them game feedback. A magical AoA weapon can break physical rules consistently if its rule is stated.
- Suppressors in the game reduce sound/flash cues according to configured gameplay rules; avoid presenting total silence as physical realism. Sound, projectile effects and magical discharge are distinct channels.

## Demonstrated and experimental inspiration
1. Laser directed energy: UK MoD reported DragonFire drone trials on 20 November 2025 and planned naval delivery from 2027. This is evidence of a program/test and future plan, not a handheld or universally deployed system. Game translation: charge readiness, heat-limited sustained beam and a readable emitter; keep any portable AoA version explicitly fictional. Source: https://www.gov.uk/government/news/boost-for-armed-forces-as-new-laser-weapon-takes-down-high-speed-drones
2. Radio-frequency directed energy: UK MoD reported a drone-swarm demonstrator trial on 17 April 2025. Game translation: a clearly telegraphed disruption pulse with eligible fictional enemy tags and limits; do not infer that every mob is electronic or vulnerable. Source: https://www.gov.uk/government/news/british-soldiers-take-down-drone-swarm-in-groundbreaking-use-of-radio-wave-weapon
3. Electromagnetic launch: ONR's 2010 railgun demonstration is historical evidence, not proof of present deployment. Game translation: a charging sequence, visible power state and recovery/thermal constraints, rather than treating an electromagnetic gun as recoil-free. Source: https://www.onr.navy.mil/media-center/news-releases/navy-sets-new-world-record-latest-electromagnetic-railgun-demo
4. Practical limits: GAO's 2023 overview highlights atmospheric/cooling limitations and the gap between demonstrations and adoption. Use these to inspire trade-offs, not arbitrary engineering claims. Source: https://www.gao.gov/products/gao-23-106717

## Explicitly fictional concepts
Dimension-folded magazines, soul-bound rounds, self-returning ammunition, stable free-flight plasma bolts and gravity-cancelled recoil are creative proposals, not verified emerging products. Give each a supply rule, cost, readable limitation and state machine. Do not cite a laboratory plasma result as proof of a portable plasma weapon.

## Evidence discipline
Prefer official program statements, scientific institutions and original authors. Record publisher, date, exact URL, what was read, observed claim, maturity, uncertainty and game-design inference separately. Manufacturer/publicity claims are claims, not independent certification. Do not assume that newest means best. Downloaded source is not executed evidence. Check licenses before asset/code reuse.

For production art rather than operating mechanics, use Atomhawk's credited Helldivers 2 work: https://atomhawk.com/project/helldivers-2/
For grounded fictional props and historical context, use Royal Armouries: https://royalarmouries.org/objects-and-stories/stories/m-41a-aliens-pulse-rifle

## AoA implementation decisions

- Preserve native resource behavior before choosing the visual supply system.
- Separate established physical concepts from artistic exaggeration and explicit magic in every weapon brief.
- Require a cutaway and hand-clearance review before surface polish.
- Let modular parts change the same documented mechanism, not bypass it invisibly.
- See [Weapon mechanism and animation QA](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Mechanism-and-Animation-QA) and [Modular armory and effect salvage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Modular-Armory-and-Effect-Salvage).

## Additional primary science and current-program checks

- [NASA rocket principles](https://www.grc.nasa.gov/WWW/k-12/TRC/Rockets/rocket_principles.html) explains action/reaction and momentum. Applying that general principle to fictional projectile recoil is our design inference, not NASA validation of this weapon.
- [DOE plasma confinement](https://www.energy.gov/science/doe-explainsplasma-confinement) explains why controlled hot plasma requires confinement. It does not establish free-flying game-style plasma bolts. Give AoA plasma a stated magical containment rule instead of pretending fusion research proves the asset realistic.
- [ATLA Ground Systems Research Center](https://www.mod.go.jp/atla/en/rikusouken.html) lists electromagnetic railgun research. This is a more recent active-research reference than the historical ONR demonstration, but a research listing alone does not prove operational deployment.
