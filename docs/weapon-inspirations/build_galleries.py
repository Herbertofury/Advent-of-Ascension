#!/usr/bin/env python3
"""Build provenance-preserving, illustrated AoA reference galleries."""
from __future__ import annotations
import argparse, base64, collections, concurrent.futures, csv, hashlib, html, io, json, lzma, re, shutil, threading, time, unicodedata
from pathlib import Path
from urllib.parse import quote, urlencode, urljoin, urlparse, parse_qs
import requests
from bs4 import BeautifulSoup
from PIL import Image
ROOT = Path(__file__).resolve().parent
DOCS = ROOT.parent
REPO = 'Herbertofury/Advent-of-Ascension'
RAW = 'https://raw.githubusercontent.com/' + REPO + '/main/docs/weapon-inspirations/images/'
WIKI = 'https://github.com/' + REPO + '/wiki/'
PAGES = ['Video-Game-Weapon-Inspirations', 'Historical-and-Experimental-Gun-Inspirations']
EXPECTED = '3895a4fb3927c025bd93511ef681f2cf12baf2de67bec71d72c7581a6bc3d684'
UA = 'Mozilla/5.0 (compatible; AoAReferenceGallery/1.0; public historical and game design research)'
LOCK = threading.Lock()
URL_LOCKS = {}
MEM = {}
LOCAL = threading.local()

def session():
    if not hasattr(LOCAL, 's'):
        LOCAL.s = requests.Session(); LOCAL.s.headers.update({'User-Agent': UA})
    return LOCAL.s

def save(path, obj):
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8'); temp.replace(path)

