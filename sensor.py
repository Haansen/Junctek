from datetime import timedelta
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator, UpdateFailed,
)
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .bluetooth import JuntekConnector

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    connector = JuntekConnector()
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="juntek",
        update_method=connector.async_fetch_data,
        update_interval=timedelta(seconds=30),
    )
    await coordinator.async_refresh()
    sensors = []
    for key, desc in connector.get_descriptors().items():
        sensors.append(JuntekSensor(coordinator, key, desc))
    async_add_entities(sensors, True)

class JuntekSensor(SensorEntity):
    def __init__(self, coordinator, key, description):
        self.coordinator = coordinator
        self.entity_key = key
        self._attr_name = f"Juntek {description}"
        self._attr_unique_id = f"juntek_{key}"
        self._attr_native_unit_of_measurement = self.get_unit(key)

    @property
    def native_value(self):
        return self.coordinator.data.get(self.entity_key)

    def get_unit(self, key):
        units = {
            "voltage": "V",
            "current": "A",
            "capacity": "Ah",
            "battery_percent": "%",
        }
        return units.get(key)
