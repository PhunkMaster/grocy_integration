"""Data update coordinator for Grocy."""
from __future__ import annotations

import logging
from logging import Logger
from typing import Any, Dict, List

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from pygrocytoo.grocy import Grocy

from . import GrocyData

from .const import (
    CONF_API_KEY,
    CONF_PORT,
    CONF_URL,
    CONF_VERIFY_SSL,
    DOMAIN,
    SCAN_INTERVAL,
)

from .helpers import extract_base_url_and_path

_LOGGER: Logger = logging.getLogger(__name__)


class GrocyDataUpdateCoordinator(DataUpdateCoordinator[Dict[str, Any]]):
    """Grocy data update coordinator."""
    grocy_data: GrocyData
    grocy_api: Grocy
    available_entities: list[str]

    def __init__(
            self,
            hass: HomeAssistant,
    ) -> None:
        """Initialize Grocy data update coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

        url: str = self.config_entry.data[CONF_URL]
        api_key: str = self.config_entry.data[CONF_API_KEY]
        port: int = self.config_entry.data[CONF_PORT]
        verify_ssl: bool = self.config_entry.data[CONF_VERIFY_SSL]

        base_url: str
        path: str
        (base_url, path) = extract_base_url_and_path(url)

        self.grocy_api = Grocy(
            base_url, api_key, path=path, port=port, verify_ssl=verify_ssl
        )
        self.grocy_data = GrocyData(hass, self.grocy_api)

        self.available_entities: List[str] = []
        self.entities: List[Entity] = []

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data."""
        data: dict[str, Any] = {}

        for entity in self.entities:
            if not entity.enabled:
                _LOGGER.debug("Entity %s is disabled.", entity.entity_id)
                continue

            try:
                data[
                    entity.entity_description.key
                ] = await self.grocy_data.async_update_data(
                    entity.entity_description.key
                )
            except Exception as error:  # pylint: disable=broad-except
                raise UpdateFailed(f"Update failed: {error}") from error

        return data
