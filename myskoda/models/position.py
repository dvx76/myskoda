"""Models for responses of api/v2/vehicle-status/{vin}/driving-range."""

from dataclasses import dataclass, field
from enum import StrEnum

from mashumaro.mixins.json import DataClassJSONMixin

from .common import Address, Coordinates


class PositionType(StrEnum):
    VEHICLE = "VEHICLE"


@dataclass
class Position:
    address: Address
    gps_coordinates: Coordinates = field(metadata={"alias": "gpsCoordinates"})
    type: PositionType


class ErrorType(StrEnum):
    VEHICLE_IN_MOTION = "VEHICLE_IN_MOTION"


@dataclass
class Error:
    type: ErrorType
    description: str


@dataclass
class Positions(DataClassJSONMixin):
    """Positional information (GPS) for the vehicle and other things."""

    errors: list[Error]
    positions: list[Position]
