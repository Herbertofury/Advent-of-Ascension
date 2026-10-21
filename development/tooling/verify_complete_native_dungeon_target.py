"""Independently reconcile every target cell with the complete original program.

Read the raw original placement stream rather than the production chunk index.
Check approved field/metadata bindings, actual native states, all cage payloads,
real generated merchants, every progression case and original boss attributes.
Generated fault controls are explicitly separate from actual native evidence.
"""
import argparse,copy,hashlib,json,re,zipfile
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)
def check(r):assert all(ref(r['path'])[k]==r[k] for k in ('sha256','bytes')),r['path']
def origin(name):
    if '.immortallis.' in name:return (-15,17,-40)
    return {'ConiferonRoom':(-75,15,-75),'HoronRoom':(75,15,-75),'PenumbraRoom':(-75,15,75),'GoldorthRoom':(75,15,75)}.get(name.rsplit('.',1)[-1],(-20,15,-20))
def state(text):
    m=re.fullmatch(r'Block\{([a-z0-9_:/.-]+)\}(?:\[([^]]+)\])?',text);assert m,text
    props={} if m[2] is None else dict(part.split('=',1) for part in m[2].split(','));return m[1],props
def verify(native,trace,programs,palette,protected,original_worlds,bosses,access):
    assert native['passed'] and native['actualNativeServer'] and not native['syntheticWorld'] and native['generatedFixture'] and not native['fullSurvivalVerified'] and not native['completeAoAPort']
    expected={r:{} for r in ('ancient_cavern','immortallis')};writes=0
    for name,rows in programs.items():
        realm='immortallis' if '.immortallis.' in name else 'ancient_cavern';offset=origin(name)
        for x,y,z,field,meta,mode in rows:expected[realm][(x+offset[0],y+offset[1],z+offset[2])]=(field,meta);writes+=1
    assert writes==52438 and sum(map(len,expected.values()))==52416
    bindings={(r['realm'],r['originalField'],r['metadata']):r['native'] for r in palette};seen=set();protection=0;fluids=0
    for realm,x,y,z,binding,wanted,actual,guard in trace:
        point=(x,y,z);identity=(realm,point);assert identity not in seen;seen.add(identity);field,meta=expected[realm][point];assert binding==field+'#'+str(meta)
        approved=bindings[(realm,field,meta)];key,props=state(actual);assert key==approved['Name'];wkey,wprops=state(wanted);assert key==wkey
        for name,value in approved.get('Properties',{}).items():
            if key=='minecraft:lava' and name=='level':assert 0<=int(props[name])<=15
            else:assert props[name]==value
        if actual!=wanted:assert key=='minecraft:lava' and all(v==props[k] for k,v in wprops.items() if k!='level');fluids+=1
        correct=field in protected[realm];assert guard==correct;protection+=int(guard)
    assert seen=={(realm,p) for realm,points in expected.items() for p in points}
    assert native['completeCells']==len(seen) and native['protectedCells']==protection==50542 and not native['nativePlacementFailures']
    worlds={r['realm']:r for r in native['worlds']};assert set(worlds)==set(expected)
    original={r['realm']:r for r in original_worlds['initial']};assert original_worlds['passed'] and original_worlds['originalRuntime'] and not original_worlds['syntheticWorld']
    mobs={'Automaton':'automaton','Bloodsucker':'bloodsucker','RockCritter':'rock_critter','Fenix':'fenix','FlowerFace':'flowerface','Ghastus':'ghastus','Goldum':'goldum','Goldus':'goldus','Reaver':'reaver','Shavo':'shavo','Skeledon':'skeledon','Skelekyte':'skelekyte','Urioh':'urioh','Urv':'urv','Visage':'visage'};cages=0
    for realm,world in worlds.items():
        assert world['completeCells']==len(expected[realm]);before={tuple(t['position']):t for t in original[realm]['completeBlockEntities']};after={tuple(t['position']):t for t in world['nativeCages']};assert set(before)==set(after) and len(after)==(8 if realm=='ancient_cavern' else 32)
        for point,tile in after.items():
            legacy=re.search(r'EntityId:"nevermine\.([A-Za-z]+)"',before[point]['completeNativeNbt']);assert legacy;entity=mobs[legacy[1]];assert tile['entity']==entity and 'id:"aoa3:'+entity+'"' in tile['completeNbt'] and 'custom_spawn_rules' in tile['completeNbt']
            for key,value in dict(Delay=20,MinSpawnDelay=200,MaxSpawnDelay=800,SpawnCount=4,MaxNearbyEntities=6,RequiredPlayerRange=16,SpawnRange=4).items():assert re.search(r'\b'+key+':'+str(value)+r's\b',tile['completeNbt'])
        actors=world['observedLoadedActorsBeforeFixture'];assert sorted(a['id'] for a in actors)==([] if realm=='ancient_cavern' else ['aoa3:dungeon_keeper','aoa3:token_collector']);cages+=len(after)
    assert cages==native['completeCages']==40
    assert sorted((r['id'],r['saveReloadOffers']) for r in native['merchantOffers'])==[('dungeon_keeper',11),('token_collector',15)]
    positions=[(28,20,2),(67,21,2),(81,21,2),(122,21,2),(141,24,2),(168,24,7),(189,20,2),(233,21,3),(0,20,0)];stages=native['completeProgressionCases'];assert len(stages)==12
    for stage,row in enumerate(stages[:9],1):assert row['stage']==stage and row['missingPrerequisiteRejected'] and tuple(row['actualDestination'])==positions[stage-1]
    assert stages[9]['fullInventoryExactRollback']
    for pure,row in zip((False,True),stages[10:]):assert row['pure']==pure and row['actualAward']==20 and row['fullCapConsumesNothing']
    keys={'generic.maxHealth':'MAX_HEALTH','generic.attackDamage':'ATTACK_DAMAGE','generic.followRange':'FOLLOW_RANGE','generic.knockbackResistance':'KNOCKBACK_RESISTANCE','generic.movementSpeed':'MOVEMENT_SPEED'}
    original_traits={r['class'].rsplit('.Entity',1)[1].lower():r for r in bosses['completeBossTraits']+bosses['completeSummonTraits']+access['completeCreatureTraits']};actual_traits={r['id']:r for r in native['completeBossTraits']+native['completeAccessTraits']}
    assert set(actual_traits)=={'coniferon','goldorth','horon','penumbra','hellspot','automaton','death_hunter'}
    for name,row in actual_traits.items():
        original_name='deathhunter' if name=='death_hunter' else name;old={keys[a['name']]:a['actual'] for a in original_traits[original_name]['attributes'] if a['present']};assert {a['attribute']:a['actual'] for a in row['attributes']}==old
    assert [r['colour'] for r in actual_traits['automaton']['completeColourSaveCases']]==[1,2,3,4,5] and all(r['nativeSaveReload'] for r in actual_traits['automaton']['completeColourSaveCases'])
    assert {(r['item'],r['exactNativePortal']) for r in native['realmstoneBindings']}=={(r+'_realmstone',r+'_portal') for r in ('ancient_cavern','immortallis')}
    return dict(completeOriginalWrites=writes,completeNativeCells=len(seen),completeCages=cages,completeMerchantOffers=26,completeProgressionCases=12,completeOriginalCreatureAttributes=35,completeNativeColourSaves=5,protectedNativeCells=protection,observedFluidCallbackDifferences=fluids)
