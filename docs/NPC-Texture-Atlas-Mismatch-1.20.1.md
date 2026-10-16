# Nine NPC texture-atlas mismatches in AoA 3.7.1

**Version: Minecraft 1.20.1, AoA3-1.20.1-3.7.1-all.jar.** These are static resource/bytecode findings and proposed restoration references. The game has not been patched or run to certify a fix.

## What the released code does

The released `AoAEntityRendering.humanoidLayerDefinition` supplier creates a vanilla humanoid mesh with `CubeDeformation.NONE`, zero vertical offset and a **64×64 texture atlas**. Nine inspected NPC registrations use that supplier, `HumanoidModel::new`, and a **64×32 PNG**.

Texture dimensions need not always equal the model's atlas dimensions, but here the humanoid mesh's UVs and the old 64×32 NPC layout visibly disagree. The static reconstruction reproduces the misplaced texture bands. Changing the declared atlas height to 32, without changing the seven-part geometry or PNG, yields the intended-looking layout below.

The neutral humanoid mesh was extracted from the official Minecraft 1.20.1 `HumanoidModel.createMesh` factory using a restricted symbolic reader. Unsupported operations stop extraction. This does not execute game code. Mojang's official mappings identify the class and method; class hashes, method calls and the released AoA supplier bytecode are retained in the evidence.

## Compare the released mapping with the proposed correction

The left image keeps the released 64×64 atlas. The right changes only atlas height to 32. Both use the exact released NPC texture and identical neutral geometry. Runtime animation, equipment and lighting are outside this comparison.

| NPC | Released atlas configuration | Proposed 64×32 atlas reference |
|---|---|---|
| [Creep Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Acreep_banker) | ![Creep Banker: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-creep_banker.webp) | ![Creep Banker: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-creep_banker.webp) |
| [Crystal Trader](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Acrystal_trader) | ![Crystal Trader: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-crystal_trader.webp) | ![Crystal Trader: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-crystal_trader.webp) |
| [Dungeon Keeper](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Adungeon_keeper) | ![Dungeon Keeper: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-dungeon_keeper.webp) | ![Dungeon Keeper: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-dungeon_keeper.webp) |
| [Explosives Expert](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Aexplosives_expert) | ![Explosives Expert: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-explosives_expert.webp) | ![Explosives Expert: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-explosives_expert.webp) |
| [Metalloid](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Ametalloid) | ![Metalloid: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-metalloid.webp) | ![Metalloid: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-metalloid.webp) |
| [Naturalist](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Anaturalist) | ![Naturalist: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-naturalist.webp) | ![Naturalist: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-naturalist.webp) |
| [Shyre Archer](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Ashyre_archer) | ![Shyre Archer: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-shyre_archer.webp) | ![Shyre Archer: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-shyre_archer.webp) |
| [Shyre Banker](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Ashyre_banker) | ![Shyre Banker: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-shyre_banker.webp) | ![Shyre Banker: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-shyre_banker.webp) |
| [Token Collector](https://herbertofury.github.io/Advent-of-Ascension/bestiary-explorer.html?v=1.20.1&entity=aoa3%3Atoken_collector) | ![Token Collector: released atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-token_collector.webp) | ![Token Collector: proposed atlas](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-bestiary-proposed-token_collector.webp) |

## Restoration checklist

- [ ] Confirm the target Enderloom build still uses this exact supplier and texture layout.
- [ ] Use a separate 64×32 layer definition for these legacy NPC textures, or deliberately convert each texture to a correct 64×64 layout. Do not change unrelated NPCs globally.
- [ ] Verify head/hat, torso, mirrored arms and mirrored legs at front, back and side views.
- [ ] Check idle/walk animations, equipment layers, baby/adult scaling where supported, resource-pack overrides and hitboxes in game.
- [ ] Add a targeted regression fixture for each of the nine registrations and preserve the original texture hashes.
- [ ] Treat the comparison image as a proposed fix until live tests pass.

## Reproducible evidence

- [Released NPC registrations, exact texture paths and hashes](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/humanoid-portrait-links-1.20.1.json)
- [Official mesh extraction trace and released layer supplier](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/vanilla-humanoid-1.20.1-evidence.json)
- [Proposed atlas comparison records](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/humanoid-proposed-portrait-links-1.20.1.json)
- [Other released renderer gaps](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Renderer-Gaps-1.20.1)
