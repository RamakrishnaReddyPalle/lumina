# src/lumina/themes/aurora/theme.py

from lumina.themes.base import Theme

from lumina.themes.models import ThemeInfo


class AuroraTheme(Theme):

    def stylesheet(self):

        return ThemeInfo(

            name="aurora",

            border_radius=24,

            blur=True,

            shadow=True,

            stylesheet_text="""

QWidget {

    background:
        rgba(
            12,
            16,
            28,
            220
        );

    color:
        rgb(
            240,
            244,
            255
        );

    border-radius: 24px;

    border:
        1px solid
        rgba(
            255,
            255,
            255,
            22
        );

    font-size: 13px;
}

#titleLabel {

    font-size: 24px;

    font-weight: 700;

    color:
        rgb(
            250,
            250,
            255
        );

    padding-bottom: 12px;
}

QLabel {

    background: transparent;
}

QSlider::groove:horizontal {

    height: 8px;

    border-radius: 4px;

    background:
        rgba(
            255,
            255,
            255,
            25
        );
}

QSlider::sub-page:horizontal {

    border-radius: 4px;

    background:
        qlineargradient(
            x1:0,
            y1:0,
            x2:1,
            y2:0,

            stop:0
            #62d0ff,

            stop:1
            #8a6cff
        );
}

QSlider::handle:horizontal {

    width: 18px;

    border-radius: 9px;

    background: white;

    margin: -5px 0;
}

"""
        )