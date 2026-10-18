"""Detect duplicate complete Java owners before an incremental compiler diagnostic.

The target JDK parses every actual selected main-source unit, with changed units
substituted by exact project-relative path. Comments, strings, nested classes,
Unicode escapes and all package-private top-level owners use javac's real AST.
"""
import collections, hashlib, os, subprocess
from pathlib import Path

def inspect(jdk, build_root, java_directories, substitutions, owner):
    build_root, owner, jdk = Path(build_root).absolute(), Path(owner).absolute(), Path(jdk).absolute()
    selected = {}
    for directory in java_directories:
        directory = Path(directory).absolute()
        if not directory.is_relative_to(build_root): raise ValueError('Main Java source root escaped its accepted project')
        for path in directory.rglob('*.java'):
            if path.is_symlink() or path.is_junction(): raise ValueError('Linked source census input excluded')
            selected[path.relative_to(build_root).as_posix()] = path
    for relative, path in substitutions.items():
        candidate = build_root / relative
        if not any(candidate.is_relative_to(Path(d).absolute()) for d in java_directories):
            raise ValueError('Changed Java unit is outside every actual main source root: '+relative)
        selected[relative] = Path(path).absolute()
    if not selected: raise ValueError('Complete source census cannot be empty')
    def artifact(path):
        with path.open('rb') as stream: digest=hashlib.file_digest(stream,'sha256').hexdigest()
        return dict(path=str(path),bytes=path.stat().st_size,sha256=digest)
    source=Path(__file__).with_name('CompleteSourceOwners.java')
    frozen=owner/'CompleteSourceOwners.java';frozen.write_bytes(source.read_bytes())
    inputs={key:artifact(path) for key,path in sorted(selected.items())}
    manifest=owner/'complete-source-owner-inputs.txt'
    if any('\n' in str(path) or '\t' in str(path) for path in selected.values()): raise ValueError('Ambiguous source census path')
    manifest.write_text('\n'.join(str(path) for _,path in sorted(selected.items()))+'\n',encoding='utf-8')
    output=owner/'complete-source-owners.tsv'
    java=jdk/'bin'/('java.exe' if os.name=='nt' else 'java')
    javac=jdk/'bin'/('javac.exe' if os.name=='nt' else 'javac')
    classes=owner/'source-owner-parser-classes';classes.mkdir()
    compiled=subprocess.run([str(javac),'-encoding','UTF-8','-d',str(classes),str(frozen)],capture_output=True,timeout=60,
                            creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    (owner/'source-owners-compiler.stdout.log').write_bytes(compiled.stdout);(owner/'source-owners-compiler.stderr.log').write_bytes(compiled.stderr)
    if compiled.returncode: raise ValueError('Target-JDK source parser compilation failed: '+compiled.stderr.decode('utf-8',errors='replace'))
    classpath=str(classes)
    if (jdk/'lib/tools.jar').is_file(): classpath+=os.pathsep+str(jdk/'lib/tools.jar')
    run=subprocess.run([str(java),'-cp',classpath,'CompleteSourceOwners',str(manifest),str(output)],capture_output=True,timeout=180,
                       creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    (owner/'source-owners.stdout.log').write_bytes(run.stdout);(owner/'source-owners.stderr.log').write_bytes(run.stderr)
    if run.returncode: raise ValueError('Complete target-JDK source census failed: '+run.stderr.decode('utf-8',errors='replace'))
    actual={key:artifact(path) for key,path in sorted(selected.items())}
    if inputs!=actual: raise ValueError('Complete source bytes changed during target-JDK parsing')
    groups=collections.defaultdict(list)
    for line in output.read_text(encoding='utf-8').splitlines():
        name,path=line.split('\t');groups[name].append(path)
    duplicates=[dict(owner=name,completeSourcePaths=paths) for name,paths in sorted(groups.items()) if len(paths)>1]
    return dict(passed=not duplicates,synthetic=False,completeUnits=len(inputs),topLevelOwners=sum(len(v) for v in groups.values()),
                completeInputs=inputs,duplicateOwners=duplicates,parser=artifact(frozen),targetJava=artifact(java),targetJavac=artifact(javac),
                completeOwners=artifact(output),sourceManifest=artifact(manifest),runtimeVerified=False)
