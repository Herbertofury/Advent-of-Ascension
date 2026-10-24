#!/usr/bin/env python3
"""Resume the requested frontier without repeating successful searches or downloading mod binaries."""
from pathlib import Path
import base64,hashlib,importlib.util,json,os,re,sys,time,zipfile
from urllib.parse import urlencode,quote,urlparse
import requests
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));sys.path.insert(0,str(ROOT))
import research as r;import collect as c
r.CACHE=ROOT/'cache';r.CACHE.mkdir(parents=True,exist_ok=True)
REPO='Herbertofury/Advent-of-Ascension'
ARTIFACTS=[(12549823512,'0ab0c4d04ecce21f87696d46beaea375bbbebd40fb18b00cae4654be25d5ac64'),(12550515486,'520b0f8c492f90ec01d901bbd538b1bd611bd12e0e7228d2b85d8a435b7856d7')]
GITHUB_TARGETS=['Arcadia-Nova/Dragon-Technology','0999312/tacz-lmr','XColorful/TacZ-PUBG','IKUNlei/IKUNleiGUNpack','PJM-Project-Minecraft/TaCZ-Mechanics','EnFFILy/GunPack','logomonkey-tw/GunPackDB','GNBmonkey/GunPack','Jiriceqq/GunPack','mywifefirefly/Tacz-Strinova']

def restore():
 for id,expected in ARTIFACTS:
  marker=ROOT/('.restored-'+str(id))
  if marker.exists():continue
  response=requests.get('https://api.github.com/repos/'+REPO+'/actions/artifacts/'+str(id)+'/zip',headers={'Authorization':'Bearer '+os.environ['GH_TOKEN']},timeout=(15,120));response.raise_for_status();raw=response.content
  assert hashlib.sha256(raw).hexdigest()==expected,(id,'artifact mismatch')
  import io
  with zipfile.ZipFile(io.BytesIO(raw)) as z:
   for name in z.namelist():
    rel=Path(name)
    if '..' in rel.parts or rel.is_absolute() or name.endswith('/') or rel.suffix not in ('.json','.txt'):continue
    dst=ROOT/rel
    if dst.exists():continue
    dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(z.read(name))
  marker.write_text(expected)

def tail_search():
 data=r.load(ROOT/'discovery.json');sources={x['id']:x for x in data['sources']};new=[]
 for entry in data['coverage']:
  if entry['terminalPageReached']:continue
  if entry['provider']!='CurseForge':continue
  proofs=entry['evidence'];successful=[x for x in proofs if x.get('read',0)>0];page=len(successful)+1
  while True:
   time.sleep(2.2)
   url=c.CF+'/minecraft/search?'+urlencode({'page':page,'pageSize':50,'sortBy':'relevancy','class':entry['class'],'search':entry['query']})
   # The previous provider backpressure has elapsed, and pressure is now deliberately reduced.
   r.get(url,force=True)
   hits,total,proof=c.cf_search('minecraft',entry['class'],entry['query'],page);proofs.append(proof)
   for x in hits:
    key='cf-'+str(x['id'])
    if key not in sources:
     item={'id':key,'name':x['name'],'summary':x.get('summary',''),'url':c.CF+'/'+x['path'],'provider':'CurseForge','downloads':x.get('downloads'),'discovery':[entry['class']+':'+entry['query']]};sources[key]=item;new.append(item)
   if page>=total and (hits or '0 Projects' in proof.get('resultsText','')):entry['terminalPageReached']=True;break
   if not hits:break
   page+=1
  entry['recordsRead']=sum(p.get('read',0) for p in proofs if p.get('status')==200);entry['pagesRead']=len([p for p in proofs if p.get('status')==200]);entry['recovery']='Resume first failed page only; provider pressure reduced to one request per 2.2 seconds'
  print('Recovered tail',entry['class'],entry['query'],entry['terminalPageReached'],flush=True)
 data['sources']=list(sources.values());r.save(ROOT/'discovery.json',data);r.save(ROOT/'tail-new-sources.json',new)
 return data