def load(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default

def fetch(url, *, binary=False):
    with LOCK:
        lock = URL_LOCKS.setdefault(url, threading.Lock())
    with lock:
        if url in MEM: return MEM[url]
        result = {'url': url, 'ok': False}
        try:
            r = session().get(url, timeout=(10, 28))
            result.update(status=r.status_code, final_url=r.url, content_type=r.headers.get('Content-Type', ''))
            if r.ok and len(r.content) <= 18000000:
                result.update(ok=True, body=r.content if binary else r.text)
            elif r.status_code == 429:
                result['retry_after'] = r.headers.get('Retry-After')
        except requests.RequestException as exc:
            result['error'] = str(exc)[:300]
        MEM[url] = result
        return result

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', unicodedata.normalize('NFKD', str(s or '')).encode('ascii','ignore').decode().lower()).strip()

def slug(s): return re.sub(r'[^a-z0-9]+', '-', norm(s)).strip('-')
def text(s): return html.escape(str(s or '')).replace('|','&#124;').replace('\n',' ')
def tokens(s): return set(norm(s).split()) - {'the','of','and','a','an','gun','rifle','pistol','weapon','weapons','model','game','games','call','duty','war','black','ops'}

def name_match(name, value):
    n, v = norm(name), norm(value)
    if n and n in v: return 1.0
    a, b = tokens(name), set(v.split())
    if not a: return 0.0
    return len(a & b) / len(a)

def video_id(url):
    if not url: return ''
    p=urlparse(url)
    if p.netloc in ('youtu.be','www.youtu.be'): return p.path.strip('/').split('/')[0]
    if 'youtube.com' in p.netloc:
        if p.path == '/watch': return parse_qs(p.query).get('v',[''])[0]
        if p.path.startswith(('/shorts/','/embed/')): return p.path.split('/')[2]
    return ''

def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values(): yield from walk(value)
    elif isinstance(obj,list):
        for value in obj: yield from walk(value)

def txt(obj):
    if not isinstance(obj,dict): return ''
    return obj.get('simpleText') or ''.join(x.get('text','') for x in obj.get('runs',[]))

HISTORY_ALIASES = {
'DP-28':'Degtyaryov machine gun','Vickers K':'Vickers K machine gun','Bren gun':'Bren light machine gun','ZB vz. 26':'ZB vz. 26','Type 11 LMG':'Type 11 light machine gun','North Korean Type 88':'Type 88 assault rifle','Johnson M1941 LMG':'M1941 Johnson machine gun','SA80 L85':'SA80','Tavor X95':'IWI X95','Heckler & Koch G11':'Heckler & Koch G11','Mateba Model 6 Unica':'Mateba Autorevolver','Dardick Tround':'Dardick tround','Bergmann 1896':'Bergmann 1896','Schwarzlose Model 1898':'Schwarzlose Model 1898','AF2011-A1 double barrel':'Arsenal Firearms AF2011A1','S333 Thunderstruck':'S333 Thunderstruck','Duck\'s Foot pistol':'Duck foot pistol','COP .357 Derringer':'COP .357 Derringer','Kel-Tec KSG-25':'Kel-Tec KSG','SRM 1216':'SRM Arms Model 1216','AA-12':'Atchisson AA-12','Atchisson Assault Shotgun':'Atchisson AA-12','M134 Minigun':'Minigun','GAU-8 Avenger':'GAU-8 Avenger','M61 Vulcan':'M61 Vulcan','GSh-6-23':'Gryazev-Shipunov GSh-6-23','Metal Storm Redback':'Metal Storm','Krummlauf':'Krummlauf','Henry 1860':'Henry rifle','Schmidt-Rubin K31':'K31','Magpul FMG-9':'Magpul FMG-9','B&T MP9':'Brugger & Thomet MP9','Vz. 61 Skorpion':'Skorpion','HK MP7':'Heckler & Koch MP7','HK CAWS':'Heckler & Koch HK CAWS','OICW XM29':'XM29 OICW','K11 dual-barrel':'S&T Daewoo K11','Anzio 20mm rifle':'Anzio 20mm rifle','Bazooka M1':'Bazooka','HK69 grenade launcher':'Heckler & Koch HK69A1','Lifebuoy flamethrower':'Flamethrower, Portable, No 2','Snaphaunce musket':'Snaphance','Gustloff Volkssturmgewehr':'Volkssturmgewehr','FP-45 Liberator':'FP-45 Liberator'}

WIKI_ROUTES = [
('Warframe','https://wiki.warframe.com/w/'),('Terraria','https://terraria.wiki.gg/wiki/'),('Enter the Gungeon','https://enterthegungeon.wiki.gg/wiki/'),('Destiny','https://www.destinypedia.com/'),('Halo','https://www.halopedia.org/'),('Ratchet','https://ratchetandclank.fandom.com/wiki/'),('Borderlands','https://borderlands.fandom.com/wiki/'),('Wonderlands','https://borderlands.fandom.com/wiki/'),('ULTRAKILL','https://ultrakill.wiki.gg/wiki/'),('Splatoon','https://splatoonwiki.org/wiki/'),('Dead Space','https://deadspace.fandom.com/wiki/'),('Quake','https://quake.fandom.com/wiki/'),('Unreal','https://unreal.fandom.com/wiki/'),('Turok','https://turok.fandom.com/wiki/'),('Resistance','https://resistance.fandom.com/wiki/'),('Half-Life','https://combineoverwiki.net/wiki/'),('Portal','https://theportalwiki.com/wiki/'),('DOOM','https://doomwiki.org/wiki/'),('Duke','https://dukenukem.fandom.com/wiki/'),('Returnal','https://returnal.fandom.com/wiki/'),('Control','https://control.fandom.com/wiki/'),('Metroid','https://metroid.fandom.com/wiki/'),('Mega Man','https://megaman.fandom.com/wiki/'),('Jak','https://jakanddaxter.fandom.com/wiki/'),('Gunfire','https://gunfirereborn.fandom.com/wiki/'),('Noita','https://noita.wiki.gg/wiki/'),('Gears','https://gearsofwar.fandom.com/wiki/'),('Titanfall','https://titanfall.fandom.com/wiki/')]

def sources_for(e):
    values=[]
    if e.get('source'): values.append(e['source'])
    if e['group']=='Historical':
        title=HISTORY_ALIASES.get(e['name'],e['name'])
        values.append('https://en.wikipedia.org/wiki/'+quote(title.replace(' ','_')))
    else:
        for key,base in WIKI_ROUTES:
            if key.lower() in e['game'].lower():
                n=e['name'].replace('Service Weapon ','').replace(' Spell','')
                values.append(base+quote(n.replace(' ','_'))); break
    return list(dict.fromkeys(values))

def image_file(e, url, kind, source):
    if not url or not url.startswith('http'): return None
    res=fetch(url,binary=True)
    if not res['ok']: return None
    try:
        image=Image.open(io.BytesIO(res['body'])); image.seek(0)
        if min(image.size)<32 or max(image.size)<70: return None
        original_size=image.size
        image.thumbnail((720,480))
        if image.mode not in ('RGB','RGBA'): image=image.convert('RGBA' if 'transparency' in image.info else 'RGB')
        path=ROOT/'images'/(e['id']+'.webp'); path.parent.mkdir(exist_ok=True)
        image.save(path,'WEBP',quality=88,method=5)
        return {'url':url,'source':source,'kind':kind,'local':'images/'+path.name,'width':image.width,'height':image.height,'original_dimensions':list(original_size),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}
    except Exception: return None

def wikipedia_image(e):
    title=HISTORY_ALIASES.get(e['name'],e['name'])
    url='https://en.wikipedia.org/w/api.php?'+urlencode({'action':'query','format':'json','redirects':1,'prop':'pageimages|info','inprop':'url','piprop':'thumbnail','pithumbsize':720,'titles':title})
    r=fetch(url)
    if not r['ok']: return None
    try:
        pages=json.loads(r['body'])['query']['pages']
        for p in pages.values():
            if p.get('thumbnail'):
                kind='Reference photograph or illustration'
                if e['name'] in ('Kel-Tec KSG-25','Metal Storm Redback','Atchisson Assault Shotgun'): continue
                return image_file(e,p['thumbnail']['source'],kind,p.get('fullurl',url))
    except (ValueError,KeyError,TypeError): pass
    return None

def source_images(e):
    for source in sources_for(e):
        r=fetch(source)
        if not r['ok']: continue
        soup=BeautifulSoup(r['body'],'html.parser')
        title=soup.title.get_text(' ',strip=True) if soup.title else ''
        page_score=name_match(e['name'],title)
        candidates=[]
        for im in soup.find_all('img'):
            u=im.get('data-src') or im.get('src') or ''
            if not u or u.startswith('data:'): continue
            u=urljoin(source,u)
            desc=' '.join([im.get('alt',''),im.get('title',''),u])
            if re.search(r'logo|avatar|badge|flag|favicon|wordmark|social|userpic',desc,re.I): continue
            score=name_match(e['name'],desc)
            if im.find_parent(class_=re.compile(r'infobox|pi-image')) and page_score>=.6: score=max(score,.9)
            if score>=.6: candidates.append((score,u,'Weapon reference image',source))
        if page_score>=.8:
            og=soup.find('meta',property='og:image')
            if og and og.get('content') and not re.search(r'logo|wordmark|placeholder',og['content'],re.I):
                candidates.append((.7,og['content'],'Source-page reference image',source))
        for _,u,kind,src in sorted(candidates,key=lambda x:x[0],reverse=True)[:6]:
            image=image_file(e,u,kind,src)
            if image: return image
    return None

def youtube_candidates(e, query):
    url='https://www.youtube.com/results?'+urlencode({'search_query':query})
    r=fetch(url)
    if not r['ok']: return []
    m=re.search(r'(?:var\s+ytInitialData|window\["ytInitialData"\]|ytInitialData)\s*=\s*',r['body'])
    if not m: return []
    try: data,_=json.JSONDecoder().raw_decode(r['body'][m.end():])
    except ValueError: return []
    results=[]
    for obj in walk(data):
        vr=obj.get('videoRenderer')
        if not vr: continue
        title=txt(vr.get('title')); vid=vr.get('videoId',''); channel=txt(vr.get('ownerText'))
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}',vid): continue
        match=name_match(e['name'],title)
        if e['group']=='Historical': match=max(match,name_match(HISTORY_ALIASES.get(e['name'],e['name']),title))
        game_tokens=tokens(e['game'])
        game_overlap=len(game_tokens & set(norm(title+' '+channel).split()))
        threshold=.68 if len(tokens(e['name']))>=3 else 1.0
        if match<threshold: continue
        if e['group']!='Historical' and len(tokens(e['name']))<=1 and not game_overlap: continue
        if re.search(r'3d print|homemade|how to build|make a gun|airsoft|replica|roblox|fortnite',title,re.I) and not any(x in e['game'].lower() for x in ('roblox','fortnite')): continue
        duration=txt(vr.get('lengthText'))
        thumbs=vr.get('thumbnail',{}).get('thumbnails',[])
        results.append({'url':'https://www.youtube.com/watch?v='+vid,'id':vid,'title':title,'channel':channel,'duration':duration,'thumbnail':thumbs[-1]['url'] if thumbs else 'https://i.ytimg.com/vi/'+vid+'/hqdefault.jpg','score':match+min(game_overlap,3)*.2+(.15 if duration and ':' in duration and len(duration)>=4 else 0),'match':'Item title matched','evidence_url':url,'playback':'Metadata checked; full playback not independently reviewed'})
    return sorted({x['id']:x for x in results}.values(),key=lambda x:x['score'],reverse=True)

