#!/usr/bin/env python3
"""Repair Markdown literal text without changing catalog data or explorer behavior."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import build

def run():
 path=ROOT/'build.py';text=path.read_text(encoding='utf-8')
 old="def md(s):return html.escape(str(s or '')).replace('|','&#124;').replace('\\n',' ')"
 new="def md(s):\n value=html.escape(str(s or '')).replace('|','&#124;').replace('\\n',' ')\n for ch in '*_`[]~':value=value.replace(ch,'&#'+str(ord(ch))+';')\n return value"
 assert old in text or new in text,'Renderer source changed; reconcile literal-text fix'
 if old in text:path.write_text(text.replace(old,new),encoding='utf-8')
 import importlib
 importlib.reload(build)
 data=json.loads((ROOT/'catalog.json').read_text());proof=json.loads((ROOT/'qa/data-verification.json').read_text())
 original=hashlib.sha256((ROOT/'catalog.json').read_bytes()).hexdigest()
 pages=build.make_wiki(data,proof)
 assert hashlib.sha256((ROOT/'catalog.json').read_bytes()).hexdigest()==original
 expected='&#91;TaCZ&#93;(COMPILATION) Bitlod&#x27;s inspiring guns'
 assert expected in pages['Minecraft-Gun-Mod-Inspirations-gun-content-pack']
 report={'catalogUnchangedSha256':original,'pagesRegenerated':len(pages),'literalTitleRegression':'[TaCZ](COMPILATION) Bitlod\'s inspiring guns','passed':True}
 (ROOT/'qa/literal-title-verification.json').write_text(json.dumps(report,indent=2))
 print(json.dumps(report),flush=True)
if __name__=='__main__':run()
