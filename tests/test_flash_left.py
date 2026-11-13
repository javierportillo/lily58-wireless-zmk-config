"""Checks for rejecting firmware that must never be sent to this controller."""

import importlib.machinery
import importlib.util
from pathlib import Path
import struct
import unittest

path = Path(__file__).resolve().parents[1] / "scripts/flash-left"
loader = importlib.machinery.SourceFileLoader("flash_left", str(path))
spec = importlib.util.spec_from_loader(loader.name, loader)
flash_left = importlib.util.module_from_spec(spec)
loader.exec_module(flash_left)


def uf2(**overrides):
    fields = dict(magic0=0x0A324655, magic1=0x9E5D5157, flags=0x2000,
                  address=0x26000, size=256, index=0, total=1, family=0xADA52840)
    fields.update(overrides)
    data = bytearray(512)
    struct.pack_into("<8I", data, 0, *fields.values())
    struct.pack_into("<I", data, 508, 0x0AB16F30)
    return bytes(data)


class FirmwareValidation(unittest.TestCase):
    def test_original_and_clean_artifacts_are_separate(self):
        self.assertEqual(flash_left.firmware_for_keymap("lily58"), flash_left.FIRMWARE)
        clean = flash_left.firmware_for_keymap("clean")
        self.assertEqual(clean, flash_left.FIRMWARE.parent / "clean" / flash_left.FIRMWARE.name)
        self.assertNotEqual(clean, flash_left.FIRMWARE)

    def test_rejects_unknown_keymaps_and_path_traversal(self):
        for name in ("../lily58", "/tmp/keymap", "clean.keymap", "missing-keymap"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                flash_left.firmware_for_keymap(name)

    def test_accepts_nicenano_application(self):
        flash_left.validate_uf2(uf2())

    def test_rejects_bootloader_or_wrong_chip(self):
        for values in ({"address": 0}, {"family": 0xE48BFF56}, {"flags": 0}, {"flags": 0x2001}):
            with self.subTest(values=values), self.assertRaises(ValueError):
                flash_left.validate_uf2(uf2(**values))

    def test_rejects_incomplete_or_malformed_files(self):
        for data in (b"", uf2()[:-1], uf2(total=2), uf2(index=1), uf2(size=0), uf2(magic0=0)):
            with self.subTest(length=len(data)), self.assertRaises(ValueError):
                flash_left.validate_uf2(data)

    def test_ignores_another_usb_controller(self):
        from unittest.mock import patch
        disks = '{"blockdevices":[{"path":"/dev/sdb","tran":"usb","serial":"OTHER","label":"NICENANO","fstype":"vfat"}]}'
        with patch.object(flash_left, "run", return_value=disks):
            self.assertIsNone(flash_left.boot_disk(flash_left.SERIAL))


if __name__ == "__main__":
    unittest.main()
