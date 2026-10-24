#!/usr/bin/env python3
"""Add source-qualified discoveries and make every inspiration publisher share navigation."""
from __future__ import annotations
import argparse, ast, collections, copy, hashlib, html, importlib.util, json, re, shutil, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent;REPO=DOCS.parent;TACZ=PARENT/'tacz'
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/Herbertofury/Advent-of-Ascension/main/docs/minecraft-gun-mods/'
sys.path[:0]=[str(PARENT),str(DOCS),str(TACZ)]

def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
def dh(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def md(s):
    s=html.escape(str(s or '')).replace('|','&#124;').replace('\n',' ')
    for ch in '*_`[]~':s=s.replace(ch,'&#'+str(ord(ch))+';')
    return s

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def save_catalog(path,data):
    data['build']['itemCount']=len(data['items']);data['build']['dataHash']=dh(data['items'])
    data['build']['lastDelta']='creator-discoveries 2026-10-23'
    data['coverage']['publishedProjects']=len(data['items'])
    if 'qualifiedProjects' in data['coverage']:data['coverage']['qualifiedProjects']=len(data['items'])
    data['coverage']['mediaProjects']=sum(bool(x.get('media')) for x in data['items'])
    data['coverage']['directVideoProjects']=sum(bool(x.get('videos')) for x in data['items'])
    if 'types' in data['coverage']:data['coverage']['types']=dict(collections.Counter(x['type'] for x in data['items']))
    if 'editions' in data['coverage']:data['coverage']['editions']=dict(collections.Counter(x['edition'] for x in data['items']))
    save(path,data)
    path.with_suffix('.js').write_text('window.GUN_ATLAS='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')

def tacz_record(item,snapshot):
    x=copy.deepcopy(item)
    for m in x['media']:m['src']='../'+m['src']
    metric={k:snapshot.get(k) for k in ('id','provider','url','downloads','favorites','followers','rating','ratingCount','checkedAt','sourceHash')}
    downloads=metric['downloads']
    x.update(metricSources=[metric],contentSources=[{'url':item['projectUrl'],'summary':item['summary'],'features':{},'checkedAt':item['checkedAt']}],variants=[{'id':x['id'],'name':x['name'],'url':x['projectUrl']}],aliases=[],familyIds=[x['id']],maintenance='No discontinuation notice found',historicalDownloadsMixed=False,metrics={'downloads':downloads,'cfDownloads':downloads,'mrDownloads':None,'favorites':metric['favorites'],'followers':None,'communityRating':None,'downloadSource':'CurseForge'},metricFreshness='Current source read',activity='Current / no discontinuation notice',curation='Research discovery',studyPriority=50,qualityReason=item['inspiration'][0],type='Gunpack (ZIP)',qualitySignals=['Creator imagery available']+(['Creator-linked footage'] if item['videos'] else []))
    x['cautions']=list(dict.fromkeys(x['cautions']+['Requires the exact TaCZ runtime and any additional dependencies named by the creator.']))
    return x

def apply_data():
    manifest=load(ROOT/'manifest.json');qualified=load(ROOT/'qualified-records.json');snapshots=load(ROOT/'metric-snapshots.json');channels=load(ROOT/'channel-evidence.json')
    parent=load(PARENT/'catalog.json');tacz=load(TACZ/'catalog.json')
    baseline_path=ROOT/'baseline.json'
    if not baseline_path.exists():save(baseline_path,{'parent':{x['id']:dh(x) for x in parent['items']},'tacz':{x['id']:dh({k:v for k,v in x.items() if k!='popularityRank'}) for x in tacz['items']},'parentCount':len(parent['items']),'taczCount':len(tacz['items'])})
    before=load(baseline_path);pidx={x['id']:x for x in parent['items']};tidx={x['id']:x for x in tacz['items']}
    expected_new={x['id'] for x in manifest['newTaCZ']}
    for key,item in qualified.items():
        if key not in pidx:pidx[key]=copy.deepcopy(item)
        if key in expected_new and key not in tidx:tidx[key]=tacz_record(item,snapshots[key])
    enriched=set()
    for spec in channels.values():
        for key in spec['ids']:
            for idx in (pidx,tidx):
                if key not in idx:continue
                x=idx[key];x['access']=spec['access'];x['accessEvidence']=spec['source'];x['creatorAccessNote']=spec['note']
                x['links']=list({v['url']:v for v in x.get('links',[])+spec['links']}.values())
                x['themes']=list(dict.fromkeys(x.get('themes',[])+['Creator channels']))
                enriched.add(key)
    # Deep-discovery overlay: keep later accepted content through every original rebuild.
    deep_ids=set()
    _deep_path=PARENT/'tacz-deep-discovery/build_deep.py'
    if _deep_path.exists() and (_deep_path.parent/'qualified-records.json').exists():
        _deep=module('deep_discovery_overlay',_deep_path);deep_ids=_deep.extend(pidx,tidx)
    # Creator-frontier overlay: retain qualified creator/source packs through normal rebuilds.
    frontier_ids=set()
    _frontier_path=PARENT/'tacz-frontier/build_frontier.py'
    if _frontier_path.exists() and (_frontier_path.parent/'qualified-records.json').exists():
        frontier_ids=module('creator_frontier_records',_frontier_path).extend(pidx,tidx)
    parent['items']=sorted(pidx.values(),key=lambda x:(-x['studyPriority'],-(x['downloads'] or 0),x['name'].lower()))
    parent['coverage']['creatorDiscoveryDelta']={'newGunpacks':4,'newBedrockReference':1,'existingCreatorGroups':len(channels)}
    parent['sources']=[s for s in parent['sources'] if s.get('role')!='Creator discoveries']+[{'provider':'Creator-controlled project and Patreon pages','role':'Creator discoveries','url':WIKI+'Minecraft-Gunpack-Creator-Discoveries','checkedAt':manifest['checkedDate']}]
    save_catalog(PARENT/'catalog.json',parent)
    tacz['items']=sorted(tidx.values(),key=lambda x:(-(x['metrics']['downloads'] if x['metrics']['downloads'] is not None else -1),x['name'].lower()))
    for n,x in enumerate(tacz['items'],1):x['popularityRank']=n
    tacz['build']['parentDataHash']=parent['build']['dataHash']
    for src in tacz['sources']:
        if src.get('provider')=='Minecraft Gun Atlas':src['dataHash']=parent['build']['dataHash']
    tacz['coverage']['creatorDiscoveryDelta']={'newGunpacks':4,'paidNonTaCZEntries':0}
    save_catalog(TACZ/'catalog.json',tacz)
    assert set(before['parent'])<=set(pidx) and set(before['tacz'])<=set(tidx)
    parent_changed=[key for key,sha in before['parent'].items() if dh(pidx[key])!=sha]
    tacz_changed=[key for key,sha in before['tacz'].items() if dh({k:v for k,v in tidx[key].items() if k!='popularityRank'})!=sha]
    assert set(parent_changed)<=enriched|deep_ids|frontier_ids,parent_changed
    assert set(tacz_changed)<=enriched|deep_ids|frontier_ids,tacz_changed
    assert set(pidx)==set(before['parent'])|set(qualified)|deep_ids|frontier_ids
    assert set(tidx)==set(before['tacz'])|expected_new|deep_ids|frontier_ids
    assert manifest['paidReference']['id'] not in tidx
    proof={'parentCount':len(pidx),'taczFamilies':len(tidx),'newTaCZ':sorted(expected_new),'newBedrock':manifest['paidReference']['id'],'existingCreatorGroupsEnriched':len(channels),'changedExistingParentIds':parent_changed,'changedExistingTaCZIds':tacz_changed,'allExistingIdsPreserved':True,'unrelatedItemBytesPreserved':True,'parentDataHash':parent['build']['dataHash'],'taczDataHash':tacz['build']['dataHash']}
    save(ROOT/'qa/data-delta.json',proof)
    return parent,tacz

def update_ui():
    for folder in (PARENT,TACZ):
        html_path=folder/'index.html';body=html_path.read_text()
        if 'id="creatorDiscoveriesLink"' not in body:
            body=body.replace('<nav aria-label="Main navigation">','<nav aria-label="Main navigation"><a id="creatorDiscoveriesLink" href="'+WIKI+'Minecraft-Gunpack-Creator-Discoveries">Creator discoveries</a>')
        if 'data-creator-preset="new"' not in body:
            body=body.replace('<div class="preset-row" aria-label="Quick filters">','<div class="preset-row" aria-label="Quick filters"><button data-creator-preset="new">New discoveries</button><button data-creator-preset="channels">Creator channels</button>')
        if folder==PARENT and 'href="tacz/"' not in body:body=body.replace('<nav aria-label="Main navigation">','<nav aria-label="Main navigation"><a href="tacz/">TaCZ gunpacks</a>')
        html_path.write_text(body,encoding='utf-8')
        js_path=folder/'app.js';js=js_path.read_text()
        if 'function creatorAccess(x)' not in js:
            at='function card(x)'
            helper='function creatorAccess(x){return x.access?`<div class="creator-access"><strong>${esc(x.access)}</strong>${x.creatorAccessNote?`<p>${esc(x.creatorAccessNote)}</p>`:\'\'}</div>`:\'\';}\n'
            assert at in js;js=js.replace(at,helper+at,1)
            js=js.replace('<p class="card-summary">${esc(x.summary)}</p>','<p class="card-summary">${esc(x.summary)}</p>${creatorAccess(x)}')
            js=js.replace('<h3>What this project brings</h3>','${creatorAccess(x)}<h3>What this project brings</h3>')
            js=js.replace("${esc(l.verified?'Project metadata checked':l.verification||'Linked by source author')}","${esc(l.kind==='creator-channel'?l.verification||'Creator-linked channel':l.verified?'Project metadata checked':l.verification||'Linked by source author')}")
            js=js.replace("const commas=n=>Number(n||0).toLocaleString('en-US');","const commas=n=>n===null||n===undefined?'Not published':Number(n).toLocaleString('en-US');")
            hook="document.addEventListener('click',event=>{const b=event.target.closest('[data-creator-preset]');if(!b)return;state={...DEFAULTS,view:state.view,theme:b.dataset.creatorPreset==='new'?'New discoveries':'Creator channels'};syncControls();render();});\n"
            js=js.replace('renderSavedViews();syncControls();render();',hook+'renderSavedViews();syncControls();render();')
        js_path.write_text(js,encoding='utf-8')
        css_path=folder/'app.css';css=css_path.read_text()
        if '/* Creator access badges */' not in css:css+='\n/* Creator access badges */\n.creator-access{margin:.75rem 0;padding:.65rem .8rem;border:1px solid var(--line);border-radius:10px;font-size:.78rem;line-height:1.5;background:var(--surface)}.creator-access p{margin:.3rem 0 0;font-weight:400}.card-body .creator-access p{display:none}\n'
        css_path.write_text(css,encoding='utf-8')

def discoveries_page(parent,tacz):
    spec=load(ROOT/'manifest.json');idx={x['id']:x for x in parent['items']};tidx={x['id']:x for x in tacz['items']}
    lines=['# Creator-hosted discoveries','', '[Weapon inspirations](Weapon-Inspirations) / **Creator-hosted discoveries**','',
      '**Four newly added TaCZ gunpacks, one separately labeled paid Bedrock reference, and verified creator channels for existing favorites.**','',
      '[Browse new Minecraft discoveries]('+SITE+'?theme=New+discoveries) · [Browse new TaCZ packs]('+SITE+'tacz/?theme=New+discoveries) · [Creator channels]('+SITE+'?theme=Creator+channels)','',
      '## Free public TaCZ packs','',
      'These are new additions to this research library, not claims of newly released software. Each entry keeps the actual file date, original creator links and version evidence.','',
      '| Embedded creator reference | Gunpack and why it stands out | Access and source |','|---|---|---|']
    def image(x):
        m=next((m for m in x.get('media',[]) if m['role']!='Project icon'),next(iter(x.get('media',[])),None))
        return '<img src="'+RAW+m['src']+'?v='+m['sha256'][:8]+'" width="240" alt="'+md(x['name'])+'"><br><sub>'+md(m['role'])+'</sub>' if m else 'Public preview not archived; use the exact creator source.'
    for s in spec['newTaCZ']:
        x=idx[s['id']];date=(x.get('latest') or {}).get('date','')[:10] or 'Not established'
        lines+=['| '+image(x)+' | **['+md(s['label'])+']('+SITE+'tacz/?item='+x['id']+')**<br>'+md(s['summary'])+'<br>'+md(s['idea'])+' | **'+md(s['access'])+'**<br>Latest fetched file: '+date+'<br>[Creator project]('+x['projectUrl']+')<br>'+md(s['caution'])+' |']
    paid=idx[spec['paidReference']['id']]
    lines+=['','## Paid creator-hosted reference: Bedrock, not TaCZ','',image(paid),'',
      '**[AEG-Tactical]('+paid['projectUrl']+') by Fission_Track Studio.** '+md(paid['summary']),'',
      '**'+md(paid['access'])+'.** '+md(paid['cautions'][1])+' '+md(paid['cautions'][2]),'',
      'The creator marks a pictured Barrett as future content; it is not presented here as an included firearm. Prices and access can change, so the listing links to the original purchase page rather than quoting an expired promotion.','',
      '[Open in Minecraft Gun Atlas]('+SITE+'?item='+paid['id']+') · [Exact public creator post]('+paid['projectUrl']+')','',
      '## Creator channels for packs already in the library','',
      'These links enrich existing entries. They are not counted as extra gunpacks, and optional support is not mislabeled as a required paid download.','',
      '| Existing pack | What the creator channel offers | Exact source links |','|---|---|---|']
    channels=load(ROOT/'channel-evidence.json')
    for s in channels.values():
        x=next((idx[k] for k in s['ids'] if k in idx),None) or next((tidx[k] for k in s['ids'] if k in tidx),None)
        assert x,s['label']
        links=' · '.join('['+md(a['provider'])+']('+a['url']+')' for a in s['links'])
        lines+=['| **'+md(s['label'])+'** | **'+md(s['access'])+'**<br>'+md(s['note'])+' | [Source]('+s['source']+')'+('<br>'+links if links else '')+' |']
    lines+=['','## Evidence and access','',
      'Only public creator descriptions, project files metadata and public previews were inspected. No purchase was made and no private attachment or mod binary was downloaded. Source claims about animation, compatibility or performance are not independent Minecraft runtime tests.','',
      '[Discovery evidence and update source](https://github.com/Herbertofury/Advent-of-Ascension/tree/main/docs/minecraft-gun-mods/creator-discoveries) · [All Minecraft gun mods](Minecraft-Gun-Mod-Inspirations) · [TaCZ rankings](TaCZ-Gunpacks)','',
      '## End of creator discoveries','']
    (DOCS/'Minecraft-Gunpack-Creator-Discoveries.md').write_text('\n'.join(lines),encoding='utf-8')

def refresh():
    parent,tacz=apply_data()
    build=module('atlas_build_current',PARENT/'build.py');proof=build.validate(parent);build.make_wiki(parent,proof)
    tbuild=module('tacz_build_current',TACZ/'build_ui.py');tbuild.wiki_build(tacz)
    discoveries_page(parent,tacz);update_ui()
    _deep_path=PARENT/'tacz-deep-discovery/build_deep.py'
    if _deep_path.exists() and (_deep_path.parent/'qualified-records.json').exists():
        module('deep_discovery_publication',_deep_path).finish(parent,tacz)
    _frontier_path=PARENT/'tacz-frontier/build_frontier.py'
    if _frontier_path.exists() and (_frontier_path.parent/'qualified-records.json').exists():
        module('creator_frontier_publication',_frontier_path).finish(parent,tacz)
    return parent,tacz

NAV_LOAD="""    import importlib.util
    _nav_path=Path(__file__).resolve().parent{parents}/'weapon_inspiration_navigation.py'
    if not _nav_path.exists():
        import subprocess
        _source=subprocess.run(['git','show','HEAD:docs/weapon_inspiration_navigation.py'],cwd=_nav_path.parent.parent,check=True,capture_output=True).stdout
        _nav_path.write_bytes(_source)
    _nav_spec=importlib.util.spec_from_file_location('weapon_nav_shared',_nav_path)
    _nav=importlib.util.module_from_spec(_nav_spec);_nav_spec.loader.exec_module(_nav)
    _nav.apply({wiki})
"""

def replace_function(path,name,new):
    text=path.read_text();tree=ast.parse(text);node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
    lines=text.splitlines(True);text=''.join(lines[:node.lineno-1])+new.rstrip()+'\n\n'+''.join(lines[node.end_lineno:]);ast.parse(text);path.write_text(text,encoding='utf-8')

def patch_publishers():
    path=PARENT/'build.py'
    body="""def publish(wiki_path):
    wiki=Path(wiki_path);manifest=json.loads((ROOT/'wiki-manifest.json').read_text())
    for page in manifest['pages']:
        name=page['name']+'.md';(wiki/name).write_bytes((DOCS/name).read_bytes())
    extra=DOCS/'Minecraft-Gunpack-Creator-Discoveries.md'
    if extra.exists():(wiki/extra.name).write_bytes(extra.read_bytes())
"""+NAV_LOAD.format(parents='.parent',wiki='wiki')+"""    for name in ('Weapon-Inspirations.md','Weapon-Reference-Library.md','Minecraft-Gun-Mod-Inspirations.md'):
        if (wiki/name).exists():(DOCS/name).write_bytes((wiki/name).read_bytes())
    print('Published one canonical Weapon Inspirations hierarchy',flush=True)
"""
    replace_function(path,'publish',body)
    path=TACZ/'publish_tacz.py'
    body="""def prepare(wiki):
    wiki=Path(wiki)
    allowed={'TaCZ-Gunpacks.md','Weapon-Inspirations.md','Minecraft-Gun-Mod-Inspirations.md','Weapon-Reference-Library.md','_Sidebar.md','Home.md','Minecraft-Gunpack-Creator-Discoveries.md'}
    before={p.name:digest(p) for p in wiki.glob('*.md') if p.name not in allowed}
    shutil.copyfile(DOCS/'TaCZ-Gunpacks.md',wiki/'TaCZ-Gunpacks.md')
    extra=DOCS/'Minecraft-Gunpack-Creator-Discoveries.md'
    if extra.exists():shutil.copyfile(extra,wiki/extra.name)
"""+NAV_LOAD.format(parents='.parent.parent',wiki='wiki')+"""    assert all(digest(wiki/name)==sha for name,sha in before.items())
    save(ROOT/'qa/preserved-wiki.json',{'unchangedPages':len(before),'sha256':before})
    print('Wiki prepared with shared navigation',flush=True)
"""
    replace_function(path,'prepare',body)
    historical=DOCS/'weapon-inspirations/build_galleries.py'
    body="""def publish(wiki):
    wiki=Path(wiki)
    for page in PAGES:
        source=DOCS/(page+'.md');assert source.exists();shutil.copyfile(source,wiki/source.name)
"""+NAV_LOAD.format(parents='.parent',wiki='wiki')+"    print('Prepared galleries with shared navigation',flush=True)\n"
    replace_function(historical,'publish',body)
    expand=DOCS/'weapon-inspirations/expand_research.py'
    if expand.exists():
        text=expand.read_text();a=text.find(" marker='<!-- additional-weapon-research:start -->'")
        if a>=0:
            b=text.index(" run_git('config','user.name'",a)
            hook=NAV_LOAD.format(parents='.parent',wiki='wiki');hook='\n'.join(' '+line[4:] if line.startswith('    ') else line for line in hook.splitlines())+'\n'
            text=text[:a]+hook+text[b:];ast.parse(text);expand.write_text(text)
    for path,needle in [(PARENT/'build.py'," print(json.dumps(proof,indent=2),flush=True)"),(TACZ/'build_tacz.py',"   polish_tacz.main()")]:
        text=path.read_text()
        if 'creator_delta_refresh' not in text:
            indent=' ' if path.parent==PARENT else '  '
            root_expr="ROOT/'creator-discoveries/build_update.py'" if path.parent==PARENT else "ROOT.parent/'creator-discoveries/build_update.py'"
            hook=indent+"# creator_delta_refresh: preserve canonical creator discoveries on rebuild\n"+indent+"import importlib.util as _iu\n"+indent+"_delta="+root_expr+"\n"+indent+"if _delta.exists():\n"+indent+" _spec=_iu.spec_from_file_location('creator_delta_update',_delta);_module=_iu.module_from_spec(_spec);_spec.loader.exec_module(_module);_module.refresh()\n"
            assert needle in text,(path,'hook owner changed')
            text=text.replace(needle,needle+'\n'+hook,1);ast.parse(text);path.write_text(text)
    # Workflow mutation is deliberately outside the content-only CI authority.
    # The connector updated the one inline publisher; module publishers use exact Git HEAD.
    workflow=REPO/'.github/workflows/publish-weapon-inspirations.yml'
    if workflow.exists():
        assert 'python3 source/weapon_inspiration_navigation.py wiki' in workflow.read_text(), 'Inline publisher still has a separate menu owner'
    save(ROOT/'qa/publisher-owner-proof.json',{'sharedOwner':'docs/weapon_inspiration_navigation.py','modulePublishers':['minecraft-gun-mods/build.py:publish','minecraft-gun-mods/tacz/publish_tacz.py:prepare','weapon-inspirations/build_galleries.py:publish','weapon-inspirations/expand_research.py:persist_and_publish'],'workflowFilesChangedByBuilder':[],'sharedModuleFromExactGitHead':True,'oldAppendOwnersReplaced':True})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--wiki');args=parser.parse_args()
    refresh();patch_publishers()
    if args.wiki:
        wiki=Path(args.wiki);manifest=load(PARENT/'wiki-manifest.json')
        for entry in manifest['pages']:
            name=entry['name']+'.md';shutil.copyfile(DOCS/name,wiki/name)
        for name in ('TaCZ-Gunpacks.md','Minecraft-Gunpack-Creator-Discoveries.md'):shutil.copyfile(DOCS/name,wiki/name)
        nav=module('navigation_final',DOCS/'weapon_inspiration_navigation.py');proof=nav.apply(wiki,ROOT/'qa/navigation-proof.json');assert not nav.apply(wiki)['changedPages']
        for name in nav.TARGETS:
            if name not in ('Home.md','_Sidebar.md') and (wiki/name).exists():shutil.copyfile(wiki/name,DOCS/name)
        (ROOT/'qa/sidebar.md').write_bytes((wiki/'_Sidebar.md').read_bytes());(ROOT/'qa/hub.md').write_bytes((wiki/'Weapon-Inspirations.md').read_bytes())
    print(json.dumps(load(ROOT/'qa/data-delta.json'),indent=2),flush=True)
if __name__=='__main__':main()
