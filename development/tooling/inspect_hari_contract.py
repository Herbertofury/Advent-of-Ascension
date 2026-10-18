"""Inspect every class/nested JAR using the exact chosen Hari Vulkan implementation.

This conservative diagnostic does not certify Minecraft loading, visuals, gameplay,
thread safety or FPS. It never executes the inspected mod classes or changes a pack.
"""
import argparse
import base64
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import time
import uuid
import zipfile


def artifact(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def archive_inventory(raw, label, depth=0):
    if depth > 16:
        raise ValueError('Nested archive inspection limit: ' + label)
    classes, archives = 0, 1
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError('Duplicate archive member: ' + label)
        for entry in archive.infolist():
            body = archive.read(entry)  # Central-directory membership and every CRC are checked too.
            if entry.filename.endswith('.class'):
                if len(body) < 10 or body[:4] != b'\xca\xfe\xba\xbe':
                    raise ValueError('Invalid class file: ' + label + '!' + entry.filename)
                classes += 1
            elif entry.filename.endswith('.jar'):
                count, nested = archive_inventory(body, label + '!' + entry.filename, depth + 1)
                classes += count; archives += nested
    return classes, archives


def run(renderer, expected_hash, jars, java_home, output):
    output = Path(output)
    if output.exists():
        raise ValueError('Preserve prior evidence; choose a fresh output')
    began = time.perf_counter()
    renderer = artifact(renderer)
    if renderer['sha256'] != expected_hash:
        raise ValueError('Selected renderer bytes differ from the explicitly chosen identity')
    inputs = [artifact(p) for p in jars]
    inventories = [archive_inventory(Path(ref['path']).read_bytes(), Path(ref['path']).name) for ref in inputs]
    source = Path(__file__).with_name('HariArtifactInspection.java')
    source_before = artifact(source)
    with zipfile.ZipFile(renderer['path']) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError('Corrupt selected renderer member: ' + bad)
        contract = archive.read('assets/vulkanmod/compat/harimt_supported_gl_methods.properties')
        metadata = archive.read('META-INF/mods.toml')
    owner = output.resolve().parent / ('hari-artifact-inspection-' + str(uuid.uuid4()))
    owner.mkdir()
    jdk = Path(java_home).resolve()
    javac, java = [jdk / 'bin' / (name + ('.exe' if os.name == 'nt' else '')) for name in ('javac', 'java')]
    compilation = subprocess.run([str(javac), '--release', '17', '-encoding', 'UTF-8', '-d', str(owner), str(source)], capture_output=True, timeout=90)
    (owner / 'compile.log').write_bytes(compilation.stdout + compilation.stderr)
    compilation.check_returncode()
    process = subprocess.run([str(java), '-Dharimt.vulkan.compatCache=false', '-cp', os.pathsep.join([str(owner), renderer['path']]),
                              'dev.enderloom.probe.HariArtifactInspection', *[ref['path'] for ref in inputs]],
                             cwd=owner, capture_output=True, timeout=180)
    (owner / 'stdout.log').write_bytes(process.stdout)
    (owner / 'stderr.log').write_bytes(process.stderr)
    report = dict(schema=1, passed=False, renderer=renderer, inputs=inputs, inspectionSource=source_before,
                  compiler=artifact(javac), java=artifact(java), exitCode=process.returncode,
                  contractSha256=hashlib.sha256(contract).hexdigest(), metadataSha256=hashlib.sha256(metadata).hexdigest(),
                  references=[], unsupported=[], classes=0, archives=0, contractOwners=0,
                  minecraftLaunched=False, nativeRuntimeVerified=False, performanceVerified=False, completeAoAPort=False,
                  scope='Complete conservative byte inspection through the selected Hari implementation; no inactive-class exemptions, gameplay or performance acceptance')
    for line in process.stdout.decode('utf-8').splitlines():
        kind, separator, value = line.partition('=')
        if not separator:
            raise ValueError('Unexpected renderer inspection output')
        if kind in ('REF', 'UNSUPPORTED'):
            value = base64.b64decode(value, validate=True).decode('utf-8')
            if kind == 'REF':
                owner_name, name, descriptor, member = value.split('\t', 3)
                report['references'].append(dict(owner=owner_name, name=name, descriptor=descriptor, member=member))
            else:
                report['unsupported'].append(value)
        elif kind in ('CLASSES', 'ARCHIVES', 'CONTRACT_OWNERS'):
            report[dict(CLASSES='classes', ARCHIVES='archives', CONTRACT_OWNERS='contractOwners')[kind]] = int(value)
        else:
            raise ValueError('Unknown renderer inspection record: ' + kind)
    if artifact(renderer['path']) != renderer or [artifact(p['path']) for p in inputs] != inputs or artifact(source) != source_before:
        raise ValueError('Input changed during complete inspection')
    report['completeArchiveInventory'] = dict(classes=sum(row[0] for row in inventories), archives=sum(row[1] for row in inventories))
    report['passed'] = process.returncode == 0 and report['classes'] > 0 and report['classes'] == report['completeArchiveInventory']['classes'] and report['archives'] == report['completeArchiveInventory']['archives'] and report['contractOwners'] > 0
    report['staticContractsSatisfied'] = report['passed'] and not report['unsupported']
    report['logs'] = [artifact(owner / name) for name in ('compile.log', 'stdout.log', 'stderr.log')]
    report['measuredMs'] = (time.perf_counter() - began) * 1000
    with output.open('x', encoding='utf-8') as file:
        json.dump(report, file, indent=2)
    print(json.dumps({key: report[key] for key in ('passed', 'staticContractsSatisfied', 'classes', 'archives', 'contractOwners', 'measuredMs')} | dict(unsupported=len(report['unsupported']), output=str(output))))
    if not report['passed']:
        raise RuntimeError('Complete inspection failed; retained logs are diagnostic evidence')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--renderer', required=True)
    parser.add_argument('--renderer-sha256', required=True)
    parser.add_argument('--java-home', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('jars', nargs='+')
    args = parser.parse_args()
    run(args.renderer, args.renderer_sha256, args.jars, args.java_home, args.output)
