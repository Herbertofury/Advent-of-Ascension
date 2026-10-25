#!/usr/bin/env python3
"""Apply explicit visual decisions without inventing firearm content from an armory title."""
from pathlib import Path
import json,collections
ROOT=Path(__file__).resolve().parent

def load(name):return json.loads((ROOT/name).read_text())
def save(name,obj):(ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))

def main():
 selection=load('selection.json');records=load('qualified-records.json');held='bilibili-BV1Hggn6WEfF'
 if held in records:
  save('deferred-doraemon-source.json',{'record':records.pop(held),'reason':'Creator release and public share exist, but available opening artwork shows a workbench rather than an established firearm roster. Do not promote a generic armory title into a verified gun family.'})
 selection['accepted']=[s for s in selection['accepted'] if s['id']!=held]
 selection['explicitDispositions']['BV1Hggn6WEfF']={'status':'unresolved firearm roster','reason':'Creator release exists; public opening artwork shows a workbench and character, not a clear additional firearm. Kept as a lead, not counted.'}
 for spec in selection['accepted']:
  if spec['id']=='bilibili-BV1JfLAzeE59':
   spec['releaseLabel']='Creator preview labels v2.1; later 2026 AK showcase'
   spec['note']=spec['note'].replace('Later creator posts show A1.10 and additional weapons,','Later creator posts show A1.10, a steam-rifle preview visibly labeled v2.1, and additional weapons in 2026,')
   rec=records[spec['id']];rec['item']['creatorAccessNote']=spec['note'];rec['item']['cautions'][0]=spec['note'];rec['item']['evidence']['releaseScope']=spec['note'];rec['editorial']['caution']=spec['note']
 preferred={
 'bilibili-BV1ihycY2E3s':'ecc9ee4a4f6ea26a',
 'bilibili-BV1fkdiYLEJy':'6c6adc87ed52dcd4',
 'bilibili-BV1LkfTYeE5o':'f99b641664f822b5',
 'bilibili-BV1JfLAzeE59':'2a809c32498a2ee9',
 'bilibili-BV1W88BzGEmD':'8a7fb83aa41810d2',
 'bilibili-BV1AXfRBkEtG':'f821315c310ed126',
 'bilibili-BV1qinS6WEHy':'772178862dad45de'}
 chosen={k:next(m['sha256'] for m in records[k]['item']['media'] if m['sha256'].startswith(prefix)) for k,prefix in preferred.items()}
 save('media-review.json',{'allCardsReviewed':True,'sourcePreviewsReviewed':20,'acceptedFamilies':len(records),'preferred':chosen,'pending':[],'deferred':[held],'notes':'Actual creator artwork selected for all seven cards. Boonie Bears uses the current remake firearm, not its chainsaw segment. TROL uses the v2.1-labeled steam-rifle preview. Source roles remain visible; no image generation.'})
 save('selection.json',selection);save('qualified-records.json',records)
 decisions=load('source-decisions.json')
 for d in decisions:
  if d['id']=='BV1Hggn6WEfF':d.update(selection['explicitDispositions'][d['id']])
 save('source-decisions.json',decisions)
 coverage=load('coverage.json');coverage.update(acceptedAdditionalFamilies=len(records),newEditorialSelections=sum(r['editorial']['shortlist'] for r in records.values()),deferredAfterVisualReview=1,visualQualificationPending=False,decisionCounts=dict(collections.Counter(d['status'] for d in decisions)))
 manifest=load('manifest-evidence.json') if (ROOT/'manifest-evidence.json').exists() else {};coverage['manifestLimitation']=manifest.get('limitation',coverage.get('manifestLimitation',''))
 save('coverage.json',coverage)
 print('Visually qualified',len(records),'families; one ambiguous armory retained as uncounted evidence.',flush=True)
if __name__=='__main__':main()
