"""Custom types for integration_blueprint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry  # type: ignore
    from homeassistant.loader import Integration

    from .api import ApiClient
    from .coordinator import DataUpdateCoordinator


type ConfigEntry = ConfigEntry[Data]


@dataclass
class Data:
    """Data for the Blueprint integration."""

    client: ApiClient
    coordinator: DataUpdateCoordinator
    integration: Integration
