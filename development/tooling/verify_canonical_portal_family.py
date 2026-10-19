"""Independent native canonical-portal cohort acceptance.

Requires a complete admitted server. Generated bad-result controls exercise
the verifier; they are not gameplay faults injected into the user's worlds.
"""
import argparse,copy,hashlib,json
from pathlib import Path


def require(value,reason):
    if not value:raise AssertionError(reason)
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def artifact(path):
    p=Path(path)
    with p.open('rb') as stream:digest=hashlib.file_digest(stream,'sha256').hexdigest()
    return dict(path=str(p),bytes=p.stat().st_size,sha256=digest)


def check_capture(result,expected):
    require(result['adapter']=='complete-native-restored-portals-1' and result['passed'] and not result['synthetic'] and result['controlledPrebuiltFrames'],'Actual native complete portal cohort required')
    rows=result['canonicalPortals'];require(len(rows)==22 and len({r['portal'] for r in rows})==22,'All 22 distinct canonical portal owners required')
    require({r['portal']:r['destination'] for r in rows}==expected,'Canonical portal/dimension identity changed')
    require(result['actualNativeEntityRoundTrips']==21 and result['nativePortalConfigurationRestored'],'Full native travel/config restoration required')
    for row in rows:
        require(row['nativeTeleporter'].startswith('net.tslat.aoa3.content.world.teleporter.specific.'),'Native teleporter substituted')
        if row['portal']=='aoa3:nowhere_portal':
            require(row['nativeFixedLobbyRoutingVerified'] and row['genericPortalCacheNotUsed'] and row['specializedPlayerOnlyEntryPreserved'],'Specialized Nowhere lobby/player-only behavior changed')
        else:
            for field in ['nativeCacheKeyVerified','immutableCachedPosition','disabledNonPlayerChoicePreserved','cooldownChoicePreserved','actualNativeEntityRoundTrip','uuidAndForgeNbtRetained']:
                require(row[field],'Incomplete native portal behavior: '+row['portal']+' / '+field)
        require(row['playerTravelVerified'] is False,'Entity-only cohort must not certify player travel')
    require(all(result[field] is False for field in ['playerTravelVerified','naturalAcquisitionVerified','multiplayerVerified','completeAoAPort']),'Unexercised gameplay claims must remain open')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['plan','server','output']:ap.add_argument(name)
    a=ap.parse_args();plan=read(a.plan);server=read(a.server)
    require(server['passed'] and server['nativeServerAdmissionVerified'] and server['compileVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Whole native build/server and unchanged authorities required')
    recorded=server['sourceRecipePlan'];actual=artifact(a.plan)
    require(Path(recorded['path']).samefile(a.plan) and (recorded['sha256'],recorded['bytes'])==(actual['sha256'],actual['bytes']),'Native server was not built from this complete plan')
    capture=read(server['capture']['path']);result=capture['restoredPortalInspection']
    expected={r['blockKey']:r['targetWorld'] for r in plan['completeCanonicalPortalAccess']['allCanonicalPortals']};require(len(expected)==22,'Full source-bound canonical portal census required')
    check_capture(result,expected)
    raw_file=Path(server['build']['build_root'])/'run/enderloom-forge1201-restored-portals.json';require(read(raw_file)==result,'Full server capture and native portal record differ')
    raw=raw_file.read_text(encoding='utf-8');log=Path(server['build']['stdout_path']).read_text(encoding='utf-8',errors='strict')
    require(log.count('ENDERLOOM_FORGE1201_RESTORED_PORTALS ')==1 and 'ENDERLOOM_FORGE1201_RESTORED_PORTALS '+raw in log,'Exact native portal evidence/log marker required')
    faults=[]
    for fault in ['missing-owner','duplicate-owner','wrong-dimension','mutable-cache','ignored-config','ignored-cooldown','lost-entity-data','wrong-nowhere-routing','lost-config-restoration','invented-player-parity']:
        bad=copy.deepcopy(result);generic=next(r for r in bad['canonicalPortals'] if r['portal']!='aoa3:nowhere_portal');special=next(r for r in bad['canonicalPortals'] if r['portal']=='aoa3:nowhere_portal')
        if fault=='missing-owner':bad['canonicalPortals'].pop()
        elif fault=='duplicate-owner':bad['canonicalPortals'][-1]=copy.deepcopy(bad['canonicalPortals'][0])
        elif fault=='wrong-dimension':generic['destination']='minecraft:overworld'
        elif fault=='mutable-cache':generic['immutableCachedPosition']=False
        elif fault=='ignored-config':generic['disabledNonPlayerChoicePreserved']=False
        elif fault=='ignored-cooldown':generic['cooldownChoicePreserved']=False
        elif fault=='lost-entity-data':generic['uuidAndForgeNbtRetained']=False
        elif fault=='wrong-nowhere-routing':special['nativeFixedLobbyRoutingVerified']=False
        elif fault=='lost-config-restoration':bad['nativePortalConfigurationRestored']=False
        elif fault=='invented-player-parity':bad['playerTravelVerified']=True
        rejected=False
        try:check_capture(bad,expected)
        except AssertionError:rejected=True
        require(rejected,'Generated broken result accepted: '+fault);faults.append(dict(fault=fault,generated=True,rejected=True))
    out=Path(a.output);frozen=Path(str(out)+'.verifier.py');require(not out.exists() and not frozen.exists(),'Preserve previous verification');frozen.write_bytes(Path(__file__).read_bytes())
    out.write_text(json.dumps(dict(passed=True,synthetic=False,scope='Controlled native entity portal travel; player UI, natural acquisition and multiplayer remain separate',plan=artifact(a.plan),server=artifact(a.server),capture=artifact(raw_file),verifier=artifact(frozen),canonicalPortals=22,actualNativeEntityRoundTrips=21,specializedNowhereLobbyRetained=True,generatedFaults=faults,completeAoAPort=False),indent=2),encoding='utf-8')
    print(json.dumps(dict(passed=True,canonicalPortals=22,actualNativeEntityRoundTrips=21,generatedFaults=len(faults),output=str(out))))


if __name__=='__main__':main()
