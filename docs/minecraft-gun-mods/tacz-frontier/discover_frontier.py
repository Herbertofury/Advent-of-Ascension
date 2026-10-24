#!/usr/bin/env python3
"""Second frontier search. Public project metadata only; no mod binaries or paid files."""
from __future__ import annotations
import concurrent.futures,datetime,hashlib,importlib.util,json,os,re,sys,time
from pathlib import Path
from urllib.parse import urlencode,urlparse
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));import research as r;import collect as c
spec=importlib.util.spec_from_file_location('previous_discovery',PARENT/'tacz-deep-discovery/discover.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
d.ROOT=ROOT;r.CACHE=ROOT/'cache';r.CACHE.mkdir(parents=True,exist_ok=True)
CF=[(kind,q) for kind in ('customization','mc-addons','texture-packs') for q in ('gun','weapon','armory','tac','firearm','arcana')]
MR=['weapon pack','armory','arsenal','arcana','gun','枪包','ガンパック']
GH=['tacz in:readme fork:false','枪包','永恒枪械','gunpack in:name fork:false','TaCZ 拓展','TaCZ 扩展','TaCZ ガン']
CONTENT=re.compile(r'tacz|tac.?zero|timeless.{0,30}(zero|classic)|gun.?pack|weapon.?pack|gun addon|firearm|枪包|枪械包|ガンパック',re.I)

def old_sources():
 old=r.load(PARENT/'tacz-deep-discovery/discovery.json',{});records={x['id']:x for x in old.get('sources',[])}
 for x in r.load(PARENT/'tacz-deep-discovery/tail-discovery.json',[]):records[x['id']]=x
 return records

def cf_search(kind,q):
 found={};ev=[];page=1;terminal=False
 while True:
  time.sleep(.7);hits,pages,proof=c.cf_search('minecraft',kind,q,page);ev.append(proof)
  for x in hits:
   key='cf-'+str(x['id']);found[key]={'id':key,'name':x['name'],'summary':x.get('summary',''),'url':c.CF+'/'+x['path'],'provider':'CurseForge','downloads':x.get('downloads'),'discovery':[kind+':'+q]}
  if page>=pages and (hits or '0 Projects' in proof.get('resultsText','')):terminal=True;break
  if not hits:break
  page+=1
 return list(found.values()),{'provider':'CurseForge','class':kind,'query':q,'pagesRead':len(ev),'recordsRead':sum(x.get('read',0) for x in ev),'terminalPageReached':terminal,'evidence':ev}

def main():
 old=old_sources();catalog=r.load(PARENT/'tacz/catalog.json');represented={x['id'] for x in catalog['items']}
 for x in catalog['items']:represented.update(x.get('aliases',[]));represented.update(x.get('familyIds',[]))
 found={};ledger=[]
 saved=r.load(ROOT/'discovery.json',{});found={x['id']:x for x in saved.get('sources',[])};ledger=saved.get('coverage',[])
 done={(x['provider'],x.get('class'),x['query']) for x in ledger if x.get('terminalPageReached')}
 queries=[('CurseForge',kind,q) for kind,q in CF]+[('Modrinth',None,q) for q in MR]+[('GitHub',None,q) for q in GH]
 for provider,kind,q in queries:
  if (provider,kind,q) in done:continue
  if provider=='CurseForge':hits,proof=cf_search(kind,q)
  elif provider=='Modrinth':hits,proof=d.discover_mr(q)
  else:time.sleep(2.1);hits,proof=d.discover_gh(q)
  for x in hits:
   if x['id'] not in found:found[x['id']]=x
   else:found[x['id']]['discovery']=list(dict.fromkeys(found[x['id']].get('discovery',[])+x.get('discovery',[])))
  ledger.append(proof)
  r.save(ROOT/'discovery.json',{'baselineFamilies':len(catalog['items']),'baselineDataHash':catalog['build']['dataHash'],'sources':list(found.values()),'coverage':ledger,'priorSourceIds':sorted(old),'representedIds':sorted(represented)})
  print('Frontier',provider,kind,q,'read',proof.get('recordsRead'),'terminal',proof['terminalPageReached'],'distinct',len(found),flush=True)
 # Retain all result identities, and qualify new potentially relevant creator sources only.
 candidates=[x for x in found.values() if x['id'] not in old and x['id'] not in represented and (x['provider']=='GitHub' or CONTENT.search(x['name']+' '+x.get('summary','')))]
 snapshots=r.load(ROOT/'snapshots.json',{});todo=[x for x in candidates if x['id'] not in snapshots]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  jobs={pool.submit(d.snapshot,x):x for x in todo}
  for i,ft in enumerate(concurrent.futures.as_completed(jobs),1):
   x=jobs[ft]
   try:snapshots[x['id']]=ft.result()
   except Exception as exc:snapshots[x['id']]={**x,'error':type(exc).__name__+': '+str(exc)}
   if i%15==0 or i==len(todo):r.save(ROOT/'snapshots.json',snapshots);print('New source qualification',i,'/',len(todo),flush=True)
 # Exact creator index pages are discovery routes, never ranking authorities or endorsed download mirrors.
 indexes={}
 for url in ['https://yuwan886.github.io/mc-tools/tacz_gun_pack.html','https://bbsmc.net/','https://www.mcmod.cn/class/14980.html']:
  res=r.get(url);indexes[url]={'status':res.get('status'),'sourceHash':hashlib.sha256(res.get('text','').encode()).hexdigest()}
  if res.get('text'):
   from bs4 import BeautifulSoup
   soup=BeautifulSoup(res['text'],'html.parser');indexes[url]['links']=list(dict.fromkeys(a['href'] for a in soup.select('a[href]') if any(t in a['href'] for t in ('curseforge.com','modrinth.com','bilibili.com','afdian','github.com'))))
 r.save(ROOT/'independent-indexes.json',indexes)
 brief=[]
 for x in snapshots.values():
  brief.append({k:v for k,v in x.items() if k not in ('rawMarkdown','creatorText','releaseMetadata','tree') }|{'creatorExcerpt':x.get('creatorText','')[:4500]})
 r.save(ROOT/'candidate-review.json',brief)
 r.save(ROOT/'discovery-summary.json',{'baselineFamilies':len(catalog['items']),'sourceIdentities':len(found),'newSourceIdentities':len(set(found)-set(old)-represented),'sourceCandidatesRead':len(snapshots),'queries':len(ledger),'terminalQueries':sum(x['terminalPageReached'] for x in ledger),'unresolvedQueryTails':[x for x in ledger if not x['terminalPageReached']],'knownIdsNotReinvestigated':len(set(found)&(set(old)|represented))})
 print(json.dumps(r.load(ROOT/'discovery-summary.json'),ensure_ascii=False),flush=True)
if __name__=='__main__':main()
