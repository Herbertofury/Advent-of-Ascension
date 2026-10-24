#!/usr/bin/env python3
"""Small, idempotent correctness delta over the completed deep-discovery implementation."""
from pathlib import Path
import ast
ROOT=Path(__file__).resolve().parent

def replace(text,old,new,label):
 assert old in text or new in text,'Reconcile changed source: '+label
 return text.replace(old,new)

def main():
 path=ROOT/'build_deep.py';text=path.read_text(encoding='utf-8')
 old="  if key not in parent_index:parent_index[key]=copy.deepcopy(item)"
 new="  if key not in parent_index or key not in load(ROOT/'baseline.json')['parent']:parent_index[key]=copy.deepcopy(item)"
 text=replace(text,old,new,'owned new-record preview refresh')
 old="   old=parent_index[key];old['themes']=list(dict.fromkeys(old.get('themes',[])+['Deep discoveries']+(['Hidden gems'] if spec.get('shortlist') else [])))"
 new=old+"\n   if item.get('preferredMediaSha256') and any(m['sha256']==item['preferredMediaSha256'] for m in old.get('media',[])):old['preferredMediaSha256']=item['preferredMediaSha256']"
 text=replace(text,old,new,'existing selected record exact preview')
 old="  jsfile.write_text(js,encoding='utf-8')"
 new="""  js=js.replace("function mediaFor(x){return (x.media||[]).find(m=>m.role!=='Project icon')||(x.media||[])[0];}","function mediaFor(x){return (x.media||[]).find(m=>m.sha256===x.preferredMediaSha256)||(x.media||[]).find(m=>m.role!=='Project icon')||(x.media||[])[0];}")
  js=js.replace("function gallery(id,index=0){const x=MAP.get(id);if(!x?.media?.length){openDetail(id);return;}lightboxId=id;", "function gallery(id,index=null){const x=MAP.get(id);if(!x?.media?.length){openDetail(id);return;}if(index===null)index=Math.max(0,x.media.findIndex(m=>m.sha256===x.preferredMediaSha256));lightboxId=id;")
  jsfile.write_text(js,encoding='utf-8')"""
 text=replace(text,old,new,'same reviewed card and lightbox preview')
 old=" decisions=[]\n for x in found:"
 new=""" decisions=[]
 extras=load(ROOT/'extra-decisions.json',{})
 _all_records={**load(ROOT/'qualified-records.json',{}),**load(ROOT/'extra-records.json',{})}
 found=list(found)
 _seen={x['id'] for x in found}
 for key,record in _all_records.items():
  if key not in _seen:found.append({'id':key,'name':record['item']['name'],'url':record['item']['projectUrl'],'summary':record['item']['summary'],'provider':record['item']['provider']})
 for x in found:"""
 text=replace(text,old,new,'creator-only source reconciled in discovered identities')
 old="  decisions.append({'id':key,'name':x.get('name'),'url':x.get('url'),'status':state,'reason':reason})"
 new="  if key in extras and key not in accepted:state,reason=extras[key]['status'],extras[key]['reason']\n"+old
 text=replace(text,old,new,'manually reviewed mirror and utility dispositions')
 ast.parse(text);path.write_text(text,encoding='utf-8')
 print('Reviewed media and source-identity delta applied without repeating research.',flush=True)
if __name__=='__main__':main()
