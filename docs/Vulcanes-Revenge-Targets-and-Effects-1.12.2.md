[Home](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Home) · [Weapon reference library](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Reference-Library) · [Modern vulcanes and Rage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Vulcanes-and-Rage-1.21.1)

# Historical vulcanes: revenge targets and effects

**Minecraft 1.12.2 / AoA 3.3.6.** These eight vulcanes use a **stored revenge target and timer**. Do not import the later release's Rage instructions into this version. Released constructors, four base methods and sixteen effect/state/helper methods support this reference; no game execution is claimed.

![Four historical vulcane source-model portraits](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/vulcane-inputs-and-effects-1.12.2.webp)

## How to activate one in this release

1. The eligible server-side player damage callback checks that the player's current health is positive and the damage source's true source is a living entity.
2. A **1-in-15 random roll** in that callback enables revenge, stores that living source as the target and sets the timer to **400**. This is a roll per eligible callback, not every fifteenth hit, every damage point or a guarantee after taking damage once.
3. Right-click the vulcane while revenge is active. It uses the **stored target**, not a newly selected crosshair target.
4. The server-side base activation attempts damage through the vulcane helper. Only if that helper reports success does it run the additional effect, play its sound, damage the item by **1**, and disable revenge.
5. If revenge has expired, the target is rejected or the damage helper returns false, the base use path returns failure. The success-only item wear and revenge clearing do not happen in that branch.

A new successful trigger replaces the stored target and resets the timer. Ordinary unsuccessful trigger rolls do not make every new attacker the target.

## The 400-update window

The normal server END player-tick callback calls the player-data update. For a non-null, non-spectator server player, that update decrements a positive revenge timer and clears the state when it reaches zero. This is nominally **20 seconds at 20 TPS**, subject to the update guards and server timing.

The `isRevengeActive` method only checks **timer > 0 and target != null**. That alone is not proof the target is still alive, attackable, nearby or in the same situation as when stored. The damage path must still decide whether the action succeeds. No unrestricted range or cross-dimension hit guarantee is established here.

## Damage rules and protections

The selected helper constructs player damage with **absolute-damage and armor-bypass flags**. It still checks the target's invulnerability response and calls **HunterUtil.canAttackTarget(target, attacker, false)** before attempting the attack. It also clears the target's hurt-resistance timer before the attack call.

The historical tooltip's “true damage” wording is not permission to claim that every defense, Hunter requirement, event cancellation or mod protection is bypassed. Constructor damage inputs remain distinct from final health loss.

## All eight entries

| Vulcane and portrait | Damage input | Durability | Additional success effect |
|---|---:|---:|---|
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-vulcane.webp" alt="Vulcane source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.Vulcane.name) | 15 | 50 | No additional effect declared. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-battle_vulcane.webp" alt="Vulcane: Battle source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Battle](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.BattleVulcane.name) | 20 | 75 | Requests Strength on the player: 200 ticks, amplifier 1 (level II). |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-equality_vulcane.webp" alt="Vulcane: Equality source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Equality](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.EqualityVulcane.name) | 20 | 75 | Requests healing of half its own damage field: 10 health points for this registration, through the checked living/injured-player helper. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-fire_vulcane.webp" alt="Vulcane: Fire source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Fire](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.FireVulcane.name) | 20 | 75 | Calls target fire with 8 seconds. |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-impairment_vulcane.webp" alt="Vulcane: Impairment source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Impairment](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.ImpairmentVulcane.name) | 20 | 75 | Requests Slowness on the target: 100 ticks, amplifier 2 (level III). |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-poison_vulcane.webp" alt="Vulcane: Poison source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Poison](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PoisonVulcane.name) | 20 | 75 | Requests Poison on the target: 140 ticks, amplifier 1 (level II). |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-power_vulcane.webp" alt="Vulcane: Power source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Power](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.PowerVulcane.name) | 20 | 75 | Requests Weakness on the target: 100 ticks, amplifier 1 (level II). |
| <img src="https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/weapon-portrait-1.12.2-wither_vulcane.webp" alt="Vulcane: Wither source-model portrait" width="72" height="72" loading="lazy"><br> [Vulcane: Wither](https://herbertofury.github.io/Advent-of-Ascension/inventory-explorer.html?v=1.12.2&id=localization%3Aitem.WitherVulcane.name) | 20 | 75 | Requests Wither on the target: 70 ticks, amplifier 2 (level III). |

Potion amplifiers are zero-based. At 20 TPS, 200/100/140/70 ticks are nominally 10/5/7/3.5 seconds. Immunity, potion handling and other hooks can prevent or change the resulting effect. Equality's requested healing is based on its configured field, not measured health lost by the target, and the helper only attempts healing on a living, positive-health, injured recipient.

## Restoration checklist

- Keep the 1.12.2 revenge trigger separate from the modern Rage system.
- Test expired, replaced, dead and rejected targets without substituting the player's current aim.
- Confirm the 1-in-15 eligible-event roll and the 400-update timer under normal server ticks and spectator transitions.
- Verify Hunter/invulnerability rejection separately from a successful attack and its additional effect.
- Check sound, wear and revenge clearing only in the successful base activation branch.
- Test each potion, fire and healing result rather than treating a request as guaranteed application.
- Preserve these semantics when adding optional animated weapon remodels; no magazine/reload requirement is inferred.

[Exact released registrations and method evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/historical-vulcane-inputs-1.12.2.json) · [Source-model crop provenance](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/vulcane-art-evidence-1.12.2.json).
