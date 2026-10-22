# Moonlit Hive: additional craftable variants

Status: concept and gameplay specification, not implemented or native accepted.

## Scope
All five release-union IDs: `aoa3:hive_blaster`, `aoa3:hive_cracker`, `aoa3:hive_howitzer`, `aoa3:hive_staff`, `aoa3:hiver`. Keep each original weapon and its base appearance available. This is an additional soul-themed craftable option, not a replacement or automatic conversion. Do not merge identities on name similarity.

## Art direction
Silver chitin, midnight understructure, soul-cyan honey cells and animated soul bees. Bees must visibly move inside chambers during idle and charge, respond to release, and return to rest. Each weapon retains its own silhouette; Hive Staff remains a staff with two pale tips, not a gun. The five separate hero sheets are candidate designs, not final modeled assets.

Two optional sights: a coordinated soul-bee swarm forms a clear perimeter, or bees quickly construct a translucent soul-honey perimeter. Neither fills or obscures the central aiming aperture. Preserve explicit attachment-off state. Reduced-motion presentation must retain an equally readable aim point and timing, without changing gameplay.

## Soul-campfire-inspired crafting proposal
Official Minecraft Java 1.20.1 recipe data was inspected directly: soul campfire uses three sticks, one item from `minecraft:soul_fire_base_blocks`, and three logs. The item tag contains soul sand and soul soil. This is source evidence, not a claim that a Moonlit recipe already exists.

Proposed 3x3 upgrade arrangement: top row existing weapon / stick / empty; middle row stick / soul sand or soul soil / stick; bottom row log / log / log. This places the weapon into an otherwise empty slot of the vanilla soul-campfire arrangement. The exact layout is a project proposal, not a user-specified final recipe. Recipe discovery, unlock requirements and balancing remain open.

Consume one eligible existing weapon and materials, producing exactly one Moonlit-configured version of that same weapon. Do not output a fresh default stack that discards the original. Preserve registry identity, damage/durability, resource state, enchantments, custom name, attachments, decals, cosmetics, provenance and all unknown extension data. Unknown fields must survive round trips. Reject already-Moonlit inputs rather than consuming materials twice, unless a separately specified operation exists. Do not create a duplicate original weapon as a remainder. Logs and soul-fire-base tags remain data-driven. Existing saves must not be rewritten in bulk.

The soul-campfire analogy does not imply an automatic damage or speed buff. No such numerical change is authorized by this proposal. Original mechanics remain unless separately specified. Shared charge/release artwork is visual direction, not evidence that every hive weapon has identical charge behavior or projectile type.

## Required implementation evidence
- Unit-level matching and data-preservation tests, including soul sand and soil, all five IDs, unknown fields, explicit off states, invalid inputs, repeated crafting, shift-click and inventory-capacity cases.
- Server-authoritative consumption and result generation, no client-only unlock or resource accounting.
- Native AoA plus TaCZ integration where appropriate, original behavior parity, multiplayer, save migration/rollback and performance.
- Individual hand fit, staff handling, sight alignment, animation continuity and reduced-motion checks for every host.

Original Advent of Ascension identity and source references: Tslat and contributors. Artwork and this proposal do not grant redistribution rights for original mod assets.
