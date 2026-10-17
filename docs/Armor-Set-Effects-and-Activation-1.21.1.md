# Armor set effects and activation · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** Choose equipment for its effect, not just its defense number. This guide connects all **48 ordinary four-piece sets** to their worn previews and **100 released tooltip lines**. Every set has a source review, including explicit unresolved summoning paths for Rosidian and Spaceking.

[Search the Armor Atelier](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1) · [Base materials and durability](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Armor-Materials-and-Set-Preparation-1.21.1) · [Craft eight armor sets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Frame-Bench-and-Armor-Infusion-1.21.1) · [Special helmets](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Special-Armor-and-Skill-Helmets-1.21.1)

![Four armor studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-gallery-overview-1.21.1.webp)

## Read effects correctly

- **Released tooltip** records what the item tells a player. It is intended description, not independent proof that every code branch matches it.
- **Per-piece / full-set** labels below follow the actual tooltip headers. A general line has no preceding piece/set header in the inspected method; its activation condition must be read separately.
- **Checked callback** describes the inspected released method and its conditions. It does not certify every hook, damage tag, multiplayer state or private Enderloom build.
- Base armor, toughness, extra reduction and invulnerability are different mechanisms. Adding their displayed numbers does not produce a universal damage-block percentage.

## What counts as a set?

The player equipment system groups armor by material, tracks piece membership and separately records a `FULL_SET` marker. Its `perPieceValue` helper subtracts that marker before multiplying the piece count. Universal-compatible headpieces participate in full-set recognition, but this does not mean their own material container automatically adds every other set’s per-piece bonus.

Equipment-change events flag a refresh. The pre-player-tick path exits for dead/spectator players, refreshes changed equipment, checks equipment requirements, then calls the stored armor callbacks. That ordering matters for equip/unequip, skill requirements and reconnect testing. See the exact shared-method evidence rather than inferring behavior from appearance alone.

## A tooltip mismatch to check: Alacrity

The tooltip promises per-piece fall resistance. The released **partial-set incoming-damage callback has no fall-source check**: it tests absence of `FULL_SET`, then installs an armor-stage reduction using `equippedPieces.size × 0.2`. The full-set invulnerability callback separately checks `IS_FALL`.

This is a bounded implementation-versus-tooltip finding. It is not a measured damage exploit, a reproduced game bug or a fix already applied to the current candidate. Test one, two and three pieces with fall and non-fall sources, then compare the full-set case before deciding which behavior is intended. Do not advertise the tooltip as a verified complete description of that partial-set path.

## How the extra reduction helper works

The checked helper returns `existingReduction + (newDamage − existingReduction) × fraction`. A purely arithmetic example with damage-stage input 10, existing reduction 2 and fraction 0.2 gives reduction **3.6**, leaving **6.4** at that stage. Other armor, enchantments, resistance, tags and hooks can still change the final health loss. This example is not a game benchmark.

## Damage categories are not interchangeable

The released helper definitions distinguish melee, ranged, guns, energy and magic. In particular, **ranged excludes gun-tagged, energy-tagged and magic-classified projectile damage**. A ranged-armor tooltip does not automatically mean it buffs guns. Magic excludes poison, while environmental requires no source entity plus the environmental tag. Active tag membership and other mods can alter which sources qualify.

## Other important boundaries

- **Ghastly:** its ternary branch can reach the crouching scan on ticks that are not divisible by five. Do not claim a universal five-tick scan throttle. This is a static frequency-review target, not measured FPS loss.
- **Biogenic:** the full-set water branch writes air supply −10 while the tooltip promises underwater breathing. The outcome depends on the target engine and hooks; underwater behavior needs acceptance testing.
- **Rosidian and Spaceking:** no local summon callbacks were found, and the bounded direct-material-reference scan found no external activation reference. Their summon claims remain unresolved; the scan does not rule out every dynamic or external route.
- **Nightmare:** the armor subtraction alone keeps non-Distortion rune costs at a minimum of one. Stored staff charges and calls that disable buffs use different paths.

## Browse all 48 sets

The images use released textures and the checked neutral armor mesh. They do not reproduce glint, animation or an actual equipped player. Every card links its four inventory entries.

### Alacrity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-alacrity-1.21.1.webp" width="220" height="220" alt="Alacrity neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=alacrity)

**Released tooltip:**

