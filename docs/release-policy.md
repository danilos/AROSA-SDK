# AROSA SDK — Experimental release support policy

**23 November 2026.** Active platform testing has moved to **64-bit AROS (x86_64)**. **32-bit AROS (i386) support is experimental, best effort, and is not guaranteed.**

## Verified

Historical AROSA baseline 0.18.6.0.0.0 i386 compiled and linked successfully. An independently built public AFileManager source checkout also compiled and linked with the i386 binary SDK, without private Pascal source paths. The resulting executable was copied to an isolated runtime test drawer and verified identical.

## Not verified

AFileManager launch on booted i386 AROS; x86_64 historical SDK build/runtime; cross-toolchain portability. An AGet transfer stalled during test setup but is not evidence of an AFileManager application failure.

**x86_64 is the forward development priority, not a claim of completed x86_64 tests.** Users are invited to file issues at https://github.com/danilos/AROSA-SDK/issues with CPU/AROS, SDK and FPC versions, reproducible steps, and logs. i386 bugs will be handled as resources permit, without guaranteed compatibility or maintenance.

## SDK artifacts and licensing

A cleaned experimental i386 SDK archive has been prepared from the private validated build, including 234 Pascal units, 234 compiled objects, four static libraries, SHA256 manifest and component origin notes. It deliberately excludes the historical executable and private source staging paths. **The binary archive has not been uploaded publicly** because original third-party notices, licensing and applicable source-availability obligations still require reconciliation. This policy does not grant a blanket license to private AROSA implementations.

Original AROSA components copyright (c) 2026 DaniloS; third-party owners retain their rights. The independently published AFileManager source remains under its existing MPL-2.0 license.
