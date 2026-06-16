# apps/widget/theme_preview.py

from pathlib import Path
import sys

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

from window import LuminaWindow

from lumina.themes.manager import ThemeManager


def main():

    app = QApplication(sys.argv)

    tm = ThemeManager()

    for theme_name in tm.available():

        window = LuminaWindow()

        theme = tm.get(theme_name)

        window.setStyleSheet(
            theme.stylesheet().stylesheet_text
        )

        window.setWindowTitle(
            f"Lumina - {theme_name}"
        )

        window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()