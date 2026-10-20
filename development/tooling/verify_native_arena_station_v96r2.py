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

def arena(record,plan_ref,template_hash,expected_blocks,expected_step=None,expected_tree=False):
    require(record['passed'] and record['synthetic'] is False and record['controlledNativePlacements'],'Actual whole native arena placement required')
    require(record['sourcePlan']['sha256']==plan_ref['sha256'] and record['templateSha256']==template_hash,'Arena must use the exact conserved source plan/template')
    cases=record['completePlacementCases'];rotations=['NONE','CLOCKWISE_90','CLOCKWISE_180','COUNTERCLOCKWISE_90'];mirrors=['NONE','LEFT_RIGHT','FRONT_BACK']
    require(len(cases)==12 and {(r['rotation'],r['mirror']) for r in cases}==set(itertools.product(rotations,mirrors)),'Every rotation and mirror required')
    require(record['completeNativeBlocksCompared']==expected_blocks*12,'All twelve complete template placements required')
    for row in cases:require(row['completeNativeBlocksCompared']==expected_blocks and row['originalAltar']==1 and row['originalGuardianSpawners']==2 and row['addedStations']==1 and row['priorWorldStatesAndTilesRestored'],'Original arena content, unique station and restored fixture states required')
    natural=record['naturalArena'];require(natural['dimension']=='aoa3:runandor' and natural['structure']=='aoa3:clunkhead_arena' and 1<=natural['candidateStarts']<=64 and natural['actualFullChunks']>=1,'Actual retained canonical natural arena required')
    require(natural['nativeStations']==1 and natural['originalAltars']==1 and natural['originalGuardianSpawners']==2 and natural['openPlayerNeighbours']>=3 and natural['manualPlacementUsed'] is False,'Naturally generated unique accessible station, altar and both guardian cages required')
    if expected_step:require(natural['nativeGenerationStep']==expected_step.upper(),'Canonical native generation order differs')
    if expected_blocks>2150:require(natural['completeNativeBlocksCompared']==expected_blocks and natural['explicitRoomAirVerified']==expected_blocks-2150,'All natural original blocks/station/explicit room-air positions required')
    if expected_tree:
        tree=natural['nativeTreeProtection'];require(tree['passed'] and tree['synthetic'] is False and tree['controlledNativeFixture'] and tree['nativeFeature']=='aoa3:runic_tree','Actual native canonical tree fixture required')
        require(tree['completeProtectedPositions']==expected_blocks and tree['actualBlockedFeatureWrites']==expected_blocks*2 and tree['adjacentChunkProtectedPositions']>0,'Every complete arena position and both overwrite choices must be protected across native chunk boundaries')
        require(tree['outsideArenaWriteCases']==1 and tree['manualGrowthCases']==1 and tree['nestedContextRestored'] and tree['contextReleased'] and tree['completePriorStatesAndBlockEntityTagsRestored'],'Outside/manual growth, nested context cleanup and full state restoration required')
        variants=tree['completeOriginalTreeVariants'];require(len(variants)==5 and {v['variant'] for v in variants}==set(range(5)) and all(v['completeOriginalGeneratorExercised'] and v['completeProtectedPositions']==expected_blocks and v['wholePriorSnapshotRestored'] for v in variants),'All five actual original tree generators, including soil writes, and complete restoration required')
        require(tree['originalNaturalTreeDistributionParityClaimed'] is False,'Controlled write fixtures cannot claim complete tree distribution parity')
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
    expected_blocks=plan['snapshotNaturalStationAcquisition']['newBlocks'];template_hash=plan['snapshotNaturalStationAcquisition']['resourceReplacement']['after']['sha256'];p,value=native_file(server,'enderloom-forge1201-arena-station.json','ENDERLOOM_FORGE1201_ARENA_STATION');expected_step=plan.get('snapshotCanonicalArenaGenerationOrder',{}).get('newStep');expected_tree=bool(plan.get('snapshotCanonicalArenaTreeProtection'));arena(value,plan_ref,template_hash,expected_blocks,expected_step,expected_tree)
    require(read(server['capture']['path'])['arenaStationInspection']==value,'Whole server capture differs from complete arena observation')
    faults=[]
    for fault in ['lost-transform','duplicate-transform','partial-arena','changed-source','lost-altar','lost-guardian','duplicate-station','buried-station','manual-generation','invented-progression']+(['wrong-generation-step'] if expected_step else [])+(['partial-tree-protection','lost-outside-growth','lost-manual-growth','leaked-tree-context','lost-tree-tag-restoration','lost-tree-variant'] if expected_tree else []):
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
        elif fault=='wrong-generation-step':bad['naturalArena']['nativeGenerationStep']='SURFACE_STRUCTURES'
        elif fault=='partial-tree-protection':bad['naturalArena']['nativeTreeProtection']['completeProtectedPositions']-=1
        elif fault=='lost-outside-growth':bad['naturalArena']['nativeTreeProtection']['outsideArenaWriteCases']=0
        elif fault=='lost-manual-growth':bad['naturalArena']['nativeTreeProtection']['manualGrowthCases']=0
        elif fault=='leaked-tree-context':bad['naturalArena']['nativeTreeProtection']['contextReleased']=False
        elif fault=='lost-tree-tag-restoration':bad['naturalArena']['nativeTreeProtection']['completePriorStatesAndBlockEntityTagsRestored']=False
        elif fault=='lost-tree-variant':bad['naturalArena']['nativeTreeProtection']['completeOriginalTreeVariants'].pop()
        elif fault=='invented-progression':bad['activePlayerProgressionVerified']=True
        rejected=False
        try:arena(bad,plan_ref,template_hash,expected_blocks,expected_step,expected_tree)
        except AssertionError:rejected=True
        require(rejected,'Generated bad native observation accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
    client=None
    if a.client:
        proof=read(a.client);verify_ref(proof['capture']);verify_ref(proof['parent']);require(proof['passed'] and proof['compileVerified'] and proof['nativeClientAdmissionVerified'] and proof['parent']['sha256']==artifact(a.server)['sha256'],'Exact current native client parent/admission required')
        f,observed=native_file(proof,'enderloom-forge1201-four-snapshot-world-client.json','ENDERLOOM_FORGE1201_FOUR_SNAPSHOT_WORLD_CLIENT');client_visuals(observed)
        require(read(proof['capture']['path'])['fourSnapshotWorldClientInspection']==observed,'Complete client result differs from actual visual capture')
        cp,ca=native_file(proof,'enderloom-forge1201-arena-station.json','ENDERLOOM_FORGE1201_ARENA_STATION');arena(ca,plan_ref,template_hash,expected_blocks,expected_step,expected_tree)
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
    result=dict(passed=True,synthetic=False,plan=plan_ref,server=artifact(a.server),nativeArena=artifact(p),verifier=artifact(frozen),completeNativeArenaPositions=expected_blocks*12,naturalAccessibleStation=True,client=client,generatedFaults=faults,activePlayerProgressionVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(passed=True,completeNativeArenaPositions=expected_blocks*12,naturalAccessibleStation=True,clientVerified=bool(client),generatedFaults=len(faults),output=str(out))))

if __name__=='__main__':main()
