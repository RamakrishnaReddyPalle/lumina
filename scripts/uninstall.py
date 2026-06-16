# scripts/uninstall.py

from pathlib import Path

FILES = [

    Path.home()
    /
    ".local/share/applications/lumina.desktop",

    Path.home()
    /
    ".local/share/icons/lumina.svg",

    Path.home()
    /
    ".config/systemd/user/lumina.service",

]

for path in FILES:

    if path.exists():

        path.unlink()

        print(
            f"Removed {path}"
        )

print(
    "Lumina uninstall complete"
)