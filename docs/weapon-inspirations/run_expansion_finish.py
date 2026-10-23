#!/usr/bin/env python3
"""Run the final research wave with atomic, per-entry media replacement."""
import copy
from pathlib import Path
import research_finish as finish


def repair_one(entry, previous):
    result = copy.deepcopy(previous)
    video = result.get('video')
    if entry['id'] in finish.VIDEO_FIX:
        video = finish.video(entry, previous)
    if not video:
        return None, 'Exact video not resolved; existing image bytes preserved'
    old_path = finish.ROOT / previous['image']['local']
    old_bytes = old_path.read_bytes()
    try:
        image = finish.exact_image(entry)
        if not image and video.get('chapter_thumbnail'):
            image = finish.save_url(entry, video['chapter_thumbnail'], video['url'],
                                    'Exact named weapon chapter frame', {'chapter': video['chapter']})
        if not image:
            old_path.write_bytes(old_bytes)
            return None, 'Exact weapon image not resolved; existing image bytes preserved'
        result.update(image=image, video=video, complete=True, status='accepted')
        result.setdefault('evidence', []).append({
            'url': image['source'], 'title': entry['name'], 'kind': image['kind']})
        return result, None
    except Exception:
        old_path.write_bytes(old_bytes)
        raise


finish.repair_one = repair_one
if __name__ == '__main__':
    finish.main()
