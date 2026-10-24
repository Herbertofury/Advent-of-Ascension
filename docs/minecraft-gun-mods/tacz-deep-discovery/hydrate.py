#!/usr/bin/env python3
"""Qualify the accepted TaCZ discoveries; preserve current source identities and evidence."""
from __future__ import annotations
import collections,concurrent.futures,copy,datetime,hashlib,json,re,sys,threading,time
from pathlib import Path
from urllib.parse import urlparse,urljoin,unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));sys.path.insert(0,str(ROOT))
import research as r
import collect as c
import discover as d
r.CACHE=ROOT/'cache';r.CACHE.mkdir(exist_ok=True);c.ROOT=ROOT
LOCK=threading.Lock()
PROMO=re.compile(r'discord|patreon|ko-fi|buymeacoffee|bisect|apexhosting|kinetichosting|sparkedhost|pebblehost|server.pro|shockbyte|hosting|donat|sponsor|billing\.',re.I)
ORIGINAL=c.objects

def normalize(value):
 if isinstance(value,dict):
  for key,item in list(value.items()):
   if item is None and key in {'latestFiles','files','members','categories','relatedProjects','gameVersions','flavors','screenshots','dependencies'}:value[key]=[]
   else:normalize(item)
 elif isinstance(value,list):
  for item in value:normalize(item)
 return value
c.objects=lambda text,key:normalize(ORIGINAL(text,key))

def current(url):
 result=r.get(url)
 if result.get('status')==429:
  # This is a later bounded recovery wave after the original provider window, with one worker/request at a time.
  time.sleep(1.2);result=r.get(url,force=True)
 return result

def coverage_recovery():
 if (ROOT/'coverage-recovery.json').exists():return
 discovery=r.load(ROOT/'discovery.json');found={x['id']:x for x in discovery['sources']};report=[];snapshots={x['id']:x for x in r.load(ROOT/'snapshots.json',[])}
 oldget=r.get
 def low_pressure(url,force=False):
  record=oldget(url,force=force)
  if record.get('status')==429 and not force:
   time.sleep(1.25);return oldget(url,force=True)
  return record
 r.get=low_pressure
 try:
  for proof in discovery['coverage']:
   if proof['provider']!='CurseForge' or proof['terminalPageReached']:continue
   kind,q=proof['class'],proof['query'];failed=next((e for e in proof['evidence'] if e.get('status')!=200 or e.get('read',0)==0),None)
   from urllib.parse import parse_qs
   page=int(parse_qs(urlparse(failed['url']).query).get('page',['1'])[0]) if failed else len(proof['evidence'])+1
   start=page;records=[];terminal=False;ev=[]
   while True:
    time.sleep(.7);hits,pages,e=c.cf_search('minecraft',kind,q,page);ev.append(e)
    for x in hits:
     if not d.GUN.search(x['name']+' '+x.get('summary','')):continue
     key='cf-'+str(x['id']);record={'id':key,'name':x['name'],'summary':x.get('summary',''),'url':c.CF+'/'+x['path'],'provider':'CurseForge','downloads':x.get('downloads'),'discovery':[kind+':'+q]}
     if key not in found:found[key]=record;records.append(record)
    if page>=pages and (hits or '0 Projects' in e.get('resultsText','')):terminal=True;break
    if not hits:break
    page+=1
   report.append({'provider':'CurseForge','class':kind,'query':q,'resumedFromPage':start,'pagesRead':len(ev),'terminalPageReached':terminal,'newLeads':[x['id'] for x in records],'evidence':ev})
   print('Tail recovery',kind,q,'new',len(records),'terminal',terminal,flush=True)
   for record in records:
    if record['id'] in snapshots:continue
    # Resolve exact metadata only when a new lead explicitly names TaCZ or a gunpack; utility decisions remain in the ledger.
    if re.search(r'tacz|tac.zero|timeless.{0,25}(zero|classic)|gunpack|gun pack',record['name']+' '+record['summary'],re.I):
     try:snapshots[record['id']]=d.snapshot(record)
     except Exception as exc:snapshots[record['id']]={**record,'error':str(exc)}
   r.save(ROOT/'coverage-recovery.json',report);r.save(ROOT/'tail-snapshots.json',list(snapshots.values()));r.save(ROOT/'tail-discovery.json',list(found.values()))
 finally:r.get=oldget


