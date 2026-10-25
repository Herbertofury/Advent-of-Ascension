#!/usr/bin/env python3
"""Scope the proven publication implementation to this additive research pass.

The previous readable publisher remains the canonical implementation of complete
archive, navigation and browser verification. This wrapper changes only named
page/filter/release fields, verifies every replacement, and retains all gates.
"""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'tacz-frontier/publish_frontier.py'
EXPECTED='d6b7596ee9979a613886fe663bdb9a841bfbb0f30384613e2899b7f9ce158e27'
assert hashlib.sha256(BASE.read_bytes()).hexdigest()==EXPECTED,'Publication base changed; reconcile before reuse'
text=BASE.read_text(encoding='utf-8')
changes=[
 ("PAGE='TaCZ-Gunpack-Creator-Frontier'","PAGE='TaCZ-Gunpack-Community-Discoveries'"),
 ("'TaCZ-Gunpack-Hidden-Gems.md',PAGE+'.md'","'TaCZ-Gunpack-Hidden-Gems.md','TaCZ-Gunpack-Creator-Frontier.md',PAGE+'.md'"),
 ('AoA-Creator-Frontier-Verification','AoA-Community-Discovery-Verification'),
 ('data-frontier-preset','data-community-preset'),
 ("(PAGE,[x for x in tacz['items'] if x['id'] in ids],'End of creator-frontier gallery')","('TaCZ-Gunpack-Creator-Frontier',[x for x in tacz['items'] if x['id'] in set(load(PARENT/'tacz-frontier/qualified-records.json'))],'End of creator-frontier gallery'),(PAGE,[x for x in tacz['items'] if x['id'] in ids],'End of community-discovery gallery')"),
 ('tacz-frontier.png','tacz-community.png'),('atlas-frontier.png','atlas-community.png'),('mobile-frontier.png','mobile-community.png'),
 ("'followup-evidence.json'","'followup-evidence.json','creator-video-evidence.json','forum-evidence.json','forum-alternate-evidence.json','manifest-evidence.json','video-search.json'"),
 ('Minecraft Gun Atlas - TaCZ Creator Frontier','Minecraft Gun Atlas - TaCZ Community Discoveries'),
 ('including four editorial study selections','including three editorial study selections'),
 ('Engineering-test and discontinued source references remain explicit','Public tests, legacy-style references and access limits remain explicit'),
 ('theme=Frontier+discoveries','theme=Community+discoveries'),
 ('python minecraft-gun-mods/tacz-frontier/build_frontier.py','python minecraft-gun-mods/tacz-community/build_community.py')
]
for old,new in changes:
 assert old in text,('Named publication scope changed',old)
 text=text.replace(old,new)
# __file__ points to this module so all canonical source and receipt paths use the new scope.
namespace={'__file__':str(Path(__file__).resolve()),'__name__':__name__}
exec(compile(text,str(Path(__file__).resolve()),'exec'),namespace)
