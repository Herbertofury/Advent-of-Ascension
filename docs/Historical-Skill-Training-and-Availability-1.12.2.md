[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Skills and progression](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Skills-and-Progression) · [Tutorial library](https://herbertofury.github.io/Advent-of-Ascension/tutorials.html?v=1.12.2)

# Historical skill training: what to do, and what remains inactive

> Minecraft 1.12.2 / AoA 3.3.6 only. This map joins the checked historical guides and a bounded released-class audit. It is not a promise that every named skill is fully playable, nor a runtime acceptance result for your restored build.

![Fifteen historical skill icons and checked training routes](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/historical-skill-training-map-1.12.2.webp)

## Choose the actual training action

Use the action column first, then open the matching walkthrough for eligibility, recipes, costs and known limits. A GUI icon, skill level field, retained armor class or XP tooltip is not enough to establish a working gameplay loop.

| Skill | Checked action or current limit | Full walkthrough |
|---|---|---|
| Alchemy | No dedicated ordinary training action located in the scoped released reference scan. | Bounded audit below |
| Anima | Harvest eligible plants, collect temporary Anima Stones or use eligible fragment-growth actions. | [Collect plant pickups](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Anima-Training-and-Fragments-1.12.2) |
| Augury | The selected released Ascension Shrine activation is inactive; retained essence XP fields are not a working training action. | [Shrine inactive](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Augury-and-Ascension-Shrine-1.12.2) |
| Butchery | Eligible melee hurt events can produce temporary Bloodlust; collect it for the XP request. | [Collect Bloodlust](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2) |
| Creation | Use a qualifying minion slab at a Creation Forge; summoning spends resource and is a different action. | [Sacrifice slabs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Creation-Minions-Slabs-and-Forge-1.12.2) |
| Engineering | No dedicated ordinary training action located in the scoped released reference scan. | Bounded audit below |
| Expedition | Sprint while grounded and eligible at player-age tick multiples; walking alone is not the selected action. | [Sprint on eligible ticks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Expedition-Sprinting-Bonuses-and-Falls-1.12.2) |
| Extraction | Use the checked device/bowl route and its success/reward conditions. | [Use the lava device](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Extraction-Device-and-Skill-Rewards-1.12.2) |
| Foraging | Follow the inspected block-break gates and reward/XP functions; not every broken block guarantees XP. | [Break eligible blocks](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2) |
| Hauling | Follow the historical rod, catch and reward-table route, including Forge fishing-hook context. | [Fish with the rod](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Fishing-Hauling-and-Boxes-1.12.2) |
| Hunter | Use registered Hunter creatures with suitable player-linked death credit; ordinary drops have separate gates. | [Defeat eligible targets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2) |
| Infusion | Harvest Pixons and convert eligible Infusion Stones; shipped Infusion crafting recipes do not declare XP. | [Harvest or convert stones](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Infusion-Pixon-Harvesting-and-Stones-1.12.2) |
| Innervation | Eligible kills can produce temporary Heart Stones; XP collection and successful healing are separate. | [Collect Heart Stones](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Butchery-Innervation-and-Combat-Pickups-1.12.2) |
| Logging | Follow the log-break gate, reward calls and copy branch rather than assuming a guaranteed reward per log. | [Break eligible logs](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Foraging-and-Logging-Rewards-1.12.2) |
| Runation | Use the exact four-post shrine layout and accepted inputs; missing first post enters the practice branch. | [Use matching rune posts](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runation-Rune-Shrines-and-Inputs-1.12.2) |

## Alchemy and Engineering: do not invent a training recipe

The released artifact retains both skill enum values, GUI/display support and armor classes that return their skill and level-100 requirement. Those declarations alone do not prove an active brewing, machine-building or crafting XP route.

The direct-reference audit scanned all **3,451 shipped AoA classfiles** under net/tslat/aoa3 for field references to Skills.ALCHEMY and Skills.ENGINEERING. It found seven referencing classes and ten methods:

- Four generated switch-map classes used by the player tab, skills renderer, XP-particle renderer and level-requirement toast.
- AlchemyArmour and EngineeringArmour: their getSkill and tooltip methods.
- The Skills enum’s initialization and ID lookup.

No dedicated training callback appears in that direct named-reference result. A separate case-insensitive text search over shipped recipe and loot JSON resources found zero Alchemy/Engineering matches in their paths or contents.

**Search boundary:** generic enum iteration, generic XP calls, reflection, runtime configuration and external mods can address a skill without a direct named reference. This is a reproducible bounded negative result, not proof of all possible runtime behavior. The retained armor classes were inspected as class definitions; this page does not infer a registered, craftable or obtainable armor set solely from their presence.

Accordingly, this wiki does not tell you that ordinary brewing trains historical Alchemy or that building machinery trains historical Engineering. A restored implementation needs a real acquisition/training/benefit loop and tests before those instructions can be added.

## Augury has a different, directly inspected limitation

The checked released Ascension Shrine activation method is inactive. Essence objects and their XP fields remain, but there is no corresponding working shrine conversion in that selected callback. Earlier source contains a different historical route; that does not make it active in AoA 3.3.6.

Read [Augury and the Ascension Shrine](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Augury-and-Ascension-Shrine-1.12.2) for the exact release distinction, retained essence references and restoration targets. Do not substitute an older wiki recipe into the current historical walkthrough without checking the artifact.

## Common training mistakes to avoid

- **Creation:** summoning spends Creation resource and a slab; the checked skill-XP action is sacrificing a slab at the forge.
- **Infusion:** Pixon harvesting and stone conversion have XP paths. The 386 shipped historical Infusion crafting recipes do not declare infusion_xp; crafting a recipe is not automatically the same training loop.
- **Butchery:** Bloodlust attempts follow eligible melee hurt events, not only kills. Collecting the temporary pickup matters.
- **Innervation:** Heart Stone XP collection and successful healing are separate; a full-health player can still follow the XP path.
- **Expedition:** player-age tick boundaries and grounded sprint eligibility matter. Distance walked is not the selected XP counter.
- **Hunter:** attack permission, death XP and ordinary loot eligibility are separate checks, especially for tameable kill credit.
- **Runation:** a missing first rune post can consume accepted inputs through the practice branch. Check the full layout before bulk use.

## Skill Crystals are not a universal starting solution

The inspected historical crystal selector chooses the lowest eligible displayed skill at level **15 or higher**, with enum-order tie breaking. It does not automatically target a level-1 inactive skill. Other eligibility and level-cap rules also apply.

Use the [Skill Crystal walkthrough and planner](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Reward-Boxes-and-Skill-Crystals-1.12.2) to inspect the exact target before spending a crystal. Generic XP support is distinct from a normal gameplay path that earns the initial levels.

## Restoration acceptance for a missing skill loop

Before promoting a retained skill to an active tutorial, require evidence for:

1. A reachable action that awards the intended skill, including server-side eligibility, actual input consumption and failed-action behavior.
2. A legitimate level-1 starting route and an explicit progression curve, rather than requiring commands or a minimum-level crystal as the only bootstrap.
3. Obtainable stations, ingredients and rewards in the target release, with illustrated recipes or acquisition instructions.
4. Benefits that have implemented callbacks and match their tooltips, including equipment transitions and configuration-disabled behavior.
5. Save/reload, multiplayer, compatibility and measured performance checks on the target build.

These are documentation and acceptance requirements, not claims that the restoration has already been implemented.

## Evidence

[Direct-reference audit and artifact fingerprint](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/retained-skill-evidence-1.12.2.json) · [Training-route index](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/skill-availability-routes-1.12.2.json) · [GUI crop provenance](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/skill-availability-art-evidence-1.12.2.json)

The individual linked guides retain their own released-method evidence and limits. Fifteen source GUI icons are used in the overview. Java and Minecraft code were not executed.

[Pinned official source context](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source). AoA artwork and systems: Tslat and contributors.

[Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix) · [Runtime acceptance](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Runtime-Acceptance-Checklist) · [Restoration roadmap](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Roadmap)
