# src/themes/models.py

from dataclasses import dataclass


@dataclass(slots=True)
class ThemeInfo:

    name: str

    stylesheet_text: str

    border_radius: int = 20

    blur: bool = False

    shadow: bool = False

    accent_color: str = "#ffffff"