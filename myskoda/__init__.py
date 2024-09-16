"""A library for interacting with the MySkoda APIs."""

from .authorization import (
    AuthorizationError,
    IDKAuthorizationCode,
    IDKCredentials,
    IDKSession,
    idk_authorize,
)
from .models import air_conditioning, charging, common, health, info, position, status
from .rest_api import RestApi, Vehicle

__all__ = [
    "AuthorizationError",
    "IDKAuthorizationCode",
    "IDKCredentials",
    "IDKSession",
    "idk_authorize",
    "air_conditioning",
    "charging",
    "common",
    "health",
    "info",
    "position",
    "status",
    "RestApi",
    "Vehicle",
]
