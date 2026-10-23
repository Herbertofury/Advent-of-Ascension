#!/usr/bin/env python3
"""Reconcile the saved source sweep without repeating finished network discovery."""
from __future__ import annotations
import collections,copy,hashlib,json,re
from pathlib import Path
from urllib.parse import urlparse
import collect as c
import research as r
ROOT=Path(__file__).resolve().parent

ANCHORS={
 'timeless-and-classics-zero':('TaCZ','Compare first-person handling, creator gun-pack authoring, attachment presentation and the weapon inspection loop. Keep its base engine separate from the gunpacks below.'),
 'vics-point-blank':('Point Blank','Compare animation-led gun presentation, attachment silhouettes and the creator content-pack workflow across exact released Minecraft branches.'),
 'pointblank-jelly':('Point Blank','Study a separate Point Blank continuation with its own handling, compatibility and creator tools. This is a gun runtime, not merely a support library.'),
 'pb-jelly':('Point Blank','Study the Point Blank continuation as its own runtime and preserve exact fork/version identity.'),
 'scorched-guns':('Scorched Guns','Strong AoA reference for Minecraft-styled industrial/fantasy guns, material identity, progression, enemy context and readable projectile effects.'),
 'scorched-guns-2':('Scorched Guns','Study block-scale fantasy firearm designs, themed materials and survival progression rather than importing a realistic-gun silhouette wholesale.'),
 'scorched-guns-2-flintlocks':('Scorched Guns','Study the narrower pirate-era musket/flintlock aesthetic and deliberate reload rhythm. It is a standalone alternative, not an add-on to install beside the parent.'),
 'just-enough-guns':('Just Enough Guns','Compare readable blocky silhouettes, varied weapon roles, animation feedback and approachable survival crafting.'),
 'guns-without-roses':('Independent','A useful contrast to tactical simulators: study simple Minecraft-scale firearms and readable fantasy combat feedback.'),
 'superb-warfare':('Superb Warfare','Study first/third-person weapon presence, mounted systems, encounter scale and the visual transition between carried and emplaced weapons.'),
 'create-big-cannons':('Create','Study mechanically visible loading, moving parts, coherent materials and the identity of large constructed weapons.'),
 'create-love-war':('Create','Compare kinetic machinery with firearm crafting and industrial visual language. Keep the project distinct from its required Create runtime.'),
 'create-armory':('Create','Study how a firearm system is visually integrated into a mechanical Minecraft technology theme.'),
 'warium':('Warium','Study combined-arms scale, industrial identity, mounted weapons and machinery rather than treating it as a simple handgun pack.'),
 'techguns':('Techguns','Legacy but valuable: compare a broad science-fiction arsenal, enemy equipment, visual effects and industrial survival progression.'),
 'modern-warfare-cubed':('Modern Warfare','Study a legacy realistic-firearm continuation for attachments and animation ideas, without confusing a page update with a recent game-version release.'),
 'vics-modern-warfare-mod':('Modern Warfare','Historic Minecraft firearm reference for detailed models, attachment silhouettes and handling conventions; verify legacy version requirements.'),
 'flans-mod-reloaded':("Flan's",'Study the modern Flan ecosystem and its modular content authoring, while keeping legacy content packs and newer release formats distinct.'),
 'musket-mod':('Independent','Study a restrained historical weapon palette, visible reload staging and a silhouette that fits Minecraft rather than a modern military loadout.'),
 'old-guns':('Independent','Study period-inspired firearms, distinct loading rhythms and how old materials translate into a coherent voxel arsenal.'),
 'diamond-caliber':('Independent','Study Minecraft-material firearm progression and the relationship between a weapon silhouette and its crafting tier.'),
 'ironsarms':('TaCZ','Study the interaction between visible firearm identity and spell-driven fantasy effects; exact dependencies and runtime compatibility remain version-specific.'),
 'arsarms':('TaCZ','Strong magic-gun crossover reference: investigate spell presentation and magical resource feedback without replacing native AoA resources.'),
 'irons-artifice':('Independent','Broader magical engineering reference: inspect the actual ranged tools and weapons within the project, not every feature as a gun.'),
 'arcanemag':('TaCZ','Study how a magic system changes ammunition/resource feedback and the resulting firearm presentation.'),
 'aplok-guns':('Independent','Bedrock reference for readable low-poly weapon design and first-person handling. Treat behavior/resource-pack requirements separately from Java loaders.'),
 'aplok-guns-minecraft-bedrock':('Independent','Bedrock reference for cohesive low-poly firearms and animation-led handling, with creator release requirements kept explicit.'),
 'actualguns-3d':('Independent','Bedrock reference for three-dimensional weapon models and animated handling; do not infer Java compatibility.'),
 'blockfront':('Independent','Study a full historical combat presentation: guns in an encounter, first/third-person poses, effects and readable equipment roles.'),
 'blockfront-guns-war-and-more':('Independent','Compare a complete historical combat experience rather than isolated weapon models.'),
 'happiness-is-a-warm-gun':('Independent','Study a Minecraft-styled firearm system with a deliberately different visual identity from realistic tactical packs.'),
 'weaponmechanics':('Independent','Server-side reference for configurable weapon systems and resource-pack presentation; this is a plugin, not a Forge/Fabric mod.'),
 'qualityarmory':('Independent','Study server-plugin gun presentation and resource-pack integration, with server software distinguished from client mod loaders.'),
 'auroras-arsenal':('Independent','Study expressive weapon geometry and the balance between a compact Minecraft silhouette and animation detail.'),
 'dochis-warfare':('Independent','Inspect an alternative firearm/warfare presentation for distinct weapon proportions and handling.'),
 'cgs':('Crayfish / CGM','Compare a Crayfish-family firearm continuation and keep its exact parent/fork identity visible.'),
}
EARLIER_PATTERNS=[r'^\[?tacz\]?.*create armorer',r'^\[?tacz\]?.*immersive armorer',r'^\[?tacz\]?.*ars armorer',r'^\[?tacz\]?.*cyber armorer',r'^\[?tacz\]?.*applied armorer',r'^\[?tacz\]?.*tti gun',r'^\[?tacz\]?.*hell ?divers2 gun',r'gucci.*vuitton.*attachments',r'^heavy recoil$',r'^exception api extension$']
EXCLUDE_IDS={'mr-M37apa3J':'Uses glass cannon as a metaphor for bosses; no firearm project identity.','mr-mdDOISAm':'Origin character described as a glass cannon, not a gun project.','mr-wGiuhx6X':'Death-announcement plugin with cannon sound, not a weapon system.','mr-4vBAd4Nd':'An End structure providing gunpowder, not a gun project.','mr-RXQBYQz3':'Only a texture for a vanilla orbital TNT mechanism; retained in discovery but outside firearm-mod scope.','mr-eNeaaazj':'Only a renamed-item texture for a vanilla orbital TNT mechanism, not an independent firearm project.'}


