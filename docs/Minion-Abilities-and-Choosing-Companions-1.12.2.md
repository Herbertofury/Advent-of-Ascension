[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Creation slabs and forge](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Creation-Minions-Slabs-and-Forge-1.12.2) · [Bestiary](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Bestiary)

# Choose a minion: abilities, costs and combat limits

> Historical Minecraft 1.12.2 / AoA 3.3.6. All 22 slab minion classes were inspected for selected stat and behavior methods. Base values and effect requests are not measured DPS, survivability or compatibility guarantees.

## Pick a role before spending a slab

- For slowing targets, compare Compeer and Waggy’s successful-hit Slowness requests.
- For damage effects, compare Spraggy’s Poison, Shaddy’s Wither, and Craggy/Hellquin fire requests. Target immunity still matters.
- For healing support during combat, Blissard and Construct Of Servility request owner healing after successful hits. Healing Golem uses its own update-based path.
- For utility, Ender Carrier opens your existing Ender Chest; Alluricorn can trade a Kinetic Rune for a short Speed effect; Gnawer exchanges a supported fish and its own health for owner healing.
- Treat Goofer as risky: its special branch damages itself rather than the intended target.
- Compare ordinary melee companions by their base health and attack inputs, then test movement and target access. A larger number is not proof of a faster or safer companion.

[Summoning levels, Creation costs, sacrifice XP and exact slab recipes](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Creation-Minions-Slabs-and-Forge-1.12.2) are kept in the crafting/training guide. The bestiary cards link directly to both guides.

## Illustrated comparison

Health and melee below are literal base getter values. Movement is a scalar, not blocks per second. “Combat AI” reflects the released isHostile helper used by minion task setup; it does not mean hostility toward the owner. A dash for melee identifies the two utility classes that do not enable the shared hostile attack setup, rather than presenting the inherited -1 sentinel as negative damage.

