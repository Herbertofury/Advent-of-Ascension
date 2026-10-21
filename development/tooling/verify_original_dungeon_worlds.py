"""Compare every authored dungeon cell with independently observed native worlds.

This preserves the observed callback differences explicitly. Original vines
deleting themselves are a recorded original bug, never an AIR conversion rule.
"""
import argparse,copy,hashlib,json,re
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def ref(p):
    p=Path(p).absolute()
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=h)
def check(r):assert all(ref(r['path'])[k]==r[k] for k in ('bytes','sha256')),r['path']
def origin(name):
    if '.immortallis.' in name:return (-15,17,-40)
    return {'ConiferonRoom':(-75,15,-75),'HoronRoom':(75,15,-75),'PenumbraRoom':(-75,15,75),'GoldorthRoom':(75,15,75)}.get(name.rsplit('.',1)[-1],(-20,15,-20))
def verify(data,programs,traits):
    assert data['passed'] and data['originalRuntime'] and not data['syntheticWorld'] and not data['clientLaunched'] and data['observedServerTicks']>=60
    vanilla={'field_150353_l':'minecraft:lava','field_150356_k':'minecraft:flowing_lava','field_150411_aY':'minecraft:iron_bars'}
    assert {r['originalField']:r['nativeRegistryIdentity'] for r in data['actualVanillaBindings']}==vanilla
    identities={r['originalField']:r['registeredIdentity'] for r in traits['completeBlockObservations']}
    final={r:{} for r in ('ancient_cavern','immortallis')}
    for name,ops in programs.items():
        realm='immortallis' if '.immortallis.' in name else 'ancient_cavern';offset=origin(name)
        for x,y,z,field,meta,mode in ops:final[realm][(x+offset[0],y+offset[1],z+offset[2])]=(field,meta)
    results=[]
    for phase in ('initial','afterSixtyActualTicks'):
        assert {r['realm'] for r in data[phase]}==set(final)
        for world in data[phase]:
            realm=world['realm'];assert world['nativeNoSky'] and len(world['completeCells'])==len(final[realm])
            seen=set();differences=[]
            for x,y,z,identity,meta in world['completeCells']:
                pos=(x,y,z);assert pos not in seen;seen.add(pos);field,expected_meta=final[realm][pos];short=field.rsplit('.',1)[1]
                expected=vanilla[short] if field.startswith('net/minecraft/') else identities[short]
                if (identity,meta)!=(expected,expected_meta):
                    assert (short in ('AncientVines','AncientVineCap') and identity=='minecraft:air' and meta==0) or (expected=='minecraft:lava' and identity=='minecraft:flowing_lava' and meta==expected_meta)
                    differences.append(dict(position=pos,originalField=field,literal=[expected,expected_meta],observed=[identity,meta]))
            assert seen==final[realm].keys()
            assert len(differences)==(53 if realm=='ancient_cavern' else 1190)
            cages={pos:field for pos,(field,meta) in final[realm].items() if '.Spawner' in field};tiles=world['completeBlockEntities'];assert len(tiles)==len(cages)==(8 if realm=='ancient_cavern' else 32)
            observed=set()
            for tile in tiles:
                pos=tuple(tile['position']);assert pos in cages and pos not in observed;observed.add(pos)
                assert tile['class']=='net.minecraft.tileentity.TileEntityMobSpawner';nbt=tile['completeNativeNbt']
                short=cages[pos].rsplit('.',1)[1][7:];short={'Goldem':'Goldum','Flowerface':'FlowerFace','CaveBug':'RockCritter'}.get(short,short)
                assert 'EntityId:"nevermine.'+short+'"' in nbt
                for key,value in dict(MaxNearbyEntities=6,RequiredPlayerRange=16,SpawnCount=4,MaxSpawnDelay=800,SpawnRange=4,Delay=20,MinSpawnDelay=200).items():assert re.search(r'\b'+key+':'+str(value)+r's\b',nbt)
            actors=world['completeLoadedAoAActors'];expected_actors=[] if realm=='ancient_cavern' else [('net.nevermine.npc.entity.EntityDungeonKeeper',15,19,5),('net.nevermine.npc.entity.EntityTokenCollector',-3,19,5)]
            assert sorted((a['class'],a['x'],a['y'],a['z']) for a in actors)==sorted(expected_actors)
            results.append(dict(phase=phase,realm=realm,completeCells=len(seen),nativeCages=len(cages),nativeActors=len(actors),completeNativeCallbackDifferences=differences))
    return results
def run(capture,program_file,traits_file,output):
    receipt=read(capture);assert receipt['passed'] and receipt['dedicatedServerOnly'] and receipt['temporaryObserverRemoved'] and receipt['allOriginalModAndLibraryBytesUnchanged']
    reference=receipt['dungeonWorldCapture'];check(reference);data=read(reference['path']);programs=read(program_file);traits=read(traits_file)
    results=verify(data,programs,traits);faults=[]
    for name in ('missing-cell','wrong-mob','changed-delay','wrong-actor-position'):
        altered=copy.deepcopy(data)
        if name=='missing-cell':altered['initial'][0]['completeCells'].pop()
        elif name=='wrong-mob':altered['initial'][0]['completeBlockEntities'][0]['completeNativeNbt']=altered['initial'][0]['completeBlockEntities'][0]['completeNativeNbt'].replace('Bloodsucker','Goldum')
        elif name=='changed-delay':altered['initial'][0]['completeBlockEntities'][0]['completeNativeNbt']=altered['initial'][0]['completeBlockEntities'][0]['completeNativeNbt'].replace('Delay:20s','Delay:0s')
        else:altered['initial'][1]['completeLoadedAoAActors'][0]['x']+=1
        try:verify(altered,programs,traits)
        except (AssertionError,KeyError):faults.append(name);continue
        raise AssertionError('Generated fault escaped: '+name)
    out=Path(output);assert not out.exists();record=dict(passed=True,originalNativeRuntime=True,capture=ref(capture),observations=reference,programs=ref(program_file),traits=ref(traits_file),completeComparisons=results,generatedFaultsRejected=faults,freshWorldClaim=False,convertedNativeGameplayVerified=False,completeAoAPort=False)
    frozen=out.with_suffix('.producer.py');frozen.write_bytes(Path(__file__).read_bytes());record['producer']=ref(frozen);out.write_text(json.dumps(record,indent=2),encoding='utf-8');print(json.dumps(dict(passed=True,cells=52416,phases=2,cages=40,faults=len(faults))))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('capture','programs','traits','output'):p.add_argument(n)
    a=p.parse_args();run(a.capture,a.programs,a.traits,a.output)
