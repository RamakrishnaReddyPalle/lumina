# apps/widget/main.py

import sys

from PyQt6.QtWidgets import QApplication

from window import LuminaWindow


def main():

    app = QApplication(sys.argv)

    window = LuminaWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()