"""Bind real dedicated transport, every dimension and saved inventory to logs.

Sky/fog captures and render intervals do not establish terrain/model raster
parity, combat, natural portal acquisition, survival or a 2,000 FPS result.
"""
import argparse,copy,datetime,gzip,hashlib,importlib.util,json,math,re,struct
from pathlib import Path


def require(value,why):
    if not value:raise AssertionError(why)


def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def artifact(p):
    p=Path(p)
    with p.open('rb') as stream:digest=hashlib.file_digest(stream,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=digest)


def check(ref):
    actual=artifact(ref['path']);require(actual['sha256']==ref['sha256'] and ('bytes' not in ref or actual['bytes']==ref['bytes']),'Changed real input/evidence: '+ref['path'])


def first_run_log_window(text, report):
    # Repeated complete runs can have identical players, dimensions and inventory.
    # Bind a rotated log to the actual first process rather than that payload alone.
    stamps=re.findall(r'^\[(\d{2}[A-Za-z]{3}\d{4} \d{2}:\d{2}:\d{2}\.\d{3})\]',text,re.M)
    if not stamps:return False
    first=datetime.datetime.strptime(stamps[0],'%d%b%Y %H:%M:%S.%f')
    last=datetime.datetime.strptime(stamps[-1],'%d%b%Y %H:%M:%S.%f')
    started=datetime.datetime.fromtimestamp(report['start']['started_at'])
    restarted=datetime.datetime.fromtimestamp(report['restart']['started_at'])
    return started-datetime.timedelta(seconds=1)<=first<restarted and first<=last<=restarted+datetime.timedelta(seconds=1)


