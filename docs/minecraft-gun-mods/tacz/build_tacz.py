#!/usr/bin/env python3
"""Single deterministic entrypoint for the source-ranked TaCZ collection."""
from pathlib import Path
import base64,hashlib,importlib,json,lzma,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))

def main():
 import hydrate_additions
 hydrate_additions.main()
 manifest=ROOT/'ui-source-manifest.json'
 if manifest.exists():
  spec=json.loads(manifest.read_text());encoded=''.join((ROOT/name).read_text().strip() for name in spec['parts']);raw=lzma.decompress(base64.b64decode(encoded,validate=True))
  assert hashlib.sha256(raw).hexdigest()==spec['sha256'],'UI source transfer hash mismatch'
  files=json.loads(raw)
  assert set(files)=={'build_ui.py','ranking.js','tacz.css','test_tacz.py'}
  for name,content in files.items():(ROOT/name).write_text(content,encoding='utf-8')
 if (ROOT/'build_ui.py').exists():
  import build_ui
  build_ui.main()
 else:print('New source qualification checkpoint saved; interface source not yet staged.',flush=True)
if __name__=='__main__':main()
