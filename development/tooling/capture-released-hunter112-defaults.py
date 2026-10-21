"""Execute the unchanged released 1.12.2 Hunter configuration constructor.

The selected real class uses Java strings/arrays and needs no game runtime.
No Minecraft classes are substituted. This proves defaults, not combat/parser
execution, a playable original client or target-native migration acceptance.
"""
import argparse,base64,hashlib,json,os,subprocess,zipfile
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb')as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)

def run(a):
    download,evidence=read(a.release),read(a.evidence);assert download['passed']and download['fileId']=='3054253'and download['projectId']=='311054'
    original=ref(download['path']);assert original['sha256']==download['sha256']and original['bytes']==download['bytes']
    with Path(original['path']).open('rb')as f:assert hashlib.file_digest(f,'sha1').hexdigest()==download['sha1']
    member='net/tslat/aoa3/utils/ConfigurationUtil$EntityConfig$SubCategoryHunterEntities.class';expected=next(r for r in evidence['method_evidence']if r['class_path']==member and r['name']=='<init>')
    with zipfile.ZipFile(original['path'])as z:class_sha=hashlib.sha256(z.read(member)).hexdigest();assert class_sha==expected['class_sha256']
    out=Path(a.output).absolute();root=Path(os.environ['ENDERLOOM_DEVELOPMENT_ROOT']).absolute();assert out.is_relative_to(root)and not out.exists();work=out.with_suffix('.runtime');assert not work.exists();work.mkdir();classes=work/'classes';classes.mkdir()
    source=work/'ReleasedHunterDefaults.java';source.write_text('''import java.net.*;import java.nio.file.*;import java.nio.charset.StandardCharsets;import java.lang.reflect.*;import java.util.*;
public class ReleasedHunterDefaults {
 public static void main(String[]args)throws Exception{
  URL url=Path.of(args[0]).toUri().toURL();
  try(URLClassLoader loader=new URLClassLoader(new URL[]{url},null)){
   Class<?> actual=Class.forName("net.tslat.aoa3.utils.ConfigurationUtil$EntityConfig$SubCategoryHunterEntities",true,loader);
   if(!actual.getProtectionDomain().getCodeSource().getLocation().equals(url)||actual.getSuperclass()!=Object.class)throw new AssertionError("Released class origin changed");
   Object config=actual.getDeclaredConstructor().newInstance();int count=0,fields=0;
   for(Field field:actual.getDeclaredFields())if(field.getType()==String[].class){field.setAccessible(true);String[]values=(String[])field.get(config);System.out.println("FIELD\\t"+field.getName());fields++;
    for(String value:values){System.out.println("ENTRY\\t"+count+"\\t"+Base64.getEncoder().encodeToString(value.getBytes(StandardCharsets.UTF_8)));count++;}}
   if(fields!=1||count!=71)throw new AssertionError("Incomplete actual released default array");System.out.println("COMPLETE\\t"+count);
  }
 }
}''',encoding='utf-8')
    jdk=Path(a.jdk);env=dict(os.environ,TEMP=str(work),TMP=str(work));compiler=subprocess.run([str(jdk/'bin/javac.exe'),'-proc:none','--release','17','-encoding','UTF-8','-d',str(classes),str(source)],env=env,capture_output=True,text=True,encoding='utf-8');(work/'compiler.log').write_text(compiler.stdout+compiler.stderr,encoding='utf-8');assert compiler.returncode==0,compiler.stderr
    child=subprocess.run([str(jdk/'bin/java.exe'),'-cp',str(classes),'ReleasedHunterDefaults',original['path']],env=env,capture_output=True,text=True,encoding='utf-8',timeout=30);stdout=work/'actual-released-defaults.log';stdout.write_text(child.stdout+child.stderr,encoding='utf-8');assert child.returncode==0,child.stderr
    entries=[base64.b64decode(line.split('\t')[2]).decode('utf-8')for line in child.stdout.splitlines()if line.startswith('ENTRY\t')];assert len(entries)==71 and entries==[r['default_entry']for r in evidence['entries']]
    rows=[]
    for entry in entries:
        parts=entry.split(' ');assert len(parts)==3 and parts[0].startswith('aoa3:')and parts[1].startswith('lvl:')and parts[2].startswith('xp:');rows.append(dict(id=parts[0],level=int(parts[1][4:]),xpText=parts[2][3:],actualReleasedDefault=entry))
    assert ref(original['path'])==original
    result=dict(passed=True,defaultsOnly=True,actualReleasedClassExecuted=True,noMinecraftStandIns=True,minecraftGameRuntimeLaunched=False,clientLaunched=False,original=original,providerReceipt=ref(a.release),releasedMethodEvidence=ref(a.evidence),originalClass=dict(path=member,sha256=class_sha),probe=ref(source),actualJvmOutput=ref(stdout),completeDefaultEntries=rows,defaultCount=71,parserAndCombatExecuted=False,targetNativeIntegrationVerified=False,completeHunterFamilyVerified=False,completeAoAPort=False,producer=ref(__file__))
    out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:result[k]for k in ['passed','actualReleasedClassExecuted','defaultCount','minecraftGameRuntimeLaunched','noMinecraftStandIns']}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('release','evidence','jdk','output'):p.add_argument(n)
    run(p.parse_args())
