"""Models for responses of api/v2/vehicle-status/{vin}."""

from dataclasses import dataclass, field
from datetime import date
from enum import StrEnum

from mashumaro.mixins.json import DataClassJSONMixin


class VehicleType(StrEnum):
    FUEL = "FUEL"


@dataclass
class StatisticsEntry:
    date: date
    average_fuel_consumption: float | None = field(metadata={"alias": "averageFuelConsumption"})
    average_speed_in_kmph: int | None = field(metadata={"alias": "averageSpeedInKmph"})
    mileage_in_km: int | None = field(metadata={"alias": "mileageInKm"})
    travel_time_in_min: int | None = field(metadata={"alias": "travelTimeInMin"})
    trip_ids: list[int] | None = field(metadata={"alias": "tripIds"})


@dataclass
class TripStatistics(DataClassJSONMixin):
    overall_average_fuel_consumption: float = field(
        metadata={"alias": "overallAverageFuelConsumption"}
    )
    overall_average_mileage_in_km: int = field(metadata={"alias": "overallAverageMileageInKm"})
    overall_average_speed_in_kmph: int = field(metadata={"alias": "overallAverageSpeedInKmph"})
    overall_average_travel_time_in_min: int = field(
        metadata={"alias": "overallAverageTravelTimeInMin"}
    )
    overall_mileage_in_km: int = field(metadata={"alias": "overallMileageInKm"})
    overall_travel_time_in_min: int = field(metadata={"alias": "overallTravelTimeInMin"})
    vehicle_type: VehicleType = field(metadata={"alias": "vehicleType"})
    detailed_statistics: list[StatisticsEntry] = field(metadata={"alias": "detailedStatistics"})
