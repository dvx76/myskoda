"""Models for responses of api/v2/vehicle-status/{vin}/driving-range endpoint."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum

from mashumaro.mixins.json import DataClassJSONMixin


class EngineType(StrEnum):
    DIESEL = "diesel"
    ELECTRIC = "electric"


@dataclass
class EngineRange:
    engine_type: EngineType = field(metadata={"alias": "engineType"})
    remaining_range_in_km: int = field(metadata={"alias": "remainingRangeInKm"})
    current_fuel_level_in_percent: int | None = field(
        metadata={"alias": "currentFuelLevelInPercent"}, default=None
    )
    current_so_c_in_percent: int | None = field(
        metadata={"alias": "currentSoCInPercent"}, default=None
    )


@dataclass
class DrivingRange(DataClassJSONMixin):
    car_captured_timestamp: datetime = field(metadata={"alias": "carCapturedTimestamp"})
    car_type: EngineType = field(metadata={"alias": "carType"})
    primary_engine_range: EngineRange = field(metadata={"alias": "primaryEngineRange"})
    total_range_in_km: int = field(metadata={"alias": "totalRangeInKm"})
