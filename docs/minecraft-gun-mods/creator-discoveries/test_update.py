#!/usr/bin/env python3
"""Regression checks for the exact additive creator-discovery update."""
from __future__ import annotations
import argparse,hashlib,http.server,json,re,shutil,socketserver,sys,tempfile,threading
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent;TACZ=PARENT/'tacz'
sys.path[:0]=[str(ROOT),str(DOCS)]
import build_update as u
import weapon_inspiration_navigation as nav
KEY='aoa.minecraft-guns.collection.v1'

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--wiki',required=True);parser.add_argument('--url');args=parser.parse_args()
 out=ROOT/'qa/targeted';out.mkdir(parents=True,exist_ok=True);report={'checks':[],'errors':[]}
 def check(name,value,details=None):
  print('CHECK',name,bool(value),flush=True);report['checks'].append({'name':name,'passed':bool(value),'details':details});u.save(out/'report.json',report);assert value,(name,details)
 parent=u.load(PARENT/'catalog.json');tacz=u.load(TACZ/'catalog.json');baseline=u.load(ROOT/'baseline.json');spec=u.load(ROOT/'manifest.json')
 check('five new parent records, no removed IDs',len(parent['items'])==baseline['parentCount']+5 and set(baseline['parent'])<={x['id'] for x in parent['items']})
 check('four new TaCZ families, no paid Bedrock contamination',len(tacz['items'])==baseline['taczCount']+4 and not any(x['edition']!='Java' for x in tacz['items']))
 before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in [PARENT/'catalog.json',TACZ/'catalog.json',PARENT/'app.js',TACZ/'app.js',PARENT/'index.html',TACZ/'index.html']}
 u.refresh()
 check('catalog and controls are idempotent',all(hashlib.sha256(p.read_bytes()).hexdigest()==sha for p,sha in before.items()))
 wiki=Path(args.wiki)
 nav.apply(wiki);check('canonical navigation idempotent',not nav.apply(wiki)['changedPages'])
 sidebar=(wiki/'_Sidebar.md').read_text();owned=sidebar[sidebar.index(nav.START):sidebar.index(nav.END)]
 check('single hub heading, no hub child',owned.count('](Weapon-Inspirations)')==1 and not re.search(r'^\s*- \[Weapon inspirations\]',owned,re.M|re.I))
 check('one flat collection list',not re.search(r'^  +- ',owned,re.M))
 check('placed beside visual references',sidebar.index(nav.START)<sidebar.index('<details><summary>Optional weapon upgrade</summary>'))
 check('legacy duplicate section removed','additional-weapon-research:' not in sidebar)
 # Execute the current canonical publishers, not a mock menu implementation.
 with tempfile.TemporaryDirectory() as temp:
  testwiki=Path(temp)/'wiki';shutil.copytree(wiki,testwiki)
  u.module('parent_publisher',PARENT/'build.py').publish(testwiki)
  u.module('tacz_publisher',TACZ/'publish_tacz.py').prepare(testwiki)
  check('parent and TaCZ republishes do not recreate nesting',(testwiki/'_Sidebar.md').read_bytes()==(wiki/'_Sidebar.md').read_bytes())
  check('publisher outputs already normalized',not nav.apply(testwiki)['changedPages'])
 # UI requests are served by the exact on-disk production source.
 class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self,*a,**kw):super().__init__(*a,directory=str(PARENT),**kw)
  def log_message(self,*a):pass
 server=socketserver.ThreadingTCPServer(('127.0.0.1',0),Handler);server.daemon_threads=True;threading.Thread(target=server.serve_forever,daemon=True).start()
 base=args.url or 'http://127.0.0.1:'+str(server.server_address[1])+'/'
 try:
  with sync_playwright() as pw:
   exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser');options={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
   if exe:options['executable_path']=exe
   b=pw.chromium.launch(**options);context=b.new_context(viewport={'width':1440,'height':1000});p=context.new_page();p.on('pageerror',lambda e:report['errors'].append(str(e)))
   for suffix,data,count in [('',parent,5),('tacz/',tacz,4)]:
    p.goto(base+suffix,wait_until='domcontentloaded',timeout=90000);p.wait_for_function('window.ATLAS_TEST')
    check(suffix+' full dataset loaded',p.evaluate('GUN_ATLAS.items.length')==len(data['items']))
    check(suffix+' one discovery nav link',p.locator('#creatorDiscoveriesLink').count()==1)
    p.locator('[data-creator-preset="new"]').click();check(suffix+' exact new-discovery filter',p.locator('.project-card').count()==count)
    for x in spec['newTaCZ']:
     card=p.locator('[data-project="'+x['id']+'"]');check(suffix+' new pack present '+x['id'],card.count()==1)
     im=card.locator('img').first;im.scroll_into_view_if_needed();p.wait_for_function('(im)=>im.complete',arg=im.element_handle());check(suffix+' new image decodes '+x['id'],im.evaluate('(im)=>im.naturalWidth>0'))
    p.screenshot(path=str(out/('tacz-new.png' if suffix else 'atlas-new.png')))
    key=spec['newTaCZ'][0]['id'];p.locator('[data-project="'+key+'"] .favorite').click();p.locator('[data-project="'+key+'"] [data-action="detail"]').click()
    check(suffix+' access label visible','Free public' in p.locator('#detailDialog .creator-access').inner_text())
    p.locator('#projectNotes').fill('Creator discovery note retained.');p.locator('[data-close="detailDialog"]').click()
    p.locator('[data-creator-preset="channels"]').click();expected=sum('Creator channels' in x['themes'] for x in data['items'])
    check(suffix+' creator filter matches exact evidence',p.locator('.project-card').count()==expected)
    gamma=p.locator('[data-project="cf-1585190"]');gamma.locator('[data-action="detail"]').click();check(suffix+' support is optional, not a paid download','optional Patreon support' in p.locator('#detailDialog .creator-access').inner_text());p.keyboard.press('Escape')
    if not suffix:
     p.goto(base+'?item=patreon-159166702',wait_until='domcontentloaded');p.wait_for_function('window.ATLAS_TEST');check('paid Bedrock identity explicit','Bedrock' in p.locator('#detailDialog').inner_text() and 'Paid creator release' in p.locator('#detailDialog .creator-access').inner_text());check('unknown paid download count not fabricated','Not published' in p.locator('#detailDialog .detail-meta').inner_text());p.keyboard.press('Escape')
   p.goto(base+'tacz/?item='+spec['newTaCZ'][0]['id'],wait_until='domcontentloaded');p.wait_for_function('window.ATLAS_TEST');check('shared note survived both explorers',p.locator('#projectNotes').input_value()=='Creator discovery note retained.');p.keyboard.press('Escape')
   p.set_viewport_size({'width':390,'height':844});p.locator('[data-creator-preset="new"]').click();check('mobile no horizontal overflow',p.evaluate('document.documentElement.scrollWidth<=innerWidth+1'));p.screenshot(path=str(out/'mobile-new.png'))
   check('no script exceptions',not report['errors']);b.close()
 finally:server.shutdown()
 report['passed']=all(x['passed'] for x in report['checks']);u.save(out/'report.json',report);print(json.dumps(report),flush=True)
if __name__=='__main__':main()
