#!/usr/bin/env python3
"""Collect public project metadata; never download or execute Minecraft mods."""
from __future__ import annotations
import collections,concurrent.futures,datetime,hashlib,html,io,json,math,re,threading,time,unicodedata
from pathlib import Path
from urllib.parse import quote,urlencode,urljoin,urlparse,parse_qs
from bs4 import BeautifulSoup
from PIL import Image
import research as r
ROOT=r.ROOT
NOW=datetime.datetime(2026,10,23,tzinfo=datetime.timezone.utc)
CF='https://www.curseforge.com'
DEC=json.JSONDecoder()
SEARCHES=[('minecraft','mc-mods',q) for q in ['gun','tacz','point blank','firearm','musket','flan','techguns','warfare','cannon','artillery','railgun','arsenal','modular warfare']]+[('minecraft','customization',q) for q in ['tacz','point blank','gun','flan','modular warfare']]+[('minecraft-bedrock','addons',q) for q in ['gun','firearm','warfare','cannon','blaster']]
GUN=re.compile(r'\b(guns?|gunners?|gunpacks?|firearms?|shotguns?|rifles?|pistols?|revolvers?|muskets?|flintlocks?|blunderbuss|blasters?|miniguns?|railguns?|artillery|cannons?|gunplay|gunsmith|tacz|taczero|techguns|gunpowder revolution)\b|point.?blank|modern warfare|timeless.and.classics|flan.s|scorched.guns',re.I)
NOISE=re.compile(r'\b(gunpowder farm|craftable gunpowder|gunpowder recipe|gunpowder from|gunpowder crafting|more gunpowder|renewable gunpowder|gunpowder block|better gunpowder|gunpowder on|gunpowder drops|craft gunpowder|gunpowder craft|gunpowder.?s)\b',re.I)
SUPPORT={'exception-api-extension','gunsmith-lib','ritchies-projectile-library','pointblank-jelly','tactical-movement','tacz-leawinds-third-person-compats'}
EXTRA=['minecraft/mc-mods/modern-warfare-cubed','minecraft/mc-mods/vics-modern-warfare-mod','minecraft/mc-mods/modular-warfare','minecraft/mc-mods/techguns','minecraft/mc-mods/flans-mod','minecraft/mc-mods/timeless-and-classic-guns-tac','minecraft/mc-mods/immersive-engineering','minecraft/mc-mods/old-guns','minecraft/mc-mods/guns-rpg','minecraft/mc-mods/diamond-caliber','minecraft/mc-mods/ava','minecraft-bedrock/addons/aplok-guns','minecraft-bedrock/addons/actualguns-3d','minecraft/mc-mods/exception-api-extension','minecraft/customization/tacz-immersive-armorer-koei','minecraft/customization/tacz-ars-armorer-koei','minecraft/customization/tacz-create-armorer-koei']

def norm(s):return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',str(s or '')).encode('ascii','ignore').decode().lower()).strip()
def clean(s):return re.sub(r'\s+',' ',BeautifulSoup(str(s or ''),'html.parser').get_text(' ',strip=True)).strip()
def iso(v):
 if isinstance(v,(int,float)):
  try:return datetime.datetime.fromtimestamp(v/1000,datetime.timezone.utc).isoformat()
  except (ValueError,OverflowError):return ''
 return str(v or '')
def rsc(markup):
 soup=BeautifulSoup(markup,'html.parser');parts=[]
 for script in soup.find_all('script'):
  m=re.search(r'self\.__next_f\.push\((\[.*\])\)',script.get_text(),re.S)
  if m:
   try:
    a=json.loads(m.group(1))
    if len(a)>1 and isinstance(a[1],str):parts.append(a[1])
   except (ValueError,IndexError):pass
 return soup,''.join(parts)
def objects(s,key):
 out=[]
 for m in re.finditer('"'+re.escape(key)+'"\s*:',s):
  try:out.append(DEC.raw_decode(s[m.end():].lstrip())[0])
  except ValueError:pass
 return out