def run(plan_file,capture_file,program_file,world_file,boss_file,access_file,output):
    plan,native,programs,world,boss,access=map(read,(plan_file,capture_file,program_file,world_file,boss_file,access_file));assert world['passed'] and boss['passed'] and access['passed'];check(world['dungeonWorldCapture']);check(boss['capture']);check(access['capture']);check(native['completeNativeCellTrace'])
    with zipfile.ZipFile(native['completeNativeCellTrace']['path']) as z:
        assert z.namelist()==['all-native-final-cells.tsv'];raw=z.read('all-native-final-cells.tsv').decode('utf-8');trace=[]
        for line in raw.splitlines():
            realm,x,y,z,binding,wanted,actual,protected=line.split('\t');assert protected in ('true','false');trace.append((realm,int(x),int(y),int(z),binding,wanted,actual,protected=='true'))
    contract=plan['completeTwoDungeonNativeRealms'];original_worlds=read(world['dungeonWorldCapture']['path']);bosses=read(boss['capture']['path']);creatures=read(access['capture']['path']);arguments=(programs,contract['completeFieldMetadataBindings'],contract['originalUnbreakableFields'],original_worlds,bosses,creatures)
    result=verify(native,trace,*arguments);faults=[]
    for name in ['missing-cell','wrong-field','wrong-native-block','changed-protection','wrong-cage','removed-stage','changed-boss-attribute','lost-colour','missing-natural-merchant']:
        data=copy.deepcopy(native);rows=list(trace)
        if name=='missing-cell':rows.pop()
        elif name=='wrong-field':r=list(rows[0]);r[4]='wrong#0';rows[0]=tuple(r)
        elif name=='wrong-native-block':r=list(rows[0]);r[6]='Block{minecraft:air}';rows[0]=tuple(r)
        elif name=='changed-protection':r=list(rows[0]);r[7]=not r[7];rows[0]=tuple(r)
        elif name=='wrong-cage':data['worlds'][0]['nativeCages'][0]['entity']='cave_bug'
        elif name=='removed-stage':data['completeProgressionCases'].pop(0)
        elif name=='changed-boss-attribute':data['completeBossTraits'][0]['attributes'][0]['actual']+=1
        elif name=='lost-colour':data['completeAccessTraits'][0]['completeColourSaveCases'].pop()
        else:next(w for w in data['worlds'] if w['realm']=='immortallis')['observedLoadedActorsBeforeFixture'].pop()
        try:verify(data,rows,*arguments)
        except (AssertionError,KeyError,ValueError):faults.append(dict(name=name,generatedFault=True,rejected=True))
        else:raise AssertionError('Generated fault accepted: '+name)
    out=Path(output);assert not out.exists();frozen=out.with_suffix('.producer.py');frozen.write_bytes(Path(__file__).read_bytes());record=dict(passed=True,synthetic=False,generatedFaults=faults,completeAoAPort=False,fullSurvivalVerified=False,producer=ref(frozen),inputs=[ref(p) for p in (plan_file,capture_file,program_file,world_file,boss_file,access_file)],nativeTrace=native['completeNativeCellTrace'],**result);out.write_text(json.dumps(record,indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,output=str(out),faultsRejected=len(faults),**result)))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('plan','capture','programs','original_world','original_boss','original_access','output'):p.add_argument(n)
    a=p.parse_args();run(a.plan,a.capture,a.programs,a.original_world,a.original_boss,a.original_access,a.output)
