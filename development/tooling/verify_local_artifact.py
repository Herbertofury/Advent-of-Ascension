"""Verify every byte/member of a supplied local candidate; never infer runtime parity."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import zipfile


def digest(stream):
    result = hashlib.sha256()
    while block := stream.read(1024 * 1024):
        result.update(block)
    return result.hexdigest()


def file_identity(stat):
    """Identify the opened object and detect writes during this bounded check."""
    return (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)


def verify(jar, inventory):
    jar = Path(jar)
    expected = inventory['members']
    if len(expected) != inventory['memberCount'] or len({row['path'] for row in expected}) != len(expected):
        raise ValueError('Incomplete or ambiguous expected member inventory')
    # Hash and inspect the same opened object. Reopening the path can combine a
    # digest from an old candidate with members from a concurrently replaced JAR.
    with jar.open('rb') as candidate:
        identity = file_identity(os.fstat(candidate.fileno()))
        if identity[2] != inventory['artifact']['bytes']:
            raise ValueError('Complete local JAR length differs')
        if digest(candidate) != inventory['artifact']['sha256']:
            raise ValueError('Complete local JAR hash differs; a new build needs its own evidence')
        candidate.seek(0)
        with zipfile.ZipFile(candidate) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != {row['path'] for row in expected}:
                raise ValueError('Complete unique member membership differs')
            for row in expected:
                if archive.getinfo(row['path']).file_size != row['bytes']:
                    raise ValueError('Member length differs: ' + row['path'])
                with archive.open(row['path']) as stream:
                    if digest(stream) != row['sha256']:
                        raise ValueError('Member hash differs: ' + row['path'])
        try:
            unchanged = (file_identity(os.fstat(candidate.fileno())) == identity
                         and file_identity(jar.stat()) == identity)
        except OSError as exc:
            raise ValueError('Candidate path changed during verification') from exc
        if not unchanged:
            raise ValueError('Candidate path or bytes changed during verification')
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
