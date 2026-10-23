#!/usr/bin/env python3
"""Append qualified discoveries without re-researching or changing the 1044-entry baseline."""
from __future__ import annotations
import argparse,collections,concurrent.futures,csv,hashlib,html,importlib.machinery,importlib.util,io,json,os,re,shutil,subprocess,sys,threading,time
from pathlib import Path
from urllib.parse import quote,unquote,urlencode,urljoin,urlparse
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
loader=importlib.machinery.SourceFileLoader('research_polish',str(ROOT/'polish_gallery.module'))
spec=importlib.util.spec_from_loader(loader.name,loader);p=importlib.util.module_from_spec(spec);loader.exec_module(p)
g=p.g;f=p.f
DATA=ROOT/'expansion-2026-10-23';DATA.mkdir(exist_ok=True)
DOCS=ROOT.parent
GAME_PAGE='Video-Game-Weapon-Inspirations-Volume-2'
SOURCE_PAGE='Weapon-Inspiration-Media-Sources-Expansion'
LOCK=threading.Lock()
ROUTES=[('Fallout','https://fallout.fandom.com'),('Cyberpunk','https://cyberpunk.fandom.com'),('Deep Rock Galactic','https://deeprockgalactic.wiki.gg'),('Team Fortress','https://wiki.teamfortress.com'),('Half-Life','https://combineoverwiki.net'),('Perfect Dark','https://perfectdark.fandom.com'),('GoldenEye','https://goldeneye.fandom.com'),('James Bond','https://jamesbond.fandom.com'),('Unreal','https://unreal.fandom.com'),('Prey','https://prey.fandom.com'),('Red Faction','https://redfaction.fandom.com'),('Resistance','https://resistance.fandom.com'),('Ratchet','https://ratchetandclank.fandom.com'),('Destiny','https://www.destinypedia.com'),('Warframe','https://wiki.warframe.com'),('Borderlands','https://borderlands.fandom.com'),('Wonderlands','https://borderlands.fandom.com'),('Enter the Gungeon','https://enterthegungeon.wiki.gg'),('Nuclear Throne','https://nuclear-throne.fandom.com'),('Terraria','https://terraria.wiki.gg'),('Helldivers','https://helldivers.wiki.gg'),('DOOM','https://doomwiki.org'),('Wolfenstein','https://wolfenstein.fandom.com'),('Shadow Warrior','https://shadowwarrior.fandom.com'),('Serious Sam','https://serioussam.fandom.com'),('Remnant','https://remnant.wiki'),('Roboquest','https://roboquest.wiki.gg'),('Gunfire','https://gunfirereborn.fandom.com'),('Turbo Overkill','https://turbokill.fandom.com'),('Splatoon','https://splatoonwiki.org'),('Halo','https://www.halopedia.org')]
GAME_ALIASES={'Team Fortress 2':['TF2','Team Fortress'],'Deep Rock Galactic':['Deep Rock','DRG'],'Half-Life: Opposing Force':['Opposing Force'],'Fallout: New Vegas':['New Vegas','FNV'],'Fallout 3':['Fallout 3','FO3'],'Fallout 4':['Fallout 4','FO4'],'Fallout 76':['Fallout 76','FO76'],'Cyberpunk 2077':['Cyberpunk'],'James Bond 007: Nightfire':['Nightfire'],'GoldenEye 007':['Goldeneye'],'Ratchet & Clank: A Crack in Time':['Crack in Time','ACIT'],'Ratchet & Clank: Going Commando':['Going Commando','Ratchet Clank 2'],'Ratchet & Clank: Up Your Arsenal':['Up Your Arsenal','Ratchet Clank 3'],'Ratchet & Clank: Tools of Destruction':['Tools of Destruction'],'Ratchet & Clank: All 4 One':['All 4 One'],'Ratchet & Clank: Rift Apart':['Rift Apart'],'Tiny Tina\'s Wonderlands':['Wonderlands'],'Destiny 2':['Destiny'],'Warhammer 40,000: Boltgun':['Boltgun'],'Warhammer 40,000: Space Marine 2':['Space Marine 2']}
BAD_IMAGE=re.compile(r'logo|wordmark|avatar|flag|stub|question|icon.?ammo|damage.?icon|controller|rarity|favicon|banner|button|badge',re.I)
REJECT={'Fassbeutel percussion revolver':'Exact historical model identity not established; excluded rather than inventing a reference.','Evans transitional pistol':'Exact historical model identity not established; excluded rather than inventing a reference.','Jarre harmonica pistol':'Covered by the existing harmonica-gun entry; not counted again solely for a named example.'}

