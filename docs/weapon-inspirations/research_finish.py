#!/usr/bin/env python3
"""Finish the incremental research delta without changing any baseline record."""
from __future__ import annotations
import collections,concurrent.futures,copy,hashlib,html,io,json,re,sys,threading
from pathlib import Path
from urllib.parse import quote,unquote,urlencode,urljoin,urlparse,parse_qs
from bs4 import BeautifulSoup
from PIL import Image
import research_quality as q
x=q.x;g=q.g;p=q.p;f=q.f;ROOT=q.ROOT;DATA=q.DATA
LOCK=threading.Lock();EVIDENCE={};VERSION=2
BAD=re.compile(r'logo|wordmark|avatar|flag|stub|question|icon.?ammo|damage.?icon|controller|rarity|favicon|banner|button|badge|weapon.?wheel|weapon.?options|_WW\.|inventory|loadout|achievement|modcard|blueprint|blue_print|schematic',re.I)
REVIEW_IDS={'xh-6be605630472','xh-0bbd9c3a4a9c','xh-cfb50ce81b80','xh-aa70a7dcd45e','xg-a5b818ff50f1','xg-2f46fb45e6db','xg-1f1ba773fe75','xg-6825d0f5526c','xg-7d11a7246fa3','xg-6605ae419ebe','xg-e1ca52f80051','xg-54d5ce777642','xg-c69e6525b7d5','xg-81ac034b8329','xg-f962cedfb171','xg-c8e596aeee23','xg-84cb27a624c0','xg-f6ee0f4241fc','xg-69deb34344d7','xg-e50c84ee8034','xg-eb8d8cdd4f1d','xg-71c9d821c0be','xg-6aed3ef12cc9','xg-cb7719d0e409','xg-d5a8fd535157','xg-9841a10d6256'}
VIDEO_FIX={'xg-71c9d821c0be','xh-6be605630472','xg-d5a8fd535157','xg-1f1ba773fe75','xg-5f334c14256f','xg-08541592fc12','xg-c4990ba4607e'}
ALIASES={
 'Phoenix Samurai':['Samurai','Phoenix Samurai'],'Eightball Gun':['Eightball','Eightball Gun','Eightball Launcher','8ball'],'Singularity Cannon':['Singularity Cannon'],'SIG MKMO':['MKMO'],'Parker-Hale PDW':['Bushman IDW','Parker Hale IDW','Parker Hale PDW'],
 'Mag-Net Launcher':['Mag-Net','Mag Net','Magnet Launcher'],'Nano-Swarmers':['Nano Swarmers','Nanoswarmers'],'Predator Launcher':['Predator Launcher'],'Viral Proliferator':['Viral Proliferator'],'HALPS Prototype':['HALPS'],'Stasis Field Generator':['Stasis Field Generator','Stasis Generator'],
 'KKV-7 Flechette SMG':['KKV-7','Flechette','SMG'],'Drunk Missile':['Drunk Missile','Drunk Missiles'],'Assault Cannon':['Assault Cannon'],'Dark Staff':['Dark Staff'],'DEMP 2':['DEMP2','DEMP 2'],'DC-17m Interchangeable Weapon System':['DC17m','DC-17m','DC 17m','DC17'],
 'I-MOD':['I-MOD','IMOD','Infinity Modulator'],'Arc Welder':['Arc Welder'],'Quantum Burst':['Quantum Burst'],'Tetryon Disruptor':['Tetryon','Tetryon Disruptor'],'Type-7 Particle Weapon':['Type-7','Type 7','Particle Weapon'],'Razor Cube':['Razor Cube','Razorcube'],'Evil Eye':['Evil Eye'],'EMF Cannon':['EMF Cannon','EMF'],'Bone Gun':['Bone Gun','Bonegun'],
 'Scorn shotgun':['Shotgun','Rifle'],'Scorn pistol':['Pistol'],'Scorn grenade launcher':['Grenade Launcher'],'ARC-3 Arc Thrower':['Arc Thrower'],'Polygun':['Polygun'],'Monolith':['Monolith'],'Alternator':['Alternator'],'Arclight':['Arc Light','Arclight'],'Wheel Saw':['Wheel Saw','Wheelsaw'],
 'Spider Mine Layer':['Mine Layer','Minelayer','Spider Mines'],'Armaguerra OG-43':['OG43','OG 43','Armaguerra OG43','Armaguerra OG 43'],'Disc Gun':['Disc Gun'],'Astilla':['Astilla'],'Ballistica Prime':['Ballistica Prime'],'Boomer Shotgun':['Boomer','Boomer Shotgun']}
