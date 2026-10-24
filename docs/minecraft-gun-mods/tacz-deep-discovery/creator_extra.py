#!/usr/bin/env python3
"""Add the publicly documented creator-only gunpack without inventing a download listing."""
from pathlib import Path
import datetime,hashlib,json,sys
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));import research as r;import collect as c
r.CACHE=ROOT/'cache';c.ROOT=ROOT
ID='bilibili-BV1MBEMzNEkJ'
SOURCE='https://www.bilibili.com/list/407541278?bvid=BV1MBEMzNEkJ&oid=114488376368078'

def main():
 path=ROOT/'extra-records.json'
 if path.exists():return
 response=r.get('https://api.bilibili.com/x/web-interface/view?bvid=BV1MBEMzNEkJ');body=response.get('json',{});assert body.get('code')==0,body
 data=body['data'];assert data['owner']['mid']==407541278 and data['bvid']=='BV1MBEMzNEkJ'
 # These are the creator's gun-specific episodes from the already resolved public collection.
 episodes=[]
 for section in (data.get('ugc_season') or {}).get('sections',[]):
  for episode in section.get('episodes',[]):
   title=episode.get('title','');arc=episode.get('arc') or {};bvid=episode.get('bvid') or arc.get('bvid')
   if bvid and any(term in title for term in ('爆弹手枪','重型爆矢枪','多管热熔','护教军套装','新月玫瑰','新武器追加')):
    episodes.append({'title':title,'bvid':bvid,'thumbnail':arc.get('pic') or episode.get('pic')})
 # The release video itself establishes identity. Gun-specific creator thumbnails supply the card previews.
 gallery=[];videos=[{'url':'https://www.bilibili.com/video/BV1MBEMzNEkJ/','label':'Creator release showcase','evidenceUrl':SOURCE,'verification':'Creator identity and public release description verified; full playback not reviewed'}]
 for episode in episodes:
  thumb=episode['thumbnail']
  if thumb:gallery.append({'url':thumb.replace('http://','https://'),'alt':'Unique Armaments: '+episode['title'],'role':'Creator gun-showcase preview','sourceUrl':'https://www.bilibili.com/video/'+episode['bvid']+'/'})
  videos.append({'url':'https://www.bilibili.com/video/'+episode['bvid']+'/','label':'Creator weapon update','evidenceUrl':SOURCE,'verification':'Named creator collection episode; full playback not reviewed'})
 gallery.append({'url':data['pic'].replace('http://','https://'),'alt':'Koei Unique Armaments creator release preview','role':'Creator release-video preview','sourceUrl':SOURCE})
 temp={'name':"Koei's Unique Armaments",'projectUrl':SOURCE,'icon':None,'gallery':gallery};c.media(temp)
 assert temp.get('media'),'No creator preview decoded'
 for media in temp['media']:media['src']='tacz-deep-discovery/'+media['src']
 published=datetime.datetime.fromtimestamp(data['pubdate'],datetime.timezone.utc).isoformat();checked=response['checkedAt']
 reason='Koei\'s creator-hosted collection includes distinctive fictional firearms, from boltpistol and paired heavy-gun concepts to energy and flame weapons. Its mixed melee/gun content is not mistaken for a melee-only accessory pack.'
 caution='The creator announces TaCZ 1.1.5+ support and Afdian distribution. An exact current downloadable file, Minecraft version/loader pair, edition price and payment requirement were not independently established. Follow the creator\'s pinned distribution post; no third-party reseller is linked.'
 item={'id':ID,'providerIds':{'bilibili':'BV1MBEMzNEkJ'},'name':"Koei's Unique Armaments",'slug':'koei-unique-armaments','summary':'Creator-hosted TaCZ firearm and melee collection with unusual fictional guns, energy weapons and dramatic handling concepts.','descriptionExcerpt':'The public creator release announcement requires TaCZ 1.1.5 or newer, names Apotheosis: Ragnarok as optional, and directs acquisition to the creator\'s pinned post and Afdian.','authors':[{'name':'Rhodes_koei / Koei','url':'https://space.bilibili.com/407541278'}],'type':'Gun / content pack','ecosystem':'TaCZ','edition':'Java','projectUrl':SOURCE,'links':[{'provider':'Creator source','label':'Exact creator release announcement','url':SOURCE,'verified':True,'lastChecked':checked},{'provider':'Creator channel','label':'Creator distribution and pinned posts','url':'https://space.bilibili.com/407541278','verified':True,'lastChecked':checked}],'crosslinks':[],'provider':'Creator-hosted','icon':None,'gallery':[],'videos':videos,'media':temp['media'],'releases':[],'versions':[],'loaders':[],'latest':None,'latestStable':None,'updated':published,'created':published,'downloads':None,'license':'See creator terms','dependencies':[],'sourceRows':[],'checkedAt':checked,'evidence':{'project':SOURCE,'releaseList':SOURCE,'releaseScope':'Creator-announced release and named gun-showcase episodes verified. No exact current downloadable file or version/loader combination independently established.'},'tags':['TaCZ','Creator-hosted','Fictional firearms'],'themes':['Deep discoveries','Hidden gems','Creator channels','Science fiction','Animation & handling'],'earlierPick':False,'curation':'Study anchor','studyPriority':110,'priorityBasis':'Editorial design reference, not a runtime quality or performance benchmark','inspiration':[reason],'cautions':[caution,'Video likes and views are not gunpack downloads, ratings or favorites.','Source research only; not independently installed or tested in Minecraft.'],'activity':'Creator release / exact file not established','access':'Creator distribution via Afdian; current edition/access not confirmed','creatorAccessNote':caution,'mediaStatus':'Creator video-preview images archived','maintenanceNotice':'No discontinuation notice found','reviewEvidence':{'creatorContentUrl':SOURCE,'checkedAt':checked,'sourceHash':hashlib.sha256(json.dumps(data,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),'qualification':'Creator public announcement and named firearm episodes establish an actual TaCZ gun-content collection; exact current purchase/download listing remains explicit unknown'}}
 metric={'id':ID,'provider':'Creator-hosted','url':SOURCE,'downloads':None,'favorites':None,'followers':None,'rating':None,'ratingCount':None,'checkedAt':checked,'sourceHash':item['reviewEvidence']['sourceHash']}
 editorial={'id':ID,'shortlist':True,'reason':reason,'type':'Creator-hosted gunpack','access':item['access'],'caution':caution}
 r.save(path,{ID:{'item':item,'metric':metric,'editorial':editorial}})
 r.save(ROOT/'creator-extra-proof.json',{'id':ID,'creatorMid':407541278,'releaseAnnouncement':SOURCE,'announcedAt':published,'gunShowcaseEpisodes':episodes,'imageCount':len(item['media']),'allGunpackPopularityMetricsUnknown':True,'videoMetricsNotUsedForPackRank':True,'privateFilesAccessed':False})
 # Explicitly reconcile meaningful international leads rather than count every repository as another pack.
 r.save(ROOT/'extra-decisions.json',{'gh-906053545':{'status':'already represented','reason':'Creator README and showcase link the same Khan\'s Oldguns Armory cf-1163154 already in the baseline; repository history is not another family.'},'gh-998164453':{'status':'unresolved lead','reason':'Japanese-language gunpack release exists, but the repository supplies only zero-byte assets/data placeholders and no specific firearm roster or reference preview. Not promoted as a quality recommendation without stronger creator evidence.'},'cf-1273925':{'status':'unresolved lead','reason':'UHPE references TaCZ and already exists in the parent atlas, but fetched creator text does not identify a distinct carried firearm roster; not padded into the gunpack collection.'},'cf-1510206':{'status':'excluded','reason':'Tacticool Equipment describes melee weapons/tools and armor intended for use alongside existing TaCZ guns.'},'cf-1544974':{'status':'excluded','reason':'BarrelSpell adds spells and existing-RPG projectile behavior rather than a new gun roster.'},'cf-1723858':{'status':'excluded','reason':'Tactical Camo is armor, melee weapons, grenades and equipment; no new firearm roster described.'}})
 print(json.dumps({'creatorExtra':ID,'images':len(item['media']),'gunEpisodeReferences':len(episodes),'metricsInvented':False}),flush=True)
if __name__=='__main__':main()
