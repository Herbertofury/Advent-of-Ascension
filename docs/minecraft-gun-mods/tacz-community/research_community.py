#!/usr/bin/env python3
"""Gap-directed public creator research, with terminal pagination and no binary downloads."""
from __future__ import annotations
import concurrent.futures,datetime,hashlib,json,re,sys,time
from pathlib import Path
from urllib.parse import urlencode,urljoin,urlparse
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));import research as r
r.CACHE=ROOT/'cache';r.CACHE.mkdir(parents=True,exist_ok=True)
QUERIES=['TACZ TCPL','TACZ RSCA','TACZ \u5f02\u4f4d\u9762','TACZ \u975e\u6cd5\u6539\u88c5','TACZ \u730e\u6740\u5bf9\u51b3','TACZ \u673a\u7532 \u67aa\u5305','TACZ \u80fd\u91cf \u67aa\u5305','TACZ \u539f\u521b \u67aa\u5305 \u53d1\u5e03','TACZ \u514d\u8d39 \u79d1\u5e7b \u67aa\u5305','TACZ \u5c0f\u4f17 \u67aa\u5305','TACZ \u751f\u5316 \u67aa\u5305','TACZ \u55b7\u706b \u67aa\u5305','TACZ \u51b0\u51bb \u67aa\u5305','TACZ \u96f7\u7535 \u67aa\u5305','TACZ \u53d8\u5f62 \u67aa\u5305','TACZ \u5947\u8469 \u67aa\u5305','TACZ \u67aa\u5305 \u914d\u5e03','TaCZ gunpack original release','TaCZ \u67aa\u5305 \u5c0f\u4f5c\u574a','TACZ EMI \u7ecf\u5178']
SEED_VIDEOS=['BV1fkdiYLEJy','BV1vNtse9EmD','BV1ihycY2E3s','BV1eMDZYnE2C','BV12RQqYHEz5','BV1x7ETzfEez','BV1zy411i7HQ','BV1jF1mYEEzV']
FORUMS=['https://www.mcbbs.app/resources/categories/java-ban-you-xi-zi-yuan.13/','https://www.mcbbs.app/resources/?direction=desc&order=download_count']
SEED_PAGES=['https://www.mcbbs.app/resources/tacz-zhi-chi-yu-tacz-de-fu-shu-qiang-bao-tcpl-xi-lie.30/','https://www.mcbbs.app/resources/tacz-zhi-chi-yu-tacz-de-emx-ni-jing-zhong-ke-de-fu-shu-qiang-bao-emx-fei-fa-gai-zhuang.36/']

def save(name,value):r.save(ROOT/name,value)
def load(name,default):return r.load(ROOT/name,default)
def text(value):return BeautifulSoup(value or '','html.parser').get_text(' ',strip=True)
def stamp():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def search_videos():
 result=load('video-search.json',{'queries':[],'videos':{}});done={x['query'] for x in result['queries']}
 for query in QUERIES:
  if query in done:continue
  page=1;proof={'query':query,'pages':[],'terminal':False};seen=set()
  while True:
   url='https://api.bilibili.com/x/web-interface/search/type?'+urlencode({'search_type':'video','keyword':query,'page':page,'order':'totalrank'})
   response=r.get(url);body=response.get('json') or {};data=body.get('data') or {};batch=data.get('result') or [];total=data.get('numPages');ev={'page':page,'httpStatus':response.get('status'),'code':body.get('code'),'returned':len(batch),'totalPages':total,'url':url};proof['pages'].append(ev)
   if body.get('code')!=0 or not isinstance(batch,list):proof['limitation']=body.get('message') or response.get('error','Search provider unavailable');break
   current=set()
   for v in batch:
    bvid=v.get('bvid')
    if not bvid:continue
    current.add(bvid);item=result['videos'].setdefault(bvid,{'bvid':bvid,'title':text(v.get('title')),'description':text(v.get('description')),'author':v.get('author'),'mid':v.get('mid'),'date':v.get('pubdate'),'pic':v.get('pic'),'url':'https://www.bilibili.com/video/'+bvid+'/','queries':[]})
    if query not in item['queries']:item['queries'].append(query)
   if total is not None and page>=int(total):proof['terminal']=True;break
   if not batch:proof['terminal']=not total;break
   if not current-seen:proof['limitation']='Provider repeated the same page; no false terminal assertion';break
   seen|=current;page+=1;time.sleep(.45)
  result['queries'].append(proof);save('video-search.json',result);print('Public video query',query,'pages',len(proof['pages']),'terminal',proof['terminal'],'unique',len(result['videos']),flush=True)
 return result

