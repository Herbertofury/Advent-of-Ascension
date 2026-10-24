#!/usr/bin/env python3
"""Publish, verify and package the additive TaCZ deep-discovery release."""
from __future__ import annotations
import argparse,hashlib,json,re,shutil,sys,zipfile
from pathlib import Path
import requests
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent
sys.path.insert(0,str(DOCS));import weapon_inspiration_navigation as nav
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/'

def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def browser(pw):
 opts={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']};exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
 if exe:opts['executable_path']=exe
 return pw.chromium.launch(**opts)

def prepare(wiki):
 wiki=Path(wiki);manifest=load(PARENT/'wiki-manifest.json')
 publish={p['name']+'.md' for p in manifest['pages']}|{'TaCZ-Gunpacks.md','TaCZ-Gunpack-Hidden-Gems.md','Minecraft-Gunpack-Creator-Discoveries.md'}
 allowed=publish|set(nav.TARGETS)
 before={p.name:digest(p) for p in wiki.glob('*.md') if p.name not in allowed}
 for name in publish:shutil.copyfile(DOCS/name,wiki/name)
 nav.apply(wiki);assert not nav.apply(wiki)['changedPages'],'Navigation is not idempotent'
 assert all(digest(wiki/name)==sha for name,sha in before.items()),'Unrelated Wiki content changed'
 for name in publish|{'Weapon-Inspirations.md','Weapon-Reference-Library.md'}:shutil.copyfile(wiki/name,DOCS/name)
 actual={name:digest(wiki/name) for name in allowed if (wiki/name).exists()}
 save(ROOT/'qa/wiki-publication-source.json',{'pages':actual,'unrelatedPagesPreserved':len(before),'unrelatedHashes':before,'recursiveHubChildren':0})
 for page in manifest['pages']:
  p=DOCS/(page['name']+'.md');page.update(bytes=p.stat().st_size,sha256=digest(p))
 save(PARENT/'wiki-manifest.json',manifest)
 print(json.dumps({'publishedPages':len(actual),'unrelatedPagesPreserved':len(before),'idempotent':True}),flush=True)

def verify(wiki):
 out=ROOT/'qa/live';out.mkdir(parents=True,exist_ok=True);expected=load(ROOT/'qa/wiki-publication-source.json');report={'rawWiki':[],'navigation':{},'renderedPages':[],'explorers':[]}
 session=requests.Session();session.headers['User-Agent']='AoA-TaCZ-Deep-Discovery-Verification/1.0'
 for name,sha in expected['pages'].items():
  response=session.get(RAW+name,timeout=40);actual=hashlib.sha256(response.content).hexdigest();ok=response.ok and actual==sha
  report['rawWiki'].append({'page':name,'status':response.status_code,'sha256':actual,'matchesSource':ok});save(out/'publication.json',report);assert ok,(name,response.status_code,actual,sha)
 parent=load(PARENT/'catalog.json');tacz=load(PARENT/'tacz/catalog.json');ids=set(load(ROOT/'qa/data-delta.json')['newQualifiedIds']);new=[x for x in tacz['items'] if x['id'] in ids]
 with sync_playwright() as pw:
  b=browser(pw);p=b.new_page(viewport={'width':1500,'height':1100})
  p.goto(WIKI+'Weapon-Inspirations',wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for()
  headings=p.locator('h3').filter(has_text=re.compile('^Weapon inspirations$'));assert headings.count()==1,headings.count()
  heading=headings.first;heading.scroll_into_view_if_needed()
  state=heading.evaluate("h=>{const w=h.parentElement.classList.contains('markdown-heading')?h.parentElement:h;const list=w.nextElementSibling;return {tag:list?.tagName,nested:list?.querySelectorAll('ul').length,links:[...list.querySelectorAll('a')].map(x=>({text:x.textContent,url:x.href}))};}")
  assert state['tag']=='UL' and state['nested']==0 and not any(x['url'].endswith('/wiki/Weapon-Inspirations') for x in state['links']),state
  assert len(state['links'])==len({x['url'] for x in state['links']})
  report['navigation']={'oneHeading':True,'recursiveChildLinks':0,'nestedLists':0,'links':state['links']};p.screenshot(path=str(out/'organized-sidebar.png'))
  for slug,items,end in [('TaCZ-Gunpacks',tacz['items'],'End of gunpack gallery'),('TaCZ-Gunpack-Hidden-Gems',new,'End of hidden-gem gallery')]:
   p.goto(WIKI+slug,wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for()
   p.evaluate("()=>document.querySelectorAll('#wiki-body img').forEach(x=>x.loading='eager')");p.wait_for_function("()=>[...document.querySelectorAll('#wiki-body img')].every(x=>x.complete)",timeout=180000)
   result=p.evaluate("()=>{const w=document.querySelector('#wiki-body');const a=[...w.querySelectorAll('img')];return {text:w.innerText,images:a.length,broken:a.filter(x=>!x.naturalWidth).map(x=>x.alt),links:[...w.querySelectorAll('a')].map(x=>x.href)};}")
   norm=lambda s:re.sub(r'\s+',' ',s).strip()
   missing=[x['id'] for x in items if norm(x['name']) not in norm(result['text']) or not any('?item='+x['id'] in u for u in result['links'])]
   record={'page':slug,'expectedEntries':len(items),'images':result['images'],'broken':result['broken'],'missingIds':missing,'endMarker':end in result['text']}
   report['renderedPages'].append(record);save(out/'publication.json',report)
   assert not missing and not record['broken'] and record['endMarker'] and record['images']==len(items),record
   p.locator('#wiki-body').scroll_into_view_if_needed();p.screenshot(path=str(out/(slug+'-top.png')));p.locator('#wiki-body h2').last.scroll_into_view_if_needed();p.screenshot(path=str(out/(slug+'-end.png')))
  for suffix,data in [('',parent),('tacz/',tacz)]:
   response=p.goto(SITE+suffix,wait_until='domcontentloaded',timeout=90000);assert response and response.status==200
   p.wait_for_function('window.ATLAS_TEST',timeout=60000);got=p.evaluate('({count:GUN_ATLAS.items.length,hash:GUN_ATLAS.build.dataHash})')
   assert got=={'count':len(data['items']),'hash':data['build']['dataHash']},(suffix,got)
   p.locator('[data-deep-preset="all"]').click();shown=p.locator('.project-card').evaluate_all('(a)=>a.map(x=>x.dataset.project)');assert set(shown)==ids
   p.evaluate("()=>document.querySelectorAll('.project-card img').forEach(x=>x.loading='eager')");p.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(x=>x.complete)",timeout=90000)
   broken=p.locator('.project-card img').evaluate_all('(a)=>a.filter(x=>!x.naturalWidth).map(x=>x.alt)');assert not broken,broken
   p.screenshot(path=str(out/('tacz-discoveries.png' if suffix else 'atlas-discoveries.png')));report['explorers'].append({'path':suffix,**got,'newDiscoveryCount':len(shown),'brokenNewImages':broken})
  p.set_viewport_size({'width':390,'height':844});p.screenshot(path=str(out/'mobile-discoveries.png'));b.close()
 report['passed']=True;save(out/'publication.json',report);print(json.dumps(report),flush=True)

def package(directory):
 directory=Path(directory).resolve();directory.mkdir(parents=True,exist_ok=True);files={};skip={'cache','research-cache','fixtures','__pycache__','visual-review'}
 private_names={'raw-projects.json','export.json','export.csv','collection.json','snapshots.json','tail-snapshots.json','candidate-review.json','followup-evidence.json'}
 for p in PARENT.rglob('*'):
  rel=p.relative_to(PARENT)
  if not p.is_file() or any(part in skip for part in rel.parts) or p.name in private_names:continue
  files['minecraft-gun-mods/'+rel.as_posix()]=p
 files['weapon_inspiration_navigation.py']=DOCS/'weapon_inspiration_navigation.py'
 for pattern in ['Minecraft-Gun*.md','TaCZ-Gunpack*.md']:
  for p in DOCS.glob(pattern):files['wiki/'+p.name]=p
 for name in ('Weapon-Inspirations.md','Weapon-Reference-Library.md'):files['wiki/'+name]=DOCS/name
 parent=load(PARENT/'catalog.json');tacz=load(PARENT/'tacz/catalog.json');delta=load(ROOT/'qa/data-delta.json')
 for folder,data in [(PARENT,parent),(PARENT/'tacz',tacz)]:
  for item in data['items']:
   for media in item.get('media',[]):
    p=(folder/media['src']).resolve();assert p.is_file(),p;assert 'minecraft-gun-mods/'+p.relative_to(PARENT.resolve()).as_posix() in files;assert digest(p)==media['sha256'],media['src']
 intro='# Minecraft Gun Atlas - TaCZ Hidden Gems\n\nExtract this ZIP and open `minecraft-gun-mods/index.html` or `minecraft-gun-mods/tacz/index.html`. Both work offline without a local server.\n\nThis complete release contains '+str(len(parent['items']))+' parent-atlas records and '+str(len(tacz['items']))+' TaCZ families, including '+str(delta['newTaCZFamilies'])+' additional firearm-content discoveries. Every referenced archived image, source record and readable build script is included.\n\nLive atlas: '+SITE+'\nTaCZ: '+SITE+'tacz/\nHidden gems: '+SITE+'tacz/?theme=Hidden+gems\nResearch: '+WIKI+'TaCZ-Gunpack-Hidden-Gems\n\nUse Back up my collection to transfer favorites, notes, private ratings and saved views. Hosted and file:// copies have separate browser origins. The old catalog IDs are preserved. No installed Minecraft mod is changed.\n\nKoei\'s creator-hosted Unique Armaments has a verified release announcement and firearm previews, but its exact current download file, edition/price and Minecraft version pair remain explicit unknowns. Legacy restrictions and paid trial/full-edition distinctions are retained. This is source research, not a native Minecraft compatibility test.\n\nThe frozen-source update is reproducible with `python minecraft-gun-mods/tacz-deep-discovery/run.py`; the packaged source requires requests, beautifulsoup4 and pillow, but does not repeat completed discovery or download mod binaries.\n'
 path=directory/'Minecraft-Gun-Atlas.zip'
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for name,p in sorted(files.items()):z.write(p,name)
  z.writestr('START-HERE.md',intro)
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  for name,p in files.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest(p),name
 receipt={'archive':path.name,'bytes':path.stat().st_size,'sha256':digest(path),'files':len(files)+1,'parentProjects':len(parent['items']),'taczFamilies':len(tacz['items']),'newTaCZFamilies':delta['newTaCZFamilies'],'completeReferencedMedia':True,'parentDataHash':parent['build']['dataHash'],'taczDataHash':tacz['build']['dataHash']}
 save(directory/'RELEASE-VERIFICATION.json',receipt);(directory/'SHA256SUMS.txt').write_text(receipt['sha256']+'  '+path.name+'\n');(directory/'START-HERE.md').write_text(intro);print(json.dumps(receipt),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('action',choices=['prepare','verify','package']);p.add_argument('target');a=p.parse_args();{'prepare':prepare,'verify':verify,'package':package}[a.action](a.target)
