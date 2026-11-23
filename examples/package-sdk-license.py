#!/usr/bin/env python3
"""Safely add the published DaniloS developer license to the historical x86_64 SDK ZIP.

Never edits its input ZIP. Preserves each existing ZIP member's uncompressed bytes
and ZIP metadata; replaces only SHA256SUMS and adds SDK-LICENSE.md.
Copyright (c) 2026 DaniloS.
"""
import argparse
import hashlib
import os
import sys
import zipfile
from collections import Counter
from pathlib import Path

ORIGINAL_SHA256 = "4779997aff0b6c61ac8047c56918106ba81d57199f11fd3c36671a0cf3bb417c"
EXPECTED_OLD_MEMBERS = 481
EXPECTED_COMPILED = 473
LICENSE_MEMBER = "SDK-LICENSE.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str):
    raise ValueError(message)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--license", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    original = args.source.resolve()
    destination = args.output.resolve()
    if original == destination:
        fail("source and output must differ")
    if destination.exists():
        fail(f"refusing to overwrite existing output: {destination}")
    if not destination.parent.is_dir():
        fail(f"output directory must exist: {destination.parent}")
    license_bytes = args.license.read_bytes()
    if not license_bytes or b"DaniloS" not in license_bytes or b"Developer License" not in license_bytes:
        fail("invalid or missing DaniloS SDK developer license")
    source_bytes = original.read_bytes()
    if sha(source_bytes) != ORIGINAL_SHA256:
        fail("source ZIP digest differs from the verified, publicly uploaded 0.18.6 x86_64 baseline")

    # Read and verify before writing anything.
    with zipfile.ZipFile(original, "r") as src:
        old_infos = src.infolist()
        names = [info.filename for info in old_infos]
        if len(names) != EXPECTED_OLD_MEMBERS or len(set(names)) != len(names):
            fail("unexpected source inventory or duplicate member")
        if "SHA256SUMS" not in names or LICENSE_MEMBER in names:
            fail("missing existing manifest or license already present")
        if src.testzip() is not None:
            fail("source ZIP CRC failure")
        original_files = {info.filename: src.read(info) for info in old_infos}
        old_manifest = {}
        for line in original_files["SHA256SUMS"].decode("utf-8").splitlines():
            fields = line.split(maxsplit=1)
            if len(fields) != 2:
                fail(f"malformed original manifest: {line!r}")
            digest, file_path = fields
            file_path = file_path.lstrip("*")
            if file_path in old_manifest:
                fail(f"duplicate manifest path: {file_path}")
            old_manifest[file_path] = digest.lower()
        expected = set(names) - {"SHA256SUMS"}
        if set(old_manifest) != expected or any(
            sha(original_files[path]) != old_manifest[path] for path in expected
        ):
            fail("original SHA256SUMS inventory or digest verification failed")
        compiled = sum(name.endswith((".ppu", ".o", ".a")) for name in names)
        if compiled != EXPECTED_COMPILED:
            fail(f"unexpected compiled artifact count: {compiled}")
        notices = sum(name.startswith("THIRD-PARTY-NOTICES/") for name in names)
        if notices != 6:
            fail(f"unexpected notice count: {notices}")

        # Keep all pre-existing manifest lines unchanged. Append the one new entry.
        previous_lines = original_files["SHA256SUMS"].decode("utf-8").rstrip("\n")
        revised_manifest = (
            previous_lines + "\n" + sha(license_bytes) + "  " + LICENSE_MEMBER + "\n"
        ).encode("utf-8")

        # Create a fresh versioned output only; do not risk modifying the source ZIP.
        try:
            with destination.open("xb") as target_file:
                with zipfile.ZipFile(target_file, "w", allowZip64=True) as output:
                    output.comment = src.comment
                    for info in old_infos:
                        data = revised_manifest if info.filename == "SHA256SUMS" else original_files[info.filename]
                        output.writestr(info, data)
                    output.writestr(LICENSE_MEMBER, license_bytes, compress_type=zipfile.ZIP_DEFLATED)
            # Independently check that the newly produced ZIP changes only the manifest + license.
            with zipfile.ZipFile(destination, "r") as new:
                current_names = new.namelist()
                if len(current_names) != EXPECTED_OLD_MEMBERS + 1:
                    fail("new member count incorrect")
                if set(current_names) != set(names) | {LICENSE_MEMBER}:
                    fail("new member inventory mismatch")
                if new.testzip() is not None:
                    fail("new ZIP CRC failure")
                for name in names:
                    if name != "SHA256SUMS" and new.read(name) != original_files[name]:
                        fail(f"pre-existing file unexpectedly modified: {name}")
                if new.read(LICENSE_MEMBER) != license_bytes:
                    fail("developer license differs from source")
                checks = {}
                for line in new.read("SHA256SUMS").decode("utf-8").splitlines():
                    digest, name = line.split(maxsplit=1)
                    checks[name.lstrip("*")] = digest.lower()
                if len(checks) != len(current_names) - 1 or set(checks) != set(current_names) - {"SHA256SUMS"}:
                    fail("new manifest inventory mismatch")
                for name, digest in checks.items():
                    if sha(new.read(name)) != digest:
                        fail(f"new manifest digest mismatch: {name}")
        except Exception:
            # Only cleanup the file this program itself created, never the source.
            if destination.exists():
                destination.unlink()
            raise

    print(f"PASS: original SDK unchanged: {original}")
    print(f"PASS: licensed SDK archive: {destination}")
    print(f"Members: {EXPECTED_OLD_MEMBERS + 1}; hashes: {len(checks)}; compiled artifacts: {compiled}; third-party notices: {notices}")
    print(f"SHA-256: {sha(destination.read_bytes())}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, zipfile.BadZipFile, UnicodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
