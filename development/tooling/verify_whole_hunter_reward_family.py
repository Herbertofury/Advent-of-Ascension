"""Read every recovered Hunter reward from the unchanged original JVM bytecode.

The full 93-owner family includes death rewards and the Vulcane level gate.
Vulcane's own XP belongs to Vulcanism, not Hunter; do not conflate the two.
Decompiler literals are checked against actual instructions, never accepted as
behavior evidence by themselves. This is source admission, not target gameplay.
"""
import argparse,hashlib,json,os,re,subprocess,zipfile
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb')as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)
def check(r):
    actual=ref(r['path']);assert all(actual[k]==r[k]for k in ('bytes','sha256')),r['path']

def run(a):
    recovery=read(a.recovery);assert recovery['passed']and recovery['analysisOnly']and recovery['completeInputBytesUnchanged'];check(recovery['original'])
    sources=recovery['completeSelectedSourceCandidates'];assert len(sources)==93
    classes=[];expected={}
    for r in sources:
        check(r);text=Path(r['path']).read_text(encoding='utf-8');package=re.search(r'^package ([\w.]+);',text,re.M)[1];owner=package+'.'+Path(r['path']).stem;classes.append(owner)
        amounts=re.findall(r'\.addExperience\((\d+(?:\.\d+)?)f, PlayerContainer\.Skills\.Hunter\)',text)
        if not amounts:assert owner=='net.nevermine.item.weapon.vulcane.BaseVulcane'and'getLevel(PlayerContainer.Skills.Hunter)'in text and'PlayerContainer.Skills.Vulcanism'in text,'Missing complete recovered reward expression: '+owner
        expected[owner]=sorted(map(float,amounts))
    out=Path(a.output).absolute();assert out.is_relative_to(Path(os.environ['ENDERLOOM_DEVELOPMENT_ROOT']).absolute())and not out.exists()
    tool=Path(a.jdk)/'bin/javap.exe';result=subprocess.run([str(tool),'-c','-p','-classpath',recovery['original']['path'],*classes],capture_output=True,text=True,encoding='utf-8',timeout=120);assert result.returncode==0,result.stderr
    raw=Path(str(out)+'.original-javap.txt');assert not raw.exists();raw.write_text(result.stdout,encoding='utf-8')
    seen={};owner=None;method=None;instructions=[];observed=[];other_skill_sites=[]
    for line in result.stdout.splitlines():
        declaration=re.match(r'^(?:public |protected |private |final |abstract )*class ([\w.$]+)',line)
        if declaration:owner=declaration[1];assert owner in expected;seen.setdefault(owner,[]);instructions=[];method=None;continue
        if re.match(r'^  (?:public|protected|private|static)',line)and line.endswith(';'):method=line.strip();instructions=[]
        instruction=re.match(r'^\s+(\d+):\s+(\w+)(.*)$',line)
        if not instruction:continue
        at,opcode,tail=instruction.groups()
        if opcode=='invokevirtual'and 'net/nevermine/container/PlayerContainer.addExperience:(FLnet/nevermine/container/PlayerContainer$Skills;)V'in tail:
            assert len(instructions)>=2 and instructions[-1][1]=='getstatic',owner
            if 'PlayerContainer$Skills.Hunter:'not in instructions[-1][2]:
                other_skill_sites.append(dict(originalClass=owner,method=method,actualSkillInstruction=instructions[-1][2].strip(),bytecodeOffset=int(at)));instructions.append((int(at),opcode,tail));continue
            load=instructions[-2];literal=re.search(r'// float ([\d.Ee+-]+)f',load[2])
            if load[1]in ('ldc','ldc_w')and literal:amount=float(literal[1])
            elif load[1]in ('fconst_0','fconst_1','fconst_2'):amount=float(load[1][-1])
            else:raise AssertionError('Nonliteral original reward requires a complete expression adapter: '+owner+' '+str(load))
            seen[owner].append(amount);observed.append(dict(originalClass=owner,method=method,bytecodeOffset=int(at),actualFloatReward=amount,actualNativeSkill='Hunter',inputBytesUnchanged=True))
        instructions.append((int(at),opcode,tail))
    assert set(seen)==set(expected)
    for key in expected:assert sorted(seen[key])==expected[key],key
    with zipfile.ZipFile(recovery['original']['path'])as z:
        members=[dict(entry=c.replace('.','/')+'.class',bytes=len(z.read(c.replace('.','/')+'.class')),sha256=hashlib.sha256(z.read(c.replace('.','/')+'.class')).hexdigest())for c in sorted(classes)]
    check(recovery['original']);frozen=Path(str(out)+'.producer.py');frozen.write_bytes(Path(__file__).read_bytes())
    report=dict(passed=True,sourceAdmissionOnly=True,original=recovery['original'],recovery=ref(a.recovery),javap=ref(tool),completeOriginalJavap=ref(raw),completeWholeClassOwners=len(classes),completeRewardCallSites=len(observed),otherSkillDependencyCallSites=other_skill_sites,originalMembers=members,completeActualRewardInstructions=observed,allRecoveredFloatLiteralsVerified=True,sourceBytesChanged=False,nativeTargetDispatchVerified=False,completeHunterFamilyVerified=False,completeAoAPort=False,producer=ref(frozen))
    out.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,completeWholeClassOwners=len(classes),completeRewardCallSites=len(observed),nativeTargetDispatchVerified=False)))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('recovery','jdk','output'):p.add_argument(key)
    run(p.parse_args())
