# AROSA SDK — Release support policy

**AROSA**  
*Written for AROS*

The historical **0.18.6.0.0.0 x86_64 developer SDK** is available on [GitHub Releases](https://github.com/danilos/AROSA-SDK/releases/tag/v0.18.6.0.0.0-x86_64).

## Platform support

**x86_64 AROS** is the primary tested target. The SDK requires a matching AROS Free Pascal cross-compiler, target RTL, libraries, and compatible AROSA runtime.

**i386 AROS** remains experimental. A historical i386 build and link succeeded, but successful application startup was not established. No i386 SDK release is provided here.

## Verified functionality

- Independent AFileManager compilation and linking against the compiled x86_64 SDK.
- AFileManager graphical startup on x86_64 AROS.
- Independent HelloAROSA sample compilation and linking.
- Licensed release archive: 482 files, 481 SHA-256 manifest entries, 473 compiled artifacts, six third-party notice files; CRC and manifest verification passed.

These tests do not establish complete application compatibility, broad functional reliability, or long-running stability. HelloAROSA runtime execution on AROS has not been verified.

## Licensing and distribution

The released SDK includes the [DaniloS SDK Developer License](../SDK-LICENSE.md), relevant third-party notices and a checksum manifest. The [public AFileManager source](https://github.com/danilos/AFileManager) is separately distributed under MPL-2.0. AROSA platform implementation source is not included in this SDK.

Report reproducible problems at [AROSA-SDK Issues](https://github.com/danilos/AROSA-SDK/issues), including the architecture, compiler version, SDK version and reproduction steps.