def cf_search(game,kind,query,page=1):
 url=CF+'/'+game+'/search?'+urlencode({'page':page,'pageSize':50,'sortBy':'relevancy','class':kind,'search':query})
 response=r.get(url)
 if not response.get('text'):return [],0,{'url':url,'status':response.get('status'),'error':response.get('error')}
 soup,data=rsc(response['text']);projects=[]
 for group in objects(data,'tileProjects'):
  if isinstance(group,list):projects.extend(group)
 unique={}
 for p in projects:
  p['path']=game+'/'+kind+'/'+p['slug'];p['discoveryQuery']=query
  unique[p['id']]=p
 pages=objects(data,'totalPages')
 count=clean(soup.select_one('.results-count') or '')
 return list(unique.values()),max([int(x) for x in pages if isinstance(x,(int,float))]+[1]),{'url':url,'status':response.get('status'),'resultsText':count,'read':len(unique)}

def discover_cf():
 path=ROOT/'discovery-curseforge.json';ledgerpath=ROOT/'discovery-cf-ledger.json'
 previous=r.load(ledgerpath,[]);done={(x['game'],x['class'],x['query']) for x in previous if x.get('terminalPageReached')}
 found={x['id']:x for x in r.load(path,[])};ledger=[x for x in previous if (x['game'],x['class'],x['query']) in done]
 for game,kind,query in SEARCHES:
  if (game,kind,query) in done:continue
  hits,pages,ev=cf_search(game,kind,query);evidence=[ev]
  for p in hits:found.setdefault(p['id'],p)
  complete=bool(hits or '0 Projects' in ev.get('resultsText',''));total=len(hits)
  if pages>1:
   with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    for hs,_,proof in pool.map(lambda p:cf_search(game,kind,query,p),range(2,pages+1)):
     evidence.append(proof);total+=len(hs)
     if not hs:complete=False
     for p in hs:found.setdefault(p['id'],p)
  ledger.append({'game':game,'class':kind,'query':query,'pages':pages,'read':total,'terminalPageReached':complete,'evidence':evidence})
  r.save(path,list(found.values()));r.save(ledgerpath,ledger)
  print('CF discovery',game,kind,query,total,'unique',len(found),flush=True)
 return list(found.values())

def relevant(name,summary,slug='',seed=False):
 text=name+' '+summary
 if slug in SUPPORT:return True,'Explicit weapon tooling dependency'
 if NOISE.search(text) and not GUN.search(name):return False,'Gunpowder resource/recipe, not a firearm project'
 if GUN.search(text):return True,'Named firearm, gun ecosystem or artillery content'
 return False,'No firearm-specific identity in project title or summary'

def kind_for(name,summary,path,body=''):
 s=norm(name+' '+summary);short=norm(name);b=norm(body[:4000])
 if 'minecraft-bedrock' in path:return 'Bedrock add-on'
 if 'resourcepack' in path or 'texture-packs' in path:return 'Visual / resource pack'
 if 'customization' in path or 'mc-addons' in path or re.search(r'gun.?pack|content.?pack',short):return 'Gun / content pack'
 if 'datapack' in path or ('datapack' in s and 'tacz' not in s and 'point blank' not in s):return 'Datapack / command weapon'
 if re.search(r'library|api extension|gunsmith lib|jelly|projectile library',short):return 'Tooling / framework support'
 if re.search(r'compat|optimization|optimised|optimized|performance|rendering|fixes|fix |scope overhaul|third person|first person|shader|hud|information|presence|durability|attribute|ammo drops|enchant|spelltrigger|arsarms|ironsarms|arcanemag|spell trigger|integration|slings|turret tacz|tacz turrets|gun displays|gun display|wall displayed|gunsandtargets|sound attracts|warden|blueprint|tacz.*(ammo|recoil|hostile|npc|mobs|curio|tweaks|expert|level|armor|labo|lab |refit|creative|light|stamina|bullet|pickup|progression|skin|golem|packs upgrader)',s):return 'Integration / handling / QoL'
 if re.search(r'cannons?|artillery|warfare|warium|missiles?|mcheli|tanks?|naval|siege|warships',short) and not re.search(r'modern warfare|modular warfare',short):return 'Artillery / combined arms'
 return 'Standalone gun mod'

