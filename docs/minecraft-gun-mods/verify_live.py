#!/usr/bin/env python3
"""Exercise the actual GitHub Wiki and Pages publication, not repo-side mirrors."""
from __future__ import annotations
import hashlib,json,shutil,sys,time
from pathlib import Path
from urllib.parse import unquote
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import requests
ROOT=Path(__file__).resolve().parent
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/'
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'

def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')

def run():
 manifest=json.loads((ROOT/'wiki-manifest.json').read_text());data=json.loads((ROOT/'catalog.json').read_text());index={x['id']:x for x in data['items']};out=ROOT/'qa'/'live';out.mkdir(parents=True,exist_ok=True)
 evidence={'site':SITE,'expectedProjects':len(index),'wikiPages':[],'browserPages':[],'navigation':{},'errors':[]}
 session=requests.Session();session.headers['User-Agent']='AoA-Catalog-Publication-Verification/1.0'
 # Raw Wiki hashes prove exact source publication; separate browser checks below prove rendered user paths.
 for entry in manifest['pages']:
  name=entry['name'];response=session.get(RAW+name+'.md',timeout=35)
  local=(ROOT.parent/(name+'.md')).read_bytes()
  ok=response.ok and response.content==local
  evidence['wikiPages'].append({'page':name,'status':response.status_code,'bytes':len(response.content),'sha256':hashlib.sha256(response.content).hexdigest(),'matchesSource':ok})
  if not ok:evidence['errors'].append(name+': raw Wiki differs')
 for name in ('Home','_Sidebar','Weapon-Inspirations','Weapon-Reference-Library'):
  rr=session.get(RAW+name+'.md',timeout=35)
  evidence['navigation'][name]={'status':rr.status_code,'hasMinecraftLink':'Minecraft-Gun-Mod-Inspirations' in rr.text,'hasExplorer':SITE in rr.text}
  if not rr.ok or 'Minecraft-Gun-Mod-Inspirations' not in rr.text:evidence['errors'].append(name+': missing navigation')
 save(out/'publication.json',evidence)
 assert not evidence['errors'],evidence['errors']
 with sync_playwright() as pw:
  exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
  options={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
  if exe:options['executable_path']=exe
  browser=pw.chromium.launch(**options);page=browser.new_page(viewport={'width':1440,'height':1000})
  for number,group in enumerate(manifest['collections']):
   slug=group['page'];page.goto(WIKI+slug,wait_until='domcontentloaded',timeout=90000);page.locator('#wiki-body').wait_for(timeout=30000)
   page.evaluate("() => document.querySelectorAll('#wiki-body img').forEach(x=>x.loading='eager')")
   expected=sum(bool(index[key].get('media')) for key in group['ids'])
   if expected:
    page.wait_for_function("() => {const a=[...document.querySelectorAll('#wiki-body img')].filter(x=>(x.getAttribute('data-canonical-src')||x.src).includes('/minecraft-gun-mods/assets/'));return a.length>0&&a.every(x=>x.complete);}",timeout=180000)
   got=page.evaluate("() => {const b=document.querySelector('#wiki-body');const a=[...b.querySelectorAll('img')].filter(x=>(x.getAttribute('data-canonical-src')||x.src).includes('/minecraft-gun-mods/assets/'));return {images:a.length,decoded:a.filter(x=>x.naturalWidth>0).length,broken:a.filter(x=>!x.naturalWidth).map(x=>x.alt),text:b.innerText,links:[...b.querySelectorAll('a')].map(x=>x.href)};}")
   missing=[key for key in group['ids'] if index[key]['name'] not in got['text']]
   record={'page':slug,'projects':len(group['ids']),'expectedImages':expected,'images':got['images'],'decoded':got['decoded'],'broken':got['broken'],'missing':missing,'endMarker':'End of gallery' in got['text']}
   evidence['browserPages'].append(record);save(out/'publication.json',evidence)
   assert got['images']==got['decoded']==expected and not missing and record['endMarker'],record
   if number<4:page.locator('#wiki-body').scroll_into_view_if_needed();page.screenshot(path=str(out/(slug+'.png')))
   print('Live Wiki verified',slug,len(group['ids']),'projects',expected,'images',flush=True)
  page.goto(WIKI+'Minecraft-Gun-Mod-Inspirations',wait_until='domcontentloaded',timeout=90000);page.locator('#wiki-body').wait_for();page.screenshot(path=str(out/'wiki-index.png'))
  # Verify canonical Pages data, not just an HTTP 200 from an old deployment.
  response=page.goto(SITE,wait_until='domcontentloaded',timeout=90000);page.wait_for_function('window.ATLAS_TEST',timeout=60000)
  actual=page.evaluate('({count:window.GUN_ATLAS.items.length,hash:window.GUN_ATLAS.build.dataHash,errors:document.querySelectorAll(".warning").length})')
  evidence['pagesExplorer']={'url':SITE,'httpStatus':response.status if response else None,**actual}
  assert actual['count']==len(index) and actual['hash']==data['build']['dataHash'],evidence['pagesExplorer']
  page.screenshot(path=str(out/'explorer-desktop.png'))
  page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(out/'explorer-mobile.png'))
  evidence['checkedAt']=__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat();save(out/'publication.json',evidence);browser.close()
 print(json.dumps({'projects':len(index),'wikiPages':len(evidence['wikiPages']),'illustratedCollections':len(evidence['browserPages']),'decodedWikiImages':sum(x['decoded'] for x in evidence['browserPages']),'errors':evidence['errors']}),flush=True)
 return evidence
if __name__=='__main__':run()
