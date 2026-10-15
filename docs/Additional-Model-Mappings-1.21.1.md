# Additional model mappings · 1.21.1

Actual geometry and texture resources from **AoA 3.7.16.1**. This page separates active source renderer mappings from unused/historical resource studies. Models and textures by **Tslat and contributors**; independent static documentation renders, not runtime availability proof.

## Eleven explicitly mapped fish variants

![Eleven explicitly mapped fish variants](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mapped-fish-variants.webp)

The pinned active renderer declarations explicitly select shared geometry for these fish. This resolves the filename-only mapping gap; it does not add new mobs to a converted build.

| Resource | Evidence | Texture |
|---|---|---|
| `blue_gemtrap` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/blue_gemtrap.png` |
| `crimson_skipper` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/crimson_skipper.png` |
| `crimson_stripefish` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/crimson_stripefish.png` |
| `green_gemtrap` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/green_gemtrap.png` |
| `pearl_stripefish` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/pearl_stripefish.png` |
| `purple_gemtrap` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/purple_gemtrap.png` |
| `red_gemtrap` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/red_gemtrap.png` |
| `turquoise_stripefish` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/turquoise_stripefish.png` |
| `violet_skipper` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/violet_skipper.png` |
| `white_gemtrap` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/white_gemtrap.png` |
| `yellow_gemtrap` | [Pinned renderer](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/yellow_gemtrap.png` |

## Eight unused or historical resource studies

![Eight unused or historical resource studies](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-unused-resource-studies.webp)

Six pairs use uniquely matching names with textures stored under an `unused` directory. They are resource studies, not verified active renderer assignments. Coratee has two texture variants, but its inspected model class is entirely commented out. That historical intent is recorded rather than represented as active implementation.

| Resource | Evidence | Texture |
|---|---|---|
| `boneback` | Unused JAR texture; unique basename match only | `assets/aoa3/textures/entity/mob/unused/boneback.png` |
| `bugeye` | Unused JAR texture; unique basename match only | `assets/aoa3/textures/entity/mob/unused/bugeye.png` |
| `goalby` | Unused JAR texture; unique basename match only | `assets/aoa3/textures/entity/mob/unused/goalby.png` |
| `night_reaper` | Unused JAR texture; unique basename match only | `assets/aoa3/textures/entity/mob/unused/night_reaper.png` |
| `nightfly` | Unused JAR texture; unique basename match only | `assets/aoa3/textures/entity/mob/unused/nightfly.png` |
| `sea_troll` | Unused JAR texture; unique basename match only | `assets/aoa3/textures/entity/mob/unused/sea_troll.png` |
| `coratee_default` | [Commented historical model](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/model/entity/animal/CorateeModel.java) | `assets/aoa3/textures/entity/animal/lborean/coratee_default.png` |
| `coratee_overgrown` | [Commented historical model](https://github.com/Tslat/Advent-Of-Ascension/blob/7919b5fe48599e6105c5740937ce36c36ef21d16/source/client/model/entity/animal/CorateeModel.java) | `assets/aoa3/textures/entity/animal/lborean/coratee_overgrown.png` |

## Still missing

The modern Trickster geometry has no corresponding texture in the inspected release JAR. No later/earlier texture is silently substituted. Runtime animation, scaling, state selection and gameplay availability remain separate verification work.

[Visual atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Visual-Atlas) · [Render coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage)
