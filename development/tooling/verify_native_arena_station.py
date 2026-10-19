"""Independently bind whole arena placement, natural access and client portals.

Generated bad records test the verifier, never player worlds. Native placement
and rendering do not certify a player's survival acquisition or the full merge.
"""
import argparse,copy,hashlib,itertools,json
from pathlib import Path

def require(good,why):
    if not good:raise AssertionError(why)

def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def artifact(path):
    p=Path(path)
    with p.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=digest)

def verify_ref(ref):
    actual=artifact(ref['path']);require(all(actual[k]==ref[k] for k in ['bytes','sha256']),'Changed exact native evidence: '+ref['path'])

def arena(record,plan_ref,template_hash):
    require(record['passed'] and record['synthetic'] is False and record['controlledNativePlacements'],'Actual whole native arena placement required')
    require(record['sourcePlan']['sha256']==plan_ref['sha256'] and record['templateSha256']==template_hash,'Arena must use the exact conserved source plan/template')
    cases=record['completePlacementCases'];rotations=['NONE','CLOCKWISE_90','CLOCKWISE_180','COUNTERCLOCKWISE_90'];mirrors=['NONE','LEFT_RIGHT','FRONT_BACK']
    require(len(cases)==12 and {(r['rotation'],r['mirror']) for r in cases}==set(itertools.product(rotations,mirrors)),'Every rotation and mirror required')
    require(record['completeNativeBlocksCompared']==25800,'All twelve complete 2,150-block placements required')
    for row in cases:require(row['completeNativeBlocksCompared']==2150 and row['originalAltar']==1 and row['originalGuardianSpawners']==2 and row['addedStations']==1 and row['priorWorldStatesAndTilesRestored'],'Original arena content, unique station and restored fixture states required')
    natural=record['naturalArena'];require(natural['dimension']=='aoa3:runandor' and natural['structure']=='aoa3:clunkhead_arena' and 1<=natural['candidateStarts']<=64 and natural['actualFullChunks']>=1,'Actual retained canonical natural arena required')
    require(natural['nativeStations']==1 and natural['originalAltars']==1 and natural['originalGuardianSpawners']==2 and natural['openPlayerNeighbours']>=3 and natural['manualPlacementUsed'] is False,'Naturally generated unique accessible station, altar and both guardian cages required')
    require(record['naturalStationPlacementVerified'] and record['activePlayerProgressionVerified'] is False and natural['activePlayerProgressionVerified'] is False and record['completeAoAPort'] is False,'Unexercised survival/full-merge acceptance must remain open')

def client_visuals(record):
    require(record['passed'] and record['synthetic'] is False and record['completeNativeFogCases']==12 and record['actualPortalGpuDraws']==8,'Actual complete four-world client cohort required')
    worlds=record['worlds'];require(len(worlds)==4 and {r['realm'] for r in worlds}=={'aoa3:'+r for r in ['ethereus','everland','playtopia','labricon']},'Every restored native effects owner required')
    for row in worlds:
        require(row['nativeEffectsDispatch'] and row['sourceBoundFixedFogFormulaCases']==3 and row['nativeEnvironmentalFogCoordinateCases']==4 and row['originalCloudHeight']==128,'All source-bound native fog/vector/coordinate/cloud cases required')
        require(row['originalEnvironmentalFog']==(row['realm']!='aoa3:labricon'),'Original MCP environmental fog boolean changed')
        models=row['portalModels'];require(len(models)==2 and {m['axis'] for m in models}=={'X','Z'},'Both native portal axes required')
        for model in models:require(model['actualNativeQuads']>0 and model['sharedNativeAnimatedMaterial'] and model['nativeTranslucentLayer'] and model['actualGpuDrawCompleted'],'Actual complete animated translucent portal rendering required')
    require(record['completeAoAPort'] is False and record['originalPortalArtClaimed'] is False,'Authored shared access material must not be represented as original portal art/full parity')