def ecosystem(name,summary,path):
 s=norm(name+' '+summary+' '+path)
 for pattern,label in [(r'tacz|taczero|timeless and classics zero','TaCZ'),(r'point blank|pointblank|\bvpb\b|\bpbj\b','Point Blank'),(r'just enough guns|\bjeg\b|mo than enough','Just Enough Guns'),(r'scorched guns|scorch','Scorched Guns'),(r'flan','Flan\'s'),(r'modular warfare','Modular Warfare'),(r'modern warfare cubed|vics modern warfare','Modern Warfare'),(r'mrcrayfish|\bcgm\b|\bcgc\b|gun crayfish','Crayfish / CGM'),(r'create|\bcbc\b','Create'),(r'superb warfare|\bsbw\b','Superb Warfare'),(r'warium','Warium'),(r'techguns','Techguns')]:
  if re.search(pattern,s):return label
 return 'Independent'

def video_links(body,base):
 urls=[]
 for raw in re.findall(r'https?://[^\s<>"\)\]]+',body):
  u=html.unescape(raw).rstrip('.,;');p=urlparse(u)
  vid=''
  if p.netloc in ('youtu.be','www.youtu.be'):vid=p.path.strip('/').split('/')[0]
  if 'youtube.com' in p.netloc:
   if p.path=='/watch':vid=parse_qs(p.query).get('v',[''])[0]
   elif p.path.startswith(('/embed/','/shorts/')):vid=p.path.split('/')[2]
  if re.fullmatch(r'[A-Za-z0-9_-]{11}',vid):u='https://www.youtube.com/watch?v='+vid
  elif not ('bilibili.com/video/' in u or 'vimeo.com/' in u):continue
  if u not in [x['url'] for x in urls]:urls.append({'url':u,'label':'Creator-linked video','evidenceUrl':base,'verification':'Linked on project page; full playback not reviewed'})
 return urls

def cf_release(obj,base):
 flavors=obj.get('flavors') or ([obj['flavor']] if obj.get('flavor') else [])
 return {'id':'cf-file-'+str(obj['id']),'name':obj.get('displayName') or obj.get('fileName'),'date':iso(obj.get('dateCreated')),'versions':obj.get('gameVersions',[]),'loaders':[x['name'] for x in flavors if isinstance(x,dict) and x.get('name')],'channel':{1:'release',2:'beta',3:'alpha'}.get(obj.get('releaseType'),'unknown'),'url':base+'/files/'+str(obj['id']),'provider':'CurseForge'}