def resolve_video(e):
    old=e.get('video',''); vid=video_id(old)
    if vid and e.get('videoMatch') in ('Item matched','Chapter matched'):
        o=fetch('https://www.youtube.com/oembed?'+urlencode({'url':'https://www.youtube.com/watch?v='+vid,'format':'json'}))
        if o['ok']:
            try:
                d=json.loads(o['body'])
                return {'url':old,'id':vid,'title':d.get('title',e['name']),'channel':d.get('author_name',''),'thumbnail':d.get('thumbnail_url',''),'match':e['videoMatch'],'evidence_url':old,'playback':'Inherited item/chapter match; metadata rechecked; full playback not independently reviewed'}
            except ValueError: pass
    suffix=' historical firearm museum demonstration' if e['group']=='Historical' else ' '+e['game']+' weapon showcase'
    results=youtube_candidates(e,e['name']+suffix)
    if not results and e['group']=='Historical':
        alternate=HISTORY_ALIASES.get(e['name'],e['name'])
        results=youtube_candidates(e,alternate+' Forgotten Weapons')
    if not results and e['group']!='Historical':
        results=youtube_candidates(e,'"'+e['name']+'" '+e['game'])
    if results: return results[0]
    if old and ('youtube.com/watch' in old or 'youtu.be/' in old or '/videos/' in old):
        return {'url':old,'id':vid,'title':'Existing collection / context video','match':'Context only; item match unresolved','evidence_url':old,'playback':'Not independently reviewed','unresolved':True}
    return None

