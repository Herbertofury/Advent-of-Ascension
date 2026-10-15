[Home](README.md) · [Versions](Version-Matrix.md) · [Worlds](Dimensions.md) · [Systems](Systems.md) · [Progress](Progress.md)

# Testing, saves & performance

## Required lanes

1. **Source and package:** accepted inventory, mappings, dependency closure, resource links, exact JVM legality and packaged metadata.
2. **Native client:** title/world load, all visible models/animations/UI/audio/effects, custom interactions and resource reload.
3. **Server:** dedicated and integrated execution, synchronization, AI/spawning, combat and progression.
4. **Worlds:** every accepted dimension, travel in/out, structures, portals, death/respawn and chunk persistence.
5. **Saves:** new and accepted historical saves, clean shutdown/restart, migration of IDs/skills/inventories/entities and rollback on copies.
6. **Compatibility:** required integrations, optional providers both present/absent, and intended renderer/modpack.
7. **Clean replay:** original input to equivalent verified output through Enderloom without manual generated-source surgery.

## Performance invariant

Improve startup and runtime alongside feature work at no capability loss. Measure launch-to-menu, launch-to-usable-world, resource reload, steady-state frame-time tails, server tick time, memory/native/VRAM and cache/disk growth. Keep comparable scenes and complete content. A benchmark with fewer mobs, removed dimensions or disabled animations is not an equivalent-work win.

Use bounded caches, incremental work and profiling before concurrency changes. Never trade safety or save correctness for a faster number. Avoid unbounded scans and backups. Existing C-drive cleanup remains outside this documentation task.

## Evidence receipt

Each pass records source/input hashes, target version/loader/Java, candidate JAR hash, exact test setup, expected/observed behavior, logs/screenshots, elapsed/performance measurements, date, result and remaining failures. Screenshots must be authentic to the tested candidate. Original diagrams and upstream reference images are never presented as runtime proof.


---
Research snapshot: **2026-10-15**. Original documentation for the owner’s Enderloom project. Advent of Ascension is created by **Tslat** and its contributors. [Official mod/source](https://github.com/Tslat/Advent-Of-Ascension) · [Official wiki](https://adventofascension.fandom.com/wiki/Advent_of_Ascension_Wiki) · [Evidence and image credits](Sources-and-Credits.md). Source presence is not target runtime proof.
