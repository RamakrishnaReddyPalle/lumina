# apps/widget/window.py

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

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSlider,
    QHBoxLayout,
    QComboBox,
)

from PyQt6.QtCore import (
    Qt,
    QTimer,
)

from lumina.daemon.service import LuminaService

from lumina.themes.manager import (
    ThemeManager
)


class LuminaWindow(QWidget):

    APPLY_DELAY_MS = 120

    def __init__(self):

        super().__init__()

        self.service = LuminaService()

        self.monitor = (
            self.service.get_primary_monitor()
        )

        #
        # Theme Manager
        #

        self.theme_manager = (
            ThemeManager()
        )

        self.current_theme_name = (
            "glass"
        )

        self.apply_theme(
            self.current_theme_name
        )

        #
        # Delayed Writers
        #

        self.brightness_timer = (
            QTimer()
        )

        self.brightness_timer.setSingleShot(
            True
        )

        self.brightness_timer.timeout.connect(
            self.apply_brightness
        )

        self.contrast_timer = (
            QTimer()
        )

        self.contrast_timer.setSingleShot(
            True
        )

        self.contrast_timer.timeout.connect(
            self.apply_contrast
        )

        self.pending_brightness = (
            self.monitor.brightness
        )

        self.pending_contrast = (
            self.monitor.contrast
        )

        #
        # Window
        #

        self.setWindowTitle(
            "Lumina"
        )

        self.setFixedSize(
            420,
            300
        )

        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.setup_ui()

    #
    # Theme Handling
    #

    def apply_theme(
        self,
        theme_name
    ):

        theme = (
            self.theme_manager.get(
                theme_name
            )
        )

        theme_info = (
            theme.stylesheet()
        )

        self.setStyleSheet(
            theme_info.stylesheet_text
        )

        self.current_theme_name = (
            theme_name
        )

    def on_theme_changed(
        self,
        theme_name
    ):

        self.apply_theme(
            theme_name
        )

    #
    # UI
    #

    def setup_ui(self):

        layout = QVBoxLayout()

        #
        # Title
        #

        title = QLabel(
            "Lumina"
        )

        title.setObjectName(
            "titleLabel"
        )

        layout.addWidget(
            title
        )

        #
        # Theme Selector
        #

        theme_row = (
            QHBoxLayout()
        )

        theme_text = QLabel(
            "Theme"
        )

        self.theme_selector = (
            QComboBox()
        )

        self.theme_selector.addItems(
            self.theme_manager.available()
        )

        self.theme_selector.setCurrentText(
            self.current_theme_name
        )

        self.theme_selector.currentTextChanged.connect(
            self.on_theme_changed
        )

        theme_row.addWidget(
            theme_text
        )

        theme_row.addStretch()

        theme_row.addWidget(
            self.theme_selector
        )

        layout.addLayout(
            theme_row
        )

        #
        # Brightness
        #

        brightness_row = (
            QHBoxLayout()
        )

        brightness_text = QLabel(
            "Brightness"
        )

        self.brightness_value = QLabel(
            f"{self.monitor.brightness}%"
        )

        brightness_row.addWidget(
            brightness_text
        )

        brightness_row.addStretch()

        brightness_row.addWidget(
            self.brightness_value
        )

        layout.addLayout(
            brightness_row
        )

        self.brightness_slider = (
            QSlider(
                Qt.Orientation.Horizontal
            )
        )

        self.brightness_slider.setRange(
            0,
            100
        )

        self.brightness_slider.setValue(
            self.monitor.brightness
        )

        self.brightness_slider.valueChanged.connect(
            self.on_brightness_changed
        )

        layout.addWidget(
            self.brightness_slider
        )

        #
        # Contrast
        #

        contrast_row = (
            QHBoxLayout()
        )

        contrast_text = QLabel(
            "Contrast"
        )

        self.contrast_value = QLabel(
            f"{self.monitor.contrast}%"
        )

        contrast_row.addWidget(
            contrast_text
        )

        contrast_row.addStretch()

        contrast_row.addWidget(
            self.contrast_value
        )

        layout.addLayout(
            contrast_row
        )

        self.contrast_slider = (
            QSlider(
                Qt.Orientation.Horizontal
            )
        )

        self.contrast_slider.setRange(
            0,
            100
        )

        self.contrast_slider.setValue(
            self.monitor.contrast
        )

        self.contrast_slider.valueChanged.connect(
            self.on_contrast_changed
        )

        layout.addWidget(
            self.contrast_slider
        )

        self.setLayout(
            layout
        )

    #
    # Brightness
    #

    def on_brightness_changed(
        self,
        value
    ):

        self.brightness_value.setText(
            f"{value}%"
        )

        self.pending_brightness = (
            value
        )

        self.brightness_timer.start(
            self.APPLY_DELAY_MS
        )

    def apply_brightness(
        self
    ):

        self.service.set_brightness(
            self.pending_brightness
        )

    #
    # Contrast
    #

    def on_contrast_changed(
        self,
        value
    ):

        self.contrast_value.setText(
            f"{value}%"
        )

        self.pending_contrast = (
            value
        )

        self.contrast_timer.start(
            self.APPLY_DELAY_MS
        )

    def apply_contrast(
        self
    ):

        self.service.set_contrast(
            self.pending_contrast
        )