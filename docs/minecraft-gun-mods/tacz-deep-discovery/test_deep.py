#!/usr/bin/env python3
"""Targeted real-browser acceptance for the additive TaCZ hidden-gem expansion."""
from __future__ import annotations
import argparse,hashlib,http.server,json,re,shutil,socketserver,sys,tempfile,threading
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent;TACZ=PARENT/'tacz'
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(DOCS));import build_deep as u;import weapon_inspiration_navigation as nav
KEY='aoa.minecraft-guns.collection.v1'

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--url');parser.add_argument('--wiki');parser.add_argument('--output');args=parser.parse_args()
 out=Path(args.output).resolve() if args.output else ROOT/'qa/targeted';out.mkdir(parents=True,exist_ok=True)
 parent=u.load(PARENT/'catalog.json');tacz=u.load(TACZ/'catalog.json');before=u.load(ROOT/'baseline.json');records={**u.load(ROOT/'qualified-records.json',{}),**u.load(ROOT/'extra-records.json',{})};ids=set(records);report={'checks':[],'errors':[],'newFamilies':len(ids),'parentDataHash':parent['build']['dataHash'],'taczDataHash':tacz['build']['dataHash']}
 def check(name,value,detail=None):
  report['checks'].append({'name':name,'passed':bool(value),'detail':detail});u.save(out/'report.json',report);assert value,(name,detail)
 check('all earlier parent identities preserved',set(before['parent'])<={x['id'] for x in parent['items']})
 check('all earlier TaCZ identities preserved',set(before['tacz'])<={x['id'] for x in tacz['items']})
 check('exact additional TaCZ identities',set(x['id'] for x in tacz['items'])-set(before['tacz'])==ids-set(before['tacz']))
 check('only Java content in TaCZ collection',all(x['edition']=='Java' for x in tacz['items']))
 check('no invented community ratings',all(x['metrics']['communityRating'] is None for x in tacz['items']))
 check('source prototype not counted as a published firearm pack','gh-967910314' not in {x['id'] for x in tacz['items']})
 paths=[PARENT/'catalog.json',TACZ/'catalog.json',PARENT/'app.js',TACZ/'app.js',PARENT/'index.html',TACZ/'index.html'];hashes={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
 u.module('deep_rebuild_regression',PARENT/'creator-discoveries/build_update.py').refresh()
 check('original rebuild retains all accepted discoveries and controls',all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in hashes.items()))
 if args.wiki:
  wiki=Path(args.wiki);nav.apply(wiki);check('navigation remains idempotent',not nav.apply(wiki)['changedPages'])
  sidebar=(wiki/'_Sidebar.md').read_text();owned=sidebar[sidebar.index(nav.START):sidebar.index(nav.END)]
  check('one flat Weapon Inspirations section',owned.count('](Weapon-Inspirations)')==1 and not re.search(r'^\s*- \[Weapon inspirations\]',owned,re.M|re.I) and not re.search(r'^  +- ',owned,re.M))
  with tempfile.TemporaryDirectory() as temp:
   clone=Path(temp)/'wiki';shutil.copytree(wiki,clone)
   u.module('deep_parent_publisher',PARENT/'build.py').publish(clone);u.module('deep_tacz_publisher',TACZ/'publish_tacz.py').prepare(clone)
   check('normal publishers preserve the organized sidebar',(clone/'_Sidebar.md').read_bytes()==(wiki/'_Sidebar.md').read_bytes())
 class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self,*a,**kw):super().__init__(*a,directory=str(PARENT),**kw)
  def log_message(self,*a):pass
 server=socketserver.ThreadingTCPServer(('127.0.0.1',0),Handler);server.daemon_threads=True;threading.Thread(target=server.serve_forever,daemon=True).start();base=args.url or 'http://127.0.0.1:'+str(server.server_address[1])+'/'
 try:
  with sync_playwright() as pw:
   exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser');opts={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
   if exe:opts['executable_path']=exe
   browser=pw.chromium.launch(**opts);context=browser.new_context(viewport={'width':1440,'height':1000});page=context.new_page();page.on('pageerror',lambda e:report['errors'].append(str(e)))
   for suffix,data in [('',parent),('tacz/',tacz)]:
    page.goto(base+suffix,wait_until='domcontentloaded',timeout=90000);page.wait_for_function('window.ATLAS_TEST',timeout=60000)
    check(suffix+' exact live dataset',page.evaluate('GUN_ATLAS.build.dataHash')==data['build']['dataHash'])
    check(suffix+' one deep-discovery button',page.locator('[data-deep-preset="all"]').count()==1)
    page.locator('[data-deep-preset="all"]').click();shown=page.locator('.project-card').evaluate_all('(a)=>a.map(x=>x.dataset.project)');check(suffix+' exact discoveries, no unrelated utility padding',set(shown)==ids)
    images=page.locator('.project-card img');page.evaluate("()=>document.querySelectorAll('.project-card img').forEach(x=>x.loading='eager')");page.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(x=>x.complete)",timeout=90000)
    broken=images.evaluate_all('(a)=>a.filter(x=>!x.naturalWidth).map(x=>x.alt)');check(suffix+' every available new preview decodes',not broken,broken)
    for key in sorted(ids):
     card=page.locator('.project-card[data-project="'+key+'"]');check(suffix+' exact new card '+key,card.count()==1 and card.locator('[data-action="detail"]').count()==1)
    page.screenshot(path=str(out/('tacz-deep.png' if suffix else 'atlas-deep.png')))
    page.locator('[data-deep-preset="gems"]').click();expected={x['id'] for x in data['items'] if 'Hidden gems' in x.get('themes',[])};check(suffix+' editorial gem filter exact',set(page.locator('.project-card').evaluate_all('(a)=>a.map(x=>x.dataset.project)'))==expected)
    # Previous discovered packs retain their own filter and source identity.
    page.locator('[data-creator-preset="new"]').click();check(suffix+' earlier discovery filter preserved',page.locator('.project-card').count()==(4 if suffix else 5))
    page.locator('#resetFilters').click()
   page.goto(base+'tacz/?theme=Deep+discoveries',wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('deep links retain all discovery identities',page.locator('.project-card').count()==len(ids))
   key=sorted(ids)[0];old=next(iter(before['tacz']))
   page.evaluate('([k,old])=>localStorage.setItem(k,JSON.stringify({schemaVersion:1,favorites:[old,"unknown-preserved-id"],notes:{[old]:"Existing note"},ratings:{[old]:4},views:[],taczViews:[]}))',[KEY,old]);page.reload();page.wait_for_function('window.ATLAS_TEST')
   page.locator('.project-card[data-project="'+key+'"] .favorite').click();page.locator('.project-card[data-project="'+key+'"] [data-action="detail"]').click();page.locator('#projectNotes').fill('Deep discovery note');page.locator('[data-rate="'+key+'"][data-value="5"]').click();page.locator('[data-close="detailDialog"]').click();page.reload();page.wait_for_function('window.ATLAS_TEST')
   saved=page.evaluate('(k)=>JSON.parse(localStorage.getItem(k))',KEY)
   check('new favorite coexists with old and unknown favorites',all(x in saved['favorites'] for x in [key,old,'unknown-preserved-id']))
   check('old and new notes preserved',saved['notes'].get(old)=='Existing note' and saved['notes'].get(key)=='Deep discovery note')
   check('old and new private ratings preserved',saved['ratings'].get(old)==4 and saved['ratings'].get(key)==5)
   page.goto(base+'tacz/?item=cf-1307174',wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('TWX free trial does not masquerade as full free edition','trial' in page.locator('#detailDialog').inner_text().lower())
   page.keyboard.press('Escape');page.goto(base+'tacz/?item=cf-1085368',wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('Menophage explicit legacy restriction retained','not compatible with TaCZ 1.1.4' in page.locator('#detailDialog').inner_text())
   page.keyboard.press('Escape');page.goto(base+'tacz/?theme=Hidden+gems',wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');page.set_viewport_size({'width':390,'height':844});check('mobile has no horizontal page overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'));page.screenshot(path=str(out/'mobile-gems.png'))
   check('no browser exceptions',not report['errors'],report['errors']);browser.close()
 finally:server.shutdown();server.server_close()
 report['passed']=all(x['passed'] for x in report['checks']);u.save(out/'report.json',report);print(json.dumps({'checks':len(report['checks']),'passed':report['passed'],'families':len(ids)}),flush=True)
if __name__=='__main__':main()
