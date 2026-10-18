# Renderer compatibility continuation · 2026-10-17

The current owner-local Enderloom playtest now uses the repaired whole-mod JAR
`5df930e3b8e88c5f5f12347fe020adea72184009b944af10f9aa119f6dc07643`.
The previous verified profile and worlds remain available. This is a tested
renderer repair; the complete historical/latest AoA merge remains unfinished.
Tslat and contributors remain credited, and vanilla hearts remain the default.

All **24,103** preceding archive members remain. The new JAR has **24,106**
members: three added state-helper classes, one repaired overlay class and a new
build timestamp. Every other complete program and resource member is unchanged.
All preceding Extraction, Anima, Holly Arrow, Pixon tribute and XP fixes remain.

The restored overlay used three direct OpenGL signatures in seven state reads.
Those reads now query the active renderer's real state: Minecraft's normal
platform API or the selected optional Hari native state interface. Renderer
selection and method handles are cached; failed native access never invents
defaults or silently falls back to physical OpenGL. Artwork, fades, geometry,
fluid ownership and complete state restoration remain.

The complete native client/server runs passed. **24 OpenGL and 24 actual Hari
Vulkan GUI draws** preserve depth, blend, write mask, separate RGB/alpha factors,
shader, texture and tint, including nondefault constant blend factors. Tests run
at the real Forge GUI boundary inside an active render pass. Generated fixture
errors remain recorded: early class loading, a remapped callback and an invalid
end-of-frame draw were corrected. These failures were not promoted or hidden.

[Minecraft Vulkan Hybrid](https://github.com/Herbertofury/Minecraft-Vulkan-Hybrid/wiki)
is the user-confirmed renderer. The exact selected Hari62 SHA-256 is
`714106dca1ed653c1cf360863a778ff5850d12960e52e3c722062b69cf8186b3`.
The production test requires native Vulkan and its documented LWJGL stack
setting. World rendering/movement and clean shutdown passed in the isolated
renderer fixture. Its development seed contains 31 GeckoLib/SmartBrainLib example
registry entries absent in production; it does not certify save migration or a
clean Hari production-world test. The separate normal standalone production
server save/restart and signed-in client test use a clean production seed.

Enderloom's Windows development workflow also resolves each explicitly selected
input through its real file handle. All bytes and file identity are checked
before native admission; 89 of 91 inputs required a physical path under Codex's
redirected storage. No source authority, input choice or integrity check is lost.

The **2,000 FPS objective remains unmeasured and unmet**. This update does not
claim full renderer/content/pack compatibility, raster parity, multiplayer,
migration, natural full progression or the complete historical/latest union.
Representative dimensions, entities, fluids, particles, weapons and shaders,
followed by matched full-resolution frame-time testing, remain required.

[Exact current metadata](current-playtest.json) ·
[Renderer receipt hashes and limits](renderer-compatibility-2026-10-17.json) ·
[Whole archive inventory](current-artifact-inventory.json).
Only original maintenance tooling and factual metadata are published here;
original AoA code/assets and the modified JAR remain local.
