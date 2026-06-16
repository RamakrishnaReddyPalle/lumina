# src/themes/base.py

from abc import ABC
from abc import abstractmethod

from lumina.themes.models import ThemeInfo


class Theme(ABC):

    @abstractmethod
    def stylesheet(self) -> ThemeInfo:
        pass