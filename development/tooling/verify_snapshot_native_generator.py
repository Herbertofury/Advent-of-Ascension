"""Read complete native generator evidence without certifying live dimensions."""
import argparse,copy,hashlib,json,zipfile
from pathlib import Path


def require(value,message):
    if not value:raise ValueError(message)


def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def artifact(path):
    path=Path(path).resolve();raw=path.read_bytes();return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def verify(ref):
    now=artifact(ref['path']);require(all(now[k]==ref[k] for k in ['sha256','bytes']),'Changed complete native authority: '+ref['path'])


def cases(value):
    require(value['passed'] and not value['synthetic'] and value['generatedDetachedFixtures'],'Real detached native fixtures required')
    expected={(realm,seed,x,z) for realm in ['aoa3:ethereus','aoa3:everland','aoa3:playtopia','aoa3:labricon'] for seed in [0,123456789] for x,z in [(0,0),(-1,-1)]}
    rows=value['completeCases'];require(len(rows)==16 and {(r['realm'],r['worldSeed'],r['chunkX'],r['chunkZ']) for r in rows}==expected,'Incomplete original realm/seed/chunk workload')
    require(all(r['allColumnAndPrototypePositionsCompared']==65536 and r['explicitGeneratedPaletteOnly'] and not r['liveLevelEdited'] for r in rows),'Omitted position or undeclared world mutation')
    require(value['completeComparedPositions']==sum(r['allColumnAndPrototypePositionsCompared'] for r in rows)==1048576,'Native position accounting differs')
    require(value['nativeCodecRoundTrips']==8 and value['crossWorldSeedMutationsRejected']==8 and value['fullRegisteredGeneratorDispatchVerified'] and value['callerColumnMutationDoesNotPoisonCache'],'Native codec, seed or isolated cache gate missing')
    require(value['explicitFixtureStone']=='aoa3:polluted_stone' and value['explicitFixtureTopAndFiller']=='minecraft:air','Different explicit generated fixture palette')
    require(all(value[k] is False for k in ['canonicalSurfaceIdentityVerified','liveLevelEdited','nativeDimensionsActivated','originalWorldEquivalenceVerified','completeAoAPort']),'Detached source fixtures cannot certify palette identity/live realms/full gameplay')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('server');p.add_argument('source_proof');p.add_argument('output');a=p.parse_args()
    output=Path(a.output);require(not output.exists(),'Retain earlier complete native proof')
    server,source_proof=read(a.server),read(a.source_proof)
    require(server['passed'] and server['compileVerified'] and server['nativeServerAdmissionVerified'] and server['allPrimaryChoicesAndAuthoritiesUnchanged'],'Full complete native mod server required')
    require(source_proof['passed'] and source_proof['server']['sha256']==artifact(a.server)['sha256'],'Independent complete-source/media proof is for another native build')
    verify(source_proof['sourceRecipePlan']);verify(source_proof['nativeCapture']);verify(source_proof['nativeJar']);verify(server['workspaceRequest'])
    plan=read(server['sourceRecipePlan']['path']);cohort=plan['snapshotNativeChunkGenerator'];verify(cohort['adapterDonor']);verify(cohort['completeNoiseNumericalProof'])
    native=Path(server['build']['build_root']);capture_file=native/'run/enderloom-forge1201-snapshot-native-generator.json';actual=read(capture_file);cases(actual)
    marker='ENDERLOOM_FORGE1201_SNAPSHOT_NATIVE_GENERATOR ';executed=[]
    with Path(server['build']['stdout_path']).open(encoding='utf-8') as log:
        for line in log:
            if marker in line:executed.append(json.loads(line.split(marker,1)[1]))
    require(executed==[actual],'Full native log and generator capture differ')
    sources=[]
    with zipfile.ZipFile(cohort['adapterDonor']['path']) as donor,zipfile.ZipFile(source_proof['nativeJar']['path']) as jar:
        for name in donor.namelist():
            if not name.startswith('src/main/java/'):continue
            raw=donor.read(name);require((native/name).read_bytes()==raw,'Complete native adapter source changed')
            entry=name[len('src/main/java/'):-len('.java')]+'.class';body=jar.read(entry)
            require(body[:4]==b'\xca\xfe\xba\xbe' and int.from_bytes(body[6:8],'big')==61,'Adapter was not compiled for the actual Java 17 target')
            sources.append(dict(path=name,sha256=hashlib.sha256(raw).hexdigest(),nativeClass=entry,nativeClassSha256=hashlib.sha256(body).hexdigest()))
    require(len(sources)==cohort['completeNativeSources']==8,'Complete native noise/surface/lifecycle family missing')
    controls=[]
    def reject(label,change):
        bad=copy.deepcopy(actual);change(bad)
        try:cases(bad)
        except (ValueError,KeyError):controls.append(dict(generatedFault=label,rejected=True));return
        raise ValueError('Generated bad result accepted: '+label)
    reject('omitted complete chunk',lambda r:r['completeCases'].pop())
    reject('omitted output position',lambda r:r['completeCases'][0].update(allColumnAndPrototypePositionsCompared=65535))
    reject('missing registered codec dispatch',lambda r:r.update(fullRegisteredGeneratorDispatchVerified=False))
    reject('cross-world seed mutation accepted',lambda r:r.update(crossWorldSeedMutationsRejected=0))
    reject('invented canonical palette acceptance',lambda r:r.update(canonicalSurfaceIdentityVerified=True))
    reject('premature live world acceptance',lambda r:r.update(nativeDimensionsActivated=True))
    frozen=output.with_suffix('.verifier.py');frozen.write_bytes(Path(__file__).read_bytes())
    report=dict(passed=True,synthetic=False,server=artifact(a.server),completeSourceMediaProof=artifact(a.source_proof),nativeCapture=artifact(capture_file),nativeJar=source_proof['nativeJar'],
                completeNewNativeSourceAndClassOwners=sources,completeGeneratorCases=16,completeComparedPositions=1048576,registeredCodecRoundTrips=8,generatedControlsRejected=controls,
                actualLogAndFullCaptureAgree=True,verifier=artifact(frozen),canonicalSurfaceIdentityVerified=False,nativeDimensionsActivated=False,originalWorldEquivalenceVerified=False,completeAoAPort=False)
    output.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k not in ['completeNewNativeSourceAndClassOwners','generatedControlsRejected']}))


if __name__=='__main__':main()
