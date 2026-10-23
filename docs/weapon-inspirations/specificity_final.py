#!/usr/bin/env python3
"""Finish only the remaining known image-identity gaps; retain all prior evidence."""
import collections,concurrent.futures,html,io,json,re,threading
from pathlib import Path
from urllib.parse import quote,urlencode,urljoin,urlparse
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw,ImageFont
import specificity_repair as sr
LOCK=threading.Lock();DETAILS={}
SPECS={
 'g-e6a2d0837146':('https://earthwormjim.fandom.com','Barn_Blaster', ['Barn Blaster','Barnblaster']),
 'c8cfb49ca2da':('https://sunsetoverdrive.fandom.com','Turret_Copter',['Turret Copter','Turretcopter']),
 '13bc6873d039':('https://sunsetoverdrive.fandom.com','Pyro_Geyser',['Pyro Geyser','Pyrogeyser']),
 'defedb1566cc':('https://borderlands.fandom.com','Quadomizer',['Quadomizer','Quadamizer']),
 '08bf86ec43ad':('https://borderlands.fandom.com','Flakker_(Borderlands_3)',['Flakker']),
 '1a72e2da8eeb':('https://borderlands.fandom.com','Conference_Call_(Borderlands_3)',['Conference Call']),
 '1f8a8d2d06cb':('https://ratchetandclank.fandom.com','Glove_of_Doom',['Glove of Doom RA','Glove of Doom from Rift Apart','Apocalypse Glove from Rift Apart']),
 '334058a1e120':('https://doom.fandom.com','Shield_Saw',['Shield Saw','Shieldsaw']),
 '6e346527298c':('https://doom.fandom.com','Rocket_launcher/Doom:_The_Dark_Ages',['Rocket Launcher DTDA','Rocket Launcher Dark Ages']),
 '8c18eb6d8c1e':('https://doom.fandom.com','Combat_Shotgun/Doom:_The_Dark_Ages',['Combat Shotgun DTDA','Combat Shotgun Dark Ages']),
 'c27ad272be79':('https://doom.fandom.com','Shredder',['Shredder']),
}
REVIEW=['15defa907669','5fd02218a0f9','2f6212002946','58bf5af04e5f']

def compact(s):return re.sub('[^a-z0-9]','',s.lower())

def wiki_image(d,e,host,page,aliases):
 g,p=d.g,d.p;api=host+'/api.php?'+urlencode({'action':'parse','format':'json','page':page,'prop':'images|wikitext','redirects':1})
 r=g.fetch(api)
 if not r['ok']:return None
 try:raw=json.loads(r['body']).get('parse',{});names=raw.get('images',[]);wt=raw.get('wikitext',{}).get('*','')
 except Exception:return None
 featured=re.findall(r'\|\s*(?:image|image1|image2|imagefile|image_name)\s*=\s*([^\n|]+)',wt[:7000],re.I)
 DETAILS[e['id']]={'page':host+'/wiki/'+quote(page),'image_names':names,'infobox_images':featured}
 ranked=[]
 for name in names:
  bare=compact(name.rsplit('.',1)[0]);score=0
  if re.search(r'logo|wordmark|avatar|stub|flag|question|arrow|rarity|damage|skill|ammo|icon.?energy|controller',name,re.I):continue
  if any(compact(n)==bare for n in aliases):score+=60
  elif any(compact(n) in bare for n in aliases):score+=25
  if any(name in a or compact(a)==bare for a in featured):score+=50
  if e['id'] in ('08bf86ec43ad','1a72e2da8eeb'):
   if re.search(r'bl3|borderlands.?3|bl.?3',name,re.I):score+=40
   if re.search(r'bl2|borderlands.?2|bl.?2',name,re.I):score-=100
  if e['id']=='1f8a8d2d06cb':
   if re.search(r'rift|\bRA\b|_RA|RA_',name,re.I):score+=100
   else:score-=80
  if score>0 and name.lower().endswith(('.png','.jpg','.jpeg','.gif','.webp')):ranked.append((score,name))
 for score,name in sorted(ranked,reverse=True):
  q=host+'/api.php?'+urlencode({'action':'query','format':'json','titles':'File:'+name,'prop':'imageinfo','iiprop':'url','iiurlwidth':720})
  response=g.fetch(q)
  if not response['ok']:continue
  try:
   for obj in json.loads(response['body'])['query']['pages'].values():
    info=obj.get('imageinfo',[{}])[0];u=info.get('thumburl') or info.get('url')
    if u:
     im=p.image_url(e,u,host+'/wiki/'+quote(page),'Named weapon image from exact source page')
     if im:DETAILS[e['id']]['selected']=name;return im
  except Exception:continue
 return None

def article_image(d,e,url,needle):
 r=d.g.fetch(url)
 if not r['ok']:return None
 soup=BeautifulSoup(r['body'],'html.parser');found=[]
 for tag in soup.select('img'):
  src=tag.get('data-src') or tag.get('src') or '';desc=' '.join([src,tag.get('alt',''),tag.get('title','')])
  if compact(needle) not in compact(desc):continue
  if src.startswith('data:'):
   src=tag.get('data-lazy-src') or tag.get('data-original') or ''
  if src:found.append(urljoin(url,src))
 DETAILS.setdefault(e['id'],{})['article_images']=found
 for src in found:
  im=d.p.image_url(e,src,url,'Weapon screenshot from named article section')
  if im:return im
 return None

