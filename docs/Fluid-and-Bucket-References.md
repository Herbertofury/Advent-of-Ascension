# Fluid and bucket reference gallery

**24 additional version-specific bucket studies** address dynamic Forge models that the ordinary JSON inventory renderer could not resolve. They supplement the regular historical atlas without silently increasing its validated static-model count.

## Minecraft 1.16.5 · AoA 3.6.11

![Eighteen source-defined bucket appearances](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.16.5-fluid-bucket-reference.webp)

The official AoA item JSONs request `forge:bucket`, the `forge:item/bucket_drip` parent and a named fluid. The documentation adapter reconstructs the base bucket and masked fluid layer using the first texture frame and source-defined RGBA tint. These are angled, pixel-extruded artwork references; not newly invented volumetric bucket models.

- **AoA fluids:** Candied Water, Clear Water and Toxic Waste.
- **Tinkers-dependent bucket registrations:** Molten Baronyte, Blazium, Elecanium, Emberstone, Ghastly, Ghoulish, Limonite, Lunar, Lyon, Mystite, Rosite, Shyrestone, Skeletal, Varsium and Charger.

The [Tinkers integration source](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/integration/tinkersconstruct/TinkersFluids.java) registers full block/bucket entries only when that integration is active. Otherwise it creates fluid-only holders. A bucket model existing inside the JAR is therefore not proof that the item is available in an AoA-only installation.

For molten metals, the active integration selects [Tinkers' molten still texture](https://github.com/SlimeKnights/TinkersConstruct/blob/41022117ee515c6f5b6b3d8a4b9853840fb2b88f/src/main/resources/assets/tconstruct/textures/block/fluid/molten/still.png). Molten Charger instead uses the builder's water-texture default. Ghastly and Ghoulish share the same source color; their matching previews are intentional.

## Minecraft 1.20.1 · AoA 3.7.1

![Three source-defined bucket appearances](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-fluid-bucket-reference.webp)

The three model JSONs select `forge:fluid_container`, `forge:item/bucket` and their registered fluid. Candied Water, Toxic Waste and Tar use the non-dripping mask. The exact four numeric tint arguments were independently verified in the official AoA 3.7.1 class files: Candied Water `(255,105,180,200)`, Toxic Waste `(38,42,23,255)`, Tar `(35,35,35,255)`. The read-only decoder inspected constant sequences and the RGBA conversion call; it did not load or execute game code.

## Minecraft 1.21.1 · AoA 3.7.16.1

![Three modern NeoForge bucket appearances](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-fluid-bucket-reference.webp)

The current pinned artifact uses `neoforge:fluid_container` and the NeoForge bucket parent. All three `getTintColor()` methods were inspected directly in that artifact: CandiedWaterClientExtension, ToxicWasteClientExtension and TarClientExtension. Their four integer arguments to the ARGB helper match the displayed source-defined colors. These studies use this release's own textures and vanilla client assets.

[NeoForge 1.21.1 loader source](https://github.com/neoforged/NeoForge/blob/00c6a3fd23d80ce54ec834a7e25d09fba37927e9/src/main/java/net/neoforged/neoforge/client/model/DynamicFluidContainerModel.java) · [Bucket parent](https://github.com/neoforged/NeoForge/blob/00c6a3fd23d80ce54ec834a7e25d09fba37927e9/src/main/resources/assets/neoforge/models/item/bucket.json)

## Evidence and rendering limits

- [Forge 1.16.x DynamicBucketModel](https://github.com/MinecraftForge/MinecraftForge/blob/b3426008d3c3a256fcfaf9d780682c45ab1d1fdb/src/main/java/net/minecraftforge/client/model/DynamicBucketModel.java): base layer, fluid mask, optional cover, tint and luminosity behavior.
- [Forge 1.16.x dripping bucket parent](https://github.com/MinecraftForge/MinecraftForge/blob/b3426008d3c3a256fcfaf9d780682c45ab1d1fdb/src/main/resources/assets/forge/models/item/bucket_drip.json) and [fluid mask](https://github.com/MinecraftForge/MinecraftForge/blob/b3426008d3c3a256fcfaf9d780682c45ab1d1fdb/src/main/resources/assets/forge/textures/item/mask/bucket_fluid_drip.png).
- [Forge 1.20.x DynamicFluidContainerModel](https://github.com/MinecraftForge/MinecraftForge/blob/243490d78001917c7e6ee6e94b45ef98776aa36f/src/main/java/net/minecraftforge/client/model/DynamicFluidContainerModel.java) and [bucket parent](https://github.com/MinecraftForge/MinecraftForge/blob/243490d78001917c7e6ee6e94b45ef98776aa36f/src/main/resources/assets/forge/models/item/bucket.json).
- [AoA fluid builder defaults](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/util/FluidUtil.java) and [core fluid registrations](https://github.com/Tslat/Advent-Of-Ascension/blob/e97502da8bdd6081b6acc4635f03296d3e2e69a0/source/common/registration/AoABlocks.java).
- [Machine-readable pins and artifact tint evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/fluid-bucket-reference-evidence.json).

The Forge commits are pinned reference implementations, not a claim that a particular installed Forge build was tested. These independent showcases composite a single fluid frame into its mask and apply ordinary documentation lighting. They do not reproduce fluid animation, emissive shaders, every translucent blend, exact layer depth, game GUI perspective or runtime item overrides. Integration registration and renderer parity still require target-game tests.

Credits: AoA artwork/designs by Tslat and contributors; Minecraft bucket/water artwork by Mojang; mask/model conventions by Minecraft Forge contributors; molten texture by SlimeKnights/Tinkers' Construct contributors. Original upstream files are not bundled in the published documentation.

[Historical inventory galleries](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-Galleries) · [Render coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage)
