[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Skills](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Bestiary](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bestiary)

# Creation: minion slabs, summoning and sacrifice training

> Historical Minecraft 1.12.2 / AoA 3.3.6. Released constructors and selected methods define this guide. It does not certify minion persistence, combat compatibility or a restored Enderloom build.

## Summoning and training are different actions

A slab has four separate values: summoning level, Creation-resource cost, sacrifice level and sacrifice XP. Spending Creation to summon a helper does not itself award Creation skill XP in the inspected BaseSlab use path. The checked training action is sacrificing a slab at a Creation Forge.

![Exact Creation Forge recipe and separate summon/sacrifice actions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/creation-forge-recipe-and-actions-1.12.2.webp)

## Craft and use the Creation Forge

1. Craft a Creation Forge from **7 Ancient Rock, 1 Blank Slab and 1 Blaze Powder**, arranged as shown above. [Open the exact illustrated recipe](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ablocks%2Ffunctional%2Futility%2Fcreation_forge).
2. Choose an available slab whose sacrifice level you meet. Keep any slabs you want to summon separate from those you intend to spend on training.
3. Hold the slab and use the forge. On the server, a qualifying activation consumes **one slab**, except in Creative mode, and requests the slab’s sacrifice XP.
4. The selected handler does not summon a minion or require Creation resource for sacrifice. It checks the skill requirement and uses the shared XP system.
5. Review XP settings first. With skills disabled, the effective-level getter returns 100, but the XP helper exits; a qualifying non-Creative sacrifice can therefore consume a slab without awarding XP. This is a code-derived test target, not a recommended training setup.

Creative mode prevents consumption at the forge but the selected handler still compares the effective skill level against the sacrifice requirement. That differs from the explicit Creative level bypass in slab summoning.

## Summon a minion

The server-side slab-use method checks the summoning level, then counts your owned AoAMinion entities inside your bounding box expanded by 30 blocks on each axis. The released maxMinions default is **10**; your actual configuration can differ. This is a local bounding-box query, not a guaranteed global count across all chunks or dimensions.

Creative bypasses the summoning level/resource payment and item consumption, but the nearby-minion cap check remains before the Creative resource branch.

For an ordinary qualifying summon, the method consumes Creation resource with force=false, shrinks the held stack by one, then calls activateSlab. Each of the 22 inspected activators creates its matching minion, places it at the player, assigns that player as owner and calls world spawn.

**Payment precedes the spawn attempt.** The selected activators discard the spawn method’s boolean result and return the object. The base use method then returns success and plays its sound. A cancelled/failed spawn therefore needs an explicit item/resource rollback test; a success sound is not proof that a usable minion entered the world.

## Illustrated slab catalog

The Creation-level columns happen to match for these 22 released definitions, but are separate fields. Cost is resource payment; XP is the sacrifice request before shared modifiers. Portraits retain their existing bestiary provenance, including clearly scoped later-version model references.

