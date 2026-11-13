# Lily58 Wireless ZMK Config

Personal [ZMK](https://zmk.dev/) firmware configuration for a wireless Lily58 split keyboard using nice!nano v2 controllers.

## Repository contents

- `config/*.keymap` — independently selectable keymaps; `lily58` is the original.
- `config/lily58.conf` — firmware feature settings.
- `config/west.yml` — ZMK version and dependencies.
- `build.yaml` — build targets for the left and right halves.
- `.github/workflows/` — automated firmware builds through GitHub Actions.
- `module/` and `zephyr/module.yml` — USB bootloader reset support for ZMK v0.3.
- `scripts/` — local build and flashing tools.

Each keymap file is the source of truth for its layout and behavior.
Use the [physical key position names](docs/key-positions.md) when discussing
individual keys or ranges.

## Local builds

With Docker running, build both halves from the repository root:

```sh
./scripts/build-local
```

Use `./scripts/build-local left` or `./scripts/build-local right` to build one half.
The script reads `build.yaml`, including any Studio snippet, and writes `.uf2`
files to `firmware/`. Flash each file to its matching keyboard half as usual.

Select a keymap by its filename without the extension:

```sh
./scripts/build-local --keymap clean       # Both halves, config/clean.keymap
./scripts/build-local left --keymap clean  # Left only
./scripts/build-local --keymap lily58      # Original
```

The default remains `lily58`. Alternative keymaps have separate build caches and
outputs under `firmware/NAME/`, so building one preserves the original artifacts.
The selector passes ZMK's `KEYMAP_FILE` CMake option explicitly. See
[keymap selection](docs/keymap-selection.md) for details.

The first run downloads the pinned Docker toolchain and the dependencies from
`config/west.yml`. Later builds reuse `.local-build/` and can run offline once
everything is cached. Run `./scripts/build-local update` to refresh dependencies;
changes to `config/west.yml` also trigger an update automatically.

Both generated directories are ignored by Git. To force a clean compilation,
remove `.local-build/build/` and build again. To reset the entire local workspace,
remove `.local-build/`; the next build downloads the dependencies again.

## Automated left-half flashing

With the left half connected over USB, run:

```sh
./scripts/flash-left
```

This builds the left firmware, requests bootloader mode through the Studio USB
serial port, waits for the matching `NICENANO` drive, saves its `CURRENT.UF2` under
`firmware/backups/`, copies the new firmware, and verifies that the same controller
returns as a USB HID keyboard. Close ZMK Studio before running it. Use `--no-build`
to flash the existing local left firmware instead.

Use `./scripts/flash-left --keymap clean` to build and install an alternative,
or add `--no-build` to install its existing artifact from `firmware/clean/`.
Omitting `--keymap` always selects the original keymap.

The default USB serial is specific to this keyboard. For another left controller,
pass `--serial SERIAL` and update the serial in the USB access rule below. The
script deliberately targets only the left half; connect and flash the right half
separately when needed.

### First installation

The running firmware must contain the USB reset module before it can respond to
the automated request. Install it once with:

```sh
./scripts/flash-left --bootstrap
```

After the build, double-tap the **left** controller's reset button when prompted.
Subsequent runs can enter the bootloader automatically. `--bootstrap` also works
as a manual fallback.

The reset module watches the existing Studio CDC port. Selecting 1200 baud and
closing the port requests the same UF2 reboot as `&bootloader`. Other baud rates
do not trigger it; a port held open at 1200 waits until it is closed. It does not
poll during normal use. The module is enabled only on the compatible USB central
build, so it does not change the right half. Set
`CONFIG_LILY58_USB_BOOTLOADER_TOUCH=n` to disable it.

Both GitHub Actions and the local build load this repository as a Zephyr module;
there is no ZMK fork or external module dependency.

The automated workflow was verified on this keyboard on 2026-10-16. See
[USB flashing notes](docs/usb-flashing.md) for the reset mechanism, device
identity, completion checks, and recovery. [AGENTS.md](AGENTS.md) provides
instructions for future coding sessions.

### USB serial access

On this Omarchy machine, install the included rule once so the active desktop
user can access this keyboard's serial port without running the flasher as root:

```sh
~/.local/bin/pkexec-tty bash -c 'install -m 644 /home/javi/Documents/projects/lily58-wireless-zmk-config/scripts/70-lily58-bootloader.rules /etc/udev/rules.d/70-lily58-bootloader.rules && udevadm control --reload-rules && udevadm trigger --action=change --subsystem-match=tty --sysname-match="ttyACM*" && udevadm settle'
```

This opens a password dialog. The rule grants access only to the configured
Lily58 USB serial; it does not add the user to a broad device-access group.
