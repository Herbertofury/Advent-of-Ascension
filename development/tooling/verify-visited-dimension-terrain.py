"""Inspect actual saved terrain around every real multiplayer dimension visit.

Read-only Anvil/NBT inspection supplements native FULL-chunk generation and
the actual signed-in client visits. It never fills voids, edits a world, substitutes
a terrain implementation, or certifies original-world/biome/feature parity.
"""
import argparse
import collections
import copy
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import zlib


def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def ref(p):
    p = Path(p).absolute()
    with p.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    return dict(path=str(p), bytes=p.stat().st_size, sha256=digest)


def check(r):
    actual = ref(r['path'])
    assert all(actual[k] == r[k] for k in ('bytes', 'sha256')), r['path']


def primitive(tag, pattern):
    return struct.unpack(pattern, tag[1])[0]


def compound(tag):
    assert tag[0] == 10
    return tag[1]


def text(tag):
    assert tag[0] == 8
    return tag[1].decode('utf-8')


def palette_counts(container, cells, min_bits, names):
    palette = container[b'palette']
    assert palette[0] == 9 and palette[1][0] == (10 if names else 8)
    rows = palette[1][1]
    labels = [text(compound(r)[b'Name']) if names else text(r) for r in rows]
    assert labels
    if len(labels) == 1:
        assert b'data' not in container or not container[b'data'][1]
        return collections.Counter({labels[0]: cells})
    bits = max(min_bits, (len(labels)-1).bit_length())
    per_long = 64//bits
    data = container[b'data']
    assert data[0] == 12 and len(data[1]) == math.ceil(cells/per_long)*8
    longs = struct.unpack('>'+'Q'*(len(data[1])//8), data[1])
    mask, counts = (1 << bits)-1, collections.Counter()
    for i in range(cells):
        index = (longs[i//per_long] >> ((i % per_long)*bits)) & mask
        assert index < len(labels), 'Invalid saved native block/biome palette'
        counts[labels[index]] += 1
    assert sum(counts.values()) == cells
    return counts


def main(a):
    out = Path(a.output)
    assert not out.exists()
    mp, native = read(a.multiplayer), read(a.native_server)
    assert mp['passed'] and mp['actualRequiredVulkan'] and mp['inventorySavedAndReloaded']
    assert mp['finalServerExit']['exit_code'] == 0 and native['nativeServerAdmissionVerified']
    check(mp['canonicalProduct'])
    assert mp['canonicalProduct']['sha256'] == native['build']['artifacts'][0]['sha256']
    capture_path = Path(native['build']['build_root'])/'run/enderloom-forge1201-whole-world-generation.json'
    native_chunks = read(capture_path)
    assert native_chunks['passed'] and native_chunks['complete'] and not native_chunks['synthetic'] and not native_chunks['errors']
    dimensions = sorted(v['dimension'] for v in mp['dimensionVisits'])
    assert len(dimensions) == len(set(dimensions)) == 28
    groups = collections.defaultdict(list)
    for c in native_chunks['completedChunks']:
        assert c['status'] == 'minecraft:full' and sum(r['count'] for r in c['completeStateCensus']) == c['completeBlockStates']
        assert sum(r['count'] for r in c['completeStateCensus'] if r['state'] not in ('Block{minecraft:air}', 'Block{minecraft:cave_air}', 'Block{minecraft:void_air}')) == c['nonAirStates']
        groups[c['dimension']].append(c)
    assert sorted(groups) == dimensions and all(len(c) == 2 for c in groups.values())
    assert all(sum(r['nonAirStates'] for r in c) > 0 for c in groups.values())
    helper = Path(__file__).parent/'lib/entity-nbt-identity.py'
    spec = importlib.util.spec_from_file_location('complete_terrain_nbt', helper)
    typed = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(typed)
    world = Path(mp['worldPath'])
    assert world.is_dir() and (world/'level.dat').is_file()
    buffers, regions, results = {}, {}, []
    air = {'minecraft:air', 'minecraft:cave_air', 'minecraft:void_air'}
    for visit in mp['dimensionVisits']:
        dimension = visit['dimension']
        namespace, name = dimension.split(':', 1)
        assert namespace == 'aoa3' and '/' not in name and '..' not in name
        cx, cz = (math.floor(visit['telemetry']['position'][i])//16 for i in (0, 2))
        cases, blocks, biomes = [], collections.Counter(), collections.Counter()
        for x in range(cx-1, cx+2):
            for z in range(cz-1, cz+2):
                path = world/'dimensions'/namespace/name/'region'/f'r.{x//32}.{z//32}.mca'
                if path not in buffers:
                    before = ref(path)
                    raw = path.read_bytes()
                    assert ref(path) == before and len(raw) >= 8192 and len(raw) % 4096 == 0
                    buffers[path], regions[path] = raw, before
                raw = buffers[path]
                location = struct.unpack_from('>I', raw, ((x % 32)+(z % 32)*32)*4)[0]
                sector, sectors = location >> 8, location & 255
                assert sector >= 2 and sectors > 0 and (sector+sectors)*4096 <= len(raw)
                start = sector*4096
                size, compression = struct.unpack_from('>IB', raw, start)
                assert 1 < size <= sectors*4096-4 and compression in (1, 2, 3)
                payload = raw[start+5:start+4+size]
                payload = gzip.decompress(payload) if compression == 1 else zlib.decompress(payload) if compression == 2 else payload
                reader = typed.Reader(payload)
                kind = reader.number('>B')
                reader.text()
                chunk = compound(reader.tag(kind))
                assert reader.offset == len(payload) and text(chunk[b'Status']) == 'minecraft:full'
                assert primitive(chunk[b'xPos'], '>i') == x and primitive(chunk[b'zPos'], '>i') == z
                sections = chunk[b'sections']
                assert sections[0] == 9 and sections[1][0] == 10
                state_counts, biome_counts = collections.Counter(), collections.Counter()
                ys = set()
                for section in sections[1][1]:
                    section = compound(section)
                    y = primitive(section[b'Y'], '>b')
                    assert y not in ys
                    ys.add(y)
                    if b'block_states' in section:
                        state_counts.update(palette_counts(compound(section[b'block_states']), 4096, 4, True))
                    if b'biomes' in section:
                        biome_counts.update(palette_counts(compound(section[b'biomes']), 64, 1, False))
                non_air = sum(n for name, n in state_counts.items() if name not in air)
                assert biome_counts and state_counts
                blocks.update(state_counts)
                biomes.update(biome_counts)
                cases.append(dict(x=x, z=z, status='minecraft:full', nonAirStates=non_air,
                                  completeSavedStates=sum(state_counts.values()), sectionY=sorted(ys)))
        assert len(cases) == 9 and sum(c['nonAirStates'] for c in cases) > 0, 'Visited area contains no generated non-air terrain/structure: '+dimension
        results.append(dict(dimension=dimension, actualVisitPosition=visit['telemetry']['position'],
                            completeNearbyChunks=cases, nonAirStates=sum(c['nonAirStates'] for c in cases),
                            blockCounts=dict(sorted(blocks.items())), biomeCellCounts=dict(sorted(biomes.items())),
                            nativeFullChunks=groups[dimension], nativeNonAirStates=sum(c['nonAirStates'] for c in groups[dimension])))
    for path, identity in regions.items():
        assert ref(path) == identity, 'Owned production region changed during read-only verification'
    assert len(results) == 28 and sum(len(r['completeNearbyChunks']) for r in results) == 252
    frozen = Path(str(out)+'.verifier.py')
    frozen.write_bytes(Path(__file__).read_bytes())
    result = dict(passed=True, synthetic=False, readOnly=True, multiplayer=ref(a.multiplayer),
                  nativeServer=ref(a.native_server), canonicalProduct=mp['canonicalProduct'],
                  nativeWholeGeneration=ref(capture_path), dimensions=results,
                  completeVisitedDimensions=28, completeNearbyProductionChunks=252,
                  completeNativeGenerationChunks=56, allSelectedChunksFull=True,
                  everyVisitedAreaHasGeneratedNonAirContent=True,
                  intentionalVoidOutskirtsNotFilled=True, worldFilesUnchanged=True,
                  sourceRegions=list(regions.values()), verifier=ref(frozen), nbtReader=ref(helper),
                  originalTerrainRasterParityVerified=False, completeBiomeAndFeatureParityVerified=False,
                  fullSurvivalVerified=False, completeAoAPort=False)
    with out.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
    print(json.dumps({k: result[k] for k in ('passed', 'completeVisitedDimensions', 'completeNearbyProductionChunks', 'completeNativeGenerationChunks', 'everyVisitedAreaHasGeneratedNonAirContent')}))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('multiplayer', 'native_server', 'output'):
        p.add_argument(name)
    main(p.parse_args())
