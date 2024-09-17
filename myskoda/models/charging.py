"""Models for responses of api/v1/charging endpoint."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any

from mashumaro.mixins.json import DataClassJSONMixin

from .common import ActiveState, EnabledState


class ChargeMode(StrEnum):
    HOME_STORAGE_CHARGING = "HOME_STORAGE_CHARGING"
    IMMEDIATE_DISCHARGING = "IMMEDIATE_DISCHARGING"
    ONLY_OWN_CURRENT = "ONLY_OWN_CURRENT"
    PREFERRED_CHARGING_TIMES = "PREFERRED_CHARGING_TIMES"
    TIMER_CHARGING_WITH_CLIMATISATION = "TIMER_CHARGING_WITH_CLIMATISATION"
    TIMER = "TIMER"
    MANUAL = "MANUAL"
    OFF = "OFF"


class MaxChargeCurrent(StrEnum):
    MAXIMUM = "MAXIMUM"
    REDUCED = "REDUCED"


class ChargingState(StrEnum):
    READY_FOR_CHARGING = "READY_FOR_CHARGING"
    CONNECT_CABLE = "CONNECT_CABLE"
    CONSERVING = "CONSERVING"
    CHARGING = "CHARGING"


class ChargeType(StrEnum):
    AC = "AC"
    DC = "DC"


class PlugUnlockMode(StrEnum):
    PERMANENT = "PERMANENT"
    ON = "ON"
    OFF = "OFF"


@dataclass
class Settings:
    available_charge_modes: list[ChargeMode] = field(metadata={"alias": "availableChargeModes"})
    battery_support: EnabledState = field(metadata={"alias": "batterySupport"})
    charging_care_mode: ActiveState = field(metadata={"alias": "chargingCareMode"})
    max_charge_current_ac: MaxChargeCurrent = field(metadata={"alias": "maxChargeCurrentAc"})
    preferred_charge_mode: ChargeMode = field(metadata={"alias": "preferredChargeMode"})
    target_state_of_charge_in_percent: int = field(
        metadata={"alias": "targetStateOfChargeInPercent"}
    )
    auto_unlock_plug_when_charged: PlugUnlockMode = field(
        metadata={"alias": "autoUnlockPlugWhenCharged"}
    )


@dataclass
class Battery:
    remaining_cruising_range_in_meters: int = field(
        metadata={"alias": "remainingCruisingRangeInMeters"}
    )
    state_of_charge_in_percent: int = field(metadata={"alias": "stateOfChargeInPercent"})


@dataclass
class Status:
    battery: Battery
    charge_power_in_kw: float | None = field(metadata={"alias": "chargePowerInKw"})
    charging_rate_in_kilometers_per_hour: float = field(
        metadata={"alias": "chargingRateInKilometersPerHour"}
    )
    remaining_time_to_fully_charged_in_minutes: int = field(
        metadata={"alias": "remainingTimeToFullyChargedInMinutes"}
    )
    state: ChargingState
    charge_type: ChargeType | None = field(metadata={"alias": "chargeType"}, default=None)


@dataclass
class Charging(DataClassJSONMixin):
    """Information related to charging an EV."""

    car_captured_timestamp: datetime = field(metadata={"alias": "carCapturedTimestamp"})
    errors: list[Any]
    is_vehicle_in_saved_location: bool = field(metadata={"alias": "isVehicleInSavedLocation"})
    settings: Settings
    status: Status | None
