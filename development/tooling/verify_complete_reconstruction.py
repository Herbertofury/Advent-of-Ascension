"""Independently bind a whole decompiler selection to every original class.

This checks source availability/lineage, never semantic or runtime equivalence.
Original resource bytes remain in the original unmodified archive.
"""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import zipfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def artifact(path):
    path = Path(path)
    with path.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    return dict(path=str(path), bytes=path.stat().st_size, sha256=digest)


def verify_ref(ref):
    actual = artifact(ref['path'])
    require((actual['bytes'], actual['sha256']) == (ref['bytes'], ref['sha256']),
            'Referenced complete file changed: ' + ref['path'])
    return actual


def verify(result, selected_override=None):
    require(not any(result[key] for key in ['semanticEquivalenceVerified',
                'sourceMutationEnabled', 'compileVerified', 'runtimeVerified']),
            'Source recovery cannot certify compilation or behavior')
    verify_ref(result['artifact'])
    with zipfile.ZipFile(result['artifact']['path']) as original:
        physical = original.infolist()
        require(len(physical) == len(result['entries']), 'Original physical membership differs')
        for ordinal, (info, entry) in enumerate(zip(physical, result['entries'])):
            raw = original.read(info)
            require((ordinal, info.filename, info.is_dir(), len(raw), hashlib.sha256(raw).hexdigest()) ==
                    tuple(entry[k] for k in ['ordinal', 'path', 'directory', 'bytes', 'sha256']),
                    'Original physical entry changed: ' + info.filename)
    classes = {r['ordinal']: r for r in result['entries'] if not r['directory'] and r['path'].endswith('.class')}
    require(len(classes) == result['classCount'] == len(result['classes']), 'Class count differs')
    for entry in result['classes']:
        require(all(entry[k] == classes[entry['ordinal']][k] for k in ['path', 'sha256', 'bytes']),
                'Original class record differs')
    verify_ref(result['selectedSourceArchive'])
    with zipfile.ZipFile(result['selectedSourceArchive']['path']) as selected:
        source_members = {i.filename: selected.read(i) for i in selected.infolist()}
        require(len(source_members) == len(selected.infolist()), 'Ambiguous selected ZIP entries')
    metadata = json.loads(source_members.pop('.enderloom/reconstruction-lineage.json'))
    require(metadata['originalArtifact'] == result['artifact'] and
            metadata['sourceMutationEnabled'] is False and metadata['semanticEquivalenceVerified'] is False,
            'Selected source authority/claim differs')
    if selected_override is not None:
        source_members = selected_override
    seen, mappings, selections, providers = [], [], [], Counter()
    expected_names = set()
    for group in result['groups']:
        verify_ref(group['normalizedInput'])
        providers_by_name = {p['name']: p for p in group['providers']}
        mapping_by_ordinal = {m['ordinal']: m for m in group['entryMappings']}
        require(len(mapping_by_ordinal) == len(group['entryMappings']), 'Duplicate class mapping')
        for ordinal, entry in mapping_by_ordinal.items():
            require(all(entry[k] == classes[ordinal][k] for k in ['path', 'sha256', 'bytes']),
                    'Class mapping changed')
        for selection in group['sourceSelections']:
            name = selection['selectedProvider']
            require(name in providers_by_name, 'No selected provider')
            assessment = selection['assessments'][name]
            provider = providers_by_name[name]
            schedule = {s['batchOrdinal']: s for s in provider['scheduling']}
            rows = {row['path']: row for row in provider['files']}
            observations = {row['path']: row for row in provider['syntaxObservations']}
            relative = selection['candidatePath']
            require(assessment['providerPassCompleted'] and assessment['eligibleSourceCandidate'] and
                    assessment['file'] == rows[relative] and assessment['syntaxObservation'] == observations[relative],
                    'Selected source is not an eligible exact provider observation')
            syntax = observations[relative]
            require(syntax['syntaxErrors'] == 0 and not syntax['providerFailureMarkers'],
                    'Selected source has syntax errors or a decompiler failure')
            raw = (Path(assessment['outputDirectory']) / relative).read_bytes()
            require((len(raw), hashlib.sha256(raw).hexdigest()) ==
                    (assessment['file']['bytes'], assessment['file']['sha256']), 'Chosen full source bytes changed')
            target = f"version-{group['version']}/java/{selection['sourcePath']}"
            require(target not in expected_names and source_members.get(target) == raw,
                    'Missing, duplicated or changed selected source: ' + target)
            expected_names.add(target)
            ordinals = selection['originalClassOrdinals']
            require(ordinals and len(set(ordinals)) == len(ordinals), 'Empty or repeated source class ownership')
            for ordinal in ordinals:
                mapping = mapping_by_ordinal[ordinal]
                require(mapping['candidatePath'] == relative and schedule[mapping['batchOrdinal']]['completed'],
                        'Selected source came from an incomplete provider pass or different family')
            seen.extend(ordinals)
            providers[name] += 1
        mappings.extend(mapping_by_ordinal)
        selections.extend(dict(row, physicalVersion=group['version']) for row in group['sourceSelections'])
    require(Counter(seen) == Counter(classes.keys()) == Counter(mappings), 'Missing or repeated original class ownership')
    require(set(source_members) == expected_names and metadata['selections'] == selections,
            'Selected archive contains missing/untracked source or different lineage')
    require(result['sourceCandidateCoverageComplete'], 'Producer did not claim complete candidate coverage')
    return dict(originalPhysicalEntries=len(physical), originalClasses=len(classes),
                selectedWholeSourceFiles=len(expected_names), selectedProviders=dict(providers),
                primaryFailuresRetained=not result['executionComplete'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('work')
    parser.add_argument('--verify-only', action='store_true', help='Read-only verification; preserve existing proof files')
    args = parser.parse_args()
    work = Path(args.work)
    receipt = read(work / 'normal-bounded-whole-reconstruction-receipt.json')
    for key in ['request', 'producer', 'worker', 'workerBuild', 'java', 'reply']:
        verify_ref(receipt[key])
    result = read(receipt['reply']['path'])['result']
    counts = verify(result)
    inventory = read(work / 'complete-permanent-1710-class-membership.json')
    original_sets = []
    for source in inventory['originalAuthorities']:
        verify_ref(source['artifact'])
        with zipfile.ZipFile(source['artifact']['path']) as archive:
            original_sets.append({i.filename for i in archive.infolist() if i.filename.endswith('.class')})
    snapshot_only = original_sets[0] - original_sets[1]
    covered = set()
    source_files = set()
    ordinal_map = {r['ordinal']: r['path'] for r in result['classes']}
    for group in result['groups']:
        for row in group['sourceSelections']:
            matching = {ordinal_map[n] for n in row['originalClassOrdinals']} & snapshot_only
            covered.update(matching)
            if matching:
                source_files.add(row['sourcePath'])
    require(covered == snapshot_only, 'Snapshot-only whole families are not covered')
    faults = []
    for name in ['missing-original-class', 'unproved-runtime-claim', 'missing-selected-source', 'changed-selected-source']:
        altered = deepcopy(result)
        override = None
        if name == 'missing-original-class':
            altered['groups'][0]['sourceSelections'][0]['originalClassOrdinals'] = []
        elif name == 'unproved-runtime-claim':
            altered['runtimeVerified'] = True
        else:
            with zipfile.ZipFile(result['selectedSourceArchive']['path']) as archive:
                override = {i.filename: archive.read(i) for i in archive.infolist() if i.filename.endswith('.java')}
            first = next(iter(override))
            if name == 'missing-selected-source':
                del override[first]
            else:
                override[first] += b'\n// generated invalid lineage control\n'
        try:
            verify(altered, override)
        except ValueError as error:
            faults.append(dict(control=name, generatedFault=True, rejected=True, reason=str(error)))
        else:
            raise ValueError('Verifier accepted generated broken control: ' + name)
    output = work / 'independent-complete-snapshot-source-candidates.json'
    require(args.verify_only or not output.exists(), 'Retain existing independent acceptance')
    proof = dict(passed=True, analysisOnly=True, **counts,
                 snapshotOnlyOriginalClasses=len(snapshot_only), snapshotOnlyWholeSourceFiles=len(source_files),
                 receipt=artifact(work / 'normal-bounded-whole-reconstruction-receipt.json'),
                 selectedSourceArchive=artifact(result['selectedSourceArchive']['path']),
                 generatedBrokenControls=faults, verifier=artifact(__file__),
                 originalSourceFidelity=False, semanticEquivalenceVerified=False,
                 targetCompilationVerified=False, gameplayVerified=False, completeAoAPort=False,
                 scope='Every original physical entry and class, complete selected source bytes, provider pass/syntax eligibility and source/class lineage. No behavior or port acceptance is inferred.')
    if not args.verify_only:
        output.write_text(json.dumps(proof, indent=2), encoding='utf-8')
        Path(work / 'independent-complete-snapshot-source-candidates.verifier.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(proof))


if __name__ == '__main__':
    main()
