#!/usr/bin/env python3
"""Resume only provider-rate-limited manifest metadata; no repeat of creator discovery."""
from pathlib import Path
import hashlib,json,time,sys,io,zipfile,os,re
import requests
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT));import resume as previous;import research_community as c

def main():
 if not (ROOT/'creator-video-evidence.json').exists():
  url='https://api.github.com/repos/Herbertofury/Advent-of-Ascension/actions/artifacts/12611824114/zip'
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
  if not data.get('manifests') and any(x.get('status')==429 for x in data.get('pages',[])):
   (ROOT/'manifest-prior-rate-limit.json').write_bytes(report.read_bytes());report.unlink()
   for cache in (ROOT/'cache').glob('github-*.json'):
    if json.loads(cache.read_text()).get('status')==429:cache.unlink()
 original=previous.gh;last=[0.0];recovery=[]
 def request(path):
  pause=.35-(time.monotonic()-last[0])
  if pause>0:time.sleep(pause)
  result=original(path);last[0]=time.monotonic()
  for attempt in range(2):
   if result.get('status')!=429:break
   body=result.get('data') or {};message=body.get('message','') if isinstance(body,dict) else str(body)
   match=re.search(r'try again in ([0-9.]+)(ms|s)',message)
   if not match:break
   delay=float(match.group(1))/(1000 if match.group(2)=='ms' else 1)
   if delay>90:break
   recovery.append({'url':result['url'],'waitSeconds':delay,'attempt':attempt+1,'reason':'Explicit provider response, not an unchanged speculative retry'})
   time.sleep(delay+1)
   cache=ROOT/'cache'/('github-'+hashlib.sha256(result['url'].encode()).hexdigest()+'.json');cache.unlink(missing_ok=True)
   result=original(path);last[0]=time.monotonic()
  return result
 previous.gh=request;evidence=previous.manifests();coverage=c.load('coverage.json',{})
 coverage.update(manifestFilesRead=len(evidence['manifests']),manifestRepositoriesRead=len(evidence['repositories']),manifestTraversalTerminal=evidence['terminal'],manifestLimitation=evidence.get('limitation',''))
 c.save('manifest-rate-recovery.json',recovery);c.save('coverage.json',coverage)
if __name__=='__main__':main()
