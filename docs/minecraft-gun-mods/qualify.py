#!/usr/bin/env python3
"""Recover narrowly identified source gaps and validate immutable archived media."""
from __future__ import annotations
import concurrent.futures,hashlib,json,re
from pathlib import Path
from urllib.parse import urlparse
from PIL import Image
import collect as c
import research as r
ROOT=Path(__file__).resolve().parent


def run():
 raw=r.load(ROOT/'raw-projects.json',{});pending=r.load(ROOT/'pending-projects.json',{});report={'mediaRepairs':[],'linkRepairs':[],'recovered':[],'remaining':[]}
 # The original source returns null for some optional arrays. Normalize only those typed collection fields.
 old_objects=c.objects
 def normalize(value):
  if isinstance(value,dict):
   for key,item in list(value.items()):
    if item is None and key in {'latestFiles','files','members','categories','relatedProjects','gameVersions','flavors','screenshots','dependencies'}:value[key]=[]
    else:normalize(item)
  elif isinstance(value,list):
   for item in value:normalize(item)
  return value
 def objects(text,key):return normalize(old_objects(text,key))
 c.objects=objects
 explicit=['minecraft/customization/tacz-cyber-armorer','minecraft/customization/tacz-applied-armorer-koei','minecraft/mc-mods/modularwarfare','minecraft/mc-mods/a-v-a-in-minecraft']
 urls=[key[3:] for key,v in pending.items() if key.startswith('cf:') and 'NoneType' in v.get('error','')]
 urls+= [path for path in explicit if not any(x['projectUrl'].rstrip('/').endswith('/'+path.split('/')[-1]) for x in raw.values())]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  jobs={pool.submit(c.cf_project,path,[]):path for path in dict.fromkeys(urls)}
  for future in concurrent.futures.as_completed(jobs):
   path=jobs[future]
   try:item,error=future.result()
   except Exception as exc:item=None;error={'url':c.CF+'/'+path,'error':str(exc)}
   if item:
    c.media(item);raw['cf:'+path]=item;pending.pop('cf:'+path,None);report['recovered'].append({'id':item['id'],'name':item['name'],'url':item['projectUrl']})
   else:pending['cf:'+path]=error;report['remaining'].append(error)
 for x in raw.values():
  for link in x.get('links',[]):
   if link['url'].startswith('www.'):
    before=link['url'];link['url']='https://'+before;link['verification']='Author-provided hostname normalized to HTTPS; external site not independently verified'
    report['linkRepairs'].append({'id':x['id'],'before':before,'after':link['url']})
  for media in x.get('media',[]):
   path=ROOT/media['src'];metadata=path.with_suffix('.json')
   if not path.exists():continue
   actual=hashlib.sha256(path.read_bytes()).hexdigest()
   if actual==media['sha256']:continue
   canonical=r.load(metadata,{})
   assert canonical.get('url')==media['url'] and canonical.get('sha256')==actual and path.stat().st_size>0,('Unexplained media mismatch',x['id'],media['src'])
   with Image.open(path) as image:image.verify()
   report['mediaRepairs'].append({'id':x['id'],'src':media['src'],'oldSha256':media['sha256'],'newSha256':actual,'cause':'Parallel shared-URL reader observed a zero-byte intermediate; completed archived asset and its sidecar agree'})
   for key in ('sha256','bytes','width','height','originalDimensions'):media[key]=canonical[key]
 r.save(ROOT/'raw-projects.json',raw);r.save(ROOT/'pending-projects.json',pending);r.save(ROOT/'source-recovery.json',report)
 print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
 return report


def public_snapshot():
 # Public catalog exports need concise creator excerpts and exact evidence, not entire copied project descriptions.
 data=r.load(ROOT/'catalog.json')
 for item in data['items']:
  words=item.get('descriptionExcerpt','').split();allowance=max(0,160-len(item['summary'].split()))
  item['descriptionExcerpt']=' '.join(words[:allowance])+(' ...' if len(words)>allowance else '')
  if item['slug']=='modularwarfare':
   item['type']='Standalone gun mod';item['ecosystem']='Modular Warfare';item['curation']='Study anchor';item['studyPriority']=110
   item['inspiration']=['Study a legacy content-pack-based weapon engine, animated models, visible attachments and a creator-friendly authoring workflow. Check the exact source branch before reusing code.']+item['inspiration']
  if item['slug']=='a-v-a-in-minecraft':
   item['curation']='Study anchor';item['studyPriority']=110;item['inspiration']=['Compare a broad game-inspired arsenal, weapon roles, attachment presentation and exact current NeoForge versus older Forge releases.']+item['inspiration']
 data['items'].sort(key=lambda x:(-x['studyPriority'],-x['downloads'],x['name'].lower()))
 data['build']['dataHash']=hashlib.sha256(json.dumps(data['items'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
 r.save(ROOT/'catalog.json',data)
 r.save(ROOT/'source-records.json',[{'id':x['id'],'name':x['name'],'projectUrl':x['projectUrl'],'providerIds':x['providerIds'],'checkedAt':x['checkedAt'],'evidence':x['evidence']} for x in r.load(ROOT/'raw-projects.json',{}).values()])
 return data
if __name__=='__main__':
 import sys
 public_snapshot() if '--public' in sys.argv else run()
