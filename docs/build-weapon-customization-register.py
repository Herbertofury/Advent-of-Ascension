from pathlib import Path
import json,hashlib,os
R=Path(os.environ.get('CATALOG_ROOT',str(Path(__file__).parent)));P=Path(__file__).parent
catalog=json.loads((R/'weapon-concept-catalog.json').read_text());features=json.loads((R/'weapon-feature-catalog.json').read_text());old=json.loads((R/'weapon-feature-coverage.json').read_text());oldby={w['id']:w for w in old['weapons']}
groups=[
('sights_scopes','Sights, scopes and aim transformations',['sights_and_aim']),
('barrels_muzzles_converters','Barrels, muzzles and converters',['barrels_and_converters','handling_and_muzzles','functional_variants']),
('magazines_feed_resource','Magazines, feed and resource modules',['feed_and_resource_modules','mechanism_and_hand_fit']),
('grips_stocks_supports','Grips, stocks, receivers and supports',['handling_and_muzzles','mechanism_and_hand_fit']),
('skins_finishes_mastercraft','Skins, finishes and mastercraft variants',['skins_mastercraft','textures_materials_uv']),
('stickers_emblems','Static, animated and glowing stickers, decals and emblems',['stickers_emblems']),
('charms_trinkets','Charms and trinkets',['charms']),
('projectiles_tracers','Projectiles, tracers and trails',['projectiles','tracers_and_trails']),
('muzzle_charge_feedback','Muzzle, charge, recoil and recovery feedback',['muzzle_feedback','animation_fire_charge']),
('impacts_world_decals','Entity, armor, terrain and fluid impacts; world decals',['impacts','decals']),
('death_finishers','Confirmed-outcome death and finisher effects',['death_finishers']),
('motion_inspect_reload','Idle, movement, equip, inspect and reload/resource service',['animation_locomotion','animation_inspect','animation_reload']),
('builds_crafting_ui','Resolved builds, combinations, crafting and UI presentation',['functional_variants','crafting_progression','ui_build_feedback','effect_salvage']),
('audio_accessibility','Audio direction, reduced-motion and effect controls',['audio','performance_accessibility','custom_effect_channels'])]
lookup={x[0] for x in groups}
known={'aoa3:abominator':{'magazines_feed_resource':['abominator-magazine-study-v1.png'],'sights_scopes':['abominator-sights-study-v1.png'],'barrels_muzzles_converters':['abominator-muzzles-converters-study-v1.png'],'skins_finishes_mastercraft':['abominator-skins-finishes-study-v1.png'],'stickers_emblems':['abominator-charms-emblems-study-v1.png'],'charms_trinkets':['abominator-charms-emblems-study-v1.png']},'aoa3:darkly_guster':{'sights_scopes':['darkly-guster-wing-sight-study-v2.png']},'aoa3:eradicator':{'sights_scopes':['eradicator-living-sight-study-v1.png']},'aoa3:hiver':{'sights_scopes':['hiver-bee-action-sights-study-v1.png'],'muzzle_charge_feedback':['hiver-bee-action-sights-study-v1.png']},'aoa3:hive_cracker':{'sights_scopes':['hive-cracker-bee-action-sights-study-v1.png'],'muzzle_charge_feedback':['hive-cracker-bee-action-sights-study-v1.png']}}
known['aoa3:abominator'].update({'projectiles_tracers':['abominator-projectiles-tracers-study-v1.png'],'impacts_world_decals':['abominator-impacts-decals-study-v1.png'],'death_finishers':['abominator-finisher-effects-study-v1.png']})
known['aoa3:darkly_guster'].update({'motion_inspect_reload':['darkly-guster-inspect-flight-study-v1.png'],'builds_crafting_ui':['darkly-guster-follower-modes-study-v1.png'],'muzzle_charge_feedback':['darkly-guster-propeller-gust-study-v1.png']})
known['aoa3:bubble_horn']={'sights_scopes':['bubble-horn-musical-sight-study-v2.png']}
known['aoa3:bubble_horn'].update({'motion_inspect_reload':['bubble-horn-trumpet-playing-study-v1.png'],'projectiles_tracers':['bubble-horn-trumpet-playing-study-v1.png'],'builds_crafting_ui':['bubble-horn-trumpet-playing-study-v1.png']})
known['aoa3:bubble_horn']['projectiles_tracers'].append('bubble-horn-musical-projectiles-study-v1.png')
known['aoa3:bubble_horn']['impacts_world_decals']=['bubble-horn-musical-projectiles-study-v1.png']
known['aoa3:abominator']['stickers_emblems'].append('abominator-emblems-stickers-study-v2.png')
known['aoa3:bubble_horn']['builds_crafting_ui'].append('bubble-horn-earned-mouthpiece-study-v2.png')
known['aoa3:bubble_horn']['barrels_muzzles_converters']=['bubble-horn-trumpet-playing-study-v1.png','bubble-horn-earned-mouthpiece-study-v2.png']
for ident in ['clownimator','clowno_pulse']:
 known.setdefault('aoa3:'+ident,{})['sights_scopes']=['clown-ribbon-focused-view-study-v2.png']
