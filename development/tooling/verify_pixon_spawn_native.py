"""Bind complete current spawn policies, actual native captures and the whole JAR.

This never promotes a menu, a controlled timer fixture or a source checklist to
complete historical/latest gameplay, save migration, full compatibility or FPS.
"""
import argparse, collections, copy, hashlib, json, re, zipfile
from pathlib import Path

def require(value,message):
    if not value: raise ValueError(message)

def artifact(path):
    p=Path(path).absolute()
    with p.open('rb') as stream: h=hashlib.file_digest(stream,'sha256').hexdigest()
    return dict(path=str(p),sha256=h,bytes=p.stat().st_size)

def check(ref):
    a=artifact(ref['path']);require((a['sha256'],a['bytes'])==(ref['sha256'],ref['bytes']),'Changed complete authority: '+ref['path']);return a

def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))

def normalized(value):
    if isinstance(value,list): return [normalized(v) for v in value]
    if not isinstance(value,dict): return value
    if value.get('type') in ['minecraft:uniform','minecraft:biased_to_bottom'] and set(value)=={'type','min_inclusive','max_inclusive'}:
        require(type(value['min_inclusive']) is int and type(value['max_inclusive']) is int,'Exact integer providers required')
        return dict(type=value['type'],value=dict(max_inclusive=value['max_inclusive'],min_inclusive=value['min_inclusive']))
    return {k:normalized(v) for k,v in value.items()}

def validate(capture,cases):
    require(capture['passed'] and not capture['synthetic'] and not capture['completeAoAPort'],'Actual bounded native Pixon capture required')
    rows=capture['completeCurrentPolicies'];require(len(rows)==len(cases)==6,'Complete six-policy domain required')
    lookup={r['name']:r for r in rows};require(len(lookup)==6,'Duplicate native Pixon policy')
    variants=set();tickets=0
    for case in cases:
        name=Path(case['resourcePath']).stem;row=lookup[name];expected=case['completeSettings']
        require(json.loads(row['completeOriginalSettings'])==normalized(expected),'Native complete policy changed')
        weights=expected['variants'];expected_tickets=[]
        for value in weights:expected_tickets.extend([value['data']]*value['weight']);variants.add(value['data'])
        require(row['completeWeightedTickets']==expected_tickets,'Missing/altered current native weighted ticket')
        require(row['completeVariantWeights']==[dict(variant=v['data'],weight=v['weight'],nativeEntity=v['data']+'_pixon') for v in weights],'Changed native saved variant identity or weight')
        tickets+=len(expected_tickets)
        dimensions=row['actualDimensions'];require(len(dimensions)==capture['completeActualDimensions'] and len({v['dimension'] for v in dimensions})==len(dimensions),'Incomplete actual native dimension domain')
        settings=expected['base_settings']
        for dimension in dimensions:
            key=dimension['dimension'];allowed=(not dimension['flat'] or settings['spawn_in_flat_world']) and (not settings.get('in_dimensions') or key in settings['in_dimensions']) and key not in settings.get('not_in_dimensions',[])
            require(dimension['passed'] and dimension['included']==allowed,'Native dimension/flat restriction changed')
        require(row['passed'] and row['passiveGatePassed'],'Native passive gate failed')
    require(sorted(variants)==capture['completeNativeVariants'] and len(variants)==8,'Complete eight-variant union changed')
    attachments=capture['completeDimensionAttachments'];require(len(attachments)==capture['completeActualDimensions'],'Incomplete dimension attachment cohort')
    for row in attachments:
        require(row['passed'] and row['afterFirstAttach']==row['afterSecondAttach'],'Duplicate or failed native spawner attachment')
        expected=sum(v['included'] for policy in rows for v in policy['actualDimensions'] if v['dimension']==row['dimension'])
        require(row['actualPixonPolicies']==expected,'Missing actual dimension-owned policy')
    live=capture['liveNativeTerrain'];require(live['passed'] and live['controlledFixture'] and live['controlledTimerReset'] and live['fakeSurvivalPlayer'],'Honest controlled live-terrain fixture required')
    require(live['terrainOrBiomeEdits']==0 and live['originalPolicySettingsUnchanged'] and live['allAdmittedFixtureEntitiesRemoved'] and live['originalPlayerAndEntityMembershipPreserved'],'Live terrain/player/entity state was changed or not restored')
    require(len(live['trials'])==32 and {r['trial'] for r in live['trials']}==set(range(32)),'Complete live trial cohort missing')
    require(live['spawnCount']==len(live['spawned'])==sum(r['actualSpawnCount'] for r in live['trials']) and live['spawnCount']>0,'Live native spawning count lost')
    for row in live['spawned']:
        require(row['nativeTerrainValid'] and 39<=row['radius']<=130 and row['health']>0,'Native terrain/annulus/factory failed')
        require(row['id'] in {v['data']+'_pixon' for v in cases[0]['completeSettings']['variants']},'Live Overworld Pixon violated the original current variant policy')
    require(not capture['naturalAcquisitionVerified'] and not live['automaticWildSchedulingVerified'] and not capture['modernMagnitudeSiphoningAndVisualsVerified'],'Controlled fixtures cannot certify automatic/full newer progression')
    require(len(capture['generatedFaultControls'])==6 and all(v['generated'] and v['rejected'] for v in capture['generatedFaultControls']),'Actual native invalid-codec controls missing')
    return dict(completePolicies=6,completeVariants=8,completeWeightedTickets=tickets,completeDimensions=capture['completeActualDimensions'],controlledLiveTrials=32,actualNativeSpawned=live['spawnCount'])