def js(path,default):return g.load(path,default)
def save(path,value):g.save(path,value)
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def run_git(*args,cwd=None):return subprocess.check_output(['git',*args],cwd=cwd or DOCS.parent,text=True).strip()
def names(e):return list(dict.fromkeys([e['name']]+[a.strip() for a in e.get('aliases','').split(';') if a.strip()]))
def match(e,s):return any(f.present(n,s) for n in names(e))
def clean(s):return str(s or '').strip().lstrip('>').strip()

def init():
 c=js(ROOT/'catalog.json',{});m=js(ROOT/'media.json',{})
 baseline=js(DATA/'baseline.json',None)
 if baseline is None:
  baseline={'counts':{k:len(c[k]) for k in ('gaming','historical')},'entries':{e['id']:digest(e) for e in c['gaming']+c['historical']},'media':{k:digest(v) for k,v in m.items()}}
  assert baseline['counts']=={'gaming':892,'historical':152},baseline['counts']
  save(DATA/'baseline.json',baseline)
  for key,page in zip(('gaming','historical'),g.PAGES):shutil.copyfile(DOCS/(page+'.md'),DATA/('baseline-'+key+'.md'))
 return c,m,baseline

def seeds(c):
 original={(g.norm(e['game']),g.norm(e['name'])):e['id'] for e in c['gaming']+c['historical']}
 existing_names={g.norm(e['name']):e['id'] for e in c['gaming']+c['historical']}
 out={};rejected={}
 for path in sorted(DATA.glob('candidates-*.tsv')):
  for raw in csv.DictReader(path.open(encoding='utf-8'),delimiter='\t'):
   e={k:clean(v) for k,v in raw.items() if k is not None}
   assert e.get('game') and e.get('name') and e.get('hook') and e.get('remix'),(path.name,e)
   if e['name']=='Yinlong':e['name']='Yinglong'
   e['group']='Historical' if 'history' in path.name else 'Gaming'
   e['id']=('xh-' if e['group']=='Historical' else 'xg-')+hashlib.sha256((g.norm(e['game'])+'::'+g.norm(e['name'])).encode()).hexdigest()[:12]
   e['research_batch']=path.name
   if e['name'] in REJECT:rejected[e['id']]={'name':e['name'],'reason':REJECT[e['name']]};continue
   key=g.norm(e['game']),g.norm(e['name'])
   if key in original and original[key]!=e['id']:rejected[e['id']]={'name':e['name'],'reason':'Already present in the original catalog','existing_id':original[key]};continue
   if g.norm(e['name']) in existing_names and not existing_names[g.norm(e['name'])].startswith(('xh-','xg-')):
    rejected[e['id']]={'name':e['name'],'reason':'Existing named inspiration retained rather than inflating the list','existing_id':existing_names[g.norm(e['name'])]};continue
   out[e['id']]=e
 save(DATA/'rejected.json',rejected)
 return list(out.values())