| Reference | Companion | Base health | Base melee input | Move scalar | Combat AI | Checked behavior |
|---|---|---:|---:|---:|---|---|
| ![Draggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-DraggyModel-thumb.webp) | [Draggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Adraggy) | 100 | 10 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Penguin reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-PenguinModel-thumb.webp) | [Penguin](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Apenguin) | 100 | 10 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Compeer reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CompeerModel-thumb.webp) | [Compeer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acompeer) | 20 | 5 | 0.3 | Yes | After a successful base melee attack, requests Slowness amplifier 1 for 40 ticks. |
| ![Waggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-WaggyModel-thumb.webp) | [Waggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Awaggy) | 110 | 10 | 0.3 | Yes | After a successful base melee attack, requests Slowness amplifier 1 for 80 ticks. |
| ![Spikeback reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-SpikebackModel-thumb.webp) | [Spikeback](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aspikeback) | 60 | 23 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Rammerhorn reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-RammerhornModel-thumb.webp) | [Rammerhorn](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Arammerhorn) | 210 | 11 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Spraggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-SpraggyModel-thumb.webp) | [Spraggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aspraggy) | 130 | 10 | 0.3 | Yes | After a successful base melee attack, requests Poison amplifier 1 for 80 ticks. |
| ![Plateosaur reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-PlateosaurModel-thumb.webp) | [Plateosaur](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aplateosaur) | 320 | 5 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Craggy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CraggyModel-thumb.webp) | [Craggy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acraggy) | 180 | 10 | 0.3 | Yes | After a successful base melee attack, calls setFire(5) on the target. |
| ![Hellquin reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/af80165e13329afc0ecd3324-thumb.webp) | [Hellquin](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahellquin) | 120 | 10 | 0.3 | Yes | After a successful base melee attack, calls setFire(7) on the target. |
| ![Horntail reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-HorntailModel-thumb.webp) | [Horntail](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahorntail) | 270 | 18 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Gnawer reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-GnawerModel-thumb.webp) | [Gnawer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agnawer) | 430 | 9 | 0.3 | Yes | An injured non-Creative owner can spend a supported fish to request healing; the minion loses the requested heal amount from its own health. |
| ![Shaddy reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ShaddyModel-thumb.webp) | [Shaddy](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ashaddy) | 200 | 10 | 0.3 | Yes | After a successful base melee attack, requests Wither amplifier 2 for 80 ticks. |
| ![Corby reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-CorbyModel-thumb.webp) | [Corby](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Acorby) | 200 | 11 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Blissard reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/b6f4a49e3cdde5a76dff43f6-thumb.webp) | [Blissard](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ablissard) | 100 | 11 | 0.3 | Yes | After a successful base melee attack, requests 2 health of healing for a resolved owner. |
| ![Ender Carrier reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-EnderCarrierModel-thumb.webp) | [Ender Carrier](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aender_carrier) | 100 | — | 0.3346 | No | Owner-only interaction opens the owner’s existing Ender Chest inventory. |
| ![Goofer reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-GooferModel-thumb.webp) | [Goofer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Agoofer) | 270 | 10 | 0.3 | Yes | One in six attack calls takes a self-damage branch instead of the ordinary target attack. Otherwise delegates to base melee. |
| ![Mecha Cyclops reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-MechaCyclopsModel-thumb.webp) | [Mecha Cyclops](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amecha_cyclops) | 100 | 30 | 0.3 | Yes | No attack, interaction or update override among the selected subclass methods; follows the shared minion behavior for those paths. |
| ![Alluricorn reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/1a393f6944f74716cbbe9a0c-thumb.webp) | [Alluricorn](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aalluricorn) | 200 | 13 | 0.3 | Yes | Owner interaction with a Kinetic Rune and no active Speed requests amplifier 3 for 150 ticks; consumes one rune outside Creative. |
| ![Construct Of Servility reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-ConstructOfServilityModel-thumb.webp) | [Construct Of Servility](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Aconstruct_of_servility) | 260 | 15 | 0.41618 | Yes | After a successful base melee attack, requests 2 health of healing for a resolved owner. |
| ![Healing Golem reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.16.5/1.16.5-model-HealingGolemModel-thumb.webp) | [Healing Golem](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Ahealing_golem) | 200 | — | 0.3 | No | While alive, tamed and with an injured resolved owner, its update requests 0.15 healing. No distance or server-side guard in this selected override. |
| ![Mecha Skellox reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/legacy-1.12.2/b3b8d8f47c3bdebe0aedc3b4-thumb.webp) | [Mecha Skellox](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.12.2&entity=aoa3%3Amecha_skellox) | 160 | 15 | 0.72 | Yes | Custom AI setup and travel override; base movement scalar 0.72. This does not by itself establish player riding or controllable flight. |

Existing portrait provenance is retained. Some thumbnails are matched later-version model references; they are not all claimed to be native 1.12.2 renders.

## Status effects after a successful hit

The selected status-effect overrides first call the shared attack method and only continue when it returns true. They then cast the target to EntityLivingBase for potion effects. Normal AI targets living entities, but unusual modded calls with a non-living target are an explicit compatibility test.

| Companion | Request | At healthy 20 TPS |
|---|---|---|
| Compeer | Slowness, amplifier 1, 40 ticks | Approximately 2 seconds |
| Waggy | Slowness, amplifier 1, 80 ticks | Approximately 4 seconds |
| Spraggy | Poison, amplifier 1, 80 ticks | Approximately 4 seconds |
| Shaddy | Wither, amplifier 2, 80 ticks | Approximately 4 seconds |
| Craggy | setFire(5) | Fire-duration argument 5 seconds before other behavior |
| Hellquin | setFire(7) | Fire-duration argument 7 seconds before other behavior |

Potion amplifiers are zero-based: 1 corresponds to the second strength tier, and 2 to the third. Effect acceptance, immunities, combining and later updates can change the result. Fire requests do not guarantee a particular amount of burn damage.

## Healing companions

**Blissard and Construct Of Servility** call the shared healing helper with 2 health after a successful base attack if their owner resolves. The helper only heals an entity that is alive, has positive health and is below maximum health. A full-health owner does not gain stored healing.

