#!/usr/bin/env python3
"""Qualify creator media without generated placeholders or promotional browse cards."""
from __future__ import annotations
import concurrent.futures,hashlib,json,re,threading
from pathlib import Path
from urllib.parse import unquote,urljoin
from bs4 import BeautifulSoup
import collect as c
import research as r
ROOT=Path(__file__).resolve().parent
PROMO=re.compile(r'discord|patreon|ko-fi|buymeacoffee|bisect|apexhosting|kinetichosting|sparkedhost|pebblehost|server.pro|shockbyte|hosting|donat|sponsor|billing\.',re.I)
EXCLUDED_SOURCES={
 'https://theme.zdassets.com/theme_assets/678183/84b82d07b293907113d9d4dafd29bfa170bbf9b6.ico':'Discord service icon, not project art',
 'https://media.forgecdn.net/attachments/description/802940/description_0c53d939-6f38-45e3-a4f2-23d172992f8e.png':'Compatibility warning sign rather than weapon artwork'
}
LOCK=threading.Lock()


def decode(value):
 for _ in range(3):value=unquote(value)
 return value


def run():
 data=r.load(ROOT/'catalog.json');report={'removedPromotions':[],'curatedGalleryChecks':[],'curatedProjects':[]};bad=dict(EXCLUDED_SOURCES)
 # Reuse already fetched source pages; do not rescan unchanged project sites.
 for item in data['items']:
  urls=[item['projectUrl']]+[x['url'] for x in item.get('providerEvidence',[])]
  for source in urls:
   cache=ROOT/'research-cache'/(hashlib.sha256(source.encode()).hexdigest()+'.json')
   if not cache.exists():continue
   res=r.load(cache,{});body=res.get('text','')
   if not body:continue
   soup=BeautifulSoup(body,'html.parser');description=soup.select_one('.project-description')
   if not description:continue
   for im in description.select('img'):
    url=im.get('src','');anchor=im.find_parent('a');href=decode(anchor.get('href','')) if anchor else ''
    if PROMO.search(url+' '+im.get('alt','')+' '+href) or url.lower().endswith('.ico'):
     bad[url]='Promotional/service-linked image, not weapon reference media'
 # Archive all exact gallery images for the entire editorial shortlist, not a sampled subset.
 curated=[x for x in data['items'] if x['curation']=='Study anchor' or x.get('earlierPick')]
 def gallery(item):
  home=next((a['url'] for a in item['links'] if a['provider']=='CurseForge'),None)
  if not home:return item,None
  url=home.rstrip('/')+'/gallery';res=r.get(url);proof={'id':item['id'],'source':url,'status':res.get('status'),'images':0}
  if res.get('text'):
   soup=BeautifulSoup(res['text'],'html.parser');urls=set(m['url'] for m in item.get('media',[]));new=[]
   for tag in soup.select('img'):
    src=tag.get('data-src') or tag.get('src','')
    if 'media.forgecdn.net/attachments/' not in src or src in urls:continue
    if PROMO.search(src+' '+tag.get('alt','')):continue
    urls.add(src);new.append({'url':src,'alt':tag.get('alt') or item['name']+' official project gallery','role':'Project gallery','sourceUrl':url})
   if new:
    # c.media uses URL-keyed sidecars. Serialize writes to prevent a second shared-URL zero-byte reader.
    temp={'id':item['id'],'name':item['name'],'projectUrl':home,'icon':None,'gallery':new}
    with LOCK:c.media(temp)
    item['media']+=temp.get('media',[]);proof['images']=len(temp.get('media',[]))
  return item,proof
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for item,proof in pool.map(gallery,curated):
   if proof:report['curatedGalleryChecks'].append(proof)
 def score(media):
  role=media['role'];caption=(media.get('alt','')+' '+media['url']).lower();width=media.get('width',1);height=media.get('height',1)
  value=100 if role=='Project gallery' else 60 if role=='Creator description image' else 10
  if re.search(r'weapon|guns|rifle|pistol|shotgun|arsenal|firearm|musket|cannon',caption):value+=25
  if re.search(r'crafting|recipe|menu|inventory|config|armor|armour|machine|furnace',caption):value-=25
  if min(width,height)<90:value-=30
  if width/max(1,height)>3.5:value-=20
  return value
 for item in data['items']:
  kept=[];seen=set()
  for media in item.get('media',[]):
   if media['url'] in bad and media['role']!='Project icon':
    report['removedPromotions'].append({'id':item['id'],'url':media['url'],'reason':bad[media['url']]});continue
   if media['sha256'] in seen:continue
   seen.add(media['sha256']);kept.append(media)
  kept.sort(key=score,reverse=True);item['media']=kept;item['mediaStatus']='Creator media archived' if kept else 'No creator image established'
  if item in curated:report['curatedProjects'].append({'id':item['id'],'name':item['name'],'media':len(kept),'cardImage':kept[0]['src'] if kept else None})
 data['coverage']['mediaProjects']=sum(bool(x.get('media')) for x in data['items'])
 data['build']['dataHash']=hashlib.sha256(json.dumps(data['items'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
 r.save(ROOT/'catalog.json',data);r.save(ROOT/'media-review.json',report)
 # Contact sheets support a real visual review of every curated card.
 from PIL import Image,ImageDraw,ImageFont
 out=ROOT/'qa'/'curated-media';out.mkdir(parents=True,exist_ok=True);font=ImageFont.load_default(size=16)
 for start in range(0,len(curated),20):
  batch=curated[start:start+20];sheet=Image.new('RGB',(1400,240*((len(batch)+3)//4)),(232,232,232));draw=ImageDraw.Draw(sheet)
  for i,item in enumerate(batch):
   x=i%4*350;y=i//4*240;media=next((a for a in item['media'] if a['role']!='Project icon'),next(iter(item['media']),None))
   if media:
    im=Image.open(ROOT/media['src']).convert('RGBA');im.thumbnail((345,192));sheet.paste(im,(x,y),im)
   draw.text((x+3,y+196),item['name'][:42],font=font,fill='black');draw.text((x+3,y+219),item['id'],font=font,fill='black')
  sheet.save(out/('shortlist-%02d.jpg'%(start//20+1)),quality=94)
 print(json.dumps({'curatedReferences':len(curated),'promotionalImagesExcluded':len(report['removedPromotions']),'galleryImagesAdded':sum(x['images'] for x in report['curatedGalleryChecks'])}),flush=True)
 return data
if __name__=='__main__':run()
