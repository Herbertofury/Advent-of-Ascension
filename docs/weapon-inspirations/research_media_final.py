#!/usr/bin/env python3
"""Resolve the bounded visual QA delta; preserve every original reference."""
from __future__ import annotations
import collections,concurrent.futures,copy,hashlib,io,json,re,sys,threading
from pathlib import Path
from urllib.parse import quote,urlencode,urljoin,unquote
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw,ImageFont
import research_finish as f2
x=f2.x;g=f2.g;p=f2.p;f=f2.f;ROOT=f2.ROOT;DATA=f2.DATA
LOCK=threading.Lock();EVIDENCE={}
PAGES={
 'xg-54d5ce777642':('https://ratchetandclank.fandom.com','Chimp-o-Matic','chimp'),
 'xg-7d11a7246fa3':('https://ratchetandclank.fandom.com','Lightning Rod (Rift Apart)','lightning.*rod'),
 'xg-6825d0f5526c':('https://wiki.teamfortress.com','Crusader\'s Crossbow','crusader.*crossbow'),
 'xg-c69e6525b7d5':('https://borderlands.fandom.com','Deliverance (shotgun)','deliverance'),
 'xg-81ac034b8329':('https://shodan.fandom.com','Annelid Launcher','annelid|worm.*launcher'),
 'xg-e50c84ee8034':('https://starwars.fandom.com','Geonosian Elite beam weapon','geonosian|beam.*weapon'),
 'xg-9841a10d6256':('https://spacemarine2.fandom.com','Multi-Melta','multi.*melta'),
 'xg-d5a8fd535157':('https://turbo-overkill.fandom.com','Boomer','boomer'),
 'xg-8f9dfe9e3ffb':('https://nuclear-throne.fandom.com','Weapons','super.*disc|disc.*super'),
 'xg-71c9d821c0be':('https://scorn.wiki.gg','Weapons','pistol'),
 'xg-1a1b00cd8c44':('https://scorn.wiki.gg','Weapons','shotgun|rifle|schrotflinte'),
 'xg-6aed3ef12cc9':('https://scorn.wiki.gg','Weapons','grenade|launcher'),
}
DIRECT={
 'xg-7d11a7246fa3':('https://static.wikia.nocookie.net/ratchet/images/0/04/Lightning_Rod_from_RA_screen.png/revision/latest?cb=20210703223806','https://ratchetandclank.fandom.com/wiki/Lightning_Rod_(Rift_Apart)','Named in-game Lightning Rod screenshot'),
 'xg-69deb34344d7':('https://archive.kontek.net/eliteforce.3dactionplanet.gamespy.com/ef1/images/weapons/photon.jpg','https://archive.kontek.net/eliteforce.3dactionplanet.gamespy.com/ef1/weapons.html','Photon Burst render beside its named archived game entry'),
 'xg-ce0d837d9245':('https://landofgames.ru/uploads/posts/2020-08/1598290042_4.jpg','https://landofgames.ru/articles/guides/9512-novoe-oruzhie-v-remnant-from-the-ashes-subject-2923.html','Original-game Fusion Rifle inventory screenshot'),
 'xh-cfb50ce81b80':('https://i.ytimg.com/vi/78js3IZSX8o/maxresdefault.jpg','https://www.youtube.com/watch?v=78js3IZSX8o','Full-resolution preview from named CP33 firsthand review'),
}
WITHDRAW={
 'xh-6be605630472':'The available image/video pair represented a Warzone recreation rather than an authenticated OG-43 historical reference. Retained in the research ledger; removed only from this new expansion until exact media is qualified.',
 'xh-aa70a7dcd45e':'The selected video cover did not show the Benelli CB-M2. Exact historical prototype imagery and substantive direct footage remain unqualified; retained as a research lead, not a completed gallery entry.'
}
BAD=re.compile(r'logo|avatar|flag|stub|question|weapon.?drops|drops.?table|rarity|ammo|controller|banner|blueprint|weapon.?wheel|weapon.?options|_WW\.|skill|achievement',re.I)


