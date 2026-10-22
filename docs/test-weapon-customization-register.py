from pathlib import Path
import json,copy,re,os,hashlib
P=Path(__file__).parent;R=Path(os.environ.get('CATALOG_ROOT',str(Path(__file__).parent)))
d=json.loads((P/'weapon-customization-art-register.json').read_text());base=json.loads((R/'weapon-concept-catalog.json').read_text());feat=json.loads((R/'weapon-feature-catalog.json').read_text())
def validate(d):
 assert d['base_catalog_sha256']==hashlib.sha256((R/'weapon-concept-catalog.json').read_bytes()).hexdigest()
 ids={w['id']for w in base['weapons']};rows=d['weapons'];assert len(rows)==len(ids)==434;assert {w['id']for w in rows}==ids;assert len({w['id']for w in rows})==len(rows)
 assert set(d['required_features'])=={f['id']for f in feat['features']};assert len(d['required_features'])==31
 groups={g['id']for g in d['sheet_groups']};assert len(groups)==14
 for w in rows:
  assert set(w['dedicated_sheets'])==groups
  assert w['implementation_acceptance']is False and w['qa_acceptance']is False
  assert re.fullmatch(r'[a-z0-9][a-z0-9._-]*\.png',w['base_concept']);assert(R/w['base_concept']).is_file()
  for s in w['dedicated_sheets'].values():
   assert s['status']in ['requires_reconciliation','partial_candidate'];assert s['owner_approved_omission']is None;assert isinstance(s['files'],list)
   if s['status']=='partial_candidate':assert s['files']
   for f in s['files']:assert re.fullmatch(r'[a-z0-9][a-z0-9._-]*\.png',f);assert(R/f).is_file()
 return True
assert validate(d);checks=1
mutations=[lambda c:c.update(base_catalog_sha256='stale'),lambda c:c['weapons'].pop(),lambda c:c['weapons'].append(c['weapons'][0]),lambda c:c['weapons'][0].update(id='aoa3:unknown'),lambda c:c['required_features'].pop(),lambda c:c['weapons'][0]['dedicated_sheets'].pop('death_finishers'),lambda c:c['weapons'][0].update(implementation_acceptance=True),lambda c:c['weapons'][0].update(qa_acceptance=True),lambda c:c['weapons'][0]['dedicated_sheets']['sights_scopes'].update(status='passed'),lambda c:c['weapons'][0]['dedicated_sheets']['sights_scopes'].update(files=['../bad.png']),lambda c:c['weapons'][0]['dedicated_sheets']['sights_scopes'].update(files=[]),lambda c:c['weapons'][0]['dedicated_sheets']['death_finishers'].update(owner_approved_omission='automatic')]
for m in mutations:
 c=copy.deepcopy(d);m(c)
 try:validate(c)
 except AssertionError:checks+=1
 else:raise AssertionError('Invalid register accepted')
print(json.dumps({'status':'PASS','regression_cases':checks,'raw_ids':434,'sheet_groups_per_id':14,'feature_groups':31,'complete_customization_packages':0,'native_accepted':0}))