def cf_project(path,seed_rows=None):
 base=CF+'/'+path;response=r.get(base)
 if not response.get('text'):return None,{'url':base,'status':response.get('status'),'error':response.get('error')}
 soup,data=rsc(response['text']);projects=[x for x in objects(data,'project') if isinstance(x,dict) and x.get('id') and x.get('slug')]
 if not projects:return None,{'url':base,'error':'Official project metadata not found'}
 obj=projects[0];canonical=soup.find('link',rel='canonical')
 if canonical and canonical.get('href'):base=canonical['href'].rstrip('/');path=urlparse(base).path.strip('/')
 description=soup.select_one('.project-description');body=str(description or '');plain=clean(description or '')
 ok,reason=relevant(obj['name'],obj.get('summary','')+' '+plain[:800],obj['slug'],bool(seed_rows))
 if not ok:return None,{'url':base,'name':obj['name'],'rejected':reason}
 files={}
 for grp in obj.get('latestFiles',[]):
  for x in grp.get('files',[]):files[x['id']]=x
 if obj.get('mainFile'):files[obj['mainFile']['id']]=obj['mainFile']
 # Public file list identifies actual current release and preserves version/loader pairs.
 rf=r.get(base+'/files/all?page=1&pageSize=50&showAlphaFiles=show&sortBy=dateCreated&sortOrder=desc')
 if rf.get('text'):
  _,fd=rsc(rf['text'])
  for arr in objects(fd,'files'):
   if isinstance(arr,list):
    for x in arr:
     if isinstance(x,dict) and x.get('id') and x.get('fileName'):files[x['id']]=x
 releases=sorted([cf_release(x,base) for x in files.values()],key=lambda x:x['date'],reverse=True)
 galleries=[]
 if description:
  for im in description.find_all('img'):
   url=im.get('src','');alt=im.get('alt','')
   if not url.startswith('http') or re.search(r'badge|shields.io|discord|patreon|bisect|apexhosting|ko-fi|donat|logo|support|banner',url+' '+alt,re.I):continue
   galleries.append({'url':url,'alt':alt or obj['name']+' creator image','role':'Creator description image','sourceUrl':base})
 for im in soup.select('.carousel img, .screenshots img, .project-gallery img'):
  url=im.get('src','')
  if url.startswith('http'):galleries.append({'url':url,'alt':im.get('alt',obj['name']),'role':'Project gallery','sourceUrl':base+'/gallery'})
 authors=[{'name':x['name'],'role':x.get('role',''),'url':CF+'/members/'+quote(x['name']),'avatar':(x.get('avatarAssets') or {}).get('asset150x150')} for x in obj.get('members',[]) if x.get('name')]
 if not authors and obj.get('author'):authors=[{'name':obj['author']['name'],'url':CF+'/members/'+quote(obj['author']['name'])}]
 dependencies=[]
 for x in files.values():
  for dep in x.get('relatedProjects',[]):
   if dep not in dependencies:dependencies.append(dep)
 all_urls=re.findall(r'https?://[^\s<>"\)\]]+',body)
 links=[{'provider':'CurseForge','label':'Project & downloads','url':base,'verified':True,'lastChecked':response['checkedAt']}]
 for label,key in [('Source code','sourceUrl'),('Wiki','wikiUrl'),('Issue tracker','issuesUrl')]:
  if obj.get(key):links.append({'provider':label,'label':label,'url':obj[key],'verified':False,'verification':'Linked by project author','lastChecked':response['checkedAt']})
 cross=[u.rstrip('/.,;') for u in all_urls if 'modrinth.com/' in u]
 item={'id':'cf-'+str(obj['id']),'providerIds':{'curseforge':obj['id']},'name':obj['name'],'slug':obj['slug'],'summary':obj.get('summary',''),'description':plain,'authors':authors,'type':kind_for(obj['name'],obj.get('summary',''),path,plain),'ecosystem':ecosystem(obj['name'],obj.get('summary',''),path),'edition':'Bedrock' if path.startswith('minecraft-bedrock') else 'Java','projectUrl':base,'links':links,'crosslinks':cross,'provider':'CurseForge','icon':obj.get('avatarUrl'),'gallery':galleries,'videos':video_links(body,base),'releases':releases,'versions':sorted(set(v for x in releases for v in x['versions'])),'loaders':sorted(set(v for x in releases for v in x['loaders'])),'updated':iso(obj.get('updateDate')),'created':iso(obj.get('dateCreated')),'downloads':obj.get('downloads',0),'license':obj.get('licenseType') or 'Not specified','dependencies':dependencies,'sourceRows':seed_rows or [],'checkedAt':response['checkedAt'],'evidence':{'project':base,'releaseList':base+'/files/all','releaseScope':'First 50 recent files plus provider latest-per-version files; not an exhaustive historical file archive','summaryHash':hashlib.sha256(response['text'].encode()).hexdigest()},'tags':[x['name'] for x in obj.get('categories',[])]}
 if re.search(r'image.{0,15}(made by ai|generated|created using ai)|ai.generated',plain,re.I):item['mediaCaution']='Creator discloses AI imagery; project icon retained only as a logo, not gameplay evidence';item['gallery']=[]
 return item,None

