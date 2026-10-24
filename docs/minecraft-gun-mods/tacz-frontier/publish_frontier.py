#!/usr/bin/env python3
"""Actual Wiki/Pages publication and reproducible complete-archive verification."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,shutil,sys,zipfile
import requests
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent
sys.path.insert(0,str(DOCS));import weapon_inspiration_navigation as nav
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/'
PAGE='TaCZ-Gunpack-Creator-Frontier'

def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def browser(pw):
 opts={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']};exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
 if exe:opts['executable_path']=exe
 return pw.chromium.launch(**opts)

def prepare(wiki):
 wiki=Path(wiki);manifest=load(PARENT/'wiki-manifest.json');names={p['name']+'.md' for p in manifest['pages']}|{'TaCZ-Gunpacks.md','TaCZ-Gunpack-Hidden-Gems.md',PAGE+'.md','Minecraft-Gunpack-Creator-Discoveries.md'};allowed=names|set(nav.TARGETS)
 before={p.name:digest(p) for p in wiki.glob('*.md') if p.name not in allowed}
 for name in names:shutil.copyfile(DOCS/name,wiki/name)
 nav.apply(wiki);assert not nav.apply(wiki)['changedPages'];assert all(digest(wiki/n)==h for n,h in before.items())
 for name in names|{'Weapon-Inspirations.md','Weapon-Reference-Library.md'}:shutil.copyfile(wiki/name,DOCS/name)
 source={name:digest(wiki/name) for name in allowed if (wiki/name).exists()}
 save(ROOT/'qa/wiki-publication-source.json',{'pages':source,'unrelatedPagesPreserved':len(before),'unrelatedHashes':before,'recursiveChildHubLinks':0})
 for page in manifest['pages']:
  p=DOCS/(page['name']+'.md');page.update(bytes=p.stat().st_size,sha256=digest(p))
 save(PARENT/'wiki-manifest.json',manifest);print(json.dumps({'publishedPages':len(source),'unchangedOtherPages':len(before)}),flush=True)

def verify(wiki):
 out=ROOT/'qa/live';out.mkdir(parents=True,exist_ok=True);source=load(ROOT/'qa/wiki-publication-source.json');report={'rawWiki':[],'renderedPages':[],'explorers':[]};s=requests.Session();s.headers['User-Agent']='AoA-Creator-Frontier-Verification/1.0'
 for name,h in source['pages'].items():
  r=s.get(RAW+name,timeout=40);actual=hashlib.sha256(r.content).hexdigest();ok=r.ok and actual==h;report['rawWiki'].append({'page':name,'status':r.status_code,'sha256':actual,'matches':ok});save(out/'publication.json',report);assert ok,(name,actual,h)
 parent=load(PARENT/'catalog.json');tacz=load(PARENT/'tacz/catalog.json');ids=set(load(ROOT/'qualified-records.json'));oldids=set(load(PARENT/'tacz-deep-discovery/qualified-records.json'))|set(load(PARENT/'tacz-deep-discovery/extra-records.json'))
 with sync_playwright() as pw:
  b=browser(pw);p=b.new_page(viewport={'width':1500,'height':1050});p.goto(WIKI+'Weapon-Inspirations',wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for();headings=p.locator('h3').filter(has_text=re.compile('^Weapon inspirations$'));assert headings.count()==1
  h=headings.first;h.scroll_into_view_if_needed();state=h.evaluate("h=>{const w=h.parentElement.classList.contains('markdown-heading')?h.parentElement:h;const list=w.nextElementSibling;return {tag:list?.tagName,nested:list?.querySelectorAll('ul').length,links:[...list.querySelectorAll('a')].map(x=>({text:x.textContent,url:x.href}))};}")
  assert state['tag']=='UL' and state['nested']==0 and not any(x['url'].endswith('/wiki/Weapon-Inspirations') for x in state['links']);assert len(state['links'])==len({x['url'] for x in state['links']});report['navigation']={'oneHeading':True,'recursiveChildLinks':0,'nestedLists':0,'links':state['links']};p.screenshot(path=str(out/'organized-navigation.png'))
  collections=[('TaCZ-Gunpacks',tacz['items'],'End of gunpack gallery'),('TaCZ-Gunpack-Hidden-Gems',[x for x in tacz['items'] if x['id'] in oldids],'End of hidden-gem gallery'),(PAGE,[x for x in tacz['items'] if x['id'] in ids],'End of creator-frontier gallery')]
  for slug,items,end in collections:
   p.goto(WIKI+slug,wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for();p.evaluate("()=>document.querySelectorAll('#wiki-body img').forEach(x=>x.loading='eager')");p.wait_for_function("()=>[...document.querySelectorAll('#wiki-body img')].every(x=>x.complete)",timeout=180000)
   got=p.evaluate("()=>{const w=document.querySelector('#wiki-body'),a=[...w.querySelectorAll('img')];return {text:w.innerText,images:a.length,broken:a.filter(x=>!x.naturalWidth).map(x=>x.alt),links:[...w.querySelectorAll('a')].map(x=>x.href)};}");norm=lambda x:re.sub(r'\s+',' ',x).strip();missing=[x['id'] for x in items if norm(x['name']) not in norm(got['text']) or not any('?item='+x['id'] in u for u in got['links'])]
   record={'page':slug,'expected':len(items),'images':got['images'],'broken':got['broken'],'missing':missing,'endMarker':end in got['text']};report['renderedPages'].append(record);save(out/'publication.json',report);assert got['images']==len(items) and not missing and not got['broken'] and record['endMarker'],record
   p.locator('#wiki-body').scroll_into_view_if_needed();p.screenshot(path=str(out/(slug+'.png')))
  for suffix,data in [('',parent),('tacz/',tacz)]:
   response=p.goto(SITE+suffix,wait_until='domcontentloaded',timeout=90000);assert response and response.status==200;p.wait_for_function('window.ATLAS_TEST',timeout=60000);got=p.evaluate('({count:GUN_ATLAS.items.length,hash:GUN_ATLAS.build.dataHash})');assert got=={'count':len(data['items']),'hash':data['build']['dataHash']},got
   p.locator('[data-frontier-preset]').click();shown=p.locator('.project-card').evaluate_all('(a)=>a.map(x=>x.dataset.project)');assert set(shown)==ids;p.evaluate("()=>document.querySelectorAll('.project-card img').forEach(x=>x.loading='eager')");p.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(x=>x.complete)",timeout=90000);assert p.locator('.project-card img').evaluate_all('(a)=>a.every(x=>x.naturalWidth>0)')
   report['explorers'].append({'path':suffix,**got,'newCards':len(shown),'brokenImages':0});p.screenshot(path=str(out/('tacz-frontier.png' if suffix else 'atlas-frontier.png')))
  p.set_viewport_size({'width':390,'height':844});p.screenshot(path=str(out/'mobile-frontier.png'));b.close()
 report['passed']=True;save(out/'publication.json',report);print(json.dumps(report),flush=True)

def package(directory):
 directory=Path(directory).resolve();directory.mkdir(parents=True,exist_ok=True);files={};skip={'cache','research-cache','working-evidence','fixtures','__pycache__','visual-review'};private={'raw-projects.json','snapshots.json','tail-snapshots.json','candidate-review.json','creator-probes.json','creator-review.json','export.json','export.csv','test-export.json','test-export.csv','collection.json','import-test.json','followup-evidence.json'}
 for p in PARENT.rglob('*'):
  rel=p.relative_to(PARENT)
  if p.is_file() and not any(x in skip for x in rel.parts) and p.name not in private:files['minecraft-gun-mods/'+rel.as_posix()]=p
 files['weapon_inspiration_navigation.py']=DOCS/'weapon_inspiration_navigation.py'
 for pattern in ['Minecraft-Gun*.md','TaCZ-Gunpack*.md']:
  for p in DOCS.glob(pattern):files['wiki/'+p.name]=p
 for name in ['Weapon-Inspirations.md','Weapon-Reference-Library.md']:files['wiki/'+name]=DOCS/name
 p=load(PARENT/'catalog.json');t=load(PARENT/'tacz/catalog.json');delta=load(ROOT/'qa/data-delta.json')
 for folder,data in [(PARENT,p),(PARENT/'tacz',t)]:
  for item in data['items']:
   for media in item.get('media',[]):
    path=(folder/media['src']).resolve();assert path.is_file() and digest(path)==media['sha256'];assert 'minecraft-gun-mods/'+path.relative_to(PARENT.resolve()).as_posix() in files
 intro='# Minecraft Gun Atlas - TaCZ Creator Frontier\n\nExtract this ZIP and open `minecraft-gun-mods/index.html` or `minecraft-gun-mods/tacz/index.html`. Both work offline, without a local server.\n\n'+str(len(p['items']))+' parent records and '+str(len(t['items']))+' TaCZ families. This release adds seven creator/source families, including four editorial study selections. Engineering-test and discontinued source references remain explicit. Every referenced archived image and readable source script is included.\n\nExplore this pass: '+SITE+'tacz/?theme=Frontier+discoveries\nResearch: '+WIKI+PAGE+'\n\nUse Back up my collection to transfer favorites, notes, private ratings and saved views between browsers or hosted/offline origins. All old identities are preserved. No installed Minecraft files are changed.\n\nCreator announcements are not exact release-file verification. Current file/access/version limits are visible; video statistics are not used as gunpack popularity. This is source research, not native Minecraft compatibility or performance testing.\n\nFrozen-input rebuild: `python minecraft-gun-mods/tacz-frontier/build_frontier.py` with requests, beautifulsoup4 and pillow installed. It uses the included qualified source records and does not repeat the search or retrieve mod binaries.\n'
 path=directory/'Minecraft-Gun-Atlas.zip'
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for name,f in sorted(files.items()):z.write(f,name)
  z.writestr('START-HERE.md',intro)
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  for name,f in files.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest(f),name
 receipt={'archive':path.name,'bytes':path.stat().st_size,'sha256':digest(path),'files':len(files)+1,'parentProjects':len(p['items']),'taczFamilies':len(t['items']),'additionalFamilies':delta['additionalFamilies'],'completeReferencedMedia':True,'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash']};save(directory/'RELEASE-VERIFICATION.json',receipt);(directory/'START-HERE.md').write_text(intro);(directory/'SHA256SUMS.txt').write_text(receipt['sha256']+'  '+path.name+'\n');print(json.dumps(receipt),flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('action',choices=['prepare','verify','package']);a.add_argument('target');v=a.parse_args();{'prepare':prepare,'verify':verify,'package':package}[v.action](v.target)