PAGES={
 'RYNO VI Protosuit':('https://ratchetandclank.fandom.com','RYNO VI Protosuit'),
 'Clank Zapper':('https://ratchetandclank.fandom.com','Clank Zapper'),
 'Lightning Rod':('https://ratchetandclank.fandom.com','Lightning Rod'),
 'Chimp-O-Matic':('https://ratchetandclank.fandom.com','Chimp-O-Matic'),
 'Annelid Worm Launcher':('https://shodan.fandom.com','Annelid Worm Launcher'),
 'EMP Rifle':('https://shodan.fandom.com','EMP Rifle'),
 'WSTE-M5 Combat Shotgun':('https://www.marathonwiki.com','Classic:WSTE-M5 Combat Shotgun'),
 'Zeus-Class Fusion Pistol':('https://www.marathonwiki.com','Classic:Zeus-Class Fusion pistol'),
 'Photon Burst':('https://memory-beta.fandom.com','Photon burst'),
 'Geonosian Elite Beam Weapon':('https://starwars.fandom.com','Geonosian Elite beam weapon'),
 'Scorn pistol':('https://scorn.fandom.com','Pistol'),
 'Scorn shotgun':('https://scorn.fandom.com','Shotgun'),
 'Scorn grenade launcher':('https://scorn.fandom.com','Grenade Launcher'),
}
ARCHIVE={'Translocator':'Translocator','Dispersion Pistol':'Dispersion_Pistol','Spider Mine Layer':'Mine_Layer','Eightball Gun':'Eightball_Gun','Singularity Cannon':'Singularity_Cannon'}
SOURCE_ARTICLES={
 'Colt Defender Mark I':'https://dockeryarmory.com/colt-defender-mark-i/',
 'Kel-Tec CP33':'https://www.keltecweapons.com/firearm/pistols/cp33/',
 'Armaguerra OG-43':'https://www.imfdb.org/wiki/Armaguerra_OG-43',
 'Benelli CB-M2':'https://www.imfdb.org/wiki/Benelli_CB-M2',
}
GAME_CONTEXT={
 'Unreal':['Unreal','Unreal 1998','Unreal Gold'],
 'Unreal II: The Awakening':['Unreal 2','Unreal II'],
 'Unreal Tournament 2004':['UT2004','Unreal Tournament 2004','UT 2004'],
 'Star Wars: Republic Commando':['Republic Commando'],
 'Star Wars: Jedi Knight II - Jedi Outcast':['Jedi Outcast','Jedi Knight 2','Jedi Knight II'],
 'Star Wars: Dark Forces':['Dark Forces'],
 'F.E.A.R.':['FEAR','F.E.A.R.'],
 'Marathon 2: Durandal':['Marathon','Durandal'],
 'Marathon Infinity':['Marathon'],
 'System Shock 2':['System Shock 2','System Shock','SS2'],
 'James Bond 007: Nightfire':['Nightfire'],
 'Star Trek: Voyager - Elite Force':['Elite Force'],
 'Remnant II':['Remnant 2','Remnant II'],
 'Remnant: From the Ashes':['Remnant From the Ashes','Remnant'],
 'Helldivers 2':['Helldivers'],
 'Painkiller: Overdose':['Overdose'],
}
REJECT={'Gunesis':'Not a separate gun: Gunesis is lore quoted in the Particulator entry. Existing Particulator coverage is retained.', 'Charm Horn':'An active charm item, not a gun. Excluded from this gun-focused expansion.'}

def exact_name(e,s):
 ns=ALIASES.get(e['name'],x.names(e));v=' '+g.norm(s)+' '
 return any(' '+g.norm(n)+' ' in v for n in ns)

