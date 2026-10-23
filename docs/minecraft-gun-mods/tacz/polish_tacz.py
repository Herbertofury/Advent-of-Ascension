#!/usr/bin/env python3
"""Final source-scoped preview behavior and exhaustive data acceptance."""
from pathlib import Path
import hashlib,json
from PIL import Image
ROOT=Path(__file__).resolve().parent

def main():
 path=ROOT/'app.js';s=path.read_text();old="function gallery(id,index=0){const x=MAP.get(id);if(!x?.media?.length){openDetail(id);return;}lightboxId=id;lightboxIndex=(index+x.media.length)%x.media.length;"
 new="function gallery(id,index=null){const x=MAP.get(id);if(!x?.media?.length){openDetail(id);return;}if(index===null)index=Math.max(0,x.media.findIndex(m=>m.sha256===x.preferredMediaSha256));lightboxId=id;lightboxIndex=(index+x.media.length)%x.media.length;"
 assert old in s or new in s,'Gallery source changed';s=s.replace(old,new)
 s=s.replace("&&mediaFor(x)&&!heroes.some(h=>h.ecosystem===x.ecosystem)","&&mediaFor(x)&&!heroes.includes(x)")
 path.write_text(s,encoding='utf-8')
 test=ROOT/'test_tacz.py';t=test.read_text();old="page.wait_for_function('window.ATLAS_TEST');report['metrics']['initialDOMms']"
 new="page.wait_for_function('window.ATLAS_TEST');page.screenshot(path=str(out/'initial-desktop.png'));report['metrics']['initialDOMms']"
 assert old in t or new in t;t=t.replace(old,new)
 old="many=next(x for x in items if len(x['media'])>1);"
 new="many=next(x for x in items if x.get('preferredMediaSha256') and len(x['media'])>1);"
 assert old in t or new in t;t=t.replace(old,new)
 old="page.keyboard.press('ArrowRight');page.keyboard.press('Escape')"
 new="check('gallery starts with the exact reviewed card preview',page.locator('#lightboxContent .lightbox-stage img').get_attribute('src')==next(m['src'] for m in many['media'] if m['sha256']==many['preferredMediaSha256']));page.keyboard.press('ArrowRight');page.keyboard.press('Escape')"
 assert old in t or new in t;t=t.replace(old,new)
 t=t.replace("page.locator('[data-action=\"detail\"][data-id=\"'+fid+'\"]')","page.locator('.project-card [data-action=\"detail\"][data-id=\"'+fid+'\"]')")
 test.write_text(t,encoding='utf-8')
 data=json.loads((ROOT/'catalog.json').read_text());items=data['items'];ids={x['id'] for x in items};assert len(ids)==len(items)
 images={m['src']:m for x in items for m in x['media']};errors=[]
 for path,m in images.items():
  actual=ROOT/path
  if hashlib.sha256(actual.read_bytes()).hexdigest()!=m['sha256']:errors.append(path)
  with Image.open(actual) as image:image.verify()
 assert not errors,errors
 for x in items:
  assert x['metrics']['communityRating'] is None
  for key,field,provider in [('cfDownloads','downloads','CurseForge'),('favorites','favorites','CurseForge'),('mrDownloads','downloads','Modrinth'),('followers','followers','Modrinth')]:
   values=[v[field] for v in x['metricSources'] if v['provider']==provider and isinstance(v.get(field),(int,float))]
   assert x['metrics'][key]==(max(values) if values else None),(x['id'],key)
 selection=json.loads((ROOT/'selection.json').read_text());additional=json.loads((ROOT/'additional-selection.json').read_text());excluded={x['id'] for x in selection['excludedExamples']}|set(additional['excluded']);assert not ids&excluded
 qa=ROOT/'qa';qa.mkdir(exist_ok=True)
 report={'projects':len(items),'referencedImageFiles':len(images),'imageHashesAndDecodePassed':True,'excludedUtilityIdsInCatalog':[],'providerMetricsIndependentlyReconciled':True,'inventedCommunityRatings':0,'parentCatalogSha256':hashlib.sha256((ROOT.parent/'catalog.json').read_bytes()).hexdigest(),'dataHash':data['build']['dataHash']}
 (qa/'data-validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report),flush=True)
if __name__=='__main__':main()