def resolve(e, previous, override):
    rec=dict(previous) if previous else {'id':e['id'],'name':e['name'],'game':e['game'],'group':e['group']}
    if override: e={**e,**override}
    try:
        image=rec.get('image'); video=rec.get('video')
        if image and not (ROOT/image['local']).exists(): image=None
        if not video or video.get('unresolved'): video=resolve_video(e)
        if not image:
            if e.get('image'): image=image_file(e,e['image'],'Catalog weapon reference image',e.get('source') or e['image'])
            if not image and e['group']=='Historical': image=wikipedia_image(e)
            if not image: image=source_images(e)
            if not image and video and not video.get('unresolved'):
                image=image_file(e,video.get('thumbnail',''),'Item-video preview (not a separate weapon photograph)',video['url'])
        rec.update(image=image,video=video)
    except Exception as exc:
        rec['error']=type(exc).__name__+': '+str(exc)[:200]
    rec['complete']=bool(rec.get('image') and rec.get('video') and not rec['video'].get('unresolved'))
    return rec

def ingest():
    gaming_path=ROOT/'gaming-source.json'
    if not gaming_path.exists():
        encoded=''.join((ROOT/f'source-payload-{i}.b64').read_text().strip() for i in range(1,5))
        raw=lzma.decompress(base64.b64decode(encoded,validate=True))
        assert hashlib.sha256(raw).hexdigest()==EXPECTED,'Source transfer hash mismatch'
        payload=json.loads(raw)
        records=[dict(zip(payload['fields'],r)) for r in payload['rows']]
        assert len(records)==538
        save(gaming_path,records)
    gaming=load(gaming_path,[])
    for e in gaming: e['group']='Gaming'
    existing={(norm(x['game']),norm(x['name'])) for x in gaming}
    for row in csv.DictReader((ROOT/'gaming-additions.tsv').open(encoding='utf-8'),delimiter='\t'):
        key=norm(row['game']),norm(row['name'])
        if key in existing: continue
        existing.add(key); row['id']='g-'+hashlib.sha256(('::'.join(key)).encode()).hexdigest()[:12]; row['group']='Gaming'; gaming.append(row)
    historical_path=ROOT/'historical-source.json'
    if not historical_path.exists():
        historical=[]; category=''
        for line in (DOCS/(PAGES[1]+'.md')).read_text(encoding='utf-8').splitlines():
            if line.startswith('## '): category=line[3:]
            if line.startswith('| **'):
                cells=[x.strip() for x in line.strip('|').split('|')]
                if len(cells)!=4: continue
                name=cells[0].strip('*')
                historical.append({'id':'h-'+hashlib.sha256(name.encode()).hexdigest()[:12],'name':name,'game':category,'group':'Historical','hook':cells[2],'remix':cells[3]})
        assert len(historical)==152,len(historical)
        save(historical_path,historical)
    historical=load(historical_path,[])
    assert len(historical)==152
    save(ROOT/'catalog.json',{'gaming':gaming,'historical':historical})
    return gaming,historical

