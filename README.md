# AROSA Developer SDK

**AROSA — Enterprise-class architecture at Amiga scale.**

Public development entry point for applications targeting the AROSA capability-based runtime on AROS.

Copyright (c) 2026 **DaniloS**. This repository is maintained separately from the private AROSA platform implementation.

## Status — 23 November 2026

**Repository initialized; public binary SDK not yet released.**

The initial engineering baseline is **AROSA 0.18.6.0.0.0**, from the immutable private AROSA source revision dated 4 November 2026. The completed local i386 validation establishes:

- Historical AFileManager successfully compiled and linked against the matching AROSA build and native dependencies.
- A private **475-file binary SDK** was packaged with 234 Pascal `.ppu` units, 234 `.o` objects, four static libraries and ancillary files.
- A separate build of the **public AFileManager source** successfully compiled and linked using precompiled SDK dependencies instead of private AROSA Pascal source paths.
- The resulting application executable matched the executable copied into the isolated runtime-test drawer.

**Not yet verified:** successful execution on a booted AROS system; x86_64 SDK; SDK redistribution permissions, third-party notices and MPL-covered-source boundary. None of those tests should be inferred from the successful compile/link steps.

## Architecture and purpose

An AROSA application declares, requests and offers capabilities. Application and provider implementations are composed through versioned service, provider, adapter and presentation contracts. The planned SDK provides application-facing Pascal contracts, target-compatible compiled units/libraries, build tooling and examples, without indiscriminately distributing internal service implementations.

The SDK must match the target architecture, FPC/AROS compiler ABI and AROSA runtime version.

## Public companion project

[AFileManager](https://github.com/danilos/AFileManager) publishes a historical MPL-2.0 application source snapshot and original artwork from the same AROSA 0.18.6.0.0.0 baseline. Its repository currently requires compatible SDK dependencies to build.

## Distribution boundaries

- **This repository does not currently contain an SDK binary download.** Do not treat an older private `*-PRIVATE-REVIEW.zip` as a published release.
- Private AROSA implementation source, build snapshots, working-tree backups and internal architecture material are not part of the public SDK.
- Binary artifacts are not automatically source-code substitutes for any MPL-2.0-covered code whose source must be made available.
- No blanket license grant over private AROSA implementations is intended. An explicit license and notices will accompany each approved SDK component before binary publication.
- The historic November source is **not claimed** to match the exact October 2026 AFileManager preview binary.

See [the 0.18.6.0.0.0 validation record](docs/0.18.6.0.0.0-status.md) and [the SDK distribution contract](docs/sdk-distribution-contract.md).

## Next release gates

Complete AROS runtime execution testing, validate the exact binary SDK inventory and redistribution rights, publish approved developer-facing artifacts with notices, then verify a clean public-consumer build. x86_64 follows as a separately verified architecture.
