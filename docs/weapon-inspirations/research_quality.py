#!/usr/bin/env python3
"""Image-identity and exact-variant overlay for the incremental research publisher."""
from __future__ import annotations
import collections,concurrent.futures,hashlib,html,io,json,re,sys
from pathlib import Path
from urllib.parse import quote,urlencode,urljoin,urlparse
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw,ImageFont
import expand_research as x

ROOT=x.ROOT;DATA=x.DATA;g=x.g;p=x.p;f=x.f
ORIGINAL_RENDER=x.render
PAGE_OVERRIDES={
 'Roth-Steyr M1907':'Roth–Steyr M1907','Hino-Komuro M1908':'Hino–Komuro pistol','Armaguerra OG-43':'Armaguerra OG-43','Nambu Type 14':'Type 14 Nambu pistol','M3 Grease Gun':'M3 submachine gun','TKB-0146':'TKB-0146','Benelli CB-M2':'Benelli CB M2','Voere VEC-91':'Voere VEC-91','QLZ-87':'QLZ-87','XM307 ACSW':'XM307 Advanced Crew Served Weapon','Kel-Tec CP33':'Kel-Tec CP33','Dreyse needle gun':'Dreyse needle gun','Winchester Defender prototype':'Colt Defender Mark I'}
CORRECTIONS={
 'MP 40-II':{'name':'MP 40/I dual-magazine prototype','page':'MP 40','aliases':'MP40 I;MP 40 I;dual magazine MP40;double magazine MP40','source':'https://www.forgottenweapons.com/mp-40i-the-dual-magazine-experimental-mp-40/'},
 'Winchester Defender prototype':{'name':'Colt Defender Mark I','page':'Colt Defender Mark I','aliases':'Colt Defender Mark I;Colt Defender shotgun;Hillberg Defender;8 barrel shotgun;8 barreled shotgun'},
 'Roth-Steyr M1907':{'aliases':'Roth Steyr 1907;Roth Steyr M1907','source':'https://www.forgottenweapons.com/roth-steyr-1907-pistol-video/'},
 'Armaguerra OG-43':{'aliases':'OG43;OG 43;Armaguerra OG43;Armaguerra OG 43'},
 'M3 Grease Gun':{'aliases':'M3 Grease Gun;M3A1 Grease Gun;M3 submachine gun','exclude_video':'PAM|Argentina|copy|clone'},
 'Hill H15':{'name':'Hill H15 and H1952 prototypes','aliases':'Hill H15;Hill H1952;Hill submachine gun','hook':'The Hill experimental family uses a horizontal top-mounted magazine. The pictured long-stock prototype is the H1952; the later H15 is a compact related design.'},
 'Hino-Komuro M1908':{'aliases':'Hino Komuro 1908;Hino Komuro pistol','exclude_video':'1904'},
 'Solothurn S-18/1000':{'aliases':'Solothurn S18;Solothurn S 18;Solothurn 20mm;Solothurn anti tank','exclude_video':'carriage'},
 'Dreyse needle gun':{'aliases':'Dreyse needle gun;Dreyse rifle','exclude_video':'book|review of'},
 'Crusader\'s Crossbow':{'exclude_video':'prop|3d print|cosplay|real life'},
 'Spider Mine Layer':{'exclude_video':'blender|modeling|3d model|animation test'},
 'Phoenix Samurai':{'aliases':'Samurai;Phoenix Samurai;Samurai laser'},
 'Eightball Gun':{'aliases':'Eightball;Eightball Launcher;Eight Ball;8ball'},
 'Singularity Cannon':{'aliases':'Singularity Cannon;Singularity','search':'Unreal 2 Singularity Cannon weapon gameplay'},
 'SIG MKMO':{'aliases':'MKMO;SIG MKMS;SIG MKPS;SIG MKMO','search':'SIG MKMO submachine gun history'},
 'Parker-Hale PDW':{'aliases':'Bushman IDW;Parker Hale PDW;Parker Hale IDW','search':'Bushman IDW individual defence weapon'},
}
REVIEW_NAMES={'Roth-Steyr M1907','Hino-Komuro M1908','Winchester Defender prototype','Nambu Type 14','Armaguerra OG-43','MP 40-II','M3 Grease Gun','TKB-0146','Benelli CB-M2','Voere VEC-91','QLZ-87','XM307 ACSW','Kel-Tec CP33','GM6 Lynx','Dreyse needle gun','Solothurn S-18/1000','Hill H15','Dispersion Pistol','Translocator','Spider Mine Layer','Crusader\'s Crossbow','Cryo Cannon','Corrosive Sludge Pump','Shard Diffractor','Hurricane Guided Rocket System','Thunderhead Heavy Autocannon'}
STRICT_VIDEO={'Roth-Steyr M1907','Hino-Komuro M1908','Winchester Defender prototype','Armaguerra OG-43','MP 40-II','M3 Grease Gun','Dreyse needle gun','Solothurn S-18/1000','Spider Mine Layer','Crusader\'s Crossbow'}
ADDITIONAL_ROUTES=[('DEATHLOOP','https://deathloop.fandom.com'),('System Shock','https://shodan.fandom.com'),('Marathon','https://marathongame.fandom.com'),('Rise of the Triad','https://riseofthetriad.fandom.com'),('Star Wars','https://starwars.fandom.com'),('Elite Force','https://memory-beta.fandom.com'),('Quake','https://quake.fandom.com'),('F.E.A.R.','https://fear.fandom.com'),('TimeShift','https://timeshift.fandom.com'),('Singularity','https://singularity.fandom.com'),('Painkiller','https://painkiller.fandom.com'),('Scorn','https://scorn.fandom.com'),('Atomic Heart','https://atomicheart.fandom.com'),('Turbo Overkill','https://turbo-overkill.fandom.com')]
x.ROUTES=ADDITIONAL_ROUTES+[r for r in x.ROUTES if r[0]!='Turbo Overkill']
x.GAME_ALIASES.update({'DEATHLOOP':['Deathloop'],'System Shock 2':['System Shock','SS2'],'Rise of the Triad':['Rise of the Triad','ROTT'],'Star Wars: Dark Forces':['Dark Forces'],'Star Wars: Jedi Knight':['Jedi Knight'],'Star Wars: Republic Commando':['Republic Commando'],'Star Trek: Voyager - Elite Force':['Elite Force'],'Quake 4':['Quake 4','Q4'],'F.E.A.R.':['F.E.A.R.','FEAR'],'Warhammer 40,000: Boltgun':['Boltgun'],'Warhammer 40,000: Space Marine 2':['Space Marine 2'],'Helldivers 2':['Helldivers'],'Remnant II':['Remnant 2','Remnant II']})


