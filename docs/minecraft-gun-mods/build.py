#!/usr/bin/env python3
"""Build the source-backed explorer, category Wiki and reproducible acceptance evidence."""
from __future__ import annotations
import base64,collections,copy,hashlib,html,json,lzma,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlparse,quote
from PIL import Image
ROOT=Path(__file__).resolve().parent
DOCS=ROOT.parent
REPO='Herbertofury/Advent-of-Ascension'
WIKI='https://github.com/'+REPO+'/wiki/'
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
RAW='https://raw.githubusercontent.com/'+REPO+'/main/docs/minecraft-gun-mods/'
BUNDLE_HASH='2614a599fe92b16425624ee71f0480d6e162cb9d96305d88ffb5f57cf813b9fd'

def save(path,value):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
def md(s):
 value=html.escape(str(s or '')).replace('|','&#124;').replace('\n',' ')
 for ch in '*_`[]~':value=value.replace(ch,'&#'+str(ord(ch))+';')
 return value
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def decode_ui():
 raw=lzma.decompress(base64.b64decode(''.join((ROOT/f'ui-source-{i}.b64').read_text().strip() for i in (1,2)),validate=True))
 assert hashlib.sha256(raw).hexdigest()==BUNDLE_HASH,'Source bundle failed its transport checksum'
 files=json.loads(raw);assert set(files)=={'index.html','app.css','app.js','qa/browser_test.py'}
 for name,body in files.items():
  p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body,encoding='utf-8')
 subprocess.run(['node','--check',str(ROOT/'app.js')],check=True)

def validate(data):
 items=data['items'];ids=[x['id'] for x in items];assert len(ids)==len(set(ids));assert len(items)>200,'Unexpected incomplete catalog'
 assert data['catalogId']=='aoa-minecraft-gun-mod-inspirations'
 errors=[];hashes={};release_pairs=0
 for x in items:
  for field in ('name','id','type','edition','projectUrl'):assert x.get(field),(x['id'],field)
  for url in [x['projectUrl']]+[a['url'] for a in x['links']]+[a['url'] for a in x['videos']]+[a['url'] for a in x['releases']]:
   if urlparse(url).scheme not in ('http','https'):errors.append([x['id'],'unsafe URL',url])
  for rel in x['releases']:
   assert isinstance(rel['versions'],list) and isinstance(rel['loaders'],list),(x['id'],'release lists')
   release_pairs+=len(rel['versions'])*max(1,len(rel['loaders']))
  for media in x.get('media',[]):
   p=ROOT/media['src']
   if not p.exists():errors.append([x['id'],'missing image',str(p)]);continue
   digest=hashlib.sha256(p.read_bytes()).hexdigest()
   if digest!=media['sha256']:errors.append([x['id'],'image hash mismatch',media['src']])
   if digest not in hashes:
    with Image.open(p) as image:image.verify()
    hashes[digest]=media['src']
 assert not errors,errors[:20]
 evidence={'projectCount':len(items),'uniqueIds':len(set(ids)),'projectsWithMedia':sum(bool(x.get('media')) for x in items),'distinctImageHashes':len(hashes),'projectsWithDirectVideos':sum(bool(x['videos']) for x in items),'releaseRecords':sum(len(x['releases']) for x in items),'recordedVersionLoaderPairs':release_pairs,'types':dict(collections.Counter(x['type'] for x in items)),'editions':dict(collections.Counter(x['edition'] for x in items)),'errors':errors,'nativeMinecraftRuntimeTested':False}
 save(ROOT/'qa'/'data-verification.json',evidence);return evidence