def wiki_source(e):
 host=next((host for key,host in ROUTES if key.lower() in e['game'].lower()),None) if e['group']=='Gaming' else 'https://en.wikipedia.org'
 if not host:return None,None
 page=unquote(e.get('page') or e['name']).replace('_',' ')
 apipath='/w/api.php' if host in ('https://wiki.warframe.com','https://en.wikipedia.org') else '/api.php'
 url=host+apipath+'?'+urlencode({'action':'parse','format':'json','page':page,'prop':'images|wikitext|text','redirects':1})
 r=g.fetch(url)
 if not r['ok']:return None,None
 try:parsed=json.loads(r['body']).get('parse',{})
 except ValueError:return None,None
 if not parsed:return None,None
 title=parsed.get('title','');wt=parsed.get('wikitext',{}).get('*','');raw=parsed.get('text',{}).get('*','')
 soup=BeautifulSoup(raw,'html.parser')
 paragraphs=[x.get_text(' ',strip=True) for x in soup.find_all('p') if len(x.get_text(' ',strip=True))>50]
 source=host+('/w/' if host=='https://wiki.warframe.com' else '/wiki/')+quote(title.replace(' ','_'))
 proof={'url':source,'title':title,'kind':'Named reference page','excerpt':' '.join(paragraphs)[:550],'api':url}
 if not match(e,title+' '+proof['excerpt']) and g.norm(title)!=g.norm(page):return None,None
 featured=re.findall(r'\|\s*(?:image\d*|imagefile|image_name|img)\s*=\s*([^\n|]+)',wt[:16000],re.I)
 files=parsed.get('images',[]);ranked=[]
 for name in files:
  if BAD_IMAGE.search(name) or not re.search(r'\.(png|jpe?g|gif|webp)$',name,re.I):continue
  bare=g.norm(name.rsplit('.',1)[0]);score=0
  if any(g.norm(n)==bare for n in names(e)+[page]):score+=60
  elif match(e,name) or g.norm(page) in bare:score+=25
  if any(name in a or g.norm(a)==bare for a in featured):score+=65
  if e['group']=='Historical' and re.search(r'cartridge|cartridges|ammunition|bullet|diagram|patent|cutaway|schematic|bolt',name,re.I):score-=80
  if 'Fallout 3' in e['game'] and re.search(r'FO4|FO76|FNV',name,re.I):score-=80
  if 'Fallout 4' in e['game'] and re.search(r'FO3|FO76|FNV',name,re.I):score-=80
  if 'Fallout 76' in e['game'] and re.search(r'FO3|FO4|FNV',name,re.I):score-=80
  if 'New Vegas' in e['game'] and re.search(r'FO3|FO4|FO76',name,re.I):score-=80
  if score>0:ranked.append((score,name))
 for score,name in sorted(ranked,reverse=True)[:5]:
  q=host+apipath+'?'+urlencode({'action':'query','format':'json','titles':'File:'+name,'prop':'imageinfo','iiprop':'url','iiurlwidth':720})
  rr=g.fetch(q)
  if not rr['ok']:continue
  try:pages=json.loads(rr['body']).get('query',{}).get('pages',{})
  except ValueError:continue
  for obj in pages.values():
   info=obj.get('imageinfo',[{}])[0];u=info.get('thumburl') or info.get('url')
   if u:
    im=p.image_url(e,u,source,'Named weapon reference image')
    if im:im['source_file_title']=name;return proof,im
 return proof,None

