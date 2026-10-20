# Balloon Bomber

[Armory](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Overhaul)

## Original identity

![Released Balloon Bomber sprite](balloon-bomber-original.png)

A red-and-gold carnival cannon that uses **Balloon ammunition**. Its released tooltip says the balloons explode on impact. Preserve its playful cylindrical body, golden hoops and twin underside handle cues rather than dressing it as a modern rifle.

## Carnival mastercraft concept

![Balloon Bomber premium concept, proposed inspection sequence and cosmetic effects](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/balloon-bomber-concept-v1.png)

**Concept storyboard only; no native animation is implemented or accepted by this image.** The lacquered crimson body, gold stars, bell charm, balloon inflation inspection and ribbon/confetti effects are proposed presentation work. The illustrated inspection changes the muzzle silhouette between panels: resolve that inconsistency into one explicit mechanical/animation design before modeling. Do not let a pretty sheet bypass continuity QA.

## Released behavior

Pinned **AoA 3.7.1 / Minecraft 1.20.1**. [Evidence](balloon-bomber-source-evidence.json) · [Reproducible selected source checks](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/cannon-profile-source-checks-v1.zip)

| Property | Inspected value |
|---|---|
| Registered damage input | 12.5 |
| Durability | 505 |
| Delay | 24 ticks |
| Constructor recoil input | 0.22 |
| Base ammo override | Balloon |
| Projectile | BalloonBombEntity |
| Age / piercing parameters | 120 / 0 |
| Projectile gravity return | 0.1 |
| Block and entity impacts | Both call its explode method |
| Explosion helper strength input | 1.5 |
| Sound reference | ITEM_BALL_CANNON_FIRE |
| Packaged upgrade | Balloon Bomber + Seaside Upgrade Kit → Water-Balloon Bomber |

The explosion strength input is **not a measured radius or guaranteed final damage**. The registered damage, inherited hit handling and projectile explosion must be tested together; do not simply sum guessed damage numbers. The helper's native terrain and ownership behavior must be retained and tested under the target server rules.

The source record establishes the upgrade recipe, not an active acquisition route or invented lore. Native flight and impact captures remain outstanding.

## Proposed personality and feedback

- **Fire:** a compact recoil hop, brief golden rim flash, a readable balloon launch and a short ribbon trail.
- **Impact:** playful confetti visual with bounded particle count, reduced-effects option and clear hit feedback. Cosmetic fragments must not imply additional damage or drops.
- **Inspect:** inflate a tiny decorative balloon, wobble it, then return it to its idle state. This must not spend or grant ammunition.
- **Grip:** develop the twin handles around actual native player arms; avoid putting either hand inside the cannon body or charm swing.
- **Optional reload:** retain native Balloon accounting and no-reload mode. A theatrical cartridge swap is not automatically appropriate for this weapon.

## Attachments, rewards and variants

| Proposed option | Purpose | QA requirement |
|---|---|---|
| Star-flare muzzle | Distinct festive silhouette and declared delivery variant | Separate projectile-origin alignment and balanced behavior |
| Bell charm | Earned charm with optional explicitly declared bonus | Bounded swing, no hand/barrel intersections, safe salvage |
| Festival skin set | Crimson/gold default plus unlockable themed lacquer and emblems | Preserve readable original identity and low-cost material tier |
| Ribbon / confetti effect choices | Projectile, impact and optional defeat-effect customization | Client cosmetics cannot duplicate server damage |
| Water-Balloon successor | Preserve the real upgrade lineage | Inspect its own released behavior; do not assume it is only a recolor |

## Completion gates

Original and concept comparison; coherent all-angle design; model/material/UV review; native hands; moving-part and charm sweep tests; equip/idle/aim/fire/recovery/inspect/optional reload interruption tests; original versus new projectile/impact captures; sound; crafting/salvage/attachments; stickers and cosmetics; server authority; save safety; compatibility; performance measurements. All remain explicitly open until their evidence exists.

## Recoil interpretation

For this pinned 1.20.1 release, the stored constructor recoil input is not the inherited modifier getter: the inspected `BaseGun.getRecoilModifier()` returns approximately 0.35. The per-shot method and later client application determine the actual recoil path. Do not infer a stronger or weaker measured kick from the constructor column alone. This clarification does not change the original values, weapon balance or acceptance state. [Resolved method routing](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Effective-Recoil-Routing-1.20.1).
