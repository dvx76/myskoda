"""Models for responses of api/v2/air-conditioning endpoint."""

from dataclasses import dataclass, field
from datetime import datetime, time
from enum import StrEnum
from typing import Any

from mashumaro.mixins.json import DataClassJSONMixin

from .common import ChargerLockedState, ConnectionState, OnOffState, Side, Weekday


class TemperatureUnit(StrEnum):
    CELSIUS = "CELSIUS"


class TimerMode(StrEnum):
    ONE_OFF = "ONE_OFF"
    RECURRING = "RECURRING"


@dataclass
class Timer:
    enabled: bool
    id: int
    selected_days: list[Weekday] = field(metadata={"alias": "selectedDays"})
    time: time
    type: TimerMode


@dataclass
class SeatHeating:
    front_left: bool = field(metadata={"alias": "frontLeft"})
    front_right: bool = field(metadata={"alias": "frontRight"})


@dataclass
class TargetTemperature:
    temperature_value: float = field(metadata={"alias": "temperatureValue"})
    unit_in_car: TemperatureUnit = field(metadata={"alias": "unitInCar"})


@dataclass
class WindowHeatingState:
    front: OnOffState
    rear: OnOffState
    unspecified: Any


@dataclass
class AirConditioning(DataClassJSONMixin):
    """Information related to air conditioning."""

    air_conditioning_at_unlock: bool = field(metadata={"alias": "airConditioningAtUnlock"})
    car_captured_timestamp: datetime = field(metadata={"alias": "carCapturedTimestamp"})
    charger_connection_state: ConnectionState = field(metadata={"alias": "chargerConnectionState"})
    charger_lock_state: ChargerLockedState = field(metadata={"alias": "chargerLockState"})
    errors: list[Any]
    estimated_date_time_to_reach_target_temperature: datetime = field(
        metadata={"alias": "estimatedDateTimeToReachTargetTemperature"}
    )
    seat_heating_activated: SeatHeating = field(metadata={"alias": "seatHeatingActivated"})
    state: OnOffState
    steering_wheel_position: Side = field(metadata={"alias": "steeringWheelPosition"})
    target_temperature: TargetTemperature | None = field(metadata={"alias": "targetTemperature"})
    timers: list[Timer]
    window_heating_enabled: bool = field(metadata={"alias": "windowHeatingEnabled"})
    window_heating_state: WindowHeatingState = field(metadata={"alias": "windowHeatingState"})
