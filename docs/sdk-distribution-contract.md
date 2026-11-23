# AROSA SDK distribution contract

Status: **proposed developer-use and binary redistribution terms — review draft, not yet an operative license grant**, 2026-11-23.

Copyright (c) 2026 Danilo Sandron for original AROSA implementations, subject to other owners' rights in incorporated components.

## Purpose and separation

The AROSA SDK enables developers to build applications consuming and providing AROSA capabilities. The SDK is **not** a source publication of the privately developed AROSA platform. Original AROSA SDK code, runtime services, implementation units and bridge code remain controlled by their respective rights holders. AFileManager's separate MPL-2.0 license does not relicense the AROSA platform or its SDK.

This document states an **intended distribution contract** and conditions to approve before any SDK binary publication. It does not override the licenses of third-party components and does not authorize release of the current withheld SDK ZIP.

## Proposed permission for future authorized SDK releases

Once Danilo Sandron expressly approves a particular, versioned SDK release and publishes its accompanying license:

1. **Use:** Recipients may use the released SDK interfaces, headers, compiled units, objects and link libraries solely to develop, compile, test, link, execute and distribute applications interoperating with compatible AROSA runtimes, subject to component-level terms.
2. **Application distribution:** Developers retain rights in their independently authored applications. Subject to applicable third-party licenses, they may distribute their applications, including portions of expressly designated AROSA SDK runtime/link code necessarily incorporated by the normal linking process. The released SDK's manifest/license must identify which components carry that permission; unspecified components are not automatically covered.
3. **SDK redistribution:** Republishing, repackaging or mirroring the SDK itself requires separate permission unless the eventual release license expressly grants that right. Linking an application is not, by itself, authorization to redistribute the complete SDK.
4. **Private platform source:** No permission is granted to copy, publish, sublicense or redistribute nonpublic AROSA service implementations, unpublished provider code, development infrastructure or unrelated repositories.
5. **Third-party rights:** ThorVG, Brotli, tinf, NanoSVG, FreeType, AROS/AROS Public License-covered materials, Free Pascal/RTL and any other third-party code retain their own notices, attribution, conditions and applicable source-availability duties. The AROSA author cannot waive those conditions.
6. **Compatibility:** The permission applies only to explicitly identified released files/versions. No guarantee is made that different versions or compilers are ABI-compatible, or that i386 support will continue. The SDK shall not be represented as a complete AROSA installation.
7. **Marks and warranty:** Distribution does not grant rights in project names or marks beyond factual identification of compatibility. Any warranty disclaimer or liability terms require final text in the adopted license and must not conflict with applicable mandatory law.

**Important:** This is a policy draft rather than a complete, legally operative SDK EULA. The actual release must carry a specific final license text, explicit identification of redistributable linked object code, copyright and license notices, source-availability instructions where relevant, and a release manifest. Counsel review is recommended before adoption.

## Intended SDK contents

Subject to component-by-component rights clearance:

- Public Pascal service/capability contracts, descriptors and documentation.
- Precompiled target-compatible Free Pascal units and object code necessary for linking applications.
- Native AROS-facing graphics, font, C++ ABI and other bridge libraries that may legally be redistributed.
- Build instructions, application templates and examples.
- A manifest identifying the six-component AROSA version, architecture, AROS variant, compiler and RTL constraints, object hashes, third-party notices and build provenance.

## Compatibility and validation gates

1. Consult the authoritative AROSA master registry and exact historical source/build evidence, preserving feature continuity.
2. Confirm archive file inventory, complete SHA-256 coverage, target ELF architecture and absence of private paths, credentials, test executables and unrelated backups.
3. Verify origin and distribution rights of each SDK object/library and any linked third-party code; include authentic notices and fulfill source-availability obligations that apply.
4. Verify a clean consumer build/link without private source paths, then separately test actual runtime operation. Record the specific test coverage.
5. Publish only architectures that pass their relevant gates, with an immutable release name and checksum.

## Historical x86_64 candidate — 0.18.6.0.0.0

The owner reports that the **private** `AROSA-SDK-0.18.6.0.0.0-x86_64-NOTICES-PRIVATE.zip` under the authorized `.../TRANSFER/AFileManager-0.30.19.2.0.0/` directory passed CRC, SHA-256 manifest and byte-preservation tests: 481 files; 480 checksums; 473 compiled unit/object/archive files identical to the previous reviewed private ZIP; six third-party notice files added; no original file removed. The original and new SDK archives have **not** been published.

An independent public-source AFileManager x86_64 compile/link and graphical startup were previously reported successful. General file operations, stability, all ABI combinations, and broad regression coverage were **not** verified. A separate experimental i386 build/link previously passed, but runtime launch has not been verified.

**Remaining release gates:** component-specific ownership/third-party obligations for compiled units and bindings; C++ ABI/FreeType/NanoSVG embedded-code distinction; precise historical vendor source-byte-to-binary provenance where needed; adoption of final SDK license; and compatibility documentation. Passing the packaging audit does not close those gates.

## Developer application lifecycle

An application declares requested and offered capabilities through descriptors and consumes SDK interfaces. At runtime, AROSA resolves compatible services and providers through capability composition. Both conventional Pascal development and AIDEa-generated application development are intended consumers.

The first independently published source consumer is [AFileManager](https://github.com/danilos/AFileManager).