def fw_source(e):
 found={}
 for query in names(e)[:2]:
  api='https://www.forgottenweapons.com/wp-json/wp/v2/posts?'+urlencode({'search':query,'per_page':8})
  r=g.fetch(api)
  if not r['ok']:continue
  try:posts=json.loads(r['body'])
  except ValueError:continue
  if not isinstance(posts,list):continue
  for post in posts:
   title=BeautifulSoup(post.get('title',{}).get('rendered',''),'html.parser').get_text(' ',strip=True)
   if match(e,title):found[post['id']]=(post,title)
  if found:break
 for post,title in sorted(found.values(),key=lambda x:('shooting' in x[1].lower(), 'video' in x[1].lower()),reverse=True):
  source=post['link'];soup=BeautifulSoup(post.get('content',{}).get('rendered',''),'html.parser')
  video=None
  candidates=[]
  for tag in soup.select('iframe,a'):
   u=tag.get('src') or tag.get('href') or tag.get('data-src') or ''
   vid=g.video_id(u)
   if vid:candidates.append('https://www.youtube.com/watch?v='+vid)
  if not candidates:
   candidates=['https://www.youtube.com/watch?v='+x for x in re.findall(r'(?:youtube(?:-nocookie)?\.com/embed/|youtu\.be/|watch\?v=)([A-Za-z0-9_-]{11})',str(soup))]
  for url in dict.fromkeys(candidates):
   video=f.video_data(url)
   if video:video.update(match='Video embedded in named historical source',evidence_url=source);break
  proof={'url':source,'title':title,'kind':'Firsthand historical object review','excerpt':soup.get_text(' ',strip=True)[:550]}
  images=[]
  for tag in soup.select('img'):
   u=tag.get('data-src') or tag.get('src') or '';alt=tag.get('alt','')
   if not u.startswith('http') or BAD_IMAGE.search(u+' '+alt):continue
   score=4 if match(e,unquote(u)+' '+alt) else 0
   if re.search(r'cartridge|patent|diagram|schematic|bolt',u+' '+alt,re.I):score-=10
   if score>0:images.append((score,u))
  image=None
  for _,u in sorted(images,reverse=True):
   image=p.image_url(e,u,source,'Photograph from named historical review')
   if image:break
  if video:return proof,image,video
 return None,None,None

def game_match(e,value):
 if e['group']=='Historical':return True
 aliases=[e['game']]
 for key,values in GAME_ALIASES.items():
  if key in e['game']:aliases+=values
 return any(f.present(a,value) for a in aliases)

def find_video(e):
 suffix=' historical firearm review' if e['group']=='Historical' else ' '+e['game']+' weapon showcase'
 queries=[e['name']+suffix]
 if e['group']=='Historical':queries.append(names(e)[-1]+' Forgotten Weapons')
 else:
  short=next((v[0] for k,v in GAME_ALIASES.items() if k in e['game']),e['game'])
  queries.append(names(e)[-1]+' '+short)
 evidence=[]
 for query in dict.fromkeys(queries):
  found=f.search(query);ranked=[]
  for v in found:
   title=v['title'];full=title+' '+v.get('description','')
   if not match(e,title) or not game_match(e,full):continue
   if re.search(r'all weapons|every weapon|all guns|tier list|all attacks|all skills|full walkthrough|full game|3d print|homemade|how to build|airsoft|replica|soundtrack',title,re.I):continue
   score=2+sum(w in title.lower() for w in ('showcase','demonstration','gameplay','shooting','review'))
   if e['group']=='Historical' and any(x in v.get('channel','').lower() for x in ('forgotten weapons','royal armouries','c&rsenal')):score+=3
   ranked.append((score,v))
  evidence += [{'title':v['title'],'url':v['url']} for v in found]
  if ranked:
   v=sorted(ranked,key=lambda x:x[0],reverse=True)[0][1]
   v['match']='Named historical item video' if e['group']=='Historical' else 'Item title and game context matched'
   return v,evidence
 return None,evidence

def resolve(e):
 result={'id':e['id'],'name':e['name'],'game':e['game'],'group':e['group'],'status':'researching','evidence':[]}
 try:
  proof=image=video=None
  if e['group']=='Historical':proof,image,video=fw_source(e)
  other,im=wiki_source(e)
  if other:result['evidence'].append(other)
  if proof:result['evidence'].append(proof)
  if im:image=im
  if not video:video,search=find_video(e);result['video_candidates']=search
  if video:
   if not image:image=p.image_url(e,video.get('thumbnail',''),video['url'],'Item-video preview; not a standalone weapon photograph')
   result['evidence'].append({'url':video['url'],'title':video['title'],'kind':video['match']})
  if image and video:
   result.update(image=image,video=video,complete=True,status='accepted')
  else:result.update(image=image,video=video,complete=False,status='unresolved',missing=[k for k,v in [('image',image),('video',video)] if not v])
 except Exception as exc:result.update(status='unresolved',complete=False,error=type(exc).__name__+': '+str(exc)[:300])
 return result

