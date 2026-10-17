# Armor set effects and activation · 1.21.1

**Minecraft 1.21.1 / AoA 3.7.16.1.** Choose equipment for its effect, not just its defense number. This guide connects all **48 ordinary four-piece sets** to their worn previews and **100 released tooltip lines**. Nine selected sets also have callback-level behavior notes.

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

## Browse all 48 sets

The images use released textures and the checked neutral armor mesh. They do not reproduce glint, animation or an actual equipped player. Every card links its four inventory entries.

### Alacrity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-alacrity-1.21.1.webp" width="220" height="220" alt="Alacrity neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=alacrity)

**Released tooltip:**

- **Per-piece:** +20% Resistance to fall damage
- **Full-set:** Full immunity to fall damage

**Checked callback:** The full-set invulnerability callback checks the fall-damage tag. The partial-set incoming-damage callback checks only absence of FULL_SET before adding an armor-stage reduction; it has no fall-source guard in this method. Its lambda uses equippedPieces.size × 0.2.

*Tooltip/implementation scope mismatch requiring target-build review; no observed combat bug or applied fix.*

### Archaic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-archaic-1.21.1.webp" width="220" height="220" alt="Archaic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=archaic)

**Released tooltip:**

- **Per-piece:** The lower your health, the more melee damage you deal
- **Per-piece:** Increased incoming melee damage depending on health
- **Full-set:** No increased incoming melee damage

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Baron

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-baron-1.21.1.webp" width="220" height="220" alt="Baron neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=baron)

**Released tooltip:**

- **General:** Extremely durable

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Battleborn

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-battleborn-1.21.1.webp" width="220" height="220" alt="Battleborn neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=battleborn)

**Released tooltip:**

- **General:** Attack speed increases while attacking
- **Per-piece:** Faster attack speed increases

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Biogenic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-biogenic-1.21.1.webp" width="220" height="220" alt="Biogenic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=biogenic)

**Released tooltip:**

- **General:** Slows melee enemies when hit, increasing with stronger hits
- **Per-piece:** Increased Slowness effect
- **Full-set:** Can see and breathe underwater

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Boreic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-boreic-1.21.1.webp" width="220" height="220" alt="Boreic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=boreic)

**Released tooltip:**

- **General:** Explodes When Hit In Water
- **Per-piece:** Increased Explosion Damage And Radius
- **Full-set:** Also stuns nearby enemies briefly when exploding

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Candy

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-candy-1.21.1.webp" width="220" height="220" alt="Candy neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=candy)

**Released tooltip:**

- **General:** Automatically consumes food when needed
- **Per-piece:** Reduced time between consumptions
- **Full-set:** Ignores consumption cooldown

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Commander

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-commander-1.21.1.webp" width="220" height="220" alt="Commander neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=commander)

**Released tooltip:**

- **General:** Grants a Strength buff to all nearby allies
- **Per-piece:** +2 Blocks range
- **Full-set:** Strength effect increased

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Crystallis

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-crystallis-1.21.1.webp" width="220" height="220" alt="Crystallis neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=crystallis)

**Released tooltip:**

- **General:** Reflects damage back at melee attackers
- **Per-piece:** +25% Damage reflected
- **Full-set:** Effect also applies to ranged attackers

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Elecanyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-elecanyte-1.21.1.webp" width="220" height="220" alt="Elecanyte neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=elecanyte)

**Released tooltip:**

- **General:** Taking damage regenerates Spirit
- **Per-piece:** Regenerate more Spirit per hit

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Embrodium

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-embrodium-1.21.1.webp" width="220" height="220" alt="Embrodium neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=embrodium)

**Released tooltip:**

- **Per-piece:** Increased Spirit regen while in hot environments
- **Full-set:** +25% Spirit regeneration at all times

**Checked callback:** Server-player tick callback reads Spirit per-tick regeneration (fallback 0.04). Full set adds 0.25×regen. Above ambient temperature 0.8, it additionally adds perPieceValue(0.25×regen)×min(1,temperature/2); only positive totals are submitted. This is an extra resource request, not a measured final recovery rate.

*Selected branch checked*

### Exoplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-exoplate-1.21.1.webp" width="220" height="220" alt="Exoplate neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=exoplate)

**Released tooltip:**

