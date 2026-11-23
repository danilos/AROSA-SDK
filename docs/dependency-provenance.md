# AROSA SDK dependency provenance and redistribution review

Review date: 2026-11-23. Publication status: **binary SDK withheld pending component-level rights clearance**.

## x86_64 candidate — verified directly from uploaded ZIP

Historical baseline: AROSA **0.18.6.0.0.0**, source revision `384eeaf25214142aeeb93792fc45ae0858d67d07`.

The corrected 64-bit private archive contains **475 files**: 234 Pascal compiled units (`.ppu`), 234 compiled object files (`.o`), five static libraries (`.a`), `SDK-STATUS.txt` and `SHA256SUMS`. All **474** checksum entries match. ZIP CRC and archive inventory checks passed. The unnecessary historical AFileManager test executable is excluded, and private absolute filesystem paths were removed from the status metadata. No underlying SDK compiled object or unit was changed between the corrected and status-refreshed candidates.

Five static libraries have x86_64 ELF object members: `libarosa_tvg.a`, `libarosa_wf.a`, `libarosa_nanosvg.a`, `libarosa_freetype2_bridge.a`, and `libarosa_cxxabi.a`.

The historical independent public-source AFileManager build/link and x86_64 graphical startup passed per owner evidence. File operations, shutdown, stability, ABI/toolchain compatibility outside the tested compiler, and general application compatibility are **not verified**.

## Upstream license families and unresolved binary correspondence

| Local component | Reference upstream | Reported upstream license | Required before SDK binary publication |
| --- | --- | --- | --- |
| `libarosa_tvg.a` / ThorVG | https://github.com/thorvg/thorvg | MIT | Match actual vendored source revision, modifications, all notices and embedded dependencies |
| Brotli objects in `libarosa_wf.a` | https://github.com/google/brotli | MIT | Identify actual source revision, included objects, license and copyright notice |
| tinf objects in `libarosa_wf.a` | https://github.com/jibsen/tinf | zlib | Verify exact fork/revision and original notices |
| `libarosa_nanosvg.a` | https://github.com/memononen/nanosvg | zlib | Verify exact AROS-local source and modifications |
| `libarosa_freetype2_bridge.a` | Original AROSA bridge, external FreeType interfaces | Under review | Show bridge object is original and document linked external FreeType requirements |
| `libarosa_cxxabi.a` | Historical C++ ABI provider | Under review | Check generated code and compiler/runtime provenance |
| `bindings/*` | FPC and AROS API bindings | Component-specific | Verify source origins and relevant AROS Public License and FPC/RTL conditions |
| `units/*` | AROSA historical source, possibly external imports | Component-specific | Audit ownership, original versus imported/modified covered code, and required source availability |

Upstream license-family references are **not** evidence that the bundled binaries were built from the referenced revisions. The historical source snapshot did not include the vendor source trees; local historical build steps reused third-party directories and AROS-local NanoSVG. Do not substitute current upstream license text for the exact vendored notices without examining provenance.

Free Pascal's runtime and package licenses commonly include a linking exception, but that does not automatically relicense independently authored AROSA code or any imported third-party code. AROS components may be subject to the AROS Public License. All relevant terms must be assessed at the component level.

## Local source and license evidence — owner terminal, 2026-11-23

In the local AROSA checkout (not the private GitHub API checkout), the owner confirmed:

| Dependency | Local license file | SHA-256 of local license file | Copyright/license evidenced by file excerpt |
| --- | --- | --- | --- |
| ThorVG | `thirdparty/thorvg/LICENSE` | `74242cdc4ccaebc73fa04fbd52a538429eae2be7a231f9eaf1dbf59d2bedc16b` | MIT; copyright 2020–2026 ThorVG Project |
| Brotli | `thirdparty/brotli/LICENSE` | `3d180008e36922a4e8daec11c34c7af264fed5962d07924aea928c38e8663c94` | MIT-form permission text; copyright 2009, 2010, 2013–2016 Brotli Authors |
| tinf | `thirdparty/tinf/LICENSE` | `f39b507b81b9ba1edce7fe742bbd68fda4b852063ce7299274ae97991d48814b` | zlib; copyright 2003–2019 Joergen Ibsen |

The owner also located `nanosvg.h` and `nanosvgrast.h` at `/home/danilo/dev/AROS/dev/AROS/libraries/nanosvg/upstream/`. Their header copyright/license text and source revision have not yet been inspected.

The `git log -1 -- thirdparty/<name>` command returned parent commit `dc8dcedc81dbdd9860f3ef1cc68f08e4ceb403aa` dated 2026-11-04, labelled *register pinned Gitea dependency submodules*. **This does not identify the submodule's own HEAD or prove those files match the historical binary build.** Required follow-up: `git submodule status`, `git -C thirdparty/<name> rev-parse HEAD`, and dirty-status checks; capture actual NanoSVG header license, source revision and modifications. Preserve exact verified notices in the eventual release archive.

## Binary release gates

1. Record each source directory or source archive with exact Git revision (or source tree digest), modifications, and matching library/object evidence.
2. Preserve the authentic copyright and license notices for the actual compiled versions, plus any required source offer/access and modification notices.
3. Classify all AROSA compiled units and bridge objects by ownership, third-party imports and covered-source obligations; do not assume compiled units are exempt.
4. Fix and document the exact FPC/AROS SDK ABI, toolchain, and runtime compatibility.
5. Revalidate the immutable release ZIP, all member hashes and manifest after notice changes, then perform an independent consumer build and runtime smoke test.
6. Publish a binary release **only when the above gates are explicitly cleared**. Public documentation can be updated independently.

## Historic i386 candidate

The earlier, separate i386 SDK candidate had 234 `.ppu`, 234 `.o`, and four `.a` libraries. Its build/link test passed, but the SDK-built AFileManager did not open on the attempted i386 AROS runtime. i386 is experimental, best-effort and not guaranteed. This review does not upgrade its status.

Original AROSA components copyright (c) 2026 **DaniloS**. Third-party copyrights remain with their respective owners. Nothing in this note grants a blanket license to private AROSA implementation code.
