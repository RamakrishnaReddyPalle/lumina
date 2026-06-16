# src/lumina/themes/dracula/theme.py

from lumina.themes.base import Theme
from lumina.themes.models import ThemeInfo


class DraculaTheme(Theme):

    def stylesheet(self):

        return ThemeInfo(

            name="dracula",

            border_radius=20,

            blur=False,

            shadow=True,

            stylesheet_text="""

QWidget {

    background: #282A36;

    color: #F8F8F2;

    border-radius: 20px;

    border: 1px solid #44475A;

    font-size: 13px;
}

#titleLabel {

    font-size: 22px;

    font-weight: 700;

    color: #BD93F9;

    padding-bottom: 10px;
}

QLabel {

    background: transparent;
}

QComboBox {

    background: #44475A;

    border-radius: 8px;

    padding: 6px;
}

QSlider::groove:horizontal {

    height: 8px;

    border-radius: 4px;

    background: #44475A;
}

QSlider::sub-page:horizontal {

    border-radius: 4px;

    background: #FF79C6;
}

QSlider::handle:horizontal {

    width: 18px;

    border-radius: 9px;

    background: #F8F8F2;

    margin: -5px 0;
}

"""
        )