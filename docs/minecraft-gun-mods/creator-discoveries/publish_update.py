#!/usr/bin/env python3
"""Publish and verify the additive creator update and organized inspiration hierarchy."""
from __future__ import annotations
import argparse,hashlib,json,re,shutil,sys,zipfile
from pathlib import Path
import requests
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;DOCS=PARENT.parent
sys.path.insert(0,str(DOCS))
import weapon_inspiration_navigation as nav
SITE='https://herbertofury.github.io/Advent-of-Ascension/minecraft-gun-mods/'
WIKI='https://github.com/Herbertofury/Advent-of-Ascension/wiki/'
RAW='https://raw.githubusercontent.com/wiki/Herbertofury/Advent-of-Ascension/'

def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def browser(pw):
    opts={'headless':True,'args':['--no-sandbox','--disable-dev-shm-usage']};exe=shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
    if exe:opts['executable_path']=exe
    return pw.chromium.launch(**opts)

def prepare(wiki):
    wiki=Path(wiki);manifest=load(PARENT/'wiki-manifest.json')
    publish={p['name']+'.md' for p in manifest['pages']}|{'TaCZ-Gunpacks.md','Minecraft-Gunpack-Creator-Discoveries.md'}
    allowed=publish|set(nav.TARGETS)
    before={p.name:digest(p) for p in wiki.glob('*.md') if p.name not in allowed}
    for name in publish:shutil.copyfile(DOCS/name,wiki/name)
    nav.apply(wiki)
    assert not nav.apply(wiki)['changedPages'],'Navigation not idempotent'
    assert all(digest(wiki/name)==sha for name,sha in before.items())
    for name in publish|{'Weapon-Inspirations.md','Weapon-Reference-Library.md'}:
        shutil.copyfile(wiki/name,DOCS/name)
    actual={name:digest(wiki/name) for name in allowed if (wiki/name).exists()}
    save(ROOT/'qa/wiki-publication-source.json',{'pages':actual,'unrelatedPagesPreserved':len(before),'unrelatedHashes':before,'duplicateHubChildren':0})
    for page in manifest['pages']:
        p=DOCS/(page['name']+'.md');page.update(bytes=p.stat().st_size,sha256=digest(p))
    save(PARENT/'wiki-manifest.json',manifest)
    print(json.dumps({'publishedPages':len(actual),'unrelatedPagesPreserved':len(before),'idempotent':True}),flush=True)