def card_row(x):
 media=next((a for a in x.get('media',[]) if a['role']!='Project icon'),next(iter(x.get('media',[])),None))
 if media:visual=f'<a href="{html.escape(x["projectUrl"],quote=True)}"><img src="{RAW+media["src"]}?v={media["sha256"][:8]}" width="190" alt="{md(x["name"])}"></a><br><sub>{md(media["role"])}</sub>'
 else:visual='No source image located'
 rel=x.get('latest');release='Exact file not established'
 if rel:release=f'[{md(rel["name"])}]({rel["url"]})<br>{md(rel["date"][:10])} · {md(rel["channel"])}<br>{md(", ".join(rel["versions"]))}<br>{md(", ".join(rel["loaders"])) or "Loader not specified"}'
 link=f'[Open project]({x["projectUrl"]}) · [Explore]({SITE}?item={quote(x["id"])})'
 if x['videos']:link+=f'<br>[Creator-linked video]({x["videos"][0]["url"]})'
 source=f'[Evidence]({WIKI}Minecraft-Gun-Mod-Inspirations-Sources#ref-{x["id"]})'
 idea=x.get('inspiration',['Inspect the creator reference.'])[0]
 return f'| {visual} | **{md(x["name"])}**<br>{md(x["summary"])}<br><sub>{md(x["ecosystem"])} · {md(x["curation"])}</sub> | {release} | {md(idea)}<br>{link}<br>{source} |'

