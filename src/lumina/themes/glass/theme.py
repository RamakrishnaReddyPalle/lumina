# src/themes/glass/theme.py

from lumina.themes.base import Theme

from lumina.themes.models import ThemeInfo


class GlassTheme(Theme):

    def stylesheet(self):

        return ThemeInfo(

            name="glass",

            stylesheet_text="""

QWidget {

    background-color:
        rgba(
            22,
            22,
            22,
            180
        );

    color: white;

    border-radius: 22px;

    border:
        1px solid
        rgba(
            255,
            255,
            255,
            30
        );

    font-size: 13px;
}

#titleLabel {

    font-size: 24px;

    font-weight: 700;

    padding-bottom: 10px;

    color: rgb(
        245,
        245,
        245
    );
}

QSlider::groove:horizontal {

    height: 6px;

    border-radius: 3px;

    background:
        rgba(
            255,
            255,
            255,
            35
        );
}

QSlider::sub-page:horizontal {

    background:
        qlineargradient(
            x1:0,
            y1:0,
            x2:1,
            y2:0,

            stop:0
            rgba(
                130,
                180,
                255,
                255
            ),

            stop:1
            rgba(
                80,
                140,
                255,
                255
            )
        );

    border-radius: 3px;
}

QSlider::handle:horizontal {

    width: 18px;

    border-radius: 9px;

    background: white;

    margin: -6px 0;
}

QLabel {

    background: transparent;
}

"""
        )