#!/usr/bin/env python3
"""Recover one exact ability frame from the credited public low-resolution clip."""
import hashlib,json,subprocess,sys,tempfile
from pathlib import Path
from urllib.parse import urlencode
from PIL import Image,ImageDraw,ImageFont
SOURCE='https://www.bilibili.com/video/BV1a5411U7Ez/'
ORIGINAL='https://www.youtube.com/watch?v=L_59BErDMTI&t=343s'
START=338.0
END=356.0
FPS=5

def run(d,entry,selected=None):
 root=d.ROOT/'qa'/'ability-capture';root.mkdir(parents=True,exist_ok=True)
 evidence={'source':SOURCE,'original_video':ORIGINAL,'options':[],'public_asset_identity_source':'https://bimp.hdslb.com/videoshotpvhdboss/571234903_bcc1bb-0001.jpg','login_used':False,'decoder':'PyAV local-file decoding'}
 api='https://api.bilibili.com/x/player/playurl?'+urlencode({'bvid':'BV1a5411U7Ez','cid':571234903,'qn':16,'fnver':0,'fnval':0,'fourk':0})
 r=d.g.fetch(api);evidence['public_playback_status']=r.get('status');payload={}
 if r['ok']:
  try:payload=json.loads(r['body'])
  except ValueError:pass
 evidence['public_playback_code']=payload.get('code');data=payload.get('data') or {};evidence['returned_quality']=data.get('quality');urls=data.get('durl') or []
 if payload.get('code')!=0 or not urls:
  d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public video URL unavailable; no access-control workaround attempted')
 try:import av
 except ImportError:
  subprocess.run([sys.executable,'-m','pip','install','--quiet','av'],check=True)
  import av
 evidence['decoder_version']=av.__version__
 with tempfile.TemporaryDirectory(prefix='aoa-ability-') as temp:
  path=Path(temp)/'public-source.mp4'
  with d.g.session().get(urls[0]['url'],headers={'Referer':SOURCE,'User-Agent':'Mozilla/5.0'},stream=True,timeout=(10,45)) as response:
   evidence['media_http_status']=response.status_code
   if not response.ok:
    d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public media request failed')
   size=0
   with path.open('wb') as out:
    for chunk in response.iter_content(1024*1024):
     if chunk:size+=len(chunk);out.write(chunk)
  evidence['source_bytes']=size;evidence['source_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
  with av.open(str(path)) as video:
   stream=video.streams.video[0];stream.thread_type='AUTO'
   video.seek(int(START/float(stream.time_base)),stream=stream,backward=True)
   next_time=START
   for frame in video.decode(stream):
    when=float(frame.pts*stream.time_base) if frame.pts is not None else None
    if when is None or when+0.0001<next_time:continue
    if when>=END:break
    number=len(evidence['options'])+1;filename='frame-%03d.png'%number
    frame.to_image().save(root/filename)
    evidence['options'].append({'file':filename,'source':SOURCE,'url':SOURCE,'time_seconds':when,'kind':'Public gameplay excerpt frame'})
    next_time+=1/FPS
 d.g.save(root/'evidence.json',evidence)
 assert evidence['options'],'No gameplay frames decoded'
 font=ImageFont.load_default(size=16)
 for start in range(0,len(evidence['options']),32):
  options=evidence['options'][start:start+32];out=Image.new('RGB',(1440,240*((len(options)+3)//4)),(230,230,230));draw=ImageDraw.Draw(out)
  for i,option in enumerate(options):
   im=Image.open(root/option['file']).convert('RGB');im.thumbnail((356,202));x=i%4*360;y=i//4*240;out.paste(im,(x,y));draw.text((x+3,y+206),option['file']+' %.3fs'%option['time_seconds'],font=font,fill='black')
  out.save(root/('contact-%02d.jpg'%(start//32+1)),quality=94)
 if selected is None:raise RuntimeError('Exact gameplay frames captured in qa/ability-capture; visual selection required before publication')
 option=next(x for x in evidence['options'] if x['file']==selected)
 im=d.p.save_image(entry,Image.open(root/selected),option['url'],option['source'],'Visually verified holy-water ability gameplay frame',{'frame_selection':option,'original_video':ORIGINAL})
 assert im
 return im
