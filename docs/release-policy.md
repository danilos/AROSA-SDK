# AROSA SDK — Experimental release support policy

**23 November 2026.** Active development prioritizes **64-bit AROS (x86_64)**. **32-bit AROS (i386) support is experimental, best effort and not guaranteed.**

## x86_64 verification

For historical AROSA **0.18.6.0.0.0**, an independent AFileManager build from public source compiled and linked with the historical x86_64 SDK and reached graphical startup, according to owner runtime evidence. The private candidate including authentic third-party notices was subsequently verified on Mint-DT: **481 ZIP members, 480 valid SHA-256 manifest entries, 473 unchanged compiled `.ppu`/`.o`/`.a` artifacts, six notice files added, no files removed and ZIP CRC passed**.

These are **specific successful checks**, not a claim that file operations, shutdown, stability, every compiler/toolchain, broader ABI or application compatibility have passed.

## i386 verification

A historical i386 AROSA SDK and independently built public AFileManager source were reported to compile/link successfully, without private AROSA source paths. A functioning i386 AFileManager graphical runtime launch was **not** verified. The i386 build is experimental and carries no ongoing maintenance guarantee.

## Public artifacts and licensing

**Neither the historical x86_64 nor i386 SDK binary ZIP has been published.** Both remain subject to component-level redistribution rights clearance, exact license/notice terms and any applicable covered-source obligations. Original AROSA implementation rights are retained by Danilo Sandron; other copyright holders retain their rights. No blanket license grant over AROSA implementations is implied by the [separate MPL-2.0 AFileManager source repository](https://github.com/danilos/AFileManager).

The [SDK distribution contract](sdk-distribution-contract.md) currently describes a **proposed**, not operative, binary SDK developer-use policy. No implied publication authorization is created by the passing private package audit.

Report reproducible issues at https://github.com/danilos/AROSA-SDK/issues, identifying CPU/AROS target, six-component SDK/AROSA versions, FPC/toolchain, repro steps and logs.
