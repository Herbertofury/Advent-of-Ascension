"""Generated fault controls for the wiki intake and existing-provider freshness gate."""
import copy
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

import upstream_guard
import wiki_checklist
import verify_local_artifact


class WikiTests(unittest.TestCase):
    def test_fenced_and_commented_examples_are_not_work(self):
        rows = wiki_checklist.tasks('# Work\n- [x] Real\n```md\n- [ ] Example\n```\n<!--\n- [ ] Hidden\n-->\n1. [ ] Open\n', 'Home.md')
        self.assertEqual([r['text'] for r in rows], ['Real', 'Open'])
        self.assertTrue(rows[0]['sourceReportedChecked'])
        self.assertTrue(all(r['acceptance'] == 'source-checklist-only' for r in rows))

    def test_html_examples_do_not_hide_later_real_tasks(self):
        rows = wiki_checklist.tasks('```html\n<!-- example\n- [ ] Example\n```\n- [ ] Real\n', 'Home.md')
        self.assertEqual([row['text'] for row in rows], ['Real'])

    def test_location_and_heading_disambiguate_identity(self):
        rows = wiki_checklist.tasks('# First\n- [ ] Task\n# Second\n- [ ] Task\n', 'Home.md')
        self.assertNotEqual(rows[0]['id'], rows[1]['id'])
        self.assertEqual(rows[0]['id'], wiki_checklist.tasks('\n# First\n\n- [ ] Task\n', 'Home.md')[0]['id'])

    def test_ambiguous_duplicate_rejected(self):
        with self.assertRaises(ValueError):
            wiki_checklist.tasks('# Same\n- [ ] Task\n- [x] Task\n', 'Home.md')

    def test_complete_git_snapshot_and_changed_tasks(self):
        with tempfile.TemporaryDirectory(prefix='enderloom-wiki-guard-') as folder:
            directory = Path(folder).resolve()
            self.assertTrue(directory.is_relative_to(Path(tempfile.gettempdir()).resolve()))
            subprocess.run(['git', 'init', '-q', folder], check=True)
            def run(*args):
                subprocess.run(['git', '-C', folder, *args], check=True, capture_output=True)
            run('config', 'user.name', 'Generated fixture')
            run('config', 'user.email', 'fixture@example.invalid')
            (directory / 'Home.md').write_text('# Work\n- [x] Documented\n- [ ] Pending\n', encoding='utf-8')
            (directory / 'Empty.md').write_text('# No tasks\n', encoding='utf-8')
            run('add', '.'); run('commit', '-qm', 'Generated complete wiki fixture')
            first = wiki_checklist.snapshot(folder)
            self.assertEqual((first['pageCount'], first['taskCount']), (2, 2))
            # Uncommitted edits cannot masquerade as an immutable Git snapshot.
            (directory / 'Home.md').write_text('# Work\n- [ ] Pending\n', encoding='utf-8')
            self.assertEqual(first, wiki_checklist.snapshot(folder))
            run('add', '.'); run('commit', '-qm', 'Generated task removal')
            changes = wiki_checklist.compare(first, wiki_checklist.snapshot(folder))
            self.assertEqual(len(changes['removed']), 1)
            self.assertTrue(changes['pageChanges'])


class FreshnessTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime.datetime(2026, 10, 16, tzinfo=datetime.timezone.utc)
        self.lock = dict(github=dict(head='a' * 40, defaultBranch='1.21'),
                         officialRelease=dict(fileId='1', version='fixture'))
        self.fresh = dict(passed=True, observedAt=self.now.isoformat(), semanticReconciliationComplete=False,
                          github=dict(commit='a' * 40, defaultBranch='1.21', completeReleaseAndTagPages=True),
                          curseforge=dict(fileId='1', version='fixture'))

    def test_exact_observation_is_not_semantic_completion(self):
        upstream_guard.validate_native_freshness(self.lock, self.fresh, self.now)

    def test_drift_and_false_completion_rejected(self):
        faults = [('old', lambda x: x.update(observedAt=(self.now - datetime.timedelta(days=2)).isoformat())),
                  ('future', lambda x: x.update(observedAt=(self.now + datetime.timedelta(minutes=2)).isoformat())),
                  ('failed', lambda x: x.update(passed=False)),
                  ('head', lambda x: x['github'].update(commit='b' * 40)),
                  ('branch', lambda x: x['github'].update(defaultBranch='next')),
                  ('new_release', lambda x: x['curseforge'].update(fileId='2')),
                  ('incomplete', lambda x: x['github'].update(completeReleaseAndTagPages=False)),
                  ('fake_merge', lambda x: x.update(semanticReconciliationComplete=True))]
        for name, change in faults:
            with self.subTest(fault=name):
                broken = copy.deepcopy(self.fresh); change(broken)
                with self.assertRaises(ValueError):
                    upstream_guard.validate_native_freshness(self.lock, broken, self.now)


class ArtifactTests(unittest.TestCase):
    def test_complete_local_identity_and_destructive_inventory_faults(self):
        with tempfile.TemporaryDirectory(prefix='enderloom-local-artifact-guard-') as folder:
            directory = Path(folder).resolve()
            self.assertTrue(directory.is_relative_to(Path(tempfile.gettempdir()).resolve()))
            jar = directory / 'generated-fixture.jar'
            payload = {'META-INF/': b'', 'fixture/data.json': b'{"fixture":true}\n'}
            with zipfile.ZipFile(jar, 'x') as archive:
                for name, raw in payload.items():
                    archive.writestr(name, raw)
            raw = jar.read_bytes()
            manifest = dict(artifact=dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()),
                            memberCount=len(payload), members=[dict(path=name, bytes=len(body), sha256=hashlib.sha256(body).hexdigest()) for name, body in payload.items()])
            self.assertTrue(verify_local_artifact.verify(jar, manifest)['passed'])
            faults = [lambda x: x['artifact'].update(sha256='0' * 64),
                      lambda x: x['members'].pop(),
                      lambda x: x['members'][1].update(sha256='0' * 64),
                      lambda x: x['members'][1].update(bytes=0),
                      lambda x: x['members'].__setitem__(1, x['members'][0].copy())]
            for index, mutate in enumerate(faults):
                with self.subTest(generated_fault=index):
                    broken = copy.deepcopy(manifest); mutate(broken)
                    with self.assertRaises(ValueError):
                        verify_local_artifact.verify(jar, broken)


if __name__ == '__main__':
    unittest.main()
