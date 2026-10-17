"""Embed one original rendering core; no external-script startup dependency."""
from pathlib import Path
import hashlib,json,argparse
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--docs-root',type=Path,default=Path(__file__).parent);R=parser.parse_args().docs_root;core=(R/'viewer-renderer-core.js').read_bytes().decode('utf-8');start='/* shared-renderer-core:start */';end='/* shared-renderer-core:end */';proof=[]
for name in ['workstation-3d.html','block-models.html','crop-states.html']:
 p=R/name;s=p.read_bytes().decode('utf-8')
 if start in s:
  a=s.index(start);b=s.index(end,a)+len(end)
  while b<len(s)and s[b]in'\r\n':b+=1
 else:
  a=s.index('function viewDepth(')
  b=s.index('function createRenderer(',a)if name=='workstation-3d.html'else s.index('const view=',a)
 s=s[:a]+start+'\n'+core+end+'\n'+s[b:]
 if name=='workstation-3d.html':s=s.replace('models=new Map(data.models.map(m=>[m.id,m]));','models=new Map(data.models.map(m=>[m.id,{...m,textures:data.textures}]));')
 p.write_bytes(s.encode('utf-8'));embedded=s.split(start+'\n')[1].split(end)[0];assert embedded==core;proof.append(dict(file=name,embedded_sha256=hashlib.sha256(embedded.encode()).hexdigest()))
(R/'viewer-renderer-core-evidence.json').write_text(json.dumps(dict(scope='One original source core embedded in three viewers. No new startup network request or game-performance claim.',core_sha256=hashlib.sha256(core.encode()).hexdigest(),core_bytes=len(core.encode()),consumers=proof,texture_promise_limit=128,canvas_density_cap=2,canvas_dimension_cap=2048),indent=2)+'\n');print('Synchronized three renderer cores;',len(core.encode()),'bytes each')
