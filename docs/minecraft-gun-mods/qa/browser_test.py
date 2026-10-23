"""Exercise the actual static explorer. Run against local or deployed HTML."""
from __future__ import annotations
import argparse,contextlib,http.server,json,os,shutil,socketserver,threading,time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]

def run(url, output):
 output.mkdir(parents=True,exist_ok=True);report={'url':url,'checks':[],'errors':[],'metrics':{}}
 def check(name,value,detail=None):
  report['checks'].append({'name':name,'passed':bool(value),'detail':detail})
  (output/'browser-report.json').write_text(json.dumps(report,indent=2))
  assert value,(name,detail)
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path=shutil.which('chromium') or shutil.which('google-chrome'),headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  context=browser.new_context(viewport={'width':1440,'height':1050},accept_downloads=True)
  page=context.new_page();page.on('pageerror',lambda err:report['errors'].append(str(err)))
  started=time.monotonic();page.goto(url,wait_until='domcontentloaded',timeout=90000);page.wait_for_function('window.ATLAS_TEST && ATLAS_TEST.count > 0',timeout=60000)
  total=page.evaluate('ATLAS_TEST.count');report['metrics']['initial_dom_ms']=round((time.monotonic()-started)*1000);report['metrics']['initial_render_ms']=page.evaluate('ATLAS_TEST.renderMs')
  check('all records rendered without pagination',page.locator('.project-card').count()==total,{'count':total})
  page.screenshot(path=str(output/'desktop-top.png'))
  first=page.evaluate('ATLAS_TEST.data.items[0]');fid=first['id']
  page.locator('#anchorsButton').click();check('study anchor preset',page.evaluate('ATLAS_TEST.shown')>0)
  page.locator('#resetFilters').click();page.locator('#search').fill('"'+first['name']+'"');page.wait_for_timeout(220)
  check('quoted search matches exact title',page.locator('[data-project="'+fid+'"]').count()==1)
  page.locator('[data-project="'+fid+'"] .favorite').click();check('favorite add',page.evaluate('(id)=>ATLAS_TEST.favorites.includes(id)',fid))
  page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('favorite survives reload',page.evaluate('(id)=>ATLAS_TEST.favorites.includes(id)',fid))
  page.locator('[data-scope="favorites"]').click();check('saved-only collection',page.evaluate('ATLAS_TEST.shown')==1)
  page.locator('[data-project="'+fid+'"] [data-action="detail"]').click();page.locator('#projectNotes').fill('QA note: preserve this idea.');page.locator('[data-close="detailDialog"]').click()
  page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');page.locator('[data-project="'+fid+'"] [data-action="detail"]').click();check('notes survive reload',page.locator('#projectNotes').input_value()=='QA note: preserve this idea.')
  official=page.locator('#detailDialog .main-link').get_attribute('href');check('external project action uses exact canonical URL',official==first['projectUrl'],official)
  check('detail shows release pairing table',page.locator('#detailDialog .releases tbody tr').count()==len(first.get('releases',[])))
  page.locator('[data-close="detailDialog"]').click();page.locator('#resetFilters').click()
  ids=page.evaluate('ATLAS_TEST.data.items.slice(0,3).map(x=>x.id)')
  for id in ids:page.locator('[data-compare="'+id+'"]').first.check()
  check('compare selection',page.evaluate('ATLAS_TEST.compare.length')==3)
  page.locator('#openCompare').click();check('compare full metadata',page.locator('.compare-table thead th').count()==4)
  page.locator('[data-remove-compare]').first.click();check('compare removal updates table',page.locator('.compare-table thead th').count()==3)
  page.locator('[data-close="utilityDialog"]').click();page.locator('#clearCompare').click();check('compare tray clears',page.locator('#compareTray').is_hidden())
  for view,selector in [('table','.project-table tbody tr'),('gallery','.project-card'),('cards','.project-card')]:
   page.locator('[data-view="'+view+'"]').click();check(view+' full view',page.locator(selector).count()==total)
  for sort in ['date','created','name','downloads','priority']:
   page.locator('#sort').select_option(sort);check('sort '+sort,page.evaluate('ATLAS_TEST.shown')==total)
  for key,id in [('edition','editionFilter'),('type','typeFilter'),('ecosystem','ecosystemFilter'),('loader','loaderFilter'),('version','versionFilter'),('theme','themeFilter'),('activity','activityFilter'),('provider','providerFilter')]:
   values=page.locator('#'+id+' option').evaluate_all('(a)=>a.map(o=>o.value).filter(Boolean)')
   if not values:continue
   value=next((v for v in values if v!='26.'),values[0]);page.locator('#'+id).select_option(value)
   count=page.evaluate('ATLAS_TEST.shown');check('facet '+key,0<=count<=total,{'value':value,'count':count});page.locator('#resetFilters').click()
  pair=page.evaluate('''() => ATLAS_TEST.data.items.flatMap(x=>x.releases||[]).find(r=>r.versions.length && r.loaders.length)''')
  if pair:
   query='version:'+pair['versions'][0]+' loader:'+pair['loaders'][0];page.locator('#search').fill(query);page.wait_for_timeout(220);check('structured version + loader',page.evaluate('ATLAS_TEST.shown')>0)
  check('impossible crossed release pair rejected',page.evaluate('''() => !ATLAS_TEST.releaseMatches({releases:[{versions:['1.20.1'],loaders:['Forge']},{versions:['1.21.1'],loaders:['Fabric']}]},'1.20.1','Fabric')'''))
  page.locator('#saveView').click();page.locator('#viewName').fill('QA saved version view');page.locator('#savedViewForm [type="submit"]').click();check('saved view created',page.locator('[data-load-view]').count()==1)
  page.locator('#resetFilters').click();page.locator('[data-load-view]').click();check('saved filters restored',page.locator('#search').input_value()==query)
  page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('saved view survives reload',page.locator('[data-load-view]').count()==1)
  page.locator('[data-delete-view]').click();check('saved view delete',page.locator('[data-load-view]').count()==0)
  for format in ['json','csv']:
   page.locator('#exportResults').click()
   with page.expect_download() as dl:page.locator('[data-export="'+format+'"]').click()
   path=output/('test-export.'+format);dl.value.save_as(path);check('export '+format,path.stat().st_size>0)
   if format=='json':check('export count reconciles',len(json.loads(path.read_text())['items'])==page.evaluate('ATLAS_TEST.shown'))
  with page.expect_download() as dl:page.locator('#backupButton').click()
  backup=output/'test-collection.json';dl.value.save_as(backup);value=json.loads(backup.read_text());check('backup contains favorites and notes',fid in value['favorites'] and fid in value['notes'])
  page.evaluate('''() => ATLAS_TEST.importCollection({favorites:['unavailable-project'],notes:{'unavailable-project':'preserve me'},views:[]})''');check('unknown imported favorite retained',page.evaluate("ATLAS_TEST.favorites.includes('unavailable-project')"))
  page.locator('#importFile').set_input_files(str(backup));page.wait_for_timeout(200);check('import preserves existing notes',page.evaluate("JSON.parse(localStorage.getItem('aoa.minecraft-guns.collection.v1')).notes['unavailable-project']")=='preserve me')
  page.locator('#themeButton').click();check('light theme',page.locator('html').get_attribute('data-theme')=='light');page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');check('theme survives reload',page.locator('html').get_attribute('data-theme')=='light');page.locator('#themeButton').click()
  page.locator('#resetFilters').click();page.locator('#sourcesButton').click();check('provenance panel',page.locator('#utilityContent').inner_text().find('Canonical sources')>=0);page.locator('[data-close="utilityDialog"]').click()
  page.locator('#queryHelp').click();check('query help',page.locator('#utilityContent').inner_text().find('loader:forge')>=0);page.keyboard.press('Escape');check('escape closes modal',not page.locator('#utilityDialog').evaluate('(x)=>x.open'))
  page.keyboard.press('/');check('slash focuses search',page.locator('#search').evaluate('(x)=>x===document.activeElement'))
  page.locator('#search').fill('no-match-zzzzzzzzzzzzzzz');page.wait_for_timeout(220);check('empty state',page.locator('#empty').is_visible());page.locator('#emptyReset').click()
  with_media=page.evaluate('ATLAS_TEST.data.items.find(x=>x.media?.length>1) || ATLAS_TEST.data.items.find(x=>x.media?.length)')
  if with_media:
   page.evaluate('(id)=>document.querySelector(`[data-project="${id}"] [data-action="gallery"]`).click()',with_media['id']);check('gallery opens',page.locator('#lightbox').evaluate('(x)=>x.open'))
   check('gallery image attribution',page.locator('#lightbox a').count()>=1)
   page.keyboard.press('ArrowRight');check('gallery keyboard navigation',page.locator('#lightbox').evaluate('(x)=>x.open'));page.keyboard.press('Escape')
  page.locator('.library').scroll_into_view_if_needed();page.screenshot(path=str(output/'desktop-catalog.png'))
  page.set_viewport_size({'width':390,'height':844});page.locator('.library').scroll_into_view_if_needed();check('mobile no horizontal overflow',page.evaluate('document.documentElement.scrollWidth <= innerWidth+1'))
  page.locator('#mobileFilters').click();check('mobile filters open',page.locator('#filters').is_visible());page.locator('#mobileFilters').click();page.screenshot(path=str(output/'mobile.png'))
  page.locator('[data-project="'+fid+'"] .favorite').click();check('favorite remove',not page.evaluate('(id)=>ATLAS_TEST.favorites.includes(id)',fid))
  check('no uncaught renderer errors',not report['errors'],report['errors'])
  # Blocked storage remains usable and exportable.
  c2=browser.new_context(viewport={'width':1000,'height':800});c2.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('Storage denied for QA')}})")
  p2=c2.new_page();p2.goto(url,wait_until='domcontentloaded');p2.wait_for_function('window.ATLAS_TEST');check('blocked storage warning',p2.locator('#storageWarning').is_visible());p2.locator('.project-card .favorite').first.click();check('blocked storage favorites still work in memory',len(p2.evaluate('ATLAS_TEST.favorites'))==1);c2.close()
  context.close();browser.close()
 report['passed']=all(x['passed'] for x in report['checks']);(output/'browser-report.json').write_text(json.dumps(report,indent=2));return report

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--url');parser.add_argument('--output',default=str(ROOT/'qa'));args=parser.parse_args()
 if args.url:result=run(args.url,Path(args.output))
 else:
  class Handler(http.server.SimpleHTTPRequestHandler):
   def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
   def log_message(self,*a):pass
  server=socketserver.ThreadingTCPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start()
  try:result=run('http://127.0.0.1:'+str(server.server_address[1])+'/',Path(args.output))
  finally:server.shutdown()
 print(json.dumps({'passed':result['passed'],'checks':len(result['checks']),'metrics':result['metrics']},indent=2))