def mr_project(project,hit=None):
 pid=project['id'];base='https://modrinth.com/'+project.get('project_type','mod')+'/'+project['slug'];body=project.get('body','');name=project['title'];summary=project.get('description','')
 ok,reason=relevant(name,summary+' '+clean(body)[:800],project['slug'])
 if not ok:return None,{'url':base,'name':name,'rejected':reason}
 ver=r.get('https://api.modrinth.com/v2/project/'+pid+'/version');releases=[]
 for v in ver.get('json',[]) if isinstance(ver.get('json'),list) else []:
  releases.append({'id':'mr-version-'+v['id'],'name':v.get('name') or v.get('version_number'),'date':v.get('date_published',''),'versions':v.get('game_versions',[]),'loaders':v.get('loaders',[]),'channel':v.get('version_type','unknown'),'url':base+'/version/'+v['id'],'provider':'Modrinth','dependencies':v.get('dependencies',[])})
 releases.sort(key=lambda x:x['date'],reverse=True)
 pairs=set();selected=[]
 for v in releases:
  fresh={(mc,loader) for mc in v['versions'] for loader in (v['loaders'] or ['Unspecified'])}-pairs
  if fresh or len(selected)<8:selected.append(v);pairs|=fresh
 galleries=[{'url':x['url'],'alt':x.get('title') or name+' gallery','role':'Project gallery','sourceUrl':base+'/gallery','featured':x.get('featured',False)} for x in project.get('gallery',[])]
 galleries.sort(key=lambda x:not x['featured'])
 links=[{'provider':'Modrinth','label':'Project & downloads','url':base,'verified':True,'lastChecked':ver['checkedAt']}]
 for label,key in [('Source code','source_url'),('Wiki','wiki_url'),('Issue tracker','issues_url')]:
  if project.get(key):links.append({'provider':label,'label':label,'url':project[key],'verified':False,'verification':'Linked by project author','lastChecked':ver['checkedAt']})
 cross=re.findall(r'https?://(?:www\.)?curseforge.com/(?:minecraft|minecraft-bedrock)/[^\s<>"\)\]]+',body)
 author=(hit or {}).get('author') or project.get('organization') or 'See project credits'
 item={'id':'mr-'+pid,'providerIds':{'modrinth':pid},'name':name,'slug':project['slug'],'summary':summary,'description':clean(body),'authors':[{'name':str(author),'url':'https://modrinth.com/user/'+quote(str(author))}],'type':kind_for(name,summary,project.get('project_type',''),body),'ecosystem':ecosystem(name,summary,project['slug']),'edition':'Java','projectUrl':base,'links':links,'crosslinks':[x.rstrip('/.,;') for x in cross],'provider':'Modrinth','icon':project.get('icon_url'),'gallery':galleries,'videos':video_links(body,base),'releases':selected,'versions':project.get('game_versions',[]),'loaders':project.get('loaders',[]),'updated':project.get('updated',''),'created':project.get('published',''),'downloads':project.get('downloads',0),'license':(project.get('license') or {}).get('id','Not specified'),'dependencies':(releases[0].get('dependencies',[]) if releases else []),'sourceRows':[],'checkedAt':ver['checkedAt'],'evidence':{'project':base,'releaseList':base+'/versions','releaseScope':'All published version metadata read; latest file for each supported version/loader combination retained','releaseCount':len(releases)},'tags':project.get('categories',[])}
 return item,None

def media(item):
 assets=ROOT/'assets';assets.mkdir(exist_ok=True)
 choices=[]
 if item.get('icon'):choices.append({'url':item['icon'],'alt':item['name']+' project logo','role':'Project icon','sourceUrl':item['projectUrl']})
 choices+=item.get('gallery',[])
 result=[];seen=set()
 # All listed project gallery media are preserved in metadata; archive thumbnails for initial cards and gallery.
 for candidate in choices:
  u=candidate['url']
  if u in seen:continue
  seen.add(u);key=hashlib.sha256(u.encode()).hexdigest()[:24];dest=assets/(key+'.webp');meta=assets/(key+'.json')
  if dest.exists() and meta.exists():result.append(r.load(meta));continue
  try:
   import requests
   response=requests.get(u,headers={'User-Agent':r.UA},timeout=(8,22))
   if not response.ok or len(response.content)>25000000:continue
   im=Image.open(io.BytesIO(response.content));size=im.size
   if min(size)<28 or max(size)<64:continue
   if candidate['role']!='Project icon' and (size[0]/max(1,size[1])>6 or size[1]/max(1,size[0])>7):continue
   im.seek(0);im.thumbnail((1000,700));im=im.convert('RGBA' if im.mode in ('RGBA','P') else 'RGB');im.save(dest,'WEBP',quality=86,method=4)
   record={**candidate,'src':'assets/'+dest.name,'width':im.width,'height':im.height,'originalDimensions':list(size),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'bytes':dest.stat().st_size}
   r.save(meta,record);result.append(record)
  except Exception:continue
 item['media']=result
 return item

