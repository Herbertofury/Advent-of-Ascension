"""Independent float-bit/default/gate validation of the actual later native run."""
import argparse,copy,hashlib,json,math,struct
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb')as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)
def check(r):assert all(ref(r['path'])[k]==r[k]for k in ('bytes','sha256'))
def f32(x):return struct.unpack('>f',struct.pack('>f',x))[0]
def bits(x):return struct.pack('>f',x)
def threshold(level):
    # The later current native framework deliberately caches after different
    # float conversions and starts vanity thresholds at 100, not 101. Retain
    # that newer implementation; do not silently replace it with 1.12 math.
    if level<=99:return f32(f32(math.pow(1.1,level))*50)
    return 0 if level>=1000 else f32(f32(f32(math.pow(level-10,2.5))/100)+630000)
def award(level,amount):
    if level>=1000 or amount==0:return level,0
    remaining=f32(amount);advance=0;required=threshold(level)
    if remaining>=required:
        remaining=f32(remaining-required);advance=1
        while True:
            left=f32(remaining-threshold(level+advance))
            if left<0 or level+advance>=1000:break
            remaining=left;advance+=1
    return level+advance,remaining

def validate(later,defaults,missing):
    assert later['passed']and later['actualModernThresholdLevels']==1000
    rows=later['completeModernProgressionSaveSyncCases'];assert len(rows)==4000
    for index,current in enumerate(rows):
        level=index//4+1;expected_threshold=threshold(level)
        amount=[0,f32(expected_threshold/2),expected_threshold,f32(expected_threshold*2.75)][index%4]
        expected_level,expected_xp=award(level,amount)
        assert current['initialLevel']==level and bits(current['threshold'])==bits(expected_threshold)
        assert bits(current['award'])==bits(amount)and current['actualLevel']==expected_level and bits(current['actualXp'])==bits(expected_xp),(current,expected_level,expected_xp)
        assert current['retainedFrameworkEqual']and current['saveAndClientSyncVerified']
    complete={r['id']:r for r in defaults['completeDefaultEntries']};assert len(complete)==71
    unresolved=later['unresolvedActualDefaults'];assert len(unresolved)==14
    assert {r.split(' ')[0]for r in unresolved}==set(missing)
    active=set(complete)-set(missing);assert len(active)==57
    rewards={r['entity']:r for r in later['completeLaterRegisteredRewards']};assert len(rewards)==len(later['completeLaterRegisteredRewards'])==57 and set(rewards)==active
    assert len({r['actualClass']for r in rewards.values()})==57
    for key,current in rewards.items():
        expected=complete[key];reward=f32(float(expected['xpText']));level,xp=award(1,reward)
        assert current['requiredLevel']==expected['level']and bits(current['reward'])==bits(reward)
        assert current['actualLevel']==level and bits(current['actualXp'])==bits(xp)and current['registeredForgeSubscriberInvoked']
    gates=later['completeLaterAttackGates'];assert len(gates)==11400
    cases={(r['entity'],r['level'],r['creative'])for r in gates};assert len(cases)==11400
    assert cases=={(key,level,creative)for key in active for level in range(1,101)for creative in [False,True]}
    for current in gates:assert current['actualAllowed']==(current['creative']or current['level']>=complete[current['entity']]['level'])
    assert not later['completeHunterFamilyVerified']and not later['missingActorsVerified']and not later['laterArmorVerified']

def run(a):
    inherited,defaults,reconciliation=map(read,(a.inherited,a.defaults,a.reconciliation));assert inherited['passed']and bool(inherited['diagnosticRuntimeReuseVerified'])!=bool(inherited['normalNativeBuildAdmissionVerified'])
    for r in [inherited['plan'],inherited['server'],inherited['capture'],inherited['candidate']]+([inherited['diagnosticReplay']]if inherited.get('diagnosticReplay')else[]):check(r)
    assert defaults['passed']and defaults['actualReleasedClassExecuted']and defaults['defaultCount']==71;check(defaults['original'])
    capture=read(inherited['capture']['path']);later=capture['canonicalHunterSkillInspection']['laterAuthorPolicy'];missing=reconciliation['missingCurrentRegistryIdentities']
    server=read(inherited['server']['path']);root=Path(server['build']['build_root']);utility=next(root.glob('Advent-Of-Ascension-*/source/util/PlayerUtil.java'))
    if inherited['normalNativeBuildAdmissionVerified']:assert server['passed']and server['nativeServerAdmissionVerified']and server['compileVerified']and server['build']['state']=='server_verified'
    actual_source=utility.read_text(encoding='utf-8');assert 'XP_MAP.put(i, (float)Math.pow(1.1, i) * 50f);'in actual_source and 'for (int i = 1; i <= 99; i++)'in actual_source and 'for (int i = 100; i <= 999; i++)'in actual_source and 'XP_MAP.put(i, (float)Math.pow(i - 10, 2.5) / 100f + 630000);'in actual_source
    validate(later,defaults,missing);faults=[]
    for label,damage in [
        ('lost modern progression case',lambda d:d['completeModernProgressionSaveSyncCases'].pop()),
        ('old cap imposed on modern player',lambda d:d['completeModernProgressionSaveSyncCases'][403].__setitem__('actualLevel',100)),
        ('fractional XP changed',lambda d:d['completeModernProgressionSaveSyncCases'][1].__setitem__('actualXp',0)),
        ('source default reward changed',lambda d:d['completeLaterRegisteredRewards'][0].__setitem__('reward',0)),
        ('creative gate removed',lambda d:next(r for r in d['completeLaterAttackGates']if r['creative']).__setitem__('actualAllowed',False)),
        ('missing actor hidden',lambda d:d['unresolvedActualDefaults'].pop()),
        ('unverified family marked complete',lambda d:d.__setitem__('completeHunterFamilyVerified',True))]:
        changed=copy.deepcopy(later);damage(changed)
        try:validate(changed,defaults,missing)
        except(AssertionError,KeyError):faults.append(dict(fault=label,generated=True,rejected=True))
        else:raise AssertionError('Generated fault accepted: '+label)
    out=Path(a.output).absolute();assert not out.exists();producer=out.with_suffix('.producer.py');producer.write_bytes(Path(__file__).read_bytes())
    result=dict(passed=True,inheritedCompleteHistoricalNativeProof=ref(a.inherited),actualReleasedDefaults=ref(a.defaults),reconciliation=ref(a.reconciliation),capture=inherited['capture'],candidate=inherited['candidate'],currentNativeThresholdSource=ref(utility),currentNativeThresholdRoundingAndVanityBoundaryPreserved=True,producer=ref(producer),modernThresholdLevels=1000,modernProgressionSaveSyncCases=4000,laterNativeGateCases=11400,laterRegisteredRewardOwners=57,unresolvedLaterActors=missing,historicalFloatCasesRetained=3200,snapshotIntegerCasesRetained=2800,historicalGateCasesRetained=8400,previousSkillBoundaryCasesRetained=112,generatedFaults=faults,normalNativeBuildAdmissionVerified=inherited['normalNativeBuildAdmissionVerified'],diagnosticRuntimeReuseVerified=inherited['diagnosticRuntimeReuseVerified'],clientRenderingVerified=False,completeHunterFamilyVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:result[k]for k in ['passed','modernThresholdLevels','modernProgressionSaveSyncCases','laterNativeGateCases','laterRegisteredRewardOwners','completeAoAPort']}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('inherited','defaults','reconciliation','output'):p.add_argument(key)
    run(p.parse_args())
