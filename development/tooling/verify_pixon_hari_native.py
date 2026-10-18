"""Extend complete Pixon proof with both actual backends and a clean Hari seed."""
import argparse,copy,gzip,hashlib,importlib.util,json,struct
from pathlib import Path

def require(value,message):
    if not value:raise ValueError(message)

def artifact(path):
    p=Path(path).absolute()
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)

def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def check(ref):
    actual=artifact(ref['path']);require((actual['bytes'],actual['sha256'])==(ref['bytes'],ref['sha256']),'Changed complete authority: '+ref['path']);return actual

def run(pixon_file,hari_file,capture_file,seed_file,output):
    proof,hari,seed=map(read,[pixon_file,hari_file,seed_file]);require(proof['passed'] and proof['client'] and not proof['completeAoAPort'],'Complete actual Pixon native client/server proof required')
    for key in ['server','sourcePlan','previousServer','nativeCapture','verifier']:check(proof[key])
    check(proof['client']['receipt']);check(proof['canonicalMod']);client=read(proof['client']['receipt']['path'])
    server=read(proof['server']['path']);canonical=server['build']['artifacts'][0]
    require(canonical==proof['canonicalMod'] and server['passed'] and client['passed'],'Different canonical native artifact')
    source=Path(__file__).with_name('verify_overlay_native.py');ref=artifact(source)
    spec=importlib.util.spec_from_file_location('retained_native_overlay_cases',source);overlay=importlib.util.module_from_spec(spec);spec.loader.exec_module(overlay)
    require(hari['passed'] and hari['nativeVulkanVerified'] and hari['nativeRendererSelected'] and not hari['physicalFallbackPresent'] and not hari['forbiddenFailures'],'Actual required Hari production run failed')
    require(hari['finished']['cleaned_up'] and hari['jvmChoicesRestored'] and hari['horizontalDistance']>0.1 and hari['observedRenderIntervals']>0,'Native world/movement/choice restoration failed')
    require(hari['cleanProductionSeedVerified'] and seed['passed'] and seed['identity']['artifact']==canonical['sha256'] and seed['identity']['target']==server['build']['primary_target'],'Wrong complete production cohort')
    require(hari['productionServer']==seed_file and artifact(seed_file)['sha256']==hari['productionServerSha256'],'Wrong production server evidence')
    require(hari['inputs'][0]['sha256']==canonical['sha256'],'Hari must exercise the exact canonical JAR')
    require(any(r['sha256']==hari['inputs'][1]['sha256'] for r in seed['identity']['dependencies']),'Exact optional Hari dependency missing from production server')
    for item in [hari['inputs'][0],hari['inputs'][1],hari['fixture']['artifact'],hari['fixture']['source'],hari['fixture']['mapping']]:check(item)
    require(artifact(hari['qaSource']['path'])['sha256']==hari['qaSource']['sha256'],'Native production runner changed')
    capture=read(capture_file);require(capture==hari['activeOverlayFixture'] and capture['physicalGlCalls']==0 and capture['fixtureBoundary']=='Actual Forge GUI overlay Post inside the native render pass','Native capture/actual boundary differs')
    native_draws=overlay.cases(capture,'Hari Vulkan')
    gl_path=Path(client['build']['build_root'])/'run/enderloom-forge1201-overlay-render-state.json';gl=read(gl_path);gl_draws=overlay.cases(gl,'OpenGL')
    require(Path(client['build']['stdout_path']).read_text(encoding='utf-8').count('ENDERLOOM_FORGE1201_OVERLAY_RENDER_STATE '+gl_path.read_text(encoding='utf-8'))==1,'Missing exact native GL draw log')
    equivalence=overlay.equivalent(canonical,hari['inputs'][0])
    preparation=read(hari['preparation']);require(artifact(hari['preparation'])['sha256']==hari['preparationSha256'] and preparation['identity']==seed['identity'] and preparation['world']==hari['world'],'Different imported production world')
    stage=read(preparation['seedStage']['path']);require(artifact(preparation['seedStage']['path'])['sha256']==preparation['seedStage']['sha256'] and stage['passed'] and stage['allOriginalSourceFilesUnchanged'] and stage['metadataChange']['exactByteInverseVerified'],'Unaccepted complete production clone')
    require(stage['sourceWorld']==seed['worldPath'] and stage['productionServer']==artifact(seed_file),'Clone belongs to another production seed')
    expected={}
    for row in stage['copied']:
        check(row['before']);relative=Path(row['copy']['path']).relative_to(stage['clone']).as_posix();selected=stage['metadataChange']['current'] if relative=='level.dat' else row['copy'];check(selected);expected[relative]=(selected['sha256'],selected['bytes'])
    old_metadata=Path(stage['sourceWorld'])/'level.dat';raw=gzip.decompress(old_metadata.read_bytes());changed=gzip.decompress(Path(stage['metadataChange']['current']['path']).read_bytes());anchor=b'\x08\x00\x09LevelName'
    require(raw.count(anchor)==changed.count(anchor)==1,'Ambiguous world display-name field')
    at=raw.index(anchor)+len(anchor);length=struct.unpack_from('>H',raw,at)[0];new=stage['newTitle'].encode('utf-8')
    require(changed==raw[:at]+struct.pack('>H',len(new))+new+raw[at+2+length:],'A world byte beyond the explicit new display name changed')
    installed=Path(hari['instance']['dir'])/'saves'/hari['world']['folder_name'];files=list(installed.rglob('*'))
    require(not any(p.is_symlink() or p.is_junction() for p in files),'Linked imported world member')
    actual={p.relative_to(installed).as_posix():(artifact(p)['sha256'],p.stat().st_size) for p in files if p.is_file()};require(actual==expected,'Complete original production world changed during testing')
    faults=[]
    for name,mutate in [('missing case',lambda d:d['completeDraws'].pop()),('physical fallback',lambda d:d.update(backend='OpenGL')),('lost state',lambda d:d.update(allStateRestored=False)),('wrong factors',lambda d:d['completeDraws'][0]['actualState'].__setitem__(3,0)),('duplicate case',lambda d:d['completeDraws'].__setitem__(0,copy.deepcopy(d['completeDraws'][1])))]:
        bad=copy.deepcopy(capture);mutate(bad);rejected=False
        try:overlay.cases(bad,'Hari Vulkan')
        except ValueError:rejected=True
        require(rejected,'Corrupt full native draw proof accepted: '+name);faults.append(dict(case=name,generated=True,rejected=True))
    require(artifact(source)==ref,'Native case verifier changed during execution')
    frozen=Path(output).with_suffix('.producer.py');frozen.write_bytes(Path(__file__).read_bytes());dependency=Path(output).with_suffix('.overlay-verifier.py');dependency.write_bytes(source.read_bytes())
    result=dict(schema=1,passed=True,synthetic=False,completeAoAPort=False,performanceVerified=False,fpsGoal=2000,canonicalMod=canonical,pixonNativeProof=artifact(pixon_file),server=proof['server'],client=proof['client']['receipt'],nativeHari=artifact(hari_file),nativeGlCapture=artifact(gl_path),nativeHariCapture=artifact(capture_file),renderer=hari['inputs'][1],actualOpenGlDraws=gl_draws,actualVulkanDraws=native_draws,hariProductionEquivalence=equivalence,completePreviousMembersRetained=proof['completePreviousMembersRetained'],currentMembers=proof['currentMembers'],cleanProductionSeedVerified=True,cleanProductionSeed=dict(server=artifact(seed_file),preparation=artifact(hari['preparation']),stage=artifact(preparation['seedStage']['path']),completeWorldFiles=len(actual),allOriginalSourceAndImportedWorldBytesUnchanged=True),generatedFaultControls=faults,verifier=artifact(frozen),verifierDependencies=[artifact(dependency)],qualifications=['Actual native GUI draws/state restoration, clean production rendering/movement and bounded current Pixon spawn fixtures are verified. Pixel-level raster parity, representative full content, full pack support, sustained FPS, migrations, multiplayer and the complete historical/latest union remain open.'])
    with Path(output).open('x',encoding='utf-8') as file:json.dump(result,file,indent=2)
    print(json.dumps(dict(passed=True,actualOpenGlDraws=gl_draws,actualVulkanDraws=native_draws,completeWorldFiles=len(actual),completeAoAPort=False,performanceVerified=False,output=output)))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['pixon','hari','capture','seed']:p.add_argument(name)
    p.add_argument('--output',required=True);a=p.parse_args();run(a.pixon,a.hari,a.capture,a.seed,a.output)
