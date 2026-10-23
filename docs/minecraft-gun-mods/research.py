#!/usr/bin/env python3
"""Source discovery for the Minecraft gun inspiration catalog. No downloads of mod binaries."""
from __future__ import annotations
import argparse,concurrent.futures,datetime,hashlib,json,os,re,threading,time
from pathlib import Path
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
CACHE=ROOT/'research-cache';CACHE.mkdir(exist_ok=True)
UA='AoA-Minecraft-Gun-Inspirations/1.0 (https://github.com/Herbertofury/Advent-of-Ascension; public project research)'
LOCK=threading.Lock();LAST=0.0
QUERIES=['gun','guns','firearm','firearms','tacz','timeless classics','point blank','pointblank','scorched','musket','flintlock','blunderbuss','revolver','pistol','rifle','shotgun','minigun','blaster','raygun','weaponry','armorer','arsenal','warfare','flans','techguns','cannon','artillery','gunpack','modern warfare','gunpowder','hell divers','helldivers','portal gun','gravity gun','railgun','create armory','laser gun','nuclear gun']

def save(path,obj):
 path.parent.mkdir(parents=True,exist_ok=True);temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8');temp.replace(path)

def load(path,default=None):return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default

def get(url,force=False):
 global LAST
 key=hashlib.sha256(url.encode()).hexdigest();path=CACHE/(key+'.json')
 if path.exists() and not force:return load(path)
 if 'api.modrinth.com' in url:
  with LOCK:
   delay=.24-(time.monotonic()-LAST)
   if delay>0:time.sleep(delay)
   LAST=time.monotonic()
 result={'url':url,'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=requests.get(url,headers={'User-Agent':UA},timeout=(10,35));result.update(status=r.status_code,finalUrl=r.url)
  if r.status_code==429:
   result['retryAfter']=r.headers.get('Retry-After');result['error']='Provider rate limit; not silently retried'
  elif r.ok:
   try:result['json']=r.json()
   except ValueError:result['text']=r.text
  else:result['error']=r.text[:300]
 except requests.RequestException as ex:result['error']=str(ex)[:250]
 save(path,result);return result

def discovery():
 found={};ledger=[]
 facets=json.dumps([['project_type:mod','project_type:datapack','project_type:resourcepack','project_type:plugin']])
 for query in QUERIES:
  offset=0;pages=0;total=None;complete=False
  while True:
   url='https://api.modrinth.com/v2/search?'+urlencode({'query':query,'limit':100,'offset':offset,'facets':facets,'index':'relevance'})
   r=get(url);data=r.get('json',{});hits=data.get('hits',[])
   if 'total_hits' not in data:break
   total=data['total_hits'];pages+=1
   for hit in hits:
    pid=hit['project_id'];found.setdefault(pid,{**hit,'discoveryQueries':[]})
    if query not in found[pid]['discoveryQueries']:found[pid]['discoveryQueries'].append(query)
   offset+=len(hits)
   if offset>=total:complete=True;break
   if not hits:break
  ledger.append({'provider':'Modrinth','query':query,'totalHits':total,'read':offset,'pages':pages,'terminalPageReached':complete})
  print('Discovery',query,offset,'/',total,'unique',len(found),flush=True)
  save(ROOT/'discovery-modrinth.json',list(found.values()));save(ROOT/'discovery-ledger.json',ledger)
 # Preserve representative official pages and repository navigation to ground provider parsers.
 probes={
  'cf-project':'https://www.curseforge.com/minecraft/mc-mods/vics-point-blank',
  'cf-files':'https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero/files/all',
  'cf-search':'https://www.curseforge.com/minecraft/search?page=1&pageSize=50&sortBy=relevancy&class=mc-mods&search=gun',
  'cf-packs':'https://www.curseforge.com/minecraft/search?page=1&pageSize=50&sortBy=relevancy&class=customization&search=tacz',
  'wiki-home':'https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/Home.md',
  'wiki-sidebar':'https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/_Sidebar.md',
  'docs-directory':'https://api.github.com/repos/Herbertofury/Advent-of-Ascension/contents/docs?ref=main',
  'vault-tree':'https://api.github.com/repos/Herbertofury/Minecraft-Mod-Vault/git/trees/main?recursive=1'
 }
 report={}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for name,res in zip(probes,pool.map(get,probes.values())):
   report[name]={k:v for k,v in res.items() if k not in ('text','json')}
   if 'text' in res:
    path=ROOT/'fixtures'/(name+'.txt');path.parent.mkdir(exist_ok=True);path.write_text(res['text'],encoding='utf-8')
    soup=BeautifulSoup(res['text'],'html.parser');report[name]['scripts']=[{'id':x.get('id'),'type':x.get('type'),'size':len(x.text)} for x in soup.find_all('script')][:12]
   if 'json' in res:
    save(ROOT/'fixtures'/(name+'.json'),res['json'])
    if name=='docs-directory':report[name]['paths']=[x['path'] for x in res['json'] if x['name'].endswith('.html') or any(t in x['name'].lower() for t in ['armory','minecraft','gun-mod'])]
    if name=='vault-tree':report[name]['paths']=[x['path'] for x in res['json'].get('tree',[]) if re.search(r'gun|tacz|catalog|catalogue|armory',x['path'],re.I) and not x['path'].endswith(('.png','.jpg','.webp','.class','.java','.cs'))][:100]
 save(ROOT/'probe-report.json',report)
 print(json.dumps(report,ensure_ascii=False),flush=True)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--discover',action='store_true');args=parser.parse_args();discovery()
