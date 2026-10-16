"""Verify every byte/member of a supplied local candidate; never infer runtime parity."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile


def digest(stream):
    result = hashlib.sha256()
    while block := stream.read(1024 * 1024):
        result.update(block)
    return result.hexdigest()


def verify(jar, inventory):
    jar = Path(jar)
    if jar.stat().st_size != inventory['artifact']['bytes']:
        raise ValueError('Complete local JAR length differs')
    with jar.open('rb') as stream:
        if digest(stream) != inventory['artifact']['sha256']:
            raise ValueError('Complete local JAR hash differs; a new build needs its own evidence')
    expected = inventory['members']
    if len(expected) != inventory['memberCount'] or len({row['path'] for row in expected}) != len(expected):
        raise ValueError('Incomplete or ambiguous expected member inventory')
    with zipfile.ZipFile(jar) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != {row['path'] for row in expected}:
            raise ValueError('Complete unique member membership differs')
        for row in expected:
            if archive.getinfo(row['path']).file_size != row['bytes']:
                raise ValueError('Member length differs: ' + row['path'])
            with archive.open(row['path']) as stream:
                if digest(stream) != row['sha256']:
                    raise ValueError('Member hash differs: ' + row['path'])
    return dict(passed=True, completeMembersVerified=len(expected),
                runtimeExecutionPerformed=False, completeAoAPort=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', required=True)
    parser.add_argument('--inventory', required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.artifact, json.loads(Path(args.inventory).read_text(encoding='utf-8')))))


if __name__ == '__main__':
    main()
