"""Independently compare native complete temples to immutable original traces.

This verifies the complete controlled cohort, not natural acquisition or the
whole AoA living union. Destructive controls are generated result mutations.
"""
import argparse,copy,hashlib,json,zipfile
from pathlib import Path

def require(value,reason):
    if not value:raise AssertionError(reason)
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(body):return hashlib.sha256(body).hexdigest()
def artifact(path):
    p=Path(path);body=p.read_bytes();return dict(path=str(p),bytes=len(body),sha256=sha(body))

def check_capture(capture,reference):
    result=capture['snapshotTempleFamilyInspection'];require(result['passed'] and not result['synthetic'] and result['generatedControlledFixtures'],'Native controlled cohort required')
    native=result['completeTemples'];require(len(native)==5,'All five complete native temples required')
    require({r['program'] for r in native}==set(reference),'Original/native program membership changed')
    for row in native:
        require(row['completeOrderedOperations']==reference[row['program']],'Original ordered placement operations changed')
        require(row['actualNativeSpawners']==12 and row['actualChunkPieces']>=9 and row['worldRestored'],'Incomplete native world/chunk/spawner placement')
        require(row['pieceUnknownNbtRetained'] and row['invalidPieceSavesRejected']==3,'Save identity/unknown NBT guard missing')
    attrs=result['guardianAttributes'];require(len(attrs)==5 and all(abs(r['actual']-r['expected'])<1e-5 for r in attrs),'Complete guardian attributes required')
    drops=result['guardianDropCases'];require(len(drops)==2048 and [r['seed'] for r in drops]==list(range(2048)) and all(r['actual']==r['expected'] for r in drops),'Full original guardian RNG cases required')
    volleys=result['completeWeaponTransactions'];require(len(volleys)==4,'Full volley resource domain missing')
    expected={'aoa3:revolution_shot':1,'aoa3:atomizer_shot':1,'aoa3:mind_blaster_shot':1,'minecraft:area_effect_cloud':1,'aoa3:shower_shot':1,'aoa3:weighted_shower_shot':1,'aoa3:heavy_shower_shot':1,'aoa3:doom_shot':1,'aoa3:ghoul_ball':1,'aoa3:power_ray':1}
    for i,row in enumerate(volleys):
        require(row['scenario']==i and row['twoSameTickUseCalls'],'Missing real cooldown repeat call')
        require(row['nativeEmissions']==(expected if i in [0,3] else {}),'Missing or substituted complete current power emission')
        require(row['remainingSpirit']==(199 if i==1 else 0) and row['damage']==(1 if i==0 else 0),'Energy/durability loss or overconsumption')
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['plan','server','original_programs','output']:ap.add_argument(name)
    ap.add_argument('--client');a=ap.parse_args();plan=read(a.plan);server=read(a.server);require(server['passed'] and server['nativeServerAdmissionVerified'] and server['compileVerified'],'Actual whole native server admission required')
    capture=read(server['capture']['path']);full=read(a.original_programs);require(full['format']=='complete-original-literal-shared-family-1','Original shared program required')
    bindings={'LabBrick':'lab_brick','LeveledBrick':'leveled_brick','LabLampDonut':'lab_lamp_donut','SpawnerMegaGuardian':'snapshot_spawner_mega_guardian','SpawnerFade':'snapshot_spawner_fade','SpawnerTorano':'snapshot_spawner_torano','SpawnerCenturion':'snapshot_spawner_centurion','SpawnerSceptron':'snapshot_spawner_sceptron','SpawnerPoseido':'snapshot_spawner_poseido'}
    reference={}
    for name,program in full['programs'].items():
        rows=[]
        for x,y,z,role,metadata,mode in full['bases'][program['base']]:
            require(metadata==0 and full['updateCallModes'][mode]=='original-default-call','Unmapped original wrapper behavior')
            block='aoa3:'+bindings[program['bindings'][role].split('.')[-1]];rows.append(f'{x},{y},{z},{block},0,3')
        reference[name]=rows
    result=check_capture(capture,reference);faults=[]
    for fault in ['lost-operation','wrong-block','wrong-update-flags','missing-temple','wrong-drop','missing-power','double-resource-consumption','lost-save-check']:
        broken=copy.deepcopy(capture);cohort=broken['snapshotTempleFamilyInspection']
        if fault=='lost-operation':cohort['completeTemples'][0]['completeOrderedOperations'].pop()
        elif fault=='wrong-block':cohort['completeTemples'][0]['completeOrderedOperations'][0]='0,0,0,minecraft:air,0,3'
        elif fault=='wrong-update-flags':cohort['completeTemples'][0]['completeOrderedOperations'][0]=cohort['completeTemples'][0]['completeOrderedOperations'][0][:-1]+'2'
        elif fault=='missing-temple':cohort['completeTemples'].pop()
        elif fault=='wrong-drop':cohort['guardianDropCases'][0]['actual']=1-cohort['guardianDropCases'][0]['actual']
        elif fault=='missing-power':cohort['completeWeaponTransactions'][0]['nativeEmissions'].popitem()
        elif fault=='double-resource-consumption':cohort['completeWeaponTransactions'][1]['remainingSpirit']=0
        elif fault=='lost-save-check':cohort['completeTemples'][0]['pieceUnknownNbtRetained']=False
        rejected=False
        try:check_capture(broken,reference)
        except AssertionError:rejected=True
        require(rejected,'Generated broken result accepted: '+fault);faults.append(dict(fault=fault,rejected=True,generated=True))
    family=plan['snapshotCompleteTempleFamily'];resources=family['exactOriginalMedia'];require(len(resources)==5,'Complete exact guardian/reward media required')
    for row in resources:
        original=row['original'];refs=plan['sourceInputs'];donor=next(r['artifact'] for r in refs if r['artifact']['sha256']==original['donorSha256'])
        require(artifact(donor['path'])==donor,'Complete original donor changed')
        with zipfile.ZipFile(donor['path']) as z:body=z.read(original['donorEntry'])
        require(sha(body)==row['sha256']==original['sha256'] and len(body)==row['bytes'],'Original full media drift')
    client=None
    if a.client:
        client=read(a.client);require(client['passed'] and client['nativeClientAdmissionVerified'],'Whole muted native client required')
        cc=read(client['capture']['path']);draws=cc['snapshotEntityEffects']['completeNativeDraws']
        require(any(r['identity']=='aoa3:mega_guardian' and r['actualNativeVertices']==864 and r['nativeBufferAndGpuDrawCompleted'] for r in draws),'Whole guardian GPU draw missing')
    out=Path(a.output);require(not out.exists(),'Keep previous verification immutable')
    out.write_text(json.dumps(dict(passed=True,synthetic=False,plan=artifact(a.plan),server=artifact(a.server),originalSharedPrograms=artifact(a.original_programs),completePrograms=5,completeOriginalOperations=sum(map(len,reference.values())),nativeSpawners=60,guardianAttributeCases=5,guardianDropCases=2048,wholeVolleyTransactions=4,exactOriginalMedia=resources,generatedFaults=faults,client=artifact(a.client) if a.client else None,automaticNaturalAcquisitionVerified=False,completeAoAPort=False),indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,temples=5,completeOriginalOperations=23410,nativeSpawners=60,guardianDrops=2048,generatedFaults=len(faults),output=str(out))))

if __name__=='__main__':main()
