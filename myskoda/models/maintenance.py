"""Models for responses of api/v3/vehicle-maintenance/vehicles/{vin} endpoint."""

from dataclasses import dataclass, field
from datetime import datetime, time
from enum import StrEnum

from mashumaro.mixins.json import DataClassJSONMixin

from .common import Address, Coordinates, Weekday


@dataclass
class MaintenanceReport:
    captured_at: datetime = field(metadata={"alias": "capturedAt"})
    inspection_due_in_days: int = field(metadata={"alias": "inspectionDueInDays"})
    mileage_in_km: int = field(metadata={"alias": "mileageInKm"})
    inspection_due_in_km: int | None = field(metadata={"alias": "inspectionDueInKm"}, default=None)
    oil_service_due_in_days: int | None = field(
        metadata={"alias": "oilServiceDueInDays"}, default=None
    )
    oil_service_due_in_km: int | None = field(metadata={"alias": "oilServiceDueInKm"}, default=None)


@dataclass
class Contact:
    email: str
    phone: str
    url: str


@dataclass
class TimeRange:
    start: time = field(metadata={"alias": "from"})
    end: time = field(metadata={"alias": "to"})


@dataclass
class OpeningHoursPeriod:
    opening_times: list[TimeRange] = field(metadata={"alias": "openingTimes"})
    period_end: Weekday = field(metadata={"alias": "periodEnd"})
    period_start: Weekday = field(metadata={"alias": "periodStart"})


class CommunicationChannel(StrEnum):
    email = "EMAIL"


@dataclass
class PredictiveMaintenanceSettings:
    email: str
    phone: str
    preferred_channel: CommunicationChannel = field(metadata={"alias": "preferredChannel"})
    service_activated: bool = field(metadata={"alias": "serviceActivated"})


@dataclass
class PredictiveMaintenance:
    setting: PredictiveMaintenanceSettings


@dataclass
class ServicePartner:
    address: Address
    brand: str
    contact: Contact
    id: str
    location: Coordinates
    name: str
    opening_hours: list[OpeningHoursPeriod] = field(metadata={"alias": "openingHours"})
    partner_number: str = field(metadata={"alias": "partnerNumber"})


@dataclass
class Maintenance(DataClassJSONMixin):
    maintenance_report: MaintenanceReport = field(metadata={"alias": "maintenanceReport"})
    predictive_maintenance: PredictiveMaintenance | None = field(
        metadata={"alias": "predictiveMaintenance"}
    )
    preferred_service_partner: ServicePartner = field(metadata={"alias": "preferredServicePartner"})
