"""Models for responses of api/v1/vehicle-health-report/warning-lights endpoint."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any

from mashumaro.mixins.json import DataClassJSONMixin


class WarningLightCategory(StrEnum):
    ASSISTANCE = "ASSISTANCE"
    COMFORT = "COMFORT"
    BRAKE = "BRAKE"
    ELECTRIC_ENGINE = "ELECTRIC_ENGINE"
    ENGINE = "ENGINE"
    LIGHTING = "LIGHTING"
    TIRE = "TIRE"
    OTHER = "OTHER"


@dataclass
class WarningLight:
    category: WarningLightCategory
    defects: list[Any]


@dataclass
class Health(DataClassJSONMixin):
    """Information about the car's health (currently only mileage)."""

    captured_at: datetime = field(metadata={"alias": "capturedAt"})
    mileage_in_km: int = field(metadata={"alias": "mileageInKm"})
    warning_lights: list[WarningLight] = field(metadata={"alias": "warningLights"})