def run(server_file,plan_file,previous_file,output,client_file=None):
    server,plan,previous=map(read,[server_file,plan_file,previous_file])
    require(server['passed'] and server['nativeServerAdmissionVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Accepted complete native server required')
    require(previous['passed'] and previous['nativeServerAdmissionVerified'],'Accepted preceding complete JAR required')
    require(server['build']['primary_target']==plan['targetCell']==previous['build']['primary_target'],'Native target mismatch')
    require(check(server['sourceRecipePlan'])==artifact(plan_file),'Current accepted source plan differs')
    jar=server['build']['artifacts'][0];old=previous['build']['artifacts'][0];check(jar);check(old)
    family=plan['pixonNaturalSpawnFamily'];cases=family['wholeCurrentPolicies'];check(family['latest'])
    with zipfile.ZipFile(family['latest']['path']) as authority,zipfile.ZipFile(jar['path']) as current,zipfile.ZipFile(old['path']) as prior:
        require(len(current.namelist())==len(set(current.namelist())) and current.testzip() is None,'Ambiguous or corrupt complete current JAR')
        before,after=set(prior.namelist()),set(current.namelist());require(before<=after,'Preceding complete archive members removed')
        added=sorted(after-before)
        resources=sorted(c['resourcePath'] for c in cases)
        helpers=['PixonBiomeSelection','PixonSpawnSettings','PixonSpawnVariant$1','PixonSpawnVariant','PixonVariantSpawner']
        require(added==sorted(resources+['net/tslat/aoa3/content/world/spawner/'+v+'.class' for v in helpers]),'Unreviewed whole artifact additions')
        changed=sorted(name for name in before if prior.read(name)!=current.read(name))
        expected=['META-INF/MANIFEST.MF','net/tslat/aoa3/common/registration/AoADatapackLoaders.class','net/tslat/aoa3/data/server/AoACustomSpawnersListener.class','net/tslat/aoa3/event/GlobalEvents.class']
        require(changed==expected,'An unrelated complete program/resource member changed')
        strip=lambda raw:re.sub(rb'(?m)^Implementation-Timestamp: [^\r\n]*',b'Implementation-Timestamp: <retained-build-time>',raw)
        require(strip(prior.read('META-INF/MANIFEST.MF'))==strip(current.read('META-INF/MANIFEST.MF')),'Manifest changed beyond the build timestamp')
        for case in cases:
            ref=case['completeOriginal'];original=authority.read(ref['donorEntry']);require(hashlib.sha256(original).hexdigest()==ref['sha256']==case['sha256'] and json.loads(original)==case['completeSettings'],'Complete current official policy authority changed')
            target=current.read(case['resourcePath']);require(hashlib.sha256(target).hexdigest()==case['nativeSha256'] and json.loads(target)==normalized(json.loads(original)),'Native numeric schema projection changed original semantics')
        client_result=None
        if client_file:
            client=read(client_file);require(client['passed'] and client['nativeClientAdmissionVerified'] and check(client['parent'])==artifact(server_file),'Exact native client from this complete server required')
            client_jar=client['build']['artifacts'][0];check(client_jar)
            with zipfile.ZipFile(client_jar['path']) as packaged:
                require(set(packaged.namelist())==after and len(packaged.namelist())==len(after),'Client/server complete archive membership differs')
                differences=sorted(name for name in after if current.read(name)!=packaged.read(name))
                require(differences in [[],['META-INF/MANIFEST.MF']],'Client/server complete program/resource bytes differ')
                require(strip(current.read('META-INF/MANIFEST.MF'))==strip(packaged.read('META-INF/MANIFEST.MF')),'Client manifest differs beyond timestamp')
            client_result=dict(receipt=artifact(client_file),artifact=client_jar,differentMembers=differences,completeProgramAndResourceBytesEqual=True)
    capture_path=Path(server['build']['build_root'])/'run/enderloom-forge1201-pixon-spawning.json';capture=read(capture_path);summary=validate(capture,cases)
    raw=capture_path.read_text(encoding='utf-8');log=Path(server['build']['stdout_path']).read_text(encoding='utf-8');require(log.count('ENDERLOOM_FORGE1201_PIXON_SPAWNING ')==1 and 'ENDERLOOM_FORGE1201_PIXON_SPAWNING '+raw in log,'Native capture not bound to the exact server log')
    faults=[]
    for name in ['missing policy','missing ticket','wrong saved identity','lost attachment','lost live spawn','lost restoration']:
        fixture=copy.deepcopy(capture)
        if name=='missing policy':fixture['completeCurrentPolicies'].pop()
        elif name=='missing ticket':fixture['completeCurrentPolicies'][0]['completeWeightedTickets'].pop()
        elif name=='wrong saved identity':fixture['completeCurrentPolicies'][0]['completeVariantWeights'][0]['nativeEntity']='minecraft:pig'
        elif name=='lost attachment':fixture['completeDimensionAttachments'][0]['afterSecondAttach']+=1
        elif name=='lost live spawn':fixture['liveNativeTerrain']['spawnCount']+=1
        elif name=='lost restoration':fixture['liveNativeTerrain']['originalPlayerAndEntityMembershipPreserved']=False
        rejected=False
        try:validate(fixture,cases)
        except (ValueError,KeyError):rejected=True
        require(rejected,'Generated corrupted full native proof was accepted: '+name);faults.append(dict(case=name,generated=True,rejected=True))
    frozen=Path(output).with_suffix('.producer.py');frozen.write_bytes(Path(__file__).read_bytes())
    result=dict(schema=1,passed=True,synthetic=False,server=artifact(server_file),sourcePlan=artifact(plan_file),previousServer=artifact(previous_file),canonicalMod=jar,nativeCapture=artifact(capture_path),completePreviousMembersRetained=len(before),currentMembers=len(after),addedMembers=added,changedMembers=changed,completeNativeSummary=summary,client=client_result,generatedFaultControls=faults,verifier=artifact(frozen),completeAoAPort=False,naturalFullGameplayVerified=False,performanceVerified=False,scope='Bounded current Pixon spawning and complete artifact/native regression acceptance. Automatic scheduling, full current magnitude/siphoning/visual reconciliation, historical/latest union, full natural playthrough, save migration, multiplayer, full-pack compatibility and FPS remain separate.')
    with Path(output).open('x',encoding='utf-8') as file:json.dump(result,file,indent=2)
    print(json.dumps(dict(passed=True,**summary,clientVerified=client_result is not None,output=output)))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('server');p.add_argument('plan');p.add_argument('previous');p.add_argument('--client');p.add_argument('--output',required=True);a=p.parse_args();run(a.server,a.plan,a.previous,a.output,a.client)
