# AROSA SDK distribution contract

Status: **developer-use license published for SDK 0.18.6.0.0.0**; see [SDK-LICENSE.md](../SDK-LICENSE.md). This document is explanatory release policy, 2026-11-23.

Copyright (c) 2026 DaniloS for original AROSA implementations, subject to other owners' rights in incorporated components.

## Purpose and separation

The AROSA SDK enables developers to build applications consuming and providing AROSA capabilities. The SDK is **not** a source publication of the privately developed AROSA platform. Original AROSA SDK code, runtime services, implementation units and bridge code remain controlled by their respective rights holders. AFileManager's separate MPL-2.0 license does not relicense the AROSA platform or its SDK.

This document explains the developer-use terms adopted for the historical SDK release. DaniloS controls authorization for original AROSA code; no external general-purpose ownership clearance is required. Specific terms of incorporated third-party components continue to apply.

## Developer permissions for authorized SDK releases

The published [SDK Developer License](../SDK-LICENSE.md) sets the operative permissions for the historical 0.18.6.0.0.0 SDK when distributed under that license:

1. **Use:** Recipients may use the released SDK interfaces, headers, compiled units, objects and link libraries solely to develop, compile, test, link, execute and distribute applications interoperating with compatible AROSA runtimes, subject to component-level terms.
2. **Application distribution:** Developers retain rights in their independently authored applications. Subject to applicable third-party licenses, they may distribute their applications, including portions of expressly designated AROSA SDK runtime/link code necessarily incorporated by the normal linking process. The released SDK's manifest/license must identify which components carry that permission; unspecified components are not automatically covered.
3. **SDK redistribution:** Republishing, repackaging or mirroring the SDK itself requires separate permission unless the eventual release license expressly grants that right. Linking an application is not, by itself, authorization to redistribute the complete SDK.
4. **Private platform source:** No permission is granted to copy, publish, sublicense or redistribute nonpublic AROSA service implementations, unpublished provider code, development infrastructure or unrelated repositories.
5. **Third-party rights:** ThorVG, Brotli, tinf, NanoSVG, FreeType, AROS/AROS Public License-covered materials, Free Pascal/RTL and any other third-party code retain their own notices, attribution, conditions and applicable source-availability duties. The AROSA author cannot waive those conditions.
6. **Compatibility:** The permission applies only to explicitly identified released files/versions. No guarantee is made that different versions or compilers are ABI-compatible, or that i386 support will continue. The SDK shall not be represented as a complete AROSA installation.
7. **Marks and warranty:** Distribution does not grant rights in project names or marks beyond factual identification of compatibility. Any warranty disclaimer or liability terms require final text in the adopted license and must not conflict with applicable mandatory law.

**Important:** The SDK Developer License is the authoritative AROSA-authored code grant, not this explanatory policy. Actual release assets must preserve the third-party notices and accompanying manifest. Any specific rights of third-party incorporated code remain governed by their individual licenses.

## Intended SDK contents

For the approved, versioned SDK package:

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

## Historical x86_64 SDK release — 0.18.6.0.0.0

The official [GitHub release](https://github.com/danilos/AROSA-SDK/releases/tag/v0.18.6.0.0.0-x86_64) contains a **licensed self-contained archive** `AROSA-SDK-0.18.6.0.0.0-x86_64-LICENSED.zip`. Owner Mint-DT output confirmed upload success and asset listing on 23 November 2026. SHA-256: `36e1c7ce16974b8e8456e3fa28a9d8f6048ac563d1eb6e2cfb3c0c8902d37f92`. The official `SDK-LICENSE.md` is inside the ZIP, with 482 ZIP entries, 481 manifest hashes, 473 byte-preserved compiled artifacts, and six authentic third-party notice files; ZIP CRC and complete SHA-256 validation passed.

The previous `AROSA-SDK-0.18.6.0.0.0-x86_64-NOTICES-PRIVATE.zip` asset is superseded; its removal from the release is still pending final owner action. AFileManager x86_64 independent build/link and GUI launch PASS; HelloAROSA independent x86_64 build/link PASS. General file operations, stability, ABI variations and HelloAROSA runtime execution have not been broadly verified. The i386 build is experimental and not part of this release.

The adopted developer license covers original AROSA-authored SDK components while respecting independent third-party licenses. Any distinct source-availability duties for incorporated third-party materials remain governed by their applicable licenses.

## Developer application lifecycle

An application declares requested and offered capabilities through descriptors and consumes SDK interfaces. At runtime, AROSA resolves compatible services and providers through capability composition. Both conventional Pascal development and AIDEa-generated application development are intended consumers.

The first independently published source consumer is [AFileManager](https://github.com/danilos/AFileManager).
