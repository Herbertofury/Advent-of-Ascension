"""Compare all 2,800 real original Snapshot Hunter rewards with the own policy.

Uses the retained actual original JVM capture; compiles only our arithmetic and
an observer. No Minecraft stand-ins, new runtime copy, client or audio device.
"""
import argparse,hashlib,json,os,struct,subprocess
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb')as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),sha256=digest,bytes=p.stat().st_size)
def check(r):
    a=ref(r['path']);assert all(a[k]==r[k]for k in ('sha256','bytes')),r['path']
def bits(v):return struct.unpack('>i',struct.pack('>f',v))[0]

def run(a):
    proof=read(a.original);assert proof['passed']and proof['originalRuntime']and not proof['sourceMutation']and proof['originalModBytesUnchanged']and proof['exit']['code']==0
    for r in [proof[k]for k in ['source','originalWholeMod','probe','stdout','stderr','capture','nativeCapture','producer']]:check(r)
    captured=read(proof['capture']['path']);cases=captured['completeHunterRewardCases'];assert captured['passed']and captured['originalRuntime']and not captured['synthetic']and len(cases)==2800
    out=Path(a.output).absolute();root=Path(os.environ['ENDERLOOM_DEVELOPMENT_ROOT']).absolute();assert out.is_relative_to(root)and not out.exists();work=out.with_suffix('.runtime');assert not work.exists();work.mkdir()
    policy=Path(a.source)if a.source else Path(__file__).with_name('java')/'HunterProgression.java';frozen=work/policy.name;frozen.write_bytes(policy.read_bytes())
    table=work/'complete-actual-original-rewards.tsv';table.write_text('\n'.join('\t'.join(map(str,[r['initialLevel'],r['requiredLevel'],bits(r['initialXp']),r['amount'],r['actualLevel'],bits(r['actualXp'])]))for r in cases)+'\n',encoding='utf-8')
    harness=work/'VerifySnapshotHunter.java';harness.write_text('''import java.nio.file.*;import net.tslat.aoa3.player.skill.HunterProgression;
public class VerifySnapshotHunter{public static void main(String[]args)throws Exception{int n=0;
for(String line:Files.readAllLines(Path.of(args[0]))){String[]r=line.split("\\t");int level=Integer.parseInt(r[0]),required=Integer.parseInt(r[1]),amount=Integer.parseInt(r[3]);float xp=Float.intBitsToFloat(Integer.parseInt(r[2]));
var result=level<required?new HunterProgression.State(level,xp):HunterProgression.awardSnapshot(level,xp,amount);
if(result.level()!=Integer.parseInt(r[4])||Float.floatToIntBits(result.xp())!=Integer.parseInt(r[5]))throw new AssertionError("Actual original Snapshot mismatch "+line+" result="+result);n++;}
System.out.println("Complete original Snapshot cases="+n);}}''',encoding='utf-8')
    jdk=Path(a.jdk);env=dict(os.environ,TEMP=str(work),TMP=str(work));faults=[]
    def execute(folder,policy_text,harness_text):
        folder.mkdir(exist_ok=True);classes=folder/'classes';classes.mkdir();p=folder/'HunterProgression.java';p.write_text(policy_text,encoding='utf-8');h=folder/'VerifySnapshotHunter.java';h.write_text(harness_text,encoding='utf-8')
        compiled=subprocess.run([str(jdk/'bin/javac.exe'),'-proc:none','--release','17','-encoding','UTF-8','-d',str(classes),str(p),str(h)],env=env,capture_output=True,text=True,encoding='utf-8');(folder/'compiler.log').write_text(compiled.stdout+compiled.stderr,encoding='utf-8');assert compiled.returncode==0,compiled.stderr
        result=subprocess.run([str(jdk/'bin/java.exe'),'-cp',str(classes),'VerifySnapshotHunter',str(table)],env=env,capture_output=True,text=True,encoding='utf-8',timeout=15);(folder/'native-comparison.log').write_text(result.stdout+result.stderr,encoding='utf-8');return result
    policy_text=frozen.read_text(encoding='utf-8');harness_text=harness.read_text(encoding='utf-8');assert execute(work/'complete',policy_text,harness_text).returncode==0
    for label,p,h in [('integer-residual-rounded',policy_text.replace('amount=(int)(amount-left)','amount=Math.round(amount-left)'),harness_text),('snapshot-policy-replaced-with-newer-float-policy',policy_text,harness_text.replace('HunterProgression.awardSnapshot(level,xp,amount)','HunterProgression.award(level,xp,(float)amount)'))]:
        assert p!=policy_text or h!=harness_text;result=execute(work/label,p,h);assert result.returncode!=0,'Generated policy regression accepted: '+label;faults.append(dict(fault=label,generated=True,rejected=True))
    result=dict(passed=True,arithmeticOnly=True,actualOriginal=ref(a.original),actualOriginalCapture=proof['capture'],ownPolicy=ref(frozen),observer=ref(harness),completeOriginalSnapshotCases=2800,allFloatBitsEqual=True,generatedFaults=faults,noOriginalRuntimeCopiesCreated=True,clientLaunched=False,minecraftTargetIntegrationVerified=False,completeHunterFamilyVerified=False,completeAoAPort=False,producer=ref(__file__))
    out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:result[k]for k in ['passed','completeOriginalSnapshotCases','allFloatBitsEqual','clientLaunched']}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('original','jdk','output'):p.add_argument(n)
    p.add_argument('--source');run(p.parse_args())