def verify(wiki):
    wiki=Path(wiki);out=ROOT/'qa/live';out.mkdir(parents=True,exist_ok=True)
    expected=load(ROOT/'qa/wiki-publication-source.json');report={'rawWiki':[],'navigation':{},'renderedPages':[],'explorers':[]}
    session=requests.Session();session.headers['User-Agent']='AoA-Creator-Discovery-Verification/1.0'
    for name,sha in expected['pages'].items():
        response=session.get(RAW+name,timeout=40);actual=hashlib.sha256(response.content).hexdigest();ok=response.ok and actual==sha
        report['rawWiki'].append({'page':name,'status':response.status_code,'sha256':actual,'matchesSource':ok});save(out/'publication.json',report)
        assert ok,(name,response.status_code,actual,sha)
    with sync_playwright() as pw:
        b=browser(pw);p=b.new_page(viewport={'width':1500,'height':1100})
        p.goto(WIKI+'Weapon-Inspirations',wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for()
        headings=p.locator('h3').filter(has_text=re.compile('^Weapon inspirations$'))
        assert headings.count()==1,{'headingCount':headings.count(),'headings':p.locator('h3').all_text_contents()}
        heading=headings.first;heading.scroll_into_view_if_needed()
        state=heading.evaluate("h=>{const w=h.parentElement.classList.contains('markdown-heading')?h.parentElement:h;const list=w.nextElementSibling;return {tag:list?.tagName,text:list?.innerText,nested:list?.querySelectorAll('ul').length,links:[...list.querySelectorAll('a')].map(x=>({text:x.textContent,url:x.href}))};}")
        assert state['tag']=='UL' and state['nested']==0,state
        assert not any(x['url'].endswith('/wiki/Weapon-Inspirations') for x in state['links'])
        assert len(state['links'])==len({x['url'] for x in state['links']})
        report['navigation']={'oneHeading':True,'recursiveChildLinks':0,'nestedLists':0,'links':state['links']}
        p.screenshot(path=str(out/'organized-sidebar.png'))
        p.locator('#wiki-body').screenshot(path=str(out/'organized-hub.png'))
        tacz=load(PARENT/'tacz/catalog.json');new=load(ROOT/'manifest.json')['newTaCZ']
        for slug,items,end in [('TaCZ-Gunpacks',tacz['items'],'End of gunpack gallery'),('Minecraft-Gunpack-Creator-Discoveries',new,'End of creator discoveries')]:
            p.goto(WIKI+slug,wait_until='domcontentloaded',timeout=90000);p.locator('#wiki-body').wait_for()
            p.evaluate("()=>document.querySelectorAll('#wiki-body img').forEach(x=>x.loading='eager')")
            p.wait_for_function("()=>[...document.querySelectorAll('#wiki-body img')].every(x=>x.complete)",timeout=180000)
            result=p.evaluate("()=>{const w=document.querySelector('#wiki-body');const a=[...w.querySelectorAll('img')];return {text:w.innerText,images:a.length,broken:a.filter(x=>!x.naturalWidth).map(x=>x.alt),links:[...w.querySelectorAll('a')].map(x=>x.href)};}")
            missing=[x['id'] for x in items if not any('?item='+x['id'] in u for u in result['links'])]
            record={'page':slug,'images':result['images'],'broken':result['broken'],'missingIds':missing,'endMarker':end in result['text']}
            assert not missing and not record['broken'] and record['endMarker'],record
            assert record['images']==len(items),record
            report['renderedPages'].append(record)
            p.locator('#wiki-body').screenshot(path=str(out/(slug+'.png')))
        for suffix,data in [('',load(PARENT/'catalog.json')),('tacz/',tacz)]:
            response=p.goto(SITE+suffix,wait_until='domcontentloaded',timeout=90000);assert response and response.status==200
            p.wait_for_function('window.ATLAS_TEST',timeout=60000)
            got=p.evaluate('({count:GUN_ATLAS.items.length,hash:GUN_ATLAS.build.dataHash})')
            assert got=={'count':len(data['items']),'hash':data['build']['dataHash']},(suffix,got)
            p.locator('[data-creator-preset="new"]').click();count=4 if suffix else 5;assert p.locator('.project-card').count()==count
            p.evaluate("()=>document.querySelectorAll('.project-card img').forEach(x=>x.loading='eager')");p.wait_for_function("()=>[...document.querySelectorAll('.project-card img')].every(x=>x.complete)")
            broken=p.locator('.project-card img').evaluate_all('(a)=>a.filter(x=>!x.naturalWidth).map(x=>x.alt)');assert not broken,broken
            p.screenshot(path=str(out/('tacz-discoveries.png' if suffix else 'atlas-discoveries.png')))
            report['explorers'].append({'path':suffix,**got,'newDiscoveryCount':count,'brokenNewImages':broken})
        b.close()
    report['passed']=True;save(out/'publication.json',report);print(json.dumps(report),flush=True)

def package(directory):
    directory=Path(directory).resolve();directory.mkdir(parents=True,exist_ok=True)
    files={};skip={'cache','research-cache','fixtures','__pycache__','visual-review'}
    for p in PARENT.rglob('*'):
        rel=p.relative_to(PARENT)
        if not p.is_file() or any(part in skip for part in rel.parts):continue
        if p.name in {'raw-projects.json','export.json','export.csv','collection.json'}:continue
        files['minecraft-gun-mods/'+rel.as_posix()]=p
    files['weapon_inspiration_navigation.py']=DOCS/'weapon_inspiration_navigation.py'
    for p in DOCS.glob('Minecraft-Gun*.md'):files['wiki/'+p.name]=p
    for name in ('TaCZ-Gunpacks.md','Weapon-Inspirations.md','Weapon-Reference-Library.md'):files['wiki/'+name]=DOCS/name
    for folder in (PARENT,PARENT/'tacz'):
        for item in load(folder/'catalog.json')['items']:
            for media in item.get('media',[]):
                p=(folder/media['src']).resolve();assert p.is_file(),p
                assert 'minecraft-gun-mods/'+p.relative_to(PARENT.resolve()).as_posix() in files
                assert digest(p)==media['sha256'],media['src']
    intro='# Minecraft Gun Atlas\n\nExtract this ZIP and open `minecraft-gun-mods/index.html` or `minecraft-gun-mods/tacz/index.html`. Both work offline without a local server.\n\nThis release includes the complete 2,367-project atlas, 160-family TaCZ collection, every archived source image, creator-access evidence, source scripts and organized wiki pages.\n\nLive atlas: '+SITE+'\nTaCZ collection: '+SITE+'tacz/\nDiscoveries: '+WIKI+'Minecraft-Gunpack-Creator-Discoveries\n\nUse Back up my collection to transfer favorites, notes, private ratings and saved views. Hosted and file:// copies have separate browser origins. Nothing silently changes your installed Minecraft mods.\n\nThe paid Bedrock AEG-Tactical reference has an explicit source-only preview fallback because its public image token could not be retrieved. No paid or private mod binaries are included.\n'
    path=directory/'Minecraft-Gun-Atlas.zip'
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for name,p in sorted(files.items()):z.write(p,name)
        z.writestr('START-HERE.md',intro)
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        for name,p in files.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest(p),name
    receipt={'archive':path.name,'bytes':path.stat().st_size,'sha256':digest(path),'files':len(files)+1,'parentProjects':len(load(PARENT/'catalog.json')['items']),'taczFamilies':len(load(PARENT/'tacz/catalog.json')['items']),'completeReferencedMedia':True}
    save(directory/'RELEASE-VERIFICATION.json',receipt);(directory/'SHA256SUMS.txt').write_text(receipt['sha256']+'  '+path.name+'\n');(directory/'START-HERE.md').write_text(intro)
    print(json.dumps(receipt),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['prepare','verify','package']);p.add_argument('target');a=p.parse_args()
    {'prepare':prepare,'verify':verify,'package':package}[a.action](a.target)
