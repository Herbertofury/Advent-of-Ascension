#!/usr/bin/env python3
"""Bounded final visual recovery using the public asset identity already recorded."""
import io,json,re,shutil,subprocess,sys
from pathlib import Path
from urllib.parse import urlencode
from PIL import Image,ImageDraw,ImageFont
SOURCE='https://www.bilibili.com/video/BV1a5411U7Ez/'
ORIGINAL='https://www.youtube.com/watch?v=L_59BErDMTI&t=343s'
START=338
FPS=5

def run(d,entry,selected=None):
 root=d.ROOT/'qa'/'ability-capture';root.mkdir(parents=True,exist_ok=True)
 evidence={'source':SOURCE,'original_video':ORIGINAL,'options':[],'public_asset_identity_source':'https://bimp.hdslb.com/videoshotpvhdboss/571234903_bcc1bb-0001.jpg','login_used':False}
 # This CID candidate is the prefix of the already verified source video storyboard.
 # The playback API must accept the BVID/CID pair before any media request is made.
 api='https://api.bilibili.com/x/player/playurl?'+urlencode({'bvid':'BV1a5411U7Ez','cid':571234903,'qn':16,'fnver':0,'fnval':0,'fourk':0})
 r=d.g.fetch(api);evidence['public_playback_status']=r.get('status');payload={}
 if r['ok']:
  try:payload=json.loads(r['body'])
  except ValueError:pass
 evidence['public_playback_code']=payload.get('code');data=payload.get('data') or {};evidence['returned_quality']=data.get('quality')
 urls=data.get('durl') or []
 if payload.get('code')==0 and urls:
  stream=urls[0]['url'];exe=shutil.which('ffmpeg')
  if not exe:
   subprocess.run([sys.executable,'-m','pip','install','--quiet','imageio-ffmpeg'],check=True)
   import imageio_ffmpeg
   exe=imageio_ffmpeg.get_ffmpeg_exe()
  command=[exe,'-nostdin','-hide_banner','-loglevel','error','-y','-ss',str(START),'-headers','Referer: '+SOURCE+'\r\nUser-Agent: Mozilla/5.0\r\n','-i',stream,'-t','18','-vf','fps='+str(FPS),'-frames:v','90','-an',str(root/'frame-%03d.png')]
  try:
   result=subprocess.run(command,capture_output=True,text=True,timeout=150)
   evidence['capture_returncode']=result.returncode
   if result.returncode:evidence['capture_error']=result.stderr.replace(stream,'<temporary public source URL>')[-1200:]
  except subprocess.TimeoutExpired:evidence['capture_error']='Finite excerpt capture timeout'
 for path in sorted(root.glob('frame-*.png')):
  number=int(path.stem.split('-')[1]);evidence['options'].append({'file':path.name,'source':SOURCE,'url':SOURCE,'time_seconds':START+(number-1)/FPS,'kind':'Public gameplay excerpt frame'})
 # Two independently published source images are fallbacks, not generic placeholders.
 for index,url in enumerate(['https://www.lawod.com/wp-content/uploads/2022/06/Forgive-Me-Father-Abilities-ss-1-1024x576.jpg','https://bimp.hdslb.com/videoshotpvhdboss/571234903_bcc1bb-0001.jpg']):
  response=d.g.fetch(url,binary=True)
  if not response['ok']:continue
  try:
   image=Image.open(io.BytesIO(response['body']))
   if index==0:
    image.save(root/'article.png');evidence['options'].append({'file':'article.png','source':'https://www.lawod.com/forgive-me-father-abilities-guide/','url':url,'kind':'Published ability reference screenshot'})
   else:
    # Keep the nearby original tiles for visual inspection, never equate timing with identity.
    for n in range(64,72):
     x=n%10*480;y=n//10*270
     if image.width>=x+480 and image.height>=y+270:
      tile=image.crop((x,y,x+480,y+270));name='storyboard-%d.png'%n;tile.save(root/name);evidence['options'].append({'file':name,'source':SOURCE,'url':url,'crop_pixels':[x,y,480,270],'kind':'Public storyboard frame'})
  except Exception as exc:evidence.setdefault('image_errors',[]).append(str(exc))
 d.g.save(root/'evidence.json',evidence)
 font=ImageFont.load_default(size=16)
 for start in range(0,len(evidence['options']),32):
  options=evidence['options'][start:start+32];out=Image.new('RGB',(1440,240*((len(options)+3)//4)),(230,230,230));draw=ImageDraw.Draw(out)
  for i,option in enumerate(options):
   im=Image.open(root/option['file']).convert('RGB');im.thumbnail((356,202));x=i%4*360;y=i//4*240;out.paste(im,(x,y));draw.text((x+3,y+206),option['file']+' '+str(option.get('time_seconds','')),font=font,fill='black')
  if options:out.save(root/('contact-%02d.jpg'%(start//32+1)),quality=94)
 if selected is None:raise RuntimeError('Final identity evidence captured in qa/ability-capture; source availability and actual pixels must be reviewed')
 option=next(x for x in evidence['options'] if x['file']==selected)
 im=d.p.save_image(entry,Image.open(root/selected),option['url'],option['source'],'Visually verified holy-water ability reference',{'frame_selection':option,'original_video':ORIGINAL})
 assert im
 return im