def make_wiki(data,proof):
 items=data['items'];groups=collections.defaultdict(list)
 for x in items:groups[x['type']].append(x)
 pages={};index=[]
 for group,values in sorted(groups.items()):
  batches=[];batch=[];size=0
  for x in values:
   row=card_row(x);length=len(row.encode())
   if size+length>310000 and batch:batches.append(batch);batch=[];size=0
   batch.append((x,row));size+=length
  if batch:batches.append(batch)
  for n,batch in enumerate(batches,1):
   name='Minecraft-Gun-Mod-Inspirations-'+slug(group)+(('-'+str(n)) if len(batches)>1 else '')
   title=group+(f' · {n}/{len(batches)}' if len(batches)>1 else '')
   lines=['# '+title,'',f'**{len(batch)} projects · source metadata checked {data["checkedDate"]}**','',f'[Main research index](Minecraft-Gun-Mod-Inspirations) · [Interactive explorer]({SITE}?type={quote(group)}) · [Weapon inspirations](Weapon-Inspirations)','',
    'Images are creator project logos, screenshots or description artwork, labeled individually. A project page update is not necessarily a new mod release. The release column shows one exact latest file; use the explorer to inspect other version/loader combinations. A pack, integration or unofficial port is not a standalone engine.','',
    '| Embedded source image | Project and study category | Latest exact file evidence | AoA study proposal and links |','|---|---|---|---|']
   lines += [row for x,row in batch]
   lines += ['',f'## End of gallery','',f'All {len(batch)} projects on this page are included. [Browse the complete catalog]({SITE}). Source verification does not establish native Minecraft compatibility or performance.','']
   body='\n'.join(lines);assert len(body.encode())<490000
   pages[name]=body;index.append({'title':title,'page':name,'count':len(batch),'ids':[x['id'] for x,row in batch]})
 prior=[x for x in items if x.get('earlierPick')];anchors=[x for x in items if x['curation']=='Study anchor']
 lines=['# Minecraft gun mod inspirations','',f'**{len(items):,} distinct project records · {len(prior)} earlier picks recovered · checked {data["checkedDate"]}**','',f'## [Open the Minecraft Gun Atlas]({SITE})','',
 'Explore the entire catalog with instant search, exact release-version/loader filters, ecosystem and visual-style filters, favorites, private notes, comparison, saved views, image galleries and portable collection backups. Favorites stay in your browser, not in a hidden account.','',
 '[Weapon Inspirations](Weapon-Inspirations) · [Ascension Armory](Weapon-Overhaul) · [Original weapon reference library](Weapon-Reference-Library)','',
 '## Start with strong study references','',
 'These are editorial study selections, not an FPS ranking or a claim that every project has been installed and tested. Earlier picks are kept separate from your new personal favorites.','',
 '| Reference | Kind / ecosystem | Why study it for AoA? |','|---|---|---|']
 for x in prior+anchors:
  lines.append(f'| [{md(x["name"])}]({SITE}?item={quote(x["id"])}) | {md(x["type"])} · {md(x["ecosystem"])} | {md(" ".join(x["inspiration"]))} |')
 lines += ['','## Complete illustrated collections','','| Collection | Projects |','|---|---:|']
 for x in index:lines.append(f'| [{md(x["title"])}]({x["page"]}) | {x["count"]} |')
 lines += ['','## Current releases, older inspiration and compatibility','',
 '- **Latest file, not latest page edit.** The explorer distinguishes release dates from project update dates and separates stable files from alpha/beta files.',
 '- **Version + loader must coexist on a release record.** A project supporting Forge 1.20.1 and NeoForge 1.21.1 does not thereby support Forge 1.21.1.',
 '- **Keep ecosystem roles distinct.** TaCZ/Point Blank packs, handling integrations, Bedrock behavior/resource packs and legacy engines are labeled rather than mixed together as interchangeable mods.',
 '- **Unofficial forks remain separate.** Confirm the exact author, dependencies and file instructions before installing or studying source.',
 '- **Study proposal versus implementation.** AoA adaptation notes are original proposals. None of these references has been silently added as an AoA dependency.','',
 '## Research coverage and evidence','',f'{data["coverage"]["sourceRecordsAccepted"]:,} accepted source records were reconciled across providers into {len(items):,} project identities. {proof["projectsWithMedia"]:,} have archived source images and {proof["projectsWithDirectVideos"]:,} have direct videos linked by their creators. Missing media is not replaced with a fabricated image or a search-results link.','',
 'The search includes Java mods, gunpacks, resource packs, datapacks, firearm-specific support and Bedrock add-ons. Public Modrinth query pagination and CurseForge query pagination are recorded in the coverage ledger. This is a broad finite research snapshot, not a provable census of every private, unlisted or newly uploaded project.','',
 f'[Source and release evidence](Minecraft-Gun-Mod-Inspirations-Sources) · [Machine-readable catalog]({SITE}catalog.json) · [Research ledgers](https://github.com/{REPO}/tree/main/docs/minecraft-gun-mods)','',
 '## Preservation','',
 'The earlier Gun Vault spreadsheet was used as a read-only discovery source. Duplicate URLs and search hubs are recorded separately, not counted as new mods. Existing weapon-history and video-game galleries remain unchanged.','',
 '## End of research index','']
 pages['Minecraft-Gun-Mod-Inspirations']='\n'.join(lines)
 # Compact per-item provenance fits in bounded source volumes.
 source_batches=[];current=[];size=0
 for x in items:
  block=f'<a id="ref-{x["id"]}"></a>\n### {x["name"]}\n\n[{x["provider"]} project]({x["projectUrl"]}) · Checked {x["checkedAt"][:10]}. Type: {x["type"]}.\n\n'
  block+=' '.join(f'[{md(a["label"])}]({a["url"]})' for a in x['links'])+'\n\n'
  for media in x.get('media',[]):block+=f'- {media["role"]}: [exact image]({media["url"]}) · [creator source]({media["sourceUrl"]}). SHA-256 `{media["sha256"]}`.\n'
  for video in x['videos']:block+=f'- [Video]({video["url"]}) · {video["verification"]}.\n'
  block+='\n'+md(x['evidence']['releaseScope'])+'\n\n'
  if size+len(block.encode())>350000 and current:source_batches.append(current);current=[];size=0
  current.append((x['id'],block));size+=len(block.encode())
 if current:source_batches.append(current)
 source_map={}
 for n,batch in enumerate(source_batches,1):
  name='Minecraft-Gun-Mod-Inspirations-Sources'+('' if n==1 else '-'+str(n))
  body='# Minecraft gun project sources'+(f' · {n}/{len(source_batches)}' if len(source_batches)>1 else '')+'\n\n[Research index](Minecraft-Gun-Mod-Inspirations) · [Explorer]('+SITE+')\n\n'
  body+=' · '.join(f'[Volume {i}](Minecraft-Gun-Mod-Inspirations-Sources'+('' if i==1 else '-'+str(i))+')' for i in range(1,len(source_batches)+1))+'\n\n'
  body+=''.join(block for key,block in batch);pages[name]=body
  for key,block in batch:source_map[key]=name
 for name,body in list(pages.items()):
  if name.startswith('Minecraft-Gun-Mod-Inspirations-Sources'):continue
  for key,source in source_map.items():
   if source!='Minecraft-Gun-Mod-Inspirations-Sources':body=body.replace('Minecraft-Gun-Mod-Inspirations-Sources#ref-'+key,source+'#ref-'+key)
  pages[name]=body
 for name,body in pages.items():(DOCS/(name+'.md')).write_text(body,encoding='utf-8')
 save(ROOT/'wiki-manifest.json',{'main':'Minecraft-Gun-Mod-Inspirations','pages':[{'name':name,'bytes':len(body.encode()),'sha256':hashlib.sha256(body.encode()).hexdigest()} for name,body in pages.items()],'collections':index,'projectCount':len(items)})
 return pages

