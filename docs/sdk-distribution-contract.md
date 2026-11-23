# AROSA SDK distribution contract

Status: **proposed SDK packaging policy**, 2026-11-23.

## Scope

The developer SDK is an interface between public AROSA capability-consuming applications and a versioned AROSA runtime, not a mirror of the private platform source tree.

Intended SDK components, subject to rights clearance:

- Public Pascal service/capability contracts, descriptors and documentation.
- Precompiled target-compatible Free Pascal units and object code necessary for linking applications.
- Native AROS-facing bridge and graphics/font libraries where redistribution is permitted.
- Reproducible build tooling, application templates and examples.
- An explicit machine-readable manifest with architecture, toolchain/ABI, AROSA runtime version, hashes, component origins and dependency/notice references.

## Compatibility

A release must identify the complete six-component AROSA version, target CPU (`i386` or `x86_64`), AROS target variant, required FPC compiler/RTL and build defines, and any platform ABI compatibility requirements. A matching SDK/runtime pair is required; different versions must not be assumed compatible merely because a unit is named the same.

## Distribution safeguards

1. Check the authoritative AROSA project registry and exact source/build revision before building; reconcile parallel features, preserve existing functionality and document changes.
2. Confirm the full inventory: no staging snapshots, logs, internal environment paths, backup copies, unrelated executables, credentials, or unintended source material.
3. Review the origin and permissions of every distributable library/object and bundled third-party dependency. Include accurate attribution, license texts and source-availability information when legally required.
4. Perform compilation/link verification against the public application repository with no private AROSA source path in the consumer build. Record failures and ABI assumptions without marking them as passed.
5. Test target runtime behavior separately from build success. Publish architecture-specific artifacts only after each architecture's gates pass.
6. Release immutable versioned artifacts with checksum manifests and traceable changes.

## Initial candidate: 0.18.6.0.0.0

The i386 private SDK build and independent AFileManager consumer build are verified. The reviewed private bundle is **not** the release artifact: it includes an unnecessary application binary and stale/private-path metadata. Its redistribution, license coverage and AROS runtime behavior remain unapproved.

The public repository intentionally begins with documentation and the validation record. It contains **no** private AROSA implementations and makes **no** blanket license grant over implementations or precompiled libraries. Component-level licensing must be established before adding distributable files.

## Developer application lifecycle (planned)

An application declares requested and offered capabilities through descriptors and consumes SDK interfaces. At runtime, AROSA resolves compatible services and providers through capability composition. The SDK is expected to support both conventional Pascal authoring and AIDEa-generated application development.

The first concrete consumer is [AFileManager](https://github.com/danilos/AFileManager).
