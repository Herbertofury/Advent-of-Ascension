#!/usr/bin/env python3
"""Hydrate newly accepted gun-content records; reuse the completed ranking sweep."""
from __future__ import annotations
import concurrent.futures,hashlib,json,re,sys,threading
from pathlib import Path
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT))
import collect as c
import research as r
r.CACHE=ROOT/'cache';r.CACHE.mkdir(exist_ok=True);c.ROOT=ROOT
LOCK=threading.Lock()
PROMO=re.compile(r'discord|patreon|ko-fi|buymeacoffee|bisect|apexhosting|kinetichosting|sparkedhost|pebblehost|server.pro|shockbyte|hosting|donat|sponsor|billing\.',re.I)

def normal(value):
 if isinstance(value,dict):
  for key,item in list(value.items()):
   if item is None and key in {'latestFiles','files','members','categories','relatedProjects','gameVersions','flavors','screenshots','dependencies'}:value[key]=[]
   else:normal(item)
 elif isinstance(value,list):
  for item in value:normal(item)
 return value
ORIGINAL=c.objects
c.objects=lambda text,key:normal(ORIGINAL(text,key))

def qualify(id,snapshot):
 url=snapshot['url'];path=urlparse(url).path.strip('/')
 item,error=c.cf_project(path,[])
 if not item:return None,{'id':id,'source':url,'error':error}
 assert item['id']==id,(id,item['id'])
 res=r.get(url);soup=BeautifulSoup(res.get('text',''),'html.parser');description=soup.select_one('.project-description');blocked=set()
 if description:
  for image in description.select('img'):
   anchor=image.find_parent('a');href=unquote(anchor.get('href','')) if anchor else '';src=image.get('src','')
   if PROMO.search(src+' '+image.get('alt','')+' '+href) or src.endswith('.ico'):blocked.add(src)
 item['gallery']=[m for m in item['gallery'] if m['url'] not in blocked]
 # Source galleries are exact item media, not a generic image-search result.
 galleryurl=url.rstrip('/')+'/gallery';gallery=r.get(galleryurl);seen={x['url'] for x in item['gallery']}
 if gallery.get('text'):
  for tag in BeautifulSoup(gallery['text'],'html.parser').select('img'):
   src=tag.get('data-src') or tag.get('src','')
   if 'media.forgecdn.net/attachments/' not in src or src in seen or src in blocked or PROMO.search(src+' '+tag.get('alt','')):continue
   seen.add(src);item['gallery'].insert(0,{'url':src,'alt':tag.get('alt') or item['name']+' creator gallery','role':'Project gallery','sourceUrl':galleryurl})
 # Serialize shared-URL writes to avoid reading an intermediate zero-byte image.
 with LOCK:c.media(item)
 for media in item.get('media',[]):media['src']='../tacz/'+media['src']
 full=item.get('description','');item=c.decorate(item)
 item['descriptionExcerpt']=' '.join(item.get('descriptionExcerpt','').split()[:100])
 item['reviewEvidence']={'creatorContentUrl':url,'checkedAt':item['checkedAt'],'mediaSource':galleryurl,'classification':'Additional TaCZ firearms explicitly described by the creator; no runtime test claimed'}
 maintenance='Discontinued by creator' if re.search(r'no longer.{0,25}(maintain|develop)|discontinued|abandoned',full,re.I) else 'Paused by creator' if re.search(r'project is currently frozen|stop updating|on hiatus|on hold',full,re.I) else 'No discontinuation notice found'
 item['maintenanceNotice']=maintenance
 if id=='cf-1336260':item['cautions'].insert(0,'Creator reports an extremely loud close-range sound bug with Breacher/Buster Shot against target dummies or a dead Ender Dragon. Read the current source warning before use.')
 if id=='cf-1738298':item['cautions'].insert(0,'Creator notes StA-18 and StA-11 do not yet have inspect animations.')
 if id=='cf-1636437':item['cautions'].insert(0,'Creator lists TaCZ Mesh Loader and an additional vehicle-set crafting dependency; check the exact release instructions.')
 return item,None

def main():
 selection=json.loads((ROOT/'additional-selection.json').read_text());research=json.loads((ROOT/'research.json').read_text());snap={x['id']:x for x in research['snapshots'] if x.get('id')}
 previous=r.load(ROOT/'additional-records.json',[]);records={x['id']:x for x in previous};errors=[]
 targets=[id for id in selection['acceptedIds'] if id not in records]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  jobs={pool.submit(qualify,id,snap[id]):id for id in targets}
  for n,ft in enumerate(concurrent.futures.as_completed(jobs),1):
   id=jobs[ft]
   try:item,error=ft.result()
   except Exception as exc:item=None;error={'id':id,'error':type(exc).__name__+': '+str(exc)}
   if item:records[id]=item
   else:errors.append(error)
   if n%10==0 or n==len(targets):r.save(ROOT/'additional-records.json',list(records.values()));print('Qualified new gunpacks',n,'/',len(targets),'errors',len(errors),flush=True)
 report={'requested':len(selection['acceptedIds']),'qualified':len(records),'errors':errors,'withMedia':sum(bool(x.get('media')) for x in records.values()),'sourceSnapshotsReused':True}
 r.save(ROOT/'additional-qualification.json',report)
 assert not errors,errors
 assert set(records)==set(selection['acceptedIds'])
 print(json.dumps(report),flush=True)
if __name__=='__main__':main()
