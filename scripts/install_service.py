# scripts/install_service.py

from pathlib import Path
import shutil
import subprocess

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

SYSTEMD_DIR = (
    Path.home()
    /
    ".config/systemd/user"
)

SYSTEMD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

source = (
    PROJECT_ROOT
    /
    "packaging"
    /
    "lumina.service"
)

target = (
    SYSTEMD_DIR
    /
    "lumina.service"
)

shutil.copy2(
    source,
    target,
)

subprocess.run(
    [
        "systemctl",
        "--user",
        "daemon-reload",
    ]
)

subprocess.run(
    [
        "systemctl",
        "--user",
        "enable",
        "lumina.service",
    ]
)

print(
    "Systemd service installed"
)