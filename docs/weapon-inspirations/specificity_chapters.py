#!/usr/bin/env python3
"""Use public chapter metadata, not player streams, for exact mod screenshots."""
import collections,concurrent.futures,json,re
from urllib.parse import urlencode
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

def run(d):
 g,p,f=d.g,d.p,d.f;root=d.ROOT;c=g.load(root/'catalog.json',{});m=g.load(root/'media.json',{});idx={e['id']:e for e in c['gaming']+c['historical']};previous=g.load(root/'specificity-report.json',{});targets=previous.get('pending',[]);report={'repaired':[],'pending':[],'sources':{},'changes':[]}
 def parse(url):
  r=g.fetch(url)
  if not r['ok']:return {'url':url,'status':r.get('status'),'chapters':[]}
  data=f.parse_json_after(r['body'],[r'(?:var\s+ytInitialData|window\["ytInitialData"\]|ytInitialData)\s*=\s*'])
  chapters=[];renderer_counts=collections.Counter()
  for obj in g.walk(data):
   for key,value in obj.items():
    if isinstance(value,dict) and any(s in key.lower() for s in ('chapter','marker')):
     renderer_counts[key]+=1
     thumbs=value.get('thumbnail',{}).get('thumbnails',[])
     if thumbs:
      title=g.txt(value.get('title')) or g.txt(value.get('titleText'))
      time=g.txt(value.get('timeDescription')) or value.get('timeRangeStartMillis') or value.get('startTimeSeconds')
      chapters.append({'renderer':key,'title':title,'time':time,'thumbnail':thumbs[-1]['url'],'source':url,'raw':value})
  return {'url':url,'status':r.get('status'),'keys':list(data),'renderers':dict(renderer_counts),'chapters':chapters}
 vids={g.video_id(m[k]['video']['url']):m[k]['video'] for k in targets}
 sources=[]
 for vid,v in vids.items():
  sources.extend(['https://www.youtube.com/watch?v='+vid,'https://www.youtube.com/results?'+urlencode({'search_query':v['title']+' Martinoz'})])
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for r in pool.map(parse,sources):report['sources'][r['url']]=r
 def match(e,chapter):
  names=[e['name'],e['name'].removeprefix('The ')]
  return any(f.present(name,chapter['title']) for name in names)
 for k in targets:
  e=idx[k];vid=g.video_id(m[k]['video']['url']);found=[]
  for source in report['sources'].values():
   for chapter in source['chapters']:
    if vid in chapter['thumbnail'] and match(e,chapter):found.append(chapter)
  if not found:
   r=parse('https://www.youtube.com/results?'+urlencode({'search_query':e['name']+' '+e['game'].replace('DOOM II - ','')+' Martinoz'}));report['sources'][r['url']]=r
   found=[x for x in r['chapters'] if vid in x['thumbnail'] and match(e,x)]
  im=None
  for ch in found:
   im=p.image_url(e,ch['thumbnail'],m[k]['video']['url'],'Exact named video chapter thumbnail')
   if im:
    im.update(chapter_title=ch['title'],chapter_time=ch['time'],chapter_metadata_source=ch['source']);break
  if im:
   m[k]['image']=im;report['repaired'].append(k);report['changes'].append({'id':k,'name':e['name'],'image':im})
  else:report['pending'].append(k)
  print('Chapter identity:',e['name'],'resolved' if im else 'pending',flush=True)
 g.save(root/'chapter-image-report.json',report)
 previous['repaired']=sorted(set(previous.get('repaired',[]))|set(report['repaired']));previous['pending']=report['pending'];g.save(root/'specificity-report.json',previous)
 d.TARGETS={};d.write_all(c,m)
 out=root/'qa'/'chapter-images';out.mkdir(parents=True,exist_ok=True);font=ImageFont.load_default(size=16)
 if report['repaired']:
  ids=report['repaired'];sheet=Image.new('RGB',(1440,250*((len(ids)+3)//4)),(238,238,238));draw=ImageDraw.Draw(sheet)
  for i,k in enumerate(ids):
   im=Image.open(root/m[k]['image']['local']).convert('RGB');im.thumbnail((350,200));x=i%4*360;y=i//4*250;sheet.paste(im,(x,y));draw.text((x+3,y+202),idx[k]['name'][:40],font=font,fill='black');draw.text((x+3,y+226),k,font=font,fill='black')
  sheet.save(out/'changes.jpg',quality=92)
 print(json.dumps({'repaired':report['repaired'],'pending':report['pending'],'sources':[{k:v for k,v in r.items() if k!='chapters'} for r in report['sources'].values()]}),flush=True)
 return report