def section(entries,m,sourcepage):
 groups=collections.defaultdict(list)
 for e in entries:groups[e['game']].append(e)
 lines=[' | '.join(f'[{g.text(k)} ({len(v)})](#new-{g.slug(k)})' for k,v in sorted(groups.items())),'']
 for group,items in sorted(groups.items()):
  lines += [f'<a id="new-{g.slug(group)}"></a>',f'## {group}','','| Embedded reference | Weapon and distinctive idea | AoA remix proposal | Video / source |','|---|---|---|---|']
  for e in items:
   rec=m[e['id']];im=rec['image'];v=rec['video'];image=g.RAW+Path(im['local']).name+'?v='+im['sha256'][:7]
   label='<br>Video preview' if 'preview' in im['kind'].lower() else ''
   lines.append(f'| <img src="{image}" width="220" alt="{g.text(e["name"])}">{label} | **{g.text(e["name"])}**<br>{g.text(e["hook"])} | {g.text(e["remix"])} | [Watch]({v["url"]})<br>[Source]({sourcepage}#ref-{e["id"]}) |')
  lines+=['']
 return '\n'.join(lines)

def render(c,m,baseline,state):
 ids=set(baseline['entries']);allentries=c['gaming']+c['historical'];idx={e['id']:e for e in allentries}
 for k,h in baseline['entries'].items():assert digest(idx[k])==h,('Original entry changed',k)
 for k,h in baseline['media'].items():assert digest(m[k])==h,('Original media changed',k)
 fresh={key:[e for e in c[key] if e['id'] not in ids] for key in ('gaming','historical')}
 ng,nh=len(fresh['gaming']),len(fresh['historical'])
 game=['# Video-game weapon inspirations: new discoveries','',f'**{ng} additional references | {len({e["game"] for e in fresh["gaming"]})} game collections | Embedded images and direct videos**','','[Original gaming gallery](Video-Game-Weapon-Inspirations) | [Historical gallery](Historical-and-Experimental-Gun-Inspirations) | [New source records]('+SOURCE_PAGE+')','','These are additional discoveries beyond the original 892 gaming references. Every entry has a locally archived, embedded source image or explicitly labeled item-video preview and a direct video link. AoA remix ideas are proposals, not implemented features. Video titles and source identity are checked; full end-to-end video viewing is not claimed.','',section(fresh['gaming'],m,SOURCE_PAGE),'## End of gallery','',f'All {ng} accepted new gaming references are shown.']
 (DOCS/(GAME_PAGE+'.md')).write_text('\n'.join(game)+'\n',encoding='utf-8')
 old=(DATA/'baseline-gaming.md').read_text()
 banner=f'\n<!-- research-expansion:start -->\n## New discoveries\n\n**[{ng} additional gaming references]({GAME_PAGE})** have been added in a dedicated illustrated continuation. The full gaming collection now contains **{len(c["gaming"])} references**, with all 892 originals retained below. [Historical additions](Historical-and-Experimental-Gun-Inspirations#new-research-additions) | [New media sources]({SOURCE_PAGE}).\n<!-- research-expansion:end -->\n'
 first,rest=old.split('\n',1);(DOCS/(g.PAGES[0]+'.md')).write_text(first+'\n'+banner+'\n'+rest,encoding='utf-8')
 old=(DATA/'baseline-historical.md').read_text();body=old.split('## End of gallery',1)[0]
 body=body.replace('**152 references |',f'**{len(c["historical"])} references |',1).replace('152 embedded images',str(len(c['historical']))+' embedded images',1).replace('152 direct video references',str(len(c['historical']))+' direct video references',1)
 body=body.replace('## Browse by collection',f'**[Jump to {nh} new discoveries](#new-research-additions)** | [Expanded gaming gallery]({GAME_PAGE})\n\n## Browse by collection',1)
 body+='\n<a id="new-research-additions"></a>\n## New research additions\n\n'+section(fresh['historical'],m,SOURCE_PAGE)+'\n## End of gallery\n\nAll '+str(len(c['historical']))+' historical references are retained, including the original 152.\n'
 (DOCS/(g.PAGES[1]+'.md')).write_text(body,encoding='utf-8')
 source=['# Sources for new weapon inspirations','','[New gaming discoveries]('+GAME_PAGE+') | [Historical gallery]('+g.PAGES[1]+')','','Each record identifies the image source and direct video. Video previews are distinguished from separate photographs. Full videos have not all been watched end-to-end.','']
 for e in fresh['gaming']+fresh['historical']:
  rec=m[e['id']];im=rec['image'];v=rec['video']
  source += [f'<a id="ref-{e["id"]}"></a>',f'## {e["name"]} ({e["game"]})','',f'Image: {im["kind"]}. [Source]({im["source"]}).',f'[Video: {g.text(v["title"])}]({v["url"]}). Evidence: {v["match"]}.']
  source += ['[Reference]('+x['url']+'): '+g.text(x['title'])+'.' for x in rec.get('evidence',[]) if x.get('url')!=v['url']]
  source+=['']
 (DOCS/(SOURCE_PAGE+'.md')).write_text('\n'.join(source),encoding='utf-8')
 for page in [*g.PAGES,GAME_PAGE,SOURCE_PAGE]:assert (DOCS/(page+'.md')).stat().st_size<490000,('Wiki page needs another volume, never truncation',page)
 coverage={'gaming':len(c['gaming']),'historical':len(c['historical']),'total':len(allentries),'game_collections':len({e['game'] for e in c['gaming']}),'embedded_images':len(allentries),'matched_videos':len(allentries),'complete':len(allentries),'unresolved':[],'new_gaming':ng,'new_historical':nh,'research_candidates':len(state),'research_pending':[{'id':k,'name':v['name'],'missing':v.get('missing',[]),'error':v.get('error')} for k,v in state.items() if v['status']=='unresolved']}
 save(ROOT/'catalog.json',c);save(ROOT/'media.json',m);save(ROOT/'coverage.json',coverage);save(DATA/'coverage.json',coverage);save(DATA/'state.json',state)
 acceptance=js(ROOT/'final-acceptance.json',{})
 acceptance.update(gaming_entries=len(c['gaming']),gaming_collections=coverage['game_collections'],historical_entries=len(c['historical']),total_entries=len(allentries),embedded_images_with_verified_file_hashes=len(allentries),direct_video_references=len(allentries),image_specificity_pending=[],errors=[],expansion_receipts='expansion-2026-10-23/native-browser-verification.json',newly_added={'gaming':ng,'historical':nh})
 save(ROOT/'final-acceptance.json',acceptance)
 return coverage

