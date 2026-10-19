"""Verify the complete native natural-temple cohort and source-bound policies.

Requires whole native build/server admission; controlled rarity-result fault
cases are generated records, not faults injected into player worlds.
"""
import argparse,copy,hashlib,json
from pathlib import Path


def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def require(value,reason):
    if not value:raise AssertionError(reason)
def artifact(path):
    p=Path(path)
    with p.open('rb') as stream:digest=hashlib.file_digest(stream,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=digest)


def check(result,policies):
    require(result['adapter']=='complete-native-natural-temple-family-1' and result['passed'] and not result['synthetic'] and result['freshDisposableWorldChunks'],'Actual complete native natural generation required')
    rows=result['naturalTemples'];require(len(rows)==5 and len({r['dimension'] for r in rows})==5,'Complete five-realm cohort required')
    require({r['dimension'] for r in rows}==set(policies),'Wrong natural dimension identity')
    for row in rows:
        realm=row['dimension'].split(':')[1];require(row['structure']=='aoa3:snapshot_fragment_temple_'+realm,'Canonical structure identity changed')
        program='net.nevermine.structures.'+('lborean.FragmentTempleBorean' if realm=='lborean' else realm+'.FragmentTemple'+realm.capitalize())
        require(row['program']==program,'Original full temple program changed')
        require(row['actualNativeGeneratorSetActive'] and row['nativeRarityPlacementUsed'] and row['manualPlacementUsed'] is False,'Actual natural generator/placement not exercised')
        require(row['completeFinalBlocksVerified']==4682 and row['actualNativeSpawnerTiles']==12,'Full native temple block/cage domain incomplete')
        require(row['candidateChunksConsidered']>=row['actualNativeCandidateStarts']>=1 and 9<=row['actualFullChunkPipelineCalls']<=16,'Actual candidate/full-chunk pipeline absent')
        x,y,z,xx,yy,zz=row['completeBounds'];cx,cz=row['startChunk'];require((xx-x,yy-y,zz-z)==(38,19,38) and 0<=x-cx*16<16 and 0<=z-cz*16<16,'Complete native bounds/random offsets changed')
        if realm=='lborean':require(row['sourceBoundSubmergedCeiling']==policies[row['dimension']]['submergedCeiling'] and yy<row['sourceBoundSubmergedCeiling'],'Source-bound submerged limit lost')
        else:require(row['sourceBoundSubmergedCeiling'] is None,'Unrequested submerged policy added')
        require(row['playerProgressionVerified'] is False,'Structure cohort cannot certify player progression')
    branches=result['completeOriginalRarityBranches'];require(len(branches)==10,'Complete short-circuit boundary cohort absent')
    rolls=[[0],[649],[650],[749],[141],[140,127],[140,126,650],[140,126,649],[140,126,0],[399,649,749]]
    for i,row in enumerate(branches):
        expected_bounds=([750] if i<4 else [400] if i==4 else [400,650] if i==5 else [400,650,750])
        require(row['case']==i and row['barathos']==(i>=4) and row['bounds']==expected_bounds and row['rolls']==rolls[i] and row['actual']==(i in [2,6]) and row['calls']==len(rolls[i]),'Original rare branch or RNG consumption changed')
    require(all(result[k] is False for k in ['originalWholeDecorationRngParityVerified','fullSurvivalProgressionVerified','existingUserChunksModified','completeAoAPort']),'Unsupported broader gameplay claim')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['plan','server','output']:ap.add_argument(name)
    ap.add_argument('--client')
    a=ap.parse_args();server,plan=read(a.server),read(a.plan);require(server['passed'] and server['nativeServerAdmissionVerified'] and server['compileVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Whole native build/server admission required')
    actual=artifact(a.plan);recorded=server['sourceRecipePlan'];require(Path(recorded['path']).samefile(a.plan) and (recorded['bytes'],recorded['sha256'])==(actual['bytes'],actual['sha256']),'Wrong complete source-plan identity')
    policies={r['dimension']:r for r in plan['completeNaturalTempleFamily']['canonicalDimensions']};capture=read(server['capture']['path']);result=capture['naturalTempleInspection'];check(result,policies)
    run=Path(server['build']['build_root'])/'run';native=run/'enderloom-forge1201-natural-temples.json';require(read(native)==result,'Server and full natural capture differ')
    log=Path(server['build']['stdout_path']).read_text(encoding='utf-8');require(log.count('ENDERLOOM_FORGE1201_NATURAL_TEMPLES ')==1 and 'ENDERLOOM_FORGE1201_NATURAL_TEMPLES '+native.read_text(encoding='utf-8') in log,'Full native capture/log mismatch')
    whole=read(run/'enderloom-forge1201-whole-world-generation.json');require(whole['passed'] and whole['complete'] and not whole['synthetic'] and not whole['errors'],'Complete inherited live world generation required')
    jobs={(r['expectedStructureOwner'],r['chunk']['x'],r['chunk']['z']) for r in whole['targetedStructureChunks']}
    for row in result['naturalTemples']:
        if row['dimension'] in ['aoa3:haven','aoa3:greckon']:require((row['structure'],*row['startChunk']) in jobs,'Legacy native chunk census omitted a real rare temple start')
    client_proof=None
    if a.client:
        client=read(a.client);require(client['passed'] and client['nativeClientAdmissionVerified'] and client['allPrimaryChoicesAndAuthoritiesUnchanged'] and client['parent']['sha256']==artifact(a.server)['sha256'],'Exact full native client admission required')
        cc=read(client['capture']['path']);check(cc['integratedServer']['naturalTempleInspection'],policies)
        client_run=Path(client['build']['build_root'])/'run';client_natural=client_run/'enderloom-forge1201-natural-temples.json';require(read(client_natural)==cc['integratedServer']['naturalTempleInspection'],'Full integrated native generation record differs')
        audio=client_run/'enderloom-client-audio-guard.json';require(read(audio)==dict(schema=1,passed=True,prelaunchMuted=True,actualNativeMasterVolume=0.0,disposableSettingsOnly=True,soundCallbacksDisabled=False),'Actual muted client/audio callbacks required')
        client_proof=dict(passed=True,receipt=artifact(a.client),capture=client['capture'],naturalCapture=artifact(client_natural),audioGuard=artifact(audio))
    faults=[]
    for fault in ['missing-realm','wrong-program','manual-substitution','lost-block','lost-cage','wrong-bounds','roof-crossing','lost-short-circuit','wrong-rarity','invented-survival']:
        bad=copy.deepcopy(result);row=bad['naturalTemples'][0]
        if fault=='missing-realm':bad['naturalTemples'].pop()
        elif fault=='wrong-program':row['program']='net.nevermine.structures.haven.FragmentTempleHaven'
        elif fault=='manual-substitution':row['manualPlacementUsed']=True
        elif fault=='lost-block':row['completeFinalBlocksVerified']-=1
        elif fault=='lost-cage':row['actualNativeSpawnerTiles']-=1
        elif fault=='wrong-bounds':row['completeBounds'][3]+=1
        elif fault=='roof-crossing':r=next(r for r in bad['naturalTemples'] if r['dimension']=='aoa3:lborean');r['sourceBoundSubmergedCeiling']=r['completeBounds'][4]
        elif fault=='lost-short-circuit':bad['completeOriginalRarityBranches'][4]['calls']=2
        elif fault=='wrong-rarity':bad['completeOriginalRarityBranches'][2]['actual']=False
        elif fault=='invented-survival':bad['fullSurvivalProgressionVerified']=True
        rejected=False
        try:check(bad,policies)
        except AssertionError:rejected=True
        require(rejected,'Generated broken natural result accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
    out=Path(a.output);frozen=Path(str(out)+'.verifier.py');require(not out.exists() and not frozen.exists(),'Retain previous immutable proof');frozen.write_bytes(Path(__file__).read_bytes())
    out.write_text(json.dumps(dict(passed=True,synthetic=False,plan=actual,server=artifact(a.server),nativeCapture=artifact(native),wholeGeneration=artifact(run/'enderloom-forge1201-whole-world-generation.json'),verifier=artifact(frozen),completeNaturalTemples=5,completeNativeBlocks=23410,nativeSpawnerTiles=60,originalRarityCases=10,generatedFaults=faults,client=client_proof,fullSurvivalProgressionVerified=False,completeAoAPort=False),indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,naturalTemples=5,nativeBlocks=23410,spawners=60,clientVerified=client_proof is not None,generatedFaults=len(faults),output=str(out))))


if __name__=='__main__':main()