def exact_video(e):
 cfg=CORRECTIONS.get(e.get('original_name',e['name']),{})
 queries=[cfg.get('search') or e['name']+' '+('historical firearm' if e['group']=='Historical' else e['game'])]
 queries += [a+' '+('historical firearm' if e['group']=='Historical' else e['game']) for a in x.names(e)[1:3]]
 seen={}
 for q in dict.fromkeys(queries):
  for v in f.search(q):seen[v['id']]=v
  good=[]
  for v in seen.values():
   title=v['title'];context=title+' '+v.get('description','')
   if not x.match(e,title) or not x.game_match(e,context):continue
   if re.search(r'all weapons|all guns|full game|full walkthrough|3d print|homemade|how to build|airsoft|replica|cosplay|soundtrack|blender|modeling|3d model',title,re.I):continue
   if cfg.get('exclude_video') and re.search(cfg['exclude_video'],title,re.I):continue
   score=sum(w in title.lower() for w in ('showcase','gameplay','shooting','demonstration','review','forgotten'))
   good.append((score,v))
  if good:
   v=sorted(good,key=lambda a:a[0],reverse=True)[0][1];v['match']='Exact item and variant title/context checked';return v
 return None


def embedded_video(url):
 r=g.fetch(url)
 if not r['ok']:return None
 soup=BeautifulSoup(r['body'],'html.parser');ids=[]
 for tag in soup.select('iframe'):
  src=tag.get('src') or tag.get('data-src') or '';vid=g.video_id(src)
  if vid:ids.append(vid)
 for vid in re.findall(r'youtube(?:-nocookie)?\.com/embed/([A-Za-z0-9_-]{11})',r['body']):ids.append(vid)
 for vid in dict.fromkeys(ids):
  v=f.video_data('https://www.youtube.com/watch?v='+vid)
  if v:v.update(match='Exact weapon video embedded in reviewed source',evidence_url=url);return v
 return None