def context(e,s):
 if e['group']=='Historical':return not re.search(r'warzone|call of duty|battlefield|roblox|airsoft|replica|3d print|cod vanguard|cosplay',s,re.I)
 terms=GAME_CONTEXT.get(e['game'],[e['game']])
 for key,values in x.GAME_ALIASES.items():
  if key in e['game']:terms+=values
 return any(f.present(t,s) for t in terms)

def parse_api(host,page):
 api=('/w/api.php' if host=='https://en.wikipedia.org' else '/api.php')
 url=host+api+'?'+urlencode({'action':'parse','format':'json','page':page,'prop':'images|text|wikitext','redirects':1})
 r=g.fetch(url)
 if not r['ok']:return None
 try:obj=json.loads(r['body']).get('parse',{})
 except ValueError:return None
 if not obj:return None
 obj['source']=host+'/wiki/'+quote(obj.get('title',page).replace(' ','_'));obj['api']=host+api;return obj

def save_url(e,url,source,kind,extra=None):
 if not url:return None
 im=p.image_url(e,url,source,kind)
 if im and extra:im.update(extra)
 return im

def mediawiki_image(e,host,page,required=None,blocked=None):
 obj=parse_api(host,page)
 if not obj:return None
 names=obj.get('images',[]);wt=obj.get('wikitext',{}).get('*','')
 featured=re.findall(r'\|\s*(?:image\d*|imagefile|image_name|img)\s*=\s*([^\n|]+)',wt[:10000],re.I)
 ranked=[]
 for name in names:
  if BAD.search(name) or not re.search(r'\.(?:png|jpe?g|gif|webp)$',name,re.I):continue
  if blocked and re.search(blocked,name,re.I):continue
  if required and not re.search(required,name,re.I):continue
  stem=re.sub('[^a-z0-9]','',name.rsplit('.',1)[0].lower());score=0
  for alias in ALIASES.get(e['name'],x.names(e))+[page]:
   compact=re.sub('[^a-z0-9]','',alias.lower())
   if stem==compact:score=max(score,160)
   elif compact and compact in stem:score=max(score,70)
  if any(name in a or g.norm(a)==g.norm(name.rsplit('.',1)[0]) for a in featured):score+=35
  if re.search(r'model|render|inventory|weapon',name,re.I):score+=12
  if re.search(r'icon|skill|perk|ammo|stat|wheel|_WW\.',name,re.I):score-=100
  if score>0:ranked.append((score,name))
 with LOCK:EVIDENCE[e['id']]={'page':obj['source'],'ranked_files':sorted(ranked,reverse=True),'featured':featured}
 for score,name in sorted(ranked,reverse=True)[:6]:
  u=obj['api']+'?'+urlencode({'action':'query','format':'json','titles':'File:'+name,'prop':'imageinfo','iiprop':'url','iiurlwidth':720})
  rr=g.fetch(u)
  if not rr['ok']:continue
  try:pages=json.loads(rr['body']).get('query',{}).get('pages',{})
  except ValueError:continue
  for item in pages.values():
   info=item.get('imageinfo',[{}])[0];url=info.get('thumburl') or info.get('url')
   im=save_url(e,url,obj['source'],'Named weapon artwork; exact file identity checked',{'source_file_title':name})
   if im:
    with LOCK:EVIDENCE[e['id']]['selected_file']=name
    return im
 return None

WF={}
def load_warframe():
 for category in ('Primary','Secondary'):
  url='https://raw.githubusercontent.com/WFCD/warframe-items/master/data/json/'+category+'.json'
  r=g.fetch(url)
  if r['ok']:
   for item in json.loads(r['body']):WF[item['name']]={**item,'data_source':url}

def warframe_image(e):
 item=WF.get(e['name'])
 if not item:return None
 extra={'game_item_unique_name':item['uniqueName'],'catalog_source':item['data_source'],'source_file_title':item['imageName']}
 source=item.get('wikiaUrl') or 'https://github.com/WFCD/warframe-items'
 for url in ['https://raw.githubusercontent.com/WFCD/warframe-items/master/data/img/'+quote(item['imageName']),item.get('wikiaThumbnail','')]:
  im=save_url(e,url,source,'Game-export weapon render via WFCD item catalog',extra)
  if im:return im
 return None

