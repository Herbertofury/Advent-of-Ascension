# Vulcanes and Rage: retaliation, thresholds and variant effects

[Open the item browser](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1) · [Blasters and Spirit](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Blasters-and-Spirit-1.21.1) · [Repairing equipment](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Mending-Table-and-Repair-Materials-1.21.1)

![All eight released Vulcane models with activation thresholds and durability](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/vulcane-rage-overview-1.21.1.webp)

**Scope:** Minecraft 1.21.1 / AoA 3.7.16.1. Eight registrations share damage input 10 and Rage activation threshold 50. Their exact durability and selected behavior are checked against the released archive. This is not a runtime test or a claim about the owner’s private Enderloom candidate.

## The important rule: 50 is the threshold, not the payment

The normal base-use path checks whether you have enough Rage, obtains the player’s last hurt-by-mob target, and attempts activation. When that succeeds, the code passes **all current Rage** to the resource-consumption method. Creative and other resource-exempt cases are handled separately.

Do not plan two ordinary activations merely because the meter reads 100 and the tooltip shows 50. A successful resource-paying activation requests the full current amount.

## How to prepare and use one

1. Choose a variant below and inspect its exact-version recipe and drop links.
2. Check your Rage and the actual recent attacker. This base path uses the player’s last hurt-by-mob reference rather than the creature under your crosshair.
3. Do not waste health farming Rage just to meet a number. Use a safe encounter and keep an escape route.
4. Expect a missing target to fail. Rejected damage and special target behavior also need checking.
5. After a successful ordinary activation, check both durability and the remaining Rage meter.
6. Test the chosen variant’s effect recipient. In particular, Battle Vulcane’s released call targets the hit entity, as explained below.

## More Rage changes the attack input

With stock maximum Rage 100, the base multiplier is `1 + (current Rage - threshold) / maximum Rage`.

| Current Rage | Threshold | Multiplier | Attack input with base damage 10 |
|---:|---:|---:|---:|
| 50 | 50 | 1 | 10 |
| 75 | 50 | 1.25 | 12.5 |
| 100 | 50 | 1.5 | 15 |

These are configured attack inputs, not guaranteed health loss. Armor, damage handling, target immunity and other hooks can change the result. Do not transfer this table to a datapack with a different maximum or a different release.

## How the inspected Rage resource changes

The bundled resource configuration sets maximum Rage 100 and per-tick drain 0.01. The selected damage handler adds the event’s **original damage** when the damage source has an attributed entity; it is not a universal reward for every environmental damage event. The selected tick handler subtracts the configured drain while the stored value is positive.

The synchronization and small-value edge cases below remain runtime acceptance targets. A UI meter is not proof of the exact server value.

## Eight variant references

| Variant | Threshold | Durability | Released special-effect observation |
|---|---:|---:|---|
| [Vulcane](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Avulcane) | 50 | 50 | Base activation; no variant effect added here. |
| [Vulcane (Battle)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Abattle_vulcane) | 50 | 75 | Strength effect is passed to the hit entity, with user as source; duration input 200 and level-builder input 2. Verify intended recipient. |
| [Vulcane (Equality)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aequality_vulcane) | 50 | 75 | Heals the user using half the passed attack input, rather than measuring the target’s final health loss. |
| [Vulcane (Fire)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Afire_vulcane) | 50 | 75 | Ignites the hit entity with an 8-second input. |
| [Vulcane (Impairment)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Aimpairment_vulcane) | 50 | 75 | Slowness on hit entity; duration input 100 ticks, level-builder input 3. |
| [Vulcane (Poison)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apoison_vulcane) | 50 | 75 | Poison on hit entity; duration input 140 ticks, level-builder input 2. |
| [Vulcane (Power)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Apower_vulcane) | 50 | 75 | Weakness on hit entity; duration input 100 ticks, level-builder input 2. |
| [Vulcane (Wither)](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.21.1&id=aoa3%3Awither_vulcane) | 50 | 75 | Wither on hit entity; duration input 70 ticks, level-builder input 2. |

Effect-builder level inputs are retained as code inputs rather than silently converted into an unverified amplifier label. Durations and recipients are selected-method observations; immunities and runtime effects still matter.

## Maintainer regression targets

### Battle Vulcane effect recipient

The released `onDamageEntity` call supplies local parameter 3 (the hit entity) as the first argument to `EntityUtil.applyPotions`, with local parameter 2 (the user) as source. The helper treats its first entity as the target. The selected effect is Strength. This is concrete call-direction evidence, not proof that a particular player observed a bug. Confirm the intended design before changing the recipient; then test attacker and victim separately.

### Rage updates and incremental synchronization

The released damage and drain handlers write the resource value directly without calling the clamping setter or marking `needsSync`. The normal setter marks that flag, while the selected server incremental resource collector checks it before serializing resource updates. After a prior sync clears the flag, these isolated mutations can leave it false.

This is a **bounded static synchronization candidate**, not an in-game reproduction: other runtime paths may trigger a later update. Test a clean post-sync state, one entity-attributed hit, passive drain, resource consumption and reconnect. Record server value and client meter together. Prefer updating through the existing clamping/dirty-marking path if the reproduction confirms the issue; do not add repeated world or inventory scans.

### Drain near zero

The selected tick handler checks positive value and subtracts the drain without the clamping setter. With value 0.005 and drain 0.01, the isolated arithmetic yields -0.005. Verify exact-build behavior and all callers before changing it. A candidate correction should preserve capacity limits, synchronization and save/client behavior.

## Acceptance checklist

- Normal resource-paying success at Rage 50, 75 and 100; confirm the requested full-amount consumption.
- No recent target, rejected damage, dead/removed targets and target lifetime changes.
- Each variant’s recipient and effect, including Equality’s healing input.
- Creative/resource-exempt handling separately from Survival.
- Rage damage accumulation, drain, near-zero boundary, sync and reconnect.
- Modified resource maximum, altered stack components, client/server consistency and durability breakage.

[Released registration and 14-class behavior evidence](https://herbertofury.github.io/Advent-of-Ascension/vulcane-rage-evidence-1.21.1.json) · [Illustration provenance](https://herbertofury.github.io/Advent-of-Ascension/vulcane-art-evidence-1.21.1.json).

Archive: `AoA3-1.21.1-3.7.16.1.jar`. No Java game classes were executed. Models and mechanics are credited to Tslat and contributors. These findings do not establish that the private owner-local candidate contains the same paths, and no game fix is claimed here.


## Historical edition boundary

The checked 1.12.2 / AoA 3.3.6 family uses a stored revenge target and timer. Use the [historical revenge guide](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-Revenge-Targets-and-Effects-1.12.2) for that release rather than applying this page's modern Rage rules.
