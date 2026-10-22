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
known.setdefault('aoa3:light_blaster',{}).setdefault('sights_scopes',[]).append('light-blaster-crystal-sight-study-v2.png')
known.setdefault('aoa3:hiver',{}).setdefault('sights_scopes',[]).append('moonlit-hive-soul-bee-sights-study-v1.png')
known.setdefault('aoa3:hiver',{}).setdefault('muzzle_charge_feedback',[]).append('moonlit-hive-living-chambers-study-v1.png')
known.setdefault('aoa3:hive_cracker',{}).setdefault('sights_scopes',[]).append('moonlit-hive-soul-bee-sights-study-v1.png')
known.setdefault('aoa3:hive_cracker',{}).setdefault('muzzle_charge_feedback',[]).append('moonlit-hive-living-chambers-study-v1.png')
known.setdefault('aoa3:hive_blaster',{}).setdefault('sights_scopes',[]).append('moonlit-hive-soul-bee-sights-study-v1.png')
known.setdefault('aoa3:hive_blaster',{}).setdefault('muzzle_charge_feedback',[]).append('moonlit-hive-living-chambers-study-v1.png')
known.setdefault('aoa3:hive_howitzer',{}).setdefault('sights_scopes',[]).append('moonlit-hive-soul-bee-sights-study-v1.png')
known.setdefault('aoa3:hive_howitzer',{}).setdefault('muzzle_charge_feedback',[]).append('moonlit-hive-living-chambers-study-v1.png')
known.setdefault('aoa3:hive_staff',{}).setdefault('sights_scopes',[]).append('moonlit-hive-soul-bee-sights-study-v1.png')
known.setdefault('aoa3:hive_staff',{}).setdefault('muzzle_charge_feedback',[]).append('moonlit-hive-living-chambers-study-v1.png')
known.setdefault('aoa3:hell_horn',{}).setdefault('projectiles_tracers',[]).append('hell-horn-musical-bubble-effects-study-v1.png')
known.setdefault('aoa3:hiver',{}).setdefault('builds_crafting_ui',[]).append('moonlit-hive-crafting-study-v1.png')
known.setdefault('aoa3:hive_cracker',{}).setdefault('builds_crafting_ui',[]).append('moonlit-hive-crafting-study-v1.png')
known.setdefault('aoa3:hive_blaster',{}).setdefault('builds_crafting_ui',[]).append('moonlit-hive-crafting-study-v1.png')
known.setdefault('aoa3:hive_howitzer',{}).setdefault('builds_crafting_ui',[]).append('moonlit-hive-crafting-study-v1.png')
known.setdefault('aoa3:hive_staff',{}).setdefault('builds_crafting_ui',[]).append('moonlit-hive-crafting-study-v1.png')
known.setdefault('aoa3:clownimator',{}).setdefault('sights_scopes',[]).append('clown-split-flag-alignment-study-v1.png')
known.setdefault('aoa3:clowno_pulse',{}).setdefault('sights_scopes',[]).append('clown-split-flag-alignment-study-v1.png')
known.setdefault('aoa3:clownershot',{}).setdefault('sights_scopes',[]).append('clown-split-flag-alignment-study-v1.png')
known.setdefault('aoa3:flaming_fury',{}).setdefault('sights_scopes',[])
if 'flaming-fury-dragon-eye-sight-study-v1.png' not in known['aoa3:flaming_fury']['sights_scopes']: known['aoa3:flaming_fury']['sights_scopes'].append('flaming-fury-dragon-eye-sight-study-v1.png')
known.setdefault('aoa3:happy_haunter',{}).setdefault('sights_scopes',[])
if 'happy-haunter-party-hat-sight-study-v1.png' not in known['aoa3:happy_haunter']['sights_scopes']: known['aoa3:happy_haunter']['sights_scopes'].append('happy-haunter-party-hat-sight-study-v1.png')
known.setdefault('aoa3:happy_haunter',{}).setdefault('audio_accessibility',[])
if 'happy-haunter-party-hat-sight-study-v1.png' not in known['aoa3:happy_haunter']['audio_accessibility']: known['aoa3:happy_haunter']['audio_accessibility'].append('happy-haunter-party-hat-sight-study-v1.png')
known.setdefault('aoa3:colour_cannon',{}).setdefault('muzzle_charge_feedback',[])
if 'colour-cannon-living-rainbow-study-v1.png' not in known['aoa3:colour_cannon']['muzzle_charge_feedback']: known['aoa3:colour_cannon']['muzzle_charge_feedback'].append('colour-cannon-living-rainbow-study-v1.png')
known.setdefault('aoa3:colour_cannon',{}).setdefault('motion_inspect_reload',[])
if 'colour-cannon-living-rainbow-study-v1.png' not in known['aoa3:colour_cannon']['motion_inspect_reload']: known['aoa3:colour_cannon']['motion_inspect_reload'].append('colour-cannon-living-rainbow-study-v1.png')
known.setdefault('aoa3:abyssro',{}).setdefault('sights_scopes',[])
if 'abyssro-living-eye-sight-study-v1.png' not in known['aoa3:abyssro']['sights_scopes']: known['aoa3:abyssro']['sights_scopes'].append('abyssro-living-eye-sight-study-v1.png')
known.setdefault('aoa3:blissful_blast',{}).setdefault('stickers_emblems',[])
if 'blissful-blast-smile-decals-study-v1.png' not in known['aoa3:blissful_blast']['stickers_emblems']: known['aoa3:blissful_blast']['stickers_emblems'].append('blissful-blast-smile-decals-study-v1.png')
known.setdefault('aoa3:blood_iron',{}).setdefault('barrels_muzzles_converters',[])
if 'blood-iron-dragon-jaw-attachment-study-v1.png' not in known['aoa3:blood_iron']['barrels_muzzles_converters']: known['aoa3:blood_iron']['barrels_muzzles_converters'].append('blood-iron-dragon-jaw-attachment-study-v1.png')
known.setdefault('aoa3:blood_iron',{}).setdefault('skins_finishes_mastercraft',[])
if 'blood-iron-dragon-jaw-attachment-study-v1.png' not in known['aoa3:blood_iron']['skins_finishes_mastercraft']: known['aoa3:blood_iron']['skins_finishes_mastercraft'].append('blood-iron-dragon-jaw-attachment-study-v1.png')
known.setdefault('aoa3:haunter_rifle',{}).setdefault('sights_scopes',[])
if 'haunter-rifle-flame-focus-study-v1.png' not in known['aoa3:haunter_rifle']['sights_scopes']: known['aoa3:haunter_rifle']['sights_scopes'].append('haunter-rifle-flame-focus-study-v1.png')
known.setdefault('aoa3:skullifact',{}).setdefault('sights_scopes',[])
if 'skullifact-soulflame-sight-study-v1.png' not in known['aoa3:skullifact']['sights_scopes']: known['aoa3:skullifact']['sights_scopes'].append('skullifact-soulflame-sight-study-v1.png')
known.setdefault('aoa3:skullette',{}).setdefault('sights_scopes',[])
if 'skullette-purple-flame-sight-study-v1.png' not in known['aoa3:skullette']['sights_scopes']: known['aoa3:skullette']['sights_scopes'].append('skullette-purple-flame-sight-study-v1.png')
known.setdefault('aoa3:abominator',{}).setdefault('grips_stocks_supports',[])
if 'abominator-handling-surfaces-study-v1.png' not in known['aoa3:abominator']['grips_stocks_supports']: known['aoa3:abominator']['grips_stocks_supports'].append('abominator-handling-surfaces-study-v1.png')
known.setdefault('aoa3:abominator',{}).setdefault('muzzle_charge_feedback',[])
if 'abominator-shot-feedback-study-v1.png' not in known['aoa3:abominator']['muzzle_charge_feedback']: known['aoa3:abominator']['muzzle_charge_feedback'].append('abominator-shot-feedback-study-v1.png')
known.setdefault('aoa3:abominator',{}).setdefault('motion_inspect_reload',[])
if 'abominator-inspect-motion-study-v1.png' not in known['aoa3:abominator']['motion_inspect_reload']: known['aoa3:abominator']['motion_inspect_reload'].append('abominator-inspect-motion-study-v1.png')
known.setdefault('aoa3:abominator',{}).setdefault('audio_accessibility',[])
if 'abominator-audio-accessibility-direction-v1.png' not in known['aoa3:abominator']['audio_accessibility']: known['aoa3:abominator']['audio_accessibility'].append('abominator-audio-accessibility-direction-v1.png')
known.setdefault('aoa3:predigun',{}).setdefault('magazines_feed_resource',[])
if 'predigun-bone-belt-motion-study-v1.png' not in known['aoa3:predigun']['magazines_feed_resource']: known['aoa3:predigun']['magazines_feed_resource'].append('predigun-bone-belt-motion-study-v1.png')
known.setdefault('aoa3:predigun',{}).setdefault('motion_inspect_reload',[])
if 'predigun-bone-belt-motion-study-v1.png' not in known['aoa3:predigun']['motion_inspect_reload']: known['aoa3:predigun']['motion_inspect_reload'].append('predigun-bone-belt-motion-study-v1.png')
known.setdefault('aoa3:darkener',{}).setdefault('grips_stocks_supports',[])
if 'darkener-support-drum-study-v1.png' not in known['aoa3:darkener']['grips_stocks_supports']: known['aoa3:darkener']['grips_stocks_supports'].append('darkener-support-drum-study-v1.png')
known.setdefault('aoa3:darkener',{}).setdefault('magazines_feed_resource',[])
if 'darkener-support-drum-study-v1.png' not in known['aoa3:darkener']['magazines_feed_resource']: known['aoa3:darkener']['magazines_feed_resource'].append('darkener-support-drum-study-v1.png')
known.setdefault('aoa3:predator',{}).setdefault('muzzle_charge_feedback',[])
if 'predator-living-arc-study-v1.png' not in known['aoa3:predator']['muzzle_charge_feedback']: known['aoa3:predator']['muzzle_charge_feedback'].append('predator-living-arc-study-v1.png')
known.setdefault('aoa3:electinator',{}).setdefault('muzzle_charge_feedback',[])
if 'electinator-electrical-pulse-study-v1.png' not in known['aoa3:electinator']['muzzle_charge_feedback']: known['aoa3:electinator']['muzzle_charge_feedback'].append('electinator-electrical-pulse-study-v1.png')
known.setdefault('aoa3:soul_spark',{}).setdefault('muzzle_charge_feedback',[])
if 'soul-spark-living-lightning-study-v1.png' not in known['aoa3:soul_spark']['muzzle_charge_feedback']: known['aoa3:soul_spark']['muzzle_charge_feedback'].append('soul-spark-living-lightning-study-v1.png')
known.setdefault('aoa3:blood_drainer',{}).setdefault('motion_inspect_reload',[])
if 'blood-drainer-living-tentacle-motion-study-v1.png' not in known['aoa3:blood_drainer']['motion_inspect_reload']: known['aoa3:blood_drainer']['motion_inspect_reload'].append('blood-drainer-living-tentacle-motion-study-v1.png')
known.setdefault('aoa3:blood_drainer',{}).setdefault('muzzle_charge_feedback',[])
if 'blood-drainer-living-tentacle-motion-study-v1.png' not in known['aoa3:blood_drainer']['muzzle_charge_feedback']: known['aoa3:blood_drainer']['muzzle_charge_feedback'].append('blood-drainer-living-tentacle-motion-study-v1.png')
known.setdefault('aoa3:death_ray',{}).setdefault('skins_finishes_mastercraft',[])
if 'death-ray-finishes-trinkets-study-v1.png' not in known['aoa3:death_ray']['skins_finishes_mastercraft']: known['aoa3:death_ray']['skins_finishes_mastercraft'].append('death-ray-finishes-trinkets-study-v1.png')
known.setdefault('aoa3:death_ray',{}).setdefault('charms_trinkets',[])
if 'death-ray-finishes-trinkets-study-v1.png' not in known['aoa3:death_ray']['charms_trinkets']: known['aoa3:death_ray']['charms_trinkets'].append('death-ray-finishes-trinkets-study-v1.png')
known.setdefault('aoa3:death_ray',{}).setdefault('stickers_emblems',[])
if 'death-ray-finishes-trinkets-study-v1.png' not in known['aoa3:death_ray']['stickers_emblems']: known['aoa3:death_ray']['stickers_emblems'].append('death-ray-finishes-trinkets-study-v1.png')
known.setdefault('aoa3:chilli_chugger',{}).setdefault('stickers_emblems',[])
if 'chilli-chugger-pepper-cosmetics-study-v1.png' not in known['aoa3:chilli_chugger']['stickers_emblems']: known['aoa3:chilli_chugger']['stickers_emblems'].append('chilli-chugger-pepper-cosmetics-study-v1.png')
known.setdefault('aoa3:chilli_chugger',{}).setdefault('charms_trinkets',[])
if 'chilli-chugger-pepper-cosmetics-study-v1.png' not in known['aoa3:chilli_chugger']['charms_trinkets']: known['aoa3:chilli_chugger']['charms_trinkets'].append('chilli-chugger-pepper-cosmetics-study-v1.png')
known.setdefault('aoa3:light_blaster',{}).setdefault('sights_scopes',[])
if 'light-blaster-crystal-geometry-focus-v1.png' not in known['aoa3:light_blaster']['sights_scopes']: known['aoa3:light_blaster']['sights_scopes'].append('light-blaster-crystal-geometry-focus-v1.png')
known.setdefault('aoa3:light_blaster',{}).setdefault('motion_inspect_reload',[])
if 'light-blaster-crystal-geometry-focus-v1.png' not in known['aoa3:light_blaster']['motion_inspect_reload']: known['aoa3:light_blaster']['motion_inspect_reload'].append('light-blaster-crystal-geometry-focus-v1.png')
known.setdefault('aoa3:dark_beast',{}).setdefault('motion_inspect_reload',[])
if 'dark-beast-living-jaw-study-v1.png' not in known['aoa3:dark_beast']['motion_inspect_reload']: known['aoa3:dark_beast']['motion_inspect_reload'].append('dark-beast-living-jaw-study-v1.png')
known.setdefault('aoa3:dark_beast',{}).setdefault('muzzle_charge_feedback',[])
if 'dark-beast-living-jaw-study-v1.png' not in known['aoa3:dark_beast']['muzzle_charge_feedback']: known['aoa3:dark_beast']['muzzle_charge_feedback'].append('dark-beast-living-jaw-study-v1.png')
known.setdefault('aoa3:moon_destroyer',{}).setdefault('skins_finishes_mastercraft',[])
if 'moon-destroyer-lunar-cosmetics-study-v1.png' not in known['aoa3:moon_destroyer']['skins_finishes_mastercraft']: known['aoa3:moon_destroyer']['skins_finishes_mastercraft'].append('moon-destroyer-lunar-cosmetics-study-v1.png')
known.setdefault('aoa3:moon_destroyer',{}).setdefault('charms_trinkets',[])
if 'moon-destroyer-lunar-cosmetics-study-v1.png' not in known['aoa3:moon_destroyer']['charms_trinkets']: known['aoa3:moon_destroyer']['charms_trinkets'].append('moon-destroyer-lunar-cosmetics-study-v1.png')
known.setdefault('aoa3:moon_destroyer',{}).setdefault('stickers_emblems',[])
if 'moon-destroyer-lunar-cosmetics-study-v1.png' not in known['aoa3:moon_destroyer']['stickers_emblems']: known['aoa3:moon_destroyer']['stickers_emblems'].append('moon-destroyer-lunar-cosmetics-study-v1.png')
for known_id, known_groups in known.items():
 if known_id not in {w['id'] for w in catalog['weapons']}: raise ValueError('Unknown weapon in study map: '+known_id)
 if set(known_groups)-lookup: raise ValueError('Unknown study group: '+str(set(known_groups)-lookup))
