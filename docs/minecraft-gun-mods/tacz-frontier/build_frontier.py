#!/usr/bin/env python3
"""Preserve the entire existing atlas while adding qualified creator-frontier records."""
from __future__ import annotations
import ast,copy,hashlib,html,importlib.util,json,re,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;TACZ=PARENT/'tacz';DOCS=PARENT.parent
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minecraft-gun-mods/'
PAGE='TaCZ-Gunpack-Creator-Frontier'

def load(p,default=None):return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
def dh(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def filehash(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def md(value):
 s=html.escape(str(value or '')).replace('|','&#124;').replace('\n',' ')
 for ch in '*_`[]~':s=s.replace(ch,'&#'+str(ord(ch))+';')
 return s

def extend(parent_index,tacz_index):
 records=load(ROOT/'qualified-records.json',{});spec=load(ROOT/'selection.json');assert set(records)=={x['id'] for x in spec['accepted']}
 previous=module('frontier_existing_record_schema',PARENT/'tacz-deep-discovery/build_deep.py');review=load(ROOT/'media-overrides.json',{'preferred':{},'exclude':[]})
 for key,record in records.items():
  record=copy.deepcopy(record);item=record['item'];item['media']=[m for m in item['media'] if m['sha256'] not in review.get('exclude',[])]
  preferred=review.get('preferred',{}).get(key)
  if preferred:
   assert any(m['sha256']==preferred for m in item['media']),(key,'reviewed preview unavailable');item['preferredMediaSha256']=preferred;item['media'].sort(key=lambda m:m['sha256']!=preferred)
  assert item['media'],(key,'no source preview')
  parent_index[key]=copy.deepcopy(item)
  t=previous.tacz_record({**record,'item':item});t['activity']=item['activity'];tacz_index[key]=t
 return set(records)

def patch_owner():
 path=PARENT/'creator-discoveries/build_update.py';text=path.read_text();needle="    parent['items']=sorted(pidx.values(),"
 hook="""    # Creator-frontier overlay: retain qualified creator/source packs through normal rebuilds.
    frontier_ids=set()
    _frontier_path=PARENT/'tacz-frontier/build_frontier.py'
    if _frontier_path.exists() and (_frontier_path.parent/'qualified-records.json').exists():
        frontier_ids=module('creator_frontier_records',_frontier_path).extend(pidx,tidx)
"""
 if '# Creator-frontier overlay:' not in text:assert needle in text;text=text.replace(needle,hook+needle,1)
 for old,new in [("assert set(parent_changed)<=enriched|deep_ids,parent_changed","assert set(parent_changed)<=enriched|deep_ids|frontier_ids,parent_changed"),("assert set(tacz_changed)<=enriched|deep_ids,tacz_changed","assert set(tacz_changed)<=enriched|deep_ids|frontier_ids,tacz_changed"),("assert set(pidx)==set(before['parent'])|set(qualified)|deep_ids","assert set(pidx)==set(before['parent'])|set(qualified)|deep_ids|frontier_ids"),("assert set(tidx)==set(before['tacz'])|expected_new|deep_ids","assert set(tidx)==set(before['tacz'])|expected_new|deep_ids|frontier_ids")]:
  if new not in text:assert old in text,(old,'owner changed');text=text.replace(old,new)
 needle="        module('deep_discovery_publication',_deep_path).finish(parent,tacz)\n    return parent,tacz"
 replacement="""        module('deep_discovery_publication',_deep_path).finish(parent,tacz)
    _frontier_path=PARENT/'tacz-frontier/build_frontier.py'
    if _frontier_path.exists() and (_frontier_path.parent/'qualified-records.json').exists():
        module('creator_frontier_publication',_frontier_path).finish(parent,tacz)
    return parent,tacz"""
 if replacement not in text:assert needle in text;text=text.replace(needle,replacement,1)
 ast.parse(text);path.write_text(text,encoding='utf-8')

def add_section(path,body):
 start='<!-- tacz-creator-frontier:start -->';end='<!-- tacz-creator-frontier:end -->';text=path.read_text();block=start+'\n'+body+'\n'+end
 if start in text:
  a=text.index(start);b=text.index(end,a)+len(end);text=text[:a]+block+text[b:]
 else:text=text.rstrip()+'\n\n'+block+'\n'
 path.write_text(text,encoding='utf-8')

def finish(parent,tacz):
 records=load(ROOT/'qualified-records.json');ids=set(records);coverage=load(ROOT/'coverage.json')
 for folder,data in ((PARENT,parent),(TACZ,tacz)):
  data['coverage']['creatorFrontierDelta']={'families':len(ids),'editorialSelections':sum(r['editorial']['shortlist'] for r in records.values()),'evidence':'tacz-frontier/coverage.json'}
  data['build']['lastDelta']='TaCZ creator frontier '+max(x['item']['checkedAt'][:10] for x in records.values())
  save(folder/'catalog.json',data);(folder/'catalog.js').write_text('window.GUN_ATLAS='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
  htmlfile=folder/'index.html';body=htmlfile.read_text()
  if 'data-frontier-preset' not in body:
   needle='<div class="preset-row" aria-label="Quick filters">';assert needle in body
   body=body.replace(needle,needle+'<button data-frontier-preset="all">Creator frontier</button>',1)
  htmlfile.write_text(body,encoding='utf-8')
  jsfile=folder/'app.js';js=jsfile.read_text()
  if 'data-frontier-preset' not in js:
   hook="document.addEventListener('click',event=>{const b=event.target.closest('[data-frontier-preset]');if(!b)return;state={...DEFAULTS,view:state.view,theme:'Frontier discoveries'};syncControls();render();});\n"
   needle='renderSavedViews();syncControls();render();';assert needle in js;js=js.replace(needle,hook+needle,1)
  jsfile.write_text(js,encoding='utf-8')
 # Retain all earlier editorial picks while rendering the complete expanded TaCZ page.
 renderer=module('frontier_tacz_renderer',TACZ/'build_ui.py');renderer.SHORTLIST.update({x['id']:x['qualityReason'] for x in tacz['items'] if x['curation']=='Quality shortlist'});renderer.wiki_build(tacz)
 add_section(DOCS/'TaCZ-Gunpacks.md','## Additional creator research\n\n[Earlier 46 hidden-gem discoveries](TaCZ-Gunpack-Hidden-Gems) · [Creator frontier: original-source releases and tests]('+PAGE+') · [Explore this pass]('+SITE+'tacz/?theme=Frontier+discoveries)')
 add_section(DOCS/'TaCZ-Gunpack-Hidden-Gems.md','## Continue into creator-hosted releases\n\n[Creator-frontier research]('+PAGE+') adds seven separately qualified sources without changing the earlier 46 discovery identities.')
 add_section(DOCS/'Minecraft-Gunpack-Creator-Discoveries.md','## Further original-creator discoveries\n\n[Creator-frontier research]('+PAGE+') covers released/test-edition gunpacks, access limits and two smaller historical/source references.')
 write_page(tacz,records,coverage)


def write_page(tacz,records,coverage):
 index={x['id']:x for x in tacz['items']};selected=load(ROOT/'selection.json')['accepted'];lines=['# TaCZ creator frontier','',
 '[Weapon inspirations](Weapon-Inspirations) / [TaCZ gunpacks](TaCZ-Gunpacks) / **Creator frontier**','',
 '**Seven additional creator/source gunpack families. Four editorial study selections; test editions and legacy sources remain explicitly labeled.**','',
 '[Explore this research pass]('+SITE+'tacz/?theme=Frontier+discoveries) · [Complete TaCZ rankings]('+SITE+'tacz/) · [Earlier hidden gems](TaCZ-Gunpack-Hidden-Gems)','',
 'This pass looks beyond provider popularity pages: original Bilibili creator releases, public Afdian destinations, author-maintained project pages and small GitHub gunpack repositories. Creator announcements are not silently turned into exact downloadable-file records. Video views, likes and author followers are not gunpack popularity.','',
 '## Qualified releases, tests and source references','','| Creator preview | Gunpack and distinctive content | Release evidence and access |','|---|---|---|']
 for spec in selected:
  x=index[spec['id']];m=next((m for m in x['media'] if m['sha256']==x.get('preferredMediaSha256')),x['media'][0]);url=SITE+'tacz/?item='+x['id']
  img='<a href="'+url+'"><img src="'+RAW+m['src'].removeprefix('../')+'?v='+m['sha256'][:8]+'" width="220" alt="'+md(x['name'])+'"></a><br><sub>'+md(m['role'])+'</sub>'
  name='**['+md(x['name'])+']('+url+')**'
  if spec.get('originalName'):name+='<br>'+md(spec['originalName'])+' ('+md(spec['meaning'])+')'
  description=name+'<br>'+md(spec['reason'])
  ann=x['releaseAnnouncements'][0] if x['releaseAnnouncements'] else None
  timing=('Announcement '+ann['date'][:10]) if ann else ('File '+x['latest']['date'][:10]) if x.get('latest') else 'Source snapshot; no release file verified'
  evidence='**'+md(spec['releaseLabel'])+'**<br>'+md(timing)+'<br>**'+md(x['access'])+'**<br>'+md(x['creatorAccessNote'])+'<br>[Original creator source]('+x['projectUrl']+')'
  if x['videos']:evidence+='<br>[Creator footage]('+x['videos'][0]['url']+')'
  lines.append('| '+img+' | '+description+' | '+evidence+' |')
 lines+=['','## Search coverage and lookalikes','',
 f'The provider sweep records **{coverage["sourceIdentities"]:,} distinct source listings**, **{coverage["queries"]} terminal query traversals**, **{coverage["sourceCandidatesRead"]} candidate source reads**, **{coverage["repositoryIdentityChecks"]} focused repository checks**, and **{coverage["creatorVideos"]} exact creator-video metadata records**. Broad results include many unrelated projects and support mods; these counts are not a claim that thousands of TaCZ gunpacks exist.','',
 'The canceled ESSENCE predecessor, unfinished Antar and AX50 previews, named-but-unillustrated ZIPs, source templates, base-runtime forks and already-listed creator packs were not padded into the published family count. The source ledger preserves unresolved leads rather than calling them nonexistent.','',
 '[Inclusion/exclusion ledger](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/minecraft-gun-mods/tacz-frontier/source-decisions.json) · [Exact coverage evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/minecraft-gun-mods/tacz-frontier/coverage.json)','',
 'Source snapshots, engineering tests, creator announcements and actual release files are different evidence classes. All older pack identities and personal collection storage remain intact. No mod binary or paid attachment was retrieved, no images were generated, and native Minecraft compatibility/performance testing is not claimed.','',
 '## End of creator-frontier gallery','']
 (DOCS/(PAGE+'.md')).write_text('\n'.join(lines),encoding='utf-8')


def proof():
 p=load(PARENT/'catalog.json');t=load(TACZ/'catalog.json');base=load(ROOT/'baseline.json');records=load(ROOT/'qualified-records.json');ids=set(records);pi={x['id']:x for x in p['items']};ti={x['id']:x for x in t['items']}
 assert set(pi)==set(base['parent'])|ids and set(ti)==set(base['tacz'])|ids
 assert not (set(base['parent'])&ids) and not (set(base['tacz'])&ids)
 changedp=[k for k,h in base['parent'].items() if dh(pi[k])!=h];changedt=[k for k,h in base['tacz'].items() if dh({a:b for a,b in ti[k].items() if a!='popularityRank'})!=h]
 assert not changedp and not changedt,(changedp,changedt)
 media={}
 for key in ids:
  x=ti[key];assert x['metrics']['communityRating'] is None
  if key.startswith('bilibili-'):assert all(x['metrics'][field] is None for field in ('downloads','cfDownloads','mrDownloads','favorites','followers'))
  for m in x['media']:
   path=TACZ/m['src'];assert path.exists() and filehash(path)==m['sha256'],path
   with Image.open(path) as im:im.verify()
   media[m['sha256']]=m
  assert x['releaseAnnouncements'] or x['releases'] or x.get('sourceSnapshot')
 report={'parentProjects':len(pi),'taczFamilies':len(ti),'additionalFamilies':len(ids),'newParentRecords':len(ids),'editorialSelections':sum(x['editorial']['shortlist'] for x in records.values()),'oldParentRecordsUnchanged':True,'oldTaCZRecordsUnchangedExceptRanks':True,'distinctNewMedia':len(media),'allNewRecordsIllustrated':True,'inventedCommunityRatings':0,'videoPopularityUsedForGunpackRanking':False,'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash'],'newIds':sorted(ids)}
 save(ROOT/'qa/data-delta.json',report)
 out=ROOT/'qa';out.mkdir(exist_ok=True);font=ImageFont.load_default(size=16);sheet=Image.new('RGB',(1400,250*((len(ids)+3)//4)),(230,230,230))
 draw=ImageDraw.Draw(sheet)
 for n,spec in enumerate(load(ROOT/'selection.json')['accepted']):
  x=ti[spec['id']];m=next((m for m in x['media'] if m['sha256']==x.get('preferredMediaSha256')),x['media'][0]);im=Image.open(TACZ/m['src']).convert('RGBA');im.thumbnail((340,195));xx=n%4*350;yy=n//4*250;sheet.paste(im,(xx,yy),im);draw.text((xx+3,yy+199),x['name'][:39],font=font,fill='black');draw.text((xx+3,yy+225),x['id'],font=font,fill='black')
 sheet.save(out/'new-cards.jpg',quality=94);print(json.dumps(report),flush=True)
 return report


def main():
 if not (ROOT/'baseline.json').exists():
  p=load(PARENT/'catalog.json');t=load(TACZ/'catalog.json');s=load(ROOT/'selection.json');assert p['build']['dataHash']==s['baselineParentDataHash'] and t['build']['dataHash']==s['baselineTaCZDataHash']
  save(ROOT/'baseline.json',{'parent':{x['id']:dh(x) for x in p['items']},'tacz':{x['id']:dh({k:v for k,v in x.items() if k!='popularityRank'}) for x in t['items']},'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash']})
 patch_owner();owner=module('frontier_canonical_owner',PARENT/'creator-discoveries/build_update.py');owner.refresh();proof()
 paths=[PARENT/'catalog.json',TACZ/'catalog.json',PARENT/'app.js',TACZ/'app.js',PARENT/'index.html',TACZ/'index.html',DOCS/(PAGE+'.md')];before={str(p):filehash(p) for p in paths};owner.refresh();assert all(filehash(Path(p))==h for p,h in before.items()),'Non-idempotent frontier update'
 save(ROOT/'qa/idempotence.json',{'passed':True,'paths':before,'canonicalUpdate':'creator-discoveries/build_update.py refresh','oldRecordsUnchanged':True})
if __name__=='__main__':main()