def api_images(e,host,page,pattern):
 api='/w/api.php' if host=='https://wiki.teamfortress.com' else '/api.php'
 url=host+api+'?'+urlencode({'action':'parse','format':'json','page':page,'prop':'images|text|wikitext','redirects':1})
 r=g.fetch(url)
 if not r['ok']:return None
 try:obj=json.loads(r['body']).get('parse',{})
 except ValueError:return None
 if not obj:return None
 source=host+'/wiki/'+quote(obj.get('title',page).replace(' ','_'));names=obj.get('images',[])
 soup=BeautifulSoup(obj.get('text',{}).get('*',''),'html.parser');wt=obj.get('wikitext',{}).get('*','')
 candidates=[]
 for name in names:
  if not re.search(pattern,name,re.I) or BAD.search(name):continue
  if not re.search(r'\.(?:png|jpe?g|webp|gif)$',name,re.I):continue
  score=100
  if re.search(r'icon|hud',name,re.I):score-=25
  if re.search(r'render|model|screen',name,re.I):score+=15
  if e['id']=='xg-6825d0f5526c' and 'backpack' in name.lower():score+=35
  if e['id']=='xg-7d11a7246fa3' and 'strike' in name.lower():continue
  if e['id']=='xg-54d5ce777642' and re.search(r'chimpositron|chimp.*enemy',name,re.I):continue
  candidates.append((score,name))
 # File names in weapon tables are sometimes abbreviated. Use the exact named row,
 # not a page-wide image or a general weapon-drop diagram.
 if e['id']=='xg-8f9dfe9e3ffb':
  for row in soup.select('tr'):
   cells=row.find_all(['th','td'],recursive=False)
   if any(g.norm(cell.get_text(' ',strip=True))=='super disc gun' for cell in cells):
    for im in row.select('img'):
     src=im.get('data-src') or im.get('src','');alt=im.get('alt','')
     if src and not BAD.search(src+' '+alt):
      if src.startswith('//'):src='https:'+src
      result=p.image_url(e,urljoin(host,src),source,'Exact Super Disc Gun sprite from its named weapon-table row')
      if result:return result
 with LOCK:EVIDENCE[e['id']]={'source':source,'all_files':names,'candidates':sorted(candidates,reverse=True),'excerpt':soup.get_text(' ',strip=True)[:400]}
 for score,name in sorted(candidates,reverse=True):
  query=host+api+'?'+urlencode({'action':'query','format':'json','titles':'File:'+name,'prop':'imageinfo','iiprop':'url','iiurlwidth':720})
  rr=g.fetch(query)
  if not rr['ok']:continue
  try:pages=json.loads(rr['body']).get('query',{}).get('pages',{})
  except ValueError:continue
  for value in pages.values():
   info=value.get('imageinfo',[{}])[0];u=info.get('thumburl') or info.get('url')
   if u:
    result=p.image_url(e,u,source,'Weapon-specific source artwork; exact file name checked')
    if result:result['source_file_title']=name;return result
 return None


def repair(e,previous):
 rec=copy.deepcopy(previous);path=ROOT/rec['image']['local'];old=path.read_bytes()
 try:
  if e['id']=='xg-71c9d821c0be':
   video=f2.video(e,rec)
   if not video: return None,'Actual Scorn gameplay video unresolved'
   rec['video']=video
  image=None
  if e['id'] in DIRECT:
   u,source,kind=DIRECT[e['id']];image=p.image_url(e,u,source,kind)
  if not image and e['id'] in PAGES:
   image=api_images(e,*PAGES[e['id']])
  if not image and e['game']=='Scorn':
   host,page,pat=PAGES[e['id']];image=api_images(e,'https://scorn.fandom.com',page,pat)
  if not image:
   path.write_bytes(old);return None,'Exact image still needs review'
  rec.update(image=image,complete=True,status='accepted')
  rec.setdefault('evidence',[]).append({'url':image['source'],'title':e['name'],'kind':image['kind']})
  return rec,None
 except Exception as exc:
  path.write_bytes(old);return None,type(exc).__name__+': '+str(exc)[:200]


def main():
 c,m,baseline=x.init();state=g.load(DATA/'state.json',{});idx={e['id']:e for e in c['gaming']+c['historical']};report={'fixed':{},'pending':{},'withdrawn':{}}
 for k,reason in WITHDRAW.items():
  assert k not in baseline['entries']
  if k in idx:
   e=idx[k];report['withdrawn'][k]={'name':e['name'],'reason':reason,'previous_media':m[k]}
   state[k]={**state[k],'status':'unresolved','complete':False,'reason':reason,'missing':['qualified exact-model media']}
   c['historical']=[v for v in c['historical'] if v['id']!=k];m.pop(k,None)
 targets=[idx[k] for k in sorted(set(PAGES)|set(DIRECT)) if k in idx]
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  jobs={pool.submit(repair,e,m[e['id']]):e for e in targets}
  for done,ft in enumerate(concurrent.futures.as_completed(jobs),1):
   e=jobs[ft];rec,error=ft.result()
   if rec:
    m[e['id']]=rec;state[e['id']]=rec;report['fixed'][e['id']]={'name':e['name'],'image':rec['image'],'video':rec['video']['url']}
   else:report['pending'][e['id']]={'name':e['name'],'reason':error}
   print('EXACT_SOURCE',done,'/',len(targets),e['name'],'fixed' if rec else error,flush=True)
 report['evidence']=EVIDENCE;g.save(DATA/'exact-source-report.json',report)
 finish=g.load(DATA/'finish-report.json',{})
 for k in report['fixed']:finish.get('pending',{}).pop(k,None)
 for k in WITHDRAW:finish.get('pending',{}).pop(k,None)
 g.save(DATA/'finish-report.json',finish)
 x.persist_and_publish(c,m,baseline,state,'--remote' in sys.argv)
 qa=DATA/'qa'/'exact-source';qa.mkdir(parents=True,exist_ok=True);font=ImageFont.load_default(size=16);ids=list(report['fixed'])
 if ids:
  out=Image.new('RGB',(1440,270*((len(ids)+3)//4)),(235,235,235));draw=ImageDraw.Draw(out)
  for i,k in enumerate(ids):
   im=Image.open(ROOT/m[k]['image']['local']).convert('RGBA');im.thumbnail((350,215));a=i%4*360;b=i//4*270;out.paste(im,(a,b),im);draw.text((a+3,b+219),idx[k]['name'][:42],font=font,fill='black');draw.text((a+3,b+242),k,font=font,fill='black')
  out.save(qa/'changes.jpg',quality=94)
 x.verify(c,m,baseline,'--remote' in sys.argv)
 print('EXACT_SOURCE_REPORT',json.dumps({k:v for k,v in report.items() if k not in ('evidence','withdrawn')},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