def observations(r,dimensions,samples):
    require(r['passed'] and not r['synthetic'] and r['actualRequiredVulkan'],'Real accepted required-Vulkan multiplayer run required')
    require(r['finished']['cleaned_up'] and r['sourceJvmChoicesRestored'] and r['serverPropertiesRestored'] and r['originalProfileAndSourceWorldBytesUnchanged'] and r['dependencyLibrariesUnchanged'],'Incomplete cleanup/source preservation')
    require(r['audio']==dict(passed=True,prelaunchMuted=True,actualNativeMasterVolume=0,disposableSettingsOnly=True,soundCallbacksDisabled=False),'Actual native master zero required')
    require(r['inventorySavedAndReloaded'] and r['inventoryBeforeRestart']==r['inventoryAfterRestart'] and 'aoa3:blank_realmstone' in r['inventoryBeforeRestart'],'Complete observed native inventory must survive save/restart/rejoin')
    require(r['start']['server_id']==r['restart']['server_id']==r['server']['id'] and r['start']['running_id']!=r['restart']['running_id'],'Two real owned dedicated processes required')
    require(r['firstServerExit']['exit_code']==r['finalServerExit']['exit_code']==0,'Both dedicated processes must exit cleanly')
    require(r['firstConnection']['player']==r['secondConnection']['player']==r['player'],'Different player rejoined')
    for connection in [r['firstConnection'],r['secondConnection']]:
        command=connection['command'];require(command['status']=='passed' and command['matched'] and command['command']=='connect 127.0.0.1 '+str(r['loopbackPort']) and 'Connecting to server' in command['assertion_evidence'],'Fresh actual loopback command evidence required')
    require(r['expectedDimensions']==dimensions and len(dimensions)>=26 and r['completeRemoteDimensionCount']==len(dimensions),'Complete current native dimension domain required')
    seen=set()
    for row in r['dimensionVisits']:
        key=row['dimension'];require(key in dimensions and key not in seen,'Duplicate/foreign dimension');seen.add(key);sample=row['telemetry'];require(sample in samples,'Observation absent from complete final native telemetry')
        require(sample['dimension']==key and len(sample['position'])==3 and all(math.isfinite(v) for v in sample['position']) and sample['screen'] is None,'Actual unobscured native world/player context required')
        require(row['at']<sample['at']<r['secondConnection']['at'] and sample['at']>=r['firstConnection']['at'],'Stale or wrong-process travel observation')
        require(sample['frame_ms'] and all(math.isfinite(v) and v>0 for v in sample['frame_ms']),'Actual rendered intervals required')
        require(row['screenshot']['at']>=sample['at'] and row['screenshot'] in r['finished']['artifacts'],'Native screenshot must follow its actual world observation')
    require(seen==set(dimensions),'A declared dimension was not exercised')
    require(not r['performanceVerified'] and not r['multiplayerSurvivalVerified'] and not r['completeAoAPort'],'Transport smoke test must not invent complete gameplay/performance acceptance')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['report','plan','output']:ap.add_argument(name)
    a=ap.parse_args();r,plan=read(a.report),read(a.plan);out=Path(a.output);require(not out.exists(),'Keep previous verification')
    check(r['qaSource']);check(r['preparation']);check(r['canonicalProduct']);check(r['fixture']);prep=read(r['preparation']['path']);installation=read(prep['installation']['path']);check(prep['installation']);check(installation['nativeServer']);native=read(installation['nativeServer']['path'])
    require(native['passed'] and native['nativeServerAdmissionVerified'] and native['build']['artifacts'][0]['sha256']==r['canonicalProduct']['sha256']==installation['identity']['artifact'],'Exact current complete native product required')
    whole_path=Path(native['build']['build_root'])/'run/enderloom-forge1201-whole-world-generation.json';whole=read(whole_path);require(whole['complete'] and not whole['synthetic'] and not whole['errors'],'Complete native dimension authority required');dimensions=sorted({row['dimension'] for row in whole['completedChunks']})
    if plan.get('expectedDimensions'):
        check(plan['priorNativeServer']);require(r['priorNativeServer']==plan['priorNativeServer'],'Different previous accepted native authority');check(r['priorDimensionAuthority']);prior=read(plan['priorNativeServer']['path']);require(prior['passed'] and prior['nativeServerAdmissionVerified'],'Accepted previous native server required')
        prior_path=Path(prior['build']['build_root'])/'run/enderloom-forge1201-whole-world-generation.json';require(artifact(prior_path)==r['priorDimensionAuthority'],'Different previous full native world capture');prior_whole=read(prior_path);require(prior_whole['complete'] and not prior_whole['synthetic'] and not prior_whole['errors'],'Complete previous world capture required')
        previous=sorted({row['dimension'] for row in prior_whole['completedChunks']});require(len(previous)>=26 and set(previous)<=set(dimensions) and previous==r['priorDimensions'],'A previous accepted world was lost');require(dimensions==plan['expectedDimensions'] and sorted(set(dimensions)-set(previous))==plan['addedDimensions']==r['addedDimensions'],'Unreviewed world-domain change')
    else:require(len(dimensions)==26,'Legacy acceptance retains its exact dimension domain')
    root=Path(r['finished']['report_dir']);telemetry=root/'telemetry.jsonl';samples=[json.loads(s) for s in telemetry.read_text(encoding='utf-8').splitlines() if s];observations(r,dimensions,samples)
    require(read(root/'report.json')==r['finished'],'Final native report differs from returned evidence')
    for ref in r['originalProfile']:check(ref)
    fixture=read(r['fixture']['path']);require(fixture['passed'] and fixture['audioGuard'],'Muted owned fixture required')
    for ref in [fixture['artifact'],fixture['source'],fixture['mapping'],fixture['audioGuardSource']]:check(ref)
    require(read(plan['fixtureOutput'])==r['remoteOverlay'] and read(plan['fixtureOutput']+'.audio.json')==r['audio'],'Actual remote native fixture files differ')
    helper=Path(__file__).with_name('conversion-hari-overlay-native-verify.py');spec=importlib.util.spec_from_file_location('mp_gui_cases',helper);gui=importlib.util.module_from_spec(spec);spec.loader.exec_module(gui);require(gui.cases(r['remoteOverlay'],'Hari Vulkan')==24 and r['remoteOverlay']['physicalGlCalls']==0,'All 24 remote actual GUI draws required')
    images=[]
    for row in r['dimensionVisits']:
        ref=row['screenshot'];check(ref);raw=Path(ref['path']).read_bytes();require(raw[:8]==b'\x89PNG\r\n\x1a\n' and raw[12:16]==b'IHDR','Actual native PNG required');width,height=struct.unpack('>II',raw[16:24]);require(width>0 and height>0,'Empty framebuffer');images.append(dict(dimension=row['dimension'],image=artifact(ref['path']),width=width,height=height))
    logs='\n'.join((root/name).read_text(encoding='utf-8') for name in ['console.log','latest.log']);require('[Hari/Vulkan] renderer=VULKAN' in logs and 'renderer=OPENGL_FALLBACK' not in logs,'Different actual renderer')
    require(not re.search('MixinApplyError|InvalidInjectionException|InjectionError|NoSuchMethodError|NoSuchFieldError|NoClassDefFoundError|Unidentified mapping|missing registry entries|Failed to initialize Vulkan',logs),'Actual fatal integration failure')
    seed=read(prep['productionServer']);require(seed['passed'] and seed['server']['id']==r['server']['id'],'Different production runtime reused')
    for ref in seed['dependencyLibraries']+seed['originalWorldFiles']:check(ref)
    stage=read(prep['seedStage']['path']);check(prep['seedStage'])
    for ref in stage['sourceFiles']+stage['importedFiles']:check(ref)
    require(artifact(Path(r['server']['dir'])/'server.properties')['sha256']==seed['originalPropertiesSha256'],'Original complete server property bytes not restored')
    # Bind the before-restart inventory to the first real server's rotated log,
    # then freeze that exact raw log rather than pinning a mutable rotation name.
    first_logs=[]
    for path in (Path(r['server']['dir'])/'logs').glob('*.log.gz'):
        if path.name.startswith('debug'):continue
        raw=gzip.decompress(path.read_bytes());text=raw.decode('utf-8');
        if first_run_log_window(text,r) and r['inventoryBeforeRestart'] in text and text.count('Teleported '+r['player'])==len(dimensions)+1 and text.count(r['player']+' joined the game')==1:first_logs.append((path,raw))
    require(len(first_logs)==1,'One complete first dedicated-run log must bind every dimension transfer, return and native inventory')
    first_path,first_raw=first_logs[0];first_frozen=Path(str(out)+'.first-dedicated.log');first_frozen.write_bytes(first_raw)
    for offset in [-86400,86400]:
        stale=copy.deepcopy(r);stale['start']['started_at']+=offset;stale['restart']['started_at']+=offset
        require(not first_run_log_window(first_raw.decode('utf-8'),stale),'A different native process time window was admitted')
    last=Path(r['serverConsole']);text=last.read_text(encoding='utf-8');require(r['inventoryAfterRestart'] in text and r['player']+' joined the game' in text and 'Saving' in text,'Final native join/inventory/save log missing')
    faults=[]
    for label in ['lost-dimension','duplicate-dimension','stale-native-telemetry','wrong-renderer','unmuted','lost-inventory']:
        bad=copy.deepcopy(r)
        if label=='lost-dimension':bad['dimensionVisits'].pop()
        elif label=='duplicate-dimension':bad['dimensionVisits'][-1]=bad['dimensionVisits'][0]
        elif label=='stale-native-telemetry':bad['dimensionVisits'][0]['telemetry']['at']=0
        elif label=='wrong-renderer':bad['actualRequiredVulkan']=False
        elif label=='unmuted':bad['audio']['actualNativeMasterVolume']=1
        else:bad['inventoryAfterRestart']='[]'
        try:observations(bad,dimensions,samples);raise RuntimeError('Generated control accepted: '+label)
        except AssertionError:faults.append(dict(fault=label,generated=True,rejected=True))
    frozen=Path(str(out)+'.verifier.py');frozen.write_bytes(Path(__file__).read_bytes())
    result=dict(passed=True,synthetic=False,report=artifact(a.report),plan=artifact(a.plan),canonicalProduct=r['canonicalProduct'],nativeServer=installation['nativeServer'],nativeDimensionAuthority=artifact(whole_path),nativeReport=artifact(root/'report.json'),nativeTelemetry=artifact(telemetry),firstDedicatedLog=artifact(first_frozen),lastDedicatedLog=artifact(last),actualRemoteDimensions=len(dimensions),completeDimensionSkyFogCaptures=images,actualRemoteGuiDraws=24,nativeMasterVolume=0,observedInventoryPreservedAcrossDedicatedRestart=True,sourceWorldsAndProfileBytesUnchanged=True,dependencyLibrariesUnchanged=True,originalServerPropertyBytesRestored=True,temporaryClientRemoved=True,generatedFaults=faults,verifier=artifact(frozen),guiVerifier=artifact(helper),fullTerrainRasterParityVerified=False,naturalPortalAcquisitionVerified=False,multiplayerSurvivalVerified=False,performanceVerified=False,completeAoAPort=False)
    with out.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2)
    print(json.dumps(dict(passed=True,actualRemoteDimensions=len(dimensions),actualRemoteGuiDraws=24,inventoryRestartVerified=True,generatedFaults=len(faults),output=str(out))))


if __name__=='__main__':main()