- **Per-piece:** +20% Resistance to fall damage
- **Full-set:** Full immunity to fall damage

**Source review:** The full-set invulnerability callback checks the fall-damage tag. The partial-set incoming-damage callback checks only absence of FULL_SET before adding an armor-stage reduction; it has no fall-source guard in this method. Its lambda uses equippedPieces.size × 0.2.

*Tooltip/implementation scope mismatch requiring target-build review; no observed combat bug or applied fix.*

### Archaic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-archaic-1.21.1.webp" width="220" height="220" alt="Archaic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=archaic)

**Released tooltip:**

- **Per-piece:** The lower your health, the more melee damage you deal
- **Per-piece:** Increased incoming melee damage depending on health
- **Full-set:** No increased incoming melee damage

**Source review:** Outgoing melee damage input is multiplied by 1 + perPieceValue(0.1875) × (1 − wearer health fraction). Without FULL_SET, incoming damage input is separately multiplied by 1 + perPieceValue(0.16) × missing-health fraction. The partial-set vulnerability is a tradeoff; full-set recognition removes that particular incoming penalty.

*Released local callback review; helper and runtime limits retained*

### Baron

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-baron-1.21.1.webp" width="220" height="220" alt="Baron neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=baron)

**Released tooltip:**

- **General:** Extremely durable

**Source review:** The inspected class declares its constructor and durability tooltip, with no local effect callback. Its registered durability multiplier is 150 in the separate material evidence. High durability is established; an additional combat ability is not inferred from the name.

*Durability claim supported; no extra ability inferred*

### Battleborn

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-battleborn-1.21.1.webp" width="220" height="220" alt="Battleborn neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=battleborn)

**Released tooltip:**

- **General:** Attack speed increases while attacking
- **Per-piece:** Faster attack speed increases

**Source review:** Outgoing melee attacks by a ServerPlayer add perPieceValue(6) to an armor cooldown counter, capped at 300, then apply an ATTACK_SPEED modifier with amount min(0.65, counter/240) and ADD_MULTIPLIED_TOTAL. The tick callback refreshes on game-time multiples of 10 and removes at counter 1. Removing the last counted piece removes the modifier and retains 75% of a positive counter. Shared cooldown behavior and re-equip cleanup still need target-build testing.

*Released local callback review; helper and runtime limits retained*

### Biogenic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-biogenic-1.21.1.webp" width="220" height="220" alt="Biogenic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=biogenic)

**Released tooltip:**

- **General:** Slows melee enemies when hit, increasing with stronger hits
- **Per-piece:** Increased Slowness effect
- **Full-set:** Can see and breathe underwater

**Source review:** Full-set ticks in water write air supply −10. Water-at-eye level separately requests NIGHT_VISION with duration input 300; leaving that eye-fluid condition or breaking the set removes a night-vision instance only if its duration is at most 300. Positive melee damage from a living attacker requests slowness with duration input ceil(newDamage × perPieceValue(3)) and level input 2 when the EnumSet size is at least two, otherwise 1. The negative air write deserves underwater testing; it is not the Hazmat maximum-air restoration path.

*Negative air write requires underwater acceptance; no observed drowning outcome claimed*

### Boreic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-boreic-1.21.1.webp" width="220" height="220" alt="Boreic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=boreic)

**Released tooltip:**

- **General:** Explodes When Hit In Water
- **Per-piece:** Increased Explosion Damage And Radius
- **Full-set:** Also stuns nearby enemies briefly when exploding

**Source review:** Positive, non-environmental damage while the wearer is in water starts the boreicArmour explosion definition, passing equippedPieces.size. FULL_SET also selects probable enemies within radius input 4 and requests slowness with duration input 40 and level input 2. Explosion damage, block effects and ownership need the separate explosion definition; they are not guessed from this callback.

*Released local callback review; helper and runtime limits retained*

### Candy

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-candy-1.21.1.webp" width="220" height="220" alt="Candy neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=candy)

**Released tooltip:**

- **General:** Automatically consumes food when needed
- **Per-piece:** Reduced time between consumptions
- **Full-set:** Ignores consumption cooldown

**Source review:** A hungry ServerPlayer may auto-consume qualifying inventory food when FULL_SET is present or the armor cooldown is inactive. Food must report positive nutrition and saturation. The found item executes finishUsingItem and its returned stack replaces that slot. Successful use sets cooldown input 12000 / counted pieces. FULL_SET bypasses the cooldown gate in this method, so inventory-consumption behavior deserves explicit testing.

