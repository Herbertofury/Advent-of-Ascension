#!/usr/bin/env python3
"""Resume exact evidence and change route after provider blocking; no paid or binary assets."""
from pathlib import Path
import base64,concurrent.futures,hashlib,io,json,os,re,sys,zipfile
from urllib.parse import quote,urlencode
import requests
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(ROOT));import research_community as c
r=c.r
ARTIFACT=12612119498
SHA='a56a264ba8e311cde770871f283b0a6379f3bfea0d4ae87798d65d6a425c0dd5'
SEEDS=['BV1LkfTYeE5o','BV1W88BzGEmD','BV1L4Ek68Eyp','BV1LaLtzFEQB','BV19H5mzCE3F','BV18rt4z7Ebn','BV11cp2zmEqc','BV1JfLAzeE59','BV1jBVkzeEZ8','BV1VRa9emEUD','BV1A2H7zhEzT','BV1UdH562EjS','BV1qinS6WEHy','BV1pxHv6ZEiy','BV173Hp6SEWW','BV1h3H56mEAK','BV1EKyWBkE2n','BV1SAaMzNExi']

def save(name,obj):c.save(name,obj)
def restore():
 if (ROOT/'creator-video-evidence.json').exists():return
 response=requests.get('https://api.github.com/repos/Herbertofury/Advent-of-Ascension/actions/artifacts/'+str(ARTIFACT)+'/zip',headers={'Authorization':'Bearer '+os.environ['GH_TOKEN']},timeout=(15,90));response.raise_for_status();raw=response.content;assert hashlib.sha256(raw).hexdigest()==SHA
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  for name in z.namelist():
   rel=Path(name)
   if rel.is_absolute() or '..' in rel.parts or name.endswith('/') or rel.suffix!='.json':continue
   p=ROOT/rel
   if not p.exists():p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(name))

