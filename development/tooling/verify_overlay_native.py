"""Independently bind the complete mod, two native backends and exact state cases.

This bounded renderer acceptance never certifies the full AoA union, all renderer
features, existing-save migration, a complete modpack or the 2,000 FPS objective.
"""
import argparse,copy,hashlib,json
from pathlib import Path
import zipfile

def require(value,message):
    if not value:raise ValueError(message)
def artifact(path):
    path=Path(path).resolve();raw=path.read_bytes();return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def check(ref):
    actual=artifact(ref['path']);require(actual['sha256']==ref['sha256'] and actual['bytes']==ref['bytes'],'Changed exact artifact: '+ref['path'])
def equivalent(a,b):
    check(a);check(b)
    with zipfile.ZipFile(a['path']) as left,zipfile.ZipFile(b['path']) as right:
        first,second=left.namelist(),right.namelist();require(len(first)==len(set(first)) and len(second)==len(set(second)) and set(first)==set(second),'Complete native archive membership differs')
        changed=[]
        for name in first:
            x,y=left.read(name),right.read(name)
            if x!=y:
                require(name=='META-INF/MANIFEST.MF','Program/resource bytes differ between native cohorts: '+name)
                normalize=lambda raw:[line for line in raw.decode('utf-8').splitlines() if not line.startswith('Implementation-Timestamp: ')]
                require(normalize(x)==normalize(y),'Non-timestamp native manifest difference');changed.append(name)
        return dict(members=len(first),differentMembers=changed,completeProgramAndResourceBytesEqual=True)
def cases(value,backend):
    require(value['passed'] and not value['synthetic'] and value['generatedFixture'] and value['backend']==backend and value['allStateRestored'],'Actual native renderer fixture failed')
    require(value['performanceVerified'] is False and value['completeAoAPort'] is False,'Bounded state test cannot certify performance/full merge')
    rows=value['completeDraws'];require(len(rows)==24,'Incomplete native overlay state cohort')
    combinations={(r['flags'],r['blendCase']) for r in rows};require(combinations=={(a,b) for a in range(8) for b in range(3)},'Missing/duplicate native renderer combinations')
    factors=[[770,771,1,0],[1,0,0,1],[32769,32770,32771,32772]]
    for row in rows:
        flags=row['flags'];require(row['actualState']==[flags&1,(flags>>1)&1,(flags>>2)&1,*factors[row['blendCase']]],'Native state differs from exact case preconditions')
        require(row.get('completeDraw',row.get('completeOverlayDraw')) is True,'Native complete overlay draw missing')
    return len(rows)
