"""Independent source-bound acceptance of native whole-temple overlap policy."""
import argparse,copy,hashlib,json
from pathlib import Path


def require(good,why):
    if not good:raise AssertionError(why)


def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def ref(p):
    p=Path(p)
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)


def jhash(value):
    h=0
    for ch in value:h=(h*31+ord(ch))&0xffffffff
    return h if h<2**31 else h-2**32


def dimension_hash(name):
    n=(31*jhash('aoa3')+jhash(name))&0xffffffff
    return n if n<2**31 else n-2**32


def check(d):
    require(d['passed'] and d['synthetic'] is False and d['numericPolicyCensusOnly'],'Actual native bounded policy census required')
    root=-1884161595195503959;require(d['savedWorldSeed']==root and d['nativeDimensionSeedProjectionVerified'] and d['failurePlacementSeed']==root+dimension_hash('lborean'),'Actual existing AoA dimension-seed projection required')
    policies=d['completePlacementPolicies'];realms=['abyss','barathos','greckon','haven','lborean'];require(len(policies)==5 and [r['realm'] for r in policies]==['aoa3:'+r for r in realms],'All five source-owned policies required')
    for index,row in enumerate(policies):
        require(row['placementSeed']==root+dimension_hash(realms[index]) and row['salt']==17102500+index and row['barathosChain']==(index==1),'Original dimension/salt/branch identity changed')
        n=row['admittedCompleteTemples'];require(0<n<=row['rawOriginalCandidates'] and row['completeCandidateChunks']==160000 and row['maximumOverlappingChunkDistance']==3 and row['allAdmittedPairsChecked']==n*(n-1)//2,'Complete nonempty bounded raw/admitted/pair census required')
    require(d['completeCandidateChunks']==800000 and d['rawOriginalCandidates']==sum(r['rawOriginalCandidates'] for r in policies) and d['admittedCompleteTemples']==sum(r['admittedCompleteTemples'] for r in policies),'Complete policy totals required')
    require(d['rawOriginalRarityUnchanged'] and d['finalAdmittedDensityEqualsRawRarity'] is False and d['exactFailurePairNoLongerBothAdmitted'],'Keep raw rarity and disclose distinct final density')
    require(d['retainedActualFailurePair']==[[1482,-999],[1483,-998]] and d['existingWorldsEdited'] is False and d['completeAoAPort'] is False,'Exact failure coordinates and bounded gameplay scope required')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['plan','server','output']:ap.add_argument(k)
    a=ap.parse_args();plan,server=read(a.plan),read(a.server);require(server['passed'] and server['nativeServerAdmissionVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Admitted unchanged whole native server required')
    actual=ref(a.plan);bound=server['sourceRecipePlan'];require(Path(bound['path']).samefile(a.plan) and (bound['sha256'],bound['bytes'])==(actual['sha256'],actual['bytes']),'Exact full source plan required')
    policy=plan['snapshotTempleOverlapProtection'];require(policy['completeTempleProgramsUnchanged']==5 and policy['radiusChunks']==3 and policy['completeProgramWidth']==39 and policy['defaultForOldCodecAndConstructor'] is False,'Complete versioned spacing source policy required')
    run=Path(server['build']['build_root'])/'run';native=run/'enderloom-forge1201-temple-spacing.json';capture=read(server['capture']['path']);d=read(native);require(d==capture['templeSpacingInspection'],'Actual whole server and separate native records must agree');check(d)
    bindings=read(run/'enderloom-temple-spacing-bindings.json');require(bindings['firstRaw'] and bindings['secondRaw'] and not(bindings['firstSafe'] and bindings['secondSafe']),'Exact failed raw pair must reproduce and be protected')
    require(bindings['failurePlacementSeed']==d['failurePlacementSeed'] and bindings['livePlacementSeed']==bindings['liveWorldSeed']+dimension_hash('lborean') and bindings['liveSalt']==17102504,'Actual runtime dimension seed/salt binding changed')
    log=Path(server['build']['stdout_path']).read_text(encoding='utf-8');raw=native.read_text(encoding='utf-8');require(log.count('ENDERLOOM_FORGE1201_TEMPLE_SPACING ')==1 and 'ENDERLOOM_FORGE1201_TEMPLE_SPACING '+raw in log,'Actual exact single runtime marker required')
    faults=[]
    for fault in ['missing-policy','wrong-projected-seed','wrong-salt','too-many-admitted','missing-pair-check','invented-density-parity','lost-failure-pair','edited-world']:
        bad=copy.deepcopy(d)
        if fault=='missing-policy':bad['completePlacementPolicies'].pop()
        elif fault=='wrong-projected-seed':bad['completePlacementPolicies'][0]['placementSeed']=bad['savedWorldSeed']
        elif fault=='wrong-salt':bad['completePlacementPolicies'][0]['salt']=0
        elif fault=='too-many-admitted':bad['completePlacementPolicies'][0]['admittedCompleteTemples']+=1000
        elif fault=='missing-pair-check':bad['completePlacementPolicies'][0]['allAdmittedPairsChecked']-=1
        elif fault=='invented-density-parity':bad['finalAdmittedDensityEqualsRawRarity']=True
        elif fault=='lost-failure-pair':bad['exactFailurePairNoLongerBothAdmitted']=False
        elif fault=='edited-world':bad['existingWorldsEdited']=True
        rejected=False
        try:check(bad)
        except AssertionError:rejected=True
        require(rejected,'Generated corrupt spacing result accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
    out=Path(a.output);frozen=Path(str(out)+'.verifier.py');require(not out.exists() and not frozen.exists(),'Keep previous verification immutable');frozen.write_bytes(Path(__file__).read_bytes())
    out.write_text(json.dumps(dict(passed=True,synthetic=False,plan=actual,server=ref(a.server),nativeCapture=ref(native),bindings=ref(run/'enderloom-temple-spacing-bindings.json'),verifier=ref(frozen),candidateChunks=800000,rawCandidates=d['rawOriginalCandidates'],admittedCompleteTemples=d['admittedCompleteTemples'],generatedFaults=faults,finalAdmittedDensityEqualsRawRarity=False,completeAoAPort=False),indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(passed=True,candidateChunks=800000,rawCandidates=d['rawOriginalCandidates'],admittedCompleteTemples=d['admittedCompleteTemples'],generatedFaults=len(faults),output=str(out))))


if __name__=='__main__':main()