def gh(path):
 url='https://api.github.com/'+path;cache=ROOT/'cache'/('github-'+hashlib.sha256(url.encode()).hexdigest()+'.json')
 if cache.exists():return json.loads(cache.read_text())
 res=requests.get(url,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'},timeout=(10,35))
 try:body=res.json()
 except ValueError:body={}
 out={'url':url,'status':res.status_code,'data':body,'checkedAt':c.stamp()};r.save(cache,out);return out

def manifests():
 prior=c.load('manifest-evidence.json',None)
 if prior:return prior
 evidence={'query':'filename:gunpack.meta.json','pages':[],'manifests':[],'repositories':{},'terminal':False};page=1;hits=[]
 while True:
  res=gh('search/code?'+urlencode({'q':evidence['query'],'per_page':100,'page':page}));d=res['data'];batch=d.get('items',[]);evidence['pages'].append({'page':page,'status':res['status'],'count':len(batch),'total':d.get('total_count'),'incomplete':d.get('incomplete_results')})
  if res['status']!=200:evidence['limitation']=d.get('message','Unavailable');break
  hits+=batch
  if len(hits)>=d['total_count']:evidence['terminal']=not d.get('incomplete_results',False);break
  if not batch or page*100>=1000:evidence['limitation']='Provider pagination or search-result ceiling reached, not claimed complete';break
  page+=1
 for hit in hits:
  repo=hit['repository'];path=hit['path'];res=gh('repos/'+repo['full_name']+'/contents/'+quote(path,safe='/'));body=res['data'];value=None
  if res['status']==200 and body.get('content'):
   try:value=json.loads(base64.b64decode(body['content']))
   except Exception:pass
  evidence['manifests'].append({'repository':repo['full_name'],'repositoryId':repo['id'],'path':path,'url':hit['html_url'],'fileSha':hit['sha'],'status':res['status'],'metadata':value})
 save('manifest-evidence.json',evidence)
 known=json.loads((PARENT/'tacz/catalog.json').read_text());known_urls={u['url'].lower().rstrip('/') for x in known['items'] for u in x.get('links',[])}
 groups={}
 for m in evidence['manifests']:groups.setdefault(m['repository'],[]).append(m)
 for repo,records in groups.items():
  source='https://github.com/'+repo
  if source.lower() in known_urls:evidence['repositories'][repo]={'status':'Already linked by the current catalog','manifests':len(records)};continue
  meta=gh('repos/'+repo);obj=meta['data'];branch=obj.get('default_branch')
  if not branch:evidence['repositories'][repo]={'status':'Repository metadata unavailable'};continue
  tree=gh('repos/'+repo+'/git/trees/'+quote(branch,safe='')+'?recursive=1')['data'];paths=tree.get('tree',[])
  guns=[x['path'] for x in paths if re.search(r'/index/guns?/.*\.json$|/guns?/index/.*\.json$',x['path'],re.I)]
  readme=gh('repos/'+repo+'/readme')['data'];text=''
  if readme.get('content'):
   try:text=base64.b64decode(readme['content']).decode('utf-8')
   except Exception:pass
  releases=gh('repos/'+repo+'/releases?per_page=100')['data']
  evidence['repositories'][repo]={'id':obj.get('id'),'branch':branch,'author':(obj.get('owner') or {}).get('login'),'description':obj.get('description'),'updated':obj.get('pushed_at'),'fork':obj.get('fork'),'treeTruncated':tree.get('truncated'),'treeCount':len(paths),'gunIndexes':guns,'previewPaths':[x['path'] for x in paths if re.search(r'\.(png|jpg|webp)$',x['path'],re.I)],'readme':text,'releases':releases if isinstance(releases,list) else [],'status':'Inspected public source manifests, gun indexes and release metadata; not executed'}
  save('manifest-evidence.json',evidence)
 print('Manifest search',len(hits),'files;',len(evidence['repositories']),'repositories;',evidence['terminal'],flush=True);return evidence

def creators():
 videos=c.load('creator-video-evidence.json',{});todo=set(SEEDS);search=c.load('video-search.json',{})
 for id,v in search.get('videos',{}).items():
  if re.search(r'\u53d1\u5e03|\u6d4b\u8bd5|Cyen|\u7ec8|\u4fa6\u67e5\u529b\u91cf|\u718a\u51fa\u6ca1',v['title'],re.I) and not re.search(r'\u57fa\u5ca9|\u7f51\u6613|\u6559\u7a0b|\u6574\u5408',v['title']):todo.add(id)
 # Exhaust every relevant episode in these author-owned gunpack collections, not recommendation widgets.
 while todo-set(videos):
  pending=sorted(todo-set(videos))
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
   for id,rec in zip(pending,pool.map(c.video,pending)):
    videos[id]=rec
    for ep in rec.get('episodes',[]):
     if re.search(r'tacz|gunpack|\u67aa\u5305|\u67aa\u68b0|TROL|IFCD|TCPL|EMI|bare|\u4ea7\u54c1|\u91cd\u94f8|\u7ea2\u77f3|\u6b66\u5668',ep.get('title') or '',re.I):todo.add(ep['bvid'])
    save('creator-video-evidence.json',videos)
  print('Author collection metadata',len(videos),'remaining',len(todo-set(videos)),flush=True)
 save('creator-collection-coverage.json',{'seedIds':SEEDS,'allRelevantReferencedEpisodesRead':not bool(todo-set(videos)),'records':len(videos),'failed':[k for k,v in videos.items() if v.get('code')!=0]});return videos

def forum_mirror():
 out=c.load('forum-alternate-evidence.json',{})
 urls=['https://mcbbs.app/resources/tacz-zhi-chi-yu-tacz-de-fu-shu-qiang-bao-tcpl-xi-lie.30/','https://mcbbs2.cn/resources/tacz-zhi-chi-yu-tacz-de-emx-ni-jing-zhong-ke-de-fu-shu-qiang-bao-emx-fei-fa-gai-zhuang.36/','https://www.mcbbs.app/resources/tacz-yi-wei-mian-chuang-zuo-qiang-bao.40/']
 from bs4 import BeautifulSoup
 from urllib.parse import urljoin
 for url in urls:
  if url in out:continue
  res=r.get(url);soup=BeautifulSoup(res.get('text',''),'html.parser');main=soup.select_one('.resourceBody-main') or soup.select_one('.p-body-main') or soup
  out[url]={'status':res.get('status'),'text':main.get_text(' ',strip=True),'images':[{'url':urljoin(url,im.get('src','')),'alt':im.get('alt','')} for im in main.select('img') if 'attachment' in im.get('src','') or 'resource_icon' in im.get('src','')],'checkedAt':res.get('checkedAt')};save('forum-alternate-evidence.json',out)
 return out

def main():
 restore();videos=creators();manifest=manifests();forum_mirror();summary=c.load('coverage.json',{})
 summary.update({'checkedAt':c.stamp(),'exactCreatorMetadataRecords':len(videos),'manifestFilesRead':len(manifest['manifests']),'manifestRepositoriesRead':len(manifest['repositories']),'manifestTraversalTerminal':manifest['terminal'],'blockedSearchRouteReused':False,'recovery':'Changed to exact creator collection metadata, official public forum mirror pages and indexed gunpack manifests; original blocked query results preserved.'});save('coverage.json',summary);print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
