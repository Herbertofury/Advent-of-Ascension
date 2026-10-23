#!/usr/bin/env python3
"""Capture a short public gameplay excerpt for one unresolved image identity."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys
from urllib.parse import urlencode
from PIL import Image,ImageDraw,ImageFont

BVID='BV1a5411U7Ez'
SOURCE='https://www.bilibili.com/video/'+BVID+'/'
ORIGINAL='https://www.youtube.com/watch?v=L_59BErDMTI&t=343s'
START=344
FPS=4

def capture(d):
 root=d.ROOT/'qa'/'ability-frames';root.mkdir(parents=True,exist_ok=True)
 evidence={'source':SOURCE,'original_video':ORIGINAL,'start_seconds':START,'sample_fps':FPS,'requested_quality':16,'login_used':False}
 session=d.g.session()
 headers={'Referer':SOURCE}
 view_url='https://api.bilibili.com/x/web-interface/view?'+urlencode({'bvid':BVID})
 response=session.get(view_url,headers=headers,timeout=(10,30));evidence['metadata_http_status']=response.status_code
 if not response.ok:
  d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public source metadata was not available; no authentication bypass attempted')
 meta=response.json();evidence['metadata_code']=meta.get('code')
 if meta.get('code')!=0:
  d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public source metadata returned an error')
 data=meta['data'];evidence.update(cid=data['cid'],title=data['title'],description=data.get('desc',''),duration=data.get('duration'))
 api='https://api.bilibili.com/x/player/playurl?'+urlencode({'bvid':BVID,'cid':data['cid'],'qn':16,'fnver':0,'fnval':0,'fourk':0})
 response=session.get(api,headers=headers,timeout=(10,30));evidence['playback_http_status']=response.status_code
 if not response.ok:
  d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public low-resolution playback unavailable; existing images preserved')
 payload=response.json();evidence['playback_code']=payload.get('code')
 streamdata=payload.get('data') or {};evidence['returned_quality']=streamdata.get('quality');evidence['format']=streamdata.get('format')
 urls=streamdata.get('durl') or []
 if payload.get('code')!=0 or not urls:
  evidence['message']=payload.get('message');d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public low-resolution source did not return a playable URL')
 stream=urls[0]['url']
 exe=shutil.which('ffmpeg')
 if not exe:
  subprocess.run([sys.executable,'-m','pip','install','--quiet','imageio-ffmpeg'],check=True)
  import imageio_ffmpeg
  exe=imageio_ffmpeg.get_ffmpeg_exe()
 command=[exe,'-nostdin','-hide_banner','-loglevel','error','-y','-ss',str(START),'-headers','Referer: '+SOURCE+'\r\nUser-Agent: Mozilla/5.0\r\n','-i',stream,'-t','10','-vf','fps='+str(FPS),'-frames:v','40','-an',str(root/'frame-%03d.png')]
 result=subprocess.run(command,capture_output=True,text=True,timeout=180)
 evidence['capture_returncode']=result.returncode
 if result.returncode:
  evidence['capture_error']=result.stderr.replace(stream,'<temporary public media URL>')[-2000:]
  d.g.save(root/'evidence.json',evidence);raise RuntimeError('Public excerpt capture failed; diagnostic preserved')
 frames=sorted(root.glob('frame-*.png'));assert frames,'No public gameplay frames decoded'
 evidence['frames']=[{'file':p.name,'approximate_seconds':START+(i/FPS),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for i,p in enumerate(frames)]
 d.g.save(root/'evidence.json',evidence)
 out=Image.new('RGB',(1440,240*((len(frames)+3)//4)),(240,240,240));draw=ImageDraw.Draw(out);font=ImageFont.load_default(size=18)
 for i,path in enumerate(frames):
  im=Image.open(path).convert('RGB');im.thumbnail((356,202));x=i%4*360;y=i//4*240;out.paste(im,(x,y));draw.text((x+4,y+207),path.stem+'  %.2fs'%(START+i/FPS),font=font,fill='black')
 out.save(root/'contact.jpg',quality=94)
 return root,evidence

def select_or_probe(d,entry,frame=None):
 root,evidence=capture(d)
 if frame is None:
  acceptance=d.g.load(d.ROOT/'final-acceptance.json',{});acceptance['image_identity_review_pending']=[entry['id']];d.g.save(d.ROOT/'final-acceptance.json',acceptance)
  raise RuntimeError('Final ability frame selection awaits visual review of qa/ability-frames/contact.jpg; all existing gallery assets preserved')
 path=root/('frame-%03d.png'%frame);assert path.exists()
 record=evidence['frames'][frame-1]
 image=d.p.save_image(entry,Image.open(path),SOURCE,ORIGINAL,'Visually reviewed holy-water ability gameplay frame',{'frame_time_seconds':record['approximate_seconds'],'video_mirror_source':SOURCE,'original_video':ORIGINAL,'frame_sha256':record['sha256'],'excerpt_start_seconds':START,'frame_sampling_fps':FPS})
 assert image
 d.g.save(root/'selection.json',{'id':entry['id'],'frame':frame,'evidence':record,'image_sha256':image['sha256']})
 return image
