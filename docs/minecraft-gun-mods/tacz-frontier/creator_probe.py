#!/usr/bin/env python3
"""Public creator metadata and image identity only. Never downloads video streams or mod files."""
from pathlib import Path
import concurrent.futures,hashlib,json,re,sys
from urllib.parse import urlencode,urlparse
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));import research as r
r.CACHE=ROOT/'cache';r.CACHE.mkdir(exist_ok=True)
ANCHORS={
 'harbinger':['BV1WmyDBbEqW','BV1HHn4z1ELE','BV1fR1RBAEGx'],
 'sentinel':['BV1Q3CvYeEEi','BV1qPK2zZEBo','BV1dDj96RE4n','BV1Fk4gzUEjW'],
 'teamfortress':['BV1kChUzKE3n'],
 'extreme-armaments':['BV1RvZXBHEh8'],
 'essence':['BV1A9NUzuEha','BV1Cm1eB7EQg'],
 'antar-unresolved':['BV1ArycBnE83'],
 'perseus-existing':['BV1uVqfBuEQR'],
 'delta-existing':['BV1AQiYBWE2S']
}

def video(bvid):
 url='https://api.bilibili.com/x/web-interface/view?'+urlencode({'bvid':bvid});res=r.get(url);body=res.get('json',{});data=body.get('data') or {}
 if body.get('code')!=0 or data.get('bvid')!=bvid:return {'bvid':bvid,'sourceUrl':url,'status':res.get('status'),'error':body.get('message') or res.get('error'),'code':body.get('code')}
 episodes=[]
 for section in (data.get('ugc_season') or {}).get('sections',[]):
  for e in section.get('episodes',[]):
   arc=e.get('arc') or {};id=e.get('bvid') or arc.get('bvid')
   if id:episodes.append({'bvid':id,'title':e.get('title') or arc.get('title'),'pic':arc.get('pic') or e.get('pic'),'published':arc.get('pubdate'),'authorMid':arc.get('mid')})
 text=data.get('desc','');rich=data.get('desc_v2') or []
 return {'bvid':bvid,'sourceUrl':'https://www.bilibili.com/video/'+bvid+'/','metadataUrl':url,'owner':data['owner'],'title':data['title'],'description':text,'richDescription':rich,'pic':data.get('pic'),'published':data['pubdate'],'duration':data.get('duration'),'episodes':episodes,'videoStatistics':data.get('stat',{}),'metricPolicy':'Video views/likes are not gunpack downloads or favorites','checkedAt':res['checkedAt'],'sourceHash':hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True).encode()).hexdigest()}

def main():
 previous=r.load(ROOT/'creator-probes.json',{});probes=previous.get('videos',{});targets=list(dict.fromkeys(b for bs in ANCHORS.values() for b in bs if b not in probes))
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  for b,rec in zip(targets,pool.map(video,targets)):probes[b]=rec
 # Inspect relevant author collection episode metadata once; never treat each episode as a new pack.
 extra={}
 for family,ids in ANCHORS.items():
  for id in ids:
   rec=probes.get(id,{})
   for e in rec.get('episodes',[]):
    title=e.get('title') or ''
    if family in ('harbinger','sentinel','teamfortress','extreme-armaments','essence','antar-unresolved'):
     if any(t in title.lower() for t in ('harbinger','essence','神秘之物','哨兵','军团','tfg','极限武装','安塔尔')) and e['bvid'] not in probes:extra[e['bvid']]=family
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  for b,rec in zip(extra,pool.map(video,extra)):probes[b]=rec
 source_pages={}
 for url in ['https://www.mcmod.cn/class/21755.html','https://afdian.com/a/LonelyBoy3540']:
  res=r.get(url);text=res.get('text','');soup=BeautifulSoup(text,'html.parser');body=soup.select_one('.class-text') or soup
  source_pages[url]={'status':res.get('status'),'checkedAt':res.get('checkedAt'),'sourceHash':hashlib.sha256(text.encode()).hexdigest(),'title':soup.title.get_text() if soup.title else None,'text':body.get_text(' ',strip=True)[:18000],'links':list(dict.fromkeys(a['href'] for a in body.select('a[href]') if any(h in a['href'] for h in ('bilibili.com','afdian','curseforge.com','modrinth.com','pan.baidu.com'))))}
 mids=sorted(set(x.get('owner',{}).get('mid') for x in probes.values() if x.get('owner')))
 dynamics={}
 for mid in mids:
  url='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?'+urlencode({'host_mid':mid})
  res=r.get(url);body=res.get('json',{});items=(body.get('data') or {}).get('items',[])
  dynamics[str(mid)]={'url':url,'status':res.get('status'),'code':body.get('code'),'message':body.get('message'),'items':items,'cursor':(body.get('data') or {}).get('offset'),'hasMore':(body.get('data') or {}).get('has_more')}
 r.save(ROOT/'creator-probes.json',{'anchors':ANCHORS,'videos':probes,'sourcePages':source_pages,'publicCreatorFeeds':dynamics,'privateFilesAccessed':False,'videoStreamsDownloaded':False})
 review=[]
 for b,x in probes.items():review.append({k:v for k,v in x.items() if k not in ('episodes','richDescription','videoStatistics')}|{'episodes':[{'bvid':e['bvid'],'title':e['title']} for e in x.get('episodes',[])]})
 r.save(ROOT/'creator-review.json',review)
 print(json.dumps({'videos':len(probes),'failed':[b for b,x in probes.items() if x.get('error')],'publicCreatorFeeds':[{'mid':k,'code':v['code'],'items':len(v['items']),'hasMore':v['hasMore']} for k,v in dynamics.items()]},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
