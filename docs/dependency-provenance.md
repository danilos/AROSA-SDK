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

## Submodule and NanoSVG checkout findings — owner terminal, 2026-11-23

The local AROSA `git submodule status` reported a leading `-` for each of the following, meaning **not initialized in that checkout**:

- Brotli gitlink: `0bbd31027957dbc2bb0d09c5908cccfeba1e8d3b`
- ThorVG gitlink: `cfbfbb9540745e3434922af6498dc32e09be3dfd`
- tinf gitlink: `655c7d23e52be48857b36aa1015be16f9827847e`

The subsequent `git -C thirdparty/{thorvg,brotli,tinf} rev-parse HEAD` returned parent AROSA HEAD `f8579925395a18c9229c2d58b7a1a453cfb67c11`, not a dependency revision, because the child directories were not initialized repositories. The recorded gitlink commits are **candidate pointers, not established source-to-binary correspondence**. Source files/license hashes exist locally, but their origins and correspondence still need verification. The owner also showed extensive unrelated modified/untracked AROSA working-tree files. Do not perform `git clean`, `reset`, or broad submodule updates as part of this audit.

NanoSVG local AROS upstream headers at `dev/AROS/libraries/nanosvg/upstream/` have:

- `nanosvg.h` SHA-256 `e34fd5d084be106cea972d19ce5d27fd96d17ba89f8d06bdceee058420c8b2b0`
- `nanosvgrast.h` SHA-256 `79a9c5f4db19debf9f3a648a1589e96d92854f245a5cb4f3d823f263785234d8`

Both embedded headers carry Mikko Mononen's 2013–2014 zlib-style copyright/license notice; the parser cites Anti-Grain Geometry 2.4 SVG example (Maxim Shemanarev) and the rasterizer cites stb_truetype rasterizer (Sean Barrett). The local `upstream` directory is **not a Git checkout**. Hashes and notices do not yet prove the packaged `libarosa_nanosvg.a` came from these precise headers; verify build source provenance.

## Vendor source paths and NanoSVG linker references — owner terminal, 2026-11-23

The parent AROSA working tree's `git ls-tree HEAD` confirms Gitlink objects (mode `160000`) with the following exact commit IDs and submodule remotes. These are **recorded revisions of private Gitea mirrors**, not proof of the precise source snapshot actually compiled into the SDK:

| Vendor | Gitlink commit | Configured Gitea submodule URL |
| --- | --- | --- |
| Brotli | `0bbd31027957dbc2bb0d09c5908cccfeba1e8d3b` | `http://gitea.starnet/danilo/AROSA-Brotli.git` |
| ThorVG | `cfbfbb9540745e3434922af6498dc32e09be3dfd` | `http://gitea.starnet/danilo/AROSA-ThorVG.git` |
| tinf | `655c7d23e52be48857b36aa1015be16f9827847e` | `http://gitea.starnet/danilo/AROSA-tinf.git` |

Source files are available in the local folders, but earlier `git submodule status` printed `-` for these submodules, and `git -C` fell back to the AROSA parent repository. The owner observed `thirdparty/thorvg/config.h` and `inc/thorvg.h` at depth ≤2; Brotli source is deeper than that scan; tinf source includes `tinfzlib.c`, `tinflate.c`, and `adler32.c`.

NanoSVG linking is controlled by AROSA `scripts/build-nanosvg-aros.sh`, which supports `AROSA_NANOSVG_REFERENCE_ARCHIVE`, and `applications/afilemanager/scripts/build.sh`, which uses a selected NanoSVG archive. The actual NanoSVG source headers are present under the separate AROS tree; **their exact use for the audited x86_64 `.a` is still not established**. The x86_64 package architecture and library checksum have separately passed.

A separate, read-only build-provenance review should now capture `scripts/build-nanosvg-aros.sh` inputs and relevant ThorVG/Brotli/tinf compiler commands, `git ls-tree <historical-SHA>` gitlinks, and source digests. Do not run `git submodule update` or cleanup against the active AROSA tree just to obtain provenance.

