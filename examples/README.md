# AROSA SDK examples

Author: **DaniloS**. Historical SDK target: **AROSA 0.18.6.0.0.0**; x86_64 AROS is the primary supported experimental target. These examples are source/documentation, **not a claim of new runtime tests**.

## Start here

1. [Minimal Pascal SDK consumer](hello_arosa.pas) — imports a compiled AROSA SDK unit using the ordinary Free Pascal `uses` mechanism.
2. [Build and link the example](build-hello-arosa.sh) — standalone cross-compile + `collect-aros` script using only SDK, matching RTL, compiler and target libraries; writes only to a pre-existing empty output directory.
3. [Validate an SDK archive](inspect_sdk.py) — runs on the development host, checks its ZIP contents, the complete SHA-256 manifest, and reports what can be imported. **No extraction, no writes.**
4. [Service usage pattern](service-pattern.md) — actual AROSA documentation-service calls taken from the public AFileManager source, with lifecycle/ownership guidance.
5. [Existing full application](https://github.com/danilos/AFileManager) — the historical public AFileManager source is the largest working integration example. Its original `scripts/build.sh` refers to a **private AROSA build environment**; do not run that script unmodified expecting a standalone SDK build.

## Build and link the minimal example

Obtain a licensed SDK ZIP, extract it into an existing directory **under your approved development area**, and use the toolchain/AROS RTL that produced the SDK units. The historical tested target is x86_64 AROS, and the `AROS_BINCOMPAT` and SMP compile definitions **must match** the SDK's compiled binding layout.

The standalone [build-hello-arosa.sh](build-hello-arosa.sh) script compiles [hello_arosa.pas](hello_arosa.pas) without private AROSA sources, finds FPC's generated `link*.res`, then invokes the native AROS `collect-aros` linker with the documented platform libraries. It does **not** create directories or delete existing files. Use a pre-existing **empty** `OUTPUT_DIR`; if it contains anything, the script stops instead of overwriting it.

```bash
# Configure these using your EXISTING installed historical AROS toolchain.
# These are variable names, not verified fixed paths for your workstation:
export SDK_ROOT="/path/to/extracted/AROSA-SDK"
export AROS_FPC="/path/to/aros-compatible/ppcx64"
export AROS_CC="/path/to/aros-x86_64-cross-gcc"
export AROS_COLLECT="/path/to/collect-aros"
export AROS_RTL="/path/to/matching/fpc/rtl/units"
export AROS_LIB="/path/to/aros/target/libraries"
export OUTPUT_DIR="/path/to/existing/empty/build-directory"

# This must match the historical SDK build, not merely a guessed default.
export AROS_SMP_DEFINE="YOUR_HISTORICAL_SMP_DEFINE"
export AROS_BINCOMPAT_DEFINE="AROS_BINCOMPAT"
export FPC_CPU_SWITCH="-Px86_64"

bash examples/build-hello-arosa.sh
file "$OUTPUT_DIR/HelloAROSA"
```

`YOUR_HISTORICAL_SMP_DEFINE` is deliberately a placeholder because the existing SDK has not published a verified generic value. Check your SDK compiler/build configuration before running. The script verifies presence of `Arosa.Version.ppu` but does not claim compatibility with a different FPC compiler/RTL. `AROS_RTL` and `AROS_LIB` are **not included** in the 0.18.6 SDK ZIP and remain prerequisite target-toolchain assets.

### Verification status

- The script follows the historical AFileManager compiler/linker command pattern. Validate it with `bash -n` locally before running; a real AROS compile/link of this particular example is still required.
- **A real AROS compile/link of this new minimal example has not yet been performed**, and its successful runtime execution on AROS is unverified.
- The owner previously compiled and linked the more substantial [AFileManager](https://github.com/danilos/AFileManager) against historical SDK binaries and verified graphical startup on x86_64 AROS. That is independent evidence for the SDK/toolchain approach, **not** a passing test for this new script.

### AROS link considerations

The compiler runs with `-n -TAROS -Cn` and matching `-Fu` and `-Fl` paths. The collector uses `-e __startup_entry`, FPC's `link*.res`, `-lposixc -lstdcio -lstdc -lm -lgcc`, and the x86_64 cross-compiler's actual `libgcc` directory. These options are grounded in the public historical AFileManager builder. Larger examples that use SVG or fonts may additionally need the applicable `libarosa_tvg`, `libarosa_wf`, `libarosa_freetype2_bridge`, `libarosa_nanosvg`, `libarosa_cxxabi`, C++ and FreeType dependencies; do **not** add all those libraries unconditionally to this minimal program.

## Mint-DT one-directory validation (owner workflow)

For DaniloS's historical test machine, **all extracted SDK files, downloaded examples and build output go under the already authorized `TRANSFER/AFileManager-0.30.19.2.0.0/` directory**. Do not create audit or delivery directories elsewhere. Use an empty dedicated output folder and read, rather than modify, the existing toolchain.

```bash
WORK="/home/danilo/dev/FPC/AIDEa-Ecosystem/aidea_transfer/aidea/TRANSFER/AFileManager-0.30.19.2.0.0"
SDK="$WORK/AROSA-SDK-0.18.6.0.0.0-x86_64-NOTICES-PRIVATE.zip"
EXAMPLE="$WORK/AROSA-SDK-example-0.18.6"
test -f "$SDK" || { echo "Missing reviewed SDK: $SDK" >&2; exit 1; }
test ! -e "$EXAMPLE" || { echo "Refusing to overwrite existing: $EXAMPLE" >&2; exit 1; }
mkdir -p "$EXAMPLE/sdk" "$EXAMPLE/output"
curl -fsSL https://raw.githubusercontent.com/danilos/AROSA-SDK/main/examples/hello_arosa.pas -o "$EXAMPLE/hello_arosa.pas"
curl -fsSL https://raw.githubusercontent.com/danilos/AROSA-SDK/main/examples/build-hello-arosa.sh -o "$EXAMPLE/build-hello-arosa.sh"
unzip -q "$SDK" -d "$EXAMPLE/sdk"
export SDK_ROOT="$EXAMPLE/sdk" OUTPUT_DIR="$EXAMPLE/output"
# Supply the *existing* toolchain paths/defines from the historical working build:
# AROS_FPC, AROS_CC, AROS_COLLECT, AROS_RTL, AROS_LIB, AROS_SMP_DEFINE
bash "$EXAMPLE/build-hello-arosa.sh"
```

The workflow intentionally does **not** invent compiler paths or SMP settings. The compiler and linker variables must be set using the already working historical AROS toolchain, not substituted with host compilers. This validates the new minimal example and creates all files solely under `TRANSFER/`. **Do not claim the example passed on Mint-DT until actual terminal output confirms it.**

## What was tested

The owner previously verified x86_64 AFileManager compilation, linking and graphical startup. The **new minimal example has not yet been compiled or run**. The host-side validator uses only Python's standard library and can be run against the private 481-file, 480-hash candidate without extracting it.

No SDK binary is included in this examples directory. The original AROSA source remains private; third-party licenses stay with their owners.
