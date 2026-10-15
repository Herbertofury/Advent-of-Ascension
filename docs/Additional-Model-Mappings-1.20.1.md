# Additional model mappings · 1.20.1

Thirteen official **AoA 3.7.1 / Minecraft 1.20.1** model/texture pairs supplement the initial geometry gallery: eleven fish variants and two Coratee appearances. The pinned 1.20 source branch supplies mapping evidence; it is not asserted to be byte-for-byte identical to the release source.

![Named 1.20.1 fish and Coratee variants](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.20.1-shared-model-variants.webp)

All thirteen model/texture byte pairs exactly matched already reviewed renders from the other inspected releases, so those corrected renders were reused rather than recomputed. Models and textures by **Tslat and contributors**. Static documentation poses do not prove animation or target runtime behavior.

## Coratee requires separate runtime validation

The artifact contains both real Coratee textures, but its texture-selection method uses a model-path helper. These pictures deliberately select the texture resources directly. They must not be used as evidence that the in-game selection path works. See the [bytecode-backed finding and fix checklist](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Source-Findings-and-Fixes).

| Resource | Mapping evidence | Texture |
|---|---|---|
| `blue_gemtrap` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/blue_gemtrap.png` |
| `crimson_skipper` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/crimson_skipper.png` |
| `crimson_stripefish` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/crimson_stripefish.png` |
| `green_gemtrap` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/green_gemtrap.png` |
| `pearl_stripefish` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/pearl_stripefish.png` |
| `purple_gemtrap` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/purple_gemtrap.png` |
| `red_gemtrap` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/red_gemtrap.png` |
| `turquoise_stripefish` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/turquoise_stripefish.png` |
| `violet_skipper` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/violet_skipper.png` |
| `white_gemtrap` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/white_gemtrap.png` |
| `yellow_gemtrap` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/AoAEntityRendering.java) | `assets/aoa3/textures/entity/animal/fish/yellow_gemtrap.png` |
| `coratee_default` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/model/entity/animal/CorateeModel.java) | `assets/aoa3/textures/entity/animal/lborean/coratee_default.png` |
| `coratee_overgrown` | [Pinned source](https://github.com/Tslat/Advent-Of-Ascension/blob/85d6beba07e3a09032834dcf79b5a01f411092c3/source/client/model/entity/animal/CorateeModel.java) | `assets/aoa3/textures/entity/animal/lborean/coratee_overgrown.png` |

[1.20.1 geometry gallery](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Geometry-Gallery-1.20.1) · [Coverage](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Render-Coverage)
