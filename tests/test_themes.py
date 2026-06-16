# tests/test_themes.py

from pathlib import Path
import sys

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

from src.lumina.themes.manager import (
    ThemeManager
)

tm = ThemeManager()

for name in tm.available():

    print(name)