def hub_block():
 return '<!-- minecraft-gun-inspirations:start -->\n### Minecraft gun mod inspirations\n\n- [Minecraft Gun Atlas: searchable explorer, filters and favorites]('+SITE+')\n- [Minecraft gun mod inspirations: illustrated research and exact release evidence](Minecraft-Gun-Mod-Inspirations)\n<!-- minecraft-gun-inspirations:end -->'

def managed(body,block,start='<!-- minecraft-gun-inspirations:start -->',end='<!-- minecraft-gun-inspirations:end -->'):
 if start in body and end in body:
  a=body.index(start);b=body.index(end,a)+len(end);return body[:a]+block+body[b:]
 return body.rstrip()+'\n\n'+block+'\n'

def publish(wiki_path):
    wiki=Path(wiki_path);manifest=json.loads((ROOT/'wiki-manifest.json').read_text())
    for page in manifest['pages']:
        name=page['name']+'.md';(wiki/name).write_bytes((DOCS/name).read_bytes())
    extra=DOCS/'Minecraft-Gunpack-Creator-Discoveries.md'
    if extra.exists():(wiki/extra.name).write_bytes(extra.read_bytes())
    import importlib.util
    _nav_path=Path(__file__).resolve().parent.parent/'weapon_inspiration_navigation.py'
    if not _nav_path.exists():
        import subprocess
        _source=subprocess.run(['git','show','HEAD:docs/weapon_inspiration_navigation.py'],cwd=_nav_path.parent.parent,check=True,capture_output=True).stdout
        _nav_path.write_bytes(_source)
    _nav_spec=importlib.util.spec_from_file_location('weapon_nav_shared',_nav_path)
    _nav=importlib.util.module_from_spec(_nav_spec);_nav_spec.loader.exec_module(_nav)
    _nav.apply(wiki)
    for name in ('Weapon-Inspirations.md','Weapon-Reference-Library.md','Minecraft-Gun-Mod-Inspirations.md'):
        if (wiki/name).exists():(DOCS/name).write_bytes((wiki/name).read_bytes())
    print('Published one canonical Weapon Inspirations hierarchy',flush=True)



def build():
 decode_ui();data=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'));proof=validate(data)
 (ROOT/'catalog.js').write_text('window.GUN_ATLAS='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
 assert 'QA-NOT-PRODUCTION' not in (ROOT/'catalog.js').read_text()
 make_wiki(data,proof)
 (ROOT/'README.md').write_text('# Minecraft Gun Atlas\n\nOpen `index.html` beside `catalog.js`, `app.css`, `app.js` and the `assets` directory. The app works as a static GitHub Pages site and as an offline folder. No build service or account is required.\n\nFavorites, notes and saved views are stored in this browser. Export a collection backup before moving devices. Import merges data and preserves unavailable project IDs. It does not write to the original spreadsheet.\n\n## Reproducibility\n\n`research.py` records source discovery; `collect.py` resolves project/release/media metadata; `catalog.json` is the canonical snapshot; `build.py` builds the portable explorer and Wiki pages; `qa/browser_test.py` exercises the real app. The four original UI source files are transported in a two-part checksum-verified bundle and are committed as normal source files after decoding.\n\nSource timestamps are evidence freshness, not a compatibility guarantee. No Minecraft mod binaries are downloaded, installed or executed by this research pipeline. Creator media is attributed per project and is reference material, not redistributed mod assets.\n',encoding='utf-8')
 print(json.dumps(proof,indent=2),flush=True)
 # creator_delta_refresh: preserve canonical creator discoveries on rebuild
 import importlib.util as _iu
 _delta=ROOT/'creator-discoveries/build_update.py'
 if _delta.exists():
  _spec=_iu.spec_from_file_location('creator_delta_update',_delta);_module=_iu.module_from_spec(_spec);_spec.loader.exec_module(_module);_module.refresh()

if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='--publish':publish(sys.argv[2])
 else:build()