def render(entries,media,title,other):
    groups=collections.defaultdict(list)
    for e in entries: groups[e['game']].append(e)
    complete=sum(media.get(e['id'],{}).get('complete',False) for e in entries)
    image_count=sum(bool(media.get(e['id'],{}).get('image')) for e in entries)
    video_count=sum(bool(media.get(e['id'],{}).get('video')) and not media[e['id']]['video'].get('unresolved') for e in entries)
    lines=['# '+title,'',f'**{len(entries):,} references | {len(groups)} collections | {image_count} embedded images | {video_count} primary item/chapter-matched direct videos**','',f'[Other inspiration collection]({other}) | [Ascension Armory](Weapon-Overhaul) | [Weapon reference library](Weapon-Reference-Library)','',
    'A visual reference library for original Advent of Ascension designs. **Reference behavior** describes the source idea; **AoA remix** is a proposal, not shipped content. Click an image or the video link to open its direct showcase. Video titles and inherited chapter matches are recorded separately from watching the full footage. An item-video preview is labeled as such rather than passed off as a standalone weapon photograph.','',
    'Images are reference material attributed through their source links, not a collection of reusable game assets. This page studies silhouettes, animation, fictional effects and playful design; it does not provide real-world weapon construction instructions.','']
    if complete<len(entries): lines += [f'> **Media work still open: {len(entries)-complete} entries.** Missing or context-only media is explicitly marked below; no search-result link is counted as an embedded image or verified item video.','']
    lines += ['## Browse by collection','', ' | '.join(f'[{text(g)} ({len(v)})](#{slug(g)})' for g,v in sorted(groups.items())),'']
    for group,items in sorted(groups.items()):
        lines += [f'## {group}','', '| Embedded reference | Weapon and distinctive hook | AoA remix proposal | Direct video and source |','|---|---|---|---|']
        for e in items:
            m=media.get(e['id'],{}); im=m.get('image'); v=m.get('video')
            if im:
                image_url=RAW+Path(im['local']).name
                link=v['url'] if v else im['source']
                cell=f'<a href="{html.escape(link,quote=True)}"><img src="{image_url}" width="220" alt="{text(e["name"])}"></a>'
                if 'preview' in im['kind'].lower(): cell+='<br><sub>Item-video preview</sub>'
            else: cell='Image not yet resolved'
            links=[]
            if v: links.append(f'[Watch video]({v["url"]})<br><sub>{text(v["match"])}</sub>')
            else: links.append('Direct video not yet resolved')
            source=(im or {}).get('source') or e.get('source')
            if source: links.append(f'[Image / reference source]({source})')
            lines.append(f'| {cell} | **{text(e["name"])}**<br>{text(e.get("hook"))} | {text(e.get("remix"))} | '+ '<br>'.join(links)+' |')
        lines += ['','[Back to collections](#browse-by-collection)','']
    lines += ['## End of gallery','',f'All {len(entries)} catalog records are included. [Machine-readable sources and media evidence](https://github.com/{REPO}/tree/main/docs/weapon-inspirations). Media matching is not gameplay implementation or a claim that every video was watched.','']
    return '\n'.join(lines)

