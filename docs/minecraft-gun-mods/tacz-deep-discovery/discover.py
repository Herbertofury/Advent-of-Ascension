#!/usr/bin/env python3
"""Broad but resumable TaCZ gun-content discovery; no mod binaries are fetched."""
from __future__ import annotations
import concurrent.futures,datetime,hashlib,json,os,re,sys,threading,time
from pathlib import Path
from urllib.parse import urlencode,urlparse,urljoin
import requests
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));import research as r;import collect as c
r.CACHE=ROOT/'cache';r.CACHE.mkdir(parents=True,exist_ok=True)
UA='AoA-TaCZ-Research/2.0 (public creator/project evidence; https://github.com/Herbertofury/Advent-of-Ascension)'
LOCK=threading.Lock()
CF_QUERIES=[('mc-mods','tacz'),('mc-addons','tacz'),('customization','tacz'),('texture-packs','tacz'),('mc-addons','gunpack'),('customization','gunpack'),('mc-mods','gunpack'),('texture-packs','gunpack'),('customization','timeless'),('mc-addons','timeless'),('texture-packs','timeless'),('mc-mods','timeless'),('customization','gun pack'),('mc-addons','gun pack'),('texture-packs','gun pack'),('customization','classic'),('mc-addons','classic'),('customization','arsenal'),('mc-addons','arsenal'),('customization','armorer'),('mc-addons','armorer'),('mc-mods','MCS2'),('mc-mods','guns zero')]
MR_QUERIES=['tacz','gunpack','gun pack','timeless','classic guns','tac zero','armorer','tacz guns']
GH_QUERIES=['tacz gunpack','tacz gun pack','taczgunpack','tacz weapons','tacz pack','TaCZ gunpack in:readme']
GUN=re.compile(r'tacz|tac.zero|timeless.{0,30}(zero|classic)|gun.?pack|gun.?pack|firearms|weapon pack',re.I)

def save(path,value):r.save(path,value)
def load(path,default=None):return r.load(path,default)
def text(value):return re.sub(r'\s+',' ',BeautifulSoup(str(value or ''),'html.parser').get_text(' ',strip=True)).strip()

