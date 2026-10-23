#!/usr/bin/env python3
"""Derive a gun-only TaCZ page from the canonical atlas plus source metric evidence."""
from __future__ import annotations
import copy,hashlib,html,json,re,sys,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/tacz/'
RAW='https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minecraft-gun-mods/'
SHORTLIST={
'cf-1084662':'Animation-focused modern guns and a separate ZIP edition. Compare the creator trailer, mesh requirements and exact release branch.',
'cf-1254350':'Detailed tactical firearm presentation with creator recoil footage. Read the source-specific texture and reticle notes before installing.',
'cf-1411291':'Ready or Not-inspired firearms with 56 guns declared in the creator description. The JAR and ZIP are editions of one pack, not two recommendations.',
'cf-1062174':'Custom models, revised animations and a varied roster including a Ray Gun. A strong starting point for distinctive firearm presentation.',
'cf-1528455':'An explicit Escape from Tarkov animation-style reference with additional weapons, not merely a replacement sound or animation pack.',
'cf-1515069':'Modular tactical gun designs with creator galleries. Inspect the actual stable file separately from its newer beta.',
'cf-1092101':'Koei\'s Create-inspired gun designs: a strong reference for mechanically readable Minecraft-styled firearms.',
'cf-1081193':'Koei\'s Immersive Engineering-inspired gunpack: industrial materials and recognizable firearm geometry.',
'cf-1317400':'Koei\'s Ars Nouveau-inspired magical firearms. Kept distinct from ArsArms, which adds spell integration rather than this gun roster.',
'cf-1187336':'Koei\'s Cyberpunk-inspired firearms: futuristic silhouettes that still work as first-person gun designs.',
'cf-1111441':'Koei\'s Applied Energistics-inspired guns: energy technology and cohesive materials rather than a generic military reskin.',
'cf-1031166':'Koei\'s Taran Tactical-inspired gunpack, retained from the earlier selections.',
'cf-1031134':'Koei\'s Helldivers 2 gunpack, useful for exaggerated sci-fi gun shapes and recognizable weapon roles.',
'cf-1038650':'Electromagnetic weapons with a Mekanism-inspired visual identity. Strong contrast to conventional rifle packs.',
'cf-1287059':'Near-future modern firearms with a cohesive creator-authored aesthetic.',
'cf-1177140':'Original energy-weapon designs. Good reference for AoA blasters with a clearer physical mechanism.',
'cf-1196617':'A large Warzone-inspired weapon collection; use its direct footage and exact file evidence instead of equating breadth with quality.',
'cf-1352297':'Unusual and historically obscure firearms, useful when ordinary AK/AR variants are not enough.',
'cf-1079856':'Historical gun experimentation and Great War designs with a distinct reload and action vocabulary.',
'cf-1115000':'Deep Rock Galactic-inspired firearms and unconventional sci-fi silhouettes.',
'cf-1389008':'Cataclysm-boss-inspired gun designs, particularly relevant to original AoA realm-themed weapons.',
'cf-1668635':'One highly specific gun with creator-declared custom model, textures, animations and handling sounds.',
'cf-1746570':'Modern-style firearms plus attachments. Check the exact pack dependencies rather than assuming TaCZ alone is sufficient.'}

SHORTLIST.update({
 'cf-1075478':'Charge into Battle: Reboot adds a substantial source-described weapon collection; inspect its explicit TaCZ and melee-support requirements.',
 'cf-1630118':'Original fictional firearm designs with creator-described PBR textures and mesh models. TaCZ Mesh Loader is an explicit dependency.',
 'cf-1202657':'Wolfenstein-inspired guns with weapon-specific attachments. Useful for distinctive alternate-history gun silhouettes.',
 'cf-1067950':'Historical and original guns spanning the line-infantry era to the Cold War; a strong reference for less-common actions and proportions.',
 'cf-1106036':'A focused creator-authored firearm collection rather than a utility bundle. Compare its individual gun models and handling in the source gallery.',
 'cf-1738298':'Custom Killzone gun models and animations with a clearly disclosed work-in-progress status. Two guns currently lack inspect animations.',
 'cf-1427153':'Gundam-inspired firearms with creator-described custom models and animations; especially useful for oversized sci-fi silhouettes.',
 'cf-1089328':'A single ALOFS-equipped break-action shotgun, selected for its unusual visible feed mechanism rather than roster size.',
 'cf-1336260':'Earth Defense Force-inspired firearms. The creator explicitly warns about a loud close-range sound bug; read that warning before use.'
})

