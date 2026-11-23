# AROSA SDK — Developer distribution guide

**AROSA**  
*Written for AROS*

The [AROSA SDK 0.18.6.0.0.0 x86_64 release](https://github.com/danilos/AROSA-SDK/releases/tag/v0.18.6.0.0.0-x86_64) contains compiled interfaces and libraries used to develop applications for compatible AROSA environments.

## License and copyright

Original AROSA SDK components are covered by the [SDK Developer License](../SDK-LICENSE.md), included in the released ZIP. That license permits developers to compile, link, execute and distribute independently written applications, including eligible AROSA object code incorporated by normal linking, subject to its terms.

AROSA's complete platform implementation source is not distributed with the SDK. The [AFileManager application source](https://github.com/danilos/AFileManager) is published separately under MPL-2.0.

Third-party libraries and system components retain their own copyrights and licenses. Their notices are preserved in the `THIRD-PARTY-NOTICES/` directory of the SDK archive. The SDK license does not replace or override those terms.

## Contents

- Precompiled Pascal interfaces and corresponding object code.
- AROS-facing native bridge and support libraries.
- The SDK developer license, third-party notices and `SHA256SUMS` manifest.
- Public [integration examples and build instructions](../examples/README.md).

The SDK is not a full operating system, runtime distribution or bundled cross-compiler. A matching AROS toolchain, Free Pascal RTL and compatible runtime are required.

## Supported targets

The historical **x86_64** SDK compiled and linked against independent AFileManager and HelloAROSA consumers; AFileManager graphical startup was observed on x86_64 AROS. Broader functionality and long-term stability remain experimental.

The historical **i386** build is experimental and is not part of this published x86_64 SDK release.

## Published asset and integrity

**Asset:** `AROSA-SDK-0.18.6.0.0.0-x86_64-LICENSED.zip`

**SHA-256:** `36e1c7ce16974b8e8456e3fa28a9d8f6048ac563d1eb6e2cfb3c0c8902d37f92`

The archive contains 482 files, 481 manifest entries, 473 compiled artifacts and six third-party notice files. Its complete CRC and SHA-256 manifest checks passed. See the [release notes](0.18.6.0.0.0-x86_64-release-notes.md) for details.

Copyright for original AROSA SDK work (c) 2026 **DaniloS**.
