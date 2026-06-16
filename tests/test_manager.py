# tests/test_manager.py

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.lumina.monitor.manager import MonitorManager

manager = MonitorManager()

monitors = manager.discover()

for monitor in monitors:

    print()

    print("ID:", monitor.id)
    print("Manufacturer:", monitor.manufacturer)
    print("Name:", monitor.name)
    print("Brightness:", monitor.brightness)
    print("Contrast:", monitor.contrast)