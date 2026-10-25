#!/usr/bin/env python3
"""Qualify original creator identities and preserve images before catalog integration."""
from __future__ import annotations
import collections,datetime,hashlib,importlib.util,json,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(ROOT));import retry_manifests

def load(p,default=None):return json.loads(p.read_text()) if p.exists() else default
def save(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2))
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
 retry_manifests.main()
 selection=load(ROOT/'selection.json');videos=load(ROOT/'creator-video-evidence.json');helper=module('community_source_schema',PARENT/'tacz-frontier/hydrate_frontier.py');helper.ROOT=ROOT
 # Correct the transcribed author field against the exact original uploader metadata, not a name match.
 for spec in selection['accepted']:
  if spec['id']=='bilibili-BV1JfLAzeE59':
   assert videos['BV1JfLAzeE59']['owner']['mid']==52473909
   spec['authorMid']=52473909
 save(ROOT/'selection.json',selection)
 records=load(ROOT/'qualified-records.json',{});proof=[]
 for spec in selection['accepted']:
  key=spec['id']
  if key in records:continue
  primary=videos[spec['primary']];assert primary['code']==0 and primary['owner']['mid']==spec['authorMid'],key
  iso=lambda t:datetime.datetime.fromtimestamp(t,datetime.timezone.utc).isoformat()
  source=primary['sourceUrl'];author={'name':primary['owner']['name'],'url':'https://space.bilibili.com/'+str(spec['authorMid'])}
  record=helper.common(spec,source,'Creator-hosted',author,primary['checkedAt'],min(iso(videos[b]['published']) for b in spec['videos']),iso(primary['published']),primary['sourceHash']);x=record['item']
  x['tags']=['TaCZ','Community discoveries'];x['themes']=['Community discoveries','Creator channels','Animation & handling']+spec['themes']+(['Hidden gems'] if spec['shortlist'] else [])
  x['links'].append({'provider':'Creator channel','label':'Original creator profile','url':author['url'],'verified':True,'lastChecked':primary['checkedAt'],'kind':'creator-channel'})
  x['lineageNames']=spec.get('lineageNames',[])
  if spec.get('runtimeRequirement'):x['creatorRuntimeRequirement']={'text':spec['runtimeRequirement'],'sourceUrl':source,'basis':'Creator-stated; no exact Minecraft/loader pair inferred'}
  for bvid in spec['videos']:
   v=videos[bvid];assert v['code']==0 and v['owner']['mid']==spec['authorMid'],('Different creator',key,bvid)
   im=helper.archive_image(v['pic'],v['sourceUrl'],spec['name']+' creator preview','Creator release/showcase preview');im['src']='tacz-community/assets/'+Path(im['src']).name;save(ROOT/'assets'/Path(im['src']).with_suffix('.json').name,im);x['media'].append(im)
   x['videos'].append({'url':v['sourceUrl']+('?p='+str(spec['showcasePage']) if spec.get('showcasePage') and bvid==spec['primary'] else ''),'label':'Original creator release / gun showcase','evidenceUrl':v['metadataUrl'],'verification':'Exact uploader, title, description and public chapter metadata checked; full playback not reviewed'})
   x['releaseAnnouncements'].append({'url':v['sourceUrl'],'title':v['title'],'date':iso(v['published']),'kind':'Creator announcement or showcase, not independently retrieved binary-file evidence'})
   if key in ('bilibili-BV1Hggn6WEfF','bilibili-BV1qinS6WEHy') and bvid==spec['primary']:
    first=(v.get('pages') or [{}])[0].get('first_frame')
    if first:
     im=helper.archive_image(first,v['sourceUrl'],spec['name']+' exact video opening frame','Public video opening frame');im['src']='tacz-community/assets/'+Path(im['src']).name;save(ROOT/'assets'/Path(im['src']).with_suffix('.json').name,im);x['media'].append(im)
  # Most recent announcement first, without calling a showcase a verified downloadable file.
  x['releaseAnnouncements'].sort(key=lambda a:a['date'],reverse=True)
  for field,label in [('creatorLink','Creator release page'),('distributionLink','Exact creator-published share')]:
   if spec.get(field):x['links'].append({'provider':'Creator distribution','label':label,'url':spec[field],'verified':False,'verification':'Published by the original creator; current file contents and access are not independently verified','lastChecked':primary['checkedAt'],'kind':'creator-channel'})
  if spec.get('distributionNote'):x['creatorAccessNote']+=' '+spec['distributionNote']
  if key=='bilibili-BV1qinS6WEHy':x['activity']='Creator public test edition'
  if key=='bilibili-BV1LkfTYeE5o':x['activity']='Intentional legacy-style reference'
  x['cautions'].append('Video likes, views and creator followers are not gunpack downloads, favorites or ratings.')
  x['media']=list({m['sha256']:m for m in x['media']}.values());assert x['media'];records[key]=record;save(ROOT/'qualified-records.json',records)
  print('Source record',x['name'],len(x['media']),'previews',flush=True)
 # Every inspected episode receives a reason; entire old creator collections are not new pack counts.
 decisions=[];acceptedvideos={b:spec['id'] for spec in selection['accepted'] for b in spec['videos']}
 for key,v in videos.items():
  if key in acceptedvideos:status,reason='accepted family evidence','Original author source for '+acceptedvideos[key]
  elif key in selection['explicitDispositions']:d=selection['explicitDispositions'][key];status,reason=d['status'],d['reason']
  elif (v.get('owner') or {}).get('mid') in [spec['authorMid'] for spec in selection['accepted']]:status,reason='same-creator lineage or nonrelease evidence','Retained as context; not counted again as another independent released gunpack.'
  else:status,reason='existing ecosystem, curator or unqualified source','Existing pack, base runtime, tool, curator comparison or insufficient distinct firearm release proof. Not promoted on keyword or video title alone.'
  decisions.append({'id':key,'title':v.get('title'),'url':v['sourceUrl'],'status':status,'reason':reason})
 for key,d in selection['explicitDispositions'].items():
  if key not in videos:decisions.append({'id':key,**d})
 save(ROOT/'source-decisions.json',decisions)
 evidence=[{'id':key,'name':rec['item']['name'],'source':rec['item']['projectUrl'],'authors':rec['item']['authors'],'checkedAt':rec['item']['checkedAt'],'sourceHash':rec['metric']['sourceHash'],'releaseAnnouncements':rec['item']['releaseAnnouncements'],'accessLimits':rec['item']['creatorAccessNote']} for key,rec in records.items()];save(ROOT/'public-creator-evidence.json',evidence)
 coverage=load(ROOT/'coverage.json',{});coverage.update({'qualifiedCandidates':len(records),'decisionCounts':dict(collections.Counter(x['status'] for x in decisions)),'all191CreatorRecordsDispositioned':len(videos)==191,'visualQualificationPending':True});save(ROOT/'coverage.json',coverage)
 out=ROOT/'qa/media-review';out.mkdir(parents=True,exist_ok=True);allmedia=[(k,m) for k,r in records.items() for m in r['item']['media']];font=ImageFont.load_default(size=15)
 for start in range(0,len(allmedia),16):
  batch=allmedia[start:start+16];sheet=Image.new('RGB',(1440,245*((len(batch)+3)//4)),(230,230,230));draw=ImageDraw.Draw(sheet)
  for i,(key,m) in enumerate(batch):
   im=Image.open(ROOT/'assets'/Path(m['src']).name).convert('RGBA');im.thumbnail((350,193));x=i%4*360;y=i//4*245;sheet.paste(im,(x,y),im);draw.text((x+3,y+197),records[key]['item']['name'][:43],font=font,fill='black');draw.text((x+3,y+220),m['sha256'][:16],font=font,fill='black')
  sheet.save(out/('options-%02d.jpg'%(start//16+1)),quality=94)
 print(json.dumps({'candidates':len(records),'sourcePreviews':len(allmedia),'coverage':coverage}),flush=True)
if __name__=='__main__':main()
