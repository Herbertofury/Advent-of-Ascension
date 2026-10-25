#!/usr/bin/env python3
"""Real-data acceptance for the additive creator-community catalog, local or deployed."""
from pathlib import Path
import argparse,http.server,json,shutil,socketserver,sys,threading,time
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;TACZ=PARENT/'tacz'
sys.path.insert(0,str(ROOT));import apply_community as u
KEY='aoa.minecraft-guns.collection.v1'

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--url');parser.add_argument('--output');args=parser.parse_args();out=Path(args.output).resolve() if args.output else ROOT/'qa/targeted';out.mkdir(parents=True,exist_ok=True)
 p=u.load(PARENT/'catalog.json');t=u.load(TACZ/'catalog.json');records=u.load(ROOT/'qualified-records.json');base=u.load(ROOT/'baseline.json');ids=set(records);report={'checks':[],'errors':[],'newFamilies':len(ids),'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash']}
 def check(name,value,detail=None):
  report['checks'].append({'name':name,'passed':bool(value),'detail':detail});u.save(out/'report.json',report);assert value,(name,detail)
 check('exact new parent identities',{x['id'] for x in p['items']}-set(base['parent'])==ids)
 check('exact new TaCZ identities',{x['id'] for x in t['items']}-set(base['tacz'])==ids)
 check('all old parent records byte-equivalent',all(u.dh(x)==base['parent'][x['id']] for x in p['items'] if x['id'] in base['parent']))
 check('all old TaCZ records unchanged except ranks',all(u.dh({k:v for k,v in x.items() if k!='popularityRank'})==base['tacz'][x['id']] for x in t['items'] if x['id'] in base['tacz']))
 check('no public star rating manufactured',all(x['metrics']['communityRating'] is None for x in t['items']))
 check('video statistics do not become gunpack popularity',all(all(x['metrics'][k] is None for k in ('downloads','favorites','followers')) for x in t['items'] if x['id'] in ids and x['id'].startswith('bilibili-')))
 coverage=u.load(ROOT/'coverage.json');check('all exact creator-source records accounted for',coverage['exactCreatorMetadataRecords']==191 and sum(coverage['decisionCounts'].values())>=191);check('blocked searches not represented as terminal',coverage['terminalVideoQueries']==0 and coverage['videoQueries']==20)
 check('no unfinished AX50 or Antar counted',not ({'bilibili-BV19EEm6gE1q','bilibili-BV1ArycBnE83'}&{x['id'] for x in t['items']}))
 class Handler(http.server.SimpleHTTPRequestHandler):
  def __init__(self,*a,**kw):super().__init__(*a,directory=str(PARENT),**kw)
  def log_message(self,*a):pass
 server=socketserver.ThreadingTCPServer(('127.0.0.1',0),Handler);server.daemon_threads=True;threading.Thread(target=server.serve_forever,daemon=True).start();site=args.url or 'http://127.0.0.1:'+str(server.server_address[1])+'/'
 try:
  with sync_playwright() as pw:
   exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser');options={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
   if exe:options['executable_path']=exe
   browser=pw.chromium.launch(**options);context=browser.new_context(viewport={'width':1440,'height':1050});page=context.new_page();page.on('pageerror',lambda e:report['errors'].append(str(e)))
   for suffix,data in [('',p),('tacz/',t)]:
    page.goto(site+suffix,wait_until='domcontentloaded',timeout=90000);page.wait_for_function('window.ATLAS_TEST',timeout=60000)
    check(suffix+' exact deployed data identity',page.evaluate('GUN_ATLAS.build.dataHash')==data['build']['dataHash'])
    check(suffix+' all projects remain available in DOM',page.locator('.project-card').count()==len(data['items']))
    check(suffix+' one creator-community filter',page.locator('[data-community-preset]').count()==1)
    started=time.perf_counter();page.locator('[data-community-preset]').click();report.setdefault('performance',[]).append({'path':suffix,'completeCatalogSize':len(data['items']),'filterMilliseconds':round((time.perf_counter()-started)*1000,2)});shown=page.locator('.project-card').evaluate_all('(a)=>a.map(x=>x.dataset.project)');check(suffix+' exact new family filter',set(shown)==ids)
    page.evaluate("()=>document.querySelectorAll('.project-card img').forEach(x=>x.loading='eager')");page.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(x=>x.complete)",timeout=90000)
    check(suffix+' all source previews load',page.locator('.project-card img').count()==len(ids) and page.locator('.project-card img').evaluate_all('(a)=>a.every(x=>x.naturalWidth>0)'))
    for key in sorted(ids):
     card=page.locator('.project-card[data-project="'+key+'"]');check(suffix+' unique new card '+key,card.count()==1)
     card.locator('[data-action="detail"]').click();detail=page.locator('#detailDialog');check(suffix+' access and limits visible '+key,records[key]['item']['access'] in detail.inner_text() and records[key]['item']['cautions'][0] in detail.inner_text());page.locator('[data-close="detailDialog"]').click()
    page.screenshot(path=str(out/('tacz-community.png' if suffix else 'atlas-community.png')))
    page.locator('[data-frontier-preset]').click();check(suffix+' earlier seven creator-frontier identities preserved',page.locator('.project-card').count()==7);page.locator('[data-deep-preset="all"]').click();check(suffix+' earlier 46 discoveries preserved',page.locator('.project-card').count()==46)
    page.locator('[data-creator-preset="new"]').click();check(suffix+' earlier creator-discovery filter preserved',page.locator('.project-card').count()==(4 if suffix else 5))
   page.goto(site+'tacz/?theme=Community+discoveries',wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('community deep link exact',page.locator('.project-card').count()==len(ids))
   key='bilibili-BV1ihycY2E3s';old=next(iter(base['tacz']))
   page.evaluate('([k,old])=>localStorage.setItem(k,JSON.stringify({schemaVersion:1,favorites:[old,"unlisted-preserved-id"],notes:{[old]:"Original note"},ratings:{[old]:4},views:[],taczViews:[]}))',[KEY,old]);page.reload();page.wait_for_function('window.ATLAS_TEST')
   page.locator('.project-card[data-project="'+key+'"] .favorite').click();page.locator('.project-card[data-project="'+key+'"] [data-action="detail"]').click();page.locator('#projectNotes').fill('Creator-frontier design note');page.locator('[data-rate="'+key+'"][data-value="5"]').click();page.locator('[data-close="detailDialog"]').click();page.reload();page.wait_for_function('window.ATLAS_TEST')
   saved=page.evaluate('(k)=>JSON.parse(localStorage.getItem(k))',KEY)
   check('old, new and unknown favorites survive restart',all(x in saved['favorites'] for x in [key,old,'unlisted-preserved-id']))
   check('old and new notes survive restart',saved['notes'].get(old)=='Original note' and saved['notes'].get(key)=='Creator-frontier design note')
   check('private ratings coexist and survive restart',saved['ratings'].get(old)==4 and saved['ratings'].get(key)==5)
   for key,word in [('bilibili-BV1qinS6WEHy','open test'),('bilibili-BV1LkfTYeE5o','historical source'),('bilibili-BV1ihycY2E3s','login'),('bilibili-BV1fkdiYLEJy','imc-7274')]:
    page.goto(site+'tacz/?item='+key,wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('source limitation remains clear '+key,word in page.locator('#detailDialog').inner_text().lower());page.keyboard.press('Escape')
   page.goto(site+'tacz/?theme=Community+discoveries',wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');page.set_viewport_size({'width':390,'height':844});check('mobile no page overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'));page.screenshot(path=str(out/'mobile-community.png'))
   check('no browser exceptions',not report['errors'],report['errors']);browser.close()
 finally:server.shutdown();server.server_close()
 report['passed']=all(x['passed'] for x in report['checks']);u.save(out/'report.json',report);print(json.dumps({'checks':len(report['checks']),'passed':report['passed']}),flush=True)
if __name__=='__main__':main()
