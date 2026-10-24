#!/usr/bin/env python3
"""Qualify seven creator/source families from frozen research, never executable mod files."""
from __future__ import annotations
import concurrent.futures,datetime,hashlib,io,json,os,re,sys,zipfile
from pathlib import Path
from urllib.parse import quote
import requests
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));import research as r
r.CACHE=ROOT/'cache';r.CACHE.mkdir(parents=True,exist_ok=True)
ARTIFACT=12549938633
DIGEST='27aa1f99c07adda06ffca47e715313c5dd74c246a58d876e7affb5a78b75e8bf'
UA='AoA-Creator-Frontier/1.0 (public reference research; no mod downloads)'

def load(path,default=None):return json.loads(path.read_text()) if path.exists() else default
def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def iso(value):return datetime.datetime.fromtimestamp(value,datetime.timezone.utc).isoformat() if isinstance(value,(int,float)) else value

def restore():
 evidence=ROOT/'working-evidence'
 if (evidence/'coverage-summary.json').exists():return evidence
 response=requests.get('https://api.github.com/repos/Herbertofury/Advent-of-Ascension/actions/artifacts/'+str(ARTIFACT)+'/zip',headers={'Authorization':'Bearer '+os.environ['GH_TOKEN']},timeout=(15,120));response.raise_for_status();raw=response.content
 assert hashlib.sha256(raw).hexdigest()==DIGEST,'Research transport hash mismatch'
 evidence.mkdir(exist_ok=True)
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  for name in z.namelist():
   rel=Path(name)
   if rel.is_absolute() or '..' in rel.parts or name.endswith('/') or '__pycache__' in rel.parts:continue
   target=evidence/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(name))
 return evidence

def archive_image(url,source,alt,role):
 url=url.replace('http://','https://',1);key=hashlib.sha256(url.encode()).hexdigest()[:24];folder=ROOT/'assets';folder.mkdir(exist_ok=True);path=folder/(key+'.webp');sidecar=folder/(key+'.json')
 if path.exists() and sidecar.exists():return load(sidecar)
 response=requests.get(url,headers={'User-Agent':UA},timeout=(10,35));response.raise_for_status();assert len(response.content)<25000000,'Unexpected oversized reference image'
 image=Image.open(io.BytesIO(response.content));image.seek(0);original=image.size
 assert min(original)>=16 and max(original)>=32,('Source icon too small',url,original)
 image.thumbnail((1100,750));image=image.convert('RGBA' if image.mode in ('RGBA','P') else 'RGB');image.save(path,'WEBP',quality=91,method=5)
 item={'url':url,'alt':alt,'role':role,'sourceUrl':source,'src':'tacz-frontier/assets/'+path.name,'width':image.width,'height':image.height,'originalDimensions':list(original),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}
 save(sidecar,item);return item

