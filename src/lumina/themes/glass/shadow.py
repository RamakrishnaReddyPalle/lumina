# src/themes/glass/shadow.py

from PyQt6.QtWidgets import (
    QGraphicsDropShadowEffect
)

from PyQt6.QtGui import QColor


def create_shadow():

    shadow = QGraphicsDropShadowEffect()

    shadow.setBlurRadius(40)

    shadow.setOffset(0, 8)

    shadow.setColor(
        QColor(
            0,
            0,
            0,
            180
        )
    )

    return shadow