*Released local callback review; helper and runtime limits retained*

### Commander

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-commander-1.21.1.webp" width="220" height="220" alt="Commander neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=commander)

**Released tooltip:**

- **General:** Grants a Strength buff to all nearby allies
- **Per-piece:** +2 Blocks range
- **Full-set:** Strength effect increased

**Source review:** On wearer tick counts divisible by 20, the callback selects other living entities whose resolved player/owner is the wearer, within radius input perPieceValue(2). It requests DAMAGE_BOOST with duration input 25 and level input 2 for FULL_SET, otherwise 1. It does not buff every nearby creature or every teammate indiscriminately.

*Released local callback review; helper and runtime limits retained*

### Crystallis

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-crystallis-1.21.1.webp" width="220" height="220" alt="Crystallis neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=crystallis)

**Released tooltip:**

- **General:** Reflects damage back at melee attackers
- **Per-piece:** +25% Damage reflected
- **Full-set:** Effect also applies to ranged attackers

**Source review:** Positive damage from a living attacker must not bypass armor. Melee qualifies; ranged damage additionally requires FULL_SET. The callback requests thorns damage equal to newDamage × perPieceValue(0.25), then calls hurtArmor with generic damage input newDamage × 2. Reflection and durability loss are separate engine operations, not guaranteed final health/durability amounts.

*Released local callback review; helper and runtime limits retained*

### Elecanyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-elecanyte-1.21.1.webp" width="220" height="220" alt="Elecanyte neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=elecanyte)

**Released tooltip:**

- **General:** Taking damage regenerates Spirit
- **Per-piece:** Regenerate more Spirit per hit

**Source review:** Positive non-environmental damage to a ServerPlayer requests Spirit equal to newDamage × perPieceValue(2.5). Resource caps, resource modifiers and other callbacks still apply; this is not an uncapped Spirit balance guarantee.

*Released local callback review; helper and runtime limits retained*

### Embrodium

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-embrodium-1.21.1.webp" width="220" height="220" alt="Embrodium neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=embrodium)

**Released tooltip:**

- **Per-piece:** Increased Spirit regen while in hot environments
- **Full-set:** +25% Spirit regeneration at all times

**Source review:** Server-player tick callback reads Spirit per-tick regeneration (fallback 0.04). Full set adds 0.25×regen. Above ambient temperature 0.8, it additionally adds perPieceValue(0.25×regen)×min(1,temperature/2); only positive totals are submitted. This is an extra resource request, not a measured final recovery rate.

*Selected branch checked*

### Exoplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-exoplate-1.21.1.webp" width="220" height="220" alt="Exoplate neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=exoplate)

**Released tooltip:**

- **Per-piece:** Increased resistance when in darker environments

**Source review:** For non-environmental incoming damage in a ServerLevel, the callback computes light = clamp(2 + the queried light level, 2, 15). Its armor-stage reduction fraction is (1 − light/15) × perPieceValue(0.0625). It therefore depends on the checked light helper and is not a flat bonus in every location.

*Released local callback review; helper and runtime limits retained*

### Explosive

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-explosive-1.21.1.webp" width="220" height="220" alt="Explosive neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=explosive)

**Released tooltip:**

- **Per-piece:** +15% Explosion damage resistance
- **Full-set:** Full immunity to explosions

**Source review:** Incoming damage must match IS_EXPLOSION before adding an armor-stage reduction using perPieceValue(0.15). FULL_SET explosion-tag invulnerability is a separate callback. Other damage types are not covered by this local gate.

*Released local callback review; helper and runtime limits retained*

### Fungal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-fungal-1.21.1.webp" width="220" height="220" alt="Fungal neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=fungal)

**Released tooltip:**

- **General:** Has a chance to poison melee attackers when hit
- **Per-piece:** +20% Chance to poison
- **Full-set:** Can also poison nearby mobs when activated

**Source review:** Positive melee damage must pass RandomUtil.percentChance(perPieceValue(0.2)). A living attacker then receives a poison request with duration input 60 and level input 2. Inside that successful outer branch, FULL_SET plus a separate one-in-four helper roll requests level-input-1 poison on probable enemies within radius 5. The area roll is nested, not an unconditional 25% event on every hit.

*Released local callback review; helper and runtime limits retained*

