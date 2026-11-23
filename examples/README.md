# AROSA SDK examples

Author: **DaniloS**. Historical SDK target: **AROSA 0.18.6.0.0.0**; x86_64 AROS is the primary supported experimental target. These examples are source/documentation, **not a claim of new runtime tests**.

## Start here

1. [Minimal Pascal SDK consumer](hello_arosa.pas) — imports a compiled AROSA SDK unit using the ordinary Free Pascal `uses` mechanism.
2. [Validate an SDK archive](inspect_sdk.py) — runs on the development host, checks its ZIP contents, the complete SHA-256 manifest, and reports what can be imported. **No extraction, no writes.**
3. [Service usage pattern](service-pattern.md) — actual AROSA documentation-service calls taken from the public AFileManager source, with lifecycle/ownership guidance.
4. [Existing full application](https://github.com/danilos/AFileManager) — the historical public AFileManager source is the largest working integration example. Its original `scripts/build.sh` refers to a **private AROSA build environment**; do not run that script unmodified expecting a standalone SDK build.

## Compile a basic consumer (illustrative cross-compiler invocation)

Extract a licensed, architecture-matched SDK to your chosen **existing** build location. Do not copy it into or depend on private AROSA source. Match SDK architecture, FPC version/RTL, target AROS variant, `AROS_SMP_DEFINE`, and `AROS_BINCOMPAT` layout. The historical AFileManager script uses `-TAROS`, `-n`, `-Cn`, the target CPU switch, and `-Fu` paths for the RTL and compiled units; a compatible collector performs the final target link.

For an `x86_64` compiler with its **matching** AROS RTL installed, the first compilation step is conceptually:

```sh
# All environment variables must point at existing, matching target assets.
: "${AROS_FPC:?set compiler path}"
: "${AROS_RTL:?set AROS RTL directory}"
: "${SDK_UNITS:?set SDK extracted units directory}"
: "${SDK_BINDINGS:?set SDK extracted bindings directory}"
: "${BUILD_OUT:?set an existing writable output directory}"

"$AROS_FPC" -n -TAROS -Px86_64 -Cn \
  -dAROS_BINCOMPAT \
  -Fu"$AROS_RTL" -Fu"$SDK_BINDINGS" -Fu"$SDK_UNITS" \
  -FU"$BUILD_OUT" -FE"$BUILD_OUT" \
  examples/hello_arosa.pas
```

This is a **compilation recipe, not a verified one-command final linker**: the exact historical FPC binary, SMP define, object library search paths, native AROS toolchain, `collect-aros` linker invocation and runtime components must match the SDK. `-Px86_64` must be replaced if your compiler frontend expects a different architecture selection; consult your installed FPC `-i` output. Because `-Cn` intentionally omits final linking, producing an executable requires the appropriate AROS collector/link response step.

**Validated example workflow from the owner:** The historical SDK tooling packet included `prepare-sdk.sh` and `build-with-sdk.sh`; the latter was used to compile/link public AFileManager without private platform source. Those scripts are not assumed to be part of this published SDK repository. See [AFileManager's source](https://github.com/danilos/AFileManager) for a full dependency/use inventory.

## What was tested

The owner previously verified x86_64 AFileManager compilation, linking and graphical startup. The **new minimal example has not yet been compiled or run**. The host-side validator uses only Python's standard library and can be run against the private 481-file, 480-hash candidate without extracting it.

No SDK binary is included in this examples directory. The original AROSA source remains private; third-party licenses stay with their owners.
