"""Independently read complete native fragment-family and muted client evidence.

Generated fault controls never become native/original acceptance. No detached
fixture is evidence for survival progression, AI or complete world equivalence.
"""
import argparse,copy,hashlib,json,zipfile
from pathlib import Path

def require(v,message):
    if not v:raise ValueError(message)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def artifact(p):
    p=Path(p).resolve();raw=p.read_bytes();return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def verify(ref):
    now=artifact(ref['path']);require(all(now[k]==ref[k] for k in ['sha256','bytes']),'Changed complete artifact: '+ref['path'])
def cases(server,client):
    require(server['passed'] and server['implemented'] and not server['synthetic'] and server['generatedDetachedFixtures'],'Missing actual native fragment fixtures')
    require(server['fullAoAPort'] is False and server['originalAiParityVerified'] is False and server['survivalProgressionVerified'] is False,'Premature full game acceptance')
    expected={k:dict(zip(['ATTACK_DAMAGE','FOLLOW_RANGE','KNOCKBACK_RESISTANCE','MOVEMENT_SPEED','MAX_HEALTH'],values)) for k,values in
        [('torano',[5,52,.7,.8,60]),('centurion',[15,52,.8,.8,300]),('sceptron',[6,52,.1,.8,65]),('poseido',[5,52,.7,.8,60])]}
    attrs=server['completeAttributeCases'];require(len(attrs)==20 and {(r['identity'],r['attribute']) for r in attrs}=={(k,a) for k,v in expected.items() for a in v},'Incomplete native attribute domain')
    for r in attrs:require(abs(r['actual']-expected[r['identity']][r['attribute']])<1e-6,'Original native stat drift')
    drops=server['completeDropCases'];require(len(drops)==1024 and {(r['identity'],r['seed']) for r in drops}=={(k,s) for k in expected for s in range(256)},'Incomplete whole-family drop domain')
    for row in drops:
        state=(row['seed']^0x5deece66d)&((1<<48)-1)
        def draw(bound):
            nonlocal state
            while True:
                state=(state*0x5deece66d+11)&((1<<48)-1);bits=state>>17
                if bound&(bound-1)==0:return (bound*bits)>>31
                n=bits%bound
                if bits-n+bound-1<1<<31:return n
        outcomes={};fragment={'torano':2,'centurion':5,'sceptron':3,'poseido':1}[row['identity']]
        if draw(2)==0:outcomes['aoa3:copper_coin']=4
        sequence=[('aoa3:snapshot_realmstone_fragment'+str(fragment),30,25),('aoa3:snapshot_fragment_banner',4,3)]
        if row['identity']=='torano':sequence.reverse()
        for key,bound,hit in sequence:
            if draw(bound)==hit:outcomes[key]=1
        require(row['actual']==outcomes==row['expected'],'Independent original Java LCG/count drift')
    transactions=server['completeStationTransactions'];require(len(transactions)==9 and {r['scenario'] for r in transactions}==set(range(9)),'Missing native complete inventory cases')
    for r in transactions:
        s=r['scenario'];missing=s if 1<=s<=5 else 0;trade=s in [0,8]
        require(r['missingFragment']==missing and r['sneaking']==(s==6) and r['offhand']==(s==7) and r['fullInventory']==(s==8),'Changed actual station input domain')
        require(r['remainingFragments']==[0 if f==missing else 1 if trade else 2 for f in range(1,6)],'Lost or duplicated original fragments')
        require(r['ownedRealmstones']==(1 if s==0 else 0) and r['droppedRealmstones']==(1 if s==8 else 0),'Lost/duplicated full inventory station reward')
    require(client['passed'] and client['implemented'] and not client['synthetic'],'Missing actual native client effects')
    draws=client['completeNativeDraws'];vertices={'aoa3:fade':312,'aoa3:evercron':408,'aoa3:snapshot_fragment_banner':120,'aoa3:torano':456,'aoa3:centurion':216,'aoa3:sceptron':168,'aoa3:poseido':264}
    require(len(draws)==7 and {r['identity'] for r in draws}==set(vertices),'Incomplete whole native model draw domain')
    for r in draws:require(r['actualNativeVertices']==r['expectedWholeBodyVertices']==vertices[r['identity']] and r['nativeBufferAndGpuDrawCompleted'] and r['visualEquivalenceVerified'] is False,'Missing native whole model geometry/GPU draw')
    screens=client['completeMobScreenImages'];require(len(screens)==22 and {r['image'] for r in screens}==set(range(1,23)),'Missing original whole MobScreen images')
    for r in screens:require(r['actualTicks']==300 and r['actualImage']==r['image'] and r['originalPngPresent'],'Dropped screen duration/image/PNG')
    require(client['actualParticles']==56 and client['clientParticleQueueRestored'],'Inherited full particle family regressed')
    require(all(client[k] is False for k in ['visualParityVerified','hariVerified','fullGameplayVerified','completeAoAPort']),'Native buffers cannot certify visual/gameplay equivalence')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ['server','source_proof','client','output']:p.add_argument(k)
    a=p.parse_args();out=Path(a.output);require(not out.exists(),'Preserve previous complete evidence')
    server,source,client=read(a.server),read(a.source_proof),read(a.client)
    require(server['passed'] and server['nativeServerAdmissionVerified'] and server['compileVerified'] and client['passed'] and client['nativeClientAdmissionVerified'],'Actual whole native server/client required')
    require(source['passed'] and source['server']['sha256']==artifact(a.server)['sha256'],'Independent complete-source proof is for another server')
    for ref in [server['sourceRecipePlan'],source['nativeJar'],server['capture'],client['capture']]:verify(ref)
    plan=read(server['sourceRecipePlan']['path']);capture=read(server['capture']['path']);client_capture=read(client['capture']['path']);family=plan['snapshotFragmentProgressionFamily']
    native=capture['snapshotFragmentFamilyInspection'];effects=client_capture['snapshotEntityEffects'];cases(native,effects)
    audio=client['quietAudioVerification'];require(audio['passed'],'Native client audio mute not verified')
    roots={'server':Path(server['build']['build_root']),'client':Path(client['build']['build_root'])}
    for label,receipt,actual,marker in [('server',server,native,'ENDERLOOM_FORGE1201_SNAPSHOT_FRAGMENT_FAMILY '),('client',client,effects,'ENDERLOOM_FORGE1201_SNAPSHOT_CLIENT_EFFECTS ')]:
        lines=[json.loads(line.split(marker,1)[1]) for line in Path(receipt['build']['stdout_path']).read_text(encoding='utf-8').splitlines() if marker in line]
        require(lines==[actual],'Actual full native log/capture mismatch: '+label)
    donors={r['artifact']['sha256']:r['artifact'] for r in plan['sourceInputs']};donors.update({r['sha256']:r for r in plan['additionalAuthorities']});archives={}
    def member(ref):
        digest=ref['donorSha256']
        if digest not in archives:verify(donors[digest]);archives[digest]=zipfile.ZipFile(donors[digest]['path'])
        body=archives[digest].read(ref['donorEntry']);require(hashlib.sha256(body).hexdigest()==ref['sha256'],'Original whole program/media changed');return body
    complete=[]
    try:
        for ref in family['completeOriginalPrograms']:member(ref)
        with zipfile.ZipFile(source['nativeJar']['path']) as jar:
            for row in family['exactOriginalMedia']:
                raw=member(row['original']);require(jar.read(row['resourcePath'])==raw,'Full author media differs in native JAR');complete.append(dict(path=row['resourcePath'],bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
            for row in family['completeModels']:
                member(row['originalCompleteSource']);member(row['originalCompleteClass']);path=row['target'];r=next(r for r in plan['sourceTransformations'] if r['path']==path)
                require((roots['server']/path).read_bytes()==r['content'].encode('utf-8'),'Actual full native model source differs')
                b=jar.read(path.removeprefix('src/main/java/').removesuffix('.java')+'.class');require(b[:4]==b'\xca\xfe\xba\xbe' and int.from_bytes(b[6:8],'big')==61,'Whole original model not compiled for native target')
    finally:
        for z in archives.values():z.close()
    controls=[]
    for label,side,mutation in [('missing drop seed',0,lambda v:v['completeDropCases'].pop()),('wrong RNG/count',0,lambda v:v['completeDropCases'][0].update(actual={})),('lost full inventory reward',0,lambda v:v['completeStationTransactions'][8].update(droppedRealmstones=0)),('wrong attribute',0,lambda v:v['completeAttributeCases'][0].update(actual=-1)),('missing whole model',1,lambda v:v['completeNativeDraws'].pop()),('missing screen',1,lambda v:v['completeMobScreenImages'].pop()),('premature complete AoA',0,lambda v:v.update(fullAoAPort=True))]:
        pair=[copy.deepcopy(native),copy.deepcopy(effects)];mutation(pair[side]);rejected=False
        try:cases(*pair)
        except (ValueError,KeyError):rejected=True
        require(rejected,'Generated bad-result accepted: '+label);controls.append(dict(generatedFault=label,rejected=True))
    frozen=out.with_suffix('.verifier.py');frozen.write_bytes(Path(__file__).read_bytes())
    report=dict(passed=True,server=artifact(a.server),sourceProof=artifact(a.source_proof),client=artifact(a.client),verifier=artifact(frozen),actualAttributes=20,actualDropCases=1024,actualStationTransactions=9,actualScreenImages=22,actualNativeWholeDraws=7,completeAuthorMedia=complete,clientAudioGuard=audio,generatedControls=controls,
        nativeDimensionsActivated=False,survivalProgressionVerified=False,fullGameplayVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k not in ['completeAuthorMedia','clientAudioGuard','generatedControls']}))

if __name__=='__main__':main()