def native_file(proof,name,marker):
    p=Path(proof['build']['build_root'])/'run'/name;value=read(p);raw=p.read_text(encoding='utf-8');log=Path(proof['build']['stdout_path']).read_text(encoding='utf-8')
    require(log.count(marker+' ')==1 and marker+' '+raw in log,'Exact single native capture/log marker required: '+name)
    return p,value

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['plan','server','output']:ap.add_argument(k)
    ap.add_argument('--client');a=ap.parse_args();plan,server=read(a.plan),read(a.server);plan_ref=artifact(a.plan)
    require(server['passed'] and server['compileVerified'] and server['nativeServerAdmissionVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Full normal server build/admission required')
    require(server['sourceRecipePlan']['sha256']==plan_ref['sha256'],'Exact complete native source cohort required');verify_ref(server['capture'])
    template_hash=plan['snapshotNaturalStationAcquisition']['resourceReplacement']['after']['sha256'];p,value=native_file(server,'enderloom-forge1201-arena-station.json','ENDERLOOM_FORGE1201_ARENA_STATION');arena(value,plan_ref,template_hash)
    require(read(server['capture']['path'])['arenaStationInspection']==value,'Whole server capture differs from complete arena observation')
    faults=[]
    for fault in ['lost-transform','duplicate-transform','partial-arena','changed-source','lost-altar','lost-guardian','duplicate-station','buried-station','manual-generation','invented-progression']:
        bad=copy.deepcopy(value)
        if fault=='lost-transform':bad['completePlacementCases'].pop()
        elif fault=='duplicate-transform':bad['completePlacementCases'][-1]=copy.deepcopy(bad['completePlacementCases'][0])
        elif fault=='partial-arena':bad['completePlacementCases'][0]['completeNativeBlocksCompared']-=1
        elif fault=='changed-source':bad['templateSha256']='0'*64
        elif fault=='lost-altar':bad['completePlacementCases'][0]['originalAltar']=0
        elif fault=='lost-guardian':bad['naturalArena']['originalGuardianSpawners']=1
        elif fault=='duplicate-station':bad['naturalArena']['nativeStations']=2
        elif fault=='buried-station':bad['naturalArena']['openPlayerNeighbours']=2
        elif fault=='manual-generation':bad['naturalArena']['manualPlacementUsed']=True
        elif fault=='invented-progression':bad['activePlayerProgressionVerified']=True
        rejected=False
        try:arena(bad,plan_ref,template_hash)
        except AssertionError:rejected=True
        require(rejected,'Generated bad native observation accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
    client=None
    if a.client:
        proof=read(a.client);verify_ref(proof['capture']);verify_ref(proof['parent']);require(proof['passed'] and proof['compileVerified'] and proof['nativeClientAdmissionVerified'] and proof['parent']['sha256']==artifact(a.server)['sha256'],'Exact current native client parent/admission required')
        f,observed=native_file(proof,'enderloom-forge1201-four-snapshot-world-client.json','ENDERLOOM_FORGE1201_FOUR_SNAPSHOT_WORLD_CLIENT');client_visuals(observed)
        require(read(proof['capture']['path'])['fourSnapshotWorldClientInspection']==observed,'Complete client result differs from actual visual capture')
        cp,ca=native_file(proof,'enderloom-forge1201-arena-station.json','ENDERLOOM_FORGE1201_ARENA_STATION');arena(ca,plan_ref,template_hash)
        audio_file,audio=native_file(proof,'enderloom-client-audio-guard.json','ENDERLOOM_CLIENT_AUDIO_VERIFIED');require(audio['passed'] and audio['prelaunchMuted'] and audio['actualNativeMasterVolume']==0 and audio['disposableSettingsOnly'] and audio['soundCallbacksDisabled'] is False,'Actual muted native client required')
        for fault in ['lost-world','lost-axis','opaque-layer','undrawn-portal','wrong-fog-policy','partial-fog-domain']:
            bad=copy.deepcopy(observed)
            if fault=='lost-world':bad['worlds'].pop()
            elif fault=='lost-axis':bad['worlds'][0]['portalModels'].pop()
            elif fault=='opaque-layer':bad['worlds'][0]['portalModels'][0]['nativeTranslucentLayer']=False
            elif fault=='undrawn-portal':bad['worlds'][0]['portalModels'][0]['actualGpuDrawCompleted']=False
            elif fault=='wrong-fog-policy':bad['worlds'][0]['originalEnvironmentalFog']=False
            elif fault=='partial-fog-domain':bad['worlds'][0]['nativeEnvironmentalFogCoordinateCases']=0
            rejected=False
            try:client_visuals(bad)
            except AssertionError:rejected=True
            require(rejected,'Generated bad client observation accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
        client=dict(proof=artifact(a.client),visuals=artifact(f),arena=artifact(cp),audio=artifact(audio_file),actualPortalGpuDraws=8,nativeFogVectorCases=12,nativeEnvironmentalFogCoordinateCases=16)
    out=Path(a.output);frozen=Path(str(out)+'.verifier.py');require(not out.exists() and not frozen.exists(),'Retain prior exact independent verification');frozen.write_bytes(Path(__file__).read_bytes())
    result=dict(passed=True,synthetic=False,plan=plan_ref,server=artifact(a.server),nativeArena=artifact(p),verifier=artifact(frozen),completeNativeArenaPositions=25800,naturalAccessibleStation=True,client=client,generatedFaults=faults,activePlayerProgressionVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(passed=True,completeNativeArenaPositions=25800,naturalAccessibleStation=True,clientVerified=bool(client),generatedFaults=len(faults),output=str(out))))

if __name__=='__main__':main()
