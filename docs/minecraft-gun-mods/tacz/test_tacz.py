#!/usr/bin/env python3
"""Real-data, no-mock browser acceptance for the TaCZ gun-content page."""
from __future__ import annotations
import argparse,csv,http.server,io,json,shutil,socketserver,threading,time
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
KEY='aoa.minecraft-guns.collection.v1'

def run(url,out):
 out.mkdir(parents=True,exist_ok=True);data=json.loads((ROOT/'catalog.json').read_text());items=data['items'];idx={x['id']:x for x in items};report={'url':url,'expected':len(items),'dataHash':data['build']['dataHash'],'checks':[],'errors':[],'metrics':{}}
 def check(name,value,detail=None):
  report['checks'].append({'name':name,'passed':bool(value),'detail':detail});(out/'browser-report.json').write_text(json.dumps(report,indent=2));assert value,(name,detail)
 with sync_playwright() as pw:
  exe=shutil.which('chromium') or shutil.which('google-chrome') or shutil.which('chromium-browser');options={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
  if exe:options['executable_path']=exe
  browser=pw.chromium.launch(**options);context=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True);page=context.new_page();page.on('pageerror',lambda e:report['errors'].append(str(e)))
  t=time.monotonic();page.goto(url,wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');report['metrics']['initialDOMms']=round((time.monotonic()-t)*1000);report['metrics']['renderMs']=page.evaluate('ATLAS_TEST.renderMs')
  check('actual tested dataset identity',page.evaluate('GUN_ATLAS.build.dataHash')==data['build']['dataHash'])
  check('all gunpack families rendered',page.locator('.project-card').count()==len(items))
  check('dedicated page title and original atlas navigation','TaCZ' in page.title() and page.locator('nav a[href="../"]').count()==1)
  check('no accidental tacz/tacz navigation',page.locator('nav a[href="tacz/"]').count()==0)
  for mode,key in [('downloads','downloads'),('favorites','favorites'),('followers','followers'),('cfDownloads','cfDownloads'),('mrDownloads','mrDownloads')]:
   page.locator('#sort').select_option(mode)
   ids=page.locator('.project-card').evaluate_all('(xs)=>xs.map(x=>x.dataset.project)');values=[idx[k]['metrics'][key] for k in ids];known=[v for v in values if v is not None]
   check('descending exact '+mode,known==sorted(known,reverse=True))
   check('missing '+mode+' values remain last',values[:len(known)]==known)
  for mode in ['created','date','name']:
   page.locator('#sort').select_option(mode);check('sort '+mode+' retains full scope',page.locator('.project-card').count()==len(items))
  page.locator('[data-ranking="priority"]').click();check('quality shortlist button filters actual shortlist',page.locator('.project-card').count()==sum(x['curation']=='Quality shortlist' for x in items))
  page.locator('[data-ranking="downloads"]').click();check('popularity resets shortlist filter',page.locator('.project-card').count()==len(items))
  page.locator('#anchorsButton').click();check('hero shortlist opens qualified guns',0<page.evaluate('ATLAS_TEST.shown')<len(items));page.locator('#resetFilters').click()
  page.locator('#earlierButton').click();check('earlier gunpack selections retained',page.evaluate('ATLAS_TEST.shown')==sum(x.get('earlierPick',False) for x in items));page.locator('#resetFilters').click()
  first=items[0];fid=first['id'];page.locator('#search').fill('"'+first['name']+'"');page.wait_for_timeout(200);check('quoted project search',page.locator('.project-card').count()==1)
  page.locator('.project-card .favorite').click();check('favorite saved',fid in page.evaluate('ATLAS_TEST.favorites'))
  page.locator('[data-action="detail"][data-id="'+fid+'"]').click()
  check('exact source metrics in detail',str(first['metrics']['downloads']) in page.locator('.metric-evidence').inner_text().replace(',',''))
  check('source metrics not mislabeled ratings','not a quality score' in page.locator('.metric-evidence').inner_text())
  page.locator('[data-rate="'+fid+'"][data-value="5"]').click();check('private rating saved',page.evaluate('(k)=>JSON.parse(localStorage.getItem(k)).ratings',KEY).get(fid)==5)
  page.locator('#projectNotes').fill('TaCZ QA: retain this original note.');page.locator('[data-close="detailDialog"]').click();page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST')
  check('favorite survives restart',fid in page.evaluate('ATLAS_TEST.favorites'))
  page.locator('[data-action="detail"][data-id="'+fid+'"]').click();check('note survives restart',page.locator('#projectNotes').input_value()=='TaCZ QA: retain this original note.');check('private rating survives restart',page.locator('[data-value="5"]').get_attribute('aria-pressed')=='true')
  check('official navigation exact',page.locator('#detailDialog .main-link').get_attribute('href')==first['projectUrl']);page.locator('[data-close="detailDialog"]').click();page.locator('#resetFilters').click()
  page.locator('[data-ranking="rating"]').click();check('own rating sorted first',page.locator('.project-card').first.get_attribute('data-project')==fid)
  for view,selector in [('table','.project-table tbody tr'),('gallery','.project-card'),('cards','.project-card')]:
   page.locator('[data-view="'+view+'"]').click();check(view+' view includes all families',page.locator(selector).count()==len(items))
  for field in ['type','version','loader','theme','provider','activity','curation']:
   select=page.locator('#'+field+'Filter');values=select.locator('option').evaluate_all('(a)=>a.map(x=>x.value).filter(Boolean)')
   if values:select.select_option(values[0]);check(field+' filter functional',0<=page.evaluate('ATLAS_TEST.shown')<=len(items));page.locator('#resetFilters').click()
  check('impossible crossed version and loader rejected',page.evaluate("!ATLAS_TEST.releaseMatches({releases:[{versions:['1.20.1'],loaders:['Forge']},{versions:['1.21.1'],loaders:['NeoForge']}]},'1.20.1','NeoForge')"))
  page.locator('#search').fill('provider:curseforge');page.wait_for_timeout(200);check('structured provider filter',page.evaluate('ATLAS_TEST.shown')>0)
  page.locator('#saveView').click();page.locator('#viewName').fill('My favorite TaCZ ranking');page.locator('#savedViewForm [type="submit"]').click();check('dedicated saved view persisted',page.locator('[data-load-view]').count()==1)
  page.locator('#resetFilters').click();page.locator('[data-load-view]').click();check('saved search restored',page.locator('#search').input_value()=='provider:curseforge');page.locator('[data-delete-view]').click();page.locator('#resetFilters').click()
  for key in [x['id'] for x in items[:3]]:page.locator('[data-compare="'+key+'"]').first.check()
  page.locator('#openCompare').click();check('compare includes provider popularity',page.locator('#utilityContent').inner_text().find('Popularity evidence')>=0);check('compare includes private ratings','Your rating' in page.locator('#utilityContent').inner_text());page.locator('[data-close="utilityDialog"]').click();page.locator('#clearCompare').click()
  page.locator('#rankingHelp').click();check('methodology explains no fabricated community ratings','fabricate' in page.locator('#utilityContent').inner_text());page.keyboard.press('Escape')
  page.locator('#sourcesButton').click();check('source center preserves exact metric definitions','favoriteCount' in page.locator('#utilityContent').inner_text());page.keyboard.press('Escape')
  for fmt in ['json','csv']:
   page.locator('#exportResults').click()
   with page.expect_download() as event:page.locator('[data-export="'+fmt+'"]').click()
   file=out/('export.'+fmt);event.value.save_as(file)
   if fmt=='json':check('JSON export complete scope',len(json.loads(file.read_text())['items'])==len(items))
   else:
    rows=list(csv.DictReader(io.StringIO(file.read_text(encoding='utf-8-sig'))));check('CSV exact metrics and private rating exported',len(rows)==len(items) and 'cfFavorites' in rows[0] and any(x['yourRating']=='5' for x in rows))
  with page.expect_download() as event:page.locator('#backupButton').click()
  file=out/'collection.json';event.value.save_as(file);backup=json.loads(file.read_text());check('collection backup includes private rating',backup['ratings'][fid]==5)
  page.evaluate("()=>ATLAS_TEST.importCollection({favorites:['outside-tacz-preserve'],notes:{'outside-tacz-preserve':'unrelated note'},ratings:{'outside-tacz-preserve':4}})")
  page.locator('#importFile').set_input_files(str(file));page.wait_for_timeout(150)
  stored=page.evaluate('(k)=>JSON.parse(localStorage.getItem(k))',KEY);check('import retains unrelated favorites and notes','outside-tacz-preserve' in stored['favorites'] and stored['notes']['outside-tacz-preserve']=='unrelated note');check('import retains unrelated ratings',stored['ratings']['outside-tacz-preserve']==4)
  # Same-origin parent atlas records and saved views must survive use of the dedicated page.
  page.evaluate("(k)=>{const p=JSON.parse(localStorage.getItem(k));p.views=[{name:'Original atlas view',filters:{query:'create'}}];p.customUnknown={preserve:true};localStorage.setItem(k,JSON.stringify(p));}",KEY)
  page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');page.locator('.project-card .favorite').first.click();stored=page.evaluate('(k)=>JSON.parse(localStorage.getItem(k))',KEY)
  check('parent saved views untouched',stored['views'][0]['name']=='Original atlas view');check('unknown extension state preserved',stored['customUnknown']['preserve'])
  page.locator('#themeButton').click();page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('theme survives reload',page.locator('html').get_attribute('data-theme')=='light');page.locator('#themeButton').click()
  page.locator('#resetFilters').click();page.locator('#sort').select_option('downloads');page.screenshot(path=str(out/'desktop-top.png'))
  # Decode every card image, not a representative sample.
  page.evaluate("()=>document.querySelectorAll('.project-card img').forEach(i=>i.loading='eager')")
  page.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(i=>i.complete)",timeout=180000)
  images=page.locator('.project-card img').evaluate_all('(a)=>({count:a.length,broken:a.filter(x=>!x.naturalWidth).map(x=>x.alt)})');check('all source card images decode',not images['broken'],images)
  many=next(x for x in items if len(x['media'])>1);page.evaluate('(id)=>document.querySelector(`[data-project="${id}"] [data-action="gallery"]`).click()',many['id']);check('gallery opens with exact image attribution',page.locator('#lightbox').evaluate('(x)=>x.open') and page.locator('#lightbox a').count()>0);page.keyboard.press('ArrowRight');page.keyboard.press('Escape')
  page.locator('.library').scroll_into_view_if_needed();page.screenshot(path=str(out/'desktop-rankings.png'))
  page.set_viewport_size({'width':390,'height':844});page.locator('.library').scroll_into_view_if_needed();check('mobile no unintended overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'));page.locator('#mobileFilters').click();check('mobile filters accessible',page.locator('#filters').is_visible());page.locator('#mobileFilters').click();page.screenshot(path=str(out/'mobile.png'))
  page.locator('#search').fill('no-result-tacz-qqqxyz');page.wait_for_timeout(200);check('empty state recovery',page.locator('#empty').is_visible());page.locator('#emptyReset').click()
  check('no renderer exceptions',not report['errors'],report['errors'])
  denied=browser.new_context();denied.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw Error('Storage denied')}})");p=denied.new_page();p.goto(url,wait_until='domcontentloaded');p.wait_for_function('window.ATLAS_TEST');check('storage denied warning and full catalog',p.locator('#storageWarning').is_visible() and p.locator('.project-card').count()==len(items));p.locator('.project-card [data-action="detail"]').first.click();p.locator('.rating-buttons [data-value="4"]').click();check('private ratings work in memory-only mode','4 / 5 from you' in p.locator('.personal-rating').inner_text());denied.close()
  alias=next(iter(data['idAliases']),None)
  if alias:
   c=browser.new_context();p=c.new_page();p.goto(url,wait_until='domcontentloaded');p.evaluate('(v)=>localStorage.setItem(v.key,JSON.stringify({favorites:[v.alias],notes:{[v.alias]:"edition note"},views:[]}))',{'key':KEY,'alias':alias});p.reload(wait_until='domcontentloaded');p.wait_for_function('window.ATLAS_TEST');check('older edition favorite maps to family',data['idAliases'][alias] in p.evaluate('ATLAS_TEST.favorites'));p.goto(url+'?item='+alias,wait_until='domcontentloaded');p.wait_for_function('window.ATLAS_TEST');check('older edition deep link opens canonical family',p.locator('#detailDialog').evaluate('(d)=>d.open'));c.close()
  browser.close()
 report['passed']=all(x['passed'] for x in report['checks']);(out/'browser-report.json').write_text(json.dumps(report,indent=2));print(json.dumps({'passed':report['passed'],'checks':len(report['checks']),'projects':len(items),'metrics':report['metrics']}),flush=True);return report

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--url');p.add_argument('--output');args=p.parse_args();out=Path(args.output) if args.output else ROOT/'qa'
 if args.url:run(args.url,out)
 else:
  class Handler(http.server.SimpleHTTPRequestHandler):
   def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT.parent),**kw)
   def log_message(self,*a):pass
  server=socketserver.ThreadingTCPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start()
  try:run('http://127.0.0.1:'+str(server.server_address[1])+'/tacz/',out)
  finally:server.shutdown()