def load(path):return json.loads(path.read_text(encoding='utf-8'))
def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def norm(s):return re.sub(r'[^a-z0-9]','',str(s).lower())
def md(s):
 t=html.escape(str(s or '')).replace('|','&#124;').replace('\n',' ')
 for ch in '*_`[]~':t=t.replace(ch,'&#'+str(ord(ch))+';')
 return t

def data_build():
 base=load(PARENT/'catalog.json');selection=load(ROOT/'selection.json');research=load(ROOT/'research.json')
 idx={x['id']:copy.deepcopy(x) for x in base['items']};snap={x['id']:x for x in research['snapshots'] if x.get('id') and not x.get('error')}
 # Previously unseen discoveries enter only after explicit creator-content review.
 for x in selection.get('extraRecords',[]):idx[x['id']]=copy.deepcopy(x)
 if (ROOT/'additional-records.json').exists():
  extra=load(ROOT/'additional-records.json')
  for x in extra:idx[x['id']]=copy.deepcopy(x)
  selection['acceptedIds']=list(dict.fromkeys(selection['acceptedIds']+[x['id'] for x in extra]))
 records={};unresolved=[]
 for id in selection['acceptedIds']:
  x=idx[id];ids=[id]+['cf-'+str(x['providerIds']['curseforge'])] if x['providerIds'].get('curseforge') else [id]
  if x['providerIds'].get('modrinth'):ids.append('mr-'+x['providerIds']['modrinth'])
  facts=[snap[k] for k in dict.fromkeys(ids) if k in snap]
  if not facts:unresolved.append(id)
  x['metricSources']=[{k:s.get(k) for k in ('id','provider','url','downloads','favorites','followers','rating','ratingCount','checkedAt','sourceHash')} for s in facts]
  x['contentSources']=[{'url':s['url'],'summary':s['summary'],'features':s.get('featureClaims',{}),'checkedAt':s['checkedAt']} for s in facts]
  x['variants']=[{'id':id,'name':x['name'],'url':x['projectUrl']}]
  x['aliases']=list(x.get('aliases',[]));x['familyIds']=[id]
  rels={v['id']:v for v in x.get('releases',[])}
  for s in facts:
   for v in s.get('releases',[]):rels[v['id']]=v
  x['releases']=sorted(rels.values(),key=lambda v:v['date'],reverse=True)
  x['maintenance']=x.get('maintenanceNotice') or ('Discontinued by creator' if any(s.get('maintenance')=='Discontinued by creator' for s in facts) else 'No discontinuation notice found')
  x['historicalDownloadsMixed']=any(s.get('historicalDownloadsMixed') for s in facts)
  x['checkedAt']=max([s['checkedAt'] for s in facts]+[x['checkedAt']]);records[id]=x
 selection['mergeProofs'] += [
  {'primary':'cf-1459599','aliases':['mr-RAIYwXWx'],'proof':'Exact same Cinder title, TCinder creator credit, description and matching artwork on both provider pages.'},
  {'primary':'cf-1671643','aliases':['mr-f6HDPJO8'],'proof':'Same CS2 to MC title, weapon roster and three identical decoded source-gallery images. Credited handles differ; source credits remain separately visible. Counts are not summed.'}]
 for proof in selection['mergeProofs']:
  target=records[proof['primary']];target['identityProof']=proof['proof']
  for id in proof['aliases']:
   if id not in records:continue
   other=records.pop(id)
   target['familyIds']+=other['familyIds'];target['aliases']=list(dict.fromkeys(target['aliases']+[id]+other['aliases']))
   for field,key in [('metricSources','id'),('contentSources','url'),('variants','id'),('links','url'),('media','sha256'),('videos','url'),('releases','id')]:
    target[field]=list({a[key]:a for a in target.get(field,[])+other.get(field,[])}.values())
   target['versions']=sorted(set(target['versions']+other['versions']));target['loaders']=sorted(set(target['loaders']+other['loaders']))
   target['releases'].sort(key=lambda v:v['date'],reverse=True)
 items=list(records.values())
 for x in items:
  def maximum(field,provider=None):
   vs=[s[field] for s in x['metricSources'] if isinstance(s.get(field),(int,float)) and (not provider or s['provider']==provider)]
   return max(vs) if vs else None
  x['metrics']={'downloads':maximum('downloads'),'cfDownloads':maximum('downloads','CurseForge'),'mrDownloads':maximum('downloads','Modrinth'),'favorites':maximum('favorites','CurseForge'),'followers':maximum('followers','Modrinth'),'communityRating':None}
  x['downloads']=x['metrics']['downloads'] if x['metrics']['downloads'] is not None else x['downloads']
  x['metrics']['downloadSource']=next((s['provider'] for s in x['metricSources'] if s.get('downloads')==x['metrics']['downloads']),None)
  x['metricFreshness']='Current source read' if x['metricSources'] else 'Current refresh unresolved; prior snapshot only'
  x['activity']='Legacy / discontinued' if x['maintenance']=='Discontinued by creator' else 'Creator paused updates' if x['maintenance']=='Paused by creator' else 'Current / no discontinuation notice'
  x['curation']='Quality shortlist' if x['id'] in SHORTLIST else 'Research discovery';x['studyPriority']=100 if x['id'] in SHORTLIST else 50
  x['qualityReason']=SHORTLIST.get(x['id'],'Creator-confirmed gun content. Inspect its source gallery and footage before deciding whether the presentation meets your standard.')
  x['inspiration']=[x['qualityReason']]+x.get('inspiration',[])
  x['type']='JAR + ZIP editions' if len(x['variants'])>1 and any('zip' in v['name'].lower() or '/customization/' in v['url'] for v in x['variants']) else 'Gun-adding add-on (JAR)' if '/mc-mods/' in x['projectUrl'] or '/mod/' in x['projectUrl'] else 'Gunpack (ZIP)'
  x['latest']=x['releases'][0] if x['releases'] else None;x['latestStable']=next((v for v in x['releases'] if v['channel']=='release'),None)
  x['descriptionExcerpt']=' '.join(x.get('descriptionExcerpt','').split()[:85])
  for m in x['media']:
   if not m['src'].startswith(('../','assets/')):raise ValueError(m['src'])
   if m['src'].startswith('assets/'):m['src']='../'+m['src']
  x['qualitySignals']=[]
  if any('animation' in s.get('features',{}) for s in x['contentSources']):x['qualitySignals'].append('Creator-described animation work')
  if any('models' in s.get('features',{}) for s in x['contentSources']):x['qualitySignals'].append('Creator-described model/texture work')
  if any(m['role']!='Project icon' for m in x['media']):x['qualitySignals'].append('Creator imagery available')
  if x['videos']:x['qualitySignals'].append('Creator-linked footage')
  x['cautions']=[v for v in x.get('cautions',[]) if not v.startswith('Content pack, not')]
  x['cautions'].append('Requires the exact TaCZ runtime and any additional dependencies named by this pack; version support is not inferred from the base mod.')
  if x['historicalDownloadsMixed']:x['cautions'].append('Lifetime project downloads include pre-TaCZ releases. Popularity is not a TaCZ-only install count.')
  if x['maintenance']=='Discontinued by creator':x['cautions'].insert(0,'The creator states that this project is no longer maintained. It is retained as a clearly marked legacy gun-content reference, not a current-quality recommendation.')
  x['evidence']['releaseScope']='Existing exact release evidence plus current provider latest-file records. ZIP packs often do not specify a loader; no loader/version combination is invented.'
 review=load(ROOT/'media-review-overrides.json')
 for x in items:
  x['media']=[m for m in x['media'] if m['sha256'] not in review['excludedPromotionalImages']]
  preferred=review['preferred'].get(x['id'])
  if preferred:
   assert any(m['sha256']==preferred for m in x['media']), ('Missing reviewed image',x['id'])
   x['preferredMediaSha256']=preferred
  if x['id'] in ('cf-1459599','cf-1671643'):x['type']='Gunpack (ZIP)'
 items.sort(key=lambda x:(-(x['metrics']['downloads'] if x['metrics']['downloads'] is not None else -1),x['name'].lower()))
 for n,x in enumerate(items,1):x['popularityRank']=n
 out={'schemaVersion':2,'catalogId':'aoa-tacz-gunpacks','title':'TaCZ Gunpack Lab','checkedDate':research['checkedAt'][:10],'generatedAt':research['checkedAt'],'items':items,'idAliases':{id:x['id'] for x in items for id in x['aliases']},'sources':[{'provider':'Minecraft Gun Atlas','role':'Canonical parent snapshot','url':'https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/catalog.json','dataHash':base['build']['dataHash']},{'provider':'CurseForge and Modrinth','role':'Live project popularity and creator gun-content evidence'}],'rankingPolicy':selection['metricsPolicy'],'coverage':{'scope':selection['scope'],'publishedProjects':len(items),'crossProviderMerges':sum(len(p['aliases']) for p in selection['mergeProofs']),'mediaProjects':sum(bool(x['media']) for x in items),'directVideoProjects':sum(bool(x['videos']) for x in items),'sourceRefreshUnresolved':unresolved,'discovery':research['coverage'],'communityRatingsAvailable':0},'build':{'parentDataHash':base['build']['dataHash'],'dataHash':hashlib.sha256(json.dumps(items,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'generator':'build_tacz.py 1.0'}}
 save(ROOT/'catalog.json',out);(ROOT/'catalog.js').write_text('window.GUN_ATLAS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8');return out

def replace(s,old,new):
 assert old in s,('Template changed',old[:120])
 return s.replace(old,new)

def ui_build(data):
 page=(PARENT/'index.html').read_text(encoding='utf-8').replace('<a href="tacz/">TaCZ gunpacks</a>','')
 page=page.replace('Minecraft Gun Mod Inspirations | The Ascension Armory','TaCZ Gunpacks | The Ascension Armory')
 page=page.replace('A source-grounded Minecraft gun-mod inspiration atlas. Explore gun mods, content packs, magical firearms, artillery, Bedrock add-ons and legacy projects. Save favorites, compare releases and keep research notes.','TaCZ gunpacks that actually add guns. Compare real downloads, CurseForge favorites and Modrinth followers; save and privately rate your favorites.')
 page=page.replace('WEAPON INSPIRATIONS / MINECRAFT','WEAPON INSPIRATIONS / TACZ GUNPACKS')
 page=page.replace('Find your next<br><em>favorite arsenal.</em>','TaCZ.<br><em>More guns. Less noise.</em>')
 page=page.replace("A field guide to Minecraft's gun-making community. Explore the handling, craftsmanship and wonderfully strange ideas worth bringing into an original AoA design.",'Gunpacks and add-ons that actually add firearms. No ammo libraries, attachment-only packs or optimization clutter. Find beautifully built arsenals, then compare the real numbers.')
 page=page.replace('Explore study anchors','Explore the quality shortlist').replace('Revisit earlier picks','Your earlier gunpack picks').replace('ON THE STUDY DESK','GUNPACK SPOTLIGHT').replace('01 / MINECRAFT','02 / TACZ').replace('projects, not search links','distinct gunpack families').replace('standalone gun mods','with CurseForge favorites').replace('gun &amp; content packs','with Modrinth followers').replace('Make room for a little firepower.','Find a gunpack worth keeping.')
 page=page.replace(WIKI+'Minecraft-Gun-Mod-Inspirations',WIKI+'TaCZ-Gunpacks')
 page=page.replace('<nav aria-label="Main navigation">','<nav aria-label="Main navigation"><a href="../">All Minecraft mods</a>')
 page=page.replace('<div class="preset-row" aria-label="Quick filters">','<div class="ranking-bar" role="group" aria-label="Rank gunpacks"><button data-ranking="downloads">Most popular</button><button data-ranking="favorites">Most favorited</button><button data-ranking="followers">Most followed</button><button data-ranking="priority">Quality shortlist</button><button data-ranking="date">Latest releases</button><button data-ranking="rating">My ratings</button><button id="rankingHelp" class="text-button">How rankings work</button></div><p id="rankingNote" class="ranking-note" aria-live="polite"></p><div class="preset-row" aria-label="Quick filters">')
 page=page.replace('<button data-preset="modern">26.x releases</button>','<button data-preset="scifi">Sci-fi &amp; energy</button>').replace('<button data-preset="bedrock">Bedrock</button>','<button data-preset="historical">Historical guns</button>').replace('Legacy gems','Legacy / discontinued')
 page=re.sub(r'(<label>Edition<select.*?</select></label>)',r'<div hidden>\1</div>',page)
 page=re.sub(r'(<label>Ecosystem<select.*?</select></label>)',r'<div hidden>\1</div>',page)
 page=re.sub(r'<select id="sort">.*?</select>','<select id="sort"><option value="downloads">Most popular: largest site downloads</option><option value="favorites">Most favorited: CurseForge</option><option value="followers">Most followed: Modrinth</option><option value="cfDownloads">CurseForge downloads</option><option value="mrDownloads">Modrinth downloads</option><option value="priority">Quality shortlist first</option><option value="date">Newest release</option><option value="created">Newest project</option><option value="rating">My rating</option><option value="name">Name A to Z</option></select>',page,flags=re.S)
 page=page.replace('All projects','All gunpacks').replace('THE CATALOG','THE GUNPACK COLLECTION').replace('/ MINECRAFT RESEARCH','/ TACZ GUNPACK LAB')
 page=page.replace('Your favorites and notes stay in this browser.','Favorites, notes and your personal ratings stay in this browser. Rankings are popularity signals, not a performance benchmark.')
 (ROOT/'index.html').write_text(page,encoding='utf-8')
 js=(PARENT/'app.js').read_text(encoding='utf-8')
 js=replace(js,"sort:'priority'","sort:'downloads'")
 js=js.replace("x.curation!=='Study anchor'","x.curation!=='Quality shortlist'").replace("x.curation==='Study anchor'","x.curation==='Quality shortlist'")
 js=replace(js,"['priority','date','created','name','downloads']","['priority','date','created','name','downloads','favorites','followers','cfDownloads','mrDownloads','rating']")
 # Saved filters are page-specific, while favorites, notes and ratings share the canonical collection store.
 js=js.replace('preferences.views','preferences.taczViews').replace('value.views','value.taczViews')
 js=replace(js,"let favorites=new Set(preferences.favorites), compare=new Set(), state={...DEFAULTS};","preferences.ratings=preferences.ratings&&typeof preferences.ratings==='object'&&!Array.isArray(preferences.ratings)?preferences.ratings:{};\nlet favorites=new Set(preferences.favorites), compare=new Set(), state={...DEFAULTS};\nfor(const [alias,id] of Object.entries(DATA.idAliases||{}))if(favorites.has(alias))favorites.add(id);\nlet rankPositions=new Map();")
 js=replace(js,"return list.sort(order[state.sort]||order.priority);","Object.assign(order,{favorites:(a,b)=>metricCompare(a,b,'favorites'),followers:(a,b)=>metricCompare(a,b,'followers'),cfDownloads:(a,b)=>metricCompare(a,b,'cfDownloads'),mrDownloads:(a,b)=>metricCompare(a,b,'mrDownloads'),downloads:(a,b)=>metricCompare(a,b,'downloads'),rating:(a,b)=>(Number(preferences.ratings[b.id])||0)-(Number(preferences.ratings[a.id])||0)||metricCompare(a,b,'downloads')});return list.sort(order[state.sort]||order.priority);")
 js=replace(js,"shown=filterItems();","shown=filterItems();rankPositions=new Map(shown.map((x,i)=>[x.id,i+1]));updateRankingNote();")
 js=replace(js,'<div class="card-body"><div class="card-topline">','<div class="card-body">${rankingCard(x)}<div class="card-topline">')
 js=replace(js,'<p class="card-summary">${esc(x.summary)}</p>','<p class="card-summary">${esc(x.summary)}</p>${x.maintenance===\'Discontinued by creator\'?\'<p class="legacy-alert">Creator discontinued this pack</p>\':\'\'}<div class="quality-signals">${x.qualitySignals.map(v=>`<span>${esc(v)}</span>`).join(\'\')}</div>')
 js=replace(js,'<td>${shortNumber(x.downloads)}</td>','<td>${rankingCard(x)}</td>')
 js=replace(js,'>Downloads</th>','>Popularity evidence</th>')
 js=replace(js,'<h3>Your research notes</h3>','${metricDetails(x)}${ratingControl(x)}<h3>Your research notes</h3>')
 js=replace(js,"const rows=[['Edition'","const rows=[['Popularity evidence',x=>rankingCard(x)],['Your rating',x=>preferences.ratings[x.id]?esc(preferences.ratings[x.id])+' / 5 (private)':'Not rated'],['Edition'")
 js=replace(js,"ITEMS.filter(x=>x.type==='Standalone gun mod').length","ITEMS.filter(x=>Number.isFinite(x.metrics.favorites)).length")
 js=replace(js,"ITEMS.filter(x=>x.type==='Gun / content pack').length","ITEMS.filter(x=>Number.isFinite(x.metrics.followers)).length")
 js=js.replace("x.activity==='Older release / legacy reference'","x.activity==='Legacy / discontinued'")
 js=js.replace("state.activity='Older release / legacy reference'","state.activity='Legacy / discontinued'")
 js=replace(js,"if(name==='bedrock')state.edition='Bedrock';","if(name==='scifi')state.theme='Science fiction';if(name==='historical')state.theme='Historical / retro';")
 js=js.replace('No hidden load-more limit. Priority is editorial; download counts are not a quality or compatibility test.','No hidden load-more limit. Missing metrics sort last, not as zero. Quality shortlist is editorial; community star ratings are not published by these sources.')
 js=replace(js,"preferences.favorites=[...favorites];try{localStorage.setItem", "preferences.favorites=[...favorites];try{const latest=JSON.parse(localStorage.getItem(KEY)||'null');if(latest&&typeof latest==='object'){for(const id of latest.favorites||[])if(typeof id==='string'&&!MAP.has(id)&&!DATA.idAliases?.[id])favorites.add(id);preferences.favorites=[...favorites];preferences.notes={...(latest.notes||{}),...preferences.notes};preferences.ratings={...(latest.ratings||{}),...preferences.ratings};if(Array.isArray(latest.views))preferences.views=latest.views;}localStorage.setItem")
 js=replace(js,"favorites.has(id)?favorites.delete(id):favorites.add(id);","if(favorites.has(id)){favorites.delete(id);for(const alias of MAP.get(id).aliases||[])favorites.delete(alias);}else favorites.add(id);")
 js=replace(js,"const mapped=MAP.has(id)?id:urls.get(value.projectURLs?.[id])||id;","const mapped=DATA.idAliases?.[id]||(MAP.has(id)?id:urls.get(value.projectURLs?.[id])||id);")
 js=replace(js,'persist();renderSavedViews();render();toast(`Imported',"if(value.ratings&&typeof value.ratings==='object')for(const [id,n] of Object.entries(value.ratings)){if(['__proto__','constructor','prototype'].includes(id))continue;if(Number.isInteger(n)&&n>=0&&n<=5)preferences.ratings[DATA.idAliases?.[id]||id]=n;}persist();renderSavedViews();render();toast(`Imported")
 js=replace(js,"if(params.get('item'))openDetail(params.get('item'));","if(params.get('item'))openDetail(DATA.idAliases?.[params.get('item')]||params.get('item'));")
 js=js.replace(WIKI+'Minecraft-Gun-Mod-Inspirations',WIKI+'TaCZ-Gunpacks')
 js=js.replace('minecraft-gun-inspirations-filtered','tacz-gunpacks-filtered')
 js=replace(js,"const fields=['name'","const fields=['cfDownloads','cfFavorites','mrDownloads','mrFollowers','yourRating','name'")
 js=replace(js,'rows.map(x=>[x.name,','rows.map(x=>[x.metrics.cfDownloads,x.metrics.favorites,x.metrics.mrDownloads,x.metrics.followers,preferences.ratings[x.id]||\'\',x.name,')
 js=replace(js,"for(const x of ITEMS){x._search",(ROOT/'ranking.js').read_text(encoding='utf-8')+"\nfor(const x of ITEMS){x._search")
 # The methodology replaces the broader atlas provenance entry point but retains its original source dialog below.
 js=replace(js,"$('#sourcesButton').onclick=sources;","$('#sourcesButton').onclick=rankingHelp;")
 js=replace(js,'renderSavedViews();syncControls();render();',"$('#rankingHelp').onclick=rankingHelp;\ndocument.addEventListener('click',event=>{const b=event.target.closest('button');if(b?.dataset.ranking){state.sort=b.dataset.ranking;if(b.dataset.ranking==='priority')state.curation='anchors';else if(state.curation==='anchors')state.curation='';syncControls();render();}if(b?.dataset.rate){const id=b.dataset.rate,n=Number(b.dataset.value);if(!MAP.has(id)||!Number.isInteger(n)||n<0||n>5)return;preferences.ratings[id]=n;persist();const holder=b.closest('.personal-rating');holder.outerHTML=ratingControl(MAP.get(id));render();toast(n?'Your private rating was saved.':'Your rating was cleared.');}});\nrenderSavedViews();syncControls();render();")
 js=js.replace("function mediaFor(x){return (x.media||[]).find(m=>m.role!=='Project icon')||(x.media||[])[0];}","function mediaFor(x){return (x.media||[]).find(m=>m.sha256===x.preferredMediaSha256)||(x.media||[]).find(m=>m.role!=='Project icon')||(x.media||[])[0];}")
 js=js.replace("switch(t.key){case 'type':", "switch(t.key){case 'id':found=norm(x.id)===v||(x.aliases||[]).some(a=>norm(a)===v);break;case 'name':found=norm(x.name).includes(v);break;case 'type':")
 (ROOT/'app.js').write_text(js,encoding='utf-8')
 (ROOT/'app.css').write_text((PARENT/'app.css').read_text()+'\n'+(ROOT/'tacz.css').read_text(),encoding='utf-8')
 # Only a navigation link changes in the parent. Canonical data and parent persistence code stay byte-identical.
 parent=(PARENT/'index.html').read_text()
 if 'href="tacz/"' not in parent:parent=parent.replace('<nav aria-label="Main navigation">','<nav aria-label="Main navigation"><a href="tacz/">TaCZ gunpacks</a>');(PARENT/'index.html').write_text(parent,encoding='utf-8')

def wiki_build(data):
 def number(v):return f'{v:,}' if v is not None else 'Not published'
 lines=['# TaCZ gunpacks: real gun content, source-ranked','',f'**{len(data["items"])} distinct gunpack families | source metrics checked {data["checkedDate"]}**','',f'## [Open the dedicated TaCZ Gunpack Lab]({SITE})','', '[Weapon Inspirations](Weapon-Inspirations) / [Minecraft Gun Mod Inspirations](Minecraft-Gun-Mod-Inspirations) / **TaCZ Gunpacks**','',
 'Browse gunpacks and gun-adding add-ons, with pictures, exact source downloads, CurseForge favorites, Modrinth followers, direct creator videos when available, favorites, personal ratings and comparison. Utilities, attachment-only packs, ammo libraries, skins, mob AI, recipes and the base TaCZ runtime are not padded into this list.','',
 '## Rankings that mean what they say','',
 '**Most popular:** largest verified single-site download count per pack family. JAR/ZIP editions and provider mirrors are not added together. **Most favorited:** CurseForge `favoriteCount`. **Most followed:** Modrinth `followers`. These are different signals and have separate rankings. Missing values stay unknown, not zero.','',
 '**Quality shortlist:** an editorial selection for presentation and design study, not a numerical review score or a guarantee that a pack runs well in your instance. **My rating:** your own browser-local 1–5 score. The fetched official source data does not provide a trustworthy community star rating, so no community stars are invented.','',
 '**Compatibility:** versions and loaders are tied to exact files. A gunpack ZIP does not inherit every loader/version of the TaCZ engine. The creator-discontinued LesRaisins Append Pack is marked as legacy, and its lifetime download count includes older TaC releases.','',
 '## Quality shortlist','', '| Pack | Why it is on the shortlist |','|---|---|']
 for x in data['items']:
  if x['id'] in SHORTLIST:lines.append(f'| [{md(x["name"])}]({SITE}?item={x["id"]}) | {md(x["qualityReason"])} |')
 lines+=['','## All gunpacks, ranked by popularity','','| Rank / embedded image | Gunpack | Popularity evidence | Direct source / video |','|---|---|---|']
 for x in data['items']:
  im=next((m for m in x['media'] if m['sha256']==x.get('preferredMediaSha256')),None) or next((m for m in x['media'] if m['role']!='Project icon'),next(iter(x['media']),None))
  image=f'<a href="{SITE}?item={x["id"]}"><img src="{RAW+im["src"].removeprefix("../")}?v={im["sha256"][:8]}" width="210" alt="{md(x["name"])}"></a><br><sub>{md(im["role"])}</sub>' if im else 'No creator image established'
  m=x['metrics'];stat=f'**{number(m["downloads"])} downloads** ({md(m["downloadSource"])})<br>CF favorites: {number(m["favorites"])}<br>MR followers: {number(m["followers"])}'
  links=f'[Project]({x["projectUrl"]}) · [Details / rate / save]({SITE}?item={x["id"]})'
  if x['videos']:links+=f'<br>[Creator video]({x["videos"][0]["url"]})'
  legacy='<br>**Legacy: discontinued by creator.**' if x['maintenance']=='Discontinued by creator' else '<br>**Creator has paused updates.**' if x['maintenance']=='Paused by creator' else ''
  lines.append(f'| **#{x["popularityRank"]}**<br>{image} | **{md(x["name"])}**<br>{md(x["summary"])}<br><sub>{md(x["type"])}</sub>{legacy} | {stat} | {links} |')
 lines+=['','## Evidence and preserved collections','',f'[Metric sources and inclusion decisions](https://github.com/Herbertofury/Advent-of-Ascension/tree/main/docs/minecraft-gun-mods/tacz) · [Machine-readable gunpack catalog]({SITE}catalog.json)','',
 'The parent Minecraft atlas is preserved. Favorites and research notes use its existing browser collection; the dedicated page additionally stores private ratings and its own saved views. Export backups before changing browsers. Full playback and native Minecraft testing of every pack are not claimed.','', '## End of gunpack gallery','']
 body='\n'.join(lines);assert len(body.encode())<490000;(DOCS/'TaCZ-Gunpacks.md').write_text(body,encoding='utf-8')

def main():
 before=hashlib.sha256((PARENT/'catalog.json').read_bytes()).hexdigest();data=data_build();ui_build(data);wiki_build(data)
 assert before==hashlib.sha256((PARENT/'catalog.json').read_bytes()).hexdigest()
 files=set();missing=[]
 for x in data['items']:
  for im in x['media']:
   p=ROOT/im['src'];files.add(im['src'])
   if not p.exists():missing.append(im['src'])
 assert not missing,missing
 save(ROOT/'build-proof.json',{'items':len(data['items']),'familiesWithImages':sum(bool(x['media']) for x in data['items']),'mediaFiles':len(files),'withCfFavorites':sum(x['metrics']['favorites'] is not None for x in data['items']),'withMrFollowers':sum(x['metrics']['followers'] is not None for x in data['items']),'shortlist':sum(x['id'] in SHORTLIST for x in data['items']),'parentCatalogUnchanged':before,'missingImages':missing,'communityRatingValuesInvented':0})
 print(json.dumps(load(ROOT/'build-proof.json'),indent=2))
if __name__=='__main__':main()
