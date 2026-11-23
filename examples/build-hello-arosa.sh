#!/usr/bin/env bash
# Copyright (c) 2026 DaniloS
# Historical AROSA SDK 0.18.6.0.0.0 — x86_64 AROS SDK consumer example.
# Does not access private AROSA sources or make directories.
set -Eeuo pipefail

here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
source_file="$here/hello_arosa.pas"

required=(AROS_FPC AROS_CC AROS_COLLECT AROS_RTL AROS_LIB SDK_ROOT OUTPUT_DIR AROS_SMP_DEFINE)
for key in "${required[@]}"; do
  if [[ -z "${!key:-}" ]]; then
    printf 'ERROR: set %s (see examples/README.md)\n' "$key" >&2
    exit 2
  fi
done

[[ -f "$source_file" ]] || { echo "ERROR: missing $source_file" >&2; exit 2; }
[[ -d "$OUTPUT_DIR" ]] || { echo "ERROR: OUTPUT_DIR must already exist: $OUTPUT_DIR" >&2; exit 2; }
[[ -d "$AROS_RTL" && -d "$AROS_LIB" ]] || { echo 'ERROR: missing AROS RTL/lib directory' >&2; exit 2; }
for dir in "$SDK_ROOT/units" "$SDK_ROOT/bindings" "$SDK_ROOT/lib"; do
  [[ -d "$dir" ]] || { echo "ERROR: missing SDK directory $dir" >&2; exit 2; }
done
[[ -f "$SDK_ROOT/units/Arosa.Version.ppu" ]] || { echo 'ERROR: wrong SDK or Arosa.Version.ppu missing' >&2; exit 2; }

# Avoid deleting or replacing unrelated build files. Require a dedicated empty output drawer.
if [[ -n "$(find "$OUTPUT_DIR" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "ERROR: OUTPUT_DIR must be empty; refusing to overwrite: $OUTPUT_DIR" >&2
  exit 2
fi

cpu_switch="${FPC_CPU_SWITCH:--Px86_64}"
bincompat_define="${AROS_BINCOMPAT_DEFINE:-AROS_BINCOMPAT}"
[[ "$cpu_switch" == -* ]] || { echo 'ERROR: FPC_CPU_SWITCH must be one compiler option' >&2; exit 2; }
[[ "$bincompat_define" =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]] || { echo 'ERROR: invalid AROS_BINCOMPAT_DEFINE' >&2; exit 2; }
[[ "$AROS_SMP_DEFINE" =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]] || { echo 'ERROR: invalid AROS_SMP_DEFINE' >&2; exit 2; }

# Disable compiler's normal linker; use the same AROS collector approach as historical AFileManager.
(
  cd "$OUTPUT_DIR"
  "$AROS_FPC" -n -TAROS "$cpu_switch" -Cn \
    "-d$AROS_SMP_DEFINE" "-d$bincompat_define" \
    -Fu"$AROS_RTL" -Fu"$SDK_ROOT/bindings" -Fu"$SDK_ROOT/units" \
    -Fl"$SDK_ROOT/lib" -FU"$OUTPUT_DIR" -FE"$OUTPUT_DIR" "$source_file"
)

mapfile -d '' response_files < <(find "$OUTPUT_DIR" -maxdepth 1 -type f -name 'link*.res' -print0)
if [[ ${#response_files[@]} -ne 1 ]]; then
  printf 'ERROR: expected one FPC link response, found %s\n' "${#response_files[@]}" >&2
  exit 1
fi

libgcc_path=$("$AROS_CC" -print-libgcc-file-name)
[[ -f "$libgcc_path" ]] || { echo "ERROR: compiler libgcc not found: $libgcc_path" >&2; exit 1; }

# Historical AFileManager used collect-aros, startup entry and target platform libraries.
"$AROS_COLLECT" -e __startup_entry \
  -L"$AROS_LIB" -L"$AROS_RTL" -L"$SDK_ROOT/bindings" -L"$SDK_ROOT/lib" \
  -L"$(dirname -- "$libgcc_path")" \
  -o "$OUTPUT_DIR/HelloAROSA" "${response_files[0]}" \
  -lposixc -lstdcio -lstdc -lm -lgcc

[[ -f "$OUTPUT_DIR/HelloAROSA" ]] || { echo 'ERROR: collector did not produce HelloAROSA' >&2; exit 1; }
file "$OUTPUT_DIR/HelloAROSA"
echo "PASS: linked example: $OUTPUT_DIR/HelloAROSA"