### Ghastly

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghastly-1.21.1.webp" width="220" height="220" alt="Ghastly neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ghastly)

**Released tooltip:**

- **General:** Shows all nearby mobs while crouching
- **Per-piece:** +4 Blocks range

**Source review:** The tick condition branches to isShiftKeyDown only when tickCount % 5 == 0 and the wearer is a Player; otherwise it evaluates isCrouching. A true result selects probable enemies within perPieceValue(4) and requests GLOWING with duration input 6. The released branch therefore does not impose a universal once-every-five-ticks scan limit. Review crouching scan frequency and intended behavior before making a performance claim.

*Branch-frequency review target; no measured FPS or timing claim*

### Ghoulish

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghoulish-1.21.1.webp" width="220" height="220" alt="Ghoulish neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ghoulish)

**Released tooltip:**

- **Per-piece:** +10% Energy damage
- **Full-set:** 30% Reduced Spirit costs on weapons

**Source review:** The local outgoing callback multiplies energy-tagged damage input by 1 + perPieceValue(0.1). Separately, AoABlaster.getSpiritCost applies a full-set multiplier of 0.7 after Spirit/ammo enchantment adjustments. Non-player shooters, infinite-material consumption and weapon overrides have separate paths; this does not make every weapon 30% cheaper.

*Local damage and external cost routes checked*

### Hazmat

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hazmat-1.21.1.webp" width="220" height="220" alt="Hazmat neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hazmat)

**Released tooltip:**

- **Full-set:** Provides its own oxygen

**Source review:** FULL_SET plus air below maximum triggers setting air to maximum. The airtight helmet method separately calls PlayerUtil.isWearingFullSet for its material.

*Selected branch checked*

### Hydrangic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydrangic-1.21.1.webp" width="220" height="220" alt="Hydrangic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hydrangic)

**Released tooltip:**

- **Full-set:** Fertilizes plants when placed at the cost of durability

**Source review:** The armor class only supplies its tooltip; the effect is in PlayerEvents.onBlockPlace. It requires a ServerPlayer, the Hydrangic full set, a placed CropBlock and successful BoneMealItem.applyBonemeal. It then emits growth effects and calls hurtArmor with generic damage input 16. That input is not a claim of exactly 16 durability lost per item or guaranteed instant crop maturity.

*External planting route checked*

### Hydroplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydroplate-1.21.1.webp" width="220" height="220" alt="Hydroplate neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hydroplate)

**Released tooltip:**

- **General:** Naturally regenerate health while in water
- **Per-piece:** Increased healing speed
- **Full-set:** 20% Resistance to all attacks while in water

**Source review:** While in water, each armor tick requests healing of perPieceValue(0.0125). Separately, FULL_SET plus water plus non-environmental incoming damage installs an armor-stage fraction of 0.2. Healing caps and final damage depend on the engine and hooks.

*Released local callback review; helper and runtime limits retained*

### Ice

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ice-1.21.1.webp" width="220" height="220" alt="Ice neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ice)

**Released tooltip:**

- **General:** Armour repairs itself when in cold environments

**Source review:** Server-side inventoryTick requires numeric slotId 36–40 inclusive, a LivingEntity wearer, damage>0, random nextFloat<0.02 and ambient temperature<0.15. It then subtracts one damage point. These are callback gates, not proof that every engine inventory slot invokes this hook identically.

*Selected branch checked*

### Infernal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-infernal-1.21.1.webp" width="220" height="220" alt="Infernal neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=infernal)

**Released tooltip:**

- **Per-piece:** +15% Fire resistance
- **Full-set:** Full immunity to fire damage

**Source review:** Incoming damage must match IS_FIRE before adding a reduction with perPieceValue(0.15). Full-set fire-tag invulnerability is a separate callback. The reduction helper acts on remaining damage at its stage.

*Selected branch checked*

### Knight

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-knight-1.21.1.webp" width="220" height="220" alt="Knight neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=knight)

**Released tooltip:**

- **Full-set:** When below 20% health, gain extra strength

**Source review:** Each ordinary slot supplies +5 MAX_HEALTH using ADD_VALUE. The tick effect requires FULL_SET, a living wearer and health fraction below 0.2; it builds DAMAGE_BOOST with duration input 2 and level input 2. Maximum health is not the same as healing current health, and effect-builder inputs are not independently simulated here.