def publish(wiki):
    wiki=Path(wiki)
    for page in PAGES:
        source=DOCS/(page+'.md');assert source.exists();shutil.copyfile(source,wiki/source.name)
    import importlib.util
    _nav_path=Path(__file__).resolve().parent.parent/'weapon_inspiration_navigation.py'
    if not _nav_path.exists():
        import subprocess
        _source=subprocess.run(['git','show','HEAD:docs/weapon_inspiration_navigation.py'],cwd=_nav_path.parent.parent,check=True,capture_output=True).stdout
        _nav_path.write_bytes(_source)
    _nav_spec=importlib.util.spec_from_file_location('weapon_nav_shared',_nav_path)
    _nav=importlib.util.module_from_spec(_nav_spec);_nav_spec.loader.exec_module(_nav)
    _nav.apply(wiki)
    print('Prepared galleries with shared navigation',flush=True)



def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--publish-only'); args=parser.parse_args()
    if args.publish_only: publish(args.publish_only); return
    gaming,historical=ingest(); all_entries=historical+gaming
    assert len({x['id'] for x in all_entries})==len(all_entries)
    media=load(ROOT/'media.json',{}); overrides={}
    for path in ROOT.glob('*-overrides.json'): overrides.update(load(path,{}))
    todo=[e for e in all_entries if not media.get(e['id'],{}).get('complete') or e['id'] in overrides]
    print(f'Catalog: {len(gaming)} gaming + {len(historical)} historical. Resolving {len(todo)} media records.',flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        jobs={pool.submit(resolve,e,media.get(e['id']),overrides.get(e['id'])):e for e in todo}
        for i,f in enumerate(concurrent.futures.as_completed(jobs),1):
            e=jobs[f]; media[e['id']]=f.result()
            if i%20==0 or i==len(todo):
                save(ROOT/'media.json',media)
                print(f'Resolved {i}/{len(todo)}; complete {sum(x.get("complete",False) for x in media.values())}',flush=True)
    report={'gaming':len(gaming),'historical':len(historical),'total':len(all_entries),'game_collections':len({x['game'] for x in gaming}),'embedded_images':sum(bool(media[e['id']].get('image')) for e in all_entries),'matched_videos':sum(bool(media[e['id']].get('video')) and not media[e['id']]['video'].get('unresolved') for e in all_entries),'complete':sum(media[e['id']]['complete'] for e in all_entries),'unresolved':[{'id':e['id'],'name':e['name'],'game':e['game'],'image':bool(media[e['id']].get('image')),'video':media[e['id']].get('video',{}),'error':media[e['id']].get('error')} for e in all_entries if not media[e['id']]['complete']]}
    save(ROOT/'coverage.json',report)
    for entries,page,title,other in ((gaming,PAGES[0],'Video-game weapon inspirations',PAGES[1]),(historical,PAGES[1],'Historical and experimental gun inspirations',PAGES[0])):
        body=render(entries,media,title,other)
        assert body.count('**<br>') == len(entries)
        assert body.count('width="220"')==sum(bool(media[e['id']].get('image')) for e in entries)
        assert '## End of gallery' in body
        (DOCS/(page+'.md')).write_text(body,encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='unresolved'}),flush=True)

if __name__=='__main__': main()
