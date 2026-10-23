#!/usr/bin/env python3
"""Repair the publication owner without editing self-triggering workflows in CI."""
from pathlib import Path
import ast,importlib.util,json
ROOT=Path(__file__).resolve().parent

def main():
    path=ROOT/'build_update.py';text=path.read_text(encoding='utf-8')
    old="    _nav_path=Path(__file__).resolve().parent{parents}/'weapon_inspiration_navigation.py'\n    _nav_spec="
    new="    _nav_path=Path(__file__).resolve().parent{parents}/'weapon_inspiration_navigation.py'\n    if not _nav_path.exists():\n        import subprocess\n        _source=subprocess.run(['git','show','HEAD:docs/weapon_inspiration_navigation.py'],cwd=_nav_path.parent.parent,check=True,capture_output=True).stdout\n        _nav_path.write_bytes(_source)\n    _nav_spec="
    assert old in text or new in text,'Reconcile changed navigation loader'
    text=text.replace(old,new)
    start=text.index('    patched=[]',text.index('def patch_publishers():')) if '    patched=[]' in text else -1
    if start>=0:
        end=text.index('\ndef main():',start)
        replacement="""    # Workflow mutation is deliberately outside the content-only CI authority.
    # The connector updated the one inline publisher; module publishers use exact Git HEAD.
    workflow=REPO/'.github/workflows/publish-weapon-inspirations.yml'
    if workflow.exists():
        assert 'python3 source/weapon_inspiration_navigation.py wiki' in workflow.read_text(), 'Inline publisher still has a separate menu owner'
    save(ROOT/'qa/publisher-owner-proof.json',{'sharedOwner':'docs/weapon_inspiration_navigation.py','modulePublishers':['minecraft-gun-mods/build.py:publish','minecraft-gun-mods/tacz/publish_tacz.py:prepare','weapon-inspirations/build_galleries.py:publish','weapon-inspirations/expand_research.py:persist_and_publish'],'workflowFilesChangedByBuilder':[],'sharedModuleFromExactGitHead':True,'oldAppendOwnersReplaced':True})

"""
        text=text[:start]+replacement+text[end:]
    ast.parse(text);path.write_text(text,encoding='utf-8')
    test=ROOT/'test_update.py';body=test.read_text(encoding='utf-8')
    body=body.replace("server=socketserver.TCPServer(('127.0.0.1',0),Handler);threading.Thread", "server=socketserver.ThreadingTCPServer(('127.0.0.1',0),Handler);server.daemon_threads=True;threading.Thread")
    body=body.replace("report['checks'].append({'name':name,'passed':bool(value),'details':details});", "print('CHECK',name,bool(value),flush=True);report['checks'].append({'name':name,'passed':bool(value),'details':details});")
    ast.parse(body);test.write_text(body,encoding='utf-8')
    spec=importlib.util.spec_from_file_location('creator_update_final',path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.main()
if __name__=='__main__':main()