def gh_get(url):
 key=ROOT/'cache'/('gh-'+hashlib.sha256(url.encode()).hexdigest()+'.json')
 if key.exists():return load(key)
 headers={'Accept':'application/vnd.github+json','User-Agent':UA}
 if os.environ.get('GH_TOKEN'):headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
 try:
  response=requests.get(url,headers=headers,timeout=(10,35));out={'url':url,'status':response.status_code,'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  if response.ok:out['json']=response.json()
  else:out['error']=response.text[:250]
 except Exception as exc:out={'url':url,'error':str(exc)[:250]}
 save(key,out);return out

def existing():
 d=load(PARENT/'tacz/catalog.json');ids={x['id'] for x in d['items']};urls={};names={}
 for x in d['items']:
  for provider,pid in x.get('providerIds',{}).items():ids.add(('cf-' if provider=='curseforge' else 'mr-')+str(pid))
  ids.update(x.get('aliases',[]))
  for a in x.get('links',[]):urls[a['url'].rstrip('/')]=x['id']
  names[x['id']]=x['name']
 ids.update(d.get('idAliases',{}));return d,ids,urls,names

def discover_cf(pair):
 kind,q=pair;found={};evidence=[];page=1;terminal=False
 while True:
  hits,pages,proof=c.cf_search('minecraft',kind,q,page);evidence.append(proof)
  for x in hits:
   if not GUN.search(x['name']+' '+x.get('summary','')):continue
   key='cf-'+str(x['id']);found[key]={'id':key,'name':x['name'],'summary':x.get('summary',''),'url':c.CF+'/'+x['path'],'provider':'CurseForge','downloads':x.get('downloads'),'discovery':[kind+':'+q]}
  if page>=pages and (hits or '0 Projects' in proof.get('resultsText','')):terminal=True;break
  if not hits:break
  page+=1
 return list(found.values()),{'provider':'CurseForge','class':kind,'query':q,'pagesRead':len(evidence),'recordsRead':sum(x.get('read',0) for x in evidence),'terminalPageReached':terminal,'evidence':evidence}

def discover_mr(q):
 found={};offset=0;evidence=[];terminal=False;total=None
 while True:
  url='https://api.modrinth.com/v2/search?'+urlencode({'query':q,'limit':100,'offset':offset,'index':'downloads'})
  res=r.get(url);body=res.get('json',{});hits=body.get('hits',[]);total=body.get('total_hits');evidence.append({'url':url,'status':res.get('status'),'read':len(hits)})
  for x in hits:
   key='mr-'+x['project_id'];found[key]={'id':key,'name':x['title'],'summary':x.get('description',''),'url':'https://modrinth.com/'+x['project_type']+'/'+x['slug'],'provider':'Modrinth','projectType':x['project_type'],'author':x.get('author'),'downloads':x.get('downloads'),'discovery':[q]}
  offset+=len(hits)
  if total is not None and offset>=total:terminal=True;break
  if not hits:break
 return list(found.values()),{'provider':'Modrinth','query':q,'totalHits':total,'recordsRead':offset,'terminalPageReached':terminal,'evidence':evidence}

def discover_gh(q):
 found=[];page=1;evidence=[];terminal=False
 while True:
  url='https://api.github.com/search/repositories?'+urlencode({'q':q,'per_page':100,'page':page,'sort':'updated'})
  res=gh_get(url);data=res.get('json',{});hits=data.get('items',[]);evidence.append({'url':url,'status':res.get('status'),'read':len(hits)})
  for x in hits:
   found.append({'id':'gh-'+str(x['id']),'name':x['full_name'],'summary':x.get('description') or '', 'url':x['html_url'],'provider':'GitHub','stars':x['stargazers_count'],'fork':x['fork'],'defaultBranch':x['default_branch'],'updated':x['pushed_at'],'discovery':[q]})
  total=data.get('total_count')
  if total is not None and page*100>=total:terminal=not data.get('incomplete_results',False);break
  if not hits or page*100>=1000:break
  page+=1
 return found,{'provider':'GitHub','query':q,'recordsRead':sum(x['read'] for x in evidence),'terminalPageReached':terminal,'evidence':evidence}

def snapshot(x):
 url=x['url'];out=dict(x);out['checkedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 if x['provider']=='CurseForge':
  res=r.get(url);out['status']=res.get('status')
  if not res.get('text'):out['error']=res.get('error','No source body');return out
  soup,body=c.rsc(res['text']);obj=next((a for a in c.objects(body,'project') if isinstance(a,dict) and a.get('id')),None)
  if not obj:out['error']='No project metadata';return out
  desc=soup.select_one('.project-description');plain=text(desc or '')
  out.update(id='cf-'+str(obj['id']),name=obj['name'],summary=obj.get('summary',''),downloads=obj.get('downloads'),favorites=obj.get('favoriteCount'),authors=[a.get('name') for a in obj.get('members') or []],sourceRepository=obj.get('sourceUrl'),updated=c.iso(obj.get('updateDate')),creatorText=plain)
  out['sourceLinks']=list(dict.fromkeys(urljoin(url,a['href']) for a in (desc.select('a[href]') if desc else []) if a['href'].startswith(('https://','http://'))))
  out['media']=[{'url':im.get('src'),'alt':im.get('alt','')} for im in (desc.select('img') if desc else []) if im.get('src','').startswith('http')];out['icon']=obj.get('avatarUrl');out['mainFile']=obj.get('mainFile')
 elif x['provider']=='Modrinth':
  res=r.get('https://api.modrinth.com/v2/project/'+x['id'][3:]);o=res.get('json',{});out['status']=res.get('status')
  if not o.get('id'):out['error']=res.get('error','No project metadata');return out
  out.update(name=o['title'],summary=o.get('description',''),creatorText=text(o.get('body','')),rawMarkdown=o.get('body',''),downloads=o.get('downloads'),followers=o.get('followers'),sourceRepository=o.get('source_url'),updated=o.get('updated'),projectType=o.get('project_type'),icon=o.get('icon_url'),gallery=o.get('gallery',[]),license=o.get('license'),team=o.get('team'))
  out['sourceLinks']=list(dict.fromkeys(re.findall(r'https?://[^\s<>"\)\]]+',o.get('body',''))))
 else:
  full=x['url'].split('github.com/')[-1];res=gh_get('https://api.github.com/repos/'+full+'/readme');o=res.get('json',{});out['status']=res.get('status')
  if o.get('content'):
   import base64
   md=base64.b64decode(o['content']).decode('utf-8','replace');out['creatorText']=text(md);out['rawMarkdown']=md;out['sourceLinks']=list(dict.fromkeys(re.findall(r'https?://[^\s<>"\)\]]+',md)))
  else:out['creatorText']='';out['error']=res.get('error','No README')
  rel=gh_get('https://api.github.com/repos/'+full+'/releases?per_page=100');out['releases']=[{'name':v.get('name'),'tag':v['tag_name'],'url':v['html_url'],'published':v['published_at'],'assets':[{'name':a['name'],'url':a['browser_download_url']} for a in v['assets']]} for v in rel.get('json',[]) if isinstance(v,dict) and 'tag_name' in v] if isinstance(rel.get('json'),list) else []
 return out

def main():
 base,known,urls,names=existing();found={};ledger=[]
 tasks=[('cf',p) for p in CF_QUERIES]+[('mr',q) for q in MR_QUERIES]
 def run(task):return discover_cf(task[1]) if task[0]=='cf' else discover_mr(task[1])
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for records,proof in pool.map(run,tasks):
   ledger.append(proof)
   for x in records:
    if x['id'] in found:found[x['id']]['discovery']=list(set(found[x['id']]['discovery']+x['discovery']))
    else:found[x['id']]=x
   print(proof['provider'],proof['query'],proof['recordsRead'],'terminal',proof['terminalPageReached'],'unique',len(found),flush=True)
   save(ROOT/'discovery.json',{'sources':list(found.values()),'coverage':ledger,'baselineDataHash':base['build']['dataHash']})
 for q in GH_QUERIES:
  records,proof=discover_gh(q);ledger.append(proof)
  for x in records:found.setdefault(x['id'],x)
  print('GitHub',q,proof['recordsRead'],flush=True)
 # The independent catalog is only a discovery index; its outbound creator pages are the qualification authority.
 indexurl='https://yuwan886.github.io/mc-tools/tacz_gun_pack.html';res=r.get(indexurl)
 if res.get('text'):
  soup=BeautifulSoup(res['text'],'html.parser')
  for a in soup.select('a[href]'):
   u=a['href'].split('?')[0].rstrip('/')
   if re.match(r'https://www.curseforge.com/minecraft/(customization|mc-addons|mc-mods|texture-packs)/[^/]+$',u) and u not in urls and not any(x['url']==u for x in found.values()):
    key='seed-'+hashlib.sha256(u.encode()).hexdigest()[:12];found[key]={'id':key,'name':text(a),'summary':'Independent catalog lead; creator source not yet qualified','provider':'CurseForge','url':u,'discovery':[indexurl]}
 # Optional web research seeds are explicit URLs and may be added incrementally.
 for seed in load(ROOT/'web-seeds.json',[]):
  if not any(x['url'].rstrip('/')==seed['url'].rstrip('/') for x in found.values()):found[seed['id']]=seed
 prior={x['id']:x for x in load(ROOT/'snapshots.json',[])}
 candidates=[x for x in found.values() if x['id'] not in known and x['url'].rstrip('/') not in urls]
 # Reuse same-day creator snapshots for previously resolved IDs, preserving their exclusion evidence.
 saved=load(PARENT/'tacz/research.json',{})
 for x in saved.get('snapshots',[]):
  if x.get('id') not in known and not x.get('error'):
   prior.setdefault(x['id'],{**x,'creatorText':x.get('descriptionExcerpt',''),'priorSnapshot':True})
 work=[x for x in candidates if x['id'] not in prior]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  futures={pool.submit(snapshot,x):x for x in work}
  for i,ft in enumerate(concurrent.futures.as_completed(futures),1):
   original=futures[ft]
   try:value=ft.result()
   except Exception as exc:value={**original,'error':type(exc).__name__+': '+str(exc)}
   prior[value['id']]=value
   if i%20==0 or i==len(work):save(ROOT/'snapshots.json',list(prior.values()));print('Source snapshots',i,'/',len(work),flush=True)
 save(ROOT/'discovery.json',{'sources':list(found.values()),'coverage':ledger,'baselineDataHash':base['build']['dataHash'],'baselineCount':len(base['items']),'discovered':len(found),'existingProviderIds':sum(x['id'] in known for x in found.values()),'newSourceLeads':len(candidates)})
 save(ROOT/'snapshots.json',list(prior.values()))
 report=[{'id':x['id'],'name':x.get('name'),'url':x.get('url'),'summary':x.get('summary'),'creatorText':x.get('creatorText','')[:10000],'authors':x.get('authors') or x.get('author'),'downloads':x.get('downloads'),'favorites':x.get('favorites'),'followers':x.get('followers'),'sourceLinks':x.get('sourceLinks',[]),'error':x.get('error'),'priorSnapshot':x.get('priorSnapshot',False)} for x in prior.values() if x['id'] not in known]
 save(ROOT/'candidate-review.json',report)
 print(json.dumps({'baseline':len(base['items']),'discovered':len(found),'newSourceLeads':len(candidates),'snapshots':len(report),'queries':len(ledger),'terminalQueries':sum(x['terminalPageReached'] for x in ledger),'errors':sum(bool(x.get('error')) for x in report)}),flush=True)
if __name__=='__main__':main()
