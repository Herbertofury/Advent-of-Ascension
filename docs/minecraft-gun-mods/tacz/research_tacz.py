#!/usr/bin/env python3
"""Scoped TaCZ gun-content research. Never downloads or executes mod binaries."""
from __future__ import annotations
import concurrent.futures,datetime,hashlib,json,re,sys,threading
from pathlib import Path
from urllib.parse import urlencode,urlparse
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT))
import research as r
import collect as c
r.CACHE=ROOT/'cache';r.CACHE.mkdir(exist_ok=True)
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()

def fetch(url):return r.get(url)
def save(name,value):r.save(ROOT/name,value)
def compact(s):return re.sub(r'[^a-z0-9]','',c.norm(s))

def discovery():
 hits={};ledger=[]
 for provider,kind in [('Modrinth',''),('CurseForge','customization'),('CurseForge','mc-addons')]:
  offset=0;page=1;total=None;complete=False
  while True:
   if provider=='Modrinth':
    url='https://api.modrinth.com/v2/search?'+urlencode({'query':'tacz','limit':100,'offset':offset,'index':'downloads'})
    result=fetch(url);body=result.get('json',{});batch=body.get('hits',[]);total=body.get('total_hits')
    for x in batch:
     key='mr-'+x['project_id'];hits[key]={'id':key,'name':x['title'],'summary':x['description'],'url':'https://modrinth.com/'+x['project_type']+'/'+x['slug'],'downloads':x.get('downloads'),'source':'Modrinth','author':x.get('author')}
    offset+=len(batch)
    if total is not None and offset>=total:complete=True;break
    if not batch:break
   else:
    batch,pages,proof=c.cf_search('minecraft',kind,'tacz',page)
    for x in batch:
     key='cf-'+str(x['id']);hits[key]={'id':key,'name':x['name'],'summary':x.get('summary',''),'url':c.CF+'/'+x['path'],'downloads':x.get('downloads'),'source':'CurseForge','author':(x.get('author') or {}).get('name')}
    offset+=len(batch);total=pages
    if page>=pages and (batch or '0 Projects' in proof.get('resultsText','')):complete=True;break
    if not batch:break
    page+=1
  ledger.append({'provider':provider,'class':kind,'query':'tacz','recordsRead':offset,'pagesOrHits':total,'terminalPageReached':complete})
  print('Discovery',ledger[-1],flush=True)
 return hits,ledger

def cf_snapshot(url):
 res=fetch(url)
 if not res.get('text'):return {'url':url,'status':res.get('status'),'checkedAt':res.get('checkedAt'),'error':res.get('error','No readable page')}
 soup,text=c.rsc(res['text']);objects=[o for o in c.objects(text,'project') if isinstance(o,dict) and o.get('id')]
 if not objects:return {'url':url,'status':res.get('status'),'error':'No official project object'}
 o=objects[0];body=soup.select_one('.project-description');plain=c.clean(body or '')
 files={}
 for group in o.get('latestFiles') or []:
  for file in group.get('files') or []:files[file['id']]=file
 if o.get('mainFile'):files[o['mainFile']['id']]=o['mainFile']
 releases=[]
 for v in files.values():
  v={**v,'gameVersions':v.get('gameVersions') or [],'flavors':v.get('flavors') or []}
  releases.append(c.cf_release(v,url))
 releases.sort(key=lambda x:x['date'],reverse=True)
 return {'provider':'CurseForge','id':'cf-'+str(o['id']),'url':url,'name':o['name'],'summary':o.get('summary',''),'description':plain,'downloads':o.get('downloads'),'favorites':o.get('favoriteCount'),'followers':None,'rating':None,'ratingCount':None,'metricFields':[k for k in o if re.search('rating|fav|vote|like|download',k,re.I)],'releases':releases,'updated':c.iso(o.get('updateDate')),'checkedAt':res['checkedAt'],'status':res['status'],'sourceHash':hashlib.sha256(res['text'].encode()).hexdigest(),'videos':c.video_links(str(body or ''),url),'authors':[x.get('name') for x in o.get('members') or []],'icon':o.get('avatarUrl'),'sourceUrl':o.get('sourceUrl')}

