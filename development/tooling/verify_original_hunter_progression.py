"""Compare the complete own Hunter arithmetic with actual original JVM values.

Compiles only our isolated arithmetic and generated observer harness. This is
not Minecraft integration, save/UI/armour acceptance or complete Hunter parity.
"""
import argparse,hashlib,json,os,struct,subprocess
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb')as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)
def check(r):
    actual=ref(r['path']);assert all(actual[k]==r[k]for k in ('bytes','sha256')),r['path']
def bits(value):return struct.unpack('>i',struct.pack('>f',value))[0]

def run(a):
    parent=read(a.original);assert parent['passed']and parent['family']=='hunter'and parent['dedicatedServerOnly']and not parent['clientLaunched']and parent['allOriginalModAndLibraryBytesUnchanged']and parent['temporaryObserverRemoved']
    for r in (parent['original'],parent['source'],parent['producer'],parent['capture'],parent['compileSdk']['receipt'],parent['compileSdk']['artifact']):check(r)
    assert all(parent['actualOriginalMod'][k]==parent['original'][k]for k in ('bytes','sha256'))
    actual=read(parent['capture']['path']);assert actual['passed']and actual['originalRuntime']and not actual['synthetic']
    cases=actual['completeOriginalExperienceCases'];gates=actual['completeNativeGateCases'];assert len(cases)==3200 and len(gates)==3700 and len(actual['completeRegisteredHunterEntities'])==48
    out=Path(a.output).absolute();root=Path(os.environ['ENDERLOOM_DEVELOPMENT_ROOT']).absolute();assert out.is_relative_to(root)and not out.exists();work=out.with_suffix('.runtime');assert not work.exists();work.mkdir();(work/'classes').mkdir()
    source=Path(a.source)if a.source else Path(__file__).with_name('java')/'HunterProgression.java'
    if not a.source and not source.is_file():source=Path(__file__).with_name('HunterProgression.java')
    assert source.is_file(),'Select the own HunterProgression.java policy with --source'
    frozen=work/source.name;frozen.write_bytes(source.read_bytes())
    rows=['\t'.join(map(str,(r['initialLevel'],bits(r['initialXp']),bits(r['award']),r['actualLevel'],bits(r['actualXp']),bits(r['originalThreshold']))))for r in cases]
    (work/'actual-original-xp.tsv').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    rows=['\t'.join(map(str,(r['level'],r['required'],int(r['actualSurvivalAllowed']),int(r['actualCreativeAllowed']))))for r in gates]
    (work/'actual-original-gates.tsv').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    harness=work/'VerifyHunter.java';harness.write_text('''import java.nio.file.*;import net.tslat.aoa3.player.skill.HunterProgression;
public class VerifyHunter{
 public static void main(String[]args)throws Exception{int cases=0,gates=0;
 for(String line:Files.readAllLines(Path.of(args[0]))){String[]r=line.split("\\t");int level=Integer.parseInt(r[0]);float xp=Float.intBitsToFloat(Integer.parseInt(r[1])),amount=Float.intBitsToFloat(Integer.parseInt(r[2]));var result=HunterProgression.award(level,xp,amount);
 if(result.level()!=Integer.parseInt(r[3])||Float.floatToIntBits(result.xp())!=Integer.parseInt(r[4])||Float.floatToIntBits(HunterProgression.threshold(level))!=Integer.parseInt(r[5]))throw new AssertionError("Actual original XP mismatch:"+line+" result="+result);cases++;}
 for(String line:Files.readAllLines(Path.of(args[1]))){String[]r=line.split("\\t");int level=Integer.parseInt(r[0]),required=Integer.parseInt(r[1]);if(HunterProgression.canHunt(level,required,false)!=(Integer.parseInt(r[2])==1)||HunterProgression.canHunt(level,required,true)!=(Integer.parseInt(r[3])==1))throw new AssertionError("Actual original gate mismatch:"+line);gates++;}
 System.out.println("Complete actual original Hunter cases="+cases+", gates="+gates);
 }}''',encoding='utf-8')
    env=dict(os.environ,TEMP=str(work),TMP=str(work));jdk=Path(a.jdk)
    compiled=subprocess.run([str(jdk/'bin/javac.exe'),'-proc:none','-encoding','UTF-8','--release','17','-d',str(work/'classes'),str(frozen),str(harness)],env=env,capture_output=True,text=True,encoding='utf-8');(work/'compiler.log').write_text(compiled.stdout+compiled.stderr,encoding='utf-8');assert compiled.returncode==0,compiled.stderr
    tested=subprocess.run([str(jdk/'bin/java.exe'),'-cp',str(work/'classes'),'VerifyHunter',str(work/'actual-original-xp.tsv'),str(work/'actual-original-gates.tsv')],env=env,capture_output=True,text=True,encoding='utf-8');(work/'native-comparison.log').write_text(tested.stdout+tested.stderr,encoding='utf-8');assert tested.returncode==0,tested.stderr
    text=frozen.read_text(encoding='utf-8');faults=[]
    variants=[('cfr-threshold-order',text.replace('            remaining-=required-xp;\n','').replace('            level++;xp=0;required=threshold(level);','            level++;xp=0;required=threshold(level);remaining-=required-xp;')),('fractional-xp-truncated',text.replace('xp+remaining','(int)(xp+remaining)')),('creative-choice-removed',text.replace('creative||level>=requirement','level>=requirement')),('zero-requirement-lost',text.replace('requirement<0','requirement<1'))]
    for label,damaged in variants:
        assert damaged!=text;directory=work/label;directory.mkdir();candidate=directory/'HunterProgression.java';candidate.write_text(damaged,encoding='utf-8');classes=directory/'classes';classes.mkdir()
        compiled_fault=subprocess.run([str(jdk/'bin/javac.exe'),'-proc:none','-encoding','UTF-8','--release','17','-d',str(classes),str(candidate),str(harness)],env=env,capture_output=True,text=True,encoding='utf-8');assert compiled_fault.returncode==0,compiled_fault.stderr
        rejected=subprocess.run([str(jdk/'bin/java.exe'),'-cp',str(classes),'VerifyHunter',str(work/'actual-original-xp.tsv'),str(work/'actual-original-gates.tsv')],env=env,capture_output=True,text=True,encoding='utf-8',timeout=15);assert rejected.returncode!=0,'Generated damaged policy accepted: '+label
        (directory/'generated-fault.log').write_text(rejected.stdout+rejected.stderr,encoding='utf-8');faults.append(dict(fault=label,generated=True,rejected=True,javaExitCode=rejected.returncode))
    record=dict(passed=True,arithmeticOnly=True,actualOriginal=ref(a.original),nativeCapture=parent['capture'],ownImplementation=ref(frozen),compiler=ref(jdk/'bin/javac.exe'),harness=ref(harness),completeExperienceCases=3200,completeNativeGateCases=3700,actualOriginalHunterEntities=48,allFloatBitsEqual=True,generatedFaults=faults,cfrThresholdEvaluationOrderTrusted=False,originalBytesChanged=False,originalDefectClaimed=False,minecraftIntegrationVerified=False,saveUiArmourVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(record,indent=2),encoding='utf-8');print(json.dumps(record))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('original','jdk','output'):p.add_argument(name)
    p.add_argument('--source',help='Explicit own policy source; supports both Enderloom and the public audit-tool layout')
    run(p.parse_args())
