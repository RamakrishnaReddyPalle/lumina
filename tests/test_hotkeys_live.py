# tests/test_hotkeys_live.py

from pathlib import Path
import sys
import time

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.lumina.shortcuts.keybinds import (
    HotkeyManager
)

manager = HotkeyManager()

manager.start()

print()
print("Hotkeys Running")
print()
print("Ctrl+Alt+Up")
print("Ctrl+Alt+Down")
print("Ctrl+Alt+Left")
print("Ctrl+Alt+Right")
print()

try:

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    print(
        "\nStopped"
    )