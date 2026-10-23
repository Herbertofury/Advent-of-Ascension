#!/usr/bin/env python3
"""Use a named source icon for the one short-lived ability reference."""
import concurrent.futures,io,json,re
from pathlib import Path
from urllib.parse import urlencode,urljoin
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw,ImageFont

def run(d,entry,selected=None):
 root=d.ROOT/'qa'/'ability-source';root.mkdir(parents=True,exist_ok=True)
 host='https://forgive-me-father.fandom.com'
 api=host+'/api.php?'+urlencode({'action':'parse','format':'json','page':'Priest','prop':'images|wikitext','redirects':1})
 report={'page':host+'/wiki/Priest','options':[],'api_status':None}
 r=d.g.fetch(api);report['api_status']=r.get('status')
 names=[]
 if r['ok']:
  try:
   parsed=json.loads(r['body']).get('parse',{});names=parsed.get('images',[]);report['image_names']=names;report['source_text']=parsed.get('wikitext',{}).get('*','')
  except ValueError:pass
 if names:
  query=host+'/api.php?'+urlencode({'action':'query','format':'json','titles':'|'.join('File:'+n for n in names),'prop':'imageinfo','iiprop':'url','iiurlwidth':720})
  rr=d.g.fetch(query)
  if rr['ok']:
   try:
    for obj in json.loads(rr['body']).get('query',{}).get('pages',{}).values():
     info=obj.get('imageinfo',[{}])[0];url=info.get('url')
     if url:report['options'].append({'title':obj['title'],'url':url,'source':report['page']})
   except ValueError:pass
 if not report['options']:
  r=d.g.fetch(report['page']);report['page_status']=r.get('status')
  if r['ok']:
   soup=BeautifulSoup(r['body'],'html.parser');article=soup.select_one('.mw-parser-output') or soup
   report['source_text']=article.get_text(' ',strip=True)
   for tag in article.select('img'):
    url=tag.get('data-src') or tag.get('src','');name=tag.get('alt','')
    if url.startswith('http') and not re.search('logo|avatar|flag',url+' '+name,re.I):report['options'].append({'title':name,'url':url,'source':report['page']})
 images=[]
 for i,option in enumerate(report['options']):
  rr=d.g.fetch(option['url'],binary=True)
  if not rr['ok']:continue
  try:
   image=Image.open(io.BytesIO(rr['body']));image.save(root/('option-%02d.png'%i));option['file']='option-%02d.png'%i;option['dimensions']=list(image.size);images.append((i,option,image))
  except Exception:pass
 if images:
  contact=Image.new('RGB',(1440,270*((len(images)+3)//4)),(224,224,224));draw=ImageDraw.Draw(contact);font=ImageFont.load_default(size=16)
  for n,(i,option,im) in enumerate(images):
   im=im.convert('RGBA');im.thumbnail((350,220));x=n%4*360;y=n//4*270;contact.paste(im,(x,y),im);draw.text((x+3,y+224),'%02d %s'%(i,option['title'][:34]),font=font,fill='black')
  contact.save(root/'contact.jpg',quality=94)
 d.g.save(root/'evidence.json',report)
 if selected is None:raise RuntimeError('Inspect exact ability source art in qa/ability-source; all existing gallery entries preserved')
 option=report['options'][selected];image=Image.open(root/option['file'])
 return d.p.save_image(entry,image,option['url'],option['source'],'Named holy-water ability icon from its character reference page',{'source_file_title':option['title']})
