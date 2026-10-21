"""Compose the complete original 19-offer family with the current Realmshifter.

This preserves the entire newer trader, every existing offer and saved state.
Source composition and target compilation are separate from gameplay acceptance.
"""
import argparse, importlib.util, json, re, zipfile
from pathlib import Path


def load_module(name, file):
    spec=importlib.util.spec_from_file_location(name,file)
    value=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def run(previous, recovery_file, server_file, output):
    here=Path(__file__).resolve().parent
    base=load_module('buyback_base',here/'conversion-functional-world-event-family-plan.py')
    edit=load_module('buyback_editor',here/'lib/source_recipe_editor_append.py')
    read=lambda p:json.loads(Path(p).read_text(encoding='utf-8'))
    plan,recovery,server=map(read,(previous,recovery_file,server_file))
    assert recovery['passed'] and server['passed'] and server['nativeServerAdmissionVerified']
    plan_ref=base.artifact(previous)
    assert Path(server['sourceRecipePlan']['path']).samefile(previous)
    assert all(server['sourceRecipePlan'][k]==plan_ref[k] for k in ['bytes','sha256'])
    original=recovery['original']
    assert base.artifact(original['path'])==original
    source=next(r for r in recovery['completeSelectedSourceCandidates'] if Path(r['path']).name=='EntityRealmShifter.java')
    assert base.artifact(source['path'])==source
    text=Path(source['path']).read_text(encoding='utf-8')
    entries=re.findall(r'new RestockedRecipe\(new ItemStack\(Itemizer\.(Realmstone\w+), 1, 1\), new ItemStack\(Itemizer\.(SilverCoin|CopperCoin), (\d+)\)\)',text)
    assert len(entries)==19 and text.count('new RestockedRecipe(')==19
    names={'Abyss':'abyss','AncientCavern':'ancient_cavern','Barathos':'barathos','Borean':'lborean','Celeve':'celeve','Crystevia':'crystevia','Deeplands':'deeplands','Dustopia':'dustopia','Gardencia':'gardencia','Haven':'haven','Iromine':'iromine','Lelyetia':'lelyetia','Mysterium':'mysterium','Precasia':'precasia','VoxPonds':'vox_ponds','Candyland':'candyland','Creeponia':'creeponia','Immortallis':'immortallis','Shyrelands':'shyrelands'}
    native=read(server['capture']['path'])
    keys=set(next(r for r in native['rootRegistries']if r['name']=='minecraft:item')['allKeys'])
    table=[]
    for old,currency,amount in entries:
        stone=names[old.removeprefix('Realmstone')]
        coin='silver_coin' if currency=='SilverCoin' else 'copper_coin'
        assert 'aoa3:'+stone+'_realmstone' in keys and 'aoa3:'+coin in keys
        table.append(dict(originalStone='Itemizer.'+old,targetStone='aoa3:'+stone+'_realmstone',originalCurrency='Itemizer.'+currency,targetCurrency='aoa3:'+coin,stoneCount=1,amount=int(amount),direction='stone-for-currency'))
    helper=here/'java/RealmstoneBuybacks.java'
    body=helper.read_text(encoding='utf-8')
    literals=re.findall(r'new Buyback\("([a-z_]+)","([a-z_]+)",(\d+)\)',body)
    assert [('aoa3:'+s+'_realmstone','aoa3:'+c,int(n))for s,c,n in literals]==[(r['targetStone'],r['targetCurrency'],r['amount'])for r in table]
    target='src/main/java/net/tslat/aoa3/content/entity/mob/historical/restored/RealmstoneBuybacks.java'
    merchant=target.replace('RealmstoneBuybacks.java','RealmshifterEntity.java')
    preceding=next(r for r in plan['sourceTransformations']if r['path']==merchant)
    assert isinstance(preceding.get('content'),str) and not preceding.get('edits')
    fragment='''\n    @Override public net.minecraft.world.item.trading.MerchantOffers getOffers() {
        var offers=super.getOffers();
        if(!level().isClientSide)RealmstoneBuybacks.ensure(offers);
        return offers;
    }
'''
    assert 'MerchantOffers getOffers()' not in preceding['content']
    out=Path(output)
    assert not out.exists()
    owner=out.with_suffix('.producer')
    owner.mkdir()
    donor_file=owner/'complete-realmshifter-buybacks.zip'
    with zipfile.ZipFile(donor_file,'x',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
        z.writestr(target,body.encode('utf-8'))
        z.writestr('realmshifter-offer-extension.fragment',fragment.encode('utf-8'))
        z.writestr('complete-original-to-canonical-buybacks.json',json.dumps(table,indent=2).encode('utf-8'))
    donor=base.artifact(donor_file)
    own=lambda n,b:base.proof(donor,n,b.encode('utf-8'))
    with zipfile.ZipFile(original['path'])as z:
        original_refs=[base.proof(original,n,z.read(n))for n in ['net/nevermine/npc/entity/EntityRealmShifter.class','net/nevermine/npc/entity/RestockedRecipe.class']]
    editor=edit.SourceRecipeEditor(plan,base)
    editor.add(target,body,[own(target,body),*original_refs],'Complete original 19 Realmshifter stone-for-currency offers without replacing newer trades')
    at=len(preceding['content'][:preceding['content'].rfind('}')].encode('utf-8'))
    editor.insert_content(merchant,at,fragment,[own('realmshifter-offer-extension.fragment',fragment),*original_refs],'Append only absent original buybacks while retaining every existing offer, price, uses and newer tier')
    editor.finish()
    producer=owner/Path(__file__).name
    producer.write_bytes(Path(__file__).read_bytes())
    frozen_helper=owner/'source_recipe_editor_append.py'
    frozen_helper.write_bytes(Path(edit.__file__).read_bytes())
    plan['sourceInputs'].append(dict(label='Complete original Realmshifter buybacks with preserved current trader',artifact=donor))
    plan['additionalAuthorities']+=[base.artifact(p)for p in [previous,recovery_file,server_file,producer,frozen_helper]]+[source,donor,server['capture']]
    plan['completeRealmshifterBuybacks']=dict(completeOriginalOffers=table,originalClassAuthorities=original_refs,sourceChanges=editor.changes,existingOffersAndSavedStateRetained=True,nativeRegistryDependenciesVerified=True,nativeGameplayVerified=False,completeAoAPort=False)
    out.write_text(json.dumps(plan,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(dict(planned=True,completeBuybacks=len(table),preservedNewerTrader=True,sourceRecipes=len(plan['sourceTransformations']),output=str(out),nativeGameplayVerified=False)))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['previous','recovery','server','output']:parser.add_argument(name)
    a=parser.parse_args()
    run(a.previous,a.recovery,a.server,a.output)
