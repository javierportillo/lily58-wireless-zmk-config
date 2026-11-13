# Automated USB flashing: implementation and verified behavior

Verified on Javi's physical Lily58 left half on **2026-10-16**, using ZMK v0.3,
Zephyr 3.5, and a nice!nano v2 with Adafruit UF2 bootloader 0.5.0. The new firmware
was installed once with a manual reset, then a complete build/reset/flash/HID
verification cycle succeeded without touching the reset button.

## Normal workflow

Run `./scripts/flash-left` from this repository. It builds the left artifact
using Docker, then performs the rest on the host using Python's standard library,
`lsblk`, `udevadm`, and `udisksctl`. Close ZMK Studio before flashing.

The default controller identity is:

| Property | Value |
| --- | --- |
| USB serial | `23E5F50B0A98298E` |
| Running firmware VID:PID | `1d50:615e` |
| Studio serial port | `/dev/serial/by-id/usb-ZMK_Project_Lily58_23E5F50B0A98298E-if00` |
| Bootloader VID:PID observed | `239a:00b3` |
| Bootloader volume label | `NICENANO` |
| `INFO_UF2.TXT` board ID | `nRF52840-nicenano-v2` |
| Application flash start | `0x26000` |
| UF2 family | nRF52840 (`0xADA52840`) |

The script checks the volume's serial and board ID before writing. Device names
such as `/dev/ttyACM0`, `/dev/sdb`, and input event numbers can change after each
reboot; identify the controller by serial.

## Firmware reset mechanism

Stock ZMK v0.3's Studio protocol has no reboot request. The module in
`module/usb_bootloader.c` adds a 1200-baud trigger to the existing Studio CDC ACM
port. It registers Zephyr's **DTE baud-rate callback**, leaving Studio's UART
interrupt callback available for RPC traffic.

When the baud changes to 1200, delayed work checks the port after 250 ms. It
enters UF2 mode only while USB HID is configured and DTR is low. If DTR stays
high, it checks every 100 ms until the port closes or the baud changes. There
are no periodic checks during normal use. The USB readiness check avoids a
reset caused solely by unplugging the cable.

The reboot uses `sys_reboot(RST_UF2)`, exactly as ZMK v0.3's reset behavior does.
The enabled nRF52 reboot hook writes `0x57` to GPREGRET before restarting.
Do not substitute a newer retention API without updating the ZMK integration.

`module/Kconfig` enables the feature only on the compatible nice!nano v2 USB
central build and selects the required UART line-control and baud callback
options. The right build has no added reset code. The left requires the
`studio-rpc-usb-uart` snippet to expose the watched port.

The host script first selects 115200, asserts DTR, changes to 1200, then drops
DTR and closes the port. The initial baud change ensures a callback even when
a previous session left the port configured at 1200. An open serial port at
1200 alone is not a complete reset request.

## Host access and completion checks

`scripts/70-lily58-bootloader.rules` grants `uaccess` to this specific keyboard's
serial port. It is installed in `/etc/udev/rules.d/` and sorts before systemd's
`73-seat-late.rules`. Normal flashing runs as the active desktop user. See the
README for the one-time privileged installation command.

Before writing, the script validates the UF2 magic, family, block counts,
payload size, and contiguous application addresses. It saves the volume's
`CURRENT.UF2` under `firmware/backups/` with the controller serial and a unique
timestamp. These backups are ignored by Git.

The bootloader can disconnect immediately after receiving the final UF2 block.
On this device, final `fsync()` reported `EIO` while the controller successfully
rebooted. The script permits that expected disconnect only after all source
bytes have been written, then requires the same serial to return with a USB
keyboard HID input device. A partial write or a missing keyboard return fails
the operation. A successful copy alone is insufficient verification.

## Checks performed on hardware

- Built left and right firmware; reset support was enabled only on the left.
- Installed the feature through `--bootstrap` and verified USB keyboard return.
- Opened the serial port at 115200 without resetting the device.
- Held the port open at 1200 for longer than the trigger delay without reset.
- Switched back to 115200 and closed it without reset.
- Ran `./scripts/flash-left` successfully with automated USB bootloader entry,
  backup, firmware transfer, and matching USB keyboard return.

The host validation tests also reject malformed/incomplete UF2s, the wrong chip
family, bootloader-region images, and another controller's bootloader drive.

## Recovery and scope

If serial permissions are missing, check the installed rule and desktop-session
ACL before changing device permissions broadly. If Studio holds the port, close
it. If the running firmware lacks reset support, use
`./scripts/flash-left --bootstrap` and double-tap the left reset button after the
build. The script waits up to 120 seconds for the bootloader by default; use
`--timeout SECONDS` to change this.

For a replacement left controller, update the udev rule and pass its serial
with `--serial SERIAL`. Keep the script's board and UF2 checks appropriate for
that hardware.

The right half still needs its own USB connection and normal flashing procedure.
ZMK's `&bootloader` behavior resets the half containing the pressed binding, so
a binding physically on the right half does not reset the USB-connected left.

For backup input, use the installed Omarchy On-Screen Keyboard plugin. Its
layer-shell panel supports pointer input without claiming keyboard focus, and
its top bar implements mouse-only dragging. The earlier custom floating-window
approach failed on focus and mouse routing and has been retired.