- **Per-piece:** Increased resistance when in darker environments

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Explosive

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-explosive-1.21.1.webp" width="220" height="220" alt="Explosive neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=explosive)

**Released tooltip:**

- **Per-piece:** +15% Explosion damage resistance
- **Full-set:** Full immunity to explosions

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Fungal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-fungal-1.21.1.webp" width="220" height="220" alt="Fungal neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=fungal)

**Released tooltip:**

- **General:** Has a chance to poison melee attackers when hit
- **Per-piece:** +20% Chance to poison
- **Full-set:** Can also poison nearby mobs when activated

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Ghastly

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghastly-1.21.1.webp" width="220" height="220" alt="Ghastly neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ghastly)

**Released tooltip:**

- **General:** Shows all nearby mobs while crouching
- **Per-piece:** +4 Blocks range

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Ghoulish

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ghoulish-1.21.1.webp" width="220" height="220" alt="Ghoulish neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ghoulish)

**Released tooltip:**

- **Per-piece:** +10% Energy damage
- **Full-set:** 30% Reduced Spirit costs on weapons

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Hazmat

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hazmat-1.21.1.webp" width="220" height="220" alt="Hazmat neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hazmat)

**Released tooltip:**

- **Full-set:** Provides its own oxygen

**Checked callback:** FULL_SET plus air below maximum triggers setting air to maximum. The airtight helmet method separately calls PlayerUtil.isWearingFullSet for its material.

*Selected branch checked*

### Hydrangic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydrangic-1.21.1.webp" width="220" height="220" alt="Hydrangic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hydrangic)

**Released tooltip:**

- **Full-set:** Fertilizes plants when placed at the cost of durability

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Hydroplate

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-hydroplate-1.21.1.webp" width="220" height="220" alt="Hydroplate neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=hydroplate)

**Released tooltip:**

- **General:** Naturally regenerate health while in water
- **Per-piece:** Increased healing speed
- **Full-set:** 20% Resistance to all attacks while in water

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Ice

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-ice-1.21.1.webp" width="220" height="220" alt="Ice neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=ice)

**Released tooltip:**

- **General:** Armour repairs itself when in cold environments

**Checked callback:** Server-side inventoryTick requires numeric slotId 36–40 inclusive, a LivingEntity wearer, damage>0, random nextFloat<0.02 and ambient temperature<0.15. It then subtracts one damage point. These are callback gates, not proof that every engine inventory slot invokes this hook identically.

*Selected branch checked*

### Infernal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-infernal-1.21.1.webp" width="220" height="220" alt="Infernal neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=infernal)

**Released tooltip:**

- **Per-piece:** +15% Fire resistance
- **Full-set:** Full immunity to fire damage

**Checked callback:** Incoming damage must match IS_FIRE before adding a reduction with perPieceValue(0.15). Full-set fire-tag invulnerability is a separate callback. The reduction helper acts on remaining damage at its stage.

*Selected branch checked*

### Knight

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-knight-1.21.1.webp" width="220" height="220" alt="Knight neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=knight)

**Released tooltip:**

- **Full-set:** When below 20% health, gain extra strength

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Lunar

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lunar-1.21.1.webp" width="220" height="220" alt="Lunar neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lunar)

**Released tooltip:**

- **Per-piece:** Jump higher
- **Per-piece:** Reduces fall damage slightly

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Lyndamyte

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyndamyte-1.21.1.webp" width="220" height="220" alt="Lyndamyte neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lyndamyte)

**Released tooltip:**

- **Per-piece:** +25% Chance to set melee attackers on fire
- **Full-set:** Sets fire to targets when meleeing

**Checked callback:** Retaliation requires positive new damage, server side, a melee source and a RandomUtil.percentChance call with perPieceValue(0.25); it requests five seconds of fire on the source entity. Full-set outgoing melee attacks separately request five seconds of fire on the target. External random-helper semantics and final immunity/hooks remain separate.

*Selected branch checked*

### Lyonic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-lyonic-1.21.1.webp" width="220" height="220" alt="Lyonic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=lyonic)

**Released tooltip:**

- **General:** Attracts nearby dropped items
- **Per-piece:** +2 Blocks attraction range
- **Full-set:** Also attracts xp orbs

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Mercurial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-mercurial-1.21.1.webp" width="220" height="220" alt="Mercurial neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=mercurial)