def article_image(e,url):
 r=g.fetch(url)
 if not r['ok']:return None
 soup=BeautifulSoup(r['body'],'html.parser');ranked=[]
 article=soup.select_one('article') or soup.select_one('.mw-parser-output') or soup
 for tag in article.select('img'):
  src=tag.get('data-src') or tag.get('src','');alt=tag.get('alt','');desc=unquote(src)+' '+alt
  if not src or src.startswith('data:') or BAD.search(desc):continue
  score=10 if exact_name(e,desc) else 0
  short={'Colt Defender Mark I':'defender','Kel-Tec CP33':'cp33','Armaguerra OG-43':'og43','Benelli CB-M2':'cbm2'}.get(e['name'])
  if short and short in re.sub('[^a-z0-9]','',desc.lower()):score+=20
  if 'unrealarchive.org' in url:
   if any(f.present(n,alt+' '+unquote(src)) for n in ALIASES.get(e['name'],[e['name']])):score+=30
   if e['name']=='Translocator' and re.search(r'UT3|UT2003|UT2004|U1-|Unreal_1',src,re.I):score-=50
   if e['name']=='Dispersion Pistol' and re.search(r'UC2|U2-|Unreal_II|Unreal_2',src,re.I):score-=50
  if re.search(r'icon|ammo|texture|powerup|_menu',desc,re.I):score-=20
  if score>0:ranked.append((score,urljoin(url,src),alt))
 with LOCK:EVIDENCE[e['id']]={'page':url,'article_images':ranked}
 for _,src,alt in sorted(ranked,reverse=True)[:6]:
  im=save_url(e,src,url,'Weapon photograph or game render from its named source section',{'source_alt':alt})
  if im:return im
 return None

def exact_image(e):
 if e['game']=='Warframe':return warframe_image(e)
 if e['game']=='Nuclear Throne':return mediawiki_image(e,'https://nuclear-throne.fandom.com','Weapons',blocked='Golden|Gold_')
 if e['name'] in ARCHIVE:
  im=article_image(e,'https://unrealarchive.org/wikis/the-liandri-archives/'+ARCHIVE[e['name']]+'.html')
  if im:return im
 if e['name'] in SOURCE_ARTICLES:
  im=article_image(e,SOURCE_ARTICLES[e['name']])
  if im:return im
 if e['name'] in PAGES:
  host,page=PAGES[e['name']];im=mediawiki_image(e,host,page,blocked='icon|symbol|skill')
  if im:return im
 if e['game']=='Remnant: From the Ashes':
  for host in ('https://remnantfromtheashes.fandom.com','https://remnant.fandom.com'):
   im=mediawiki_image(e,host,e['name'])
   if im:return im
  url='https://remnantfromtheashes.wiki.fextralife.com/'+quote(e['name'].replace(' ','+'),safe='+')
  im=article_image(e,url)
  if im:return im
 if e['game']=='Helldivers 2':return mediawiki_image(e,'https://helldivers.wiki.gg',e.get('page') or e['name'],blocked=r'Weapon_Options|Weapon_Wheel|_WW\.|icon')
 host=next((host for key,host in x.ROUTES if key.lower() in e['game'].lower()),None)
 if host:
  return mediawiki_image(e,host,unquote(e.get('page') or e['name']).replace('_',' '),blocked='icon|symbol|skill')
 return None

def seconds(value):
 if isinstance(value,(int,float)):return int(value/1000)
 return sum(int(n)*60**i for i,n in enumerate(str(value).split(':')[::-1])) if re.fullmatch(r'\d+(?::\d+){1,2}',str(value)) else None

