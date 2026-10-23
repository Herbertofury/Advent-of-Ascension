#!/usr/bin/env python3
"""Repair shared compilation covers with named images or exact chapter frames."""
import bisect,collections,concurrent.futures,hashlib,io,json,re,threading
from pathlib import Path
from urllib.parse import parse_qs,quote,urlencode,urlparse
from PIL import Image,ImageStat
LOCK=threading.Lock()
DIAGNOSTICS={}
ROUTES={
 'Borderlands 3':('https://borderlands.fandom.com',{}),
 'Devil May Cry 5':('https://devilmaycry.fandom.com',{}),
 'Ratchet & Clank: Rift Apart':('https://ratchetandclank.fandom.com',{'RYNO 8':'RYNO_8'}),
 'Splatoon':('https://splatoonwiki.org',{}),
 'Sunset Overdrive':('https://sunsetoverdrive.fandom.com',{}),
 'Warframe':('https://wiki.warframe.com',{'Laetum Incarnon':'Laetum','Phenmor Incarnon':'Phenmor'}),
 'Far Cry 6':('https://farcry.fandom.com',{'El Pequeno':'El_Peque\u00f1o'}),
 'Terraria - Calamity Mod':('https://calamitymod.wiki.gg',{}),
 'Red Faction: Guerrilla':('https://redfaction.fandom.com',{}),
 'Bulletstorm':('https://bulletstorm.fandom.com',{}),
 'Earthworm Jim 2':('https://earthwormjim.fandom.com',{}),
}

def second(url):
 raw=parse_qs(urlparse(url).query).get('t',[''])[0]
 if not raw:return None
 return sum(int(n)*{'h':3600,'m':60,'s':1,'':1}[u] for n,u in re.findall(r'(\d+)([hms]?)',raw))

