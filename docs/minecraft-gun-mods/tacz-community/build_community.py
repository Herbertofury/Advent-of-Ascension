#!/usr/bin/env python3
"""Single entrypoint: reuse frozen qualification, then apply the additive community overlay."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))

def main():
 if not (ROOT/'qualified-records.json').exists():
  import hydrate_community
  hydrate_community.main()
 if (ROOT/'apply_community.py').exists():
  import apply_community
  apply_community.main()
 else:print('Exact creator records and source previews checkpointed for visual qualification.',flush=True)
if __name__=='__main__':main()
