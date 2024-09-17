"""Models for responses of api/v2/garage/vehicles/{vin}."""

from dataclasses import dataclass, field
from datetime import date
from enum import StrEnum

from mashumaro.mixins.json import DataClassJSONMixin


class CapabilityId(StrEnum):
    AIR_CONDITIONING = "AIR_CONDITIONING"
    AIR_CONDITIONING_SAVE_AND_ACTIVATE = "AIR_CONDITIONING_SAVE_AND_ACTIVATE"
    AIR_CONDITIONING_SMART_SETTINGS = "AIR_CONDITIONING_SMART_SETTINGS"
    AIR_CONDITIONING_TIMERS = "AIR_CONDITIONING_TIMERS"
    AUTOMATION = "AUTOMATION"
    BATTERY_CHARGING_CARE = "BATTERY_CHARGING_CARE"
    BATTERY_SUPPORT = "BATTERY_SUPPORT"
    CARE_AND_INSURANCE = "CARE_AND_INSURANCE"
    CHARGE_MODE_SELECTION = "CHARGE_MODE_SELECTION"
    CHARGING = "CHARGING"
    CHARGING_MEB = "CHARGING_MEB"
    CHARGING_PROFILES = "CHARGING_PROFILES"
    CHARGING_STATIONS = "CHARGING_STATIONS"
    CUBIC = "CUBIC"
    DEALER_APPOINTMENT = "DEALER_APPOINTMENT"
    DESTINATIONS = "DESTINATIONS"
    DESTINATION_IMPORT = "DESTINATION_IMPORT"
    DESTINATION_IMPORT_UPGRADABLE = "DESTINATION_IMPORT_UPGRADABLE"
    DIGICERT = "DIGICERT"
    EMERGENCY_CALLING = "EMERGENCY_CALLING"
    EV_ROUTE_PLANNING = "EV_ROUTE_PLANNING"
    EXTENDED_CHARGING_SETTINGS = "EXTENDED_CHARGING_SETTINGS"
    FUEL_STATUS = "FUEL_STATUS"
    GEO_FENCE = "GEO_FENCE"
    GUEST_USER_MANAGEMENT = "GUEST_USER_MANAGEMENT"
    HONK_AND_FLASH = "HONK_AND_FLASH"
    ICE_VEHICLE_RTS = "ICE_VEHICLE_RTS"
    MAP_UPDATE = "MAP_UPDATE"
    MEASUREMENTS = "MEASUREMENTS"
    MISUSE_PROTECTION = "MISUSE_PROTECTION"
    NEWS = "NEWS"
    ONLINE_SPEECH_GPS = "ONLINE_SPEECH_GPS"
    PARKING_INFORMATION = "PARKING_INFORMATION"
    PARKING_POSITION = "PARKING_POSITION"
    PAY_TO_FUEL = "PAY_TO_FUEL"
    PAY_TO_PARK = "PAY_TO_PARK"
    PLUG_AND_CHARGE = "PLUG_AND_CHARGE"
    POI_SEARCH = "POI_SEARCH"
    POWERPASS_TARIFFS = "POWERPASS_TARIFFS"
    ROADSIDE_ASSISTANT = "ROADSIDE_ASSISTANT"
    ROUTE_IMPORT = "ROUTE_IMPORT"
    ROUTE_PLANNING_5_CHARGERS = "ROUTE_PLANNING_5_CHARGERS"
    ROUTING = "ROUTING"
    SERVICE_PARTNER = "SERVICE_PARTNER"
    SPEED_ALERT = "SPEED_ALERT"
    STATE = "STATE"
    SUBSCRIPTIONS = "SUBSCRIPTIONS"
    TRAFFIC_INFORMATION = "TRAFFIC_INFORMATION"
    TRIP_STATISTICS = "TRIP_STATISTICS"
    VEHICLE_HEALTH_INSPECTION = "VEHICLE_HEALTH_INSPECTION"
    VEHICLE_HEALTH_WARNINGS = "VEHICLE_HEALTH_WARNINGS"
    VEHICLE_HEALTH_WARNINGS_WITH_WAKE_UP = "VEHICLE_HEALTH_WARNINGS_WITH_WAKE_UP"
    VEHICLE_SERVICES_BACKUPS = "VEHICLE_SERVICES_BACKUPS"
    VEHICLE_WAKE_UP = "VEHICLE_WAKE_UP"
    VEHICLE_WAKE_UP_TRIGGER = "VEHICLE_WAKE_UP_TRIGGER"
    WARNING_LIGHTS = "WARNING_LIGHTS"
    WEB_RADIO = "WEB_RADIO"
    WINDOW_HEATING = "WINDOW_HEATING"


class CapabilityStatus(StrEnum):
    DEACTIVATED_BY_ACTIVE_VEHICLE_USER = "DEACTIVATED_BY_ACTIVE_VEHICLE_USER"
    INSUFFICIENT_BATTERY_LEVEL = "INSUFFICIENT_BATTERY_LEVEL"


@dataclass
class Capability:
    id: CapabilityId
    statuses: list[CapabilityStatus]


@dataclass
class Capabilities:
    capabilities: list[Capability]


@dataclass
class Battery:
    capacity: int = field(metadata={"alias": "capacityInKWh"})


class BodyType(StrEnum):
    SUV = "SUV"
    COMBI = "Combi"


class VehicleState(StrEnum):
    ACTIVATED = "ACTIVATED"


@dataclass
class Engine:
    power: int = field(metadata={"alias": "powerInKW"})
    type: str
    capacity_in_liters: float | None = field(metadata={"alias": "capacityInLiters"}, default=None)


@dataclass
class Gearbox:
    type: str


@dataclass
class Specification:
    battery: Battery | None
    body: BodyType
    engine: Engine
    manufacturing_date: date = field(metadata={"alias": "manufacturingDate"})
    max_charging_power: int = field(metadata={"alias": "maxChargingPowerInKW"})
    model: str
    model_year: str = field(metadata={"alias": "modelYear"})
    system_code: str = field(metadata={"alias": "systemCode"})
    system_model_id: str = field(metadata={"alias": "systemModelId"})
    title: str
    trim_level: str = field(metadata={"alias": "trimLevel"})


@dataclass
class ServicePartner:
    id: str = field(metadata={"alias": "servicePartnerId"})


class ErrorType(StrEnum):
    MISSING_RENDER = "MISSING_RENDER"


@dataclass
class Error:
    description: str
    type: ErrorType


@dataclass
class Info(DataClassJSONMixin):
    """Basic vehicle information."""

    software_version: str = field(metadata={"alias": "softwareVersion"})
    state: VehicleState
    specification: Specification
    vin: str
    name: str
    device_platform: str = field(metadata={"alias": "devicePlatform"})
    service_partner: ServicePartner = field(metadata={"alias": "servicePartner"})
    workshop_mode_enabled: bool = field(metadata={"alias": "workshopModeEnabled"})
    capabilities: Capabilities
    license_plate: str = field(metadata={"alias": "licensePlate"})
    errors: list[Error] | None = field(default_factory=list)
