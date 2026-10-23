#!/usr/bin/env python3
"""Publish and prove the actual Wiki/Pages and a complete portable TaCZ snapshot."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,zipfile
import requests
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/'
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/tacz/'

def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2))
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def browser(pw):
 options={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']};exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
 if exe:options['executable_path']=exe
 return pw.chromium.launch(**options)

def prepare(wiki):
 wiki=Path(wiki);allowed={'TaCZ-Gunpacks.md','Weapon-Inspirations.md','Minecraft-Gun-Mod-Inspirations.md','_Sidebar.md','Home.md'}
 before={p.name:digest(p) for p in wiki.glob('*.md') if p.name not in allowed}
 shutil.copyfile(DOCS/'TaCZ-Gunpacks.md',wiki/'TaCZ-Gunpacks.md')
 start='<!-- tacz-gunpack-lab:start -->';end='<!-- tacz-gunpack-lab:end -->'
 block=start+'\n### TaCZ gunpacks: actual additional guns\n\n- [Dedicated TaCZ Gunpack Lab: popularity, favorites and your ratings]('+SITE+')\n- [Illustrated TaCZ gunpack rankings and methodology](TaCZ-Gunpacks)\n'+end
 for name in allowed-{'TaCZ-Gunpacks.md'}:
  p=wiki/name;assert p.exists(),name;body=p.read_text()
  if start in body and end in body:
   a=body.index(start);b=body.index(end,a)+len(end);body=body[:a]+block+body[b:]
  elif '<!-- minecraft-gun-inspirations:end -->' in body:body=body.replace('<!-- minecraft-gun-inspirations:end -->',block+'\n<!-- minecraft-gun-inspirations:end -->')
  else:body=body.rstrip()+'\n\n'+block+'\n'
  p.write_text(body)
 assert all(digest(wiki/name)==sha for name,sha in before.items())
 save(ROOT/'qa/preserved-wiki.json',{'unchangedPages':len(before),'sha256':before})
 print('Wiki prepared; preserved',len(before),'other pages',flush=True)

def verify():
 d=json.loads((ROOT/'catalog.json').read_text());out=ROOT/'qa/live';out.mkdir(parents=True,exist_ok=True)
 r=requests.get(RAW+'TaCZ-Gunpacks.md',timeout=45);assert r.ok and r.content==(DOCS/'TaCZ-Gunpacks.md').read_bytes(),'Published Wiki bytes differ'
 report={'projects':len(d['items']),'sourceHash':digest(DOCS/'TaCZ-Gunpacks.md'),'dataHash':d['build']['dataHash'],'navigation':{}}
 for name in ['Weapon-Inspirations','Minecraft-Gun-Mod-Inspirations','_Sidebar','Home']:
  r=requests.get(RAW+name+'.md',timeout=30);assert r.ok and 'TaCZ-Gunpacks' in r.text and SITE in r.text,name;report['navigation'][name]=True
 with sync_playwright() as pw:
  b=browser(pw);p=b.new_page(viewport={'width':1440,'height':1050});p.goto(WIKI+'TaCZ-Gunpacks',wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for()
  p.evaluate("()=>document.querySelectorAll('#wiki-body img').forEach(x=>x.loading='eager')")
  p.wait_for_function("()=>[...document.querySelectorAll('#wiki-body img')].every(x=>x.complete)",timeout=180000)
  got=p.evaluate("()=>{const w=document.querySelector('#wiki-body'),ims=[...w.querySelectorAll('img')];return {text:w.innerText,images:ims.length,broken:ims.filter(x=>!x.naturalWidth).map(x=>x.alt),links:[...w.querySelectorAll('a')].map(x=>x.href)};}")
  norm=lambda s:re.sub(r'\s+',' ',s).strip()
  missing=[x['id'] for x in d['items'] if norm(x['name']) not in norm(got['text']) or not any('?item='+x['id'] in u for u in got['links'])]
  report['wiki']={'images':got['images'],'broken':got['broken'],'missing':missing,'endMarker':'End of gunpack gallery' in got['text']}
  assert got['images']==len(d['items']) and not got['broken'] and not missing and report['wiki']['endMarker'],report['wiki']
  p.locator('#wiki-body').scroll_into_view_if_needed();p.screenshot(path=str(out/'wiki-top.png'))
  response=p.goto(SITE,wait_until='domcontentloaded',timeout=90000);assert response and response.status==200,'Dedicated Pages path not deployed';p.wait_for_function('window.ATLAS_TEST',timeout=60000)
  actual=p.evaluate('({count:GUN_ATLAS.items.length,hash:GUN_ATLAS.build.dataHash})');assert actual=={'count':len(d['items']),'hash':d['build']['dataHash']},actual
  report['pages']=actual;p.screenshot(path=str(out/'pages-top.png'));b.close()
 save(out/'publication.json',report);print(json.dumps(report),flush=True)

def package(out):
 out=Path(out).resolve();out.mkdir(parents=True,exist_ok=True);d=json.loads((ROOT/'catalog.json').read_text());files={}
 for p in ROOT.rglob('*'):
  if not p.is_file() or any(part in {'cache','__pycache__','visual-review'} for part in p.relative_to(ROOT).parts):continue
  if p.name in {'export.json','export.csv','collection.json'}:continue
  files['minecraft-gun-mods/tacz/'+p.relative_to(ROOT).as_posix()]=p
 for x in d['items']:
  for m in x['media']:
   p=(ROOT/m['src']).resolve();rel=p.relative_to(PARENT.resolve());files['minecraft-gun-mods/'+rel.as_posix()]=p
 for name in ['catalog.json','app.js','app.css','research.py','collect.py']:
  files['minecraft-gun-mods/'+name]=PARENT/name
 files['minecraft-gun-mods/source-inputs/index.html']=PARENT/'index.html';files['TaCZ-Gunpacks.md']=DOCS/'TaCZ-Gunpacks.md'
 intro='# TaCZ Gunpack Lab\n\nExtract this ZIP and open `minecraft-gun-mods/tacz/index.html`. No server or install is required.\n\nLive explorer: '+SITE+'\nWiki: '+WIKI+'TaCZ-Gunpacks\n\n'+str(len(d['items']))+' gunpack families, real provider rankings, private ratings, favorites, notes, comparisons and portable collection backups. Favorites are browser-local; hosted and file:// origins have separate storage.\n\nThe complete TaCZ snapshot and every referenced image are included. The much larger parent atlas remains available online. Source inputs and scripts are included for reproducibility; source metadata is not native Minecraft compatibility or performance testing.\n\nTo rebuild from frozen inputs, install the documented Python dependencies (requests, beautifulsoup4, pillow), then run `python minecraft-gun-mods/tacz/rebuild_portable.py`. No new discovery is required.\n'
 landing='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Minecraft Gun Atlas</title><h1>Minecraft Gun Atlas</h1><p>This portable package contains the complete dedicated TaCZ collection.</p><p><a href="tacz/">Open the offline TaCZ Gunpack Lab</a></p><p><a href="https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/">Open the full Minecraft Gun Atlas online</a></p></html>'
 rebuild="from pathlib import Path\nimport subprocess,sys\nr=Path(__file__).resolve().parent;p=r.parent;old=(p/'index.html').read_bytes()\ntry:\n (p/'index.html').write_bytes((p/'source-inputs/index.html').read_bytes())\n subprocess.run([sys.executable,str(r/'build_tacz.py')],check=True)\nfinally:(p/'index.html').write_bytes(old)\n"
 path=out/'TaCZ-Gunpack-Lab.zip'
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for name,p in sorted(files.items()):z.write(p,name)
  z.writestr('START-HERE.md',intro);z.writestr('minecraft-gun-mods/index.html',landing);z.writestr('minecraft-gun-mods/tacz/rebuild_portable.py',rebuild)
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  for name,p in files.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest(p),name
 save(out/'RELEASE-VERIFICATION.json',{'archive':path.name,'bytes':path.stat().st_size,'sha256':digest(path),'projects':len(d['items']),'referencedImages':len({m['src'] for x in d['items'] for m in x['media']}),'dataHash':d['build']['dataHash'],'completeReferencedFiles':True})
 (out/'SHA256SUMS.txt').write_text(digest(path)+'  '+path.name+'\n');(out/'START-HERE.md').write_text(intro)
 with zipfile.ZipFile(path) as z:z.extractall(out/'portable-test')
 print('Complete portable archive:',path.stat().st_size,'bytes',flush=True)

def offline(out):
 out=Path(out).resolve();root=out/'portable-test/minecraft-gun-mods/tacz';d=json.loads((root/'catalog.json').read_text());report={'expected':len(d['items']),'checks':[]}
 def check(name,value):report['checks'].append({'name':name,'passed':bool(value)});assert value,name
 with sync_playwright() as pw:
  b=browser(pw);c=b.new_context();c.route('https://**/*',lambda r:r.abort());c.route('http://**/*',lambda r:r.abort());p=c.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto((root/'index.html').as_uri(),wait_until='domcontentloaded');p.wait_for_function('window.ATLAS_TEST')
  check('packaged data identity',p.evaluate('GUN_ATLAS.build.dataHash')==d['build']['dataHash']);check('all offline cards',p.locator('.project-card').count()==len(d['items']))
  p.evaluate("()=>document.querySelectorAll('.project-card img').forEach(x=>x.loading='eager')");p.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(x=>x.complete)",timeout=60000);check('all packaged card images decode',p.locator('.project-card img').evaluate_all('(a)=>a.every(x=>x.naturalWidth>0)'))
  p.locator('.project-card .favorite').first.click();saved=p.evaluate('ATLAS_TEST.favorites');p.locator('.project-card [data-action="detail"]').first.click();p.locator('[data-value="4"]').click();p.locator('[data-close="detailDialog"]').click();p.reload();p.wait_for_function('window.ATLAS_TEST');check('offline favorite restart',p.evaluate('ATLAS_TEST.favorites')==saved)
  p.locator('.project-card [data-action="detail"]').first.click();check('offline private rating restart',p.locator('[data-value="4"]').get_attribute('aria-pressed')=='true');check('no offline errors',not errors);b.close()
 report['passed']=all(x['passed'] for x in report['checks']);save(out/'OFFLINE-VERIFICATION.json',report);print(json.dumps(report),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('action',choices=['prepare','verify','package','offline']);p.add_argument('target',nargs='?');a=p.parse_args()
 {'prepare':lambda:prepare(a.target),'verify':verify,'package':lambda:package(a.target),'offline':lambda:offline(a.target)}[a.action]()
