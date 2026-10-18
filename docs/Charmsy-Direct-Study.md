# Charmsy × Punchy: direct release study

Inspected 18 October 2026. Downloaded the actual [Charmsy 1.0.0 release](https://modrinth.com/resourcepack/charmsy/version/1.0.0), version ID `AYwmKVhE`, from the official Modrinth CDN. Its SHA-1 matches the release metadata: `9aca0722a284938a753934fa534b150abf026b36`. This was static file inspection, not an in-game test.

## What the archive actually contains

- 217 ZIP entries including directories; 125 item-part definitions and 18 geometry JSONs.
- Nine charm selector names across sword/spear definitions: allay, axol, bee, camel, chicken, creeper, puffer, warden and zombie, each ending `_charm`.
- Each inspected definition supplies item identifiers, a `customName`, geometry, textures, bone-specific textures and `bone_physics` configuration. All 125 referenced geometry paths resolve inside the ZIP.
- Separate sword and spear inspection animations declare lengths 15.75 and 10.2083. Their animated bones include both arms and the right item grip. Those are data values, not measured in-game timing.
- The allay diamond-sword definition configures a forward-mode chain pendulum and full-mode wing movement, with explicit angular limits and motion/camera sensitivity. This provides a useful data-driven attachment/secondary-motion reference; it does not prove that its numeric settings fit TaCZ gun rigs.
- Pack metadata advertises format ranges and overlays. Declared ranges do not establish working behavior on every Minecraft or Punchy version.

## What to carry into our architecture

Separate the charm's stable identity, attachment socket, geometry/material, secondary-motion profile, unlock record and gameplay bonus. The visible name may be renamed by the player; it should not be the authority for whether a boss-earned bonus is owned. Resolve earned ownership and bonus rules on the server, and render the attached collectible on the client.

Cache parsed definitions when resources load. Rebuild only affected weapon assemblies when their revision changes. Use bounded secondary motion, reset safely on teleport/weapon swap, and test collision clearance against hands and reload parts. Provide a no-swing setting without removing the earned bonus.

The inspected resource pack is a presentation reference. The requested boss/achievement unlocks, functional bonuses and AoA/TaCZ adapters require our own implementation and validation. Do not infer those systems from charm model files.

## Rights and evidence

The [project page](https://modrinth.com/mod/charmsy) lists All Rights Reserved. Study the organization and behavior, link and credit the reference, and create original AoA charm assets. This study does not republish the archive's geometry, textures or animation keyframes.

[File hashes and static inventory](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/charmsy-direct-study-evidence.json) · [Our earned charm and effects roadmap](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Charms-and-Effect-Customization)
