#!/usr/bin/env python3
"""Add creator-community gun families without replacing a single established catalog record."""
from __future__ import annotations
import ast,copy,hashlib,html,importlib.util,json,re,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;TACZ=PARENT/'tacz';DOCS=PARENT.parent
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
RAW='https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minecraft-gun-mods/'
PAGE='TaCZ-Gunpack-Community-Discoveries'

def load(path,default=None):return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default
def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def dh(obj):return hashlib.sha256(json.dumps(obj,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def fh(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def md(text):
 text=html.escape(str(text or '')).replace('|','&#124;').replace('\n',' ')
 for char in '*_`[]~':text=text.replace(char,'&#'+str(ord(char))+';')
 return text

def extend(pidx,tidx):
 records=load(ROOT/'qualified-records.json');spec=load(ROOT/'selection.json');review=load(ROOT/'media-review.json');ids={x['id'] for x in spec['accepted']}
 assert set(records)==ids and review['allCardsReviewed'] and not review['pending'], 'Complete creator/media acceptance required'
 mapper=module('community_existing_schema',PARENT/'tacz-deep-discovery/build_deep.py')
 for key,record in records.items():
  record=copy.deepcopy(record);item=record['item'];chosen=review['preferred'][key]
  assert chosen in {m['sha256'] for m in item['media']},key
  item['preferredMediaSha256']=chosen;item['media'].sort(key=lambda m:m['sha256']!=chosen)
  pidx[key]=copy.deepcopy(item);tidx[key]=mapper.tacz_record(record);tidx[key]['activity']=item['activity']
 return ids

def patch_owner():
 path=PARENT/'creator-discoveries/build_update.py';text=path.read_text();needle="    parent['items']=sorted(pidx.values(),"
 hook="""    # Creator-community overlay: new source-qualified guns retain the existing canonical owner.
    community_ids=set()
    _community_path=PARENT/'tacz-community/apply_community.py'
    if _community_path.exists() and (_community_path.parent/'qualified-records.json').exists():
        community_ids=module('creator_community_records',_community_path).extend(pidx,tidx)
"""
 if '# Creator-community overlay:' not in text:assert needle in text;text=text.replace(needle,hook+needle,1)
 replacements=[('enriched|deep_ids|frontier_ids,parent_changed','enriched|deep_ids|frontier_ids|community_ids,parent_changed'),('enriched|deep_ids|frontier_ids,tacz_changed','enriched|deep_ids|frontier_ids|community_ids,tacz_changed'),("set(before['parent'])|set(qualified)|deep_ids|frontier_ids","set(before['parent'])|set(qualified)|deep_ids|frontier_ids|community_ids"),("set(before['tacz'])|expected_new|deep_ids|frontier_ids","set(before['tacz'])|expected_new|deep_ids|frontier_ids|community_ids")]
 for old,new in replacements:
  if new not in text:assert old in text,old;text=text.replace(old,new)
 needle="        module('creator_frontier_publication',_frontier_path).finish(parent,tacz)\n    return parent,tacz"
 replacement="""        module('creator_frontier_publication',_frontier_path).finish(parent,tacz)
    _community_path=PARENT/'tacz-community/apply_community.py'
    if _community_path.exists() and (_community_path.parent/'qualified-records.json').exists():
        module('creator_community_publication',_community_path).finish(parent,tacz)
    return parent,tacz"""
 if replacement not in text:assert needle in text;text=text.replace(needle,replacement,1)
 ast.parse(text);path.write_text(text,encoding='utf-8')

def managed(path,body):
 text=path.read_text();start='<!-- tacz-community:start -->';end='<!-- tacz-community:end -->';block=start+'\n'+body+'\n'+end
 if start in text:
  a=text.index(start);b=text.index(end,a)+len(end);text=text[:a]+block+text[b:]
 else:text=text.rstrip()+'\n\n'+block+'\n'
 path.write_text(text,encoding='utf-8')

def finish(parent,tacz):
 records=load(ROOT/'qualified-records.json');selection=load(ROOT/'selection.json');coverage=load(ROOT/'coverage.json');ids=set(records)
 for folder,data in ((PARENT,parent),(TACZ,tacz)):
  data['coverage']['creatorCommunityDelta']={'families':len(ids),'editorialSelections':sum(x['editorial']['shortlist'] for x in records.values()),'evidence':'tacz-community/coverage.json'}
  data['build']['lastDelta']='TaCZ community discoveries '+max(x['item']['checkedAt'][:10] for x in records.values())
  save(folder/'catalog.json',data);(folder/'catalog.js').write_text('window.GUN_ATLAS='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
  path=folder/'index.html';text=path.read_text()
  if 'data-community-preset' not in text:
   needle='<div class="preset-row" aria-label="Quick filters">';assert needle in text;text=text.replace(needle,needle+'<button data-community-preset="all">Community discoveries</button>',1)
  path.write_text(text,encoding='utf-8')
  path=folder/'app.js';text=path.read_text()
  if 'data-community-preset' not in text:
   needle='renderSavedViews();syncControls();render();';assert needle in text
   hook="document.addEventListener('click',event=>{const b=event.target.closest('[data-community-preset]');if(!b)return;state={...DEFAULTS,view:state.view,theme:'Community discoveries'};syncControls();render();});\n"
   text=text.replace(needle,hook+needle,1)
  path.write_text(text,encoding='utf-8')
 renderer=module('community_tacz_renderer',TACZ/'build_ui.py');renderer.SHORTLIST.update({x['id']:x['qualityReason'] for x in tacz['items'] if x['curation']=='Quality shortlist'});renderer.wiki_build(tacz)
 # Preserve the established research trail without adding nested or competing navigation menus.
 frontier=module('community_prior_frontier',PARENT/'tacz-frontier/build_frontier.py')
 frontier.add_section(DOCS/'TaCZ-Gunpacks.md','## Additional creator research\n\n[Earlier hidden gems](TaCZ-Gunpack-Hidden-Gems) / [Creator frontier](TaCZ-Gunpack-Creator-Frontier) / [Community discoveries]('+PAGE+')')
 managed(DOCS/'TaCZ-Gunpacks.md','[Explore this community-source pass]('+SITE+'tacz/?theme=Community+discoveries) adds '+str(len(ids))+' distinct families with original creator footage and explicit release/access limits.')
 managed(DOCS/'TaCZ-Gunpack-Creator-Frontier.md','## Continue the research\n\n[Community discoveries]('+PAGE+') follows original creator collections and public forum releases without changing the earlier seven identities.')
 write_page(tacz,selection,coverage)

def write_page(tacz,selection,coverage):
 index={x['id']:x for x in tacz['items']};records=load(ROOT/'qualified-records.json');review=load(ROOT/'media-review.json')
 lines=['# TaCZ community discoveries','','[Weapon inspirations](Weapon-Inspirations) / [TaCZ gunpacks](TaCZ-Gunpacks) / **Community discoveries**','',
 '**'+str(len(records))+' additional creator gunpack families. '+str(sum(x['editorial']['shortlist'] for x in records.values()))+' editorial study selections.**','',
 '[Explore this pass]('+SITE+'tacz/?theme=Community+discoveries) / [Complete rankings]('+SITE+'tacz/) / [Earlier creator frontier](TaCZ-Gunpack-Creator-Frontier)','',
 'This pass follows original creator collections, obscure forum releases and public gunpack manifests. New to the catalog does not mean newly released. Creator announcements, public shares, engineering tests and exact binary releases remain different evidence classes. Source previews are attributed, not generated.','',
 '## Additional gunpack families','','| Original creator preview | What makes the pack distinctive | Release, access and exact limits |','|---|---|---|']
 for spec in selection['accepted']:
  x=index[spec['id']];im=next(m for m in x['media'] if m['sha256']==review['preferred'][x['id']]);url=SITE+'tacz/?item='+x['id'];image='<a href="'+url+'"><img src="'+RAW+im['src'].removeprefix('../')+'?v='+im['sha256'][:8]+'" width="220" alt="'+md(x['name'])+'"></a><br><sub>'+md(im['role'])+'</sub>'
  title='**['+md(x['name'])+']('+url+')**'
  if spec.get('originalName'):title+='<br>'+md(spec['originalName'])+' ('+md(spec['meaning'])+')'
  evidence='**'+md(spec['releaseLabel'])+'**<br>**'+md(x['access'])+'**<br>'+md(x['creatorAccessNote'])+'<br>[Original creator source]('+x['projectUrl']+')'
  if x['videos']:evidence+='<br>[Creator footage]('+x['videos'][0]['url']+')'
  lines.append('| '+image+' | '+title+'<br>'+md(spec['reason'])+' | '+evidence+' |')
 lines+=['','## Coverage and what was not counted','',
 'The original-community sweep inspected **'+str(coverage['exactCreatorMetadataRecords'])+' exact creator-video metadata records** and followed every relevant episode exposed by the selected author-owned collections. Video views and creator followers are not pack download or quality metrics.','',
 'Twenty Bilibili search queries were attempted. The provider blocked most requests and subsequent result pages, so none is falsely marked as a complete keyword traversal. Exact author-owned collections provided a different usable route. The existing completed CurseForge/Modrinth sweeps were not repeated.','',
 'GitHub manifest search: '+str(coverage.get('manifestFilesRead',0))+' files inspected; terminal traversal '+('confirmed' if coverage.get('manifestTraversalTerminal') else 'not established')+'. '+md(coverage.get('manifestLimitation','')),'',
 'The newly released Create-styled cosmetic redesign, Valorant Recon cosmetics, Otherworld HK416 repaint, TacBench editor, ambiguous Cyen/GHC clips and unreleased Rainbow Six progress video were not padded into the firearm-family count. The same creator\'s renamed TROL/IFCD lineage is not counted repeatedly.','',
 '[Inclusion and exclusion ledger](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/minecraft-gun-mods/tacz-community/source-decisions.json) / [Coverage evidence](https://github.com/Herbertofury/Advent-of-Ascension/blob/main/docs/minecraft-gun-mods/tacz-community/coverage.json)','',
 'No paid attachments or mod binaries were retrieved. Exact access and version gaps remain explicit; native Minecraft runtime compatibility and full playback of every linked video are not claimed.','',
 '## End of community-discovery gallery','']
 (DOCS/(PAGE+'.md')).write_text('\n'.join(lines),encoding='utf-8')

def proof():
 p=load(PARENT/'catalog.json');t=load(TACZ/'catalog.json');records=load(ROOT/'qualified-records.json');base=load(ROOT/'baseline.json');ids=set(records);pi={x['id']:x for x in p['items']};ti={x['id']:x for x in t['items']}
 assert set(pi)==set(base['parent'])|ids and set(ti)==set(base['tacz'])|ids
 assert not [k for k,h in base['parent'].items() if dh(pi[k])!=h]
 assert not [k for k,h in base['tacz'].items() if dh({a:b for a,b in ti[k].items() if a!='popularityRank'})!=h]
 media={}
 for key in ids:
  x=ti[key];assert all(x['metrics'][k] is None for k in ('communityRating','downloads','cfDownloads','mrDownloads','favorites','followers'))
  for m in x['media']:
   path=TACZ/m['src'];assert path.exists() and fh(path)==m['sha256'],path
   with Image.open(path) as im:im.verify()
   media[m['sha256']]=m
  assert x['releaseAnnouncements'] and x['media']
 report={'parentProjects':len(pi),'taczFamilies':len(ti),'additionalFamilies':len(ids),'editorialSelectionsAdded':sum(x['editorial']['shortlist'] for x in records.values()),'oldParentRecordsUnchanged':True,'oldTaCZRecordsUnchangedExceptRanks':True,'distinctNewMedia':len(media),'allNewRecordsIllustrated':True,'inventedPublicMetrics':0,'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash'],'newIds':sorted(ids)};save(ROOT/'qa/data-delta.json',report)
 out=ROOT/'qa';out.mkdir(exist_ok=True);font=ImageFont.load_default(size=16);sheet=Image.new('RGB',(1400,250*((len(ids)+3)//4)),(230,230,230));draw=ImageDraw.Draw(sheet)
 for n,spec in enumerate(load(ROOT/'selection.json')['accepted']):
  x=ti[spec['id']];m=next(m for m in x['media'] if m['sha256']==x['preferredMediaSha256']);im=Image.open(TACZ/m['src']).convert('RGBA');im.thumbnail((340,195));xx=n%4*350;yy=n//4*250;sheet.paste(im,(xx,yy),im);draw.text((xx+3,yy+199),x['name'][:39],font=font,fill='black');draw.text((xx+3,yy+225),x['id'],font=font,fill='black')
 sheet.save(out/'new-cards.jpg',quality=94);print(json.dumps(report),flush=True);return report

def main():
 if not (ROOT/'baseline.json').exists():
  p=load(PARENT/'catalog.json');t=load(TACZ/'catalog.json');assert len(p['items'])==2417 and len(t['items'])==213
  save(ROOT/'baseline.json',{'parent':{x['id']:dh(x) for x in p['items']},'tacz':{x['id']:dh({k:v for k,v in x.items() if k!='popularityRank'}) for x in t['items']},'parentDataHash':p['build']['dataHash'],'taczDataHash':t['build']['dataHash']})
 patch_owner();owner=module('community_canonical_owner',PARENT/'creator-discoveries/build_update.py');owner.refresh();proof()
 paths=[PARENT/'catalog.json',TACZ/'catalog.json',PARENT/'app.js',TACZ/'app.js',PARENT/'index.html',TACZ/'index.html',DOCS/(PAGE+'.md')];before={str(p):fh(p) for p in paths};owner.refresh();assert all(fh(Path(p))==h for p,h in before.items()),'Non-idempotent community update'
 save(ROOT/'qa/idempotence.json',{'passed':True,'paths':before,'canonicalUpdate':'creator-discoveries/build_update.py refresh','oldRecordsUnchanged':True})
if __name__=='__main__':main()
