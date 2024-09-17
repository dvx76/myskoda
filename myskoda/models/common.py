"""Common models used in multiple responses."""

from dataclasses import dataclass, field
from enum import StrEnum


class OnOffState(StrEnum):
    ON = "ON"
    OFF = "OFF"
    INVALID = "INVALID"


class EnabledState(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ActiveState(StrEnum):
    ACTIVATED = "ACTIVATED"
    DEACTIVATED = "DEACTIVATED"


class OpenState(StrEnum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    UNSUPPORTED = "UNSUPPORTED"


class DoorLockedState(StrEnum):
    LOCKED = "YES"
    UNLOCKED = "NO"


class ChargerLockedState(StrEnum):
    LOCKED = "LOCKED"
    UNLOCKED = "UNLOCKED"


class ConnectionState(StrEnum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"


class Side(StrEnum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


@dataclass
class Coordinates:
    latitude: float
    longitude: float


@dataclass
class Address:
    city: str
    country_code: str = field(metadata={"alias": "countryCode"})
    street: str
    zip_code: str = field(metadata={"alias": "zipCode"})
    house_number: str | None = field(metadata={"alias": "houseNumber"}, default=None)
    country: str | None = None


class Weekday(StrEnum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