def common(spec,source,provider,author,checked,created,updated,source_hash):
 note=spec['note'];item={'id':spec['id'],'providerIds':{'bilibili':spec['id'].split('-',1)[1]} if provider=='Creator-hosted' else {'github':int(spec['id'][3:])},'name':spec['name'],'slug':re.sub('[^a-z0-9]+','-',spec['name'].lower()).strip('-'),'summary':spec['reason'],'descriptionExcerpt':spec['reason'],'authors':[author],'type':'Gun / content pack','ecosystem':'TaCZ','edition':'Java','projectUrl':source,'links':[{'provider':provider,'label':'Original creator source','url':source,'verified':True,'lastChecked':checked}],'crosslinks':[],'provider':provider,'icon':None,'gallery':[],'media':[],'videos':[],'releases':[],'releaseAnnouncements':[],'versions':[],'loaders':[],'latest':None,'latestStable':None,'updated':updated,'created':created,'downloads':None,'license':'See creator terms','dependencies':[],'sourceRows':[],'checkedAt':checked,'evidence':{'project':source,'releaseList':source,'releaseScope':note},'tags':['TaCZ','Creator frontier'],'themes':['Frontier discoveries','Creator channels','Animation & handling']+(['Hidden gems'] if spec['shortlist'] else []),'earlierPick':False,'curation':'Study anchor' if spec['shortlist'] else 'Research discovery','studyPriority':110 if spec['shortlist'] else 45,'priorityBasis':'Editorial design study, not a native runtime quality or performance benchmark','inspiration':[spec['reason']],'cautions':[note,'Source and media research only; not independently installed or tested in Minecraft.'],'activity':'Creator release / exact file not established','access':spec['access'],'creatorAccessNote':note,'mediaStatus':'Creator reference media archived','maintenanceNotice':'No discontinuation notice found','reviewEvidence':{'creatorContentUrl':source,'checkedAt':checked,'sourceHash':source_hash,'qualification':'Creator firearm content and public source identity verified; exact file/access limits remain explicit'}}
 if spec.get('originalName'):item['originalTitle']={'name':spec['originalName'],'englishMeaning':spec['meaning']}
 facts={'id':spec['id'],'provider':provider,'url':source,'downloads':None,'favorites':None,'followers':None,'rating':None,'ratingCount':None,'checkedAt':checked,'sourceHash':source_hash}
 return {'item':item,'metric':facts,'editorial':{'id':spec['id'],'shortlist':spec['shortlist'],'reason':spec['reason'],'type':'Creator-hosted gunpack' if provider=='Creator-hosted' else 'Gunpack (ZIP)' if spec['id']=='gh-928434009' else 'Legacy source gunpack','access':spec['access'],'caution':note}}

def build_bilibili(spec,videos,mcmod):
 primary=videos[spec['primary']];assert primary['owner']['mid']==spec['authorMid'];source=primary['sourceUrl'];author={'name':primary['owner']['name'],'url':'https://space.bilibili.com/'+str(spec['authorMid'])}
 record=common(spec,source,'Creator-hosted',author,primary['checkedAt'],min(iso(videos[b]['published']) for b in spec['videos']),iso(primary['published']),primary['sourceHash']);x=record['item'];x['themes'].append('Science fiction' if spec['shortlist'] else 'Modern firearms')
 x['links'].append({'provider':'Creator channel','label':'Creator profile and pinned distribution','url':author['url'],'verified':True,'lastChecked':primary['checkedAt'],'kind':'creator-channel'})
 for b in spec['videos']:
  v=videos[b];assert v['owner']['mid']==spec['authorMid'],('Different author',b)
  x['media'].append(archive_image(v['pic'],v['sourceUrl'],spec['name']+' creator preview: '+v['title'],'Creator release/showcase preview'))
  x['videos'].append({'url':v['sourceUrl'],'label':'Original creator release / weapon showcase','evidenceUrl':v['metadataUrl'],'verification':'Author identity, public title and release/showcase metadata checked; full playback not reviewed'})
  x['releaseAnnouncements'].append({'url':v['sourceUrl'],'title':v['title'],'date':iso(v['published']),'kind':'Creator announcement or showcase, not an independently retrieved release file'})
 for field,label,provider in [('creatorLink','Creator project / distribution destination','Creator channel'),('distributionLink','Creator-linked public share','Creator distribution')]:
  if spec.get(field):x['links'].append({'provider':provider,'label':label,'url':spec[field],'verified':False,'verification':'Exact link published by the creator; current file contents and payment terms not independently retrieved','lastChecked':primary['checkedAt'],'kind':'creator-channel'})
 if spec.get('distributionNote'):x['creatorAccessNote']+=' '+spec['distributionNote']
 x['cautions'].append('Video views, video likes and creator follower counts are not gunpack popularity or rating metrics.')
 if spec['id']=='bilibili-BV1kChUzKE3n':
  assert '1.20.1' in mcmod['text'],'TFG declared version source changed'
  x['versions']=['1.20.1'];x['declaredCompatibility']={'minecraft':['1.20.1'],'source':'https://www.mcmod.cn/class/21755.html','basis':'Author-maintained project declaration; no exact file/loader pair'}
  x['authors'].append({'name':'Dzowo','role':'Programmer credited on the project page','url':'https://www.mcmod.cn/class/21755.html'})
 if spec['id']=='bilibili-BV1Q3CvYeEEi':x['activity']='Creator engineering-test edition';x['themes'].append('Experimental / test edition')
 return record

