# New artwork, preserved source contracts

AoA 3.7.1 / Minecraft 1.20.1. These are source inspection notes, not native gameplay acceptance. New geometry does not replace the original mechanics.

## Gas Blaster: keep the healing branch

The inspected item extends BaseBlaster and emits ToxicShotEntity. Its impact override routes players and the shooter’s own tame animals to a 0.05 healing call instead of inherited impact handling. The method does not check team membership, so the tooltip’s “allies” wording should not be expanded into an unverified friendly-team filter. The helper passes an absolute amount to healing, not a percentage. Modpack events, hit eligibility and effective healing rate require capture.

The underbody drum and rear gas canister are owner-directed visual parts. They do not authorize replacing the blaster’s spirit resource with ordinary ammunition.

## Germinator: sight breath is not another attack

The item creates GreenBulletEntity and inherits BaseGun’s Limonite Bullet getter and automatic mode. Its living-target impact applies a poison effect through EffectsLib. The stored effect-builder inputs are recorded separately; their duration units and effective result are not asserted here. The new salamander and breath-formed sight must not create an independent damage stream or consume resources on focus alone.

## Golder Bomber: preserve the extra projectile path

The item inherits Cannonball ammunition and nonautomatic mode from BaseCannon. After inherited firing succeeds, its server-side branch creates an additional GoldenCannonballEntity. The bundled description corroborates the two-for-one intent, but collision, total resource use and actual native shot count still require testing. The living dinosaur, metallic glints and spike sight are visual additions, not permission to alter cadence or invent explosive behavior.

## Luxon Stickler: drum appearance is not ammo identity

Unlike the inherited cannon default, Luxon Stickler explicitly returns the Grenade item as ammunition. It creates LuxonSticklerShotEntity; on living-target impact it calls inherited damage, creates a stuck entity, then discards the initial projectile. That stuck entity’s full effects and lifetime remain a separate review. Keep this distinction when authoring drum and reload presentation.

## Bozo Blaster: do not copy another horn’s upgrades

Bozo creates BozoBallEntity, inherits Cannonball ammunition and nonautomatic mode, and selects the Clowner firing sound. Its squeezable front horn-grip concept does not automatically include the separately requested earned blowing-mode damage, count and speed buffs for Bubble Horn and Hell Horn.

## Evidence and next checks

[Artifact hashes and scoped observations](recent-concept-source-contracts-1.20.1.json). Original game classes, decompiled text and JAR are not redistributed. Stored baseline constants remain in the existing release-specific baseline index.

Before implementation acceptance, capture resource use, projectile/effect outcomes, input cancellation, allies/enemies, multiplayer authority, attachment off/on and save/load with AoA and TaCZ together. All native gates remain open.
