# Artifact verification identity regression (2026-11-13)

The validator previously hashed a candidate, closed it, then reopened its path for ZIP-member verification. A generated test atomically replaces the file after hashing with a same-length ZIP containing identical members but different archive metadata. The baseline incorrectly returns `passed: true` although the path now has a different whole-file hash.

The validator now hashes and reads members from one open file and checks the descriptor and path identity at the end. Replacement, removal and in-place rewrite during the check are rejected. This bounds verification to the observed object; it does not lock the path after return or establish gameplay acceptance.

Validation: `python -m unittest discover -s development/tooling -p 'test_*.py' -v` passed 15 tests, including the three generated race cases. Existing length/hash/member/duplicate and wiki/freshness controls are retained. No private artifact, original AoA code or original assets are published.

Freshness: official default branch `1.21` remains `7919b5fe48599e6105c5740937ce36c36ef21d16`; the existing GitHub drift guard passes, including the complete 46-file changelog tree, releases and tags. All 46 changelogs were retained for this review. Official production remains [3.7.16.1, file 7424722](https://www.curseforge.com/minecraft/mc-mods/advent-of-ascension-nevermine/files/7424722), matching the lock. The official Modrinth version API also lists 3.7.16.1 first. Tslat and contributors retain attribution. No modern-source adoption, private native promotion or completed historical/latest union is claimed.
