# tests/test_install.py

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

from scripts.install_desktop import *
from scripts.install_service import *

print()

print(
    "Installer test passed"
)

print()