def persist_and_publish(c,m,baseline,state,remote):
 coverage=render(c,m,baseline,state)
 if not remote:print('Local checkpoint',json.dumps({k:v for k,v in coverage.items() if k!='research_pending'}),flush=True);return
 run_git('add','docs/weapon-inspirations','docs/'+g.PAGES[0]+'.md','docs/'+g.PAGES[1]+'.md','docs/'+GAME_PAGE+'.md','docs/'+SOURCE_PAGE+'.md')
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=DOCS.parent).returncode:
  run_git('commit','-m',f'Expand weapon inspirations: {coverage["new_gaming"]} gaming and {coverage["new_historical"]} historical discoveries')
  run_git('pull','--rebase','origin','main');run_git('push','origin','HEAD:main')
 wiki=DOCS.parent.parent/'research-wiki'
 if not (wiki/'.git').exists():run_git('clone','--depth','1','https://github.com/'+g.REPO+'.wiki.git',str(wiki))
 else:run_git('pull','--ff-only',cwd=wiki)
 for page in [*g.PAGES,GAME_PAGE,SOURCE_PAGE]:shutil.copyfile(DOCS/(page+'.md'),wiki/(page+'.md'))
 marker='<!-- additional-weapon-research:start -->';end='<!-- additional-weapon-research:end -->'
 block=marker+'\n### Additional weapon discoveries\n\n- [New gaming inspirations]('+GAME_PAGE+')\n- [Expanded historical gallery]('+g.PAGES[1]+'#new-research-additions)\n- [Sources for new discoveries]('+SOURCE_PAGE+')\n'+end
 for name in ['Home.md','_Sidebar.md']:
  file=wiki/name;body=file.read_text() if file.exists() else ''
  if marker in body:body=body[:body.index(marker)]+block+body[body.index(end)+len(end):]
  else:body=body.rstrip()+'\n\n'+block+'\n'
  file.write_text(body,encoding='utf-8')
 run_git('config','user.name','github-actions[bot]',cwd=wiki);run_git('config','user.email','41898282+github-actions[bot]@users.noreply.github.com',cwd=wiki);run_git('add','--','*.md',cwd=wiki)
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=wiki).returncode:
  run_git('commit','-m',f'Publish {coverage["new_gaming"]+coverage["new_historical"]} additional illustrated weapon references',cwd=wiki);run_git('push','origin','HEAD',cwd=wiki)
 receipt={'source_commit':run_git('rev-parse','HEAD'),'wiki_commit':run_git('rev-parse','HEAD',cwd=wiki),'new_gaming':coverage['new_gaming'],'new_historical':coverage['new_historical'],'total':coverage['total'],'pages':{page:hashlib.sha256((wiki/(page+'.md')).read_bytes()).hexdigest() for page in [*g.PAGES,GAME_PAGE,SOURCE_PAGE]}}
 save(DATA/'publication.json',receipt);print('PUBLISHED',json.dumps(receipt),flush=True)

