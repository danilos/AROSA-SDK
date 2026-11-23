# AROSA SDK examples

**AROSA**  
*Written for AROS*

Version **0.18.6.0.0.0** · x86_64 AROS · Original AROSA author: **DaniloS**

Download the [licensed SDK binary](https://github.com/danilos/AROSA-SDK/releases/tag/v0.18.6.0.0.0-x86_64), including compiled Pascal units, native libraries, `SDK-LICENSE.md`, third-party notices and a checksum manifest.

## Examples

1. [hello_arosa.pas](hello_arosa.pas) — minimal Pascal consumer importing `Arosa.Version`.
2. [build-hello-arosa.sh](build-hello-arosa.sh) — compiles and links the sample with the matching AROS cross-compiler and `collect-aros` linker.
3. [inspect_sdk.py](inspect_sdk.py) — checks an SDK ZIP’s CRC, manifest and compiled-file inventory without extracting or modifying it.
4. [service-pattern.md](service-pattern.md) — documentation-service consumption example derived from AFileManager.
5. [package-sdk-license.py](package-sdk-license.py) — historical release-maintenance utility for producing a new ZIP containing the developer license; **not required** for the current licensed download.
6. [AFileManager](https://github.com/danilos/AFileManager) — complete example application source, released separately under MPL-2.0.

## Build HelloAROSA

The SDK does **not** supply Free Pascal, AROS system libraries or the complete operating system. Install a compatible x86_64 AROS toolchain and use the matching Free Pascal RTL and SDK build defines.

```bash
export SDK_ROOT="/path/to/extracted/AROSA-SDK"
export AROS_FPC="/path/to/AROS/ppcrossx64"
export AROS_CC="x86_64-aros-gcc"
export AROS_COLLECT="x86_64-aros-collect-aros"
export AROS_RTL="/path/to/matching/x86_64-aros/rtl/units"
export AROS_LIB="/path/to/AROS/target/libraries"
export OUTPUT_DIR="/path/to/pre-existing/empty/output-directory"

export AROS_SMP_DEFINE="AROSPLATFORM_SMP"
export AROS_BINCOMPAT_DEFINE="AROS_BINCOMPAT"
export FPC_CPU_SWITCH="-Px86_64"

bash examples/build-hello-arosa.sh
file "$OUTPUT_DIR/HelloAROSA"
```

The script requires an **existing empty output directory** and refuses to overwrite populated directories. The compiler and SDK must agree on target architecture, RTL, binding layouts and AROS ABI. For the historical validated build, `AROSPLATFORM_SMP` was the SMP compile definition.

## Validation results

- The independent HelloAROSA sample compiled and linked on x86_64 AROS using the historical Free Pascal cross-compiler, AROS GCC and `collect-aros` (23 November 2026).
- The output was identified as an x86-64 AROS ELF executable.
- The historical AFileManager example separately compiled, linked and launched its GUI on x86_64 AROS.
- Executing **HelloAROSA itself** inside booted AROS is not yet verified. General compatibility and long-term runtime stability are not guaranteed.

## Release integrity

The published [licensed ZIP](https://github.com/danilos/AROSA-SDK/releases/tag/v0.18.6.0.0.0-x86_64) contains **482 entries, 481 SHA-256 checksums, 473 compiled artifacts and six third-party notice files**.

**SHA-256:** `36e1c7ce16974b8e8456e3fa28a9d8f6048ac563d1eb6e2cfb3c0c8902d37f92`

```bash
python3 examples/inspect_sdk.py /path/to/AROSA-SDK-0.18.6.0.0.0-x86_64-LICENSED.zip
```

See [SDK release notes](../docs/0.18.6.0.0.0-x86_64-release-notes.md) and the [SDK Developer License](../SDK-LICENSE.md) for terms, supported targets and limitations.
