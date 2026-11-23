#!/usr/bin/env python3
"""Read-only SHA-256/ZIP integrity checker for an AROSA SDK archive.

Copyright (c) 2026 DaniloS.
Usage: python3 examples/inspect_sdk.py /path/to/AROSA-SDK-*.zip
Uses only the Python standard library. Does not write/extract files.
"""
import hashlib
import sys
import zipfile
from collections import Counter
from pathlib import Path


def verify(filename: Path) -> bool:
    with zipfile.ZipFile(filename) as sdk:
        names = sdk.namelist()
        duplicates = [n for n, v in Counter(names).items() if v != 1]
        if duplicates:
            print("FAIL: duplicate ZIP names:", duplicates)
            return False
        bad = sdk.testzip()
        if bad is not None:
            print("FAIL: ZIP CRC failed:", bad)
            return False
        if "SHA256SUMS" not in names:
            print("FAIL: missing SHA256SUMS")
            return False

        checksums = {}
        for line in sdk.read("SHA256SUMS").decode("utf-8").splitlines():
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                print("FAIL: malformed manifest line:", line)
                return False
            digest, path = parts
            path = path.removeprefix("*")
            if path in checksums:
                print("FAIL: duplicate manifest entry:", path)
                return False
            checksums[path] = digest.lower()

        expected = set(names) - {"SHA256SUMS"}
        if set(checksums) != expected:
            print("FAIL: manifest inventory mismatch")
            print("Missing:", sorted(expected - set(checksums)))
            print("Unexpected:", sorted(set(checksums) - expected))
            return False

        mismatch = [
            name for name in sorted(expected)
            if hashlib.sha256(sdk.read(name)).hexdigest() != checksums[name]
        ]
        if mismatch:
            print("FAIL: SHA-256 mismatches:", mismatch)
            return False

        ppus = [n for n in names if n.endswith(".ppu")]
        objs = [n for n in names if n.endswith(".o")]
        libs = [n for n in names if n.endswith(".a")]
        notices = [n for n in names if n.startswith("THIRD-PARTY-NOTICES/")]
        print("PASS: all ZIP CRC and SHA-256 manifest checks")
        print(f"Members: {len(names)}, hashes: {len(checksums)}")
        print(f"Compiled units: {len(ppus)}; objects: {len(objs)}; archives: {len(libs)}")
        print("Libraries:", ", ".join(sorted(libs)) or "(none)")
        print("Third-party notice files:", len(notices))
        return True


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} <sdk.zip>", file=sys.stderr)
        return 2
    try:
        return 0 if verify(Path(sys.argv[1])) else 1
    except (OSError, ValueError, UnicodeError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
