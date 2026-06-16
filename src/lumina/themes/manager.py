# src/lumina/themes/manager.py

from lumina.themes.aurora.theme import AuroraTheme
from lumina.themes.minimal.theme import MinimalTheme
from lumina.themes.glass.theme import GlassTheme
from lumina.themes.dracula.theme import DraculaTheme
from lumina.themes.nord.theme import NordTheme
from lumina.themes.catppuccin.theme import CatppuccinTheme


class ThemeManager:

    def __init__(self):

        self.themes = {

            "glass": GlassTheme(),

            "aurora": AuroraTheme(),

            "minimal": MinimalTheme(),

            "dracula": DraculaTheme(),

            "nord": NordTheme(),

            "catppuccin": CatppuccinTheme(),
        }

    def get(
        self,
        name: str
    ):

        return self.themes.get(
            name,
            self.themes["glass"]
        )

    def available(self):

        return sorted(
            self.themes.keys()
        )

    def exists(
        self,
        name: str
    ):

        return name in self.themes

    def theme_info(
        self,
        name: str
    ):

        return self.get(
            name
        ).stylesheet()

    @classmethod
    def load(
        cls,
        name="glass"
    ):

        manager = cls()

        return manager.get(
            name
        )