"""Run inside the pinned Docker toolchain; invoked by build-local."""

import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys

import yaml


def run(*args):
    print("+", " ".join(map(str, args)), flush=True)
    subprocess.run(args, check=True)


def main():
    target = sys.argv[1]
    keymap = sys.argv[2]
    keymap_file = Path("/config") / (keymap + ".keymap")
    if not keymap_file.is_file():
        raise ValueError(f"Keymap not found: {keymap_file}")
    manifest = Path("/config/west.yml").read_bytes()
    manifest_hash = hashlib.sha256(manifest).hexdigest()
    marker = Path(".manifest-hash")
    initialized = Path(".west/config").exists()
    needs_update = (
        not initialized
        or not marker.exists()
        or marker.read_text() != manifest_hash
        or target == "update"
    )
    if needs_update:
        Path("config").mkdir(exist_ok=True)
        Path("config/west.yml").write_bytes(manifest)
        if not initialized:
            run("west", "init", "-l", "config")
        run("west", "update", "--fetch-opt=--filter=tree:0")
        run("west", "zephyr-export")
        marker.write_text(manifest_hash)
    if target == "update":
        return

    # Avoid Zephyr discovering a different workspace through a stale environment.
    os.environ["ZEPHYR_BASE"] = "/workspace/zephyr"
    matrix = yaml.safe_load(Path("/build.yaml").read_text())
    if set(matrix) != {"include"}:
        raise ValueError("Local builds currently require an explicit include-only build.yaml")
    selected = [
        entry for entry in matrix["include"]
        if target == "all" or entry.get("shield", "").endswith("_" + target)
    ]
    if not selected:
        raise ValueError(f"No build targets found for {target}")
    for entry in selected:
        board = entry["board"]
        shield = entry.get("shield", "")
        name = entry.get("artifact-name", f"{shield + '-' if shield else ''}{board}-zmk")
        # Preserve the original paths; isolate every alternative keymap.
        variant = Path() if keymap == "lily58" else Path(keymap)
        build_dir = Path("build") / variant / name
        output = Path("/firmware") / variant / (name + ".uf2")
        output.parent.mkdir(parents=True, exist_ok=True)
        # Remove an old artifact so a failed build cannot leave a misleading UF2.
        output.unlink(missing_ok=True)
        command = ["west", "build", "-p", "auto", "-s", "zmk/app", "-d", str(build_dir), "-b", board]
        if entry.get("snippet"):
            command += ["-S", entry["snippet"]]
        command += ["--", "-DZMK_CONFIG=/config", "-DZMK_EXTRA_MODULES=/local-module"]
        if shield:
            command += [f"-DSHIELD={shield}"]
        # Match the workflow's optional matrix CMake arguments.
        if entry.get("cmake-args"):
            import shlex
            command += shlex.split(entry["cmake-args"])
        # Always set this explicitly: CMake caches KEYMAP_FILE between builds.
        command += [f"-DKEYMAP_FILE={keymap_file}"]
        run(*command)
        shutil.copy2(build_dir / "zephyr/zmk.uf2", output)
        print(f"Firmware ready: {output.relative_to('/')}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)
