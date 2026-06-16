# src/lumina/themes/nord/theme.py

from lumina.themes.base import Theme
from lumina.themes.models import ThemeInfo


class NordTheme(Theme):

    def stylesheet(self):

        return ThemeInfo(

            name="nord",

            border_radius=18,

            blur=False,

            shadow=True,

            stylesheet_text="""

QWidget {

    background: #2E3440;

    color: #ECEFF4;

    border-radius: 18px;

    border: 1px solid #4C566A;

    font-size: 13px;
}

#titleLabel {

    font-size: 22px;

    font-weight: 700;

    color: #88C0D0;

    padding-bottom: 10px;
}

QLabel {

    background: transparent;
}

QComboBox {

    background: #3B4252;

    border: 1px solid #4C566A;

    border-radius: 8px;

    padding: 6px;
}

QSlider::groove:horizontal {

    height: 8px;

    border-radius: 4px;

    background: #4C566A;
}

QSlider::sub-page:horizontal {

    border-radius: 4px;

    background: #88C0D0;
}

QSlider::handle:horizontal {

    width: 18px;

    border-radius: 9px;

    background: #ECEFF4;

    margin: -5px 0;
}

"""
        )