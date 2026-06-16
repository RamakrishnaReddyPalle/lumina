# src/monitor/manager.py

from lumina.monitor.models import Monitor
from lumina.monitor.ddcutil_backend import DDCUtilBackend


class MonitorManager:

    def __init__(self):

        self.backends = [
            DDCUtilBackend()
        ]

        self._cache = None

    def discover(self, force=False):

        if self._cache is not None and not force:
            return self._cache

        monitors = []

        for backend in self.backends:

            displays = backend.parse_displays()

            for index, display in enumerate(displays):

                monitor = Monitor(
                    id=str(index),
                    name=display["model"],
                    manufacturer=display["manufacturer"],
                    brightness=backend.get_brightness(),
                    contrast=backend.get_contrast(),
                    backend=backend
                )

                monitors.append(monitor)

        self._cache = monitors

        return monitors

    def primary_monitor(self):

        monitors = self.discover()

        if not monitors:
            raise RuntimeError(
                "No compatible monitor detected."
            )

        return monitors[0]