def mirror_for(d,v):
 g=d.g;vid=g.video_id(v['url']);query=v['title'];url='https://api.bilibili.com/x/web-interface/search/type?'+urlencode({'search_type':'video','keyword':query,'page':1})
 r=g.fetch(url)
 if not r['ok']:DETAILS['mirror-'+vid]={'status':r.get('status')};return None
 try:body=json.loads(r['body']);results=(body.get('data') or {}).get('result',[])
 except Exception:return None
 info={'search_url':url,'code':body.get('code'),'candidates':[]};DETAILS['mirror-'+vid]=info
 for row in results:
  bvid=row.get('bvid');title=BeautifulSoup(row.get('title',''),'html.parser').get_text(' ',strip=True)
  if not bvid:continue
  entry={'bvid':bvid,'title':title,'description':row.get('description','')};info['candidates'].append(entry)
  if vid in entry['description']:info['matched']=bvid;return bvid
 for row in results:
  bvid=row.get('bvid');title=BeautifulSoup(row.get('title',''),'html.parser').get_text(' ',strip=True)
  if not bvid:continue
  if len(g.tokens(query)&g.tokens(title))<2:continue
  q='https://api.bilibili.com/x/web-interface/view?'+urlencode({'bvid':bvid});rr=g.fetch(q)
  if not rr['ok']:continue
  try:data=json.loads(rr['body']).get('data') or {}
  except Exception:continue
  desc=data.get('desc','');info.setdefault('view_descriptions',[]).append({'bvid':bvid,'title':data.get('title'),'desc':desc})
  if vid in desc:info['matched']=bvid;return bvid
 return None

def candidates_from_moddb(d,url,label):
 r=d.g.fetch(url)
 if not r['ok']:DETAILS[label]={'status':r.get('status')};return
 soup=BeautifulSoup(r['body'],'html.parser');items=[];seen=set()
 out=d.ROOT/'qa'/'specificity-final';out.mkdir(parents=True,exist_ok=True)
 for tag in soup.select('img'):
  src=tag.get('data-src') or tag.get('src','')
  if not src or '/images/' not in src or 'media.moddb.com' not in src:continue
  if re.search('icon|logo|thumbs|avatar',src,re.I):continue
  src=re.sub(r'/cache/images/','/images/',src);src=re.sub(r'/(?:thumb_\d+x\d+|crop_\d+x\d+)/','/',src)
  if src in seen:continue
  seen.add(src);rr=d.g.fetch(src,binary=True)
  if not rr['ok']:continue
  try:
   im=Image.open(io.BytesIO(rr['body']));im.thumbnail((640,400));name=label+'-'+str(len(items))+'.jpg';im.convert('RGB').save(out/name,quality=92);items.append({'url':src,'caption':tag.get('alt',''),'file':name})
  except Exception:continue
 DETAILS[label]={'url':url,'images':items}

def run(d):
 g=d.g;c=g.load(d.ROOT/'catalog.json',{});m=g.load(d.ROOT/'media.json',{});idx={e['id']:e for e in c['gaming']+c['historical']};prior=g.load(d.ROOT/'specificity-report.json',{})
 targets=sorted(set(prior.get('pending',[]))|set(SPECS)|set(REVIEW));report={'repaired':[],'pending':[],'changes':[]}
 # Only separately published public mirrors qualify; no login or access-control bypass.
 mirrors={}
 videos={g.video_id(m[k]['video']['url']):m[k]['video'] for k in targets if 'Brutal' in idx[k]['game']}
 for vid,v in videos.items():mirrors[vid]=mirror_for(d,v)
 def work(k):
  e=idx[k];im=None
  if k in SPECS:im=wiki_image(d,e,*SPECS[k])
  if k=='defedb1566cc' and not im:im=article_image(d,e,'https://www.gamespot.com/gallery/borderlands-3s-best-legendary-rare-very-rare-guns/2900-3034/','3580239')
  if not im and e['game']=='DOOM: The Dark Ages':im=article_image(d,e,'https://beebom.com/doom-the-dark-ages-weapons/',e['name'].split(' - ')[0])
  if not im and 'Brutal' in e['game']:
   bv=mirrors.get(g.video_id(m[k]['video']['url']))
   if bv:im=sr.bilibili_frame(d,e,m[k]['video'],bv)
  return k,im
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  futures={pool.submit(work,k):k for k in targets}
  for ft in concurrent.futures.as_completed(futures):
   k=futures[ft]
   try:k,im=ft.result()
   except Exception as exc:im=None;DETAILS[k]={'error':str(exc)}
   if im:
    m[k]['image']=im;report['repaired'].append(k);report['changes'].append({'id':k,'name':idx[k]['name'],'source':im['source'],'kind':im['kind']})
   else:report['pending'].append(k)
 if any('CyberDoom' in idx[k]['game'] for k in report['pending']):candidates_from_moddb(d,'https://www.moddb.com/mods/brutal-cyberdoom','cyberdoom')
 report['evidence']=DETAILS;g.save(d.ROOT/'specificity-final-report.json',report)
 prior['repaired']=sorted(set(prior['repaired'])|set(report['repaired']));prior['pending']=report['pending'];g.save(d.ROOT/'specificity-report.json',prior)
 d.TARGETS={};d.write_all(c,m)
 out=d.ROOT/'qa'/'specificity-final';out.mkdir(parents=True,exist_ok=True);font=ImageFont.load_default(size=16)
 ids=report['repaired'];sheet=Image.new('RGB',(1440,250*((len(ids)+3)//4)),(238,238,238));draw=ImageDraw.Draw(sheet)
 for i,k in enumerate(ids):
  im=Image.open(d.ROOT/m[k]['image']['local']).convert('RGB');im.thumbnail((350,200));x=i%4*360;y=i//4*250;sheet.paste(im,(x,y));draw.text((x+3,y+201),idx[k]['name'][:40],font=font,fill='black');draw.text((x+3,y+226),k,font=font,fill='black')
 if ids:sheet.save(out/'changes.jpg',quality=92)
 print(json.dumps(report,ensure_ascii=False),flush=True)
 return report