def repository_proofs():
 out=r.load(ROOT/'repository-proofs.json',{})
 for repo in GITHUB_TARGETS:
  if repo in out:continue
  meta=r.get('https://api.github.com/repos/'+repo);obj=meta.get('json',{});branch=obj.get('default_branch');record={'repository':repo,'status':meta.get('status'),'id':obj.get('id'),'branch':branch,'description':obj.get('description'),'updated':obj.get('pushed_at'),'author':(obj.get('owner') or {}).get('login')}
  if not branch:out[repo]=record;continue
  tree=r.get('https://api.github.com/repos/'+repo+'/git/trees/'+quote(branch,safe='')+'?recursive=1');body=tree.get('json',{});paths=body.get('tree',[]);record['treeTruncated']=body.get('truncated',False);record['treeCount']=len(paths)
  record['packPaths']=[x['path'] for x in paths if re.search(r'gunpack.meta|readme|\.png$|\.jpg$|\.webp$|gun/index|/index/gun|/guns/|/gun/|lang/|pack.mcmeta|\.zip$',x['path'],re.I)]
  metas=[x for x in paths if x['path'].endswith(('gunpack.meta.json','pack.mcmeta'))]
  record['packMetadata']=[]
  for x in metas:
   response=r.get('https://raw.githubusercontent.com/'+repo+'/'+branch+'/'+quote(x['path'],safe='/'));record['packMetadata'].append({'path':x['path'],'status':response.get('status'),'data':response.get('json') or response.get('text','')[:5000]})
  record['releases']=r.get('https://api.github.com/repos/'+repo+'/releases?per_page=100').get('json',[])
  out[repo]=record;r.save(ROOT/'repository-proofs.json',out)
  print('Repository content identity',repo,'tree',len(paths),'pack manifests',len(metas),flush=True)
 return out

def more_creators():
 import creator_probe as p
 data=r.load(ROOT/'creator-probes.json');videos=data['videos']
 for b in ['BV1adAfenEpm','BV1zWxqzQEAp','BV19EEm6gE1q']:
  if b not in videos:videos[b]=p.video(b)
 # All relevant episodes in the two new author-owned series, not cross-author suggestions.
 wanted={}
 for b in ['BV1adAfenEpm','BV1zWxqzQEAp','BV19EEm6gE1q']:
  for e in videos[b].get('episodes',[]):
   if e['bvid'] not in videos and any(t in (e.get('title') or '').lower() for t in ('龙之科技','tacz','枪包','极限','mk14')):wanted[e['bvid']]=e
 for b in wanted:videos[b]=p.video(b)
 data['videos']=videos;r.save(ROOT/'creator-probes.json',data)
 print('Exact creator release/showcase records',len(videos),flush=True)

def main():
 restore();data=tail_search();repository_proofs();more_creators()
 old=set(data['priorSourceIds']);known=set(data['representedIds']);snapshots=r.load(ROOT/'snapshots.json',{})
 spec=importlib.util.spec_from_file_location('prior',PARENT/'tacz-deep-discovery/discover.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d);d.ROOT=ROOT
 for x in r.load(ROOT/'tail-new-sources.json',[]):
  if x['id'] not in old|known and x['id'] not in snapshots and re.search(r'tacz|tac.?zero|timeless|gun.?pack|枪包',x['name']+' '+x.get('summary',''),re.I):snapshots[x['id']]=d.snapshot(x)
 r.save(ROOT/'snapshots.json',snapshots)
 r.save(ROOT/'coverage-summary.json',{'baselineFamilies':206,'sourceIdentities':len(data['sources']),'newSourceIdentities':len({x['id'] for x in data['sources']}-old-known),'sourceCandidatesRead':len(snapshots),'queries':len(data['coverage']),'terminalQueries':sum(x['terminalPageReached'] for x in data['coverage']),'unresolvedQueries':[x for x in data['coverage'] if not x['terminalPageReached']],'creatorVideos':len(r.load(ROOT/'creator-probes.json')['videos']),'repositoryIdentityChecks':len(r.load(ROOT/'repository-proofs.json'))})
 print(json.dumps(r.load(ROOT/'coverage-summary.json'),ensure_ascii=False),flush=True)
if __name__=='__main__':main()
