# src/lumina/themes/catppuccin/theme.py

from lumina.themes.base import Theme
from lumina.themes.models import ThemeInfo


class CatppuccinTheme(Theme):

    def stylesheet(self):

        return ThemeInfo(

            name="catppuccin",

            border_radius=22,

            blur=False,

            shadow=True,

            stylesheet_text="""

QWidget {

    background: #1E1E2E;

    color: #CDD6F4;

    border-radius: 22px;

    border: 1px solid #313244;

    font-size: 13px;
}

#titleLabel {

    font-size: 22px;

    font-weight: 700;

    color: #F5C2E7;

    padding-bottom: 10px;
}

QLabel {

    background: transparent;
}

QComboBox {

    background: #313244;

    border-radius: 8px;

    padding: 6px;
}

QSlider::groove:horizontal {

    height: 8px;

    border-radius: 4px;

    background: #45475A;
}

QSlider::sub-page:horizontal {

    border-radius: 4px;

    background: #89B4FA;
}

QSlider::handle:horizontal {

    width: 18px;

    border-radius: 9px;

    background: #CDD6F4;

    margin: -5px 0;
}

"""
        )