def merge(items):
 byid={x['id']:x for x in items};bycf={str(x['providerIds']['curseforge']):x['id'] for x in items if x['providerIds'].get('curseforge')};byurl={x['projectUrl'].lower().rstrip('/'):x['id'] for x in items};byslug=collections.defaultdict(list)
 for x in items:byslug[norm(x['name'])].append(x['id'])
 redirects={};records=[]
 for x in list(items):
  if x['id'] in redirects:continue
  candidates=[]
  for url in x.get('crosslinks',[]):
   other=byurl.get(url.lower().split('?')[0].rstrip('/'))
   if other and other!=x['id']:candidates.append((other,'Author-linked cross-provider project'))
  for other in byslug[norm(x['name'])]:
   if other==x['id'] or byid[other]['provider']==x['provider']:continue
   y=byid[other];a={norm(v['name']) for v in x['authors']};b={norm(v['name']) for v in y['authors']}
   if a&b:candidates.append((other,'Exact normalized project name and creator identity'))
  for other,reason in candidates:
   if other in redirects:continue
   y=byid[other]
   if y['edition']!=x['edition']:continue
   # Prefer CurseForge identity for long-standing seed continuity; keep all release records and homes.
   target,source=(x,y) if x['provider']=='CurseForge' else (y,x)
   if target['id'] in redirects:continue
   target['providerIds'].update(source['providerIds']);target['links']+=source['links'];target['releases']+=source['releases'];target['videos']+=source['videos'];target['media']+=source.get('media',[]);target['sourceRows']=sorted(set(target['sourceRows']+source['sourceRows']));target['versions']=sorted(set(target['versions']+source['versions']));target['loaders']=sorted(set(target['loaders']+source['loaders']));target.setdefault('providerEvidence',[]).append({'id':source['id'],'url':source['projectUrl'],'updated':source['updated'],'downloads':source['downloads'],'evidence':source['evidence']});target['downloads']=max(target['downloads'],source['downloads']);target['releases'].sort(key=lambda q:q['date'],reverse=True)
   target['media']=list({m['sha256']:m for m in target['media']}.values());target['links']=list({q['url']:q for q in target['links']}.values());target['videos']=list({q['url']:q for q in target['videos']}.values());redirects[source['id']]=target['id'];records.append({'from':source['id'],'to':target['id'],'reason':reason})
 return [x for x in items if x['id'] not in redirects],records

