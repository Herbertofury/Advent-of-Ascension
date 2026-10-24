#!/usr/bin/env python3
"""Resume the exact qualified snapshot, then apply only the required content delta."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
ARTIFACT=12545901700
DIGEST='8d5604f104a9bc02c5b25d076a6ac91cb43e87aee6ce4b7feab089fbf6f23d38'

def restore():
 if (ROOT/'qualified-records.json').exists() and (ROOT/'coverage-recovery.json').exists():return
 with tempfile.TemporaryDirectory(prefix='tacz-qualified-') as temp:
  archive=Path(temp)/'source.zip'
  with archive.open('wb') as out:subprocess.run(['gh','api','repos/Herbertofury/Advent-of-Ascension/actions/artifacts/'+str(ARTIFACT)+'/zip'],stdout=out,check=True)
  assert hashlib.sha256(archive.read_bytes()).hexdigest()==DIGEST,'Qualified evidence artifact hash changed'
  with zipfile.ZipFile(archive) as z:
   for info in z.infolist():
    rel=Path(info.filename)
    if info.is_dir() or '..' in rel.parts or rel.is_absolute():continue
    if rel.suffix=='.py' or rel.name in {'selection.json','stage.txt'} or '__pycache__' in rel.parts:continue
    if rel.parts[0] not in {'cache','assets'} and rel.suffix!='.json':continue
    target=ROOT/rel
    if target.exists():continue
    target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(info))
 report=json.loads((ROOT/'qualification-report.json').read_text());assert report['qualified']==43 and not report['errors']
 print('Restored all qualified records and terminal search-tail evidence; no repeated sweep.',flush=True)

def source_decisions():
 path=ROOT/'reviewed-dispositions.json';review=json.loads(path.read_text());outpath=ROOT/'extra-decisions.json';decisions=json.loads(outpath.read_text())
 for key in review['supportOrExistingGunBehavior']:decisions[key]={'status':'excluded from gun-content count','reason':'Reviewed source identity describes a base runtime, gameplay/support, AI/equipment, packaging or existing-gun behavior. An independently authored additional firearm roster was not established for this collection.'}
 for key in review['otherEngineOrNonGunContent']:decisions[key]={'status':'excluded','reason':'Source identity targets another weapon engine, a standalone/legacy mod, cosmetics, crossbows or non-firearm collectibles rather than additional TaCZ firearms.'}
 for entry in review['representedVariants']:decisions[entry['id']]={'status':'already represented','reason':entry['reason']}
 for entry in review['notPromotedWithoutMoreEvidence']:decisions[entry['id']]={'status':'unresolved lead','reason':entry['reason']}
 outpath.write_text(json.dumps(decisions,ensure_ascii=False,indent=2),encoding='utf-8')

def main():
 restore()
 import creator_extra
 creator_extra.main()
 import late_qualification
 late_qualification.main()
 source_decisions()
 import finalize_deep
 finalize_deep.main()
 import build_deep
 build_deep.main()
if __name__=='__main__':main()
