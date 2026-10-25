#!/usr/bin/env python3
"""Retry only the named rate-limit failure, after its Retry-After window; preserve all other evidence."""
from pathlib import Path
import hashlib,json,time,sys,io,zipfile,os
import requests
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT));import resume as previous;import research_community as c

def main():
 url='https://api.github.com/repos/Herbertofury/Advent-of-Ascension/actions/artifacts/12611824114/zip'
 if not (ROOT/'creator-video-evidence.json').exists():
  res=requests.get(url,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN']},timeout=(10,90));res.raise_for_status();assert hashlib.sha256(res.content).hexdigest()=='a9b8cc239b3ca4a834f847a05fe11c6b2dd46ad418fede19095e19c63a654fd5'
  with zipfile.ZipFile(io.BytesIO(res.content)) as z:
   for name in z.namelist():
    p=Path(name)
    if p.is_absolute() or '..' in p.parts or p.suffix!='.json':continue
    target=ROOT/p
    if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(name))
 report=ROOT/'manifest-evidence.json'
 if report.exists():
  data=json.loads(report.read_text())
  if data.get('terminal'):return
  if len(data.get('manifests',[]))==0 and any(x.get('status')==429 for x in data.get('pages',[])):
   (ROOT/'manifest-first-rate-limit.json').write_bytes(report.read_bytes());report.unlink()
   for cache in (ROOT/'cache').glob('github-*.json'):
    body=json.loads(cache.read_text())
    if body.get('status')==429:cache.unlink()
 # The previous 20.6-second window has elapsed between workflow stages; finite backpressure handles a new 429.
 original=previous.gh
 def request(path):
  result=original(path)
  if result.get('status')==429:
   message=(result.get('data') or {}).get('message','');import re
   match=re.search(r'try again in ([0-9.]+)s',message)
   if match and float(match.group(1))<=90:
    time.sleep(float(match.group(1))+1)
    cache=ROOT/'cache'/('github-'+hashlib.sha256(result['url'].encode()).hexdigest()+'.json')
    cache.unlink(missing_ok=True);return original(path)
  return result
 previous.gh=request
 evidence=previous.manifests();coverage=c.load('coverage.json',{})
 coverage.update(manifestFilesRead=len(evidence['manifests']),manifestRepositoriesRead=len(evidence['repositories']),manifestTraversalTerminal=evidence['terminal'])
 c.save('coverage.json',coverage)
if __name__=='__main__':main()
