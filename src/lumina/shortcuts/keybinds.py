# src/shortcuts/keybinds.py

from pynput import keyboard

from lumina.daemon.service import LuminaService


class HotkeyManager:

    def __init__(self):

        self.service = LuminaService()

        self.listener = None

    #
    # helpers
    #

    def brightness_up(self):

        monitor = self.service.get_primary_monitor()

        value = min(
            100,
            monitor.brightness + 5
        )

        self.service.set_brightness(
            value
        )

        print(
            f"Brightness -> {value}"
        )

    def brightness_down(self):

        monitor = self.service.get_primary_monitor()

        value = max(
            0,
            monitor.brightness - 5
        )

        self.service.set_brightness(
            value
        )

        print(
            f"Brightness -> {value}"
        )

    def contrast_up(self):

        monitor = self.service.get_primary_monitor()

        value = min(
            100,
            monitor.contrast + 5
        )

        self.service.set_contrast(
            value
        )

        print(
            f"Contrast -> {value}"
        )

    def contrast_down(self):

        monitor = self.service.get_primary_monitor()

        value = max(
            0,
            monitor.contrast - 5
        )

        self.service.set_contrast(
            value
        )

        print(
            f"Contrast -> {value}"
        )

    #
    # listener
    #

    def start(self):

        self.listener = keyboard.GlobalHotKeys({

            "<ctrl>+<alt>+up":
                self.brightness_up,

            "<ctrl>+<alt>+down":
                self.brightness_down,

            "<ctrl>+<alt>+right":
                self.contrast_up,

            "<ctrl>+<alt>+left":
                self.contrast_down,

        })

        self.listener.start()

        print(
            "Lumina hotkeys active"
        )

    def join(self):

        if self.listener:

            self.listener.join()