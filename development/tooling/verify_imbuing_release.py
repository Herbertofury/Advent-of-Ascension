"""Verify two official AoA archives and observe the shipped Imbuing input boundary.

This only reads archives and invokes javap, never loads or runs mod classes.
No network access, JAR extraction, or redistribution is needed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile


MODERN_ID = "vIo8vp51"
MODERN_SHA512 = (
    "f95109a9072946e36451daa4c25a588feeda02cf1b24ab810d2176a0635f5cfb5c"
    "9408e0345c725a96c4fe70f97251ac55aed25687ed3f4daf12082317ca0f57"
)
FORGE_ID = "ADsBtG85"
FORGE_SHA512 = (
    "bdee7d12aab1903e1e74f377d4f0ae7ac948d791f46ec0368d191d86a3d5a03cfbd"
    "2e6d1295f1fe690f303b1fa709da89db980543e4d450fc0fdbbf6d9e694e6"
)
INPUT = "net.tslat.aoa3.content.recipe.ImbuingRecipe$ImbuingRecipeInput"
MENU = "net.tslat.aoa3.common.menu.ImbuingChamberMenu"
ENTRY = INPUT.replace(".", "/") + ".class"


def archive_receipt(path, size, sha512, version_id):
    if not path.is_file() or path.stat().st_size != size:
        raise ValueError(f"{version_id}: file size is not the pinned release")
    with path.open("rb") as data:
        actual = hashlib.file_digest(data, "sha512").hexdigest()
        if actual != sha512:
            raise ValueError(f"{version_id}: SHA-512 is not the pinned release")
        data.seek(0)
        sha256 = hashlib.file_digest(data, "sha256").hexdigest()
    with zipfile.ZipFile(path) as jar:
        inputs = [name for name in jar.namelist() if name.endswith("ImbuingRecipeInput.class")]
    return {
        "modrinthVersionId": version_id,
        "bytes": size,
        "sha512": sha512,
        "sha256": sha256,
        "inputClassCount": len(inputs),
        "exactInputClassCount": inputs.count(ENTRY),
    }


def disassemble(java, path, name):
    return subprocess.check_output(
        [java, "--module", "jdk.jdeps/com.sun.tools.javap.Main", "-classpath",
         str(path.resolve()), "-c", "-p", name],
        text=True, encoding="utf-8", timeout=20,
    )


def observe(java, neo, forge):
    modern = archive_receipt(neo, 139631628, MODERN_SHA512, MODERN_ID)
    older = archive_receipt(forge, 139674143, FORGE_SHA512, FORGE_ID)
    if modern["inputClassCount"] != 1 or modern["exactInputClassCount"] != 1:
        raise ValueError("Unexpected Imbuing recipe input entries in the current release")
    if older["inputClassCount"] != 0:
        raise ValueError("Unexpected Imbuing recipe input entry in the Forge comparison release")

    code = disassemble(java, neo, INPUT)
    matches = re.search(
        r"(?ms)^  public boolean equals\(java\.lang\.Object\);\n(.*?)(?=^  \S|\Z)", code
    )
    if not matches:
        raise ValueError("Could not distinguish the exact equals method")
    body = matches.group(1)
    # Match the three adjacent instructions, not just any reference to Objects.equals.
    recursive = re.search(
        r"(?m)^\s*\d+: aload_0[ \t]*\n\s*\d+: aload_2[ \t]*\n"
        r"\s*\d+: invokestatic\s+#\d+\s+// Method java/util/Objects\.equals:",
        body,
    )
    if not recursive or "checkcast" not in body or "ImbuingRecipe$ImbuingRecipeInput" not in body:
        raise ValueError("Did not verify delegation to Objects.equals on the same wrapper arguments")
    menu_code = disassemble(java, neo, MENU)
    constructs = re.search(
        r"(?m)^\s*\d+: new\s+#\d+\s+// class "
        r"net/tslat/aoa3/content/recipe/ImbuingRecipe\$ImbuingRecipeInput[ \t]*$",
        menu_code,
    )
    if not constructs:
        raise ValueError("Did not verify the shipped menu creates this input object")
    return {
        "scope": "static checks of two pinned original releases; no mod execution",
        "neoForge1211": modern,
        "forge1201Reference": older,
        "modernEqualsDelegatesOnWrapperArguments": True,
        "modernMenuConstructsInputWrapper": True,
        "gameplayEqualsCallEstablished": False,
        "ownerPlaytestVerified": False,
        "runtimeOrAdoptionAccepted": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("neoforge_archive", type=Path)
    parser.add_argument("forge_archive", type=Path)
    parser.add_argument("--java", default="java")
    args = parser.parse_args()
    try:
        print(json.dumps(observe(args.java, args.neoforge_archive, args.forge_archive), indent=2))
    except (ValueError, OSError, subprocess.SubprocessError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Imbuing release verification failed: {error}\n")


if __name__ == "__main__":
    main()
