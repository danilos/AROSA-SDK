# AROSA Developer SDK

**AROSA — Enterprise-class architecture at Amiga scale.**

Public developer entry point for applications using AROSA capability, service, provider and adapter interfaces on AROS.

## Experimental developer preview — 23 November 2026

**x86_64 AROS is the primary development and testing target. i386 (32-bit) is experimental, best-effort and NOT guaranteed.**

The initial historical baseline is AROSA **0.18.6.0.0.0**, revision `384eeaf`. **Both i386 and x86_64 SDK compilation/link tests have now passed.** On each architecture, the public [AFileManager](https://github.com/danilos/AFileManager) application source independently compiled and linked against compiled AROSA SDK dependencies without using private AROSA Pascal source. The x86_64 output was identified by `file` as **ELF 64-bit, x86-64, AROS**, and its historical executable was about 17 MB.

**Runtime status:** The owner reports the i386 SDK-built AFileManager did not open in the AROS test environment; the cause has not been established. **x86_64 runtime launch has not yet been tested.** Successful linking is not a runtime guarantee. Issue reports are welcome at [GitHub Issues](https://github.com/danilos/AROSA-SDK/issues).

## Contents and availability

- [Release and platform support policy](docs/release-policy.md)
- [x86_64 build validation record](docs/0.18.6.0.0.0-x86_64-status.md)
- [i386 historical validation record](docs/0.18.6.0.0.0-status.md)
- [SDK distribution contract](docs/sdk-distribution-contract.md)
- [Dependency and redistribution review](docs/dependency-provenance.md)

A clean **i386 candidate** archive has been assembled separately. A **private x86_64 SDK** has also been produced (476 files, as reported by the build tool), but no redistributable x86_64 binary artifact has yet been reviewed. **Neither binary SDK is currently published as a GitHub release.** Component-level third-party notices and any applicable covered-source obligations require reconciliation before public binary upload.

The [public AFileManager source](https://github.com/danilos/AFileManager) retains its MPL-2.0 license. This repository does not grant a blanket license over private AROSA implementation source. The November historical baseline is not claimed to correspond exactly to an October 2026 AFileManager preview executable.

Original AROSA components copyright (c) 2026 **DaniloS**; all third-party copyrights and licenses remain with their respective owners.
