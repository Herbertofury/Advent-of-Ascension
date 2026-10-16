"""Read-only GitHub drift gate; official release admission uses Enderloom's provider resolver."""
import argparse
import concurrent.futures
import datetime
import json
import os
from pathlib import Path
import urllib.parse
import urllib.request

REPOSITORY = 'Tslat/Advent-Of-Ascension'
API = 'https://api.github.com/repos/' + REPOSITORY


def get(endpoint):
    headers = {'User-Agent': 'Enderloom-AoA-upstream-reconciliation', 'Accept': 'application/vnd.github+json'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    request = urllib.request.Request(API + endpoint, headers=headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def pages(endpoint):
    result = []
    for page in range(1, 101):
        rows = get(endpoint + '?per_page=100&page=' + str(page))
        if not isinstance(rows, list):
            raise ValueError('Unexpected paginated GitHub response')
        result.extend(rows)
        if len(rows) < 100:
            return result
    raise ValueError('Pagination budget reached; incomplete upstream observation is rejected')


def observe():
    metadata = get('')
    if metadata['full_name'] != REPOSITORY:
        raise ValueError('Wrong official repository')
    branch = metadata['default_branch']
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        head = pool.submit(get, '/commits/' + urllib.parse.quote(branch, safe=''))
        release_rows = pool.submit(pages, '/releases')
        tag_rows = pool.submit(pages, '/tags')
        commit, releases, tags = head.result(), release_rows.result(), tag_rows.result()
    tree = get('/git/trees/' + commit['sha'])
    if tree.get('truncated'):
        raise ValueError('Incomplete upstream root tree')
    selected = [row for row in tree['tree'] if row['path'] == 'changelogs' and row['type'] == 'tree']
    if len(selected) != 1:
        raise ValueError('Missing or ambiguous official changelog directory')
    changelogs = get('/git/trees/' + selected[0]['sha'] + '?recursive=1')
    if changelogs.get('truncated'):
        raise ValueError('Incomplete official changelog tree')
    return dict(repository=REPOSITORY, defaultBranch=branch, head=commit['sha'],
                changelogTree=changelogs['sha'],
                changelogs=sorted([dict(path=row['path'], gitBlobSha1=row['sha'], bytes=row['size'])
                                   for row in changelogs['tree'] if row['type'] == 'blob'], key=lambda row: row['path']),
                releases=sorted([dict(id=row['id'], tag=row['tag_name'], draft=row['draft'],
                                     prerelease=row['prerelease'], published=row['published_at'])
                                 for row in releases], key=lambda row: row['id']),
                tags=sorted([dict(name=row['name'], commit=row['commit']['sha']) for row in tags], key=lambda row: row['name']))


def validate_native_freshness(lock, fresh, now=None):
    """Bind the existing complete provider observation; never infer a merge from freshness."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    at = datetime.datetime.fromisoformat(fresh['observedAt'].replace('Z', '+00:00'))
    if not fresh.get('passed') or not 0 <= (now - at).total_seconds() <= 86400:
        raise ValueError('A successful live upstream/provider observation within 24 hours is required')
    if fresh.get('semanticReconciliationComplete') is not False:
        raise ValueError('Freshness must not masquerade as completed semantic reconciliation')
    if fresh['github']['commit'] != lock['github']['head'] or fresh['github']['defaultBranch'] != lock['github']['defaultBranch']:
        raise ValueError('Official source changed; reconcile the canonical project before native promotion')
    if (fresh['curseforge']['fileId'], fresh['curseforge']['version']) != (lock['officialRelease']['fileId'], lock['officialRelease']['version']):
        raise ValueError('Official production release changed; reconcile before native promotion')
    if not fresh['github'].get('completeReleaseAndTagPages'):
        raise ValueError('Incomplete official release/tag observation')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lock', required=True)
    parser.add_argument('--native-freshness')
    parser.add_argument('--output')
    args = parser.parse_args()
    lock = json.loads(Path(args.lock).read_text(encoding='utf-8'))
    if args.native_freshness:
        fresh = json.loads(Path(args.native_freshness).read_text(encoding='utf-8'))
        validate_native_freshness(lock, fresh)
        result = dict(passed=True, githubAndProviderFreshnessVerified=True,
                      semanticReconciliationComplete=False, completeAoAPort=False)
    else:
        current = observe()
        changed = [key for key in current if current[key] != lock['github'].get(key)]
        result = dict(passed=not changed, observedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      changedFields=changed, github=current, officialProviderReleaseRechecked=False,
                      semanticReconciliationComplete=False, completeAoAPort=False)
    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in result if key != 'github'}))
    if not result['passed']:
        raise SystemExit('Upstream drift detected; do not silently overwrite the accepted source or drop historical content')


if __name__ == '__main__':
    main()
