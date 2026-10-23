#!/usr/bin/env python3
"""Scoped source overlays applied after checksum-verified UI decoding."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def replace_once(text,old,new,label):
 assert old in text or new in text,'Source changed; reconcile '+label
 return text.replace(old,new)

def run():
 p=ROOT/'app.js';s=p.read_text(encoding='utf-8')
 s=replace_once(s,"const versions=terms.filter(t=>t.key==='version'&&!t.negative).map(t=>t.value),loaders=terms.filter(t=>t.key==='loader'&&!t.negative).map(t=>t.value);","const versions=[...terms.filter(t=>t.key==='version'&&!t.negative).map(t=>t.value),...(state.version?[state.version]:[])],loaders=[...terms.filter(t=>t.key==='loader'&&!t.negative).map(t=>t.value),...(state.loader?[state.loader]:[])];",'coupled release filters')
 s=replace_once(s,"function closeDialog(id){$('#'+id).close();}","function closeDialog(id){if(id==='detailDialog'){detailId=null;updateURL();}$('#'+id).close();}",'synchronous detail URL cleanup')
 p.write_text(s,encoding='utf-8')
 # A browser can restore an open <dialog> from a deep link; test notes directly if it is already open.
 test=ROOT/'qa'/'browser_test.py';t=test.read_text(encoding='utf-8')
 old="page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');page.locator('[data-project=\"'+fid+'\"] [data-action=\"detail\"]').click();check('notes survive reload'"
 new="page.reload(wait_until='domcontentloaded');page.wait_for_function('window.ATLAS_TEST');page.locator('[data-project=\"'+fid+'\"] [data-action=\"detail\"]').click();check('notes survive reload'"
 # Keep the immediate close/reload regression test intact; the implementation, not the test, is repaired.
 assert old in t or new in t
 test.write_text(t,encoding='utf-8')
if __name__=='__main__':run()