rows=[]
for w in catalog['weapons']:
 rows.append({'id':w['id'],'name':w['name'],'families':w['families'],'release_lanes':w['lanes'],'base_concept':w['concept'],'base_art_review':'open','existing_feature_manifest':oldby.get(w['id'],{}).get('manifest'),'existing_feature_record_preserved':w['id'] in oldby,'dedicated_sheets':{gid:{'status':'partial_candidate' if known.get(w['id'],{}).get(gid) else 'requires_reconciliation','files':known.get(w['id'],{}).get(gid,[]),'owner_approved_omission':None}for gid,_,_ in groups},'implementation_acceptance':False,'qa_acceptance':False})
for row in rows:
 if row['id'] in ['aoa3:clownimator','aoa3:clowno_pulse','aoa3:clownershot']:
  row['dedicated_sheets']['sights_scopes']['review_note']='Focused appearance only; old side transition superseded by paired split-open apertures with vertical pole alignment. Replacement integrated transition artwork remains open.'
d={'schema':1,'revision':'20261022-dragon-and-lunar-studies-1124-customization','scope':'All 434 audited raw release-union IDs; 411 first-target identities. Registry identities are not deduplicated by shared art.','base_catalog':'weapon-concept-catalog.json','base_catalog_sha256':hashlib.sha256((R/'weapon-concept-catalog.json').read_bytes()).hexdigest(),'feature_catalog':'weapon-feature-catalog.json','required_features':[f['id']for f in features['features']],'sheet_groups':[{'id':i,'title':t,'feature_ids':f}for i,t,f in groups],'policy':['Base art coverage does not complete dedicated customization art.','No category may be silently omitted. A family-appropriate equivalent or explicitly approved omission must be recorded.','Existing evidence and old 228-firearm coverage are retained, not reset or replaced. Requires reconciliation does not assert that no older artwork exists.','Partial candidate is not complete or approved. Each option and compatibility combination needs individual review.','Separate concept, implementation and native AoA plus TaCZ QA. No static artwork proves animation or gameplay.','Cosmetic channels cannot silently alter source damage, resource costs or target rules; functional conversions require separate explicit specification.'],'weapons':rows}
(P/'weapon-customization-art-register.json').write_text(json.dumps(d,indent=2)+'\n');print('Registered',len(rows),'IDs with',len(groups),'dedicated sheet groups and',len(d['required_features']),'required feature groups')
