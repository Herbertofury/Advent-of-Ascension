# Imbuing recipe input: official release boundary

This extends the [source finding in issue #8](https://github.com/Herbertofury/Advent-of-Ascension/issues/8) to actual published files. It does not change AoA, close the issue, or claim a player crash.

| Official artifact | Static observation |
| --- | --- |
| [3.7.16.1 for 1.21.1 / NeoForge](https://modrinth.com/mod/adventofascension/version/3.7.16.1), also [CurseForge file 7424722](https://www.curseforge.com/minecraft/mc-mods/advent-of-ascension-nevermine/files/7424722) | The shipped input wrapper compares the same wrapper arguments through Java's object-equality helper, matching the recursive source defect. The compiled Imbuing Chamber menu does create this exact wrapper. |
| [3.7.1 for 1.20.1 / Forge](https://modrinth.com/mod/adventofascension/version/ADsBtG85) | No class named `ImbuingRecipeInput` is present in this official comparison file. This is not inspection of the owner's modified 1.20.1 artifact. |

Both Modrinth files match their published size and SHA-512. The repository's read-only upstream guard matched the locked official source branch, complete changelog-tree manifest, GitHub releases and tags. The provider pages listed 3.7.16.1 as the current official release; this does not substitute for Enderloom's native promotion receipt.

To verify the two exact archives you obtained from the original providers, with Python 3.11+ and Java 21 with the `jdk.jdeps` module:

```sh
python development/tooling/verify_imbuing_release.py \
  /local/AoA3-1.21.1-3.7.16.1.jar /local/AoA3-1.20.1-3.7.1-all.jar
```

The tool disassembles only the named unmodified classes; it never runs mod code, writes to the JARs, needs a game account, or starts a game. Two positive reads returned identical output; reversed inputs and a byte-changed copy were refused. The [JSON receipt](imbuing-release-bytecode-2026-11-23.json) records hashes and limits, not original source, classfiles, or JARs. Advent of Ascension is created by Tslat and contributors.

**Next acceptance gate:** establish the intended backing-inventory equality contract and qualify a separately reviewed correction in the matching NeoForge client and dedicated server before modern adoption. Actual gameplay invocation of equality and acceptance of the owner-local playtest are not established here.
