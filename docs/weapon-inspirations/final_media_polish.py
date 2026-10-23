#!/usr/bin/env python3
"""Final visual QA corrections, bounded to five already identified records."""
import json,re
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import specificity_final as sf

def run(d):
 g,p,f=d.g,d.p,d.f;root=d.ROOT;c=g.load(root/'catalog.json',{});m=g.load(root/'media.json',{});idx={e['id']:e for e in c['gaming']+c['historical']};report={'changes':[],'pending':[],'candidates':[]}
 qa=root/'qa'/'final-polish';qa.mkdir(parents=True,exist_ok=True)
 k='g-4e491482f415'
 im=sf.wiki_image(d,idx[k],'https://redfaction.fandom.com','EDF_Singularity_Bombs',['Singularity Bomb','Singularity','SingularityBomb'])
 if im:m[k]['image']=im;report['changes'].append(k)
 else:report['pending'].append(k)
 # The source author's Mancubus chapter at 11:35 still shows Revenant launchers.
 # Keep that evidence, and select another demonstrably v22 chapter rather than silently substituting a variant.
 k='1ea23263a704';cr=g.load(root/'chapter-image-report.json',{});choices={}
 for src in cr.get('sources',{}).values():
  for ch in src.get('chapters',[]):
   if 'mancubus' in ch.get('title','').lower() and 'QEZgQIDzFOo' not in ch['thumbnail'] and 'XoD6xOrIOGY' not in ch['thumbnail']:
    match=re.search(r'/vi/([^/]+)/',ch['thumbnail'])
    if match:choices[match.group(1)]=ch
 for vid,ch in choices.items():
  meta=f.video_data('https://www.youtube.com/watch?v='+vid)
  if not meta:continue
  candidate={'video':meta,'chapter':{x:v for x,v in ch.items() if x!='raw'}}
  rr=g.fetch(ch['thumbnail'],binary=True)
  if rr['ok']:
   import io
   try:Image.open(io.BytesIO(rr['body'])).convert('RGB').save(qa/('mancubus-'+vid+'.jpg'),quality=94)
   except Exception:pass
  report['candidates'].append(candidate)
  title=g.norm(meta['title'])
  if 'brutal doom' in title and ('v22' in title or '22' in title.split()):
   im=p.image_url(idx[k],ch['thumbnail'],meta['url'],'Mancubus weapon screenshot from exact v22 chapter')
   if im:
    value=ch.get('time');sec=(value//1000 if isinstance(value,(int,float)) else sum(int(n)*60**i for i,n in enumerate(str(value).split(':')[::-1])))
    meta.update(url=meta['url']+'&t='+str(int(sec))+'s',match='Item chapter matched',chapter=ch['title'],evidence_url=ch['source'])
    im.update(chapter_title=ch['title'],chapter_time_seconds=sec)
    m[k]['image']=im;m[k]['video']=meta;m[k]['source_note']='The previous source labels 11:35 as Mancubus but the chapter image still shows Revenant launchers. Replaced with the independently matched v22 weapon chapter.'
    report['changes'].append(k);break
 if k not in report['changes']:report['pending'].append(k)
 # Three instant-use abilities formerly used a preceding knife frame from a coarse storyboard.
 keys=['6c110f752d77','236d40511d64','d21c72146df8'];vid='L_59BErDMTI';url='https://www.youtube.com/watch?v='+vid;r=g.fetch(url)
 data=f.parse_json_after(r.get('body',''),[r'(?:var\s+ytInitialData|window\["ytInitialData"\]|ytInitialData)\s*=\s*']) if r['ok'] else {}
 for k in keys:
  name=idx[k]['name'];chosen=None
  for obj in g.walk(data):
   ch=obj.get('chapterRenderer') or obj.get('macroMarkersListItemRenderer')
   if not ch:continue
   title=g.txt(ch.get('title'));thumbs=ch.get('thumbnail',{}).get('thumbnails',[])
   if f.present(name,title) and thumbs:chosen=(title,thumbs[-1]['url'],ch.get('timeRangeStartMillis') or g.txt(ch.get('timeDescription')));break
  if chosen:
   title,img,time=chosen;im=p.image_url(idx[k],img,m[k]['video']['url'],'Named ability chapter screenshot')
   if im:im.update(chapter_title=title,chapter_time=time);m[k]['image']=im;report['changes'].append(k)
 for k in ('13bc6873d039','c8cfb49ca2da'):
  if g.video_id(m[k]['video']['url'])=='mF-HD9Us0SU':m[k]['video']['match']='Named multi-item episode; collection reference'
 report['source_image_evidence']=sf.DETAILS
 g.save(root/'final-polish-report.json',report);d.TARGETS={};d.write_all(c,m)
 ids=report['changes'];font=ImageFont.load_default(size=16)
 if ids:
  sheet=Image.new('RGB',(1440,250*((len(ids)+3)//4)),(238,238,238));draw=ImageDraw.Draw(sheet)
  for i,k in enumerate(ids):
   im=Image.open(root/m[k]['image']['local']).convert('RGB');im.thumbnail((350,200));x=i%4*360;y=i//4*250;sheet.paste(im,(x,y));draw.text((x+3,y+202),idx[k]['name'][:40],font=font,fill='black');draw.text((x+3,y+226),k,font=font,fill='black')
  sheet.save(qa/'changes.jpg',quality=94)
 print(json.dumps(report,ensure_ascii=False),flush=True)
 return report
