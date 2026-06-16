# tests/test_service.py

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.lumina.daemon.service import LuminaService

service = LuminaService()

monitor = service.get_primary_monitor()

print()

print("Monitor:", monitor.name)
print("Brightness:", monitor.brightness)

service.set_brightness(55)

print("Brightness set to 55")

service.refresh()

monitor = service.get_primary_monitor()

print(
    "Current brightness:",
    monitor.brightness
)