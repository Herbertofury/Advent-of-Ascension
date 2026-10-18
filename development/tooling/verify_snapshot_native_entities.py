"""Independently verify the complete real native entity dependency cohort.

All recipes and imported new media are read in full. Generated bad-result
controls stay separate from original captures and never certify full gameplay.
"""
import argparse,concurrent.futures,copy,hashlib,json,zipfile
from pathlib import Path


def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(raw):return hashlib.sha256(raw).hexdigest()
def require(value,message):
    if not value:raise ValueError(message)
def artifact(path):
    p=Path(path);raw=p.read_bytes();return dict(path=str(p.resolve()),bytes=len(raw),sha256=sha(raw))
def verify(ref):
    actual=artifact(ref['path']);require(all(actual[k]==ref[k] for k in ['bytes','sha256']),'Full native authority changed: '+ref['path']);return actual


def cases(value):
    require(value['passed'] and value['implemented'] and not value['synthetic'],'Real complete native entity observations required')
    expected={('aoa3:fade','MAX_HEALTH'):50,('aoa3:fade','MOVEMENT_SPEED'):.8,('aoa3:fade','ATTACK_DAMAGE'):4,
        ('aoa3:fade','FOLLOW_RANGE'):52,('aoa3:fade','KNOCKBACK_RESISTANCE'):.3,('aoa3:evercron','MAX_HEALTH'):2500,
        ('aoa3:evercron','MOVEMENT_SPEED'):.6499999761581421,('aoa3:evercron','ATTACK_DAMAGE'):15,('aoa3:evercron','KNOCKBACK_RESISTANCE'):1}
    attributes=value['completeAttributeCases'];require(len(attributes)==len(expected),'Missing whole entity attribute domain')
    require({(r['entity'],r['attribute']) for r in attributes}==set(expected),'Different complete entity attribute identity')
    for r in attributes:require(abs(r['actual']-expected[(r['entity'],r['attribute'])])<1e-6,'Original native attribute changed')
    require(value['fadeWitherVerified'],'Official original effect missing')
    drops=value['fadeDropCases'];require(len(drops)==128 and {r['seed'] for r in drops}==set(range(128)),'Incomplete Fade drop seed domain')
    for r in drops:require(r['actual']==r['expected'] and all(k in {'aoa3:copper_coin','aoa3:snapshot_realmstone_fragment4','aoa3:snapshot_fragment_banner'} for k in r['actual']),'Actual native original drop differs')
    # Independent implementation of the original Java LCG and bounded nextInt.
    for row in drops:
        state=(row['seed']^0x5deece66d)&((1<<48)-1)
        def next_int(bound):
            nonlocal state
            while True:
                state=(state*0x5deece66d+11)&((1<<48)-1);bits=state>>(48-31)
                if bound&(bound-1)==0:return (bound*bits)>>31
                result=bits%bound
                if bits-result+(bound-1)<1<<31:return result
        expected_drops={}
        if next_int(2)==0:expected_drops['aoa3:copper_coin']=4
        if next_int(30)==25:expected_drops['aoa3:snapshot_realmstone_fragment4']=1
        if next_int(4)==3:expected_drops['aoa3:snapshot_fragment_banner']=1
        require(row['actual']==expected_drops,'Independent original LCG/drop outcome differs')
    rewards=value['hunterRewardCases'];require(len(rewards)==700 and {(r['level'],r['amount']) for r in rewards}=={(level,amount) for level in range(1,101) for amount in [0,1,49,50,999,10000,1000000]},'Missing complete Hunter reward boundary domain')
    for r in rewards:
        require(1<=r['expectedLevel']<=100 and r['expectedXp']>=0,'Invalid Hunter reward result')
        if 'actualLevel' in r:require((r['actualLevel'],r['actualXp'])==(r['expectedLevel'],r['expectedXp']),'Native persisted reward differs')
        if r['level']<30:require((r['expectedLevel'],r['expectedXp'])==(r['level'],0),'Original Hunter gate lost')
    projectile=value['projectileCases'];require(projectile and projectile[0]['kind']=='save-load-gravity-lifetime','Missing whole projectile save/gravity/lifetime domain')
    first=projectile[0];require(abs(first.get('actualRestoredDamage',first.get('damage',0))-18.5)<1e-6 and abs(first.get('actualGravity',first.get('gravity',0))-.075)<1e-6 and first['liveTicksBeforeExpiry']==40 and first['expiryCallbackTick']==41,'Original projectile semantics changed')
    require(all(value.get(key) is False for key in ['originalBehaviorEquivalenceVerified','fullEntityGameplayVerified','nativeVisualVerified','nativeDimensionsActivated','completeAoAPort']),'Callback observations cannot certify full gameplay or dimensions')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('server');p.add_argument('output');a=p.parse_args()
    out=Path(a.output);require(not out.exists(),'Retain complete previous independent proof')
    server=read(a.server);require(server['passed'] and server['compileVerified'] and server['nativeServerAdmissionVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Accepted complete actual native server required')
    verify(server['sourceRecipePlan']);verify(server['workspaceRequest']);verify(server['capture'])
    plan=read(server['sourceRecipePlan']['path']);request=read(server['workspaceRequest']['path']);capture=read(server['capture']['path'])
    require(request['sourceTransformations']==plan['sourceTransformations'],'Whole accepted recipe cohort changed');cases(capture['snapshotEntityFamilyInspection'])
    source=Path(server['build']['build_root'])
    def source_row(row):
        actual=artifact(source/row['path']);require(actual['sha256']==row['sha256'],'Actual whole source owner differs: '+row['path']);return actual
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:source_rows=list(pool.map(source_row,plan['sourceTransformations']))
    jars=list((source/'build/libs').glob('aoa3-*.jar'));require(len(jars)==1,'Ambiguous actual whole native JAR')
    jar=artifact(jars[0]);rows=plan['snapshotNativeEntityFamily'];donors={r['artifact']['sha256']:r['artifact'] for r in plan['sourceInputs']};donors.update({r['sha256']:r for r in plan['additionalAuthorities']})
    donor_files={};zip_files={}
    def member(ref):
        digest=ref['donorSha256'];require(digest in donors,'Unbound original complete program/media')
        if digest not in zip_files:
            donor_files[digest]=verify(donors[digest]);zip_files[digest]=zipfile.ZipFile(donors[digest]['path'])
        body=zip_files[digest].read(ref['donorEntry']);require(sha(body)==ref['sha256'],'Original complete member changed');return body
    try:
        for ref in rows['originalCompletePrograms']:member(ref)
        resources=[]
        with zipfile.ZipFile(jars[0]) as native:
            for media in rows['originalCompleteMedia']:
                raw=member(media['original']);body=native.read(media['target']);require(body==raw,'Whole original media changed in target JAR');resources.append(dict(path=media['target'],bytes=len(body),sha256=sha(body)))
            for texture in plan['snapshotEntityModelFoundation']['completeOriginalTextures']:
                raw=member(texture['original']);body=native.read(texture['resourcePath']);require(body==raw,'Original model texture differs');resources.append(dict(path=texture['resourcePath'],bytes=len(body),sha256=sha(body)))
    finally:
        for archive in zip_files.values():archive.close()
    log=Path(server['build']['stdout_path']).read_text(encoding='utf-8',errors='strict');marker='ENDERLOOM_FORGE1201_SNAPSHOT_ENTITY_FAMILY '
    lines=[line.split(marker,1)[1] for line in log.splitlines() if marker in line];require(len(lines)==1 and json.loads(lines[0])==capture['snapshotEntityFamilyInspection'],'Native executed log and complete captured domain differ')
    controls=[]
    def reject(name,change):
        fake=copy.deepcopy(capture['snapshotEntityFamilyInspection']);change(fake)
        try:cases(fake)
        except (ValueError,KeyError):controls.append(dict(name=name,generatedFault=True,rejected=True));return
        raise ValueError('Generated bad-result control accepted: '+name)
    reject('missing drop seed',lambda v:v['fadeDropCases'].pop())
    reject('different native attribute',lambda v:v['completeAttributeCases'][0].update(actual=-1))
    reject('wrong effect',lambda v:v.update(fadeWitherVerified=False))
    reject('omitted Hunter case',lambda v:v['hunterRewardCases'].pop())
    reject('premature full-gameplay claim',lambda v:v.update(fullEntityGameplayVerified=True))
    report=dict(schema=1,passed=True,synthetic=False,server=artifact(a.server),sourceRecipePlan=server['sourceRecipePlan'],nativeCapture=server['capture'],nativeJar=jar,
        completeSourceOwners=len(source_rows),completeSourceBytes=sum(r['bytes'] for r in source_rows),originalCompletePrograms=len(rows['originalCompletePrograms']),completeOriginalResources=resources,
        actualAttributeCases=9,actualDropCases=128,actualHunterBoundaryCases=700,actualProjectileCases=len(capture['snapshotEntityFamilyInspection']['projectileCases']),
        actualLogAndFullCaptureAgree=True,generatedControlsRejected=controls,nativeVisualVerified=False,fullGameplayVerified=False,nativeDimensionsActivated=False,completeAoAPort=False)
    out.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k not in ['completeOriginalResources','generatedControlsRejected']}))


if __name__=='__main__':main()