## Historical 0.18.6 versus current working-tree vendor pins — 2026-11-23

**Correction to interpretation of the current gitlinks:** owner ran `git ls-tree 384eeaf25214142aeeb93792fc45ae0858d67d07 thirdparty/thorvg thirdparty/brotli thirdparty/tinf` and it printed **no entries**. Thus the current checkout's three Gitea gitlinks are **not recorded at those paths in that historical commit**. Their SHA values cannot be attributed to the historical SDK build, even provisionally, without independent build inputs or source digests. No source-to-binary correspondence claim is made.

Current `scripts/build-nanosvg-aros.sh` is an architecture-aware *rebuilder*: it reads object names from `AROSA_NANOSVG_REFERENCE_ARCHIVE` (default `$AROS_ROOT/dev/AROS/libraries/nanosvg/build/libarosa_nanosvg.a`), maps each member uniquely to a .c/.cc/.cpp under `NANOSVG_SOURCE_ROOT`, compiles with the selected cross-compiler and archives at `$AROSA_BUILD/nanosvg/root/build/libarosa_nanosvg.a`. It does not prove the historical x86_64 SDK archive was built through this current script or which source revisions its inputs had. Current AFM build script displays `Building ThorVG (libarosa_tvg.a)` and `Building the outline font engine (libarosa_wf.a)`, but those echo lines alone do not identify vendor compilation commands.

Next evidence should prioritize historical versions of the build scripts using `git show 384eeaf...:<path>` (where existing), local SDK builder scripts and generated build logs, actual source checksums and archive member provenance. Read-only collection only; no repo reset, submodule update or private code publication.

## Exact historical AFM build commands — owner terminal, 2026-11-23

Read-only `git ls-tree 384eeaf25214142aeeb93792fc45ae0858d67d07 thirdparty/` and grep-based inventory show the historical commit **has no `thirdparty/` tree or pinned dependency gitlinks**. This is not evidence that vendor dependencies were absent at build time: the build referenced external checkout trees.

The actual **historical** `applications/afilemanager/scripts/build.sh` (from `git show`) gives the following evidence:

- `NANOSVG_ROOT` defaults to `$AROS_ROOT/dev/AROS/libraries/nanosvg`, with existing archive `$NANOSVG_ROOT/build/libarosa_nanosvg.a`; the script checks it exists.
- `source/platform/aros/fonts/arosa_freetype2_bridge.c` is compiled with `$AROS_CC -O2 -fno-common` into `$AROSA_BUILD/fontbridge/libarosa_freetype2_bridge.a`.
- `source/platform/vectorgraphics/build-tvg.sh aros $AROSA_BUILD/tvg` is invoked to construct `libarosa_tvg.a`.
- `source/platform/webfont/build-wf.sh aros $AROSA_BUILD/<WF_OUT>` is invoked to construct `libarosa_wf.a` (exact `WF_OUT` assignment not yet supplied).
- Final AFileManager invocation of `$AROS_COLLECT` references `-L` paths for AROS libs, RTL, bindings, NanoSVG, FreeType bridge, ThorVG and webfont, and links `-larosa_tvg -lstdc++`, conditional C++ ABI objects, `-larosa_wf -larosa_freetype2_bridge -lfreetype2 -lposixc -lstdcio -lstdc -lm -lgcc`. The snippet does not itself demonstrate which linker response-file objects include NanoSVG.
- SDK 0.18.6 current candidate contains five .a libraries and compiled Pascal units; distinguishing bundled .a contents from external `-lfreetype2` and RTL/runtime dependencies is required.

Next review historical contents of `source/platform/vectorgraphics/build-tvg.sh`, `source/platform/webfont/build-wf.sh`, original NanoSVG build script in AROS tree, and their source tree checksums (not only today's HEAD). Historical vendors' exact revisions, compiled-code license obligations and source correspondence are still unresolved; no binary release.

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
