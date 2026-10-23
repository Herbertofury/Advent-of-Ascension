#!/usr/bin/env python3
"""Fetch only newly selected public creator sources; never download mod binaries."""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse, urlunparse, urlencode
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;TACZ=PARENT/'tacz'
sys.path[:0]=[str(PARENT),str(TACZ)]
import research as r
import collect as c
import research_tacz as tr
r.CACHE=ROOT/'cache';r.CACHE.mkdir(exist_ok=True);c.ROOT=ROOT
orig_objects=c.objects

def normalize(o):
    if isinstance(o,dict):
        for k,v in list(o.items()):
            if v is None and k in {'latestFiles','files','members','categories','relatedProjects','gameVersions','flavors','dependencies'}:o[k]=[]
            else:normalize(v)
    elif isinstance(o,list):
        for x in o:normalize(x)
    return o
c.objects=lambda body,key:normalize(orig_objects(body,key))

def clean_url(url):
    for _ in range(3):
        p=urlparse(url);q=parse_qs(p.query)
        redir=q.get('remoteUrl') or q.get('url') or q.get('redirect')
        if redir and redir[0].startswith('http'):url=unquote(redir[0])
        else:break
    p=urlparse(url)
    q=[(k,v) for k,vs in parse_qs(p.query).items() if not k.startswith(('utm_','ref_')) for v in vs]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(q),p.fragment))

def channels(source,known=()):
    response=r.get(source);result=[]
    if response.get('text'):
        soup=BeautifulSoup(response['text'],'html.parser')
        description=soup.select_one('.project-description') or soup
        for tag in description.select('a[href]'):
            url=clean_url(tag['href']);host=urlparse(url).netloc.lower()
            provider=next((label for domain,label in [('patreon.com','Patreon'),('ko-fi.com','Ko-fi'),('afdian.com','Afdian'),('afdian.net','Afdian'),('ifdian.net','Afdian')] if host==domain or host.endswith('.'+domain)),None)
            if provider:result.append({'provider':provider,'label':provider+' creator channel','url':url,'kind':'creator-channel','verified':True,'verification':'Linked in the creator-controlled project description','evidenceUrl':source,'lastChecked':response['checkedAt']})
    for link in known:
        result.append({**link,'url':clean_url(link['url']),'kind':'creator-channel','verified':True,'verification':'Public creator source and destination identity inspected; private posts not accessed','evidenceUrl':source,'lastChecked':'2026-10-23'})
    return list({x['url']:x for x in result}.values())

def cf_record(spec):
    item,error=c.cf_project(spec['path'],[])
    assert item is not None,(spec['id'],error)
    assert item['id']==spec['id']
    source=r.get(spec['source']);soup=BeautifulSoup(source.get('text',''),'html.parser');description=soup.select_one('.project-description')
    blocked=set();promo=re.compile(r'discord|patreon|ko-fi|bisect|hosting|sponsor|donat|apexhosting',re.I)
    if description:
        for tag in description.select('img'):
            parent=tag.find_parent('a');url=parent.get('href','') if parent else ''
            if promo.search(tag.get('src','')+' '+tag.get('alt','')+' '+url):blocked.add(tag.get('src',''))
    item['gallery']=[m for m in item['gallery'] if m['url'] not in blocked]
    gallery=r.get(spec['source']+'/gallery');seen={m['url'] for m in item['gallery']}
    if gallery.get('text'):
        for tag in BeautifulSoup(gallery['text'],'html.parser').select('img'):
            url=tag.get('data-src') or tag.get('src','')
            if 'media.forgecdn.net/attachments/' in url and url not in seen and url not in blocked and not promo.search(url+' '+tag.get('alt','')):
                seen.add(url);item['gallery'].insert(0,{'url':url,'alt':tag.get('alt') or item['name']+' creator artwork','role':'Project gallery','sourceUrl':spec['source']+'/gallery'})
    c.media(item)
    assert item['media'],('No verified creator media',spec['id'])
    item=c.decorate(item)
    item['summary']=spec['summary'];item['descriptionExcerpt']='';item['inspiration']=[spec['idea']]
    item['access']=spec['access'];item['accessEvidence']=spec['source']
    item['cautions']=list(dict.fromkeys([spec['caution']]+item['cautions']))
    item['themes']=list(dict.fromkeys(item['themes']+['New discoveries']))
    item['links']+=channels(spec['source'])
    if any(x.get('kind')=='creator-channel' for x in item['links']):item['themes'].append('Creator channels')
    for m in item['media']:m['src']='creator-discoveries/'+m['src']
    item['ecosystem']='TaCZ';item['type']='Gun / content pack';item['creatorDiscovery']=True
    snap=tr.cf_snapshot(spec['source']);assert not snap.get('error'),snap
    snap={k:v for k,v in snap.items() if k!='description'}
    snap['descriptionExcerpt']=spec['summary'];snap['featureClaims']={}
    return item,snap