def decorate(item):
 s=norm(item['name']+' '+item['summary']+' '+item['description'][:8000]);themes=[]
 for pattern,label in [(r'magic|spell|ars nouveau|ars armorer|iron.?s spell','Magic & spells'),(r'create|steampunk|diesel|industrial','Mechanical / industrial'),(r'sci fi|science fiction|halo|destiny|helldiver|laser|plasma|railgun','Science fiction'),(r'vanilla|pixel|blocky','Minecraft-styled'),(r'world war|ww1|ww2|musket|flintlock|historic|western|cowboy','Historical / retro'),(r'animation|animated|reload|inspect','Animation & handling'),(r'attachments|customization|customisation|modular','Modularity & attachments'),(r'craft|survival|progression','Survival progression'),(r'creatures|mobs|enemies|hostile|patrol','Armed mobs / encounters'),(r'optim|performance|fps','Performance / integration')]:
  if re.search(pattern,s):themes.append(label)
 item['themes']=themes
 item['earlierPick']=any(x in s for x in ('create armorer','immersive armorer','ars armorer','cyber armorer','applied armorer','tti gun','gucci attachment','helldivers2 gun pack by koei','hell divers2','heavy recoil','exception api extension'))
 item['curation']='Earlier pick' if item['earlierPick'] else 'Research discovery'
 anchors=['timeless-and-classics-zero','vics-point-blank','scorched-guns','just-enough-guns','superb-warfare','aplok-guns','actualguns-3d','create-big-cannons','create-love-war','warium','musket-mod','modern-warfare-cubed','techguns','modular-warfare','guns-without-roses','arsarms','ironsarms','flans-mod-reloaded','pointblank-jelly']
 if item['slug'] in anchors:item['curation']='Study anchor'
 item['studyPriority']=100 if item['earlierPick'] else 95 if item['curation']=='Study anchor' else 75 if item['type'] in ('Standalone gun mod','Artillery / combined arms') and item['downloads']>=100000 else 65 if item['type']=='Gun / content pack' and item['downloads']>=50000 else 50
 item['priorityBasis']='Editorial research ordering, not an in-game quality/performance benchmark'
 directions={'Magic & spells':'Study how spell identity changes silhouettes, resource feedback and projectile presentation while preserving AoA resources.','Mechanical / industrial':'Study visible moving parts, material consistency and readable charging/reload sequences.','Science fiction':'Compare energy effects and unconventional weapon silhouettes with AoA realm-specific blasters.','Minecraft-styled':'Compare block-scale geometry, readable colors and first/third-person proportions.','Historical / retro':'Study period-inspired shapes and distinctive action/reload rhythms.','Animation & handling':'Review draw, firing, reload, inspect and third-person clips in actual footage before adopting a technique.','Modularity & attachments':'Study attachment visibility, authoring workflow and reversible customization.','Survival progression':'Compare crafting, ammunition and progression without replacing native AoA resource rules.','Armed mobs / encounters':'Study encounter readability and server-authoritative weapon state rather than assuming cross-mod compatibility.','Performance / integration':'Inspect the specific compatibility claim and reproduce it on a pinned version before using it.'}
 item['inspiration']=[directions[t] for t in themes[:3]] or ['Inspect the project-specific weapon shapes and feedback as an original AoA design reference.']
 item['latest']=item['releases'][0] if item['releases'] else None
 item['latestStable']=next((x for x in item['releases'] if x['channel']=='release'),None)
 date=(item['latest'] or {}).get('date') or item.get('updated')
 try:age=(NOW-datetime.datetime.fromisoformat(date.replace('Z','+00:00'))).days
 except Exception:age=None
 item['activity']='Updated within 90 days' if age is not None and age<=90 else 'Updated within a year' if age is not None and age<=365 else 'Older release / legacy reference' if age is not None else 'Date not established'
 item['cautions']=[]
 if re.search(r'unofficial|fork|port',norm(item['name']+' '+item['summary'])):item['cautions'].append('Unofficial fork/port or separate continuation; do not combine it with its parent without checking exact release instructions.')
 if item['type']=='Gun / content pack':item['cautions'].append('Content pack, not a standalone firearm runtime. Match the required base mod and pack release.')
 if item['edition']=='Bedrock':item['cautions'].append('Bedrock reference, not a Java mod. Check behavior/resource pack pairing and current creator requirements.')
 if not item['releases']:item['cautions'].append('No exact downloadable release was established from the fetched metadata.')
 if item.get('mediaCaution'):item['cautions'].append(item['mediaCaution'])
 item['cautions'].append('Catalog verification is source metadata and media validation, not native Minecraft compatibility or performance testing.')
 item['descriptionExcerpt']=item['description'][:1000];del item['description']
 return item

