# Model Observatory: local archives and troubleshooting

[Open the local-JAR Model Observatory](https://herbertofury.github.io/Advent-of-Ascension/)

Inspect supported Bedrock/GeckoLib cuboid geometry and textures directly from an AoA archive. The viewer reads files as data; it does not launch Minecraft or execute mod classes.

![Smash source-model reference, not an in-game screenshot](https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/previews/1.21.1-mob-smash.png)

## Choose the quickest route

- **Browse without opening a JAR:** use [creature turntables](https://herbertofury.github.io/Advent-of-Ascension/model-turntable.html), [block models](https://herbertofury.github.io/Advent-of-Ascension/block-models.html?v=1.21.1) or [plant states](https://herbertofury.github.io/Advent-of-Ascension/crop-states.html?v=1.21.1).
- **Inspect your local archive:** choose its .jar or .zip file. Its contents remain in the browser; the viewer does not upload them.
- **Use the pinned official archive:** the download button fetches the 139,631,628-byte AoA 3.7.16.1 / Minecraft 1.21.1 archive from Modrinth and checks its SHA-512. This happens only when requested.

Normal webpage assets still load from the site. “Local archive contents stay in your browser” is not a claim that visiting the website causes no network requests.

## Controls

1. Open a supported archive and choose a model from the searchable list.
2. Drag to orbit, or focus the preview and use arrow keys.
3. Scroll or use + / − to zoom. Home or Reset returns to the default view.
4. Choose a texture candidate when variants are listed.
5. Auto-rotate is opt-in and stops when the page becomes hidden.
6. Save preview PNG becomes available only when the preview is ready. It creates a Download PNG link for the resulting image.

A saved PNG is an independent static model reference, not a Minecraft runtime screenshot or proof that a restored mob works in-game.

## What “geometry resources” means

| Inspected release | Archive entries | Matching geometry resources |
|---|---:|---:|
| 1.12.2 / 3.3.6 | 18,275 | 0 |
| 1.16.5 / 3.6.11 | 22,131 | 46 |
| 1.20.1 / 3.7.1 | 20,891 | 116 |
| 1.21.1 / 3.7.16.1 | 20,552 | 130 |

This table counts paths under assets/aoa3/geo/ ending in .geo.json. It is not a mob count, a complete Java-model inventory or a runtime support guarantee. The inspected 1.21.1 archive’s 130 matching resources were all read successfully and converted to finite cuboid vertex buffers in the documentation tests.

A release with no matching geometry is not automatically diagnosed as broken or exclusively Java-based. It can be an unsupported layout or an unrelated archive. The historical source atlases remain available for Java-coded model references.

[Archive-layout evidence](https://herbertofury.github.io/Advent-of-Ascension/observatory-archive-coverage.json) · [Historical model atlas](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Legacy-Model-Atlas) · [Version matrix](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Version-Matrix)

## Texture and appearance limits

Texture candidates are selected using archive paths and filenames. That is a convenience heuristic, not certification of the mod’s custom renderer mapping. A matching texture can still require special layers, animation logic, tints or runtime state that this rest-pose viewer does not reproduce.

The software fallback uses per-pixel depth and cutout transparency. Partial transparency, custom render layers and animation expressions can differ from the game. This local-archive renderer is separate from the lighter shared software core used by the block, plant-state and workstation viewers.

For local files, check the release you actually selected. The pinned official-download button identifies one known archive; it does not certify arbitrary local filenames or a private merged build.

## Rapid switching and recovery

The viewer now tracks model, texture and archive requests so a slow earlier read cannot replace a later selection. A superseded error also cannot clear the newer preview.

A deterministic test reproduced the old model-selection problem: model A finished reading after model B and incorrectly replaced B’s displayed name. The corrected path keeps B selected. Separate checks cover texture switching, archive switching, stale failures and overlapping PNG exports. Export filenames are captured with the requested preview; a late older export cannot replace the newer download link.

When a new model or texture is loading, drawing and PNG capture wait for a ready model/texture pair. Selecting a local file cancels a pending official download; superseded download results cannot replace the selected local archive.

## Archive limits and useful errors

- The existing local-file size limit is 1 GB.
- The existing per-entry uncompressed limit is 32 MiB.
- Deflated entries are now accumulated through a bounded reader. It cancels when output exceeds the declared entry size or the hard limit, rather than allocating the complete output before checking its length.
- Stored entries must also match their declared uncompressed size.
- Truncated payloads, encrypted entries and unsupported compression methods are rejected.
- ZIP64 is not supported by this viewer.

These checks are not a comprehensive hostile-archive security audit. The browser still needs memory for the archive, decompression buffers, decoded images and geometry. Use trusted releases; the entry accumulation limit is not an absolute browser-memory bound.

## Validation and provenance

- [Original-viewer audit and regression scope](https://herbertofury.github.io/Advent-of-Ascension/observatory-audit-evidence.json)
- [All 130 geometry read receipts](https://herbertofury.github.io/Advent-of-Ascension/observatory-zip-read-receipts.json)
- [Source and art credits](https://github.com/Herbertofury/Advent-of-Ascension/wiki/Sources-and-Credits)

The viewer’s ZIP output was checked independently against Python’s ZIP reader for every matching 1.21.1 geometry resource. Stored/deflated fixtures, early cancellation, malformed sizes, encryption and unsupported methods are covered. Geometry conversion and drawing algorithms remain unchanged apart from the ready-state gate. No gameplay, live mod compatibility, browser FPS improvement or GPU certification is claimed by these tests.

Original AoA geometry and textures are by Tslat and contributors. The archive reader, renderer and explanatory documentation are independent tools for inspecting source data.
