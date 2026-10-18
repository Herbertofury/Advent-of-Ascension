"""Verify complete selected native family receipts against the exact admitted mod.

This verifies scoped native fixtures. It never certifies the whole historical
union, natural full playthrough, public release or untested target cells.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import zipfile


def require(value, message):
    if not value:
        raise ValueError(message)


def artifact(path):
    path = Path(path).absolute()
    digest = hashlib.sha256()
    size = 0
    with path.open('rb') as source:
        while chunk := source.read(1024 * 1024):
            digest.update(chunk)
            size += len(chunk)
    return dict(path=str(path), sha256=digest.hexdigest(), bytes=size)


def check(ref):
    actual = artifact(ref['path'])
    require((actual['sha256'], actual['bytes']) == (ref['sha256'], ref['bytes']), 'Changed complete artifact: ' + ref['path'])
    return actual


def validate(capture):
    xp, anima, extraction = [capture[key] for key in ['skillXpBoundaryInspection', 'animaInspection', 'extractionInspection']]
    for value in [xp, anima, extraction]:
        require(value['passed'] and value['synthetic'] is False and value['generatedDisposableFixtures'] is True and value['completeAoAPort'] is False,
                'Actual, explicitly scoped disposable native fixtures required')
    rows = xp['completeBoundaryCases']
    require(xp['actualAoALoginHandlerInvoked'] is True and xp['onlineForgeLoginVerified'] is False and xp['generatedPlayerAgeTicks'] == 1, 'An honestly scoped, correctly initialised post-login disposable player is required')
    skills = {row['skillClass'] for row in rows}
    require(len(skills) == xp['completeRegisteredSkillCount'] == 12 and len(rows) == 96, 'Incomplete canonical native skill boundary cohort')
    require(len({(r['skillClass'], r['before']) for r in rows}) == len(rows), 'Duplicated skill boundary')
    for skill in skills:
        subset = [row for row in rows if row['skillClass'] == skill]
        require({r['before'] for r in subset} == {1, 2, 4, 5, 99, 100, 999, 1000}, 'Missing exact skill threshold/cap')
        require(all(r['after'] == min(1000, r['before'] + 1) and r['remainingXp'] == 0 and r['completeSaveRoundtrip'] for r in subset), 'Native skill threshold/save differs')
    require(len(anima['progressionAndSyncCases']) == 20 and all(r['clientSync'] for r in anima['progressionAndSyncCases']), 'Anima boundary/sync cohort incomplete')
    for field in ['cancelledGrowthPreserved', 'forgeAllowHonored', 'ordinaryBonemealDoesNotTrain', 'actualCropGrowth',
                  'pickupInventoryAndGroundStonesConservedAsXp', 'nativePickupOwnershipAndDelayPreserved', 'completeDisposableStateRestored']:
        require(anima[field] is True, 'Anima native interaction absent: ' + field)
    counts = [0, 4, 4, 8, 4, 4, 8, 2, 1, 4, 1, 4, 32, 32, 4, 64, 16, 1, 2, 1, 1, 1]
    outcomes = extraction['completeOriginalOutcomes']
    require(len(outcomes) == 22 and {r['originalOutcome'] for r in outcomes} == set(range(22)), 'Missing/duplicate original extraction outcome')
    require(all(r['actualCount'] == counts[r['originalOutcome']] for r in outcomes), 'Original extraction quantity differs')
    require(len(set(extraction['dyes'])) == len(extraction['dyes']) == 16 and len(set(extraction['runes'])) == len(extraction['runes']) == 14, 'Incomplete original dye/rune identities')
    rows = extraction['interactions']
    require(len(rows) == 46 and {(r['expectedOutcome'], r['fullInventory']) for r in rows} == {(r, full) for r in range(-1, 22) for full in [False, True]}, 'Every outcome must exercise real empty/full inventory interaction')
    for row in rows:
        fail = row['expectedOutcome'] == -1
        require(row['failure'] == fail and row['day'] == (not row['fullInventory']), 'Constructed branch/context differs')
        require(row['awarded'] == (0 if fail else counts[row['expectedOutcome']]), 'Inventory/drop reward conservation differs')
        require((row['actualXp'] > 0) == (not fail) and row['pluton'] == (0 if fail else 2) and row['bowlDamage'] == (0 if fail else 1), 'Failure/success XP/tribute/durability boundary differs')
    arrows = extraction['nativeArrowWrappingAndSaveLoad']
    require(len(arrows) == 2 and len({r['weapon'] for r in arrows}) == 2 and all(r['nativeSaveLoad'] and 'AddonOwner' in r['pickupStack'] for r in arrows), 'Original arrow/addon data not retained through both native wrappers')
    require({r['registeredWeapon'] for r in arrows} == {'aoa3:alacrity_bow', 'aoa3:mecha_crossbow'}, 'The wrappers must exercise actual registered native weapons')
    pixons = extraction['pixonTributeInteractions']
    require(len(pixons) == 2 and {r['day'] for r in pixons} == {False, True} and all(r['originalNativeHarvestUnits'] == 5 and r['luxon'] == (25 if r['day'] else 0) for r in pixons), 'Native Pixon per-unit/day gate differs')
    require(all(r['survivalMode'] and r['belowLevelRejected'] and r['actualRequiredImbuingLevel'] > 1 and r['bowlDamage'] == 5 for r in pixons), 'Pixon level gate or survival bowl wear bypassed')
    require(extraction['currentUpstreamExtractionBlocks'] == 3, 'Current upstream extraction additions not exercised')
    return dict(completeNativeSkills=12, exactSkillThresholdCases=96, animaProgressionSyncCases=20, originalExtractionOutcomes=22,
                extractionInventoryInteractions=46, exactDyeIdentities=16, exactRuneIdentities=14, arrowWrapperSaveCases=2, pixonInteractions=2)


def verify_client(client_file, server_ref, server_jar):
    client_ref = artifact(client_file)
    client = json.loads(Path(client_file).read_text(encoding='utf-8'))
    require(client['passed'] and client['nativeClientAdmissionVerified'] and client['allPrimaryChoicesAndAuthoritiesUnchanged']
            and client['build']['state'] == 'client_verified', 'Complete admitted native client required')
    require(check(client['parent'])['sha256'] == server_ref['sha256'], 'Client did not use this exact native server parent')
    check(client['capture'])
    family_path = Path(client['capture']['path']).with_name('enderloom-forge1201-anima-extraction-client.json')
    family_ref = artifact(family_path)
    raw = family_path.read_text(encoding='utf-8')
    family = json.loads(raw)
    with Path(client['build']['stdout_path']).open(encoding='utf-8') as stream:
        require(any(line.rstrip('\r\n') == 'ENDERLOOM_FORGE1201_ANIMA_EXTRACTION_CLIENT ' + raw for line in stream),
                'Client family evidence is not the actual native log result')
    require(family['passed'] and family['synthetic'] is False and family['rasterParityVerified'] is False
            and family['completeAoAPort'] is False, 'Client scope or native result differs')
    require(family['renderer'] == 'net.tslat.aoa3.client.render.custom.AnimaSkillRenderer', 'Actual Anima renderer missing')
    expected = {
        'aoa3:textures/item/anima_stone.png': '2d2d7156da8e853239222c4cd27c46e7e5482f6ae8e1ce18d25a16bff72a7d32',
        'aoa3:textures/item/fragmented_anima_stone.png': 'acee2525ad033d5fb6d7c06d5faa058ca2fdc721340425d49ef2a1bfc2d8b9de',
        'aoa3:textures/gui/anima_circle.png': 'e86ee93a5ebb7b485213f1eaf84536d9beaeffced5c73d1e1dcb9a9d35cf266e'}
    textures = family['completeOriginalTextures']
    require(len(textures) == len(expected) and {r['resource']: r['sha256'] for r in textures} == expected,
            'Complete original client texture identities differ')
    require(all(r['decodedPixels'] == r['width'] * r['height'] > 0 for r in textures), 'Incomplete native PNG decode')
    require(next(r for r in textures if r['resource'].endswith('anima_circle.png'))['width'] == 255, 'Original Anima atlas was resized')
    models = family['actualBakedModels']
    require(len(models) == 5 and all(r['missing'] is False for r in models), 'Incomplete actual item/block model cohort')
    require({r['item'] for r in models if 'item' in r} == {'ANIMA_STONE', 'FRAGMENTED_ANIMA_STONE', 'HOLLY_ARROW'}, 'Missing canonical native item model')
    require({(r['filled'], r['actualParticleTexture']) for r in models if 'block' in r} ==
            {(False, 'aoa3:block/extraction_device'), (True, 'aoa3:block/extraction_device_filled')}, 'Actual lava state textures differ')
    jars = [r for r in client['build']['artifacts'] if Path(r['path']).name == 'aoa3-3.7.1.jar']
    require(len(jars) == 1, 'One unambiguous client mod required')
    client_jar = check(jars[0])
    differences = []
    with zipfile.ZipFile(server_jar['path']) as left, zipfile.ZipFile(client_jar['path']) as right:
        names = left.namelist()
        require(len(names) == len(set(names)) == len(right.namelist()) == len(set(right.namelist()))
                and set(names) == set(right.namelist()), 'Native mod archive members differ')
        for name in names:
            a, b = left.read(name), right.read(name)
            if a != b:
                require(name == 'META-INF/MANIFEST.MF', 'Client/server program or resource differs: ' + name)
                # Keep every manifest field, including attribution and Mixin
                # declarations. Only this exact build-time field may differ.
                normalize = lambda value: [line for line in value.decode('utf-8').splitlines()
                                           if not line.startswith('Implementation-Timestamp: ')]
                require(normalize(a) == normalize(b), 'A non-timestamp manifest field differs')
                differences.append(dict(member=name, onlyImplementationTimestamp=True))
        for resource, digest in expected.items():
            name = 'assets/aoa3/' + resource.split(':', 1)[1]
            require(hashlib.sha256(left.read(name)).hexdigest() == digest, 'Native proof and packaged original art differ')
    return dict(receipt=client_ref, familyCapture=family_ref, canonicalMod=client_jar, completeArchiveMembers=len(names),
                archiveDifferences=differences, completeOriginalTextures=3, actualBakedModels=5,
                nativeClientVerified=True, rasterParityVerified=False)


def run(server_file, plan_file, output, client_file=None):
    server_ref, plan_ref = artifact(server_file), artifact(plan_file)
    server = json.loads(Path(server_file).read_text(encoding='utf-8'))
    plan = json.loads(Path(plan_file).read_text(encoding='utf-8'))
    require(server['passed'] and server['compileVerified'] and server['nativeServerAdmissionVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'], 'Complete admitted native build/server required')
    require(server['build']['primary_target'] == plan['targetCell'] and server['build']['source_sha256'] == plan['originalSourceSha256'], 'Different complete mod/target')
    require(check(server['sourceRecipePlan']) == plan_ref, 'Native server did not admit this exact complete candidate')
    capture_ref = check(server['capture'])
    capture = json.loads(Path(capture_ref['path']).read_text(encoding='utf-8'))
    require(capture['serverTicks'] >= 40, 'Incomplete native lifecycle')
    summary = validate(capture)
    mods = [ref for ref in server['build']['artifacts'] if Path(ref['path']).name == 'aoa3-3.7.1.jar']
    require(len(mods) == 1, 'One unambiguous canonical mod required')
    jar = check(mods[0])
    with zipfile.ZipFile(jar['path']) as archive:
        require(len(archive.namelist()) == len(set(archive.namelist())) == mods[0]['entries'], 'Incomplete/duplicate actual mod archive')
        for name in ['player/skill/AnimaSkill.class', 'content/item/misc/FragmentedAnimaStone.class', 'content/block/functional/utility/ExtractionDevice.class', 'content/item/misc/HistoricalHollyArrow.class']:
            require('net/tslat/aoa3/' + name in archive.namelist(), 'Exercised native source missing from packaged mod')
        require(json.loads(archive.read('data/aoa3/player/skills/anima.json')), 'Anima disabled by empty skill data')
    faults = []
    for name, mutate in [
        ('missing_inventory_outcome', lambda x: x['extractionInspection']['interactions'].pop()),
        ('changed_reward_quantity', lambda x: x['extractionInspection']['completeOriginalOutcomes'][1].update(actualCount=3)),
        ('omitted_skill_boundary', lambda x: x['skillXpBoundaryInspection']['completeBoundaryCases'].pop()),
        ('lost_pickup_ownership', lambda x: x['animaInspection'].update(nativePickupOwnershipAndDelayPreserved=False)),
        ('false_whole_mod_completion', lambda x: x['animaInspection'].update(completeAoAPort=True))]:
        fixture = copy.deepcopy({key: capture[key] for key in ['skillXpBoundaryInspection', 'animaInspection', 'extractionInspection']})
        mutate(fixture)
        rejected = False
        try: validate(fixture)
        except (ValueError, KeyError): rejected = True
        require(rejected, 'Generated invalid proof accepted: ' + name)
        faults.append(dict(case=name, synthetic=True, rejected=True))
    client_result = verify_client(client_file, server_ref, jar) if client_file else None
    result = dict(schema=1, passed=True, synthetic=False, server=server_ref, plan=plan_ref, nativeCapture=capture_ref,
                  canonicalMod=jar, completeNativeSummary=summary, generatedFaults=faults, verifier=artifact(__file__),
                  completeAoAPort=False, naturalFullGameplayVerified=False, nativeClientVerified=client_result is not None,
                  client=client_result,
                  scope='Scoped actual native whole-mod and connected-family fixtures; optional client proof includes every packaged member. Every unaffected native regression remains required; the complete historical/latest union, natural full playthrough and production promotion remain separate.')
    with Path(output).open('x', encoding='utf-8') as file: json.dump(result, file, indent=2)
    print(json.dumps(dict(passed=True, **summary, output=output, completeAoAPort=False)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('server')
    parser.add_argument('plan')
    parser.add_argument('--output', required=True)
    parser.add_argument('--client', help='Optional accepted native client from this exact server parent')
    args = parser.parse_args()
    run(args.server, args.plan, args.output, args.client)
