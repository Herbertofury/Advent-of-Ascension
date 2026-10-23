#!/usr/bin/env python3
"""Offline acceptance against the exact production snapshot and real Chromium."""
from pathlib import Path
import json,shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]

def main():
 data=json.loads((ROOT/'catalog.json').read_text());report={'mode':'file:// with all HTTP/HTTPS blocked','expectedProjects':len(data['items']),'checks':[]};out=ROOT/'qa'/'offline';out.mkdir(exist_ok=True)
 def check(name,value):
  report['checks'].append({'name':name,'passed':bool(value)});(out/'report.json').write_text(json.dumps(report,indent=2));assert value,name
 with sync_playwright() as pw:
  exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser');options={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']}
  if exe:options['executable_path']=exe
  browser=pw.chromium.launch(**options);context=browser.new_context(viewport={'width':1440,'height':1000});context.route('http://**/*',lambda route:route.abort());context.route('https://**/*',lambda route:route.abort())
  page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto((ROOT/'index.html').as_uri(),wait_until='domcontentloaded',timeout=60000);page.wait_for_function('window.ATLAS_TEST',timeout=30000)
  check('complete snapshot available offline',page.evaluate('GUN_ATLAS.items.length')==len(data['items']))
  check('every project remains in the DOM',page.locator('[data-project].project-card').count()==len(data['items']))
  first=page.locator('.project-card').first;key=first.get_attribute('data-project');first.locator('.favorite').click()
  check('favorite can be saved offline',page.evaluate('(id)=>ATLAS_TEST.favorites.includes(id)',key))
  page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST')
  check('offline favorite survives reload',page.evaluate('(id)=>ATLAS_TEST.favorites.includes(id)',key))
  first=page.locator('.project-card').first;image=first.locator('img').first
  if image.count():image.scroll_into_view_if_needed();page.wait_for_function('(im)=>im.complete',arg=image.element_handle());check('archived image decodes without network',image.evaluate('im=>im.naturalWidth>0'))
  page.locator('#search').fill('version:1.20.1 loader:forge');page.wait_for_timeout(250)
  check('offline structured filtering works',0<page.locator('.project-card').count()<len(data['items']))
  check('no offline script exceptions',not errors)
  page.screenshot(path=str(out/'offline-explorer.png'));browser.close()
 report['passed']=all(x['passed'] for x in report['checks']);(out/'report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report),flush=True)
if __name__=='__main__':main()
