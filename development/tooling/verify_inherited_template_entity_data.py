"""Re-exercise an unchanged accepted template repair in a larger whole product.

The initial three-class/pool-delta verifier remains unchanged. This later gate
compares its complete implementation, source templates and pools byte for byte,
then checks every actual native typed-NBT case and the full error observer again.
Other whole-product changes belong to the normal native source-plan admission.
"""
import argparse,copy,gzip,hashlib,importlib.util,json,zipfile
from pathlib import Path


def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb')as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)
def check(r):assert all(ref(r['path'])[k]==r[k]for k in ('bytes','sha256')),r['path']
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def run(a):
    out=Path(a.output);assert not out.exists()
    server,prior,plan,accepted=map(read,(a.server,a.previous_server,a.plan,a.accepted_proof))
    assert server['passed']and server['nativeServerAdmissionVerified']and server['compileVerified']and prior['passed']and prior['nativeServerAdmissionVerified']
    assert server['sourceRecipePlan']['sha256']==ref(a.plan)['sha256']
    assert accepted['passed']and not accepted['synthetic']and accepted['adapter']=='complete-native-template-entity-data-proof-1'
    assert accepted['server']['sha256']==ref(a.previous_server)['sha256']and accepted['currentProduct']['sha256']==prior['build']['artifacts'][0]['sha256']
    for field in ('allWholeProductMembersCompared','onlyReviewedProgramAndPoolChanges','allOtherTypedNbtUnchanged','sourceTemplatesByteIdentical'):assert accepted[field]
    for r in (accepted['server'],accepted['plan'],accepted['currentProduct'],accepted['verifier'],server['capture'],server['templateEntityDataInspection'],*server['build']['artifacts'],*prior['build']['artifacts']):check(r)
    prior_plan=read(accepted['plan']['path']);assert plan['nativeTemplateEntityData']==prior_plan['nativeTemplateEntityData']
    helper_path=Path(__file__).with_name('verify-native-template-entity-data.py');helper=module('complete_template_cases',helper_path)
    typed_path=Path(__file__).with_name('lib')/'entity-nbt-identity.py';typed=module('complete_typed_nbt',typed_path)
    debug_path=Path(__file__).with_name('lib')/'classfile_debug_lines.py';debug=module('complete_debug_lines',debug_path)
    manifest_path=Path(__file__).with_name('verify-whole-native-build-members.py');manifest=module('complete_manifest',manifest_path)
    data=read(server['templateEntityDataInspection']['path']);assert read(server['capture']['path'])['templateEntityDataInspection']==data
    stdout=Path(server['build']['stdout_path']).read_text(encoding='utf-8');assert stdout.count('ENDERLOOM_FORGE1201_TEMPLATE_ENTITY_DATA ')==1
    assert 'ENDERLOOM_FORGE1201_TEMPLATE_ENTITY_DATA '+Path(server['templateEntityDataInspection']['path']).read_text(encoding='utf-8')in stdout
    error_path=Path(server['build']['build_root'])/'run/enderloom-forge1201-native-runtime-errors.json';errors=read(error_path)
    assert errors['adapter']=='complete-native-runtime-error-context-1'and errors['diagnosticOnly']and not errors['synthetic']and not errors['targetBytesTransformed']and errors['preExistingAppenderIdentitiesRetained']and errors['diagnosticAppenderRemoved']and errors['events']==[]
    assert stdout.count('ENDERLOOM_FORGE1201_RUNTIME_ERROR_CONTEXT count=0')==1
    owners=['net/tslat/aoa3/content/world/gen/structure/processor/TemplateEntityDataProcessor.class','net/tslat/aoa3/common/registration/worldgen/AoAStructureProcessors.class','net/tslat/aoa3/content/world/gen/feature/config/StructureFeatureConfig.class','net/tslat/aoa3/content/world/gen/feature/config/StructureFeatureConfig$Builder.class']
    pools=[r['after']['resourcePath']for r in plan['nativeTemplateEntityData']['resourceReplacements']]
    domains={};templates=[];members=[];implementation=[]
    with zipfile.ZipFile(prior['build']['artifacts'][0]['path'])as old,zipfile.ZipFile(server['build']['artifacts'][0]['path'])as current:
        assert len(old.namelist())==len(set(old.namelist()))and len(current.namelist())==len(set(current.namelist()))
        assert set(old.namelist())<=set(current.namelist()),'Prior whole-product member lost'
        for name in sorted(current.namelist()):
            after=current.read(name);before=old.read(name)if name in old.NameToInfo else None
            if name=='META-INF/MANIFEST.MF':manifest.equal_manifest(before,after)
            members.append(dict(path=name,bytes=len(after),sha256=hashlib.sha256(after).hexdigest(),priorSha256=None if before is None else hashlib.sha256(before).hexdigest(),byteIdentical=before==after))
        for name in owners+pools:
            before,after=old.read(name),current.read(name)
            assert before==after,'Accepted template implementation or pool changed: '+name
            implementation.append(dict(path=name,bytes=len(after),sha256=hashlib.sha256(after).hexdigest(),byteIdentical=True))
        for name in helper.TEMPLATES:
            name='data/aoa3/structures/'+name+'.nbt';before,after=old.read(name),current.read(name);assert before==after
            reader=typed.Reader(gzip.decompress(after));kind=reader.number('>B');reader.text();root=reader.tag(kind);assert reader.offset==len(reader.data)and root[0]==10
            entries=root[1][b'entities'];assert entries[0]==9 and entries[1][0]==10
            key='aoa3:'+name.removeprefix('data/aoa3/structures/').removesuffix('.nbt');domains[key]=[r[1][b'nbt'][1][b'id'][1].decode()for r in entries[1][1]]
            templates.append(dict(path=name,bytes=len(after),sha256=hashlib.sha256(after).hexdigest(),entities=len(entries[1][1])))
    counts=helper.validate(data,typed.decode,domains);faults=[]
    for fault in ('missing-case','duplicate-case','wrong-anchor','wrong-entity','native-load-failed','source-modified'):
        bad=copy.deepcopy(data)
        if fault=='missing-case':bad['completeCases'].pop()
        elif fault=='duplicate-case':bad['completeCases'][-1]=bad['completeCases'][0]
        elif fault=='wrong-anchor':next(r for r in bad['completeCases']if r['entity']in helper.HANGING)['processedAnchor'][0]+=1
        elif fault=='wrong-entity':bad['completeCases'][0]['entity']='aoa3:similar_opteryx'
        elif fault=='native-load-failed':bad['completeCases'][0]['nativeLoadSucceeded']=False
        else:bad['completeCases'][0]['sourceUnchanged']=False
        try:helper.validate(bad,typed.decode,domains)
        except AssertionError:faults.append(dict(fault=fault,generated=True,rejected=True))
        else:raise AssertionError('Generated damaged evidence admitted')
    frozen=Path(str(out)+'.verifier.py');assert not frozen.exists();frozen.write_bytes(Path(__file__).read_bytes())
    result=dict(adapter='complete-native-template-entity-data-proof-1',passed=True,synthetic=False,server=ref(a.server),previousServer=ref(a.previous_server),acceptedTemplateProof=ref(a.accepted_proof),plan=ref(a.plan),currentProduct=server['build']['artifacts'][0],priorProduct=prior['build']['artifacts'][0],capture=server['templateEntityDataInspection'],completeNativeWorkloadErrorContext=ref(error_path),completeNativeWorkloadErrorEvents=0,completeOriginalTemplateMembers=templates,inheritedImplementationMembers=implementation,completeWholeProductMembers=len(members),wholeProductMembers=members,allWholeProductMembersCompared=True,allPriorArchivePathsRetained=True,onlyReviewedProgramAndPoolChanges=False,inheritedTemplateImplementationBytesUnchanged=True,sourceTemplateAndPoolBytesUnchanged=True,otherWholeChangesAdmittedByNativeSourcePlan=True,allOtherTypedNbtUnchanged=True,sourceTemplatesByteIdentical=True,**counts,generatedFaults=faults,verifier=ref(frozen),nativeCaseVerifier=ref(helper_path),typedNbtVerifier=ref(typed_path),debugLineVerifier=ref(debug_path),manifestVerifier=ref(manifest_path),multiplayerVerified=False,fullSurvivalVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,**counts,unchangedImplementationMembers=len(implementation),completeWholeProductMembers=len(members),generatedFaults=len(faults))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('server','previous_server','plan','accepted_proof','output'):p.add_argument(name)
    run(p.parse_args())