def mr_snapshot(id):
 res=fetch('https://api.modrinth.com/v2/project/'+id);o=res.get('json',{})
 if not isinstance(o,dict) or not o.get('id'):return {'id':'mr-'+id,'status':res.get('status'),'error':res.get('error','No official project object')}
 url='https://modrinth.com/'+o['project_type']+'/'+o['slug'];body=o.get('body','');versions=fetch('https://api.modrinth.com/v2/project/'+id+'/version');rels=[]
 for v in versions.get('json',[]) if isinstance(versions.get('json'),list) else []:
  rels.append({'id':'mr-version-'+v['id'],'name':v.get('name',v.get('version_number')),'date':v['date_published'],'versions':v.get('game_versions',[]),'loaders':v.get('loaders',[]),'channel':v.get('version_type','unknown'),'url':url+'/version/'+v['id'],'provider':'Modrinth'})
 rels.sort(key=lambda x:x['date'],reverse=True)
 return {'provider':'Modrinth','id':'mr-'+o['id'],'url':url,'name':o['title'],'summary':o.get('description',''),'description':c.clean(body),'downloads':o.get('downloads'),'followers':o.get('followers'),'favorites':None,'rating':None,'ratingCount':None,'metricFields':[k for k in o if re.search('rating|fav|vote|like|follow|download',k,re.I)],'releases':rels,'updated':o.get('updated'),'checkedAt':res['checkedAt'],'status':res['status'],'sourceHash':hashlib.sha256(json.dumps(o,sort_keys=True).encode()).hexdigest(),'videos':c.video_links(body,url),'icon':o.get('icon_url'),'gallery':o.get('gallery',[]),'sourceUrl':o.get('source_url')}

def main():
 selection=json.loads((ROOT/'selection.json').read_text());base=json.loads((PARENT/'catalog.json').read_text());idx={x['id']:x for x in base['items']}
 hits,ledger=discovery();jobs={}
 for id in selection['acceptedIds']:
  x=idx[id]
  for link in x['links']:
   if link['provider']=='CurseForge':jobs['cf:'+link['url']]=('cf',link['url'])
   if link['provider']=='Modrinth':jobs['mr:'+link['url'].rstrip('/').rsplit('/',1)[1]]=('mr',link['url'].rstrip('/').rsplit('/',1)[1])
 for h in hits.values():
  if h['id'] in idx:continue
  if re.search(r'gun.?pack|gun.? pack|armorer|adds? .{0,30}(guns|firearms)|arsenal|weapons from',h['name']+' '+h['summary'],re.I):
   jobs['new:'+h['id']]=('mr',h['id'][3:]) if h['id'].startswith('mr-') else ('cf',h['url'])
 snapshots=[]
 def work(pair):return cf_snapshot(pair[1]) if pair[0]=='cf' else mr_snapshot(pair[1])
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
  pending={pool.submit(work,v):k for k,v in jobs.items()}
  for n,ft in enumerate(concurrent.futures.as_completed(pending),1):
   try:o=ft.result()
   except Exception as exc:o={'requestKey':pending[ft],'error':str(exc)}
   snapshots.append(o)
   if n%15==0:print('Exact project sources',n,'/',len(pending),flush=True)
 # Long descriptions remain in private working cache; published proof is a bounded creator excerpt plus field evidence.
 private={o.get('id',o.get('url','unknown')):o for o in snapshots};save('cache/qualified-raw.json',private)
 public=[]
 for o in snapshots:
  body=o.pop('description','');summary=o.get('summary','');remaining=max(0,170-len(summary.split()));o['descriptionExcerpt']=' '.join(body.split()[:remaining])
  o['featureClaims']={}
  for name,pattern in [('animation',r'[^.\n]{0,90}(?:animations?|reloading|inspect)[^.\n]{0,120}'),('models',r'[^.\n]{0,90}(?:models?|textures?|PBR)[^.\n]{0,120}'),('gunContent',r'[^.\n]{0,80}(?:adds?|contains?|includes?|gunpack|gun pack)[^.\n]{0,150}'),('requirements',r'[^.\n]{0,70}(?:require[sd]?|dependenc|tacz v?1\.)[^.\n]{0,130}')]:
   match=re.search(pattern,body,re.I)
   if match:o['featureClaims'][name]={'present':True,'sourceUrl':o.get('url'),'basis':'Creator describes this feature; not a runtime test'}
  o['maintenance']='Discontinued by creator' if re.search(r'no longer.{0,20}(maintain|develop)|discontinued|abandoned',body,re.I) else 'See exact release date'
  o['historicalDownloadsMixed']=bool(re.search(r'1\.16\.5',body) and re.search(r'\bTaC\b',body))
  public.append(o)
 save('research.json',{'checkedAt':NOW,'sourceCatalogHash':base['build']['dataHash'],'selectionCount':len(selection['acceptedIds']),'discovery':list(hits.values()),'coverage':ledger,'snapshots':public,'metricPolicy':selection['metricsPolicy'],'errors':[x for x in public if x.get('error')],'newCandidates':[x for x in public if x.get('id') not in idx]})
 print(json.dumps({'sources':len(public),'errors':len([x for x in public if x.get('error')]),'newCandidates':len([x for x in public if x.get('id') not in idx]),'favoriteFields':sorted(set(k for x in public for k in x.get('metricFields',[])))}),flush=True)
if __name__=='__main__':main()
