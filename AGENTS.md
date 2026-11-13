# Working in this repository

This is Javi's wireless Lily58 configuration for nice!nano v2 controllers,
pinned to ZMK v0.3. `config/lily58.keymap` is the preserved original;
`config/clean.keymap` is the new design in progress. Read the selected keymap for
its layout. Keep the
README independent of individual bindings and layer contents.

Use the physical position naming scheme in `docs/key-positions.md` when discussing
keys: side `L`/`R`, row `A`–`E`, columns numbered from center outward. Main columns
are `1`–`6`, extra inner keys are `LD0`/`RD0`, and thumbs are `E1`–`E4`.
These names are independent of the assigned keys and ZMK's numeric indices.
Omitting the side means both halves: `D0` means `LD0` and `RD0`.
Read `docs/keymap-design-brief.md` before proposing changes to the clean layout;
it records Javi's ergonomics, workflow requirements, and unresolved decisions.
`docs/keymap-draft.md` describes the first complete map implemented in
`config/clean.keymap`. Both halves compile; viewer review and physical testing
remain. Do not confuse build verification with a physical trial or flash.

## Build and install firmware

Local Docker builds and automated USB flashing are already installed and were
verified on the physical left controller on 2026-10-16.

- Build both halves: `./scripts/build-local`
- Build one half: `./scripts/build-local left` or `./scripts/build-local right`
- When asked to install left firmware: `./scripts/flash-left`
- Install an already-built left artifact: `./scripts/flash-left --no-build`
- Manual recovery/first installation: `./scripts/flash-left --bootstrap`

Both scripts accept `--keymap NAME`, selecting `config/NAME.keymap`. For example,
`./scripts/build-local --keymap clean` builds the new map, and
`./scripts/flash-left --keymap clean` installs it when requested. The default
remains `lily58`. Alternatives use separate caches and `firmware/NAME/` outputs.
Keep the original keymap until Javi explicitly requests its retirement. Building
the new keymap does not change the layout currently installed on the keyboard.
See `docs/keymap-selection.md` for the verified CMake selection mechanism.

The left half is normally connected by USB. Its serial is
`23E5F50B0A98298E`. The running left firmware supports the 1200-baud bootloader
trigger. Start with automated flashing; request a manual reset only if recovery
is necessary. The right half has no automated reset support in this setup.

The flash script builds, validates the UF2, targets the controller by USB serial,
requests reset, waits for its bootloader volume, backs up `CURRENT.UF2`, writes
the firmware, and verifies that the same serial returns as a USB HID keyboard.
Use this script to preserve those identity and completion checks.

Read [docs/usb-flashing.md](docs/usb-flashing.md) for implementation details,
verified behavior, and recovery. User-facing commands are also in `README.md`.

## Environment and implementation constraints

- Docker contains West, Python, and the Zephyr SDK. Use the pinned image in
  `scripts/build-local`; the host Python is newer than this ZMK toolchain.
- `.local-build/` caches dependencies and build output; `firmware/` holds UF2s
  and backups. Both are ignored by Git.
- Preserve `studio-rpc-usb-uart` on the left build in `build.yaml`.
- `zephyr/module.yml` registers this repository as a Zephyr module. GitHub's
  pinned reusable workflow discovers it; the local builder mounts `module/`
  and `zephyr/` explicitly. Keep both build paths working.
- The USB reset module uses ZMK v0.3's `sys_reboot(RST_UF2)` / GPREGRET path.
  Newer ZMK retention boot-mode APIs require a deliberate migration.
- Serial access is already configured through
  `/etc/udev/rules.d/70-lily58-bootloader.rules`. Its source is in `scripts/`.
  Run normal builds/flashes as Javi. For privileged setup, use Javi's
  `~/.local/bin/pkexec-tty` helper and follow the user's global instructions.
- Device access and Docker may require execution outside the Codex sandbox.
  A sandbox device-access error alone does not mean the keyboard is missing.

## Verification

For flashing-script changes, run `python -m unittest discover -s tests -v`.
For firmware/module changes, compile both halves and confirm that
`CONFIG_LILY58_USB_BOOTLOADER_TOUCH=y` appears only in the left build's `.config`.
Report build verification and physical flash verification separately.

## Backup input

The Omarchy plugin `io.github.abdxdev.onscreen-keyboard` is installed. Open it
with `omarchy-shell shell toggle io.github.abdxdev.onscreen-keyboard` if a backup
keyboard is needed. It accepts mouse clicks, retains the target application's
keyboard focus, and supports mouse dragging via its own top bar. Use this plugin
instead of recreating the temporary GTK/XWayland or wvkbd experiments from this
session; those experiments were removed.
