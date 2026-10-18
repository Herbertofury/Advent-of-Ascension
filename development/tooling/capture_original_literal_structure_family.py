"""Execute unchanged complete original literal-structure programs on fixtures.

The set-block boundary is labelled synthetic fixture infrastructure. This is
original bytecode evidence, never original Minecraft or target world acceptance.
Strict constant-pool contracts reject unknown program dependencies.
"""
import argparse,hashlib,json,os,re,struct,subprocess,zipfile
from pathlib import Path

def require(v,why):
    if not v:raise ValueError(why)
def artifact(p):
    p=Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def contracts(raw):
    require(raw[:4]==b'\xca\xfe\xba\xbe','Original class magic differs');count=struct.unpack_from('>H',raw,8)[0];at=10;pool=[None]*count;i=1
    while i<count:
        tag=raw[at];at+=1
        if tag==1:
            n=struct.unpack_from('>H',raw,at)[0];at+=2;pool[i]=(tag,raw[at:at+n].decode('utf-8',errors='replace'));at+=n
        elif tag in [7,8,16,19,20]:pool[i]=(tag,struct.unpack_from('>H',raw,at)[0]);at+=2
        elif tag in [9,10,11,12,17,18]:pool[i]=(tag,*struct.unpack_from('>HH',raw,at));at+=4
        elif tag in [3,4]:pool[i]=(tag,);at+=4
        elif tag in [5,6]:pool[i]=(tag,);at+=8;i+=1
        elif tag==15:pool[i]=(tag,);at+=3
        else:raise ValueError('Unsupported complete constant-pool tag '+str(tag))
        i+=1
    refs=[]
    for r in pool:
        if r and r[0] in [9,10,11]:
            owner=pool[pool[r[1]][1]][1];pair=pool[r[2]];refs.append(dict(kind='field' if r[0]==9 else 'method',owner=owner,name=pool[pair[1]][1],descriptor=pool[pair[2]][1]))
    return refs
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['authority','java','output']:p.add_argument(name)
    a=p.parse_args();authority=json.loads(Path(a.authority).read_text(encoding='utf-8'));original=authority['original'];require(artifact(original['path'])==original,'Complete original archive changed')
    owner=Path(a.output).resolve();root=Path(os.environ['ENDERLOOM_DEVELOPMENT_ROOT']).resolve();require(root in owner.parents and not owner.exists(),'Use a new explicit development owner');owner.mkdir(parents=True)
    sources=owner/'fixture-sources';fixtures=owner/'fixture-classes';classes=owner/'unchanged-original-classes';sources.mkdir();fixtures.mkdir();classes.mkdir();programs=[];bindings={};all_contracts=[]
    suffixes=['FragmentTempleAbyss','FragmentTempleBarathos','FragmentTempleGreckon','FragmentTempleHaven','FragmentTempleBorean']
    with zipfile.ZipFile(original['path']) as z:
        for suffix in suffixes:
            matches=[n for n in z.namelist() if n.endswith('/'+suffix+'.class')];require(len(matches)==1,'Ambiguous/missing whole original temple '+suffix);name=matches[0];raw=z.read(name);refs=contracts(raw)
            for r in refs:
                if r['kind']=='field':
                    require(r['owner'] in ['net/nevermine/izer/Blockizer','net/minecraft/init/Blocks'] and r['descriptor']=='Lnet/minecraft/block/Block;','Unknown complete literal block dependency: '+str(r))
                    require(re.fullmatch(r'[A-Za-z_$][A-Za-z0-9_$]*',r['name']),'Nonliteral fixture binding');bindings.setdefault(r['owner'],set()).add(r['name'])
                else:require((r['owner']=='net/minecraft/world/gen/feature/WorldGenerator' and r['name']=='<init>' and r['descriptor'] in ['()V','(Z)V']) or
                    (r['owner']=='net/minecraft/world/World' and (r['name'],r['descriptor']) in [('func_147449_b','(IIILnet/minecraft/block/Block;)Z'),('func_147465_d','(IIILnet/minecraft/block/Block;II)Z')]) or
                    (r['owner']==name[:-6] and re.fullmatch(r'generate\d+',r['name']) and r['descriptor']=='(Lnet/minecraft/world/World;Ljava/util/Random;III)Z'),'Nonliteral/unsupported whole program dependency: '+str(r))
            target=classes/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw);programs.append(dict(className=name[:-6].replace('/','.'),originalEntry=name,originalSha256=hashlib.sha256(raw).hexdigest(),retainedClass=artifact(target)));all_contracts.append(dict(originalEntry=name,completeFieldAndMethodContracts=refs))
    payload={
        'net/minecraft/block/Block.java':'package net.minecraft.block; public final class Block { public final String field; public Block(String field){this.field=field;} }\n',
        'net/minecraft/world/gen/feature/WorldGenerator.java':'package net.minecraft.world.gen.feature; public class WorldGenerator { public WorldGenerator(){} public WorldGenerator(boolean notify){} }\n',
        'net/minecraft/world/World.java':'''package net.minecraft.world;
import java.util.*;import net.minecraft.block.Block;
public final class World {
 public final TreeMap<String,String> states=new TreeMap<String,String>();public final StringBuilder events=new StringBuilder();public int writes;
 private boolean put(int x,int y,int z,Block block,int metadata,String flags){if(block==null)throw new IllegalStateException("Missing original field");String pos=x+","+y+","+z;states.put(pos,block.field+" "+metadata);events.append("W ").append(x).append(' ').append(y).append(' ').append(z).append(' ').append(block.field).append(' ').append(metadata).append(' ').append(flags).append('\\n');writes++;return true;}
 public boolean func_147449_b(int x,int y,int z,Block block){return put(x,y,z,block,0,"original-default-call");}
 public boolean func_147465_d(int x,int y,int z,Block block,int metadata,int flags){return put(x,y,z,block,metadata,Integer.toString(flags));}
 public String finalStates(){StringBuilder out=new StringBuilder();for(Map.Entry<String,String> e:states.entrySet())out.append(e.getKey()).append(' ').append(e.getValue()).append('\\n');return out.toString();}
}
'''}
    for package,fields in bindings.items():
        pkg,name=package.rsplit('/',1);payload[package+'.java']='package '+pkg.replace('/','.')+';\nimport net.minecraft.block.Block;\npublic final class '+name+' {\n'+''.join(' public static final Block '+field+'=new Block('+json.dumps(package+'.'+field)+');\n' for field in sorted(fields))+'}\n'
    payload['OriginalLiteralStructureFamily.java']='''import java.lang.reflect.*;import java.nio.charset.StandardCharsets;import java.nio.file.*;import java.util.*;import net.minecraft.world.World;
public final class OriginalLiteralStructureFamily {
 public static final class CountedRandom extends Random {public int calls;public CountedRandom(long seed){super(seed);}@Override protected int next(int bits){calls++;return super.next(bits);}}
 public static void main(String[] args)throws Exception {
  Path out=Paths.get(args[0]);Files.createDirectory(out);String[] programs=PROGRAMS;
  int[][] origins={{0,0,0},{31,37,-47},{-64,1,127},{100000,64,-100000},{29999900,64,-29999900},{-29999900,0,29999900},{13,127,-11}};
  long[] seeds={0,1,-1,123456789,Long.MIN_VALUE,Long.MAX_VALUE,-71};
  for(int program=0;program<programs.length;program++)for(int fixture=0;fixture<origins.length;fixture++){
   World world=new World();CountedRandom random=new CountedRandom(seeds[fixture]);int[] origin=origins[fixture];Class<?> type=Class.forName(programs[program]);Object value=type.getConstructor().newInstance();
   Object result=type.getMethod("func_76484_a",World.class,Random.class,int.class,int.class,int.class).invoke(value,world,random,origin[0],origin[1],origin[2]);if(!Boolean.TRUE.equals(result))throw new IllegalStateException("Original complete program returned false");
   String name="program-"+program+"-case-"+fixture;Files.write(out.resolve(name+".events.txt"),world.events.toString().getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);Files.write(out.resolve(name+".states.txt"),world.finalStates().getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);
   System.out.println(name+" "+program+" "+fixture+" "+origin[0]+" "+origin[1]+" "+origin[2]+" "+world.writes+" "+world.states.size()+" "+random.calls);
  }
 }
}
'''.replace('PROGRAMS','new String[]{'+','.join(json.dumps(r['className']) for r in programs)+'}')
    source_refs=[]
    for name,text in payload.items():
        target=sources/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8');source_refs.append(artifact(target))
    java=artifact(a.java);javac=artifact(Path(a.java).with_name('javac.exe'));arguments=['--release','8','-encoding','UTF-8','-d',str(fixtures),*[r['path'] for r in source_refs]]
    compiler=subprocess.run([javac['path'],*arguments],capture_output=True,timeout=120,creationflags=subprocess.CREATE_NO_WINDOW);(owner/'compiler.stdout.log').write_bytes(compiler.stdout);(owner/'compiler.stderr.log').write_bytes(compiler.stderr);require(compiler.returncode==0,'Literal fixture compilation failed: '+compiler.stderr.decode('utf-8',errors='replace')[-2000:])
    command=[java['path'],'-Xmx512M','-Djava.awt.headless=true','-classpath',os.pathsep.join([str(fixtures),str(classes)]),'OriginalLiteralStructureFamily',str(owner/'complete-traces')]
    result=subprocess.run(command,capture_output=True,timeout=120,creationflags=subprocess.CREATE_NO_WINDOW);(owner/'run.stdout.log').write_bytes(result.stdout);(owner/'run.stderr.log').write_bytes(result.stderr);require(result.returncode==0,'Original literal program execution failed: '+result.stderr.decode('utf-8',errors='replace')[-2000:])
    cases=[];canonical={}
    for line in result.stdout.decode('utf-8').splitlines():
        name,program,fixture,x,y,z,writes,states,calls=line.split();program,fixture=int(program),int(fixture);origin=list(map(int,[x,y,z]));events=artifact(owner/'complete-traces'/(name+'.events.txt'));final=artifact(owner/'complete-traces'/(name+'.states.txt'))
        rows=[r.split(' ') for r in Path(events['path']).read_text(encoding='utf-8').splitlines()];require(len(rows)==int(writes)>1000 and len(Path(final['path']).read_text(encoding='utf-8').splitlines())==int(states) and int(calls)==0,'Incomplete/nonliteral original geometry/RNG domain')
        relative=[[int(r[1])-origin[0],int(r[2])-origin[1],int(r[3])-origin[2],r[4],int(r[5]),r[6]] for r in rows];require(all(r[0]=='W' and len(r)==7 for r in rows),'Unknown original complete event')
        if program in canonical:require(relative==canonical[program],'Original complete structure is not translation invariant')
        else:canonical[program]=relative
        cases.append(dict(id=name,originalClass=programs[program]['className'],fixture=fixture,origin=origin,completeWrites=int(writes),completeWrittenPositions=int(states),randomCalls=int(calls),completeOrderedEvents=events,completeFinalWrittenStates=final,allRelativeEventsEqual=True))
    require(len(cases)==35 and len(canonical)==5,'Incomplete five-temple whole-program domain');data=owner/'complete-relative-placement-programs.json';data.write_text(json.dumps({programs[i]['className']:rows for i,rows in sorted(canonical.items())},separators=(',',':')),encoding='utf-8')
    require(artifact(original['path'])==original,'Original complete mod bytes changed');producer=owner/Path(__file__).name;producer.write_bytes(Path(__file__).read_bytes())
    report=dict(passed=True,originalBytecodeExecuted=True,originalMinecraftRuntime=False,generatedWorldFixtures=True,fixtureSetBlockAlwaysSucceeds=True,completeOriginalPrograms=programs,completeDependencyContracts=all_contracts,originalArchive=original,sourceRecoveryAuthority=artifact(a.authority),completeCases=cases,completeRelativePrograms=artifact(data),fixtureSources=source_refs,java=java,javac=javac,command=command,stdout=artifact(owner/'run.stdout.log'),stderr=artifact(owner/'run.stderr.log'),producer=artifact(producer),nativeRegistryIdentityVerified=False,nativePlacementVerified=False,originalWorldParityVerified=False,completeAoAPort=False)
    out=owner/'complete-original-literal-family.json';out.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,completeOriginalPrograms=5,completeCases=35,completeOrderedWrites=sum(r['completeWrites'] for r in cases),completeRelativePrograms=report['completeRelativePrograms'],output=str(out),nativePlacementVerified=False)))

if __name__=='__main__':main()