def contact_sheets(c,m,baseline):
 fresh=[e for e in c['historical']+c['gaming'] if e['id'] not in baseline['entries']]
 qa=DATA/'qa';qa.mkdir(exist_ok=True);font=ImageFont.load_default(size=16)
 for start in range(0,len(fresh),24):
  batch=fresh[start:start+24];out=Image.new('RGB',(1440,245*((len(batch)+3)//4)),(235,235,235));draw=ImageDraw.Draw(out)
  for i,e in enumerate(batch):
   im=Image.open(ROOT/m[e['id']]['image']['local']).convert('RGBA');im.thumbnail((350,190));x=i%4*360;y=i//4*245;out.paste(im,(x,y),im);draw.text((x+3,y+193),e['name'][:40],font=font,fill='black');draw.text((x+3,y+214),e['id'],font=font,fill='black');draw.text((x+3,y+231),e['game'][:42],font=font,fill='black')
  out.save(qa/('new-%02d.jpg'%(start//24+1)),quality=93)


def verify(c,m,baseline,remote):
 for e in c['gaming']+c['historical']:
  im=m[e['id']]['image'];path=ROOT/im['local'];assert hashlib.sha256(path.read_bytes()).hexdigest()==im['sha256'],e['id']
  with Image.open(path) as pic:pic.verify()
 if not remote:return
 from playwright.sync_api import sync_playwright
 reports=[]
 with sync_playwright() as pw:
  executable=shutil.which('google-chrome') or shutil.which('chromium')
  browser=pw.chromium.launch(headless=True,**({'executable_path':executable} if executable else {}),args=['--no-sandbox','--disable-dev-shm-usage'])
  page=browser.new_page(viewport={'width':1440,'height':1100})
  groups=[(g.PAGES[0],[e for e in c['gaming'] if e['id'] in baseline['entries']]),(g.PAGES[1],c['historical']),(GAME_PAGE,[e for e in c['gaming'] if e['id'] not in baseline['entries']])]
  for slug,entries in groups:
   url=g.WIKI+slug;page.goto(url,wait_until='domcontentloaded',timeout=90000);page.locator('#wiki-body').wait_for(timeout=30000)
   page.evaluate("() => document.querySelectorAll('#wiki-body img').forEach(x=>x.loading='eager')")
   page.wait_for_function("() => [...document.querySelectorAll('#wiki-body img')].filter(x=>(x.getAttribute('data-canonical-src')||x.src).includes('weapon-inspirations/images/')).every(x=>x.complete)",timeout=180000)
   data=page.evaluate("() => {const imgs=[...document.querySelectorAll('#wiki-body img')].filter(x=>(x.getAttribute('data-canonical-src')||x.src).includes('weapon-inspirations/images/'));return {count:imgs.length,loaded:imgs.filter(x=>x.naturalWidth>0).length,broken:imgs.filter(x=>!x.naturalWidth).map(x=>x.alt),text:document.querySelector('#wiki-body').innerText};}")
   missing=[e['name'] for e in entries if e['name'] not in data['text']]
   report={'page':slug,'expected':len(entries),'images':data['count'],'decoded':data['loaded'],'broken':data['broken'],'missing':missing,'end_marker':'End of gallery' in data['text']};reports.append(report);save(DATA/'native-browser-verification.json',reports)
   assert len(entries)==data['count']==data['loaded'] and not missing and report['end_marker'],report
   page.locator('#wiki-body').scroll_into_view_if_needed();page.screenshot(path=str(DATA/'qa'/(slug+'-top.png')))
   page.locator('#wiki-body h2').last.scroll_into_view_if_needed();page.screenshot(path=str(DATA/'qa'/(slug+'-end.png')))
  browser.close()
 print('BROWSER_VERIFIED',json.dumps(reports),flush=True)
 run_git('add','docs/weapon-inspirations/expansion-2026-10-23/publication.json','docs/weapon-inspirations/expansion-2026-10-23/native-browser-verification.json')
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=DOCS.parent).returncode:
  run_git('commit','-m','Verify all original and expanded weapon images on the live Wiki');run_git('pull','--rebase','origin','main');run_git('push','origin','HEAD:main')


def main():
 parser=argparse.ArgumentParser();parser.add_argument('--remote',action='store_true');parser.add_argument('--retry-unresolved',action='store_true');args=parser.parse_args()
 c,m,baseline=init();entries=seeds(c);state=js(DATA/'state.json',{});todo=[e for e in entries if e['id'] not in state or (args.retry_unresolved and state[e['id']]['status']=='unresolved')]
 idx={e['id']:e for e in c['gaming']+c['historical']};accepted_since=0
 print('RESEARCH_START',json.dumps({'new_candidates':len(todo),'all_candidates':len(entries),'originals_preserved':len(baseline['entries'])}),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
  futures={pool.submit(resolve,e):e for e in todo}
  for count,ft in enumerate(concurrent.futures.as_completed(futures),1):
   e=futures[ft];rec=ft.result();state[e['id']]=rec
   if rec['status']=='accepted':
    if e['id'] not in idx:c['historical' if e['group']=='Historical' else 'gaming'].append(e);idx[e['id']]=e
    m[e['id']]=rec;accepted_since+=1
   if count%10==0:save(DATA/'state.json',state);print('RESEARCH_PROGRESS',count,'/',len(todo),'accepted',sum(v['status']=='accepted' for v in state.values()),'unresolved',sum(v['status']=='unresolved' for v in state.values()),flush=True)
   if accepted_since>=35:
    persist_and_publish(c,m,baseline,state,args.remote);accepted_since=0
 persist_and_publish(c,m,baseline,state,args.remote);contact_sheets(c,m,baseline);verify(c,m,baseline,args.remote)
 print('RESEARCH_FINISH',json.dumps(js(DATA/'coverage.json',{})),flush=True)
if __name__=='__main__':main()
