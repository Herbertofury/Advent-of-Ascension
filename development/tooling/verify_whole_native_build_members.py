"""Compare every member of independently built native mod products.

Only the parsed main manifest's explicit Implementation-Timestamp value may
differ. No class, asset, other header, section, entry or duplicate is ignored.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path

def require(v,why):
    if not v:raise ValueError(why)
def artifact(p):
    p=Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def manifest(raw):
    lines=raw.decode('utf-8').replace('\r\n','\n').split('\n');sections=[];headers=[]
    for line in lines:
        if not line:
            if headers:sections.append(headers);headers=[]
        elif line.startswith(' '):
            require(headers,'Orphan folded manifest line');headers[-1][1]+=line[1:]
        else:
            key,separator,value=line.partition(': ');require(separator and key,'Invalid complete manifest header')
            require(key.lower() not in {k.lower() for k,_ in headers},'Duplicate manifest header');headers.append([key,value])
    if headers:sections.append(headers)
    require(sections,'Empty complete manifest');return sections
def equal_manifest(left,right):
    a,b=manifest(left),manifest(right);require(len(a)==len(b),'Different complete manifest section membership')
    times=[]
    for sections in [a,b]:
        positions=[i for i,(k,_) in enumerate(sections[0]) if k=='Implementation-Timestamp'];require(len(positions)==1,'Exactly one main implementation timestamp required')
        at=positions[0];times.append(sections[0][at][1]);sections[0][at][1]='<explicit-build-time>'
    require(a==b,'A manifest field/section outside explicit build time changed');return times
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['server_jar','client_jar','output']:p.add_argument(name)
    a=p.parse_args();out=Path(a.output);require(not out.exists(),'Retain previous complete artifact comparison');refs=[artifact(a.server_jar),artifact(a.client_jar)]
    members=[];times=None
    with zipfile.ZipFile(a.server_jar) as x,zipfile.ZipFile(a.client_jar) as y:
        require(len(x.namelist())==len(set(x.namelist())) and len(y.namelist())==len(set(y.namelist())),'Duplicate native archive owner')
        require(set(x.namelist())==set(y.namelist()),'Independent products have different complete archive membership')
        for name in sorted(x.namelist()):
            left,right=x.read(name),y.read(name)
            if name=='META-INF/MANIFEST.MF':times=equal_manifest(left,right)
            else:require(left==right,'Native byte difference outside build timestamp: '+name)
            members.append(dict(path=name,serverBytes=len(left),clientBytes=len(right),serverSha256=hashlib.sha256(left).hexdigest(),clientSha256=hashlib.sha256(right).hexdigest()))
    require(times is not None,'Missing native main manifest');frozen=out.with_suffix('.verifier.py');frozen.write_bytes(Path(__file__).read_bytes())
    report=dict(passed=True,serverJar=refs[0],clientJar=refs[1],completeMembers=len(members),allMemberBytesCompared=True,onlyPermittedDifference='Parsed main Implementation-Timestamp value',actualBuildTimestamps=times,completeMemberObservations=members,verifier=artifact(frozen),fullGameplayVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k!='completeMemberObservations'}))

if __name__=='__main__':main()
