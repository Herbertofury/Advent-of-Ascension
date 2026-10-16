# Multi-state plant and portal references

The age-only crop pass could not represent Thorny Plant’s combined age/height selector. This supplement reads the exact released blockstate maps for **1.16.5, 1.20.1 and 1.21.1** and accounts for **141 version-specific states**.

- Thorny Plant: 45 age/height combinations per release, 135 total.
- Of those, 31 per release have visible texture regions; 14 per release reference fully transparent regions. Transparent tiles are labeled rather than filled with invented artwork.
- Nowhere activity portal: two axis states per release, six total.

These are independent block-state resource views. They are not an assembled plant, a claim that every combination occurs naturally, a growth-rate simulation, or a portal shader test. Click each image for readable full-size labels. Original models/textures are credited to Tslat and contributors.

## 1.16.5 · Thorny Plant

![1.16.5 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-thorny-states-00.webp)

![1.16.5 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-thorny-states-05.webp)

![1.16.5 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-thorny-states-10.webp)

## 1.16.5 · Nowhere activity portal

![1.16.5 aoa3:nowhere_activity_portal state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-nowhere-portal-states.webp)

## 1.20.1 · Thorny Plant

![1.20.1 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-thorny-states-00.webp)

![1.20.1 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-thorny-states-05.webp)

![1.20.1 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-thorny-states-10.webp)

## 1.20.1 · Nowhere activity portal

![1.20.1 aoa3:nowhere_activity_portal state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-nowhere-portal-states.webp)

## 1.21.1 · Thorny Plant

![1.21.1 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-thorny-states-00.webp)

![1.21.1 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-thorny-states-05.webp)

![1.21.1 aoa3:thorny_plant_crop state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-thorny-states-10.webp)

## 1.21.1 · Nowhere activity portal

![1.21.1 aoa3:nowhere_activity_portal state reference](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-nowhere-portal-states.webp)

## Verification and limits

The extractor requires every state to name one explicit model and rejects unexpected variant options. Thorny Plant must have the exact 15 × 3 selector grid. When a render is blank, the referenced UV regions are checked for zero alpha before it is classified as transparent. Model and blockstate hashes are retained.

The activity-portal pictures use the first declared texture frame with documentation lighting. They do not reproduce animation, full translucent sorting or effects. State pictures do not turn block-only forms into independent inventory items.

[Exact state/model evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/multistate-block-reference-evidence.json) · [Inventory preview resolution ledger](Inventory-Preview-Resolution-Ledger) · [Age-only growth references](Crops-and-Growth-Stages).
