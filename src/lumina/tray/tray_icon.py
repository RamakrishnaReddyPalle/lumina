# apps/tray/tray_icon.py

# from pathlib import Path
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

from PyQt6.QtWidgets import (
    QSystemTrayIcon,
    QMenu,
    QApplication,
    QStyle,
)

from PyQt6.QtGui import (
    QAction,
)


class LuminaTrayIcon(QSystemTrayIcon):

    def __init__(
        self,
        widget_window,
        parent=None,
    ):

        super().__init__(parent)

        self.widget_window = widget_window

        #
        # Temporary icon
        # Replace later with Lumina SVG
        #

        self.setIcon(
            QApplication.style().standardIcon(
                QStyle.StandardPixmap.SP_ComputerIcon
            )
        )

        self.setToolTip(
            "Lumina Monitor Control"
        )

        #
        # Menu
        #

        self.menu = QMenu()

        self.show_action = QAction(
            "Show / Hide Widget"
        )

        self.show_action.triggered.connect(
            self.toggle_widget
        )

        self.quit_action = QAction(
            "Quit Lumina"
        )

        self.quit_action.triggered.connect(
            self.exit_app
        )

        self.menu.addAction(
            self.show_action
        )

        self.menu.addSeparator()

        self.menu.addAction(
            self.quit_action
        )

        self.setContextMenu(
            self.menu
        )

        self.activated.connect(
            self.tray_clicked
        )

    def tray_clicked(
        self,
        reason,
    ):

        if (
            reason
            ==
            QSystemTrayIcon.ActivationReason.Trigger
        ):

            self.toggle_widget()

    def toggle_widget(
        self
    ):

        if self.widget_window.isVisible():

            self.widget_window.hide()

        else:

            self.widget_window.show()

            self.widget_window.raise_()

            self.widget_window.activateWindow()

    def exit_app(
        self
    ):

        QApplication.quit()