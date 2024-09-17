"""Models for responses of api/v2/vehicle-status/{vin}."""

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro.mixins.json import DataClassJSONMixin

from myskoda.models.common import DoorLockedState, OnOffState, OpenState


@dataclass
class Detail:
    bonnet: OpenState
    sunroof: OpenState
    trunk: OpenState


@dataclass
class Overall:
    doors: OpenState
    doors_locked: DoorLockedState = field(metadata={"alias": "doorsLocked"})
    lights: OnOffState
    locked: DoorLockedState
    windows: OpenState


@dataclass
class Status(DataClassJSONMixin):
    """Current status information for a vehicle."""

    car_captured_timestamp: datetime = field(metadata={"alias": "carCapturedTimestamp"})
    detail: Detail
    overall: Overall