def titlekey(name):
 name=re.sub(r'^\s*\[(?:tacz|sbw|vpb|cgm|pbj)\]\s*','',name,flags=re.I)
 return c.norm(name).replace('point blank','pointblank')

def author_keys(item):
 out={c.norm(a['name']) for a in item['authors']}
 for link in item['links']:
  parsed=urlparse(link['url'])
  if parsed.netloc.lower()=='github.com' and len(parsed.path.strip('/').split('/'))>=2:out.add(c.norm(parsed.path.strip('/').split('/')[0]))
 return out-{'see project credits','qa','none'}

def source_codes(item):
 return {a['url'].lower().rstrip('/').removesuffix('.git') for a in item['links'] if a.get('label')=='Source code' and 'github.com/' in a['url']}

def combine(target,source,reason):
 for key in ('links','media','videos','releases'):
  ident='url' if key in ('links','videos') else 'sha256' if key=='media' else 'id'
  target[key]=list({a[ident]:a for a in target.get(key,[])+source.get(key,[])}.values())
 target['providerIds'].update(source['providerIds'])
 for key in ('versions','loaders','sourceRows','tags'):target[key]=sorted(set(target.get(key,[])+source.get(key,[])))
 target['downloads']=max(target['downloads'],source['downloads'])
 target.setdefault('providerEvidence',[]).append({'id':source['id'],'url':source['projectUrl'],'evidence':source['evidence'],'identityProof':reason})
 target['releases'].sort(key=lambda v:v['date'],reverse=True)
 target['updated']=max(target['updated'],source['updated'])
 return target


