"""Share identical ordered geometry with explicit per-program field bindings.

Every original operation, overwrite, position, metadata and update-call mode
must expand identically. This is an exact data representation, not native
registry/world/gameplay acceptance.
"""
import argparse,copy,hashlib,json
from pathlib import Path

def require(v,why):
    if not v:raise ValueError(why)
def artifact(p):
    p=Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def expand(data,name):
    program=data['programs'][name];roles=program['bindings'];modes=data['updateCallModes']
    return [[x,y,z,roles[role],metadata,modes[mode]] for x,y,z,role,metadata,mode in data['bases'][program['base']]]
def verify_all(data,original):
    require(set(data['programs'])==set(original),'Whole-program membership differs')
    for name,rows in original.items():require(expand(data,name)==rows,'Complete original operation sequence differs: '+name)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('oracle');p.add_argument('output');a=p.parse_args();out=Path(a.output);require(not out.exists(),'Keep previous full shared representation')
    oracle=json.loads(Path(a.oracle).read_text(encoding='utf-8'));require(oracle['passed'] and oracle['originalBytecodeExecuted'] and oracle['generatedWorldFixtures'] and not oracle['originalMinecraftRuntime'],'Complete labelled original bytecode oracle required')
    ref=oracle['completeRelativePrograms'];require(artifact(ref['path'])==ref,'Complete original operation authority changed');original=json.loads(Path(ref['path']).read_text(encoding='utf-8'))
    groups={}
    for name,rows in sorted(original.items()):
        geometry=json.dumps([[row[i] for i in [0,1,2,4,5]] for row in rows],separators=(',',':'));groups.setdefault(geometry,[]).append(name)
    data=dict(format='complete-original-literal-shared-family-1',bases=[],programs={},updateCallModes=[])
    for names in groups.values():
        roles={};operations=[]
        for ordinal,row in enumerate(original[names[0]]):
            vector=tuple(original[name][ordinal][3] for name in names)
            if vector not in roles:roles[vector]=len(roles)
            mode=row[5]
            if mode not in data['updateCallModes']:data['updateCallModes'].append(mode)
            operations.append([row[0],row[1],row[2],roles[vector],row[4],data['updateCallModes'].index(mode)])
        base=len(data['bases']);data['bases'].append(operations)
        for column,name in enumerate(names):data['programs'][name]=dict(base=base,bindings=[vector[column] for vector in roles])
    verify_all(data,original);controls=[]
    for label,change in [('missing ordered placement',lambda d:d['bases'][0].pop()),('wrong source binding',lambda d:d['programs'][next(iter(d['programs']))]['bindings'].__setitem__(0,'unverified:substitute')),('wrong metadata',lambda d:d['bases'][0][0].__setitem__(4,1)),('wrong update call',lambda d:d['updateCallModes'].__setitem__(0,'unsupported-call'))]:
        bad=copy.deepcopy(data);change(bad);rejected=False
        try:verify_all(bad,original)
        except (ValueError,IndexError,KeyError):rejected=True
        require(rejected,'Generated bad shared representation accepted: '+label);controls.append(dict(generatedFault=label,rejected=True))
    compact=out.with_suffix('.shared-programs.json');raw=json.dumps(data,separators=(',',':')).encode('utf-8');require(not compact.exists(),'Retain prior shared data');compact.write_bytes(raw)
    producer=out.with_suffix('.producer.py');require(not producer.exists(),'Retain prior producer');producer.write_bytes(Path(__file__).read_bytes())
    report=dict(passed=True,oracle=artifact(a.oracle),completeOriginalPrograms=ref,sharedRepresentation=artifact(compact),wholePrograms=len(original),sharedWholeGeometryBases=len(data['bases']),originalOrderedOperations=sum(len(v) for v in original.values()),storedOrderedOperations=sum(len(v) for v in data['bases']),allOriginalOperationsExpandIdentically=True,originalUncompressedRepresentationBytes=ref['bytes'],sharedUncompressedRepresentationBytes=len(raw),generatedFaults=controls,producer=artifact(producer),originalMinecraftRuntime=False,nativeRegistryIdentityVerified=False,nativePlacementVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k!='generatedFaults'}))

if __name__=='__main__':main()
