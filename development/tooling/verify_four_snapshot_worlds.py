"""Independent native admission for all four complete historical worlds.

Generated corrupt records test this verifier; they never edit game worlds.
"""
import argparse,copy,hashlib,json
from pathlib import Path


def require(good,why):
    if not good:raise AssertionError(why)


def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def artifact(p):
    p=Path(p)
    with p.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=digest)


REALMS=['ethereus','everland','playtopia','labricon']


def check(record):
    require(record['passed'] and record['synthetic'] is False and record['adapter']=='four-complete-native-snapshot-worlds-1','Actual native world result required')
    rows=record['worlds'];require(len(rows)==4 and {r['realm'] for r in rows}=={'aoa3:'+r for r in REALMS},'All four distinct source-owned realms required')
    for row in rows:
        require(row['completeComparedPositions']==131072 and row['sentinelAbsentFromEveryPosition'] and row['nativeNoRespawnPolicy'],'Complete native columns, non-emitted sentinel and source respawn policy required')
        require(row['exactFixedAngle']==(.45 if row['realm']=='aoa3:labricon' else 0),'Exact original provider angle required')
        chunks=row['completeChunks'];require(len(chunks)==2 and {(c['x'],c['z']) for c in chunks}=={(0,0),(-3,5)},'Whole positive/negative native chunks required')
        require(all(c['status']=='minecraft:full' and c['completeComparedPositions']==65536 and c['nonAirStates']>0 for c in chunks),'Complete materialized nonempty native worlds required')
        require(row['nonAirStates']==sum(c['nonAirStates'] for c in chunks) and row['playerTraversalVerified'] is False,'Counts must be complete and unexercised player traversal remain open')
    require(record['completeComparedPositions']==524288 and record['exactNativeProviderTimeCases']==16,'Complete four-world position/time cohort required')
    stones=record['currentCanonicalRealmstones'];require(len(stones)==22 and len(set(stones))==22 and all(s.startswith('aoa3:') and s.endswith('_realmstone') for s in stones),'All current native realmstone references required')
    require(record['stableLabriconStack64SaveAndExtensionVerified'],'Stable collectible identity, count, max stack and unknown save data required')
    require(all(record[k] is False for k in ['fullSurvivalProgressionVerified','existingWorldMigrationVerified','originalFullWorldParityVerified','completeAoAPort']),'Unexercised full gameplay must stay open')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['plan','server','output']:ap.add_argument(k)
    a=ap.parse_args();plan,server=read(a.plan),read(a.server)
    require(server['passed'] and server['nativeServerAdmissionVerified'] and server['compileVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Full native build and unchanged primary authorities required')
    actual=artifact(a.plan);recorded=server['sourceRecipePlan']
    require(Path(recorded['path']).samefile(a.plan) and (actual['sha256'],actual['bytes'])==(recorded['sha256'],recorded['bytes']),'Exact complete source plan required')
    cfg=plan['snapshotFourWorldActivation'];require(cfg['realms']==REALMS and cfg['existingRealmstoneReferencesRepaired']==19 and cfg['existingLabriconStackMaximum']==64 and cfg['existingChunksModified'] is False,'Complete source-bound world/identity policy required')
    closure=cfg['completeAbsentSurfaceProgramOwners'];require(len(closure)==249 and len({r['path'] for r in closure})==249,'Every original builder/schematic owner required')
    recipes={r['path']:r for r in plan['sourceTransformations']}
    for row in closure:require(recipes[row['path']]['sha256']==row['sha256'],'Whole source program changed after surface absence proof')
    capture=read(server['capture']['path'])['fourSnapshotWorldInspection'];check(capture)
    file=Path(server['build']['build_root'])/'run/enderloom-forge1201-four-snapshot-worlds.json';require(read(file)==capture,'Native owned full result differs from the server capture')
    log=Path(server['build']['stdout_path']).read_text(encoding='utf-8');raw=file.read_text(encoding='utf-8')
    require(log.count('ENDERLOOM_FORGE1201_FOUR_SNAPSHOT_WORLDS ')==1 and 'ENDERLOOM_FORGE1201_FOUR_SNAPSHOT_WORLDS '+raw in log,'Exact single actual runtime marker required')
    faults=[]
    for fault in ['missing-realm','duplicate-realm','partial-column','wrong-angle','visible-sentinel','empty-world','wrong-coordinate','unbound-stone','lost-stack','invented-survival']:
        bad=copy.deepcopy(capture)
        if fault=='missing-realm':bad['worlds'].pop()
        elif fault=='duplicate-realm':bad['worlds'][-1]=copy.deepcopy(bad['worlds'][0])
        elif fault=='partial-column':bad['worlds'][0]['completeChunks'][0]['completeComparedPositions']-=1
        elif fault=='wrong-angle':bad['worlds'][3]['exactFixedAngle']=.44999
        elif fault=='visible-sentinel':bad['worlds'][0]['sentinelAbsentFromEveryPosition']=False
        elif fault=='empty-world':bad['worlds'][0]['completeChunks'][0]['nonAirStates']=0
        elif fault=='wrong-coordinate':bad['worlds'][0]['completeChunks'][0]['x']=1
        elif fault=='unbound-stone':bad['currentCanonicalRealmstones'].pop()
        elif fault=='lost-stack':bad['stableLabriconStack64SaveAndExtensionVerified']=False
        elif fault=='invented-survival':bad['fullSurvivalProgressionVerified']=True
        rejected=False
        try:check(bad)
        except AssertionError:rejected=True
        require(rejected,'Generated corrupt result accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
    output=Path(a.output);frozen=Path(str(output)+'.verifier.py');require(not output.exists() and not frozen.exists(),'Retain previous independent verification');frozen.write_bytes(Path(__file__).read_bytes())
    result=dict(passed=True,synthetic=False,plan=artifact(a.plan),server=artifact(a.server),nativeCapture=artifact(file),verifier=artifact(frozen),completeNativeWorlds=4,completeComparedPositions=524288,currentCanonicalRealmstones=22,generatedFaults=faults,fullSurvivalProgressionVerified=False,completeAoAPort=False)
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(passed=True,completeNativeWorlds=4,completeComparedPositions=524288,generatedFaults=len(faults),output=str(output))))


if __name__=='__main__':main()
