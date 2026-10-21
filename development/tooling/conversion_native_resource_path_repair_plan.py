"""Repair target-native resource identifiers without changing original art bytes."""
import argparse, copy, importlib.util, json, re, zipfile
from pathlib import Path


def run(previous, failed_client, output):
    here=Path(__file__).resolve().parent
    spec=importlib.util.spec_from_file_location('resource_repair_base',here/'conversion-functional-world-event-family-plan.py')
    base=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    read=lambda p:json.loads(Path(p).read_text(encoding='utf-8'))
    plan,failure=map(read,(previous,failed_client))
    assert not failure['passed'] and failure['build']['state']=='client_verified'
    assert 'Native owned item/block model resources are absent' in failure['error']
    groups=[plan['resourceAdditions']]+[layer['resources']for layer in plan['resourceLayers']]
    selected={r['resourcePath']:(g,i,r)for g in groups for i,r in enumerate(g)}
    donors={r['sha256']:r for r in plan['additionalAuthorities']}
    donors.update({r['artifact']['sha256']:r['artifact']for r in plan['sourceInputs']})
    opened={}
    def member(row):
        donor=donors[row['donorSha256']]
        if donor['sha256'] not in opened:
            assert base.artifact(donor['path'])==donor
            opened[donor['sha256']]=zipfile.ZipFile(donor['path'])
        raw=opened[donor['sha256']].read(row['donorEntry'])
        assert base.sha(raw)==row['sha256']
        return raw
    renames={n:n.lower()for n in selected if n.startswith(('assets/','data/'))and n!=n.lower()}
    assert len(renames)==10 and all(n.startswith('assets/aoa3/textures/block/dungeons/')and n.endswith('.png')for n in renames)
    assert len(set(renames.values()))==len(renames) and not set(renames.values()).intersection(selected)
    references={'aoa3:'+old.removeprefix('assets/aoa3/textures/').removesuffix('.png'):'aoa3:'+new.removeprefix('assets/aoa3/textures/').removesuffix('.png')for old,new in renames.items()}
    repairs=[]
    for old,new in renames.items():
        group,index,row=selected[old]
        raw=member(row)
        updated=copy.deepcopy(row)
        updated['resourcePath']=new
        group[index]=updated
        repairs.append(dict(before=copy.deepcopy(row),after=copy.deepcopy(updated),bytes=len(raw),originalArtBytesUnchanged=True))
    changed={}
    def project(value):
        if isinstance(value,str):return references.get(value,value)
        if isinstance(value,list):return [project(v)for v in value]
        if isinstance(value,dict):return {k:project(v)for k,v in value.items()}
        return value
    for name,(_,_,row)in selected.items():
        if not name.startswith('assets/aoa3/models/')or not name.endswith('.json'):continue
        raw=member(row)
        data=json.loads(raw)
        after=project(data)
        if data!=after:changed[name]=(row,(json.dumps(after,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
    assert len(changed)==8
    eggs={f'assets/aoa3/models/item/{name}_spawn_egg.json':b'{"parent":"minecraft:item/template_spawn_egg"}\n'for name in ['coniferon','goldorth','horon','penumbra']}
    assert not set(eggs).intersection(selected)
    out=Path(output)
    assert not out.exists()
    owner=out.with_suffix('.producer')
    owner.mkdir()
    donor_file=owner/'complete-native-resource-path-repairs.zip'
    with zipfile.ZipFile(donor_file,'x',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
        for name,(_,raw)in changed.items():z.writestr(name,raw)
        for name,raw in eggs.items():z.writestr(name,raw)
        z.writestr('complete-original-art-path-projection.json',json.dumps(repairs,indent=2).encode('utf-8'))
    donor=base.artifact(donor_file)
    replacements=[]
    for name,(old,raw)in changed.items():
        group,index,_=selected[name]
        replacement={k:old[k]for k in ['donorSha256','donorEntry','sha256']}
        replacement['reason']='Exact modern ResourceLocation path projection; all other model geometry/material values retained'
        prior=old.get('replacement')
        if prior:replacement['history']=copy.deepcopy(prior.get('history',[]))+[{k:prior[k]for k in ['donorSha256','donorEntry','sha256','reason']}]
        row=dict(resourcePath=name,donorSha256=donor['sha256'],donorEntry=name,sha256=base.sha(raw),replacement=replacement)
        group[index]=row
        replacements.append(dict(before=copy.deepcopy(old),after=copy.deepcopy(row),onlyExactTextureLocationStringsChanged=True))
    plan['resourceLayers'].append(dict(id='complete-native-cavern-resource-path-repairs',title='Exact historical art through valid modern resource paths and all boss spawn eggs',resources=[dict(resourcePath=n,donorSha256=donor['sha256'],donorEntry=n,sha256=base.sha(raw))for n,raw in eggs.items()]))
    plan['sourceInputs'].append(dict(label='Exact target-native resource path corrections and complete boss egg models',artifact=donor))
    frozen=owner/Path(__file__).name
    frozen.write_bytes(Path(__file__).read_bytes())
    plan['additionalAuthorities']+=[base.artifact(p)for p in [previous,failed_client,frozen]]+[donor]
    plan['nativeResourcePathRepairs']=dict(retainedFailedClient=base.artifact(failed_client),completeArtPathRepairs=repairs,completeModelTextureReferenceRepairs=replacements,spawnEggModels=sorted(eggs),originalArtBytesUnchanged=True,registryIdentitiesUnchanged=True,nativeClientVerified=False,completeAoAPort=False)
    assert not any(r['resourcePath']!=r['resourcePath'].lower()for g in groups for r in g if r['resourcePath'].startswith(('assets/','data/')))
    for archive in opened.values():archive.close()
    out.write_text(json.dumps(plan,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(dict(planned=True,exactOriginalArtPathRepairs=len(repairs),completeModelReferenceRepairs=len(replacements),addedBossEggModels=len(eggs),originalArtBytesUnchanged=True,output=str(out))))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['previous','failed_client','output']:parser.add_argument(name)
    a=parser.parse_args()
    run(a.previous,a.failed_client,a.output)