def aeg_record(spec):
    response=r.get(spec['url']);candidates=[];known=('2468b2297cbf4a3884d04c5a85562837','1f2311a4600d4648bfd55ec511c62a3c')
    text=response.get('text','')
    for raw in re.findall(r'https?[^\s<>"\\]+',text):
        url=raw.replace('&amp;','&')
        if 'patreonusercontent.com' in url and any(k in url for k in known):candidates.append(url)
    candidates+=spec['fallbackPublicMedia']
    media_record={'id':spec['id'],'name':spec['name'],'projectUrl':spec['url'],'icon':None,'gallery':[{'url':url,'alt':'AEG-Tactical public release preview','role':'Public creator preview','sourceUrl':spec['url']} for url in dict.fromkeys(candidates)]}
    c.media(media_record)
    for m in media_record.get('media',[]):m['src']='creator-discoveries/'+m['src']
    item={'id':spec['id'],'providerIds':{'patreonPost':'159166702'},'name':spec['name'],'slug':'aeg-tactical','summary':spec['summary'],'descriptionExcerpt':'','authors':[{'name':spec['author'],'url':spec['creatorUrl']}],'type':'Bedrock add-on','ecosystem':'Independent','edition':'Bedrock','projectUrl':spec['url'],'links':[{'provider':'Patreon','label':'Paid creator release and public details','url':spec['url'],'kind':'project','verified':True,'verification':spec['publicEvidence'],'lastChecked':'2026-10-23'},{'provider':'Patreon','label':'Official creator channel','url':spec['creatorUrl'],'kind':'creator-channel','verified':True,'verification':'Public creator identity','lastChecked':'2026-10-23'}],'provider':'Patreon','media':media_record.get('media',[]),'videos':[],'releases':[],'versions':[],'loaders':[],'updated':'','created':'','downloads':None,'license':'Creator custom license; see source','dependencies':[],'sourceRows':[],'checkedAt':'2026-10-23','tags':['Paid creator release'],'themes':['New discoveries','Creator channels','Animation & handling'],'inspiration':[spec['idea']],'cautions':spec['cautions'],'curation':'Research discovery','studyPriority':55,'priorityBasis':'Creator-source design reference, not a runtime benchmark','earlierPick':False,'latest':None,'latestStable':None,'activity':'Date not established','access':spec['access'],'accessEvidence':spec['url'],'creatorDiscovery':True,'mediaStatus':'Public release preview archived' if media_record.get('media') else 'Public preview URL unavailable; see creator post','evidence':{'project':spec['url'],'releaseList':spec['url'],'releaseScope':'Public creator description only. The purchased binary, its version/loader pairing and private attachments were not inspected.','publicDescriptionRead':True,'remoteFetchStatus':response.get('status')}}
    return item

def main():
    manifest=r.load(ROOT/'manifest.json');path=ROOT/'qualified-records.json'
    records=r.load(path,{});snapshots=r.load(ROOT/'metric-snapshots.json',{})
    for spec in manifest['newTaCZ']:
        if spec['id'] not in records:
            item,snapshot=cf_record(spec);records[item['id']]=item;snapshots[item['id']]=snapshot
            r.save(path,records);r.save(ROOT/'metric-snapshots.json',snapshots)
            print('Qualified',item['name'],'with',len(item['media']),'creator images',flush=True)
    paid=manifest['paidReference']
    if paid['id'] not in records:records[paid['id']]=aeg_record(paid);r.save(path,records)
    enrichment=r.load(ROOT/'channel-evidence.json',{})
    for spec in manifest['creatorEnrichment']:
        if spec['label'] in enrichment:continue
        links=channels(spec['source'],spec['knownLinks'])
        if spec.get('modrinthId'):
            data=r.get('https://api.modrinth.com/v2/project/'+spec['modrinthId']).get('json',{})
            for donation in data.get('donation_urls',[]):
                if 'patreon.com' in donation.get('url',''):links.append({'provider':'Patreon','label':'Official creator Patreon','url':clean_url(donation['url']),'kind':'creator-channel','verified':True,'verification':'Author-published Modrinth donation URL','evidenceUrl':spec['source'],'lastChecked':'2026-10-23'})
        enrichment[spec['label']]={**spec,'links':list({x['url']:x for x in links}.values())};r.save(ROOT/'channel-evidence.json',enrichment)
    assert len(records)==5
    report={'newTaCZ':len(manifest['newTaCZ']),'newBedrock':1,'newIds':list(records),'withImages':sum(bool(x['media']) for x in records.values()),'existingCreatorGroupsEnriched':len(enrichment),'paidFilesDownloaded':False,'privateContentAccessed':False,'notes':'The Bedrock paid reference is separate from the Java TaCZ collection. Missing media/metrics remain explicit.'}
    r.save(ROOT/'research-proof.json',report)
    from PIL import Image,ImageDraw,ImageFont
    out=ROOT/'qa';out.mkdir(exist_ok=True);font=ImageFont.load_default(size=15)
    media=[(x,m) for x in records.values() for m in x['media']]
    for start in range(0,len(media),16):
        batch=media[start:start+16];sheet=Image.new('RGB',(1440,270*((len(batch)+3)//4)),(232,232,232));draw=ImageDraw.Draw(sheet)
        for i,(item,m) in enumerate(batch):
            image=Image.open(PARENT/m['src']).convert('RGBA');image.thumbnail((350,215));x=i%4*360;y=i//4*270;sheet.paste(image,(x,y),image);draw.text((x+3,y+218),item['name'][:42],font=font,fill='black');draw.text((x+3,y+242),Path(m['src']).name[:32],font=font,fill='black')
        sheet.save(out/('new-media-%02d.jpg'%(start//16+1)),quality=94)
    print(json.dumps(report),flush=True)
if __name__=='__main__':main()
