# apps/tray/main.py

# from pathlib import Path
import sys

# import app

# PROJECT_ROOT = (
#     Path(__file__)
#     .resolve()
#     .parent
#     .parent
#     .parent
# )

# sys.path.insert(
#     0,
#     str(PROJECT_ROOT)
# )

from PyQt6.QtWidgets import QApplication

from lumina.widget.window import (
    LuminaWindow
)

from lumina.tray.tray_icon import (
    LuminaTrayIcon
)


def main():

    app = QApplication(
        sys.argv
    )

    app.setQuitOnLastWindowClosed(
        False
    )

    window = LuminaWindow()

    tray = LuminaTrayIcon(
        window
    )

    tray.show()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    main()