*Slot modifiers and low-health gate checked*

### Lunar

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lunar-1.21.1.webp" width="220" height="220" alt="Lunar neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lunar)

**Released tooltip:**

- **Per-piece:** Jump higher
- **Per-piece:** Reduces fall damage slightly

**Source review:** Each armor tick requests JUMP with duration input 2 and level input equal to counted pieces, marked ambient with hidden particles. EffectBuilder level semantics and actual jump motion are not independently simulated in this documentation.

*Released local callback review; helper and runtime limits retained*

### Lyndamyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyndamyte-1.21.1.webp" width="220" height="220" alt="Lyndamyte neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lyndamyte)

**Released tooltip:**

- **Per-piece:** +25% Chance to set melee attackers on fire
- **Full-set:** Sets fire to targets when meleeing

**Source review:** Retaliation requires positive new damage, server side, a melee source and a RandomUtil.percentChance call with perPieceValue(0.25); it requests five seconds of fire on the source entity. Full-set outgoing melee attacks separately request five seconds of fire on the target. External random-helper semantics and final immunity/hooks remain separate.

*Selected branch checked*

### Lyonic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyonic-1.21.1.webp" width="220" height="220" alt="Lyonic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lyonic)

**Released tooltip:**

- **General:** Attracts nearby dropped items
- **Per-piece:** +2 Blocks attraction range
- **Full-set:** Also attracts xp orbs

**Source review:** On even world-game ticks, the callback searches within perPieceValue(2.5), then pulls eligible entities with strength input 0.05. Nonempty item entities must have no pickup delay. FULL_SET also admits experience orbs and eligible embedded arrows; that arrow branch clears inGround, sets base damage to zero, nudges upward and marks motion for synchronization. It is not a promise to vacuum every item or hostile projectile.

*Released local callback review; helper and runtime limits retained*

### Mercurial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-mercurial-1.21.1.webp" width="220" height="220" alt="Mercurial neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=mercurial)

**Released tooltip:**

- **General:** Taking explosive damage grants resistance
- **Per-piece:** Increased resistance time
- **Full-set:** Increased resistance amount

**Source review:** After positive explosion-tagged damage, the callback requests DAMAGE_RESISTANCE with duration input perPieceValue(80), level input 2 for FULL_SET or 1 otherwise, marked ambient. It reacts after damage rather than proving immunity to the triggering explosion.

*Released local callback review; helper and runtime limits retained*

### Necro

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-necro-1.21.1.webp" width="220" height="220" alt="Necro neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=necro)

**Released tooltip:**

- **General:** Protects items from the user's inventory on death
- **General:** Prioritises hotbar items first
- **Per-piece:** +1 Item protected
- **Full-set:** Saves the wearer from a killing blow once per hour at the cost of durability

**Source review:** Before damage, FULL_SET can zero a non-environmental damage input that is at least current health when its cooldown gate permits. It calls hurtArmor with generic input 2000, raises health to 4 only if currently lower, and sets ServerPlayer cooldown input 72000. On a ServerPlayer death, a separate path requests storage of up to the counted-piece number of eligible inventory stacks, excluding Intervention and Vanishing Curse enchantments. Selection, storage return and save migration require their own acceptance tests; this is not guaranteed resurrection or preservation of a chosen item.

*Released local callback review; helper and runtime limits retained*

### Nethengeic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nethengeic-1.21.1.webp" width="220" height="220" alt="Nethengeic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=nethengeic)

**Released tooltip:**

- **Per-piece:** +10% Damage to targets on fire
- **Full-set:** +50% Damage if the wearer is on fire

**Source review:** With FULL_SET and the wearer on fire, outgoing damage input is multiplied by 1.5. If the target is on fire, a separate multiplication by 1 + perPieceValue(0.1) follows. Both conditions can apply sequentially. This local method has no melee-only gate, and final damage still passes through other hooks.

*Released local callback review; helper and runtime limits retained*

### Nightmare

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nightmare-1.21.1.webp" width="220" height="220" alt="Nightmare neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=nightmare)

**Released tooltip:**

- **Full-set:** Staves require 1 less of each Rune
- **Full-set:** Staves will no longer consume Distortion Runes on use

