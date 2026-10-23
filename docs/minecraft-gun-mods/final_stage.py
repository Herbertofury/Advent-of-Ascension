#!/usr/bin/env python3
"""Finish the preserved catalog with explicit identity proofs and visual-media QA."""
from pathlib import Path
import collections,hashlib,json
import research as r
import refine
import media_review
import build
import harden
ROOT=Path(__file__).resolve().parent
# These pairs were individually reviewed against both creator-linked source repositories.
# Related gun packs, unofficial forks and the distinct same-named Flashfest JEG are not merged.
PAIRS=[
 ('cf-1028108','mr-SzzJttH8'),('cf-820727','mr-n1EbSfq3'),
 ('cf-350869','mr-IkpfYUd0'),('cf-354562','mr-967vM4zw'),
 ('cf-1342532','mr-FTtiRPsV'),('cf-1353462','mr-OypNE65K'),
 ('cf-1265947','mr-lvoGABiq'),('cf-1471691','mr-nXACETjw'),
 ('cf-1011217','mr-V9uNAQBc'),('cf-1552880','mr-CGgARreW'),
 ('cf-889487','mr-WZoCbc26'),('cf-1432620','mr-zSKr1DYY'),
 ('cf-1566345','mr-jtL0NCGC'),('cf-1620285','mr-NiMg4Heu'),
 ('cf-1495339','mr-ARzh0EYV'),('cf-1627594','mr-AMul5zyZ')]

def reconcile():
 data=r.load(ROOT/'catalog.json');idx={x['id']:x for x in data['items']};report=r.load(ROOT/'final-identity-review.json',{'aliases':[]})
 for target,source in PAIRS:
  if source not in idx:continue
  assert target in idx,(target,source)
  a,b=idx[target],idx[source];shared=refine.source_codes(a)&refine.source_codes(b)
  assert shared and a['edition']==b['edition'],('Cross-provider proof changed',target,source)
  proof='Individually reviewed same project, exact shared creator-linked source repository: '+', '.join(sorted(shared))
  priority=max(a['studyPriority'],b['studyPriority']);anchor='Study anchor' in (a['curation'],b['curation'])
  ideas=list(dict.fromkeys(a['inspiration']+b['inspiration']))
  refine.combine(a,b,proof);a['inspiration']=ideas;a['studyPriority']=priority
  if anchor:a['curation']='Study anchor'
  a['latest']=a['releases'][0] if a['releases'] else None;a['latestStable']=next((v for v in a['releases'] if v['channel']=='release'),None)
  a.setdefault('aliases',[]).append(source)
  report['aliases'].append({'from':source,'to':target,'sourceRepository':sorted(shared),'sourceUrl':b['projectUrl'],'targetUrl':a['projectUrl'],'proof':proof})
  del idx[source]
 data['items']=sorted(idx.values(),key=lambda x:(-x['studyPriority'],-x['downloads'],x['name'].lower()))
 data['idAliases']={x['from']:x['to'] for x in report['aliases']}
 pending=r.load(ROOT/'pending-projects.json',{})
 data['coverage'].update({'publishedProjects':len(idx),'qualifiedProjects':len(idx),'unresolvedSources':sum(not x.get('rejected') for x in pending.values()),'excludedSources':sum(bool(x.get('rejected')) for x in pending.values()),'additionalReviewedAliasMerges':len(report['aliases']),'types':dict(collections.Counter(x['type'] for x in idx.values())),'editions':dict(collections.Counter(x['edition'] for x in idx.values())),'mediaProjects':sum(bool(x.get('media')) for x in idx.values()),'directVideoProjects':sum(bool(x['videos']) for x in idx.values())})
 data['build']['itemCount']=len(idx);data['build']['dataHash']=hashlib.sha256(json.dumps(data['items'],sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 r.save(ROOT/'catalog.json',data);r.save(ROOT/'final-identity-review.json',report)
 return data

def main():
 reconcile();media_review.run();build.build();harden.run()
 data=r.load(ROOT/'catalog.json');qa=r.load(ROOT/'qa'/'data-verification.json')
 ledger=r.load(ROOT/'discovery-ledger.json',[]);cf=r.load(ROOT/'discovery-cf-ledger.json',[])
 evidence={'projects':len(data['items']),'modrinthQueries':len(ledger),'curseforgeQueries':len(cf),'modrinthTerminalQueries':sum(x['terminalPageReached'] for x in ledger),'curseforgeTerminalQueries':sum(x['terminalPageReached'] for x in cf),'earlierPicks':sum(x.get('earlierPick',False) for x in data['items']),'studyAnchors':sum(x['curation']=='Study anchor' for x in data['items']),'dataProof':qa,'nativeMinecraftRuntimeTested':False,'fullVideoPlaybackReviewed':False}
 r.save(ROOT/'qa'/'research-acceptance.json',evidence)
 print(json.dumps(evidence,indent=2),flush=True)
if __name__=='__main__':main()