**Healing Golem** requests 0.15 health from its update while the golem is not dead, is tamed and its resolved owner is injured. This override does not perform a range check or an explicit server-side guard. Actual owner resolution, entity ticking and effect synchronization need runtime checks; do not advertise global healing or a guaranteed per-second total.

**Gnawer** accepts the inspected HealingFishFood class or vanilla ItemFishFood from its injured, non-Creative owner. It consumes one fish, requests owner healing, then reduces its own current health by the requested amount. It does not reduce that cost to the owner’s actual missing health. This can spend more minion health than the owner actually recovers.

The vanilla-fish branch shrinks the stack before calling the fish heal-amount lookup with that stack. Test single-item versus multi-item stacks and each fish metadata variant instead of assuming the final-item behavior is identical. Also test minion health below the requested cost, full-health owners and Creative owners.

## Utility interactions

**Alluricorn:** the player must match a resolved owner, hold a Kinetic Rune and have no active Speed effect. Outside Creative, one rune is consumed. The request is Speed amplifier 3 for 150 ticks, approximately 7.5 seconds at 20 TPS. An existing weaker Speed effect still blocks this selected branch. The inspected override does not supply its own explicit server-only guard; side/cost synchronization is a test target.

**Ender Carrier:** the owner UUID check opens that player’s Ender Chest. This is the same personal inventory, not proof of extra portable storage slots or a separately saved inventory on the minion.

## Goofer’s self-damage branch

Goofer draws nextInt(6). On zero it attacks itself using its current attack-damage attribute as the damage input, returns true, and does not delegate to the ordinary target attack. On the other five outcomes it delegates to the base attack.

The one-in-six figure is conditional on this attack method being called. Self-damage still passes through damage handling, so it is not a guaranteed exact health loss. A true return value here does not mean that the intended target was damaged.

## Mecha Skellox movement

Mecha Skellox declares a 0.72 base movement scalar, compared with 0.3 for most slab companions; Construct Of Servility uses 0.41618 and Ender Carrier 0.3346. These are attribute inputs, not measured world speed.

Its AI setup includes follow-owner parameters distinct from the generic base setup and it overrides the large travel method. That method contains water, lava, ground and Elytra-state branches. Merely finding those branches is not proof that the player can mount it, give it usable wings or control flight. Pathfinding, collisions, stepping, fluids and other movement mods need dedicated validation.

## Shared attack details and test checklist

The shared base attack reads the current attack-damage attribute, casts it to an integer and then to float before making the damage call. Fractional modifiers can therefore be truncated on that selected path. Goofer’s self-damage branch instead casts the attribute directly to float. Base getter comparisons alone do not describe these later differences.

- Test successful versus rejected base attacks before expecting status effects or owner healing.
- Test effect-immune targets, existing stronger/weaker effects and fire immunity.
- Test owner online/offline, injured/full/dead states and nearby/distant loaded minions.
- Test Alluricorn and Gnawer interactions with one-item/multi-item stacks, both hands and Creative.
- Test ordinary fractional damage modifiers against the base integer cast and Goofer’s separate float cast.
- Keep Hunter gating, ownership, lifespan and ordinary-drop checks from the [Creation guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Creation-Minions-Slabs-and-Forge-1.12.2) and [Hunter guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Hunter-Requirements-and-Training-1.12.2).

## Evidence

[106 selected released methods and declared-method inventories](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minion-ability-evidence-1.12.2.json) · [Readable companion catalog](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minion-ability-catalog-1.12.2.json)

Twenty-two classes, twenty combat-AI declarations and two utility-only declarations are covered. Absence of a selected subclass override is not a claim that external mods cannot add behavior. No Java or Minecraft code was executed.

[Pinned official source context](https://github.com/Tslat/Advent-Of-Ascension/tree/29dd8a8a20642ee182b851e34ef58b65f68e68bf/source). AoA portraits and systems: Tslat and contributors.
