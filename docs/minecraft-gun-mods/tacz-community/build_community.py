#!/usr/bin/env python3
"""One deterministic additive build from frozen creator evidence; no hidden refresh."""
from pathlib import Path
import base64,hashlib,json,lzma,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
SOURCE_HASH='0663395f3b8ef555166203cb352d6bfd44c6f27de838bf0b6728dd26b7bf842a'

def main():
 raw=lzma.decompress(base64.b64decode((ROOT/'community-source.b64').read_text().strip(),validate=True));assert hashlib.sha256(raw).hexdigest()==SOURCE_HASH
 files=json.loads(raw);assert set(files)=={'apply_community.py','test_community.py','finalize_community.py'}
 for name,content in files.items():
  if name=='finalize_community.py':content=content.replace("manifest=load('manifest-evidence.json');coverage['manifestLimitation']=manifest.get('limitation','')", "manifest=load('manifest-evidence.json') if (ROOT/'manifest-evidence.json').exists() else {};coverage['manifestLimitation']=manifest.get('limitation',coverage.get('manifestLimitation',''))")
  (ROOT/name).write_text(content,encoding='utf-8')
 if not (ROOT/'qualified-records.json').exists():
  import hydrate_community
  hydrate_community.main()
 import finalize_community
 finalize_community.main()
 import apply_community
 apply_community.main()
if __name__=='__main__':main()
