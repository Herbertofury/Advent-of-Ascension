# King BamBamBam: interrupt the healing loop

[Open his stats and illustrated boss loot](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.21.1&entity=aoa3%3Aking_bambambam) · [Prepare the encounter](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Boss-Entry-and-Token-Preparation-1.21.1) · [Original trophies and elite progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Trophies-Gold-Crafting-and-Elite-Encounters-1.21.1)

![King BamBamBam summon and gold-healing loop](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/king-bambambam-gold-loop-1.21.1.webp)

**Release scope:** normal King BamBamBam in Minecraft 1.21.1 / AoA 3.7.16.1. Selected released methods were inspected alongside pinned source. This is a source-derived field guide, not a completed live-combat test. The elite encounter and older releases require separate analysis.

## Prepare for a fight with several priorities

The released normal builder specifies **740 maximum health, 12 base projectile damage, 10 armour, 30 armour toughness and 1 knockback resistance**. Actual damage depends on difficulty, equipment, effects and other mods. Bring a sustainable weapon and its real ammunition/battery requirements, food, healing and room to reposition. Do not plan around pushing the boss away with every hit.

You need to manage the boss, his summoned minions and the gold objects created when those minions die. Those objects can undo your progress if you ignore them.

## The most important mechanic: gold is returning health

The three inspected summon variants are **Little Bam, Piglin Brute and Embrake**. Their encounter-specific death-loot overrides each create **three special gold objects** drawn from a list of gold tools, armour, ingots and nuggets. These are not ordinary collectible drops from naturally spawned creatures.

1. Watch where a summoned minion dies.
2. Once a gold object's age exceeds **60 entity ticks**, its special movement logic pulls it toward the boss. This is a source threshold, not a guaranteed three-second wall-clock window on a lagging server.
3. A player in the object's expanded detection box can intercept it: the object is discarded. The box expands by 0.75 horizontally and 2 vertically; it is not a spherical pickup radius.
4. If the object reaches the boss first, it requests **50 healing and 30 energy**, then disappears. Normal health and energy caps still apply.
5. The boss-distance test runs before the player-interception test. If both are satisfied on the same tick, the boss branch wins. Intercept away from him rather than waiting until the object is already touching him.

The boss reach check is **squared distance < 3.1**, approximately 1.76 blocks of ordinary distance. Do not misread it as a 3.1-block radius. The special item is marked never-pickup; walking through it is a denial mechanic, not a promise of gold in your inventory. Its damage handler also discards it, but whether a particular weapon can hit it reliably needs runtime testing.

**Practical tactic to test:** handle minions where you can see their resulting objects, then move across their return paths before resuming long damage windows on the boss. In multiplayer, assigning someone to interception may be more useful than having everyone ignore the objects and attack him continuously.

## Energy and the exhaustion opening

Energy starts at 100 and is clamped to 0–100. While not exhausted, the damage callback consumes the floored incoming callback damage amount from energy. The server AI adds one energy every fifth entity tick. Successfully spawned Little Bams, Piglin Brutes and Embrakes cost 20, 30 and 40 energy respectively.

At zero energy, the Rest behavior can start: it sets the exhausted flag, stops movement/navigation and clears the path memory. Its configured duration is 200 ticks, and its continuation check stops when energy reaches 100. On exit it clears exhaustion and refills energy. Gold returning during this phase can therefore shorten the opening by restoring energy.

Treat the exhausted pose as an opportunity to assess and attack, while still watching surviving minions, gold and projectiles. It is not a claim that all arena damage stops or that every animation frame is safe. Damaging him while exhausted does not drain energy through the normal damage callback, so do not assume hits permanently lock him in that state.

## Charged staff and fireballs

The staff charge uses a delayed action. Its activation checks for players in a forward-expanded region and can trigger a discharge explosion in front of him. Avoid treating standing directly in front of the charging staff as a free damage opportunity.

The Fireballs behavior requires the charged staff and no attack-cooldown memory. Its tick method waits until running time reaches 20, then attempts to spawn **two Sticky Fireballs per behavior tick**, launched upward with randomized horizontal motion. The behavior has a configured 200-tick duration and continues only while energy is nonzero. Its stop method clears the charge and sets a 60-tick attack cooldown.

This describes scheduler settings and spawn attempts, not a guaranteed total projectile count or exact safe interval. Successful ranged damage also increases the target's burning duration. Fire protection may help with fire-related consequences but is not proof of immunity to projectile impact, discharge damage or all minions.

## Minion cleanup and loot distinctions

The summoned variants are transient: their inspected tick handlers discard them when the boss is dead or their age exceeds 12,000 ticks, and they report that they should not be saved. Their damage filters also differ from ordinary wild creatures, including explosion protection. Do not assume another hostile mob will clear the summons for you.

Their special gold objects likewise are not saved and discard themselves if the boss dies. These encounter rewards must stay separate from the normal boss loot panel and from the wild Little Bam or Embrake loot tables. Winning the boss encounter can produce an original trophy through its separate released boss loot table; consult the trophy guide before altering its displayed entity with a spawn egg.

## Evidence and acceptance checklist

[Released methods, hashes, attributes and seven independent gold-interception branch cases](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/king-bambambam-combat-evidence-1.21.1.json) · [Pinned normal boss source](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/content/entity/boss/king_bambambam/KingBamBamBamEntity.java) · [Portrait/layout provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/king-bambambam-art-evidence-1.21.1.json).

Before certifying the restored encounter, test gold interception versus boss-first precedence, minion spawn rejection, player ownership/damage filters, rest interruption, projectile lifetime, multiplayer targeting, save/reload cleanup and measured performance. Preserve the encounter rather than deleting its healing objects or reducing summon behavior merely to make it easier to render.

AoA artwork and behavior are credited to Tslat and contributors. Diagram and explanatory text are independent documentation.
