#!/usr/bin/env python3
"""Reviewed delta over the checksum-locked TaCZ UI source. No source rediscovery."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent

def replace(text,old,new,label):
    assert old in text or new in text, 'Reconcile changed source: '+label
    return text.replace(old,new)

def main():
    path=ROOT/'build_ui.py';s=path.read_text()
    old=" for proof in selection['mergeProofs']:"
    new=""" selection['mergeProofs'] += [
  {'primary':'cf-1459599','aliases':['mr-RAIYwXWx'],'proof':'Exact same Cinder title, TCinder creator credit, description and matching artwork on both provider pages.'},
  {'primary':'cf-1671643','aliases':['mr-f6HDPJO8'],'proof':'Same CS2 to MC title, weapon roster and three identical decoded source-gallery images. Credited handles differ; source credits remain separately visible. Counts are not summed.'}]
 for proof in selection['mergeProofs']:"""
    s=replace(s,old,new,'reviewed provider variants')
    old=" items.sort(key=lambda x:(-(x['metrics']['downloads']"
    new=""" review=load(ROOT/'media-review-overrides.json')
 for x in items:
  x['media']=[m for m in x['media'] if m['sha256'] not in review['excludedPromotionalImages']]
  preferred=review['preferred'].get(x['id'])
  if preferred:
   assert any(m['sha256']==preferred for m in x['media']), ('Missing reviewed image',x['id'])
   x['preferredMediaSha256']=preferred
  if x['id'] in ('cf-1459599','cf-1671643'):x['type']='Gunpack (ZIP)'
 items.sort(key=lambda x:(-(x['metrics']['downloads']"""
    s=replace(s,old,new,'preferred weapon imagery')
    s=replace(s,"im=next((m for m in x['media'] if m['role']!='Project icon'),next(iter(x['media']),None))","im=next((m for m in x['media'] if m['sha256']==x.get('preferredMediaSha256')),None) or next((m for m in x['media'] if m['role']!='Project icon'),next(iter(x['media']),None))",'Wiki preferred image')
    old=" (ROOT/'app.js').write_text(js,encoding='utf-8')"
    new=""" js=js.replace("function mediaFor(x){return (x.media||[]).find(m=>m.role!=='Project icon')||(x.media||[])[0];}","function mediaFor(x){return (x.media||[]).find(m=>m.sha256===x.preferredMediaSha256)||(x.media||[]).find(m=>m.role!=='Project icon')||(x.media||[])[0];}")
 js=js.replace("switch(t.key){case 'type':", "switch(t.key){case 'id':found=norm(x.id)===v||(x.aliases||[]).some(a=>norm(a)===v);break;case 'name':found=norm(x.name).includes(v);break;case 'type':")
 (ROOT/'app.js').write_text(js,encoding='utf-8')"""
    s=replace(s,old,new,'preferred card image and exact identity search')
    path.write_text(s,encoding='utf-8')
    test=ROOT/'test_tacz.py';t=test.read_text()
    old="first=items[0];fid=first['id'];page.locator('#search').fill('\"'+first['name']+'\"');page.wait_for_timeout(200);check('quoted project search',page.locator('.project-card').count()==1)"
    new="""first=items[0];fid=first['id'];page.locator('#search').fill('"'+first['name']+'"');page.wait_for_timeout(200)
  found=page.locator('.project-card').evaluate_all('(a)=>a.map(x=>x.dataset.project)')
  import unicodedata
  def normalized(s):return ''.join(c for c in unicodedata.normalize('NFKD',str(s or '')) if not unicodedata.combining(c)).lower()
  phrase=normalized(first['name'])
  expected={x['id'] for x in items if phrase in normalized(' '.join([x['name'],x['summary'],x.get('descriptionExcerpt',''),x['ecosystem'],x['type']]+[a['name'] for a in x.get('authors',[])]+x.get('tags',[])+x.get('themes',[])+x.get('versions',[])))}
  check('quoted search preserves exact phrase references',set(found)==expected and fid in found,{'actual':found,'expected':sorted(expected)})
  page.locator('#search').fill('id:'+fid);page.wait_for_timeout(200);check('exact project identity search',page.locator('.project-card').count()==1 and page.locator('.project-card').get_attribute('data-project')==fid)"""
    t=replace(t,old,new,'quoted search versus exact identity')
    test.write_text(t,encoding='utf-8')
    (ROOT/'patch-source-proof.json').write_text(json.dumps({'overlayVersion':1,'buildSourceSha256':hashlib.sha256(s.encode()).hexdigest(),'browserTestSha256':hashlib.sha256(t.encode()).hexdigest(),'purpose':'Exact identity search, mathematically correct phrase regression, source-credited preview selection and two proven family variants'},indent=2))
if __name__=='__main__':main()