known.setdefault('aoa3:clownershot',{})['sights_scopes']=['clown-ribbon-focused-view-study-v2.png']
known['aoa3:hiver']['skins_finishes_mastercraft']=['hiver-material-variants-study-v1.png']
for ident in ['hiver','hive_cracker']:
 known['aoa3:'+ident]['charms_trinkets']=['hive-family-charms-study-v1.png']
known.setdefault('aoa3:flame_wrecker',{})['sights_scopes']=['flame-wrecker-flame-sight-study-v1.png']
known.setdefault('aoa3:hot_shot',{})['sights_scopes']=['hotshot-flame-sight-study-v1.png']
known.setdefault('aoa3:heat_wave',{})['sights_scopes']=['heatwave-three-flame-sight-study-v2.png']
known.setdefault('aoa3:mk_fung',{})['sights_scopes']=['mk-fung-spore-sight-study-v1.png']
known.setdefault('aoa3:fragment',{})['sights_scopes']=['fragment-living-shard-sight-study-v1.png']
known.setdefault('aoa3:froster',{}).setdefault('sights_scopes',[]).append('froster-living-frost-sight-study-v1.png')
known.setdefault('aoa3:whimsy_winder',{}).setdefault('sights_scopes',[]).append('whimsy-winder-angel-sight-study-v1.png')
known.setdefault('aoa3:hell_horn',{}).setdefault('sights_scopes',[]).append('hell-horn-flaming-bubble-sight-study-v1.png')
known.setdefault('aoa3:hell_horn',{}).setdefault('builds_crafting_ui',[]).append('hell-horn-earned-mouthpiece-study-v1.png')
known.setdefault('aoa3:skullo_blaster',{}).setdefault('sights_scopes',[]).append('skullo-blaster-purple-flame-sight-study-v1.png')
rows=[]
for w in catalog['weapons']:
 rows.append({'id':w['id'],'name':w['name'],'families':w['families'],'release_lanes':w['lanes'],'base_concept':w['concept'],'base_art_review':'open','existing_feature_manifest':oldby.get(w['id'],{}).get('manifest'),'existing_feature_record_preserved':w['id'] in oldby,'dedicated_sheets':{gid:{'status':'partial_candidate' if known.get(w['id'],{}).get(gid) else 'requires_reconciliation','files':known.get(w['id'],{}).get(gid,[]),'owner_approved_omission':None}for gid,_,_ in groups},'implementation_acceptance':False,'qa_acceptance':False})
for row in rows:
 if row['id'] in ['aoa3:clownimator','aoa3:clowno_pulse','aoa3:clownershot']:
  row['dedicated_sheets']['sights_scopes']['review_note']='Focused appearance only; old side transition superseded by paired split-open apertures with vertical pole alignment. Replacement integrated transition artwork remains open.'
d={'schema':1,'revision':'20261022-customization-coverage-0725','scope':'All 434 audited raw release-union IDs; 411 first-target identities. Registry identities are not deduplicated by shared art.','base_catalog':'weapon-concept-catalog.json','base_catalog_sha256':hashlib.sha256((R/'weapon-concept-catalog.json').read_bytes()).hexdigest(),'feature_catalog':'weapon-feature-catalog.json','required_features':[f['id']for f in features['features']],'sheet_groups':[{'id':i,'title':t,'feature_ids':f}for i,t,f in groups],'policy':['Base art coverage does not complete dedicated customization art.','No category may be silently omitted. A family-appropriate equivalent or explicitly approved omission must be recorded.','Existing evidence and old 228-firearm coverage are retained, not reset or replaced. Requires reconciliation does not assert that no older artwork exists.','Partial candidate is not complete or approved. Each option and compatibility combination needs individual review.','Separate concept, implementation and native AoA plus TaCZ QA. No static artwork proves animation or gameplay.','Cosmetic channels cannot silently alter source damage, resource costs or target rules; functional conversions require separate explicit specification.'],'weapons':rows}
(P/'weapon-customization-art-register.json').write_text(json.dumps(d,indent=2)+'\n');print('Registered',len(rows),'IDs with',len(groups),'dedicated sheet groups and',len(d['required_features']),'required feature groups')
