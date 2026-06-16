# src/monitor/backend.py

from abc import ABC, abstractmethod


class MonitorBackend(ABC):

    @abstractmethod
    def detect_displays(self):
        pass

    @abstractmethod
    def get_brightness(self):
        pass

    @abstractmethod
    def set_brightness(self, value):
        pass

    @abstractmethod
    def get_contrast(self):
        pass

    @abstractmethod
    def set_contrast(self, value):
        pass