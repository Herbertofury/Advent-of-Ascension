#!/usr/bin/env python3
"""Small tested-source overlay applied after checksum-verified UI decoding."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def run():
 p=ROOT/'app.js';s=p.read_text(encoding='utf-8')
 old="const versions=terms.filter(t=>t.key==='version'&&!t.negative).map(t=>t.value),loaders=terms.filter(t=>t.key==='loader'&&!t.negative).map(t=>t.value);"
 new="const versions=[...terms.filter(t=>t.key==='version'&&!t.negative).map(t=>t.value),...(state.version?[state.version]:[])],loaders=[...terms.filter(t=>t.key==='loader'&&!t.negative).map(t=>t.value),...(state.loader?[state.loader]:[])];"
 assert old in s or new in s,'Compatibility filter source changed; reconcile before patching'
 s=s.replace(old,new)
 p.write_text(s,encoding='utf-8')
 # Use the browser already installed on the runner; no managed-browser download is needed.
 test=ROOT/'qa'/'browser_test.py';t=test.read_text(encoding='utf-8')
 t=t.replace("query='version:'+pair['versions'][0]+' loader:'+pair['loaders'][0]", "query='version:'+pair['versions'][0]+' loader:'+pair['loaders'][0]")
 test.write_text(t,encoding='utf-8')
if __name__=='__main__':run()
