#!/usr/bin/env python3
"""Single-flight continuation of the TaCZ research, build and verification stages."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
ARTIFACT=12544699488
DIGEST='30a04606137edd65713f2beb1e0a096fbe62aa50f6edec959e5f6324322453d1'

def restore():
 if (ROOT/'discovery.json').exists() and (ROOT/'snapshots.json').exists():return
 with tempfile.TemporaryDirectory(prefix='tacz-evidence-') as temp:
  archive=Path(temp)/'source.zip'
  with archive.open('wb') as out:subprocess.run(['gh','api','repos/Herbertofury/Advent-of-Ascension/actions/artifacts/'+str(ARTIFACT)+'/zip'],stdout=out,check=True)
  assert hashlib.sha256(archive.read_bytes()).hexdigest()==DIGEST,'Original discovery artifact hash changed'
  with zipfile.ZipFile(archive) as z:
   for info in z.infolist():
    rel=Path(info.filename)
    if info.is_dir() or '..' in rel.parts or rel.is_absolute():continue
    if rel.parts[0]!='cache' and rel.name not in {'discovery.json','snapshots.json','candidate-review.json'}:continue
    target=ROOT/rel
    if target.exists():continue
    target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(info))
 assert (ROOT/'snapshots.json').exists()
 print('Restored exact discovery evidence; no repeated source sweep.',flush=True)

def main():
 restore()
 import hydrate
 hydrate.main()
 if (ROOT/'build_deep.py').exists():
  import build_deep
  build_deep.main()
 else:print('Qualified media and search-tail evidence saved. Catalog publication waits for final identity review.',flush=True)
if __name__=='__main__':main()
