#!/usr/bin/env python3
"""One idempotent navigation owner for the weapon inspiration collections."""
from pathlib import Path
import argparse, hashlib, json, re
SITE='https://herbertofury.github.io/Advent-of-Ascension/'
START='<!-- weapon-inspirations-navigation:start -->'
END='<!-- weapon-inspirations-navigation:end -->'
LEGACY=('weapon-inspirations','minecraft-gun-inspirations','tacz-gunpack-lab','additional-weapon-research','weapon-inspirations-navigation')
TARGETS=('Home.md','_Sidebar.md','Weapon-Inspirations.md','Weapon-Reference-Library.md','Minecraft-Gun-Mod-Inspirations.md')

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def strip_managed(text):
    """Remove only publisher-owned blocks, including previously nested blocks."""
    for name in LEGACY:
        pattern=re.compile(r'<!--\s*'+re.escape(name)+r':start\s*-->.*?<!--\s*'+re.escape(name)+r':end\s*-->',re.S)
        text=pattern.sub('',text)
    return re.sub(r'\n{4,}','\n\n\n',text).rstrip()

def records(wiki):
    candidates=[
      ('Video-game weapons','Video-Game-Weapon-Inspirations','Iconic guns, unusual projectiles and animated weapon ideas.'),
      ('More gaming references','Video-Game-Weapon-Inspirations-Volume-2','The continuation of the gaming-history collection.'),
      ('Historical & experimental guns','Historical-and-Experimental-Gun-Inspirations','Unconventional real-world silhouettes and operating motions.'),
      ('Minecraft gun mods','Minecraft-Gun-Mod-Inspirations','Gun engines, content packs, artillery and integrations, clearly separated.'),
      ('TaCZ gunpacks','TaCZ-Gunpacks','Only packs that add guns, with separate popularity and quality views.'),
      ('Creator-hosted discoveries','Minecraft-Gunpack-Creator-Discoveries','Overlooked packs and verified creator channels, including paid or early-access releases.')]
    return [x for x in candidates if (wiki/(x[1]+'.md')).exists()]

def navigation(wiki,kind):
    available={slug for _,slug,_ in records(wiki)}
    if kind=='sidebar':
        lines=[START,'### [Weapon inspirations](Weapon-Inspirations)','',
          '- [Gaming weapons](Video-Game-Weapon-Inspirations)'+(' · [Volume 2](Video-Game-Weapon-Inspirations-Volume-2)' if 'Video-Game-Weapon-Inspirations-Volume-2' in available else ''),
          '- [Historical & experimental guns](Historical-and-Experimental-Gun-Inspirations)',
          '- [Minecraft gun mods](Minecraft-Gun-Mod-Inspirations) · [Explore]('+SITE+'minecraft-gun-mods/)',
          '- [TaCZ gunpacks](TaCZ-Gunpacks) · [Rankings]('+SITE+'minecraft-gun-mods/tacz/)']
        if 'Minecraft-Gunpack-Creator-Discoveries' in available: lines+=['- [Creator-hosted discoveries](Minecraft-Gunpack-Creator-Discoveries)']
        return '\n'.join(lines+['',END])
    lines=[START,'## [Weapon inspirations](Weapon-Inspirations)','',
      '| Collection | Browse |','|---|---|']
    for title,slug,desc in records(wiki):
        link='[Illustrated collection]('+slug+')'
        if slug=='Minecraft-Gun-Mod-Inspirations': link='[Wiki]('+slug+') · [Interactive atlas]('+SITE+'minecraft-gun-mods/)'
        if slug=='TaCZ-Gunpacks': link='[Wiki]('+slug+') · [Ranked explorer]('+SITE+'minecraft-gun-mods/tacz/)'
        lines+=['| '+title+' | '+link+' |']
    return '\n'.join(lines+['',END])