**Source review:** ItemUtil.findAndConsumeRunes enables the armor adjustment only when allowBuffs is true and the full set is recognized. After the rune-cost enchantment stage, the lambda removes Distortion Rune requirements and applies max(cost − 1, 1) to other runes; an ammo-cost enchantment stage follows. A one-rune requirement therefore does not become free from the armor subtraction alone. Infinite-material callers and stored staff charges can bypass this payment route.

*External rune-payment route and lambda checked*

### Omni

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-omni-1.21.1.webp" width="220" height="220" alt="Omni neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=omni)

**Released tooltip:**

- **Per-piece:** +10% Explosion damage
- **Full-set:** Creates an explosion when hit by a melee attack

**Source review:** Explosion-tagged outgoing damage input is multiplied by 1 + perPieceValue(0.1). Positive melee damage received with FULL_SET separately invokes the OMNI_ARMOUR explosion definition. The actual blast settings are outside this callback and are not assumed harmless to blocks or allies.

*Released local callback review; helper and runtime limits retained*

### Phantasm

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-phantasm-1.21.1.webp" width="220" height="220" alt="Phantasm neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=phantasm)

**Released tooltip:**

- **General:** Crammed full of clovers

**Source review:** Each ordinary slot supplies +1 LUCK using ADD_VALUE. That is an attribute increase, not a universal extra-drop percentage; the particular loot table must actually use luck for it to affect that outcome.

*Four slot-specific attribute modifiers checked*

### Poison

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-poison-1.21.1.webp" width="220" height="220" alt="Poison neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=poison)

**Released tooltip:**

- **Per-piece:** +25% Resistance to poison damage
- **Full-set:** Immunity to poison damage
- **Full-set:** Gives a brief defense boost when inflicted with poison

**Source review:** Poison-classified incoming damage receives an armor-stage fraction perPieceValue(0.25); FULL_SET separately grants poison-damage invulnerability. A full-set Poison effect-application attempt is rejected, and server-side code schedules a resistance request one tick later with duration input 60. Damage classification and effect-application events are distinct paths.

*Released local callback review; helper and runtime limits retained*

### Predatious

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-predatious-1.21.1.webp" width="220" height="220" alt="Predatious neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=predatious)

**Released tooltip:**

- **Per-piece:** +10% Ranged damage dealt
- **Full-set:** Deals minor Thorns damage to melee attackers

**Source review:** Ranged outgoing damage input is multiplied by 1 + perPieceValue(0.1). FULL_SET retaliation requires a melee source and a living direct attacker, then requests one point of thorns damage. Unlike several other retaliation callbacks, this inspected method contains no explicit positive-new-damage guard; test blocked-hit behavior rather than assuming identical gates.

*Released local callback review; helper and runtime limits retained*

### Primordial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-primordial-1.21.1.webp" width="220" height="220" alt="Primordial neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=primordial)

**Released tooltip:**

- **General:** Melee attackers suffering from wither deal less damage
- **Per-piece:** +15% Damage reduction
- **Full-set:** Effect not restricted to melee attackers

**Source review:** Incoming damage is reduced only when the source has a living attacker with Wither, and either FULL_SET is present or the source is melee. The event amount is multiplied by 1 − perPieceValue(0.15). The status is checked on the attacker, not on the wearer.

*Released local callback review; helper and runtime limits retained*

### Purity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-purity-1.21.1.webp" width="220" height="220" alt="Purity neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=purity)

**Released tooltip:**

- **Full-set:** Keeps The Wearer Clean From Physical Impairments

**Source review:** The inspected onEquip callback removes existing Weakness, Slowness, Mining Fatigue, Blindness and Nausea without a FULL_SET guard in that method. Separately, onEffectApplication requires FULL_SET before rejecting those five future effects. Clearing an existing effect on equip and preventing reapplication are distinct gates; verify transitions rather than treating a single piece as permanent immunity.

*Equip-time cleanup versus full-set prevention distinguished*

### Rockbone

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rockbone-1.21.1.webp" width="220" height="220" alt="Rockbone neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=rockbone)

**Released tooltip:**

- **Per-piece:** +10% Resistance to ranged damage
- **Full-set:** 10% Chance to dodge a ranged attack

**Source review:** Ranged incoming damage with FULL_SET first attempts RandomUtil.oneInNChance(10); success cancels the event. The achievement path additionally checks Projectile Protection level at least 4 on every worn armor slot. A non-cancelled ranged hit is multiplied by 1 − perPieceValue(0.1). The cancellation roll and advancement condition are separate.