def forum_sources():
 result=load('forum-evidence.json',{'indexes':[],'resources':{}});queue=list(FORUMS);visited={x['url'] for x in result['indexes']};resources=set(SEED_PAGES)|set(result['resources'])
 while queue:
  url=queue.pop(0)
  if url in visited:continue
  visited.add(url);res=r.get(url);soup=BeautifulSoup(res.get('text',''),'html.parser');links=[];nexts=[]
  for a in soup.select('a[href]'):
   dest=urljoin(url,a['href']);p=urlparse(dest)
   if p.netloc not in ('www.mcbbs.app','mcbbs.app'):continue
   if re.search(r'/resources/[^/?]+\.\d+/$',p.path) and not '/categories/' in p.path:
    title=a.get_text(' ',strip=True)
    if title:links.append({'url':dest,'title':title});resources.add(dest)
   if 'pageNav-jump--next' in a.get('class',[]) or (a.get('rel') and 'next' in a['rel']):nexts.append(dest)
  queue.extend(x for x in dict.fromkeys(nexts) if x not in visited);result['indexes'].append({'url':url,'status':res.get('status'),'resources':links,'next':list(dict.fromkeys(nexts)),'terminal':bool(res.get('status')==200 and not nexts)});save('forum-evidence.json',result)
 # Every resource in the complete public indexes is inspected, not just keyword snippets.
 for url in sorted(resources):
  if url in result['resources']:continue
  res=r.get(url);soup=BeautifulSoup(res.get('text',''),'html.parser');main=soup.select_one('.resourceBody-main') or soup.select_one('.p-body-main') or soup;body=main.get_text(' ',strip=True);title=(soup.select_one('h1') or soup.title);images=[];urls=[]
  for im in main.select('img'):
   src=im.get('data-src') or im.get('src','')
   if src and ('attachment' in src or '/data/resource_icons/' in src):images.append({'url':urljoin(url,src),'alt':im.get('alt','')})
  for a in main.select('a[href]'):
   dest=urljoin(url,a['href'])
   if any(host in dest for host in ('bilibili.com','afdian.com','github.com','modrinth.com','curseforge.com')):urls.append({'url':dest,'label':a.get_text(' ',strip=True)})
  result['resources'][url]={'title':title.get_text(' ',strip=True) if title else '', 'status':res.get('status'),'text':body,'images':list({x['url']:x for x in images}.values()),'links':list({x['url']:x for x in urls}.values()),'checkedAt':res.get('checkedAt'),'sha256':hashlib.sha256(res.get('text','').encode()).hexdigest()};save('forum-evidence.json',result)
  print('Forum source',title.get_text(' ',strip=True) if title else url,flush=True)
 return result

def video(bvid):
 url='https://api.bilibili.com/x/web-interface/view?'+urlencode({'bvid':bvid});res=r.get(url);body=res.get('json') or {};d=body.get('data') or {}
 record={'bvid':bvid,'sourceUrl':'https://www.bilibili.com/video/'+bvid+'/','metadataUrl':url,'status':res.get('status'),'code':body.get('code'),'title':d.get('title'),'description':d.get('desc'),'published':d.get('pubdate'),'pic':d.get('pic'),'owner':d.get('owner'),'pages':d.get('pages'),'checkedAt':res.get('checkedAt'),'sourceHash':hashlib.sha256(json.dumps(body,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),'episodes':[]}
 season=d.get('ugc_season') or {}
 for section in season.get('sections') or []:
  for e in section.get('episodes') or []:
   if e.get('bvid'):record['episodes'].append({'bvid':e['bvid'],'title':e.get('title'),'ownerMid':(e.get('arc') or {}).get('author',{}).get('mid')})
 return record

def creator_sources(search,forum):
 output=load('creator-video-evidence.json',{});todo=set(SEED_VIDEOS)
 for f in forum['resources'].values():
  for link in f['links']:
   match=re.search(r'(BV[A-Za-z0-9]{10})',link['url'])
   if match:todo.add(match.group(1))
 prior=json.loads((PARENT/'tacz-frontier/source-decisions.json').read_text());existing={x['id'] for x in prior}
 # Candidate screening never upgrades search metadata into a creator-confirmed release.
 for id,v in search['videos'].items():
  title=v['title']+' '+v.get('description','')
  if 'bilibili-'+id in existing:continue
  if re.search(r'TCPL|RSCA|CQ1cz|\u5f02\u4f4d\u9762|\u730e\u6740\u5bf9\u51b3|\u975e\u6cd5\u6539\u88c5|\u7ecf\u5178\u4e0d\u94f8|\u65b0\u67aa\u5305|\u539f\u521b\u67aa\u5305|gunpack.{0,25}release',title,re.I):todo.add(id)
 for wave in range(2):
  pending=sorted(todo-set(output))
  if not pending:break
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
   for id,record in zip(pending,pool.map(video,pending)):
    output[id]=record
    if record.get('owner',{}).get('mid') in (1163799255,5742092) or id in SEED_VIDEOS:
     for ep in record['episodes']:
      if re.search(r'tacz|\u67aa\u5305|\u730e\u6740|TCPL|RSCA|EMI',ep.get('title',''),re.I):todo.add(ep['bvid'])
    save('creator-video-evidence.json',output)
  print('Exact creator metadata wave',wave+1,'records',len(output),flush=True)
 return output

def main():
 baseline=json.loads((PARENT/'tacz/catalog.json').read_text());assert len(baseline['items'])>=213
 save('baseline-identity.json',{'taczCount':len(baseline['items']),'taczHash':baseline['build']['dataHash'],'names':[{'id':x['id'],'name':x['name'],'url':x['projectUrl']} for x in baseline['items']]})
 forum=forum_sources();search=search_videos();videos=creator_sources(search,forum)
 summary={'checkedAt':stamp(),'baselineTaCZ':len(baseline['items']),'forumIndexPages':len(forum['indexes']),'forumResourcesRead':len(forum['resources']),'videoQueries':len(search['queries']),'terminalVideoQueries':sum(x['terminal'] for x in search['queries']),'uniqueVideoSearchResults':len(search['videos']),'exactCreatorMetadataRecords':len(videos),'sourceAccessFailures':sum(x.get('code')!=0 for x in videos.values()),'scope':'New original-community and creator distribution dimensions; no repeat of completed provider sweeps. Search misses remain unresolved, not absence.','modBinariesDownloaded':False,'imageGenerationUsed':False}
 save('coverage.json',summary);print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
