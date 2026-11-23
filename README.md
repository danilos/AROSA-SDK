# AROSA Developer SDK

**AROSA — Enterprise-class architecture at Amiga scale.**

Public developer entry point for applications using AROSA service, provider, adapter and capability interfaces on AROS.

## Experimental developer preview — 23 November 2026

**Primary development and testing have moved to x86_64 AROS. The i386 (32-bit) target is experimental, best-effort and NOT guaranteed.** This is a support-policy change, not a claim that x86_64 testing has passed.

The first engineering baseline is AROSA **0.18.6.0.0.0**, historical AROSA revision **384eeaf**. The i386 SDK compilation/link tests **passed**: public [AFileManager](https://github.com/danilos/AFileManager) source compiled and linked independently using compiled AROSA SDK units rather than private AROSA Pascal source. A matching executable was staged for runtime testing.

**i386 AROS runtime execution has not been verified.** AGet/ATransfer stalled during test deployment; it does not prove that the SDK-built AFileManager failed to run. **The historical x86_64 SDK has not yet been compiled or tested.** Bugs are welcome at [Issues](https://github.com/danilos/AROSA-SDK/issues), but continued i386 compatibility or fixes are not promised.

## Contents and availability

- [Release and platform support policy](docs/release-policy.md)
- [i386 historical validation record](docs/0.18.6.0.0.0-status.md)
- [SDK distribution contract](docs/sdk-distribution-contract.md)

A clean experimental i386 SDK **candidate archive** has been prepared externally, containing 234 compiled Pascal units, 234 compiled object files, four static libraries and an integrity manifest. The historical test executable and private filesystem paths were removed. **The candidate binary has not been published to GitHub**: exact third-party license notices and required source availability still need review before general redistribution. The original internal PRIVATE-REVIEW archive must never be published unmodified.

The public application source can be found at [danilos/AFileManager](https://github.com/danilos/AFileManager), under its existing MPL-2.0 terms. Publishing binary SDK objects does not by itself satisfy any applicable covered-source obligations, and this repository does not grant rights to unrelated private AROSA implementation source.

Original AROSA components copyright (c) 2026 **DaniloS**; all third-party copyrights and licenses remain with their owners.
