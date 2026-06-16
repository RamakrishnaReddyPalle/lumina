# src/daemon/service.py

from lumina.monitor.manager import MonitorManager


class LuminaService:

    def __init__(self):

        self.monitor_manager = MonitorManager()

        self.monitors = (
            self.monitor_manager.discover()
        )

    def refresh(self):

        self.monitors = (
            self.monitor_manager.discover(
                force=True
            )
        )

        return self.monitors

    def get_primary_monitor(self):

        if not self.monitors:
            self.refresh()

        return self.monitors[0]

    def get_brightness(self):

        return (
            self.get_primary_monitor()
            .brightness
        )

    def get_contrast(self):

        return (
            self.get_primary_monitor()
            .contrast
        )

    def set_brightness(self, value):

        monitor = self.get_primary_monitor()

        monitor.backend.set_brightness(
            int(value)
        )

        monitor.brightness = int(value)

    def set_contrast(self, value):

        monitor = self.get_primary_monitor()

        monitor.backend.set_contrast(
            int(value)
        )

        monitor.contrast = int(value)