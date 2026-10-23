#!/usr/bin/env python3
"""Close the four named media gaps and publish an auditable research checkpoint."""
from __future__ import annotations
import collections,copy,hashlib,json,re,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import research_media_final as last
x=last.x;g=last.g;p=last.p;f=last.f;ROOT=last.ROOT;DATA=last.DATA;f2=last.f2


def main():
 c,m,baseline=x.init();state=g.load(DATA/'state.json',{});idx={e['id']:e for e in c['gaming']+c['historical']};report={'fixed':{},'pending':{},'chapter_candidates':{}}
 qa=DATA/'qa'/'sealed';qa.mkdir(parents=True,exist_ok=True)
 # The weapon itself is visible in this already reviewed guide image. Crop the
 # named crossbow, retaining the exact source and crop provenance.
 k='xg-6825d0f5526c';old=m[k]['image'];pic=Image.open(ROOT/old['local'])
 box=(40,0,min(465,pic.width),min(205,pic.height))
 im=p.save_image(idx[k],pic.crop(box),old['url'],old['source'],'Crusader crossbow detail from its named gameplay-guide preview',{'crop_pixels':list(box),'uncropped_source_sha256':old['sha256'],'visual_review':'Crossbow appears in the upper-left; unrelated comparison guns excluded from the crop'})
 assert im;m[k]['image']=im;state[k]=m[k];report['fixed'][k]={'name':idx[k]['name'],'source':im['source']}
 # MediaWiki page names after the first character are case-sensitive.
 k='xg-e50c84ee8034';im=last.api_images(idx[k],'https://starwars.fandom.com','Geonosian elite beam weapon','geonosian|beam|weapon')
 if im:m[k]['image']=im;state[k]=m[k];report['fixed'][k]={'name':idx[k]['name'],'source':im['source']}
 else:report['pending'][k]='Exact Geonosian source artwork not returned'
 # A named gameplay chapter replaces the former replica review and boss cover.
 videos={}
 for query in ['Scorn All Weapons and Equipment Reloads Animations Sounds Hectorlo','Scorn all weapons showcase']:
  for v in f.search(query):
   title=v['title'].lower()
   if 'scorn' in title and re.search(r'all weapons|all guns|weapons showcase|all.*equipment',title) and not re.search(r'replica|real life|prop|cosplay',title):videos[v['id']]=v
 for k in ('xg-71c9d821c0be','xg-6aed3ef12cc9'):
  e=idx[k];choices=[]
  for v in videos.values():
   chapter=f2.named_chapter(e,v)
   if chapter and chapter.get('chapter_thumbnail'):choices.append(chapter)
  report['chapter_candidates'][k]=choices
  if not choices:report['pending'][k]='No named gameplay chapter thumbnail';continue
  chosen=choices[0]
  image=p.image_url(e,chosen['chapter_thumbnail'],chosen['url'],'Exact named Scorn weapon chapter screenshot')
  if not image:report['pending'][k]='Chapter screenshot did not decode';continue
  image.update(chapter_title=chosen.get('chapter'),chapter_time_seconds=chosen.get('chapter_seconds'),chapter_metadata_source=chosen.get('evidence_url',chosen['url']))
  m[k].update(image=image,video=chosen,complete=True,status='accepted');state[k]=m[k]
  report['fixed'][k]={'name':e['name'],'source':image['source'],'video_title':chosen['title'],'chapter':chosen['chapter']}
  for n,option in enumerate(choices):
   r=g.fetch(option['chapter_thumbnail'],binary=True)
   if r['ok']:
    import io
    try:Image.open(io.BytesIO(r['body'])).convert('RGB').save(qa/(k+'-choice-'+str(n)+'.jpg'),quality=94)
    except Exception:pass
 report['source_evidence']=last.EVIDENCE;g.save(DATA/'seal-report.json',report)
 exact=g.load(DATA/'exact-source-report.json',{})
 for k in report['fixed']:exact.get('pending',{}).pop(k,None)
 g.save(DATA/'exact-source-report.json',exact)
 if report['pending']:
  g.save(DATA/'state.json',state);g.save(ROOT/'media.json',m)
  raise RuntimeError('Named media gaps remain: '+json.dumps(report['pending']))
 x.persist_and_publish(c,m,baseline,state,'--remote' in sys.argv)
 ids=list(report['fixed']);out=Image.new('RGB',(1440,300),(235,235,235));draw=ImageDraw.Draw(out);font=ImageFont.load_default(size=16)
 for i,k in enumerate(ids):
  image=Image.open(ROOT/m[k]['image']['local']).convert('RGBA');image.thumbnail((350,235));a=i*360;out.paste(image,(a,0),image);draw.text((a+3,240),idx[k]['name'],font=font,fill='black');draw.text((a+3,268),k,font=font,fill='black')
 out.save(qa/'final-four.jpg',quality=94)
 x.verify(c,m,baseline,'--remote' in sys.argv)
 counts=collections.Counter(r['status'] for r in state.values());coverage=g.load(DATA/'coverage.json',{});publication=g.load(DATA/'publication.json',{});browser=g.load(DATA/'native-browser-verification.json',[])
 assert len(baseline['entries'])==1044
 assert all(v['expected']==v['images']==v['decoded'] and not v['broken'] and not v['missing'] and v['end_marker'] for v in browser)
 acceptance=g.load(ROOT/'final-acceptance.json',{})
 acceptance.update(video_evidence_labels=dict(collections.Counter(v['video']['match'] for v in m.values())),full_video_playback_reviewed=False,original_entry_hashes_preserved=1044,original_media_hashes_preserved=1044,research_outcomes=dict(counts),research_deferred_count=counts['unresolved'],published_media_identity_repairs_pending=[],live_browser_receipt='expansion-2026-10-23/native-browser-verification.json',live_wiki_receipt='expansion-2026-10-23/publication.json')
 g.save(ROOT/'final-acceptance.json',acceptance)
 lines=['# Weapon inspiration research checkpoint','','## Published result','',f'- Original references retained unchanged: 1,044.',f'- New gaming references: {coverage["new_gaming"]}.',f'- New historical references: {coverage["new_historical"]}.',f'- Total published references, embedded images and direct video links: {coverage["total"]}.',f'- Gaming collections across both volumes: {coverage["game_collections"]}.','', '## Evidence and quality','', '- Every published image passed file-hash, image-decoding and live Chromium checks.', '- Every original entry and media record was preserved against the baseline hash ledger.', '- Named source artwork, gameplay screenshots and item-video previews are distinguished in the media records.', '- Direct videos were checked through item titles, game identity, source context or named chapters. Full end-to-end playback of every video is not claimed.', '- Two newly researched historical records were withdrawn because their selected media did not establish the exact model. No original references were removed.','', '## Research reconciliation','',f'- Candidate records investigated after initial duplicate screening: {len(state)}.',f'- Accepted and published: {counts["accepted"]}.',f'- Deferred pending stronger item/model media: {counts["unresolved"]}.',f'- Rejected as non-gun or incorrect identity: {counts["rejected"]}.','', 'The deferred leads are not counted as gallery entries. The full candidate, rejection, source and repair ledgers remain alongside this file.','', '## Canonical pages','', '- https://github.com/Herbertofury/Advent-of-Ascension/wiki/Video-Game-Weapon-Inspirations', '- https://github.com/Herbertofury/Advent-of-Ascension/wiki/Video-Game-Weapon-Inspirations-Volume-2', '- https://github.com/Herbertofury/Advent-of-Ascension/wiki/Historical-and-Experimental-Gun-Inspirations', '- https://github.com/Herbertofury/Advent-of-Ascension/wiki/Weapon-Inspiration-Media-Sources-Expansion','', '## Verified publication lineage','',f'- Source publication commit: `{publication["source_commit"]}`.',f'- Wiki publication commit: `{publication["wiki_commit"]}`.','', 'Exact next action after this checkpoint: inspect `qa/sealed/final-four.jpg`, then preserve the verified complete artifact in the existing Drive snapshot. Do not restart source discovery.','']
 (DATA/'RESEARCH-CHECKPOINT.md').write_text('\n'.join(lines),encoding='utf-8')
 if '--remote' in sys.argv:
  x.run_git('add','docs/weapon-inspirations/final-acceptance.json','docs/weapon-inspirations/expansion-2026-10-23/RESEARCH-CHECKPOINT.md')
  import subprocess
  if subprocess.run(['git','diff','--cached','--quiet'],cwd=x.DOCS.parent).returncode:
   x.run_git('commit','-m','Record complete expansion research, deferred leads and verified live Wiki coverage');x.run_git('pull','--rebase','origin','main');x.run_git('push','origin','HEAD:main')
 print('SEALED_RESEARCH',json.dumps({'published':coverage['total'],'new_gaming':coverage['new_gaming'],'new_historical':coverage['new_historical'],'research':dict(counts),'media_repairs_pending':report['pending']}),flush=True)
if __name__=='__main__':main()