**Released tooltip:**

- **General:** Taking explosive damage grants resistance
- **Per-piece:** Increased resistance time
- **Full-set:** Increased resistance amount

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Necro

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-necro-1.21.1.webp" width="220" height="220" alt="Necro neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=necro)

**Released tooltip:**

- **General:** Protects items from the user's inventory on death
- **General:** Prioritises hotbar items first
- **Per-piece:** +1 Item protected
- **Full-set:** Saves the wearer from a killing blow once per hour at the cost of durability

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Nethengeic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nethengeic-1.21.1.webp" width="220" height="220" alt="Nethengeic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=nethengeic)

**Released tooltip:**

- **Per-piece:** +10% Damage to targets on fire
- **Full-set:** +50% Damage if the wearer is on fire

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Nightmare

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-nightmare-1.21.1.webp" width="220" height="220" alt="Nightmare neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=nightmare)

**Released tooltip:**

- **Full-set:** Staves require 1 less of each Rune
- **Full-set:** Staves will no longer consume Distortion Runes on use

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Omni

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-omni-1.21.1.webp" width="220" height="220" alt="Omni neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=omni)

**Released tooltip:**

- **Per-piece:** +10% Explosion damage
- **Full-set:** Creates an explosion when hit by a melee attack

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Phantasm

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-phantasm-1.21.1.webp" width="220" height="220" alt="Phantasm neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=phantasm)

**Released tooltip:**

- **General:** Crammed full of clovers

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Poison

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-poison-1.21.1.webp" width="220" height="220" alt="Poison neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=poison)

**Released tooltip:**

- **Per-piece:** +25% Resistance to poison damage
- **Full-set:** Immunity to poison damage
- **Full-set:** Gives a brief defense boost when inflicted with poison

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Predatious

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-predatious-1.21.1.webp" width="220" height="220" alt="Predatious neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=predatious)

**Released tooltip:**

- **Per-piece:** +10% Ranged damage dealt
- **Full-set:** Deals minor Thorns damage to melee attackers

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Primordial

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-primordial-1.21.1.webp" width="220" height="220" alt="Primordial neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=primordial)

**Released tooltip:**

- **General:** Melee attackers suffering from wither deal less damage
- **Per-piece:** +15% Damage reduction
- **Full-set:** Effect not restricted to melee attackers

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Purity

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-purity-1.21.1.webp" width="220" height="220" alt="Purity neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=purity)

**Released tooltip:**

- **Full-set:** Keeps The Wearer Clean From Physical Impairments

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Rockbone

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rockbone-1.21.1.webp" width="220" height="220" alt="Rockbone neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=rockbone)

**Released tooltip:**

- **Per-piece:** +10% Resistance to ranged damage
- **Full-set:** 10% Chance to dodge a ranged attack

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Rosidian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-rosidian-1.21.1.webp" width="220" height="220" alt="Rosidian neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=rosidian)

**Released tooltip:**

- **Per-piece:** +4% Chance to spawn a friendly Rosid when hit
- **Full-set:** Guaranteed Rosid spawn when damaged 4 health or more

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Runic

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-runic-1.21.1.webp" width="220" height="220" alt="Runic neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=runic)

**Released tooltip:**

- **Per-piece:** +10% Resistance to magic damage
- **Full-set:** Grants a small shield when taking magic damage
- **Full-set:** Effect can only be used once every 5 minutes

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Sharpshot

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-sharpshot-1.21.1.webp" width="220" height="220" alt="Sharpshot neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=sharpshot)

**Released tooltip:**

- **Per-piece:** +7% Gun damage
- **Full-set:** +10% Extra Sniper damage

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Skeletal

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-skeletal-1.21.1.webp" width="220" height="220" alt="Skeletal neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=skeletal)

**Released tooltip:**

- **Full-set:** Stops hunger drain while worn

**Checked callback:** For a ServerPlayer with saturation<1 and FULL_SET, the callback saves the food level, calls FoodData.eat(1,0.5), then restores the food level. This is saturation maintenance rather than a direct command to set a full hunger bar.

*Selected branch checked*

