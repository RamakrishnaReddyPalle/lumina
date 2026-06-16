# tests/test_backend.py

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from src.lumina.monitor.ddcutil_backend import DDCUtilBackend

backend = DDCUtilBackend()

print(backend.detect_displays())

print(
    "Brightness:",
    backend.get_brightness()
)

print(
    "Contrast:",
    backend.get_contrast()
)