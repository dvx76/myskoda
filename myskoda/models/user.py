"""User that is using the API."""

from dataclasses import dataclass, field
from datetime import date
from enum import StrEnum

from mashumaro.mixins.json import DataClassJSONMixin


class UserCapabilityId(StrEnum):
    SPIN_MANAGEMENT = "SPIN_MANAGEMENT"
    THIRD_PARTY_OFFERS = "THIRD_PARTY_OFFERS"
    MARKETING_CONSENT = "MARKETING_CONSENT"
    TEST_DRIVE = "TEST_DRIVE"


@dataclass
class UserCapability:
    id: UserCapabilityId


@dataclass
class User(DataClassJSONMixin):
    capabilities: list[UserCapability]
    country: str
    email: str
    first_name: str = field(metadata={"alias": "firstName"})
    id: str
    last_name: str = field(metadata={"alias": "lastName"})
    nickname: str
    phone: str
    preferred_contact_channel: str = field(metadata={"alias": "preferredContactChannel"})
    preferred_language: str = field(metadata={"alias": "preferredLanguage"})
    profile_picture_url: str = field(metadata={"alias": "profilePictureUrl"})
    date_of_birth: date | None = field(metadata={"alias": "dateOfBirth"}, default=None)
