#!/usr/bin/env python3
"""Additive, idempotent TaCZ discovery overlay over the existing canonical atlas."""
from __future__ import annotations
import argparse,collections,copy,hashlib,html,importlib.util,json,re,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent;TACZ=PARENT/'tacz'
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minecraft-gun-mods/'

def load(p,default=None):return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
def dh(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def md(s):
 s=html.escape(str(s or '')).replace('|','&#124;').replace('\n',' ')
 for ch in '*_`[]~':s=s.replace(ch,'&#'+str(ord(ch))+';')
 return s

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def tacz_record(record):
 item=copy.deepcopy(record['item']);spec=record['editorial'];facts=record.get('metrics') or [record['metric']]
 for media in item['media']:
  if not media['src'].startswith('../'):media['src']='../'+media['src']
 def maximum(field,provider=None):
  values=[x[field] for x in facts if isinstance(x.get(field),(int,float)) and (provider is None or x['provider']==provider)]
  return max(values) if values else None
 metrics={'downloads':maximum('downloads'),'cfDownloads':maximum('downloads','CurseForge'),'mrDownloads':maximum('downloads','Modrinth'),'favorites':maximum('favorites','CurseForge'),'followers':maximum('followers','Modrinth'),'communityRating':None}
 metrics['downloadSource']=next((x['provider'] for x in facts if metrics['downloads'] is not None and x.get('downloads')==metrics['downloads']),'Not published')
 maintenance=spec.get('maintenance',item.get('maintenanceNotice','No discontinuation notice found'))
 item.update(metricSources=facts,contentSources=[{'url':item['projectUrl'],'summary':item['summary'],'features':{},'checkedAt':item['checkedAt']}],variants=[{'id':item['id'],'name':item['name'],'url':item['projectUrl']}],familyIds=[item['id']],aliases=list(item.get('aliases',[])),maintenance=maintenance,historicalDownloadsMixed=False,metrics=metrics,metricFreshness='Current exact creator-source read',activity='Legacy / discontinued' if maintenance!='No discontinuation notice found' else 'Current / no discontinuation notice',curation='Quality shortlist' if spec.get('shortlist') else 'Research discovery',studyPriority=100 if spec.get('shortlist') else 50,qualityReason=spec['reason'],qualitySignals=(['Creator imagery available'] if item['media'] else [])+(['Creator-linked footage'] if item['videos'] else []))
 item['type']=spec.get('type') or ('Gun-adding add-on (JAR)' if '/mc-mods/' in item['projectUrl'] else 'Creator-hosted gunpack' if item.get('provider') not in ('CurseForge','Modrinth') else 'Gunpack (ZIP)')
 item['cautions']=list(dict.fromkeys(item['cautions']+['Requires the exact TaCZ runtime and any additional dependencies named by its creator. This listing is source research, not a native Minecraft compatibility test.']))
 if isinstance(item.get('license'),dict):item['license']=item['license'].get('name') or item['license'].get('id') or 'See creator license'
 return item


def extend(parent_index,tacz_index):
 records=load(ROOT/'qualified-records.json',{})
 if not records:return set()
 selection=load(ROOT/'selection.json');accepted={x['id'] for x in selection['accepted']}|set(load(ROOT/'extra-records.json',{}));records={**records,**load(ROOT/'extra-records.json',{})}
 assert set(records)==accepted,{'unqualified':sorted(accepted-set(records)),'unexpected':sorted(set(records)-accepted)}
 review=load(ROOT/'media-overrides.json',{'preferred':{},'exclude':[]})
 for key,rec in records.items():
  rec=copy.deepcopy(rec);item=rec['item'];spec=rec['editorial']
  item['media']=[m for m in item['media'] if m['sha256'] not in review.get('exclude',[])]
  if key in review.get('preferred',{}):
   sha=review['preferred'][key];assert any(m['sha256']==sha for m in item['media']),(key,'reviewed image absent');item['preferredMediaSha256']=sha
   item['media'].sort(key=lambda m:m['sha256']!=sha)
  if isinstance(item.get('license'),dict):item['license']=item['license'].get('name') or item['license'].get('id') or 'See creator license'
  if key not in parent_index:parent_index[key]=copy.deepcopy(item)
  else:
   # Only the deliberately selected old records gain discovery facets; all other data remains intact.
   old=parent_index[key];old['themes']=list(dict.fromkeys(old.get('themes',[])+['Deep discoveries']+(['Hidden gems'] if spec.get('shortlist') else [])))
  if key not in tacz_index:tacz_index[key]=tacz_record({**rec,'item':item})
  else:
   # Idempotent source-image corrections are scoped to this update's own records.
   target=tacz_index[key];target['media']=copy.deepcopy(item['media'])
   for m in target['media']:
    if not m['src'].startswith('../'):m['src']='../'+m['src']
   if item.get('preferredMediaSha256'):target['preferredMediaSha256']=item['preferredMediaSha256']
 return set(records)


def patch_owner():
 path=PARENT/'creator-discoveries/build_update.py';text=path.read_text()
 marker='    parent[\'items\']=sorted(pidx.values(),'
 hook="""    # Deep-discovery overlay: keep later accepted content through every original rebuild.
    deep_ids=set()
    _deep_path=PARENT/'tacz-deep-discovery/build_deep.py'
    if _deep_path.exists() and (_deep_path.parent/'qualified-records.json').exists():
        _deep=module('deep_discovery_overlay',_deep_path);deep_ids=_deep.extend(pidx,tidx)
"""
 if '# Deep-discovery overlay:' not in text:
  assert marker in text;text=text.replace(marker,hook+marker,1)
 text=text.replace("assert set(parent_changed)<=enriched,parent_changed","assert set(parent_changed)<=enriched|deep_ids,parent_changed")
 text=text.replace("assert set(tacz_changed)<=enriched,tacz_changed","assert set(tacz_changed)<=enriched|deep_ids,tacz_changed")
 text=text.replace("assert len(parent['items'])==before['parentCount']+5","assert set(pidx)==set(before['parent'])|set(qualified)|deep_ids")
 text=text.replace("assert len(tacz['items'])==before['taczCount']+4","assert set(tidx)==set(before['tacz'])|expected_new|deep_ids")
 old="    discoveries_page(parent,tacz);update_ui()\n    return parent,tacz"
 new="""    discoveries_page(parent,tacz);update_ui()
    _deep_path=PARENT/'tacz-deep-discovery/build_deep.py'
    if _deep_path.exists() and (_deep_path.parent/'qualified-records.json').exists():
        module('deep_discovery_publication',_deep_path).finish(parent,tacz)
    return parent,tacz"""
 assert old in text or new in text;text=text.replace(old,new)
 import ast;ast.parse(text);path.write_text(text,encoding='utf-8')


def finish(parent,tacz):
 records={**load(ROOT/'qualified-records.json',{}),**load(ROOT/'extra-records.json',{})};ids=set(records)
 for folder,data in ((PARENT,parent),(TACZ,tacz)):
  data['coverage']['deepDiscoveryDelta']={'families':len(ids),'newToThisCollection':len(ids-set(load(ROOT/'baseline.json')[('parent' if folder==PARENT else 'tacz')])),'sourceEvidence':'tacz-deep-discovery/coverage.json'}
  data['build']['lastDelta']='TaCZ deep discoveries 2026-10-23'
  save(folder/'catalog.json',data);(folder/'catalog.js').write_text('window.GUN_ATLAS='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
  page=folder/'index.html';body=page.read_text()
  if 'data-deep-preset="all"' not in body:
   body=body.replace('<div class="preset-row" aria-label="Quick filters">','<div class="preset-row" aria-label="Quick filters"><button data-deep-preset="all">Deep discoveries</button><button data-deep-preset="gems">Hidden gems</button>')
  if 'id="deepDiscoveryLink"' not in body:body=body.replace('<nav aria-label="Main navigation">','<nav aria-label="Main navigation"><a id="deepDiscoveryLink" href="'+WIKI+'TaCZ-Gunpack-Hidden-Gems">Hidden-gem research</a>')
  page.write_text(body,encoding='utf-8')
  jsfile=folder/'app.js';js=jsfile.read_text()
  if 'data-deep-preset' not in js:
   hook="document.addEventListener('click',event=>{const b=event.target.closest('[data-deep-preset]');if(!b)return;state={...DEFAULTS,view:state.view,theme:b.dataset.deepPreset==='gems'?'Hidden gems':'Deep discoveries'};syncControls();render();});\n"
   needle='renderSavedViews();syncControls();render();';assert needle in js;js=js.replace(needle,hook+needle,1)
  jsfile.write_text(js,encoding='utf-8')
 # The standard TaCZ renderer remains authoritative; add the new editorial selections to its data-driven pass.
 tb=module('tacz_deep_renderer',TACZ/'build_ui.py')
 tb.SHORTLIST.update({key:r['editorial']['reason'] for key,r in records.items() if r['editorial'].get('shortlist')})
 tb.wiki_build(tacz)
 p=DOCS/'TaCZ-Gunpacks.md';body=p.read_text();needle='## All gunpacks, ranked by popularity'
 links='## Newly researched hidden gems\n\n[Explore all deep discoveries]('+SITE+'tacz/?theme=Deep+discoveries) · [Curated hidden gems]('+SITE+'tacz/?theme=Hidden+gems) · [Research, access labels and source coverage](TaCZ-Gunpack-Hidden-Gems)\n\n'
 assert needle in body;p.write_text(body.replace(needle,links+needle,1),encoding='utf-8')
 write_research_page(tacz,records)


def write_research_page(tacz,records):
 selected=[x for x in tacz['items'] if x['id'] in records]
 lines=['# TaCZ gunpack hidden gems','', '[Weapon inspirations](Weapon-Inspirations) / [TaCZ gunpacks](TaCZ-Gunpacks) / **Deep discoveries**','',f'**{len(selected)} additional gun-content families qualified from the wider source search.**','',f'[Explore all additions]({SITE}tacz/?theme=Deep+discoveries) · [Focus on the editorial hidden-gem shortlist]({SITE}tacz/?theme=Hidden+gems)','',
 'These are additions to the research collection, not a claim that every pack was recently released. Exact published file dates, declared TaCZ dependencies and legacy restrictions stay visible. Popularity remains source-specific; no community rating is invented.','',
 '## Standout designs and focused discoveries','','| Creator image | Pack and design hook | Access and exact source |','|---|---|---|']
 for x in selected:
  m=next((m for m in x['media'] if m['sha256']==x.get('preferredMediaSha256')),None) or next((m for m in x['media'] if m['role']!='Project icon'),next(iter(x['media']),None))
  image=f'<a href="{SITE}tacz/?item={x["id"]}"><img src="{RAW+m["src"].removeprefix("../")}?v={m["sha256"][:8]}" width="210" alt="{md(x["name"])}"></a><br><sub>{md(m["role"])}</sub>' if m else 'Creator preview not established'
  file=(x.get('latest') or {});date=file.get('date','')[:10] or 'Release date not independently established'
  right=f'**{md(x.get("access","See creator release"))}**<br>[Creator source]({x["projectUrl"]})<br>File evidence: {md(date)}'
  if x['videos']:right+=f'<br>[Creator footage]({x["videos"][0]["url"]})'
  if records[x['id']]['editorial'].get('caution'):right+='<br>'+md(records[x['id']]['editorial']['caution'])
  lines.append(f'| {image} | **[{md(x["name"])}]({SITE}tacz/?item={x["id"]})**<br>{md(x["qualityReason"])} | {right} |')
 coverage=load(ROOT/'coverage.json',{})
 lines+=['','## Search coverage and rejected lookalikes','',
 'The source sweep covers CurseForge mods, customization, add-ons and resource packs; paginated Modrinth searches; creator GitHub projects; independent discovery indexes; public Chinese/Japanese creator sources; and creator-linked support pages. Mirrors, renamed projects, server modpacks, attachment-only packages, skins, recipes and unpublished source prototypes are not padded into the gunpack count.','',
 '[Machine-readable inclusion, exclusion and unresolved-source ledger](https://github.com/Herbertofury/Advent-of-Ascension/tree/main/docs/minecraft-gun-mods/tacz-deep-discovery) records the finite coverage. Search results are leads, not automatic acceptance. Public sources cannot prove that every private, unlisted or inaccessible creator pack has been found.','',
 'Only creator descriptions, release metadata and public reference imagery were inspected. No mod binary was installed or executed. Source-only prototypes and access-limited distribution remain separate from verified public release files.','',
 '## End of hidden-gem gallery','']
 (DOCS/'TaCZ-Gunpack-Hidden-Gems.md').write_text('\n'.join(lines),encoding='utf-8')


def ledger():
 found=load(ROOT/'tail-discovery.json',load(ROOT/'discovery.json')['sources']);coverage=load(ROOT/'discovery.json')['coverage'];recovery=load(ROOT/'coverage-recovery.json',[]);accepted=set(load(ROOT/'qualified-records.json',{}))|set(load(ROOT/'extra-records.json',{}));selection=load(ROOT/'selection.json');excluded=selection['excludedOrRelated'];prior=load(PARENT/'tacz/additional-selection.json',{}).get('excluded',{})
 known=load(ROOT/'baseline.json')['tacz'];tacz=load(TACZ/'catalog.json');existing=set(known)
 for x in tacz['items']:
  if x['id'] not in accepted:existing.update(x.get('aliases',[]));existing.update(('cf-' if p=='curseforge' else 'mr-')+str(v) for p,v in x.get('providerIds',{}).items())
 decisions=[]
 for x in found:
  key=x['id'];value=' '.join([x.get('name',''),x.get('summary','')]).lower()
  if key in accepted:state,reason='accepted','Creator source establishes additional TaCZ firearm content; source, release and media qualification retained.'
  elif key in existing:state,reason='already represented','Existing canonical family or provider identity; not counted again.'
  elif key in excluded or key in prior:state,reason='excluded or source-limited',excluded.get(key,prior.get(key))
  elif x.get('projectType') in ('modpack','shader'):state,reason='excluded','Modpack or shader, not an independent TaCZ firearm-content pack.'
  elif not re.search(r'tacz|tac.zero|timeless.{0,30}(zero|classic)|gun.?pack',value):state,reason='excluded','Search-term collision without a TaCZ gun-content identity in the project title or summary.'
  elif re.search(r'compat|fix|optim|performance|render|api|library|lib\b|ammo|ammunition|npc|zombie|mobs|loot|recipe|integration|blueprint|enchant|attachment|skin|sound|hud|crosshair|scope|recoil|tweak|durability|armor|movement|sway|port|fork|refabric|reloader|reload|animation|melee|knife|knives|sword|tactical equipment|server|modpack|server|template|tutorial|example|making diary',value):state,reason='excluded from gun-content count','Source identity indicates supporting behavior, integration, cosmetic content, distribution or development tooling rather than a separately qualified firearm roster.'
  else:state,reason='unresolved lead','Not promoted without sufficient distinct creator firearm, release and identity evidence.'
  decisions.append({'id':key,'name':x.get('name'),'url':x.get('url'),'status':state,'reason':reason})
 effective=[]
 for x in coverage:
  tail=next((y for y in recovery if y['provider']==x['provider'] and y.get('class')==x.get('class') and y['query']==x['query']),None)
  effective.append({'provider':x['provider'],'class':x.get('class'),'query':x['query'],'terminalPageReached':bool(x['terminalPageReached'] or tail and tail['terminalPageReached']),'initialRecordsRead':x.get('recordsRead'),'recoveryPages':len(tail.get('evidence',[])) if tail else 0})
 report={'baselineFamilies':len(known),'discoveredSourceIdentities':len(found),'acceptedAdditionalFamilies':len(accepted),'decisions':dict(collections.Counter(x['status'] for x in decisions)),'queries':effective,'terminalQueries':sum(x['terminalPageReached'] for x in effective),'queryCount':len(effective),'finiteCoverageNotUniversalCensus':True}
 save(ROOT/'source-decisions.json',decisions);save(ROOT/'coverage.json',report)
 return report


def proof_and_contacts():
 p=load(PARENT/'catalog.json');t=load(TACZ/'catalog.json');before=load(ROOT/'baseline.json');records={**load(ROOT/'qualified-records.json',{}),**load(ROOT/'extra-records.json',{})};ids=set(records);pi={x['id']:x for x in p['items']};ti={x['id']:x for x in t['items']}
 assert set(before['parent'])<=set(pi) and set(before['tacz'])<=set(ti)
 assert set(ti)-set(before['tacz'])==ids-set(before['tacz'])
 changedp=[k for k,v in before['parent'].items() if dh(pi[k])!=v];changedt=[k for k,v in before['tacz'].items() if dh({a:b for a,b in ti[k].items() if a!='popularityRank'})!=v]
 assert set(changedp)<=ids and not changedt,(changedp,changedt)
 images={}
 for key in ids:
  x=ti[key];assert x['metrics']['communityRating'] is None
  for media in x['media']:
   path=TACZ/media['src'];assert path.is_file(),str(path)
   actual=hashlib.sha256(path.read_bytes()).hexdigest();assert actual==media['sha256'],str(path)
   if actual not in images:
    with Image.open(path) as im:im.verify()
    images[actual]=str(path)
 coverage=ledger();proof={'parentProjects':len(pi),'taczFamilies':len(ti),'newParentRecords':len(set(pi)-set(before['parent'])),'newTaCZFamilies':len(ids-set(before['tacz'])),'newQualifiedIds':sorted(ids),'oldParentIdsPreserved':True,'oldTaCZIdsPreserved':True,'changedOldParentIds':changedp,'unchangedOldTaCZItemsExceptRanks':True,'newReferenceImageHashes':len(images),'newEntriesWithMedia':sum(bool(ti[k]['media']) for k in ids),'newShortlistEntries':sum(ti[k]['curation']=='Quality shortlist' for k in ids),'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash'],'coverage':{k:v for k,v in coverage.items() if k!='queries'}}
 save(ROOT/'qa/data-delta.json',proof)
 out=ROOT/'qa/new-media';out.mkdir(parents=True,exist_ok=True);font=ImageFont.load_default(size=16);selected=[x for x in t['items'] if x['id'] in ids]
 for start in range(0,len(selected),20):
  batch=selected[start:start+20];sheet=Image.new('RGB',(1400,250*((len(batch)+3)//4)),(230,230,230));draw=ImageDraw.Draw(sheet)
  for i,x in enumerate(batch):
   media=next((m for m in x['media'] if m['sha256']==x.get('preferredMediaSha256')),None) or next((m for m in x['media'] if m['role']!='Project icon'),next(iter(x['media']),None));xx=i%4*350;yy=i//4*250
   if media:
    im=Image.open(TACZ/media['src']).convert('RGBA');im.thumbnail((345,199));sheet.paste(im,(xx,yy),im)
   draw.text((xx+3,yy+205),x['name'][:40],font=font,fill='black');draw.text((xx+3,yy+229),x['id'],font=font,fill='black')
  sheet.save(out/('cards-%02d.jpg'%(start//20+1)),quality=94)
 print(json.dumps(proof,indent=2),flush=True)
 return proof


def main():
 baseline=ROOT/'baseline.json'
 if not baseline.exists():
  p=load(PARENT/'catalog.json');t=load(TACZ/'catalog.json');selection=load(ROOT/'selection.json');assert t['build']['dataHash']==selection['baselineDataHash']
  save(baseline,{'parent':{x['id']:dh(x) for x in p['items']},'tacz':{x['id']:dh({k:v for k,v in x.items() if k!='popularityRank'}) for x in t['items']},'parentCount':len(p['items']),'taczCount':len(t['items'])})
 patch_owner();u=module('creator_delta_with_deep',PARENT/'creator-discoveries/build_update.py');u.refresh();proof_and_contacts()
 # Regenerating is a no-op for canonical data and controls, not a reset to an earlier snapshot.
 paths=[PARENT/'catalog.json',TACZ/'catalog.json',PARENT/'app.js',TACZ/'app.js',PARENT/'index.html',TACZ/'index.html']
 hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths};u.refresh()
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==v for p,v in hashes.items()),'Deep overlay is not idempotent'
 save(ROOT/'qa/idempotence.json',{'passed':True,'verifiedPaths':list(hashes),'sharedNavigationOwner':'docs/weapon_inspiration_navigation.py'})
if __name__=='__main__':main()
