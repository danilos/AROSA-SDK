# AROSA SDK — Included libraries and notices

**AROSA**  
*Written for AROS*

This page describes the components included in the published [AROSA SDK 0.18.6.0.0.0 x86_64 release](https://github.com/danilos/AROSA-SDK/releases/tag/v0.18.6.0.0.0-x86_64).

## SDK inventory

The licensed ZIP contains 234 compiled Pascal units (`.ppu`), 234 corresponding object files (`.o`), five static libraries (`.a`), the DaniloS `SDK-LICENSE.md`, six third-party notice files, and `SHA256SUMS`.

| Library | Role | Upstream component or provenance |
| --- | --- | --- |
| `libarosa_tvg.a` | Vector graphics integration | ThorVG (MIT) and AROSA integration code |
| `libarosa_wf.a` | Webfont/decoding support | Brotli (MIT-form), tinf (zlib), and AROSA integration code |
| `libarosa_nanosvg.a` | SVG parsing/rasterization bridge | NanoSVG (zlib) and AROSA integration code |
| `libarosa_freetype2_bridge.a` | AROSA font integration | Original AROSA bridge; relies on compatible external FreeType |
| `libarosa_cxxabi.a` | AROS C++ ABI compatibility | Original AROSA bridge |

Compiled AROSA-authored components are covered by the [SDK Developer License](../SDK-LICENSE.md). Third-party components retain their own copyrights and applicable license terms. Refer to the exact `THIRD-PARTY-NOTICES/` files included in the ZIP.

Some applications also require external AROS system libraries, Free Pascal RTL and FreeType libraries; these are not a complete toolchain bundled inside the SDK.

## Integrity and verification

The published licensed archive has **482 ZIP entries, 481 manifest entries, 473 preserved compiled artifacts and six third-party notice files**. Full ZIP CRC and SHA-256 manifest validation passed.

The reviewed historical ThorVG and webfont library member inventories matched the corresponding source compilation layout. That structural result is not a claim of byte-for-byte reproducible vendor builds.

**Official x86_64 release SHA-256:** `36e1c7ce16974b8e8456e3fa28a9d8f6048ac563d1eb6e2cfb3c0c8902d37f92`

See the [release notes](0.18.6.0.0.0-x86_64-release-notes.md) and [developer examples](../examples/README.md) for usage requirements and tested functionality. The separate i386 target is experimental and not included in this release.

Copyright for original AROSA code: **DaniloS**. Third-party copyrights remain with their respective owners.