| Visual reference | Minion and source card | Summon level | Creation cost | Sacrifice level | Base sacrifice XP | Recipe output / route |
|---|---|---:|---:|---:|---:|---|
| ![Draggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-DraggyModel-thumb.webp) | [Draggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Adraggy) | 1 | 100 | 1 | 20 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fdraggy_slab) |
| ![Penguin reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-PenguinModel-thumb.webp) | [Penguin](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Apenguin) | 1 | 120 | 1 | 9 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fpenguin_slab) |
| ![Compeer reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CompeerModel-thumb.webp) | [Compeer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acompeer) | 10 | 120 | 10 | 40 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fcompeer_slab) |
| ![Waggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-WaggyModel-thumb.webp) | [Waggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Awaggy) | 15 | 120 | 15 | 50 | [Recipe: 1 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fwaggy_slab) |
| ![Spikeback reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-SpikebackModel-thumb.webp) | [Spikeback](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aspikeback) | 16 | 140 | 16 | 220 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fspikeback_slab) |
| ![Rammerhorn reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-RammerhornModel-thumb.webp) | [Rammerhorn](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Arammerhorn) | 27 | 140 | 27 | 200 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Frammerhorn_slab) |
| ![Spraggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-SpraggyModel-thumb.webp) | [Spraggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aspraggy) | 30 | 140 | 30 | 200 | [Recipe: 1 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fspraggy_slab) |
| ![Plateosaur reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-PlateosaurModel-thumb.webp) | [Plateosaur](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aplateosaur) | 33 | 140 | 33 | 250 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fplateosaur_slab) |
| ![Craggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CraggyModel-thumb.webp) | [Craggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acraggy) | 45 | 160 | 45 | 400 | [Recipe: 1 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fcraggy_slab) |
| ![Hellquin reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/af80165e13329afc0ecd3324-thumb.webp) | [Hellquin](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahellquin) | 45 | 140 | 45 | 500 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fhellquin_slab) |
| ![Horntail reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-HorntailModel-thumb.webp) | [Horntail](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahorntail) | 54 | 160 | 54 | 2000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fhorntail_slab) |
| ![Gnawer reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-GnawerModel-thumb.webp) | [Gnawer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agnawer) | 60 | 180 | 60 | 2000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fgnawer_slab) |
| ![Shaddy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ShaddyModel-thumb.webp) | [Shaddy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashaddy) | 60 | 160 | 60 | 850 | [Recipe: 1 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fshaddy_slab) |
| ![Corby reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CorbyModel-thumb.webp) | [Corby](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acorby) | 63 | 120 | 63 | 3000 | L’Borean world-loot definition; see below |
| ![Blissard reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/b6f4a49e3cdde5a76dff43f6-thumb.webp) | [Blissard](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ablissard) | 70 | 180 | 70 | 2500 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fblissard_slab) |
| ![Ender Carrier reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-EnderCarrierModel-thumb.webp) | [Ender Carrier](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aender_carrier) | 70 | 130 | 70 | 1000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fender_carrier_slab) |
| ![Goofer reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-GooferModel-thumb.webp) | [Goofer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agoofer) | 74 | 180 | 74 | 500 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fgoofer_slab) |
| ![Mecha Cyclops reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-MechaCyclopsModel-thumb.webp) | [Mecha Cyclops](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amecha_cyclops) | 78 | 160 | 78 | 4500 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fmecha_cyclops_slab) |
| ![Alluricorn reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/1a393f6944f74716cbbe9a0c-thumb.webp) | [Alluricorn](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aalluricorn) | 80 | 180 | 80 | 4000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Falluricorn_slab) |
| ![Construct Of Servility reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfServilityModel-thumb.webp) | [Construct Of Servility](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_of_servility) | 83 | 180 | 83 | 3000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fconstruct_of_servility_slab) |
| ![Healing Golem reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-HealingGolemModel-thumb.webp) | [Healing Golem](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahealing_golem) | 90 | 200 | 90 | 4000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fhealing_golem_slab) |
| ![Mecha Skellox reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/b3b8d8f47c3bdebe0aedc3b4-thumb.webp) | [Mecha Skellox](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amecha_skellox) | 92 | 200 | 92 | 8000 | [Recipe: 4 slabs](https://herbertofury.github.io/Advent-of-Ascension/recipe-explorer.html?v=1.12.2&recipe=aoa3%3Ainfusion%2Finfusing%2Fslabs%2Fmecha_skellox_slab) |

### Infusion crafting is a third system

Twenty-one slabs have shipped Infusion recipe definitions. Each uses a Blank Slab in the separate base slot plus its listed ingredient entries. Waggy, Spraggy, Craggy and Shaddy recipes output one slab; the other seventeen indexed slab recipes output four.

These 21 definitions do not declare an infusion_level or infusion_xp field. Do not copy the slab’s Creation use level into a made-up crafting requirement. Follow [historical Infusion crafting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-and-Enchanting-1.12.2) for parser defaults, slot rules and XP behavior. Repeated ingredients need separate occupied ingredient slots under that recipe-matching system.

Corby has no output recipe in this selected recipe catalog. Its item is present in the released L’Borean world-loot supplies pool: weight 5, quality 2, quantity 1–4; the pool defines 0–2 rolls plus 0–1 bonus rolls. This resource declaration is not a flat per-kill drop percentage or proof that every creature in that dimension invokes the table. Other acquisition routes remain a separate audit.

## Ownership, lifespan and combat

- All 22 slab minion constructors pass lifespan **-1** to the base class. Its update only applies the age cutoff when lifespan is positive. This means no expiry from that selected timer; it does not mean immortal, always loaded or guaranteed to survive every save/migration.
- The selected base AI includes swimming, wandering, looking, following an owner and conditional hostile-target tasks. Individual subclasses can add behaviors. No breeding item is accepted by the base implementation.
- The base attack-class filter rejects AoAMinion subclasses. Player-owner Hunter requirements also gate target and revenge-target assignment. See [Hunter requirements and drop eligibility](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2) before assuming a minion bypasses progression or guarantees ordinary drops.
- The base invulnerability check accepts its superclass result or damage whose true-source UUID matches the owner UUID. This is not protection against every indirect hazard or unrelated attacker.
- Ownership persistence inherits Minecraft tameable behavior. This guide does not yet certify owner reconnect, unload/reload, dimension transfers or offline-owner behavior for all 22 classes.

### Two checked utility behaviors

**Ender Carrier:** interaction checks that the interacting player’s UUID equals the owner ID, then opens that player’s existing Ender Chest inventory. It is not a separately proven custom chest inventory carried by the entity.

**Healing Golem:** its selected update gets the owner and requests 0.15 healing when the golem is not dead, is tamed, the owner resolves and the owner is injured. The inspected method has no distance check or explicit server-only guard of its own. Do not turn that into a promise of unlimited-range healing or guaranteed healing per second; owner resolution, ticking, side effects and other mods require testing.

## Creation resource and armor

The selected regeneration path requests 0.033 Creation per eligible resource-regeneration call while the stored amount is below 200. The inspected Augury maximum-Creation helper returns 200. These helper values are not proof of an increased maximum from a retained level field or an unconditional per-second recovery rate.

The Creation full-set callback requests an additional 0.05 Creation per effect call. At slab activation, a recognized full Creation set can apply one of four equally selected effects to the returned minion: Speed, Strength, Regeneration or Resistance, each amplifier 1 for 1200 ticks with ambient and particle flags true.

The armor tooltip advertises a 30% Creation XP bonus, but the inspected CreationArmour class does not override addBuffs and the inherited AdventArmour implementation is empty. Treat that tooltip-to-callback mismatch as a restoration/test target; do not promise the bonus is active merely because the tooltip says so.

## Recovery and compatibility checklist

- Confirm actual maxMinions and test counts at 9/10/11, boundary positions, unloaded entities and multiple dimensions.
- Test insufficient level/resource, exactly enough resource, Creative, skills/resources disabled and full Creation armor.
- Cancel or reject the world spawn and check both the item stack and resource balance. The checked ordering does not provide a rollback guarantee.
- Test one-item and multi-item stacks, both hands, and forge use so training never accidentally becomes a summon.
- Test owner disconnect/reconnect, save/reload, chunk unload, dimension travel and owner transfer assumptions.
- Test Hunter-gated targets, friendly minions, owner damage, ordinary mob damage and player/pet kill-credit differences.
- Verify Healing Golem ticking/side behavior and Ender Carrier access by owner versus another player.
- Confirm Creation armor’s advertised XP bonus against actual XP, and validate regeneration/buff timing rather than inferring it from constants.

## Sources and limits

[90 released methods, slab values and recipe definitions](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/creation-minion-evidence-1.12.2.json) · [Recipe diagram provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/creation-minion-art-evidence-1.12.2.json)

22 slab classes were matched to their exact activated entity classes and existing creature-card references. Twenty-one slab recipes and one forge recipe are included. Selected behavior checks are static; Java and Minecraft code were not executed.

[Pinned official source context](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source). AoA assets/designs: Tslat and contributors; vanilla assets: Mojang.

[Infusion crafting](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Table-Crafting-and-Enchanting-1.12.2) · [Hunter training](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist)