def qualify(spec,snapshots):
 key=spec['id'];snapshot=snapshots.get(key,{});url=spec.get('url') or snapshot.get('url');assert url,(key,'No exact creator URL')
 result=current(url)
 item,error=c.cf_project(urlparse(url).path.strip('/'),[])
 if not item:return None,{'id':key,'source':url,'error':error}
 assert item['id']==key,(key,item['id'])
 soup,raw=c.rsc(result.get('text',''));obj=next((x for x in c.objects(raw,'project') if isinstance(x,dict) and x.get('id')),None);assert obj,(key,'Metric source missing')
 description=soup.select_one('.project-description');blocked=set()
 if description:
  for im in description.select('img'):
   src=im.get('src','');a=im.find_parent('a');href=unquote(a.get('href','')) if a else ''
   if PROMO.search(src+' '+im.get('alt','')+' '+href) or src.endswith('.ico'):blocked.add(src)
 item['gallery']=[m for m in item['gallery'] if m['url'] not in blocked]
 galleryurl=url.rstrip('/')+'/gallery';res=current(galleryurl);seen={m['url'] for m in item['gallery']}
 if res.get('text'):
  for im in BeautifulSoup(res['text'],'html.parser').select('img'):
   src=im.get('data-src') or im.get('src','')
   if 'media.forgecdn.net/attachments/' not in src or src in seen or src in blocked or PROMO.search(src+' '+im.get('alt','')):continue
   seen.add(src);item['gallery'].insert(0,{'url':src,'alt':im.get('alt') or item['name']+' creator gallery','role':'Project gallery','sourceUrl':galleryurl})
 with LOCK:c.media(item)
 for m in item.get('media',[]):m['src']='tacz-deep-discovery/'+m['src']
 full=item['description'];item=c.decorate(item)
 # Keep public excerpts bounded, not a copy of the entire creator description.
 budget=max(0,130-len(item['summary'].split()));item['descriptionExcerpt']=' '.join(item.get('descriptionExcerpt','').split()[:budget])
 item['inspiration']=[spec['reason']]+[x for x in item.get('inspiration',[]) if x!=spec['reason']]
 item['themes']=list(dict.fromkeys(item['themes']+['Deep discoveries']+(['Hidden gems'] if spec.get('shortlist') else [])))
 item['curation']='Study anchor' if spec.get('shortlist') else 'Research discovery';item['studyPriority']=110 if spec.get('shortlist') else 55
 item['access']=spec.get('access','Free public release');item['accessEvidence']=url
 if spec.get('creatorUrl'):item['links'].append({'provider':'Creator support','label':'Creator support / editions','url':spec['creatorUrl'],'kind':'creator-channel','verified':True,'verification':'Exact link supplied by the creator project description','lastChecked':item['checkedAt']})
 if spec.get('caution'):item['cautions'].insert(0,spec['caution']);item['creatorAccessNote']=spec['caution']
 item['maintenanceNotice']=spec.get('maintenance','No discontinuation notice found')
 if item['maintenanceNotice']!='No discontinuation notice found':item['activity']='Older release / legacy reference'
 item['reviewEvidence']={'creatorContentUrl':url,'sourceHash':hashlib.sha256(result.get('text','').encode()).hexdigest(),'checkedAt':result['checkedAt'],'qualification':'Creator-described additional TaCZ firearm content; exact release metadata and creator media inspected; no native runtime test'}
 metrics={'id':key,'provider':'CurseForge','url':url,'downloads':obj.get('downloads'),'favorites':obj.get('favoriteCount'),'followers':None,'rating':None,'ratingCount':None,'checkedAt':result['checkedAt'],'sourceHash':item['reviewEvidence']['sourceHash']}
 return {'item':item,'metric':metrics,'editorial':spec},None


def followups():
 report=[]
 for full in ['tomatium208/TaCZ-Valine3g-Things','AlternateFire/TACZ-MCX-LT','Goood-indeed/MurasametCraftGunpack-Tacz-','black458cn/TACZ-ZERO-Expansion-Pack','uchihassasuke353/tacz-gunpack','jasonbrod3/Sharpsharp-Rpg-weapon-WIKI---TACZ']:
  res=d.gh_get('https://api.github.com/repos/'+full);meta=res.get('json',{});branch=meta.get('default_branch');evidence={'repository':full,'status':res.get('status')}
  if branch:
   tree=d.gh_get('https://api.github.com/repos/'+full+'/git/trees/'+branch+'?recursive=1').get('json',{})
   evidence.update(branch=branch,truncated=tree.get('truncated'),paths=[x['path'] for x in tree.get('tree',[]) if re.search(r'gunpack|guns/|gun/|promo|screenshot|\.bbmodel|README|\.png$|\.jpg$',x['path'],re.I)])
  report.append(evidence)
 url='https://api.bilibili.com/x/web-interface/view?bvid=BV1MBEMzNEkJ';res=r.get(url);report.append({'creator':'Koei Unique Armaments','source':url,'status':res.get('status'),'metadata':res.get('json'),'error':res.get('error')})
 r.save(ROOT/'followup-evidence.json',report)


def main():
 selection=r.load(ROOT/'selection.json');snapshots={x['id']:x for x in r.load(ROOT/'snapshots.json',[])};records=r.load(ROOT/'qualified-records.json',{});errors=[]
 targets=[s for s in selection['accepted'] if s['id'] not in records]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  jobs={pool.submit(qualify,s,snapshots):s['id'] for s in targets}
  for i,ft in enumerate(concurrent.futures.as_completed(jobs),1):
   key=jobs[ft]
   try:record,error=ft.result()
   except Exception as exc:record=None;error={'id':key,'error':type(exc).__name__+': '+str(exc)}
   if record:records[key]=record
   else:errors.append(error)
   if i%10==0 or i==len(targets):r.save(ROOT/'qualified-records.json',records);print('Qualified',i,'/',len(targets),'errors',len(errors),flush=True)
 r.save(ROOT/'qualification-report.json',{'requested':len(selection['accepted']),'qualified':len(records),'errors':errors,'withMedia':sum(bool(x['item']['media']) for x in records.values())})
 followups();coverage_recovery()
 assert not errors,errors
 print('Source-qualified records:',len(records),flush=True)
if __name__=='__main__':main()