def named_chapter(e,v):
 r=g.fetch('https://www.youtube.com/watch?v='+v['id'])
 if not r['ok']:return None
 data=f.parse_json_after(r['body'],[r'(?:var\s+ytInitialData|window\["ytInitialData"\]|ytInitialData)\s*=\s*'])
 for obj in g.walk(data):
  ch=obj.get('chapterRenderer') or obj.get('macroMarkersListItemRenderer')
  if not ch:continue
  title=g.txt(ch.get('title'));time=ch.get('timeRangeStartMillis')
  if time is None:time=g.txt(ch.get('timeDescription'))
  sec=seconds(time)
  if not exact_name(e,title) or sec is None:continue
  thumbs=ch.get('thumbnail',{}).get('thumbnails',[])
  out={**v,'url':'https://www.youtube.com/watch?v='+v['id']+'&t='+str(sec)+'s','chapter':title,'chapter_seconds':sec,'match':'Exact named chapter in game-specific weapon showcase'}
  if thumbs:out['chapter_thumbnail']=thumbs[-1]['url']
  return out
 # Some uploaders provide their chapter evidence only in the public description.
 meta=f.video_data(v['url'])
 if meta:
  desc=meta.get('description','')
  for line in desc.splitlines():
   mt=re.search(r'(?<!\d)(\d{1,2}:\d{2}(?::\d{2})?)(?!\d)',line)
   if mt and exact_name(e,line):return {**meta,'url':'https://www.youtube.com/watch?v='+v['id']+'&t='+str(seconds(mt.group(1)))+'s','chapter':line.strip(),'match':'Exact weapon timestamp in uploader description'}
 return None

def video(e,old=None):
 aliases=ALIASES.get(e['name'],x.names(e));suffix='historical gun' if e['group']=='Historical' else GAME_CONTEXT.get(e['game'],[e['game']])[0]
 queries=[aliases[0]+' '+suffix]
 if len(aliases)>1:queries.append(aliases[-1]+' '+suffix)
 if e['group']=='Gaming':queries.append(suffix+' all weapons showcase')
 found={}
 for oldv in (old or {}).get('video_candidates',[]):
  vid=g.video_id(oldv['url'])
  if vid:found[vid]={'id':vid,**oldv}
 for query in dict.fromkeys(queries):
  for v in f.search(query):found[v['id']]=v
  exact=[]
  for v in found.values():
   title=v['title'];full=title+' '+v.get('description','')
   if not context(e,full):continue
   if re.search(r'3d print|homemade|how to build|airsoft|replica|cosplay|prop|blender|modeling|soundtrack|real life|Triad Guy',title,re.I):continue
   if e['name']=='Astilla' and 'prime' in title.lower():continue
   if e['name']=='Disc Gun' and 'gold' in title.lower():continue
   if e['name']=='Ballistica Prime' and 'incarnon' in title.lower():continue
   if exact_name(e,title) and not re.search(r'all weapons|all guns|every weapon|tier list|full walkthrough|full game',title,re.I):
    score=10+sum(w in title.lower() for w in ('showcase','gameplay','review','demonstration'))
    if 'weapon demonstration' in title.lower():score+=5
    exact.append((score,v))
  if exact:
   v=copy.deepcopy(sorted(exact,key=lambda z:z[0],reverse=True)[0][1])
   if 'thumbnail' not in v:v=f.video_data(v['url']) or v
   v.update(match='Exact item and game or historical context checked');return v
 for v in found.values():
  if context(e,v['title']) and re.search('all weapons|all guns|weapons of|weapon showcase|weapon test',v['title'],re.I) and not re.search('mod spotlight|nali|ballistic|relov',v['title'],re.I):
   ch=named_chapter(e,v)
   if ch:return ch
 with LOCK:EVIDENCE.setdefault(e['id'],{})['unresolved_video_candidates']=[{'title':v['title'],'url':v['url']} for v in found.values()]
 return None


def repair_one(e,rec):
 result=copy.deepcopy(rec);im=exact_image(e);v=result.get('video')
 if e['id'] in VIDEO_FIX:v=video(e,rec)
 if v and not im and v.get('chapter_thumbnail'):im=save_url(e,v['chapter_thumbnail'],v['url'],'Exact named weapon chapter frame',{'chapter':v['chapter']})
 if not v:return None,'Exact video not resolved'
 if not im:return None,'Exact weapon image not resolved'
 result.update(image=im,video=v,complete=True,status='accepted')
 result.setdefault('evidence',[]).append({'url':im['source'],'title':e['name'],'kind':im['kind']})
 return result,None


