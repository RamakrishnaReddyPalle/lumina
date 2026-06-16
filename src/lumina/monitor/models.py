# src/monitor/models.py

from dataclasses import dataclass


@dataclass
class Monitor:

    id: str
    name: str
    manufacturer: str

    brightness: int | None = None
    contrast: int | None = None

    backend: object = None