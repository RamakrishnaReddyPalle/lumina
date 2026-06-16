# src/monitor/ddcutil_backend.py

import subprocess
import re

from .backend import MonitorBackend


class DDCUtilBackend(MonitorBackend):

    def run(self, command):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        return result.stdout

    def detect_displays(self):
        return self.run(["ddcutil", "detect"])

    def get_brightness(self):
        output = self.run(
            ["ddcutil", "getvcp", "10"]
        )

        match = re.search(
            r"current value =\s*(\d+)",
            output
        )

        return int(match.group(1))

    def set_brightness(self, value):
        self.run(
            ["ddcutil", "setvcp", "10", str(value)]
        )

    def get_contrast(self):
        output = self.run(
            ["ddcutil", "getvcp", "12"]
        )

        match = re.search(
            r"current value =\s*(\d+)",
            output
        )

        return int(match.group(1))

    def set_contrast(self, value):
        self.run(
            ["ddcutil", "setvcp", "12", str(value)]
        )

    def parse_displays(self):
        output = self.detect_displays()

        displays = []

        manufacturer = None
        model = None

        for line in output.splitlines():

            line = line.strip()

            if line.startswith("Mfg id:"):
                manufacturer = (
                    line.split(":")[1]
                    .strip()
                    .split("-")[0]
                    .strip()
                )

            if line.startswith("Model:"):
                model = (
                    line.split(":")[1]
                    .strip()
                )

                displays.append(
                    {
                        "manufacturer": manufacturer,
                        "model": model
                    }
                )

        return displays