*Released local callback review; helper and runtime limits retained*

### Rosidian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rosidian-1.21.1.webp" width="220" height="220" alt="Rosidian neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=rosidian)

**Released tooltip:**

- **Per-piece:** +4% Chance to spawn a friendly Rosid when hit
- **Full-set:** Guaranteed Rosid spawn when damaged 4 health or more

**Source review:** The released class declares only its constructor and tooltip; no local Rosid-spawn callback was found. The bounded direct-material-reference scan also found no external ROSIDIAN material reference beyond its own class/registration. That does not rule out item-ID, tag, reflection or external-mod paths. Treat the tooltip’s summon promise as unresolved in this inspected implementation until an activation path is demonstrated.

*Summoning activation unresolved; bounded absence evidence only*

### Runic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-runic-1.21.1.webp" width="220" height="220" alt="Runic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=runic)

**Released tooltip:**

- **Per-piece:** +10% Resistance to magic damage
- **Full-set:** Grants a small shield when taking magic damage
- **Full-set:** Effect can only be used once every 5 minutes

**Source review:** Magic-classified incoming damage input is multiplied by 1 − perPieceValue(0.1). FULL_SET magic damage can request ABSORPTION with duration input 200 when the player cooldown is inactive, then sets cooldown input 6000. The inspected post-damage method has no explicit positive-new-damage guard. Poison classification and engine hook order remain relevant.

*Released local callback review; helper and runtime limits retained*

### Sharpshot

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-sharpshot-1.21.1.webp" width="220" height="220" alt="Sharpshot neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=sharpshot)

**Released tooltip:**

- **Per-piece:** +7% Gun damage
- **Full-set:** +10% Extra Sniper damage

**Source review:** The source must be gun-classified and the wearer must currently hold an AoAGun in the main hand, otherwise the offhand is checked. FULL_SET with the selected gun being an AoASniper uses multiplier 1.38; other cases use 1 + perPieceValue(0.07). The check uses the currently selected held-item path, not an independently verified original projectile weapon snapshot.

*Released local callback review; helper and runtime limits retained*

### Skeletal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-skeletal-1.21.1.webp" width="220" height="220" alt="Skeletal neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=skeletal)

**Released tooltip:**

- **Full-set:** Stops hunger drain while worn

**Source review:** For a ServerPlayer with saturation<1 and FULL_SET, the callback saves the food level, calls FoodData.eat(1,0.5), then restores the food level. This is saturation maintenance rather than a direct command to set a full hunger bar.

*Selected branch checked*

### Spaceking

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-spaceking-1.21.1.webp" width="220" height="220" alt="Spaceking neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=spaceking)

**Released tooltip:**

- **Full-set:** 33% Chance to summon a friendly Orbling when attacked
- **Full-set:** Orblings can be absorbed to regain health

**Source review:** The released class declares only its constructor and tooltip; no local Orbling-summon or absorption callback was found. The bounded direct-material-reference scan found no external SPACEKING material reference beyond its own class/registration. Item-ID, tag, reflection and external-mod routes are outside that absence check. Keep the summon/heal promises unresolved rather than marking them operational.

*Summoning activation unresolved; bounded absence evidence only*

### Speed

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-speed-1.21.1.webp" width="220" height="220" alt="Speed neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=speed)

**Released tooltip:**

- **Full-set:** +10% Movement speed

**Source review:** Four slot-specific MOVEMENT_SPEED modifiers each use amount 0.1 with ADD_MULTIPLIED_TOTAL. The FULL_SET equip callback applies a separate transient modifier of the same amount/operation; the matching unequip callback removes it. These are independent attribute operations, not a proof that adding five displayed percentages gives the final movement speed.

*Slot modifiers and full-set equip/unequip pair checked*

### Subterranean

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-subterranean-1.21.1.webp" width="220" height="220" alt="Subterranean neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=subterranean)

**Released tooltip:**

- **Full-set:** +40% Mining speed

**Source review:** FULL_SET equip applies a transient ATTACK_SPEED modifier of −0.16666667 using ADD_MULTIPLIED_TOTAL, and unequip removes it. The full-set tick callback also builds DIG_SPEED with duration input 2 and level input 2, hiding particles. Preserve the tradeoff and its cleanup when porting; the tooltip alone does not enumerate every attribute operation.

*Attribute tradeoff and full-set effect callback checked*