def main():
 cf=discover_cf();seedrows=collections.defaultdict(list);seedpaths=set(EXTRA);mrseeds=set();seed_evidence=[]
 for line in (ROOT/'seed-projects.tsv').read_text().splitlines():
  if not line or line.startswith('#'):continue
  key,rows=line.split('\t');rownums=[int(x) for x in rows.split(',') if x.isdigit()]
  if key.startswith('cf/'):
   path=key[3:];seedpaths.add(path);seedrows[path]+=rownums
  elif key.startswith('mr/'):mrseeds.add(key.rsplit('/',1)[1])
  seed_evidence.append({'seed':key,'sourceRows':rownums})
 paths={p['path'] for p in cf if relevant(p['name'],p.get('summary',''),p.get('slug',''))[0]}|seedpaths
 rejected=[];raw=r.load(ROOT/'raw-projects.json',{});pending=r.load(ROOT/'pending-projects.json',{})
 work=[x for x in sorted(paths) if 'cf:'+x not in raw and 'cf:'+x not in pending]
 print('Collect CF project pages:',len(work),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  futures={pool.submit(cf_project,path,sorted(set(seedrows[path]))):path for path in work}
  for i,ft in enumerate(concurrent.futures.as_completed(futures),1):
   key='cf:'+futures[ft]
   try:item,error=ft.result()
   except Exception as exc:item=None;error={'url':CF+'/'+futures[ft],'error':type(exc).__name__+': '+str(exc)}
   if item:raw[key]=item
   else:pending[key]=error
   if i%25==0 or i==len(work):r.save(ROOT/'raw-projects.json',raw);r.save(ROOT/'pending-projects.json',pending);print('CF details',i,'/',len(work),'accepted',len(raw),flush=True)
 hits=r.load(ROOT/'discovery-modrinth.json',[]);hmap={x['project_id']:x for x in hits};ids=[x['project_id'] for x in hits if relevant(x['title'],x.get('description',''),x['slug'])[0]]
 details={}
 for start in range(0,len(ids),80):
  response=r.get('https://api.modrinth.com/v2/projects?'+urlencode({'ids':json.dumps(ids[start:start+80])}))
  for obj in response.get('json',[]) if isinstance(response.get('json'),list) else []:details[obj['id']]=obj
 for slug in sorted(mrseeds):
  if any(x['slug']==slug for x in details.values()):continue
  res=r.get('https://api.modrinth.com/v2/project/'+slug)
  if isinstance(res.get('json'),dict) and res['json'].get('id'):details[res['json']['id']]=res['json']
 work=[x for x in details.values() if 'mr:'+x['id'] not in raw and 'mr:'+x['id'] not in pending]
 print('Collect Modrinth release metadata:',len(work),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
  futures={pool.submit(mr_project,obj,hmap.get(obj['id'])):obj for obj in work}
  for i,ft in enumerate(concurrent.futures.as_completed(futures),1):
   obj=futures[ft];key='mr:'+obj['id']
   try:item,error=ft.result()
   except Exception as exc:item=None;error={'url':'https://modrinth.com/project/'+obj['id'],'error':str(exc)}
   if item:raw[key]=item
   else:pending[key]=error
   if i%25==0 or i==len(work):r.save(ROOT/'raw-projects.json',raw);r.save(ROOT/'pending-projects.json',pending);print('MR details',i,'/',len(work),flush=True)
 work=[x for x in raw.values() if 'media' not in x]
 with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
  futures={pool.submit(media,x):x for x in work}
  for i,ft in enumerate(concurrent.futures.as_completed(futures),1):
   try:ft.result()
   except Exception as exc:print('Media error',str(exc),flush=True)
   if i%50==0 or i==len(work):r.save(ROOT/'raw-projects.json',raw);print('Media archived',i,'/',len(work),flush=True)
 items,merges=merge(list(raw.values()));items=[decorate(x) for x in items]
 items.sort(key=lambda x:(-x['studyPriority'],-x['downloads'],x['name'].lower()))
 snapshot={'schemaVersion':1,'catalogId':'aoa-minecraft-gun-mod-inspirations','title':'Minecraft Gun Mod Inspirations','generatedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checkedDate':'2026-10-23','sources':[{'role':'Read-only original seeds','provider':'Google Sheets','id':'11LhBV_M7zIxVPkKdYhxmA-bAKOwT79JekqQNc2LJzak','url':'https://docs.google.com/spreadsheets/d/11LhBV_M7zIxVPkKdYhxmA-bAKOwT79JekqQNc2LJzak/edit','modified':'2026-10-23T06:36:42.853Z'},{'role':'Current project and release evidence','provider':'Modrinth API / official CurseForge project pages'}],'items':items,'build':{'generator':'collect.py v1','sourceRevision':__import__('os').environ.get('GITHUB_SHA','local'),'itemCount':len(items),'dataHash':hashlib.sha256(json.dumps(items,ensure_ascii=False,sort_keys=True).encode()).hexdigest()},'coverage':{'modrinthSearchHits':len(hits),'curseforgeSearchHits':len(cf),'sourceRecordsAccepted':len(raw),'crossProviderMerges':len(merges),'publishedProjects':len(items),'unresolvedSources':sum(not x.get('rejected') for x in pending.values()),'excludedSources':sum(bool(x.get('rejected')) for x in pending.values()),'mediaProjects':sum(bool(x.get('media')) for x in items),'directVideoProjects':sum(bool(x['videos']) for x in items),'types':dict(collections.Counter(x['type'] for x in items)),'editions':dict(collections.Counter(x['edition'] for x in items)),'scope':'Extensive finite source search, not a claim to enumerate every Minecraft weapon project or certify native compatibility.'}}
 r.save(ROOT/'catalog.json',snapshot);r.save(ROOT/'deduplication.json',merges);r.save(ROOT/'seed-provenance.json',seed_evidence)
 print(json.dumps(snapshot['coverage'],indent=2),flush=True)
if __name__=='__main__':main()