def exclusion(x):
 if x['id'] in EXCLUDE_IDS:return EXCLUDE_IDS[x['id']]
 title=c.norm(x['name']);summary=c.norm(x['summary'])
 if 'glass cannon' in summary and not re.search(r'gun|firearm|pistol|rifle|artillery|shotgun',summary):return 'Figurative glass-cannon description, not a firearm project.'
 if 'gunpowder' in title and not re.search(r'gunpowder revolution|gunpowder weapons|gunpowder warfare|gunpowder age|guns|muskets|firearms',title):return 'Gunpowder material/recipe project rather than firearm design or handling.'
 if re.search(r'land claim|land protection|claim protection',summary) and 'gun' not in summary:return 'Land-claim project found through a Flan name collision.'
 if 'portal gun not included' in summary:return 'Portal props explicitly exclude the gun; not a firearm reference.'
 if re.search(r'dupe|duper|duplicat|tnt tracker|rangefinder|osc fire control',title) and re.search(r'tnt|cannon|osc',summary+title) and not re.search(r'firearm|rifle|gun mod',summary):return 'Vanilla TNT engineering or diagnostic utility, outside firearm-mod inspiration scope.'
 return None


def classify(x):
 title=c.norm(x['name']);s=c.norm(x['summary']);body=c.norm(x.get('description',''));p=urlparse(x['projectUrl']).path
 loaders={v.lower() for v in x.get('loaders',[])}
 if loaders&{'paper','spigot','purpur','bukkit','folia'}:return 'Server weapon plugin'
 if x['edition']=='Bedrock':return 'Bedrock add-on'
 if '/resourcepack/' in p or '/texture-packs/' in p:return 'Visual / resource pack'
 if loaders&{'datapack','minecraft'} or '/datapack/' in p:return 'Datapack / command weapon'
 if x['slug'] in ('pointblank-jelly','pb-jelly'):return 'Standalone gun mod'
 if re.search(r'library|api extension|gunsmith lib|projectile library',title):return 'Tooling / framework support'
 if re.search(r'gun.?pack|content pack|weapon pack|armorer|attachment pack|attachments pack',title+' '+s) or '/customization/' in p or '/mc-addons/' in p:return 'Gun / content pack'
 if re.search(r'addon|add on|expansion|additional',s) and re.search(r'adds.{0,60}(guns|weapons)|guns from|weapons from|gun content',s+body[:400]):return 'Gun / content pack'
 if re.search(r'gucci.*attachments|vuitton.*attachments|gun pack|counter strike',title) and x['ecosystem'] in ('TaCZ','Point Blank'):return 'Gun / content pack'
 if re.search(r'compat|optimization|optimized|performance|scope overhaul|recoil|chest loot|loot table|ammo|ammunition|armor|brass|blueprint|enchant|radial menu|gun display|skin|presence|hostile|npc|armed mobs|gun information|gun detection|durability|tweak|fix |fixes|first person|third person|attachments? animations?|recipe|tacz.*(level|pickup|progress|creative)|tactical camo|dont punch|dont-punch',title) and x['slug'] not in ANCHORS:
  return 'Integration / handling / QoL'
 if re.search(r'cannons?|artillery|superb warfare|warium|missiles?|mcheli|tanks?|naval|siege|warships|helicopter|ships|vehicles',title) and not re.search(r'modern warfare|modular warfare',title):return 'Artillery / combined arms'
 if re.search(r'prop|decorat|cosmetic|no damage|no function|display only',s) and not re.search(r'functioning|working gun',s):return 'Visual / resource pack'
 if not re.search(r'gun|firearm|rifle|pistol|tac|flan|blaster|warfare|scorch|arsenal|musket|weapon|cgm|cgc|caliber|shot|flint|sniper|point ?blank|armory|arms',title) and re.search(r'adds|mod adds|includes',s):return 'Broader content with ranged weapons'
 return x['type'] if x['type'] not in ('Tooling / framework support','Gun / content pack') else 'Standalone gun mod'


