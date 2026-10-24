#!/usr/bin/env python3
"""Qualify only two concrete omissions discovered during the final evidence challenge."""
from pathlib import Path
import copy,hashlib,json,re,sys
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent
sys.path.insert(0,str(PARENT));sys.path.insert(0,str(ROOT))
import research as r;import collect as c;import discover as d
r.CACHE=ROOT/'cache';r.CACHE.mkdir(exist_ok=True);c.ROOT=ROOT

def main():
 records=r.load(ROOT/'extra-records.json',{});proof=r.load(ROOT/'late-qualification.json',{})
 key='mr-rwImxLJB'
 if key not in records:
  response=r.get('https://api.modrinth.com/v2/project/rwImxLJB');project=response.get('json',{});assert project.get('id')=='rwImxLJB'
  team=r.get('https://api.modrinth.com/v2/team/'+project['team']+'/members').get('json',[])
  authors=[{'name':v['user']['username'],'url':'https://modrinth.com/user/'+v['user']['username'],'role':v.get('role','')} for v in team if v.get('user')]
  item,error=c.mr_project(project,{'author':authors[0]['name'] if authors else 'See creator credits'});assert item and not error,error
  item['authors']=authors or item['authors'];body=project.get('body','')
  for alt,url in re.findall(r'!\[([^\]]*)\]\((https?://[^)]+)\)',body):
   if not re.search(r'badge|shields.io|discord|donat|patreon|hosting',url,re.I):item['gallery'].append({'url':url,'alt':alt or 'Originium Weapons creator preview','role':'Creator description image','sourceUrl':item['projectUrl']})
  c.media(item);assert item['media']
  for media in item['media']:media['src']='tacz-deep-discovery/'+media['src']
  item=c.decorate(item);item['descriptionExcerpt']=' '.join(item.get('descriptionExcerpt','').split()[:100])
  reason='A creator-authored Arknights and Metal Gear crossover gunpack with fictional Originium-powered firearms, separate from the same creator\'s older Metal Gear Solid V pack.'
  caution='The title specifies TaCZ 1.1.5+ and Arcana while the installation prose says 1.1.4+. Treat the exact current file requirements as authoritative; the conflicting prose is not silently resolved into a compatibility promise.'
  item.update(type='Gun / content pack',ecosystem='TaCZ',curation='Study anchor',studyPriority=110,access='Free public release; optional creator sponsorship',creatorAccessNote=caution,maintenanceNotice='No discontinuation notice found')
  item['themes']=list(dict.fromkeys(item['themes']+['Deep discoveries','Hidden gems','Creator channels']));item['inspiration']=[reason]+item['inspiration'];item['cautions'].insert(0,caution)
  item['links']+=[{'provider':'Creator channel','label':'Creator Bilibili page','url':'https://space.bilibili.com/76824223','verified':True,'kind':'creator-channel','verification':'Exact creator-provided link','lastChecked':response['checkedAt']},{'provider':'Creator support','label':'Creator sponsorship','url':'https://ifdian.net/a/youde79','verified':True,'kind':'creator-channel','verification':'Exact creator-provided sponsorship destination','lastChecked':response['checkedAt']}]
  metric={'id':key,'provider':'Modrinth','url':item['projectUrl'],'downloads':project.get('downloads'),'followers':project.get('followers'),'favorites':None,'rating':None,'ratingCount':None,'checkedAt':response['checkedAt'],'sourceHash':hashlib.sha256(json.dumps(project,sort_keys=True,ensure_ascii=False).encode()).hexdigest()}
  records[key]={'item':item,'metric':metric,'editorial':{'id':key,'shortlist':True,'type':'Gunpack (ZIP)','reason':reason,'caution':caution}}
  proof[key]={'source':item['projectUrl'],'creatorNames':[a['name'] for a in authors],'publishedReleaseRecords':len(item['releases']),'sourceHash':metric['sourceHash'],'checkedAt':response['checkedAt']}
 key='gh-1429852946';full='miku3928/ai-tacz-gunpack';source='https://github.com/'+full
 if key not in records:
  response=d.gh_get('https://api.github.com/repos/'+full);project=response.get('json',{});assert project.get('id')==1429852946
  rels=d.gh_get('https://api.github.com/repos/'+full+'/releases?per_page=100').get('json',[]);release=next(v for v in rels if v['tag_name']=='v1.0.0')
  asset=next(a for a in release['assets'] if a['name']=='Rifle3_GunPack_1.0.0.zip')
  branch=project['default_branch'];gallery=[{'url':'https://raw.githubusercontent.com/'+full+'/'+branch+'/'+path,'alt':label,'role':'Creator model-render preview (AI-assisted project)','sourceUrl':source} for path,label in [('docs/images/hero.png','R3 Carbine creator hero render'),('docs/images/side.png','R3 Carbine creator side render'),('docs/images/catalog_groups.png','R3 Carbine creator model groups')]]
  temp={'name':'R3 Carbine','projectUrl':source,'icon':None,'gallery':gallery};c.media(temp);assert temp.get('media')
  for media in temp['media']:media['src']='tacz-deep-discovery/'+media['src']
  reason='A newly published, source-available experimental carbine with a documented modeling and first-person authoring workflow. This is a distinct gun release, not the separate ammo-only or editor download in the same repository.'
  caution='The creator discloses AI-assisted model/texture production and a high-polygon mesh requiring TML. The creator\'s native test and performance claims have not been independently reproduced. Keep this as an experimental design/authoring reference, not a measured performance recommendation.'
  checked=response['checkedAt'];file={'id':'gh-release-'+str(release['id']),'name':'R3 Carbine v1.0.0','date':release['published_at'],'versions':['1.20.1'],'loaders':['Forge'],'channel':'release','url':release['html_url'],'provider':'GitHub','compatibilityBasis':'Creator README declares Minecraft 1.20.1, Forge 47.4.10, TaCZ 1.1.8-hotfix2 and TML 0.1.8; not independently installed'}
  item={'id':key,'providerIds':{'github':project['id']},'name':'R3 Carbine','slug':'r3-carbine','summary':'Experimental TaCZ carbine with creator-disclosed AI-assisted source models, weapon attachments and a public v1.0.0 release.','descriptionExcerpt':'The creator publishes the gunpack separately from its ammo-only pack and first-person tuning utility. The release requires TaCZ and TML; the source contains a reproducible model/export workflow.','authors':[{'name':'miku3928','url':'https://github.com/miku3928'}],'type':'Gun / content pack','ecosystem':'TaCZ','edition':'Java','projectUrl':source,'links':[{'provider':'GitHub','label':'Creator source and documentation','url':source,'verified':True,'lastChecked':checked},{'provider':'GitHub release','label':'Exact gunpack release','url':release['html_url'],'verified':True,'lastChecked':checked}],'crosslinks':[],'provider':'GitHub','icon':None,'gallery':[],'media':temp['media'],'videos':[],'releases':[file],'versions':['1.20.1'],'loaders':['Forge'],'latest':file,'latestStable':file,'created':project['created_at'],'updated':release['published_at'],'downloads':None,'license':'Creator lists MIT code/documents and CC BY 4.0 models/textures','dependencies':[],'sourceRows':[],'checkedAt':checked,'tags':['TaCZ','Carbine','Experimental','AI-assisted creator project'],'themes':['Deep discoveries','Animation & handling','Modularity & attachments'],'curation':'Research discovery','studyPriority':55,'earlierPick':False,'priorityBasis':'Experimental source-backed design reference; not native runtime or performance proof','inspiration':[reason],'cautions':[caution,file['compatibilityBasis']],'access':'Free public source and release','creatorAccessNote':caution,'maintenanceNotice':'No discontinuation notice found','mediaStatus':'Creator model-render previews archived','activity':'Updated within 90 days','evidence':{'project':source,'releaseList':source+'/releases','releaseScope':'Exact creator release and firearm ZIP identity verified; README-declared version pair retained separately from runtime testing.'}}
  # GitHub stars and tool/ammo downloads are not converted into gunpack favorites or download totals.
  metric={'id':key,'provider':'GitHub','url':release['html_url'],'downloads':None,'favorites':None,'followers':None,'rating':None,'ratingCount':None,'checkedAt':checked,'sourceHash':hashlib.sha256(json.dumps(release,sort_keys=True,ensure_ascii=False).encode()).hexdigest()}
  records[key]={'item':item,'metric':metric,'editorial':{'id':key,'shortlist':False,'type':'Creator-hosted gunpack','reason':reason,'caution':caution}}
  proof[key]={'source':source,'releaseUrl':release['html_url'],'releaseDate':release['published_at'],'gunAssetId':asset['id'],'gunAssetName':asset['name'],'imageCount':len(item['media']),'creatorAIAssistanceDisclosed':True,'ourImageGenerationUsed':False,'modBinariesDownloaded':False,'inventedMetrics':False}
 r.save(ROOT/'extra-records.json',records);r.save(ROOT/'late-qualification.json',proof);print(json.dumps(proof,indent=2),flush=True)
if __name__=='__main__':main()