def run(server_file,client_file,hari_file,hari_capture_file,previous_file,output):
    output=Path(output);require(not output.exists(),'Preserve accepted/failed evidence; select a fresh output')
    server,client,hari,previous=map(read,[server_file,client_file,hari_file,previous_file])
    require(server['passed'] and server['nativeServerAdmissionVerified'] and client['passed'] and client['nativeClientAdmissionVerified'],'Complete accepted native server/client required')
    require(server['allPrimaryChoicesAndAuthoritiesUnchanged'] and client['allPrimaryChoicesAndAuthoritiesUnchanged'],'Native source choices changed')
    canonical=server['build']['artifacts'][0];client_equivalence=equivalent(canonical,client['build']['artifacts'][0])
    require(hari['passed'] and hari['nativeVulkanVerified'] and hari['nativeRendererSelected'] and not hari['physicalFallbackPresent'] and not hari['forbiddenFailures'],'Native-required production Hari run did not pass')
    require(hari['finished']['cleaned_up'] and hari['jvmChoicesRestored'] and hari['horizontalDistance']>0.1 and hari['observedRenderIntervals']>0,'Native production run lacks movement/render/clean restoration')
    hari_equivalence=equivalent(canonical,hari['inputs'][0]);check(hari['inputs'][1]);check(hari['fixture']['artifact']);check(hari['fixture']['source']);check(hari['fixture']['mapping'])
    require(artifact(hari['qaSource']['path'])['sha256']==hari['qaSource']['sha256'],'Changed actual native production runner')
    capture=read(hari_capture_file);require(capture==hari['activeOverlayFixture'],'Native fixture and production admission differ')
    require(capture['physicalGlCalls']==0 and capture['fixtureBoundary']=='Actual Forge GUI overlay Post inside the native render pass','Native GUI boundary absent')
    native_count=cases(capture,'Hari Vulkan')
    gl_path=Path(client['build']['build_root'])/'run/enderloom-forge1201-overlay-render-state.json';gl_raw=gl_path.read_text(encoding='utf-8');gl=read(gl_path)
    gl_count=cases(gl,'OpenGL');stdout=Path(client['build']['stdout_path']).read_text(encoding='utf-8');require(stdout.count('ENDERLOOM_FORGE1201_OVERLAY_RENDER_STATE '+gl_raw)==1,'Native GL capture lacks its exact runtime log marker')
    old=previous['files'][0];check(old);old_names,new_names,changed,added=[],[],[],[]
    with zipfile.ZipFile(old['path']) as before,zipfile.ZipFile(canonical['path']) as after:
        old_names=before.namelist();new_names=after.namelist();require(len(old_names)==len(set(old_names)) and len(new_names)==len(set(new_names)),'Duplicate archive ownership')
        require(not set(old_names)-set(new_names),'Inherited mod member was removed')
        added=sorted(set(new_names)-set(old_names));require(added==['net/tslat/aoa3/client/gui/overlay/OverlayRenderState$Query.class','net/tslat/aoa3/client/gui/overlay/OverlayRenderState$Selected.class','net/tslat/aoa3/client/gui/overlay/OverlayRenderState.class'],'Unreviewed added mod member')
        changed=[n for n in old_names if before.read(n)!=after.read(n)]
        require(set(changed)=={'META-INF/MANIFEST.MF','net/tslat/aoa3/client/gui/overlay/ScreenOverlayRenderer.class'},'Unreviewed inherited program/resource change')
    controls=[]
    for label,mutate in [('missing case',lambda v:v['completeDraws'].pop()),('wrong backend',lambda v:v.update(backend='OpenGL')),('lost restoration',lambda v:v.update(allStateRestored=False)),('wrong separate blend',lambda v:v['completeDraws'][0]['actualState'].__setitem__(3,0)),('duplicate case',lambda v:v['completeDraws'].__setitem__(0,copy.deepcopy(v['completeDraws'][1])))]:
        bad=copy.deepcopy(capture);mutate(bad)
        try:cases(bad,'Hari Vulkan')
        except ValueError:controls.append(dict(label=label,generated=True,rejected=True))
        else:raise ValueError('Generated native state corruption accepted: '+label)
    frozen=output.with_suffix('.producer.py');frozen.write_bytes(Path(__file__).read_bytes())
    report=dict(schema=1,passed=True,synthetic=False,completeAoAPort=False,performanceVerified=False,fpsGoal=2000,
                canonicalMod=canonical,completePreviousMembersRetained=len(old_names),currentMembers=len(new_names),addedMembers=added,changedMembers=changed,
                server=artifact(server_file),client=artifact(client_file),nativeGlCapture=artifact(gl_path),nativeHari=artifact(hari_file),nativeHariCapture=artifact(hari_capture_file),renderer=hari['inputs'][1],
                actualOpenGlDraws=gl_count,actualVulkanDraws=native_count,clientServerEquivalence=client_equivalence,hariProductionEquivalence=hari_equivalence,
                verifier=artifact(frozen),generatedFaultControls=controls,
                qualifications=['The Hari state fixture uses a disposable development seed containing 31 GeckoLib/SmartBrainLib example registry entries absent in production; this does not certify save migration or clean production-world parity.',
                                'Actual native GUI draws/state restoration are verified; pixel-level raster parity, representative full content, full-pack support, sustained FPS and the complete historical/latest union remain open.'])
    with output.open('x',encoding='utf-8') as file:json.dump(report,file,indent=2)
    print(json.dumps({k:report[k] for k in ['passed','completePreviousMembersRetained','currentMembers','actualOpenGlDraws','actualVulkanDraws','performanceVerified','completeAoAPort']}))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('server');p.add_argument('client');p.add_argument('hari');p.add_argument('hari_capture');p.add_argument('previous');p.add_argument('--output',required=True);a=p.parse_args();run(a.server,a.client,a.hari,a.hari_capture,a.previous,a.output)