def run():
 original=r.load(ROOT/'catalog.json');raw=r.load(ROOT/'raw-projects.json',{})
 assert raw and original['items'],'The preserved collection checkpoint is required'
 exclusions=[];identities={};merges=[]
 for value in raw.values():
  x=copy.deepcopy(value);reason=exclusion(x)
  if reason:exclusions.append({'id':x['id'],'name':x['name'],'url':x['projectUrl'],'reason':reason});continue
  if x['id'] in identities:
   identities[x['id']]=combine(identities[x['id']],x,'Same official provider project ID; alternate seed URL')
  else:identities[x['id']]=x
 groups=collections.defaultdict(list)
 for x in identities.values():groups[(x['edition'],titlekey(x['name']))].append(x)
 removed=set()
 for group in groups.values():
  cf=[x for x in group if x['provider']=='CurseForge'];mr=[x for x in group if x['provider']=='Modrinth']
  if len(cf)!=1 or len(mr)!=1:continue
  a,b=cf[0],mr[0];proof=None
  if author_keys(a)&author_keys(b):proof='Matching normalized title and creator/source-owner identity'
  elif source_codes(a)&source_codes(b):proof='Matching normalized title and exact author-linked source repository'
  elif a['projectUrl'] in b.get('crosslinks',[]) or b['projectUrl'] in a.get('crosslinks',[]):proof='Matching normalized title and creator-provided cross-provider project link'
  if proof:
   combine(a,b,proof);removed.add(b['id']);merges.append({'from':b['id'],'to':a['id'],'proof':proof})
 items=[]
 for x in identities.values():
  if x['id'] in removed:continue
  x['type']=classify(x)
  x=c.decorate(x)
  title=x['name'].lower()
  x['earlierPick']=any(re.search(pattern,title,re.I) for pattern in EARLIER_PATTERNS)
  x['curation']='Earlier pick' if x['earlierPick'] else 'Research discovery'
  x['studyPriority']=100 if x['earlierPick'] else 55
  if x['slug'] in ANCHORS:
   ecosystem,idea=ANCHORS[x['slug']];x['ecosystem']=ecosystem;x['inspiration']=[idea]+x['inspiration'];x['curation']='Study anchor';x['studyPriority']=110
  elif x['type'] in ('Standalone gun mod','Artillery / combined arms','Bedrock add-on') and x['downloads']>=100000:
   x['curation']='Established ecosystem reference';x['studyPriority']=85
  elif x['type']=='Gun / content pack' and x['downloads']>=50000:x['studyPriority']=75
  x['priorityBasis']='Editorial study selection and source evidence; not a native Minecraft quality or FPS benchmark'
  # Only display a license name/identifier, never stringify an unexamined provider object.
  if isinstance(x.get('license'),dict):x['license']=x['license'].get('name') or x['license'].get('id') or 'See project license'
  # Relevant support often ships without visual art. Keep it, and label missing imagery explicitly.
  x['mediaStatus']='Creator media archived' if x.get('media') else 'No creator image established'
  x['videos']=list({v['url']:v for v in x['videos']}.values())
  items.append(x)
 # Every provider project ID now has one canonical owner; a pack's link to its runtime is not identity proof.
 ownership=collections.defaultdict(list)
 for x in items:
  for provider,pid in x['providerIds'].items():ownership[(provider,str(pid))].append(x['id'])
 bad={str(k):v for k,v in ownership.items() if len(v)>1};assert not bad,bad
 items.sort(key=lambda x:(-x['studyPriority'],-x['downloads'],x['name'].lower()))
 report={'sourceRecords':len(raw),'previousNaiveCount':len(original['items']),'canonicalProjects':len(items),'crossProviderMerges':merges,'exclusions':exclusions,'duplicateProviderIds':bad,'identityRule':'A linked dependency is not the same project. Merge only same provider ID, or exact normalized name with creator/source/cross-provider proof.','earlierPicks':[{'id':x['id'],'name':x['name']} for x in items if x['earlierPick']],'studyAnchors':[{'id':x['id'],'name':x['name']} for x in items if x['curation']=='Study anchor']}
 original['items']=items;original['build']['itemCount']=len(items);original['build']['generator']='collect.py + refine.py (identity-qualified)'
 original['build']['dataHash']=hashlib.sha256(json.dumps(items,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 original['coverage'].update({'sourceRecordsAccepted':len(raw),'crossProviderMerges':len(merges),'publishedProjects':len(items),'qualifiedProjects':len(items),'editorialExclusions':len(exclusions),'mediaProjects':sum(bool(x.get('media')) for x in items),'directVideoProjects':sum(bool(x['videos']) for x in items),'types':dict(collections.Counter(x['type'] for x in items)),'editions':dict(collections.Counter(x['edition'] for x in items))})
 r.save(ROOT/'catalog.json',original);r.save(ROOT/'identity-and-curation.json',report)
 print(json.dumps(original['coverage'],indent=2),flush=True)
 return original
if __name__=='__main__':run()
