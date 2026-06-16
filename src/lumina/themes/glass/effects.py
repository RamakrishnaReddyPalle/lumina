# src/themes/glass/effects.py

from PyQt6.QtCore import Qt


def apply_glass_window(window):

    window.setAttribute(
        Qt.WidgetAttribute.WA_TranslucentBackground
    )

    window.setWindowFlags(
        Qt.WindowType.FramelessWindowHint
        |
        Qt.WindowType.WindowStaysOnTopHint
    )