def hub(wiki,old):
    lines=['# Weapon inspirations','',
      'A single starting point for weapon design references, Minecraft gun content and creator-hosted discoveries. Original concepts and research are kept separate from implemented AoA features.','',
      '**[Minecraft Gun Atlas]('+SITE+'minecraft-gun-mods/)** · **[TaCZ Gunpack Lab]('+SITE+'minecraft-gun-mods/tacz/)** · [Ascension Armory](Weapon-Overhaul)','',
      '## Choose a collection','',
      '| Collection | What you will find |','|---|---|']
    for title,slug,desc in records(wiki):lines+=['| **['+title+']('+slug+')** | '+desc+' |']
    lines+=['','## Browse, compare and save','',
      'Use the interactive explorers for image galleries, precise version and loader filters, favorites, private notes and comparisons. The TaCZ page also separates downloads, CurseForge favorites, Modrinth followers and your personal ratings.','',
      'Use the illustrated wiki collections for reading and following source references. Creator-hosted releases are labeled as free, supporter-only, paid or access-unconfirmed rather than mixed into a misleading download ranking.','',
      '## Research and provenance','',
      '- [Original weapon reference library](Weapon-Reference-Library)',
      '- [Historical and gaming media sources](Weapon-Inspiration-Media-Sources)',
      '- [Additional gaming media sources](Weapon-Inspiration-Media-Sources-Expansion)',
      '- [Minecraft project and release evidence](Minecraft-Gun-Mod-Inspirations-Sources)','',
      'External references are inspiration, not a claim of in-game implementation or tested cross-mod compatibility.','']
    known={'Weapon-Inspirations','Weapon-Overhaul','Weapon-Reference-Library','Weapon-Inspiration-Media-Sources','Weapon-Inspiration-Media-Sources-Expansion','Minecraft-Gun-Mod-Inspirations-Sources'}|{x[1] for x in records(wiki)}
    extra=[]
    for title,url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',strip_managed(old)):
        if url.split('#')[0] in known or url.startswith(SITE):continue
        if (title,url) not in extra:extra.append((title,url))
    if extra:lines+=['## Additional references','']+['- ['+title+']('+url+')' for title,url in extra]+['']
    return '\n'.join(lines)

def apply(wiki_path,report_path=None):
    wiki=Path(wiki_path)
    assert (wiki/'Home.md').exists() and (wiki/'_Sidebar.md').exists(), 'Wrong Wiki root'
    before={p.name:digest(p) for p in wiki.glob('*.md')}
    changes={}
    for name in TARGETS:
        p=wiki/name
        if not p.exists() and name!='Weapon-Inspirations.md':continue
        old=p.read_text(encoding='utf-8') if p.exists() else ''
        if name=='Weapon-Inspirations.md':new=hub(wiki,old)
        elif name=='Minecraft-Gun-Mod-Inspirations.md':
            new=strip_managed(old)+'\n\n'+START+'\n## Related collections\n\n[TaCZ gunpacks](TaCZ-Gunpacks) · [TaCZ ranked explorer]('+SITE+'minecraft-gun-mods/tacz/)'
            if (wiki/'Minecraft-Gunpack-Creator-Discoveries.md').exists():new+=' · [Creator-hosted discoveries](Minecraft-Gunpack-Creator-Discoveries)'
            new+='\n'+END+'\n'
        elif name=='_Sidebar.md':
            body=strip_managed(old)
            block=navigation(wiki,'sidebar')
            anchor='<details><summary>Optional weapon upgrade</summary>'
            new=(body[:body.index(anchor)].rstrip()+'\n\n'+block+'\n\n'+body[body.index(anchor):]+'\n') if anchor in body else body+'\n\n'+block+'\n'
        else:new=strip_managed(old)+'\n\n'+navigation(wiki,'table')+'\n'
        if new!=old:p.write_text(new,encoding='utf-8');changes[name]={'before':hashlib.sha256(old.encode()).hexdigest(),'after':digest(p)}
    untouched={name:sha for name,sha in before.items() if name not in TARGETS}
    assert all(digest(wiki/name)==sha for name,sha in untouched.items()), 'Unrelated Wiki content changed'
    sidebar=(wiki/'_Sidebar.md').read_text()
    owned=sidebar[sidebar.index(START):sidebar.index(END)]
    assert owned.count('](Weapon-Inspirations)')==1 and not re.search(r'^\s*[-*]\s+\[Weapon inspirations\]',owned,re.M|re.I)
    urls=re.findall(r'\]\(([^)]+)\)',owned);assert len(urls)==len(set(urls)), 'Repeated navigation target'
    report={'changedPages':changes,'unrelatedPagesPreserved':len(untouched),'unrelatedHashes':untouched,'sidebarTargets':urls,'duplicateChildHubLinks':0}
    if report_path:Path(report_path).write_text(json.dumps(report,indent=2),encoding='utf-8')
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('wiki');parser.add_argument('--report');args=parser.parse_args()
    print(json.dumps(apply(args.wiki,args.report),indent=2))
