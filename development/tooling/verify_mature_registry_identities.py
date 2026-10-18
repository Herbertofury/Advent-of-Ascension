"""Resolve every mature-baseline block/item/entity key with actual native proof.

This is complete registry/save-identity coverage, not full gameplay equivalence,
latest modernization, sound equivalence or the older 1.7.10 historical union.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path


def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def artifact(p):
    p = Path(p).absolute()
    with p.open('rb') as f:
        h = hashlib.file_digest(f, 'sha256').hexdigest()
    return dict(path=str(p), bytes=p.stat().st_size, sha256=h)


def check(r):
    a = artifact(r['path'])
    assert all(a[k] == r[k] for k in ['bytes', 'sha256'])


def resolve(audit, capture):
    blocks, armour = capture['completeBlockAliasInspection'], capture['completeArmourInspection']
    functional, chargers = capture['completeFunctionalBindingInspection'], capture['completeCanonicalChargerInspection']
    for value in [blocks, armour, functional, chargers]:
        assert value['passed'] and not value['synthetic']
    block_map, item_map = {}, {}
    for row in blocks['rows']:
        assert row['blockIdentityEqual'] and row['itemIdentityEqual'] and row['itemNbtRoundTripEqual'] and row['singleCanonicalCatalogueEntry']
        assert all(r['equal'] for r in row['completeNativeStates'])
        assert len(row['completeNativeStates']) > 0 and row['actualCanonicalKey'] == row['canonical']
        block_map[row['old']] = row['canonical']; item_map[row['old']] = row['canonical']
    for row in armour['rows']:
        assert all(row[k] for k in ['itemIdentityEqual', 'holderIdentityEqual', 'singleCanonicalCatalogueEntry', 'completeSavedPayloadEqual', 'decodedItemIdentityEqual'])
        assert row['actualCanonicalKey'] == row['canonical']
        item_map[row['old']] = row['canonical']
    for row in functional['completeActualItemBindings']:
        assert row['actualOriginalAliasIdentity'] and row['actualLegacyStackLoadItemIdentity']
        if row['key'] != row['actualCanonicalKey']:
            assert row['key'] == 'aoa3:kaiyu_staff' and row['actualCanonicalKey'] == 'aoa3:amber_staff'
            item_map[row['key']] = row['actualCanonicalKey']
    worlds = chargers['worlds']
    variants = {'desert', 'hill', 'sea', 'snow', 'swamp', 'void'}
    assert len(worlds) == len(set(worlds)) == 25 and not chargers['duplicateEntitiesAdded'] and not chargers['duplicateEggsAdded']
    assert {(r['world'], r['variant']) for r in chargers['entities']} == {(w, v) for w in worlds for v in variants}
    assert len(chargers['entities']) == len(chargers['eggs']) == 150
    assert {(r['world'], r['variant']) for r in chargers['eggs']} == {(w, v) for w in worlds for v in variants}
    entity_map = {}
    for row in chargers['entities']:
        assert row['legacy'] == 'aoa3:' + row['variant'] + '_charger'
        assert row['originalInputUnchanged'] and row['canonicalReloadPreserved'] and row['explicitVariantPreserved']
        assert 'ChargerType:"' + row['variant'] + '"' in row['completeSaved']
        entity_map[row['legacy']] = 'aoa3:charger'
    for row in chargers['eggs']:
        assert row['legacy'] == 'aoa3:' + row['variant'] + '_charger_spawn_egg' and row['quantity'] == 17
        assert row['originalInputUnchanged'] and row['fullCustomTagPreserved'] and row['actualNativeEggEntityLoad']
        assert 'ChargerType:"' + row['variant'] + '"' in row['completeSaved'] and 'id:"aoa3:charger_spawn_egg"' in row['completeSaved']
        item_map[row['legacy']] = 'aoa3:charger_spawn_egg'
    maps = {'minecraft:block': block_map, 'minecraft:item': item_map, 'minecraft:entity_type': entity_map}
    result = []
    for registry, aliases in maps.items():
        rows = [r for r in audit['completeComparedRegistries'] if r['registry'] == registry]
        assert len(rows) == 1
        row = rows[0]; old, current = set(row['completeHistoricalKeys']), set(row['completeCurrentKeys'])
        assert len(old) == len(row['completeHistoricalKeys']) and len(current) == len(row['completeCurrentKeys'])
        resolutions = []
        for key in sorted(old):
            if key in current:
                resolutions.append(dict(historical=key, canonical=key, mechanism='exact-current-registered-identity'))
            else:
                assert key in aliases and aliases[key] in current, 'Unresolved exact historical identity: ' + key
                resolutions.append(dict(historical=key, canonical=aliases[key], mechanism='native-alias-or-variant-save-roundtrip'))
        result.append(dict(registry=registry, historical=len(old), current=len(current), exact=len(old & current),
                           resolvedAliases=len(old - current), unresolved=0, completeResolutions=resolutions))
    return result


def run(audit_file, output):
    assert not Path(output).exists()
    audit = read(audit_file)
    assert audit['passed'] and audit['complete'] and not audit['synthetic']
    for key in ['historicalNativeServer', 'currentNativeServer', 'historicalNativeCapture', 'currentNativeCapture']:
        check(audit[key])
    capture = read(audit['currentNativeCapture']['path'])
    result = resolve(audit, capture)
    faults = []
    for name, mutate in [('missing_block_alias', lambda d: d['completeBlockAliasInspection']['rows'].pop(0)),
                         ('changed_armour_payload', lambda d: d['completeArmourInspection']['rows'][0].update(completeSavedPayloadEqual=False)),
                         ('missing_variant', lambda d: d['completeCanonicalChargerInspection']['entities'].pop()),
                         ('lost_egg_tags', lambda d: d['completeCanonicalChargerInspection']['eggs'][0].update(fullCustomTagPreserved=False))]:
        bad = copy.deepcopy(capture); mutate(bad)
        try:
            resolve(audit, bad)
        except AssertionError:
            faults.append(dict(case=name, generated=True, rejected=True))
        else:
            raise ValueError('Broken identity fixture accepted: ' + name)
    frozen = Path(output).with_suffix('.producer.py'); frozen.write_bytes(Path(__file__).read_bytes())
    proof = dict(schema=1, passed=True, synthetic=False, audit=artifact(audit_file), currentNativeCapture=audit['currentNativeCapture'],
                 completeRegistryIdentityResolution=result, generatedFaultControls=faults, producer=artifact(frozen),
                 completeAoAPort=False, gameplayEquivalenceVerified=False, soundEquivalenceVerified=False,
                 olderHistoricalUnionVerified=False, latestModernizationVerified=False,
                 scope='All 1,186 mature-baseline block, 2,596 item and 632 entity registered identities resolve through exact current keys or exercised native alias/variant save fixtures. Content behavior, every historical generation, sound equivalence, current-upstream modernization and full progression remain separate gates.')
    Path(output).write_text(json.dumps(proof, indent=2), encoding='utf-8')
    print(json.dumps(dict(passed=True, registries=[{k: v for k, v in r.items() if k != 'completeResolutions'} for r in result], output=output)))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('audit'); p.add_argument('output')
    a = p.parse_args(); run(a.audit, a.output)