### Utopian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-utopian-1.21.1.webp" width="220" height="220" alt="Utopian neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=utopian)

**Released tooltip:**

- **Per-piece:** +5% Xp gain across all skills
- **Full-set:** +10% Xp gain across all skills

**Source review:** ServerPlayer equip callbacks add 0.05 to every skill XP modifier per ordinary piece and 0.1 for the FULL_SET marker; unequip removes the corresponding amount. This is an adjustment to the skill modifier, not a guarantee that every XP event scales identically. Verify balanced equip/unequip, requirements and reconnect, especially with compatible helmets.

*Released local callback review; helper and runtime limits retained*

### Void

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-void-1.21.1.webp" width="220" height="220" alt="Void neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=void)

**Released tooltip:**

- **Per-piece:** +2.5% Chance to briefly stun melee attackers
- **Full-set:** +10% Chance to briefly stun melee attackers

**Source review:** Requires positive new damage, a LivingEntity attacker and a melee source. RandomUtil.percentChance receives 0.2 for FULL_SET, otherwise perPieceValue(0.025). Successful calls build MOVEMENT_SLOWDOWN with duration input 30 and level input 20 for the attacker. The full-set branch is a total input, not a second additive random roll.

*Selected branch checked; EffectBuilder level/duration interpretation not reimplemented*

### Weaken

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-weaken-1.21.1.webp" width="220" height="220" alt="Weaken neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=weaken)

**Released tooltip:**

- **Per-piece:** +17.5% Chance to weaken melee attackers
- **Full-set:** Strongly weakens enemies when activating

**Source review:** Positive melee damage from a living attacker must pass RandomUtil.percentChance(perPieceValue(0.175)). It then requests WEAKNESS with duration input 60, level input 2 for FULL_SET or 1 otherwise, marked ambient. These are helper/effect inputs rather than measured proc rates or a simulated final potion amplifier.

*Released local callback review; helper and runtime limits retained*

### Wither

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-wither-1.21.1.webp" width="220" height="220" alt="Wither neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=wither)

**Released tooltip:**

- **Per-piece:** +25% Resistance to wither damage
- **Full-set:** Immunity to wither damage
- **Full-set:** Grants a brief defense boost when inflicted with wither

**Source review:** Incoming reduction requires the IS_WITHER tag and perPieceValue(0.25). Full set plus that tag sets invulnerability and builds DAMAGE_RESISTANCE with duration input 60, ambient and hidden-icon flags. The effect is requested on a qualifying damage check, not merely because a status-effect icon exists.

*Selected branch checked*

### Zargonite

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-zargonite-1.21.1.webp" width="220" height="220" alt="Zargonite neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=zargonite)

**Released tooltip:**

- **Per-piece:** +10% Magic damage dealt

**Source review:** Magic-classified outgoing damage input is multiplied by 1 + perPieceValue(0.1). Its scope follows DamageUtil.isMagicDamage and the surrounding event dispatch; it is not a universal damage bonus.

*Released local callback review; helper and runtime limits retained*

## Acceptance checklist

1. Compare one, two, three and four pieces. Include an approved universal-compatible helmet and mixed materials.
2. Test intended versus unrelated damage types, positive versus blocked damage, entity ownership and attack direction.
3. Check temperature/resource thresholds, hunger versus saturation, damage-immunity tags and status-effect application.
4. Test equipment requirements, full inventory, death/spectator transitions, reconnect and client/server agreement using copied saves.
5. Keep event-driven equipment tracking; measure before adding repeated scans or per-frame searches. Existing tick callbacks are source behavior, not a performance endorsement.

## Evidence and credits

- [48-set tooltip and method index](https://herbertofury.github.io/Advent-of-Ascension/armour-effect-index-1.21.1.json)
- [All-set route reviews and shared dispatch audit](https://herbertofury.github.io/Advent-of-Ascension/armour-effect-route-audit-1.21.1.json)
- [Material/registration evidence](https://herbertofury.github.io/Advent-of-Ascension/armour-material-evidence-1.21.1.json)
- [Worn-image provenance](https://herbertofury.github.io/Advent-of-Ascension/worn-armour-render-evidence-1.21.1.json)

AoA descriptions, systems and textures: Tslat and contributors. Vanilla mesh: Mojang/Microsoft. Original documentation tooling and presentation. No Java/game code was executed for this analysis.