def build_github(spec,repositories,snapshots):
 repo=spec['repository'];proof=repositories[repo];assert proof['id']==int(spec['id'][3:]) and not proof['treeTruncated'] and proof['packMetadata'];source='https://github.com/'+repo;snapshot=snapshots[spec['id']];checked=snapshot['checkedAt'];source_hash=hashlib.sha256(json.dumps(proof,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 record=common(spec,source,'GitHub',{'name':proof['author'],'url':'https://github.com/'+proof['author']},checked,proof['updated'],proof['updated'],source_hash);x=record['item'];x['themes']+=['Historical / retro' if spec['id']=='gh-928434009' else 'Game-inspired','Legacy source reference']
 for path in spec['images']:
  assert path in proof['packPaths'],path
  url='https://raw.githubusercontent.com/'+repo+'/'+proof['branch']+'/'+quote(path,safe='/')
  x['media'].append(archive_image(url,'https://github.com/'+repo+'/blob/'+proof['branch']+'/'+quote(path,safe='/'),spec['name']+' original in-game inventory icon','Creator weapon inventory icon'))
 x['links'].append({'provider':'Source code','label':'Exact TaCZ gunpack manifest','url':source+'/blob/'+proof['branch']+'/'+proof['packMetadata'][0]['path'],'verified':True,'lastChecked':checked})
 if spec['id']=='gh-928434009':
  release=proof['releases'][0];asset=next(a for a in release['assets'] if a['name']=='lmr-1.0.0.zip')
  rel={'id':'github-asset-'+str(asset['id']),'name':asset['name'],'date':release['published_at'],'versions':[],'loaders':[],'channel':'release','url':release['html_url'],'provider':'GitHub','runtimeRequirement':'TaCZ 1.1.4+ according to creator release notes','exactAssetUrl':asset['browser_download_url']}
  x['releases']=[rel];x['latest']=rel;x['latestStable']=rel;x['downloads']=asset['download_count'];x['activity']='Older release / historical reference';record['metric']['downloads']=asset['download_count'];record['metric']['basis']='Download count of the exact firearm ZIP asset only; not repository stars'
  x['links'].append({'provider':'GitHub release','label':'Creator release and gunpack download','url':release['html_url'],'verified':True,'lastChecked':checked})
 else:
  x['activity']='Legacy / discontinued';x['maintenanceNotice']='Discontinued by creator';record['editorial']['maintenance']='Discontinued by creator';x['license']='Code GPL-3.0; assets CC BY-NC-ND 4.0 as declared by creator';x['sourceSnapshot']={'branch':proof['branch'],'updated':proof['updated'],'namespace':proof['packMetadata'][0]['data']['namespace'],'publishedGunIndexes':[p for p in proof['packPaths'] if re.search('/index/guns/.+\\.json$',p)]}
 return record

def ledger(evidence,records,selection):
 discovered=load(evidence/'discovery.json');snapshots=load(evidence/'snapshots.json');old=set(discovered['priorSourceIds'])|set(discovered['representedIds']);overrides=selection['explicitDispositions'];decisions=[]
 for x in discovered['sources']:
  key=x['id'];s=snapshots.get(key,{});value=' '.join([x.get('name',''),x.get('summary','')]).lower()
  if key in records:status,reason='accepted','Exact creator pack source, firearm roster and attributed preview qualified.'
  elif key in old:status,reason='previously researched identity','Reuse previous inclusion/exclusion decision; not counted again.'
  elif key in overrides:status,reason=overrides[key]['status'],overrides[key]['reason']
  elif s.get('error'):status,reason='unresolved source access','The source response did not establish independent firearm content; not treated as proof of absence.'
  elif not re.search(r'tacz|tac.?zero|timeless.{0,25}(zero|classic)|gun.?pack|\u67aa\u5305|\u67aa\u68b0|\u30ac\u30f3',value):status,reason='outside title/summary frontier','Broad keyword collision; no TaCZ firearm-pack signal in the source identity. Not counted as a pack.'
  elif re.search(r'compat|fix|optim|library|api|ammo|npc|loot|recipe|enchant|attachment|skin|shader|hud|scope|recoil|movement|server|modpack|template|tutorial|resource|example|editor|plugin|script|fork|port|animation|curios|knives|knife|armor',value):status,reason='not qualified as gun content','Source identity indicates support, cosmetic content, development or redistribution; no separately verified gun roster promoted.'
  else:status,reason='unresolved source lead','Insufficient distinct creator/release/preview evidence for promotion. Preserved for a future evidence-led check.'
  decisions.append({'id':key,'name':x.get('name'),'url':x.get('url'),'status':status,'reason':reason})
 for key,rec in records.items():
  if key not in {x['id'] for x in discovered['sources']}:decisions.append({'id':key,'name':rec['item']['name'],'url':rec['item']['projectUrl'],'status':'accepted','reason':'Original creator release/test announcement and firearm preview, outside provider listing search.'})
 for key,v in overrides.items():
  if key not in {x['id'] for x in decisions}:decisions.append({'id':key,**v})
 import collections
 summary=load(evidence/'coverage-summary.json');summary.update({'acceptedAdditionalFamilies':len(records),'newEditorialSelections':sum(x['editorial']['shortlist'] for x in records.values()),'decisionCounts':dict(collections.Counter(x['status'] for x in decisions)),'ledgerIdentities':len(decisions),'scope':'Finite provider traversal plus exact creator evidence; not a universal census of inaccessible/private packs','imageGenerationUsed':False,'modBinariesDownloaded':False,'nativeMinecraftRuntimeTested':False})
 save(ROOT/'source-decisions.json',decisions);save(ROOT/'coverage.json',summary)
 save(ROOT/'public-creator-evidence.json',[{'id':k,'name':v['item']['name'],'source':v['item']['projectUrl'],'author':v['item']['authors'],'releaseAnnouncements':v['item']['releaseAnnouncements'],'sourceHash':v['metric']['sourceHash'],'checkedAt':v['item']['checkedAt'],'qualification':v['item']['reviewEvidence']['qualification'],'limits':v['item']['creatorAccessNote']} for k,v in records.items()])
 return summary

def main():
 selection=load(ROOT/'selection.json');existing=load(ROOT/'qualified-records.json')
 if existing and set(existing)=={x['id'] for x in selection['accepted']}:
  print('Reuse all qualified source records and archived previews',flush=True);return
 evidence=restore();videos=load(evidence/'creator-probes.json')['videos'];mcmod=load(evidence/'creator-probes.json')['sourcePages']['https://www.mcmod.cn/class/21755.html'];repositories=load(evidence/'repository-proofs.json');snapshots=load(evidence/'snapshots.json');records={}
 for spec in selection['accepted']:
  record=build_bilibili(spec,videos,mcmod) if spec.get('primary') else build_github(spec,repositories,snapshots)
  assert record['item']['media'];records[spec['id']]=record;save(ROOT/'qualified-records.json',records);print('Qualified',record['item']['name'],len(record['item']['media']),'source previews',flush=True)
 report=ledger(evidence,records,selection);out=ROOT/'qa/media-review';out.mkdir(parents=True,exist_ok=True)
 all_media=[(k,m) for k,v in records.items() for m in v['item']['media']];font=ImageFont.load_default(size=15)
 for start in range(0,len(all_media),16):
  batch=all_media[start:start+16];sheet=Image.new('RGB',(1440,245*((len(batch)+3)//4)),(225,225,225));draw=ImageDraw.Draw(sheet)
  for i,(key,m) in enumerate(batch):
   im=Image.open(PARENT/m['src']).convert('RGBA');im.thumbnail((350,193));x=i%4*360;y=i//4*245;sheet.paste(im,(x,y),im);draw.text((x+3,y+197),records[key]['item']['name'][:43],font=font,fill='black');draw.text((x+3,y+218),m['sha256'][:16],font=font,fill='black')
  sheet.save(out/('options-%02d.jpg'%(start//16+1)),quality=94)
 print(json.dumps(report,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