def storyboard(d,e,video):
 g,p,f=d.g,d.p,d.f;vid=g.video_id(video['url']);t=second(video['url'])
 if not vid or t is None:return None
 r=g.fetch('https://www.youtube.com/watch?v='+vid)
 if not r['ok']:return None
 data=f.parse_json_after(r['body'],[r'(?:var\s+)?ytInitialPlayerResponse\s*=\s*'])
 duration=float(data.get('videoDetails',{}).get('lengthSeconds',0) or 0)
 spec=data.get('storyboards',{}).get('playerStoryboardSpecRenderer',{}).get('spec','')
 with LOCK:DIAGNOSTICS.setdefault('youtube',{})[vid]={'keys':list(data),'duration':duration,'storyboard_present':bool(spec),'playability':data.get('playabilityStatus',{}).get('status'),'reason':data.get('playabilityStatus',{}).get('reason')}
 if not spec:return None
 base,*levels=spec.split('|');options=[]
 for level,part in enumerate(levels):
  fields=part.split('#')
  if len(fields)<8:continue
  try:w,h,count,cols,rows,ms=map(int,fields[:6])
  except ValueError:continue
  interval=ms/1000 if ms else duration/count if duration and count else 0
  if not interval or w<100:continue
  frame=min(count-1,int((t+2)/interval));sheet,cell=divmod(frame,cols*rows)
  url=base.replace('$L',str(level)).replace('$N',fields[6]).replace('$M',str(sheet))
  url+=('&' if '?' in url else '?')+'sigh='+fields[7]
  options.append((w,h,cols,rows,cell,url,frame*interval,interval))
 for w,h,cols,rows,cell,url,when,interval in sorted(options,reverse=True):
  r=g.fetch(url,binary=True)
  if not r['ok']:continue
  try:
   im=Image.open(io.BytesIO(r['body']));x=(cell%cols)*w;y=(cell//cols)*h
   if im.width<x+w or im.height<y+h:continue
   crop=im.crop((x,y,x+w,y+h))
   if max(ImageStat.Stat(crop.convert('RGB')).stddev)<7:continue
   return p.save_image(e,crop,url,video['url'],'Weapon chapter gameplay frame',{'frame_time_seconds':when,'chapter_time_seconds':t,'frame_interval_seconds':interval,'crop_pixels':[x,y,w,h],'frame_selection':'Public video storyboard at the matched weapon chapter; exact crop recorded'})
  except Exception:continue
 return None

def bilibili_frame(d,e,v,bvid):
 g,p=d.g,d.p;t=second(v['url'])
 if t is None:return None
 api='https://api.bilibili.com/x/player/videoshot?'+urlencode({'bvid':bvid,'index':1})
 r=g.fetch(api)
 if not r['ok']:return None
 try:body=json.loads(r['body']);data=body.get('data') or {};idx=data.get('index',[]);urls=data.get('image',[])
 except ValueError:return None
 with LOCK:DIAGNOSTICS.setdefault('bilibili',{})[bvid]={'api':api,'code':body.get('code'),'frames':len(idx),'sheets':len(urls),'fields':list(data)}
 if not(idx and urls):return None
 frame=max(0,bisect.bisect_right(idx,t+2)-1)
 w,h=data['img_x_size'],data['img_y_size'];cols,rows=data['img_x_len'],data['img_y_len'];sheet,cell=divmod(frame,cols*rows)
 if sheet>=len(urls):return None
 url=urls[sheet];url='https:'+url if url.startswith('//') else url
 r=g.fetch(url,binary=True)
 if not r['ok']:return None
 try:
  im=Image.open(io.BytesIO(r['body']));x=cell%cols*w;y=cell//cols*h
  if im.width<x+w or im.height<y+h:return None
  crop=im.crop((x,y,x+w,y+h))
  return p.save_image(e,crop,url,'https://www.bilibili.com/video/'+bvid+'/','Weapon chapter gameplay frame from credited video mirror',{'frame_time_seconds':idx[frame],'chapter_time_seconds':t,'crop_pixels':[x,y,w,h],'storyboard_metadata':api,'original_video':v['url']})
 except Exception:return None

def targeted_video(d,e,old):
 g,p,f=d.g,d.p,d.f
 query=e['name']+' '+e['game']+' weapon showcase'
 results=f.search(query);good=[]
 for v in results:
  title=g.norm(v['title']);context=g.norm(v['title']+' '+v.get('description',''))
  if not f.present(e['name'],v['title']):continue
  if re.search(r'all weapons|every weapon|all guns|all attacks|all skills|tier list|full game|full walkthrough|soundtrack',title):continue
  if not g.tokens(e['game']) & set(context.split()):continue
  if g.video_id(v['url'])==g.video_id(old['url']):continue
  score=sum(w in title for w in ('showcase','weapon','gameplay','guide'))
  good.append((score,v))
 for score,v in sorted(good,key=lambda a:a[0],reverse=True)[:3]:
  im=p.image_url(e,v.get('thumbnail',''),v['url'],'Item-focused video preview; title and game checked')
  if im:return im
 with LOCK:DIAGNOSTICS.setdefault('item_search',{})[e['id']]=[{'title':v['title'],'url':v['url']} for v in results[:10]]
 return None

def run(d):
 g,p=d.g,d.p;root=d.ROOT
 c=g.load(root/'catalog.json',{});m=g.load(root/'media.json',{});idx={e['id']:e for e in c['gaming']+c['historical']}
 by_hash=collections.defaultdict(list)
 for e in c['gaming']:by_hash[m[e['id']]['image']['sha256']].append(e['id'])
 duplicates={k for ids in by_hash.values() if len(ids)>1 for k in ids}
 previous=g.load(root/'specificity-report.json',{})
 targets=sorted(duplicates|set(previous.get('pending',[]))|{'g-c7cf78d773de'})
 settled=set(previous.get('repaired',[]));targets=[k for k in targets if k not in settled]
 report={'before_duplicate_entries':len(duplicates),'targets':targets,'repaired':list(settled),'pending':[],'changes':previous.get('changes',[])}
 def work(k):
  e=idx[k];old=m[k];im=None
  if k=='g-c7cf78d773de':
   im=p.image_url(e,'https://www.giantbomb.com/a/uploads/scale_super/0/6861/264951-monkey_gun.jpg','https://wiki-origin.giantbomb.com/wiki/Objects/Monkey_Gun','Named Monkey Gun weapon image; visually verified')
  if e['game']=='Forgive Me Father':im=bilibili_frame(d,e,old['video'],'BV1a5411U7Ez')
  if not im and e['game'] in ROUTES:
   host,aliases=ROUTES[e['game']];page=aliases.get(e['name'],e['name']).replace(' ','_')
   im=d.mediawiki_image(e,{'wiki':host,'page':page})
  if not im:im=storyboard(d,e,old['video'])
  if not im:im=targeted_video(d,e,old['video'])
  if im and im['sha256']==old['image']['sha256']:im=None
  return k,im
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  futures={pool.submit(work,k):k for k in targets}
  for n,ft in enumerate(concurrent.futures.as_completed(futures),1):
   k=futures[ft]
   try:k,im=ft.result()
   except Exception as exc:im=None;DIAGNOSTICS[k]={'error':str(exc)}
   if im:
    report['changes'].append({'id':k,'name':idx[k]['name'],'old_sha256':m[k]['image']['sha256'],'new_sha256':im['sha256'],'kind':im['kind'],'source':im['source']})
    m[k]['image']=im;report['repaired'].append(k)
   else:report['pending'].append(k)
   print('Specific images',n,'/',len(targets),'repaired',len(report['repaired']),'pending',len(report['pending']),flush=True)
 idx['g-e6a2d0837146']['game']='Earthworm Jim 2';m['g-e6a2d0837146']['game']='Earthworm Jim 2'
 report['diagnostics']=DIAGNOSTICS
 g.save(root/'specificity-report.json',report)
 d.TARGETS={};d.write_all(c,m)
 from PIL import ImageDraw,ImageFont
 outdir=root/'qa'/'specificity';outdir.mkdir(parents=True,exist_ok=True)
 font=ImageFont.load_default(size=15)
 changed=[k for k in report['repaired'] if k in idx]
 for page in range(0,len(changed),24):
  batch=changed[page:page+24];out=Image.new('RGB',(1440,240*((len(batch)+3)//4)),(238,238,238));draw=ImageDraw.Draw(out)
  for i,k in enumerate(batch):
   im=Image.open(root/m[k]['image']['local']).convert('RGB');im.thumbnail((350,195));x=(i%4)*360;y=(i//4)*240;out.paste(im,(x,y));draw.text((x+3,y+199),idx[k]['name'][:40],font=font,fill='black');draw.text((x+3,y+219),k,font=font,fill='black')
  out.save(outdir/('changed-%02d.jpg'%(page//24+1)),quality=92)
 print(json.dumps({'repaired':len(report['repaired']),'pending':report['pending'],'diagnostics':DIAGNOSTICS},ensure_ascii=False),flush=True)
 return report
