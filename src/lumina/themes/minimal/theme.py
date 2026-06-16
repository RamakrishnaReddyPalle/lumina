# src/themes/minimal/theme.py

from lumina.themes.base import Theme
from lumina.themes.models import ThemeInfo


class MinimalTheme(Theme):

    def stylesheet(self):

        return ThemeInfo(

            name="minimal",

            border_radius=12,

            blur=False,

            shadow=False,

            stylesheet_text="""

QWidget {

    background: #ffffff;

    color: #111111;

    border-radius: 12px;

    font-size: 13px;
}

#titleLabel {

    font-size: 22px;

    font-weight: 700;

    padding-bottom: 10px;
}

QLabel {

    background: transparent;
}

QComboBox {

    background: #f4f4f4;

    border: 1px solid #dddddd;

    border-radius: 8px;

    padding: 6px;
}

QSlider::groove:horizontal {

    height: 4px;

    background: #dddddd;

    border-radius: 2px;
}

QSlider::sub-page:horizontal {

    background: #111111;

    border-radius: 2px;
}

QSlider::handle:horizontal {

    width: 14px;

    border-radius: 7px;

    background: #111111;

    margin: -5px 0;
}

"""
        )