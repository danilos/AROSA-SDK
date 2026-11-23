# SDK dependency provenance and redistribution review

Review date: 2026-11-23. Scope: historical AROSA 0.18.6.0.0.0 experimental i386 SDK candidate.

## Verified artifact inventory

The cleaned i386 candidate (not yet published as a GitHub binary) contains **234 Pascal .ppu units, 234 .o object files and four .a static libraries**. The archive's CRC and SHA-256 file manifest were verified. It does not contain the historical test AFileManager executable or private source paths. The binary units and objects still embody compiled implementations.

## Third-party license families

| Component / bundled library | Upstream | License family | Release follow-up |
| --- | --- | --- | --- |
| ThorVG, libarosa_tvg.a | https://github.com/thorvg/thorvg | MIT | Confirm exact bundled revision; bundle corresponding copyright/license text |
| Brotli, within libarosa_wf.a | https://github.com/google/brotli | MIT | Confirm exact vendored revision; include notice |
| tinf, within libarosa_wf.a | https://github.com/jibsen/tinf | zlib | Confirm this is the exact upstream/derivative lineage and include correct copyright |
| NanoSVG, libarosa_nanosvg.a | https://github.com/memononen/nanosvg | zlib | Confirm bundled revision and preserve relevant source notices |
| FreeType bridge, libarosa_freetype2_bridge.a | AROSA bridge / external FreeType APIs | Requires separation | Confirm whether bundled archive contains only the original bridge; document external library requirements |
| FPC/AROS precompiled bindings | Local Free Pascal and AROS toolchain | Component-specific | Identify actual source and linking/redistribution terms; provide required notices and source access |
| AROSA Pascal compiled units | Original AROSA source and any imports | Component-specific | Preserve owner rights; audit any third-party derived components and MPL-covered obligations |

**The license-family information does not prove the exact locally built source revisions or satisfy required copyright notices by itself.**

The historical source snapshot was extracted from Git commit `384eeaf25214142aeeb93792fc45ae0858d67d07`. The historical revision did not include the build's vendor source trees. The private builder reused local `thirdparty/thorvg`, `thirdparty/brotli`, `thirdparty/tinf`, while NanoSVG was linked from the local AROS build tree. Therefore **the exact component provenance is not yet pinned to the historical AROSA Git revision**.

## Distribution decision

- The repository documentation and experimental support policy are public.
- **The binary SDK candidate remains withheld from GitHub** pending copyright/notice and covered-source review. Experimental quality labeling does not waive legal license obligations.
- A separate exact-source correspondence question remains for the previously distributed October AFileManager preview binaries. The 4 November AROSA snapshot is not claimed to be identical to that October build.
- No further i386 runtime testing is required as an engineering prerequisite for stating `experimental/unsupported`, but no unverified runtime results will be claimed.

## Primary development direction

All new platform test effort should focus on `x86_64`. The historical SDK build kit supports `prepare-sdk.sh x86_64` and `build-with-sdk.sh x86_64`; running these requires the matching x86_64 cross-toolchain and native AROS libraries. It must generate separate architecture-specific artifacts, including any necessary x86_64 C++ ABI bridge.

Do not publish the resulting x86_64 artifact until compile/link, provenance, licensing and package checks are recorded.

Original AROSA components copyright (c) 2026 DaniloS. Upstream third-party authors retain their copyrights.