def page_image(e):
 if e['group']=='Historical':
  page=PAGE_OVERRIDES.get(e.get('original_name',e['name']),e.get('page') or e['name']);host='https://en.wikipedia.org';api='/w/api.php'
  if e.get('original_name',e['name']) in {'MP 40-II','GM6 Lynx','Hill H15','Solothurn S-18/1000'}:return None
  q=host+api+'?'+urlencode({'action':'query','format':'json','redirects':1,'titles':page,'prop':'pageimages|info','inprop':'url','piprop':'thumbnail|name','pithumbsize':720,'pilicense':'any'})
  r=g.fetch(q)
  if r['ok']:
   try:
    for obj in json.loads(r['body']).get('query',{}).get('pages',{}).values():
     if obj.get('thumbnail') and not re.search(r'diagram|patent|cartridge|silhouette|cutaway|schematic',obj.get('pageimage',''),re.I):
      im=p.image_url(e,obj['thumbnail']['source'],obj.get('fullurl',host+'/wiki/'+quote(page)),'Exact article lead photograph or weapon render')
      if im:im['source_file_title']=obj.get('pageimage');return im
   except (ValueError,TypeError):pass
  return None
 host=next((host for key,host in x.ROUTES if key.lower() in e['game'].lower()),None)
 if not host:return None
 page=__import__('urllib.parse',fromlist=['unquote']).unquote(e.get('page') or e['name']).replace('_',' ')
 api='/w/api.php' if host=='https://wiki.warframe.com' else '/api.php'
 q=host+api+'?'+urlencode({'action':'parse','format':'json','page':page,'prop':'text|images','redirects':1});r=g.fetch(q)
 if not r['ok']:return None
 try:obj=json.loads(r['body']).get('parse',{})
 except ValueError:return None
 soup=BeautifulSoup(obj.get('text',{}).get('*',''),'html.parser');source=host+('/w/' if host=='https://wiki.warframe.com' else '/wiki/')+quote(obj.get('title',page).replace(' ','_'))
 areas=soup.select('.portable-infobox .pi-image, .infobox, .infoboxtable, .weaponbox, .mw-parser-output > figure')
 choices=[]
 for area in areas[:2]:
  for im in area.select('img'):
   u=im.get('data-src') or im.get('src','');alt=im.get('alt','');w=im.get('width','0')
   if not u or u.startswith('data:') or x.BAD_IMAGE.search(u+' '+alt):continue
   if str(w).isdigit() and int(w)<100:continue
   if re.search(r'icon|schematic|symbol',u,re.I):continue
   choices.append((u,alt))
 for u,alt in choices:
  if u.startswith('//'):u='https:'+u
  elif u.startswith('/'):u=host+u
  im=p.image_url(e,u,source,'Weapon image from the named article infobox')
  if im:im['source_alt']=alt;return im
 return None


def apply_quality(c,m,baseline,state):
 idx={e['id']:e for e in c['gaming']+c['historical']};report=g.load(DATA/'quality-report.json',{'fixed':{},'pending':{}})
 targets=[e for e in idx.values() if e['id'] not in baseline['entries'] and e['name'] in REVIEW_NAMES and e['id'] not in report['fixed']]
 def work(entry):
  oldname=entry['name'];e=dict(entry);e['original_name']=oldname;cfg=CORRECTIONS.get(oldname,{})
  for k,v in cfg.items():
   if k not in ('source','exclude_video','search'):e[k]=v
  rec=dict(m[e['id']]);im=None;video=rec.get('video')
  if oldname in STRICT_VIDEO:
   video=embedded_video(cfg['source']) if cfg.get('source') else exact_video(e)
  if not video:return entry,None,'Exact item video unresolved'
  im=page_image(e)
  if not im:im=p.image_url(e,video.get('thumbnail',''),video['url'],'Item-specific video preview; exact identity reviewed')
  if not im:return entry,None,'Exact image unresolved'
  rec.update(image=im,video=video,name=e['name'],complete=True,status='accepted')
  rec.setdefault('evidence',[]).append({'url':video.get('evidence_url',video['url']),'title':video['title'],'kind':'Exact variant correction'})
  if oldname!=e['name']:rec['source_note']='Catalog naming corrected from '+oldname+' to '+e['name']+'; original record identity retained.'
  e.pop('original_name',None);return e,rec,None
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  jobs={pool.submit(work,e):e for e in targets}
  for ft in concurrent.futures.as_completed(jobs):
   original=jobs[ft]
   try:e,rec,error=ft.result()
   except Exception as exc:e=original;rec=None;error=str(exc)
   if rec:
    idx[e['id']].update(e);m[e['id']]=rec;state[e['id']]=rec;report['fixed'][e['id']]={'name':e['name'],'image':rec['image']['source'],'video':rec['video']['url']};report['pending'].pop(e['id'],None)
   else:report['pending'][e['id']]={'name':e['name'],'reason':error}
 g.save(DATA/'quality-report.json',report)
 return report


def patched_render(c,m,baseline,state):
 coverage=ORIGINAL_RENDER(c,m,baseline,state)
 path=x.DOCS/(g.PAGES[1]+'.md');body=path.read_text();count=len({e['game'] for e in c['historical']});body=re.sub(r'(\*\*\d+ references \| )\d+( collections)',lambda z:z[1]+str(count)+z[2],body,count=1);path.write_text(body,encoding='utf-8')
 return coverage
x.render=patched_render


def main():
 c,m,baseline=x.init();state=g.load(DATA/'state.json',{})
 report=apply_quality(c,m,baseline,state)
 x.persist_and_publish(c,m,baseline,state,'--remote' in sys.argv)
 x.contact_sheets(c,m,baseline)
 print('QUALITY_CORRECTIONS',json.dumps(report),flush=True)
 # New candidates use improved exact-item image selection before thumbnail fallback.
 old_resolve=x.resolve
 def resolve(e):
  rec=old_resolve(e)
  if rec.get('complete'):
   im=page_image(e)
   if im:rec['image']=im
  return rec
 x.resolve=resolve
 x.main()
if __name__=='__main__':main()