### Spaceking

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-spaceking-1.21.1.webp" width="220" height="220" alt="Spaceking neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=spaceking)

**Released tooltip:**

- **Full-set:** 33% Chance to summon a friendly Orbling when attacked
- **Full-set:** Orblings can be absorbed to regain health

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Speed

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-speed-1.21.1.webp" width="220" height="220" alt="Speed neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=speed)

**Released tooltip:**

- **Full-set:** +10% Movement speed

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Subterranean

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-subterranean-1.21.1.webp" width="220" height="220" alt="Subterranean neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=subterranean)

**Released tooltip:**

- **Full-set:** +40% Mining speed

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Utopian

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-utopian-1.21.1.webp" width="220" height="220" alt="Utopian neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=utopian)

**Released tooltip:**

- **Per-piece:** +5% Xp gain across all skills
- **Full-set:** +10% Xp gain across all skills

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Void

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-void-1.21.1.webp" width="220" height="220" alt="Void neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=void)

**Released tooltip:**

- **Per-piece:** +2.5% Chance to briefly stun melee attackers
- **Full-set:** +10% Chance to briefly stun melee attackers

**Checked callback:** Requires positive new damage, a LivingEntity attacker and a melee source. RandomUtil.percentChance receives 0.2 for FULL_SET, otherwise perPieceValue(0.025). Successful calls build MOVEMENT_SLOWDOWN with duration input 30 and level input 20 for the attacker. The full-set branch is a total input, not a second additive random roll.

*Selected branch checked; EffectBuilder level/duration interpretation not reimplemented*

### Weaken

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-weaken-1.21.1.webp" width="220" height="220" alt="Weaken neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=weaken)

**Released tooltip:**

- **Per-piece:** +17.5% Chance to weaken melee attackers
- **Full-set:** Strongly weakens enemies when activating

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

### Wither

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-wither-1.21.1.webp" width="220" height="220" alt="Wither neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=wither)

**Released tooltip:**

- **Per-piece:** +25% Resistance to wither damage
- **Full-set:** Immunity to wither damage
- **Full-set:** Grants a brief defense boost when inflicted with wither

**Checked callback:** Incoming reduction requires the IS_WITHER tag and perPieceValue(0.25). Full set plus that tag sets invulnerability and builds DAMAGE_RESISTANCE with duration input 60, ambient and hidden-icon flags. The effect is requested on a qualifying damage check, not merely because a status-effect icon exists.

*Selected branch checked*

### Zargonite

<img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/worn-armour-zargonite-1.21.1.webp" width="220" height="220" alt="Zargonite neutral armor-only study">

[View set and all four pieces](https://herbertofury.github.io/Advent-of-Ascension/armour-gallery.html?v=1.21.1&set=zargonite)

**Released tooltip:**

- **Per-piece:** +10% Magic damage dealt

Effect-by-effect callback interpretation is still pending. The evidence retains the declared methods; the tooltip above is not silently promoted to runtime certification.

## Acceptance checklist

1. Compare one, two, three and four pieces. Include an approved universal-compatible helmet and mixed materials.
2. Test intended versus unrelated damage types, positive versus blocked damage, entity ownership and attack direction.
3. Check temperature/resource thresholds, hunger versus saturation, damage-immunity tags and status-effect application.
4. Test equipment requirements, full inventory, death/spectator transitions, reconnect and client/server agreement using copied saves.
5. Keep event-driven equipment tracking; measure before adding repeated scans or per-frame searches. Existing tick callbacks are source behavior, not a performance endorsement.

## Evidence and credits

- [48-set tooltip and method index](https://herbertofury.github.io/Advent-of-Ascension/armour-effect-index-1.21.1.json)
- [Nine selected routes and shared dispatch audit](https://herbertofury.github.io/Advent-of-Ascension/armour-effect-route-audit-1.21.1.json)
- [Material/registration evidence](https://herbertofury.github.io/Advent-of-Ascension/armour-material-evidence-1.21.1.json)
- [Worn-image provenance](https://herbertofury.github.io/Advent-of-Ascension/worn-armour-render-evidence-1.21.1.json)

AoA descriptions, systems and textures: Tslat and contributors. Vanilla mesh: Mojang/Microsoft. Original documentation tooling and presentation. No Java/game code was executed for this analysis.