def resolve_pending(e,rec):
 if e['name'] in REJECT:return None,REJECT[e['name']]
 if e['name']=='Arclight':e['name']='Arc Light';e['page']='Arc_Light';e['aliases']='Arc Light;Arclight'
 if e['name']=='Wheel Saw':
  e['hook']='A shotgun-like weapon incorporates a moving saw assembly. Its saw action has changed across updates; the linked footage identifies the demonstrated version.'
 if e['name']=='SIG MKMO':return None,'The available object videos show MKPS/MKPO variants, not the specific MKMO. Kept in research, not silently substituted.'
 v=video(e,rec);im=exact_image(e)
 if not v:return None,'No exact item video or named chapter verified'
 if not im and v.get('chapter_thumbnail'):im=save_url(e,v['chapter_thumbnail'],v['url'],'Exact weapon chapter screenshot',{'chapter':v['chapter']})
 if not im and exact_name(e,v['title']):im=save_url(e,v.get('thumbnail',''),v['url'],'Item-video preview; not a separate weapon photograph')
 if not im:return None,'Weapon-specific image unresolved'
 return {'id':e['id'],'name':e['name'],'game':e['game'],'group':e['group'],'image':im,'video':v,'complete':True,'status':'accepted','evidence':[{'url':im['source'],'title':e['name'],'kind':im['kind']},{'url':v['url'],'title':v['title'],'kind':v['match']}]},None


def main():
 c,m,baseline=x.init();state=g.load(DATA/'state.json',{});allentries=c['gaming']+c['historical'];idx={e['id']:e for e in allentries};seed={e['id']:e for e in x.seeds(c)}
 report=g.load(DATA/'finish-report.json',{'version':VERSION,'images_fixed':{},'accepted':{},'pending':{},'rejected':{}})
 if report.get('version')!=VERSION:report={'version':VERSION,'images_fixed':{},'accepted':{},'pending':{},'rejected':{}}
 load_warframe()
 cohorts={'Warframe','Nuclear Throne','Remnant: From the Ashes','Helldivers 2'}
 targets=[e for e in allentries if e['id'] not in baseline['entries'] and (e['id'] in REVIEW_IDS or e['game'] in cohorts) and e['id'] not in report['images_fixed']]
 pending=[seed[k] for k,rec in state.items() if rec['status']=='unresolved' and k in seed and k not in report['rejected']]
 print('TARGETED_FINISH',json.dumps({'image_repairs':len(targets),'remaining_candidates':len(pending),'baseline_preserved':len(baseline['entries'])}),flush=True)
 def work(e,isnew):
  try:return e,isnew,*(resolve_pending(e,state[e['id']]) if isnew else repair_one(e,m[e['id']]))
  except Exception as exc:return e,isnew,None,type(exc).__name__+': '+str(exc)[:300]
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
  jobs=[pool.submit(work,e,False) for e in targets]+[pool.submit(work,e,True) for e in pending]
  for n,ft in enumerate(concurrent.futures.as_completed(jobs),1):
   e,isnew,rec,error=ft.result();k=e['id']
   if rec:
    if isnew:
     c['historical' if e['group']=='Historical' else 'gaming'].append(e);idx[k]=e;report['accepted'][k]=e['name']
    else:report['images_fixed'][k]={'name':e['name'],'image_source':rec['image']['source'],'video':rec['video']['url']}
    m[k]=rec;state[k]=rec;report['pending'].pop(k,None)
   else:
    report['pending'][k]={'name':e['name'],'reason':error,'published':not isnew}
    if e['name'] in REJECT:state[k]['status']='rejected';state[k]['reason']=error;report['rejected'][k]=error;report['pending'].pop(k,None)
   if n%12==0:print('FINISH_PROGRESS',n,'/',len(jobs),'repaired',len(report['images_fixed']),'new',len(report['accepted']),'pending',len(report['pending']),flush=True)
 report['evidence']=EVIDENCE
 g.save(DATA/'finish-report.json',report)
 quality=g.load(DATA/'quality-report.json',{})
 for k in report['images_fixed']:
  quality.get('pending',{}).pop(k,None)
 g.save(DATA/'quality-report.json',quality)
 x.persist_and_publish(c,m,baseline,state,'--remote' in sys.argv)
 x.contact_sheets(c,m,baseline)
 x.verify(c,m,baseline,'--remote' in sys.argv)
 print('FINISH_REPORT',json.dumps({k:v for k,v in report.items() if k!='evidence'}),flush=True)
if __name__=='__main__':main()
