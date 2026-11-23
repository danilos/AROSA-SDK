# AROSA SDK 0.18.6.0.0.0 — Experimental developer preview

Released documentation: 2026-11-23.

## Platform policy

**x86_64 is now the active development and testing priority. i386 support is experimental, best-effort and not guaranteed.**

## Historical i386 validation

Passed: complete historical i386 application compilation and linking, SDK binary compilation, and independent public AFileManager build against precompiled AROSA units. The copied application executable matches the independent build.

Not passed/not performed: AROS i386 runtime execution, historical x86_64 SDK compilation or runtime. An AGet transfer stalled while preparing a runtime test; no AFileManager startup failure was observed.

## Binary distribution

A cleaned i386 SDK candidate ZIP was generated separately with 234 PPU, 234 O and four A static libraries; no source files or historical test executable. Checksums and archive CRC verified. **This candidate is not a GitHub release binary** and remains withheld from public distribution until component-level copyright/license notices and source-availability obligations are resolved. GitHub documentation is public and issue reports are open.

## Resources

Public application source: https://github.com/danilos/AFileManager

Support policy: https://github.com/danilos/AROSA-SDK/blob/main/docs/release-policy.md

Report issues: https://github.com/danilos/AROSA-SDK/issues

Original project copyright (c) 2026 DaniloS. Third-party rights are reserved.
