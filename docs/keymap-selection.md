# Selecting keymaps

The original `config/lily58.keymap` remains the default. The new
`config/clean.keymap` is the independent replacement design. Preserve the
original until Javi is comfortable with its replacement and requests retirement.

## Commands and artifacts

| Command | Selected file | Output directory |
| --- | --- | --- |
| `./scripts/build-local` | `config/lily58.keymap` | `firmware/` |
| `./scripts/build-local --keymap clean` | `config/clean.keymap` | `firmware/clean/` |
| `./scripts/build-local left --keymap clean` | `config/clean.keymap`, left half | `firmware/clean/` |
| `./scripts/build-local --keymap lily58` | `config/lily58.keymap` | `firmware/` |

The filename of each half's UF2 stays the same inside the selected output
directory. Build caches are isolated under `.local-build/build/NAME/` for
alternatives; the original keeps its existing `.local-build/build/` paths.

`./scripts/flash-left --keymap clean` builds and installs the new left map.
`./scripts/flash-left --keymap clean --no-build` installs the already-built clean
artifact. `./scripts/flash-left` selects the original. The flash script validates
the selection before interacting with the device and never falls back to another
keymap's artifact if the requested file is missing.

## ZMK v0.3 support

The pinned source's
`app/keymap-module/modules/modules.cmake` explicitly supports `KEYMAP_FILE`.
When supplied, it sets `DTC_OVERLAY_FILE` to that file and bypasses automatic
keymap discovery. Inside the local Docker workspace, the relevant arguments are:

```sh
west build -s zmk/app -d build/clean/lily58_left-nice_nano_v2-zmk \
  -b nice_nano_v2 -S studio-rpc-usb-uart -- \
  -DZMK_CONFIG=/config -DZMK_EXTRA_MODULES=/local-module \
  -DSHIELD=lily58_left -DKEYMAP_FILE=/config/clean.keymap
```

The wrapper supplies `KEYMAP_FILE` explicitly for the original too, preventing
CMake's cached selection from accidentally persisting across keymap choices.
Both variants share `config/lily58.conf`, the hardware definitions, and the USB
reset module. Selecting a keymap changes the bindings without replacing the
working firmware infrastructure.

GitHub Actions continues building the original targets from the unchanged
`build.yaml`. Its reusable workflow accepts `cmake-args` for passing the same
`KEYMAP_FILE` option if named variants are added to its matrix in the future.
The local selector does not modify the GitHub matrix.

## Verification

During initial setup on 2026-10-16, both halves built with `KEYMAP_FILE=/config/clean.keymap` and
produced valid nRF52840 UF2s. The generated devicetrees contained exactly one
QWERTY layer and no legacy custom home row modifier nodes. USB reset support
remained enabled only on the left. A subsequent default build selected
`/config/lily58.keymap` for both halves; the original keymap file was unchanged.
These were build checks; the alternative keymap was not flashed during setup.

Later that day, the complete ten-layer clean map replaced the minimal starting
point and both halves compiled successfully again. The generated devicetrees
contain all ten clean layers and the new home-row/one-shot behaviors. USB reset
support remains left-only. On 2026-10-21, `./scripts/flash-left --keymap clean`
rebuilt and installed the left artifact, backed up the previous firmware, and
verified the same USB serial returned as a HID keyboard. The right half was not
flashed. See `keymap-draft.md` for bindings and pending typing/shortcut checks.
