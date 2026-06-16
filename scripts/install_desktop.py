# scripts/install_desktop.py

from pathlib import Path
import shutil

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

DESKTOP_DIR = (
    Path.home()
    /
    ".local/share/applications"
)

ICON_DIR = (
    Path.home()
    /
    ".local/share/icons"
)

DESKTOP_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

ICON_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

desktop_source = (
    PROJECT_ROOT
    /
    "packaging"
    /
    "lumina.desktop"
)

desktop_target = (
    DESKTOP_DIR
    /
    "lumina.desktop"
)

icon_source = (
    PROJECT_ROOT
    /
    "assets"
    /
    "icons"
    /
    "app"
    /
    "lumina.svg"
)

icon_target = (
    ICON_DIR
    /
    "lumina.svg"
)

shutil.copy2(
    desktop_source,
    desktop_target,
)

shutil.copy2(
    icon_source,
    icon_target,
)

print(
    "Desktop entry installed"
)